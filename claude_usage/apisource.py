"""Server-side usage from the https://api.anthropic.com/api/oauth/usage endpoint,
with an OAuth Bearer token (see oauth.py).

The response returns a `limits` array, each item:
    {kind, group, percent, resets_at (ISO|null), scope:{model,surface}}
We pick the 5-hour window and the weekly limit out of it and load them into the
Metrics structure the widget uses.
"""

from __future__ import annotations

import threading
import time
from datetime import datetime
from typing import Callable, List, Optional, Tuple

from . import oauth
from .i18n import tr
from .datasource import (FIVE_HOURS_MS, WEEK_MS, DetailRow, ExtraUsage, Metrics, ProfileInfo,
                         Sample)


# Polling cadence. The usage endpoint rate-limits: at one request per minute every
# second call came back as 429. So we poll at BASE_INTERVAL, stretch the interval
# when the server pushes back, and shrink it again while it answers.
BASE_INTERVAL = 120.0
MAX_INTERVAL = 600.0
MANUAL_RETRIES = 5              # "Refresh now" keeps trying until it gets an answer
AUTO_RETRIES = 1
RETRY_DELAYS = (8.0, 15.0, 25.0, 40.0, 60.0)


PROFILE_EVERY_S = 6 * 3600      # the plan rarely changes - ask seldom
PROFILE_RETRY_S = 30 * 60
PLAN_NAMES = {"claude_pro": "pro", "claude_max": "max", "claude_team": "team",
              "claude_enterprise": "enterprise"}
# legacy top-level windows of the usage response -> (row id, category, label)
LEGACY_ROWS = (
    ("seven_day_opus", "model:Opus", "model", "Opus"),
    ("seven_day_sonnet", "model:Sonnet", "model", "Sonnet"),
    ("seven_day_oauth_apps", "surface:oauth_apps", "surface", "@oauth_apps"),
    ("cinder_cove", "kind:cinder_cove", "other", "Cinder Cove"),
)


def _dbg(msg: str) -> None:
    """Diagnostic log of API queries (%APPDATA%\\ClaudeUsageMonitor\\api.log)."""
    try:
        import os
        from datetime import datetime as _dt

        from .settings import config_dir

        path = os.path.join(config_dir(), "api.log")
        if os.path.exists(path) and os.path.getsize(path) > 80_000:
            with open(path, "r", encoding="utf-8", errors="replace") as fh:
                tail = fh.readlines()[-200:]
            with open(path, "w", encoding="utf-8") as fh:
                fh.writelines(tail)
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(f"{_dt.now():%H:%M:%S}  {msg}\n")
    except OSError:
        pass


HISTORY_FILE = "api-history.json"   # the claude.ai series survives restarts and self-updates
HISTORY_MAX = 4000
HISTORY_SAVE_EVERY_S = 60.0


def _history_path() -> str:
    import os

    from .settings import config_dir

    return os.path.join(config_dir(), HISTORY_FILE)


def _load_history() -> List[Sample]:
    """The saved claude.ai samples of the last week ([] when there are none or the file is damaged)."""
    import json

    try:
        with open(_history_path(), "r", encoding="utf-8") as fh:
            raw = json.load(fh)
        cutoff = int(time.time() * 1000) - WEEK_MS
        rows = [Sample(t=int(r[0]), org="", fh=float(r[1]), sd=float(r[2]), mo=float(r[3]))
                for r in raw.get("samples", []) if int(r[0]) >= cutoff]
    except (OSError, ValueError, TypeError, IndexError, AttributeError):
        return []
    rows.sort(key=lambda s: s.t)
    return rows[-HISTORY_MAX:]


def _backfill_from_desktop(series: List[Sample]) -> List[Sample]:
    """Fill the gaps of the last week from Claude Desktop's own log (plan-usage-history.json, a sample every
    ~15 min with the same server figures). Only where no claude.ai sample of ours lies within 5 minutes, and only
    when that log holds a single account - with several we cannot tell which one is signed in here."""
    import json

    from .datasource import default_data_path

    try:
        with open(default_data_path(), "r", encoding="utf-8") as fh:
            raw = json.load(fh).get("samples", [])
        if len({str(r.get("org", "")) for r in raw}) != 1:
            return series
        cutoff = int(time.time() * 1000) - WEEK_MS
        extra = [Sample(t=int(r["t"]), org="", fh=float((r.get("u") or {}).get("fh", 0) or 0),
                        sd=float((r.get("u") or {}).get("sd", 0) or 0)) for r in raw if int(r["t"]) >= cutoff]
    except (OSError, ValueError, TypeError, KeyError, AttributeError):
        return series
    have = sorted(s.t for s in series)
    near = 5 * 60 * 1000

    def covered(t: int) -> bool:
        import bisect

        i = bisect.bisect_left(have, t)
        return any(0 <= j < len(have) and abs(have[j] - t) <= near for j in (i - 1, i))

    added = [s for s in extra if not covered(s.t)]
    if not added:
        return series
    _dbg(f"history: {len(added)} sample(s) filled in from the Claude Desktop log")
    merged = sorted(series + added, key=lambda s: s.t)
    return merged[-HISTORY_MAX:]


def _save_history(series: List[Sample]) -> None:
    """Atomic write (temp file + replace), so a crash never leaves half a file behind."""
    import json
    import os

    path = _history_path()
    tmp = path + ".tmp"
    try:
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump({"v": 1, "samples": [[s.t, s.fh, s.sd, s.mo] for s in series]}, fh, separators=(",", ":"))
        os.replace(tmp, path)
    except OSError as e:
        _dbg(f"history save failed: {e}")


def _parse_iso_ms(value) -> Optional[int]:
    if isinstance(value, (int, float)):
        return int(value * 1000)
    if not isinstance(value, str) or not value.strip():
        return None
    txt = value.strip().replace("Z", "+00:00")
    try:
        return int(datetime.fromisoformat(txt).timestamp() * 1000)
    except ValueError:
        return None


class ApiReader:
    """UsageReader-compatible interface: read() -> Metrics. The network runs on a
    background thread, read() never blocks; refreshes the token on expiry."""

    def __init__(self, tokens: Optional[dict] = None,
                 on_tokens_changed: Optional[Callable[[dict], None]] = None):
        self._tokens = tokens or {}
        self._on_tokens_changed = on_tokens_changed
        self._lock = threading.Lock()
        self._raw: Optional[dict] = None
        self._fetched_at: Optional[int] = None
        self._error = ""
        self._inflight = False
        self._force_pending = False   # "Refresh now" arrived while a fetch was running
        self._last_fetch = 0.0        # time of the last network attempt (s)
        self._interval = BASE_INTERVAL   # adaptive: grows on 429, shrinks on success
        self._retry_at: Optional[float] = None   # a failed fetch is retried at this time
        self._retries_left = 0
        self._retry_no = 0
        self._last_status = 0
        self._series: List[Sample] = _backfill_from_desktop(_load_history())
        self._saved_at = 0.0          # last history write (s)
        self.model_filter = "Fable"   # which model-scoped weekly limit to surface
        self._limits_logged = False
        self._profile: Optional[ProfileInfo] = None
        self._profile_next = 0.0      # when to ask the profile endpoint again

    # ------------------------------------------------------------------ token

    def set_tokens(self, tokens: dict) -> None:
        with self._lock:
            self._tokens = tokens or {}
            self._raw = None
            self._error = ""
            self._profile = None      # another account may have signed in
            self._profile_next = 0.0

    def has_tokens(self) -> bool:
        with self._lock:
            return bool(self._tokens.get("access_token"))

    @property
    def last_error(self) -> str:
        """The most recent fetch error ("" when the last fetch succeeded)."""
        with self._lock:
            return self._error

    @property
    def busy(self) -> bool:
        """A network request is running (or queued) right now."""
        with self._lock:
            return self._inflight or self._force_pending

    @property
    def retry_in(self) -> Optional[float]:
        """Seconds until the automatic retry of a failed fetch (None = none planned)."""
        with self._lock:
            if self._retry_at is None:
                return None
            return max(0.0, self._retry_at - time.time())

    @property
    def rate_limited(self) -> bool:
        with self._lock:
            return self._last_status == 429

    def _valid_access_token(self) -> Tuple[str, str]:
        """Returns a valid access token (refreshing if needed). (token, error)."""
        with self._lock:
            tokens = dict(self._tokens)
        access = tokens.get("access_token", "")
        exp = tokens.get("expires_at")
        need_refresh = not access or (isinstance(exp, (int, float)) and exp <= time.time())
        if need_refresh and tokens.get("refresh_token"):
            new, err = oauth.refresh(tokens["refresh_token"])
            if new and new.get("access_token"):
                with self._lock:
                    self._tokens = new
                if self._on_tokens_changed:
                    self._on_tokens_changed(new)
                return new["access_token"], ""
            return "", err or tr("err.session_expired")
        if not access:
            return "", tr("err.not_signed_in")
        return access, ""

    # ------------------------------------------------------------------ network

    def refresh_async(self, force: bool = False) -> None:
        now = time.time()
        with self._lock:
            if self._inflight:
                if force:
                    # Do not drop a manual refresh: run it again as soon as the
                    # in-flight fetch finishes (this was why "Refresh now"
                    # sometimes appeared to do nothing).
                    self._force_pending = True
                return
            retry_due = self._retry_at is not None and now >= self._retry_at
            if not force and not retry_due and (now - self._last_fetch) < self._interval:
                return          # too soon - do not burden the server
            if not retry_due or force:
                # a fresh attempt (not the retry of a failed one): new retry budget
                self._retries_left = MANUAL_RETRIES if force else AUTO_RETRIES
                self._retry_no = 0
            self._retry_at = None
            self._inflight = True
            self._last_fetch = now
        threading.Thread(target=self._worker, daemon=True).start()

    def force_refresh(self) -> None:
        """Immediate network query (called by "Refresh now")."""
        self.refresh_async(force=True)

    def _worker(self) -> None:
        # CRITICAL: whatever happens, _inflight is reset at the end - otherwise the
        # flag stays true and no new query ever starts again.
        try:
            access, err = self._valid_access_token()
            if not access:
                with self._lock:
                    self._error = err
                _dbg(f"nincs access token: {err}")
                return

            raw, status, ferr, retry_after = oauth.fetch_usage(access)
            with self._lock:
                refresh_token = self._tokens.get("refresh_token")
            if status == 401 and refresh_token:
                _dbg("401 -> token refresh and retry")
                new, rerr = oauth.refresh(refresh_token)
                if new and new.get("access_token"):
                    with self._lock:
                        self._tokens = new
                    if self._on_tokens_changed:
                        self._on_tokens_changed(new)
                    raw, status, ferr, retry_after = oauth.fetch_usage(new["access_token"])
                else:
                    _dbg(f"token refresh failed: {rerr}")

            now = int(time.time() * 1000)
            with self._lock:
                self._last_status = status
                if raw is not None and status == 200:
                    self._raw = raw
                    self._fetched_at = now
                    self._error = ""
                    self._retries_left = 0
                    self._interval = max(BASE_INTERVAL, self._interval * 0.75)
                    self._append_series(raw, now)
                    _dbg("OK 200")
                    if not self._limits_logged:
                        # once per run: which limits the server reports (no secrets)
                        self._limits_logged = True
                        # structure only (field NAMES, never values): shows which other
                        # figures the server offers for this account
                        try:
                            shape = []
                            for key, val in raw.items():
                                if isinstance(val, dict):
                                    shape.append(f"{key}{{{','.join(sorted(map(str, val)))}}}")
                                elif isinstance(val, list):
                                    inner = sorted({str(k) for it in val if isinstance(it, dict) for k in it})
                                    shape.append(f"{key}[{len(val)}]{{{','.join(inner)}}}")
                                else:
                                    shape.append(f"{key}:{type(val).__name__}")
                            _dbg("response shape: " + " | ".join(shape)[:900])
                            for key, val in raw.items():
                                if isinstance(val, dict) and key != "extra_usage" and \
                                        isinstance(val.get("utilization"), (int, float)):
                                    _dbg("window %s: utilization=%s used=%s limit=%s resets_at=%s" % (
                                        key, val.get("utilization"), val.get("used_dollars"),
                                        val.get("limit_dollars"), val.get("resets_at")))
                        except Exception:  # noqa: BLE001 - diagnostics must never break the fetch
                            pass
                        for lim in (raw.get("limits") or []):
                            if isinstance(lim, dict):
                                sc = lim.get("scope") or {}
                                _dbg("limit kind=%s group=%s model=%s percent=%s" % (
                                    lim.get("kind"), lim.get("group"),
                                    (sc.get("model") or {}).get("display_name"),
                                    lim.get("percent")))
                elif status in (401, 403):
                    self._error = tr("err.session_expired_nl")
                    _dbg(f"{status} auth hiba")
                else:
                    # 429 / network hiccup / 5xx: keep the old data, back off, retry by itself
                    if status == 429:
                        self._interval = min(MAX_INTERVAL, self._interval * 1.5)
                        self._error = tr("err.rate_limited")
                    else:
                        self._error = ferr or tr("err.query_http", status)
                    if self._retries_left > 0:
                        self._retries_left -= 1
                        delay = RETRY_DELAYS[min(self._retry_no, len(RETRY_DELAYS) - 1)]
                        self._retry_no += 1
                        if retry_after:
                            delay = max(delay, min(float(retry_after), 300.0))
                        self._retry_at = time.time() + delay
                        _dbg(f"status={status} -> retry in {delay:.0f}s "
                             f"(left {self._retries_left}, interval {self._interval:.0f}s)")
                    else:
                        _dbg(f"status={status} -> giving up until the next poll "
                             f"(interval {self._interval:.0f}s) {str(ferr)[:80]!r}")
            if status == 200:
                self._maybe_fetch_profile()
        except Exception as e:  # noqa: BLE001 - the thread must never die silently
            import traceback
            with self._lock:
                self._error = tr("err.unexpected", e)
            _dbg("EXCEPTION:\n" + traceback.format_exc())
        finally:
            with self._lock:
                self._inflight = False
                again = self._force_pending
                self._force_pending = False
            if again:
                self.refresh_async(force=True)

    def _maybe_fetch_profile(self) -> None:
        """Plan badge data. A separate, rare request - failure only means no badge."""
        now = time.time()
        with self._lock:
            if now < self._profile_next:
                return
            self._profile_next = now + PROFILE_RETRY_S
            access = self._tokens.get("access_token", "")
        if not access:
            return
        raw, status = oauth.fetch_profile(access)
        if not isinstance(raw, dict):
            _dbg(f"profile: status={status}")
            return
        org = raw.get("organization") or {}
        acc = raw.get("account") or {}
        org_type = str(org.get("organization_type") or "")
        info = ProfileInfo(
            plan=PLAN_NAMES.get(org_type, ""),
            tier=str(org.get("rate_limit_tier") or ""),
            name=str(acc.get("display_name") or acc.get("full_name") or ""),
            org_type=org_type,
            billing_type=str(org.get("billing_type") or ""),
            has_extra_usage=org.get("has_extra_usage_enabled")
            if isinstance(org.get("has_extra_usage_enabled"), bool) else None,
            created_at=str(acc.get("created_at") or ""),
        )
        with self._lock:
            self._profile = info
            self._profile_next = now + PROFILE_EVERY_S
        # the plan is not a secret, the person is: never log name or e-mail
        _dbg(f"profile: plan={info.plan or '?'} tier={info.tier or '?'} org_type={org_type or '?'}")

    # ------------------------------------------------------------------ analysis

    @staticmethod
    def _pick_rows(raw: dict) -> List[DetailRow]:
        """Every limit besides the 5-hour window and the overall weekly one:
        model-scoped and surface-scoped windows, plus kinds we do not know yet."""
        rows: List[DetailRow] = []
        seen = set()

        def add(row: DetailRow) -> None:
            key = row.id.lower()
            if key not in seen:
                seen.add(key)
                rows.append(row)

        limits = raw.get("limits") if isinstance(raw, dict) else None
        for lim in limits if isinstance(limits, list) else []:
            if not isinstance(lim, dict):
                continue
            kind, group = str(lim.get("kind", "")), str(lim.get("group", ""))
            if kind == "five_hour" or group == "session":
                continue
            if lim.get("is_active") is False:
                continue                        # present in the answer, but not in force for this account
            scope = lim.get("scope") if isinstance(lim.get("scope"), dict) else {}
            model = (scope.get("model") or {}).get("display_name") if isinstance(scope.get("model"), dict) else None
            surface = scope.get("surface")
            if isinstance(surface, dict):
                surface = surface.get("display_name") or surface.get("name") or surface.get("id")
            pct = lim.get("percent")
            pct = float(pct) if isinstance(pct, (int, float)) else 0.0
            reset = _parse_iso_ms(lim.get("resets_at"))
            if model:
                add(DetailRow(f"model:{model}", "model", str(model), pct, reset))
            elif surface:
                add(DetailRow(f"surface:{surface}", "surface", str(surface), pct, reset))
            elif kind in ("seven_day", "weekly_all") or group == "weekly_all":
                continue                        # the overall weekly window has its own gauge
            else:
                label = kind.replace("_", " ").strip().title() or group
                add(DetailRow(f"kind:{kind or group}", "other", label, pct, reset))

        has_surface = any(r.category == "surface" for r in rows)
        for key, rid, category, label in LEGACY_ROWS:
            win = raw.get(key) if isinstance(raw, dict) else None
            if not isinstance(win, dict) or not isinstance(win.get("utilization"), (int, float)):
                continue
            if category == "surface" and has_surface:
                continue                        # limits[] already describes the surfaces
            add(DetailRow(rid, category, label, float(win["utilization"]),
                          _parse_iso_ms(win.get("resets_at"))))

        # any other filled top-level window (server code names such as "nimbus_quill")
        known = {"five_hour", "seven_day", "extra_usage", "limits"} | {k for k, *_ in LEGACY_ROWS}
        taken = [(r.value, r.reset_at) for r in rows]
        for base in ("five_hour", "seven_day"):
            win = raw.get(base) if isinstance(raw, dict) else None
            if isinstance(win, dict) and isinstance(win.get("utilization"), (int, float)):
                taken.append((float(win["utilization"]), _parse_iso_ms(win.get("resets_at"))))
        for lim in limits if isinstance(limits, list) else []:
            if isinstance(lim, dict) and isinstance(lim.get("percent"), (int, float)):
                taken.append((float(lim["percent"]), _parse_iso_ms(lim.get("resets_at"))))

        def repeats(value: float, reset: Optional[int]) -> bool:
            for v, rs in taken:
                same_reset = (rs is None and reset is None) or \
                             (rs is not None and reset is not None and abs(rs - reset) < 120_000)
                if abs(v - value) < 0.75 and same_reset:
                    return True
            return False

        for key, win in (raw.items() if isinstance(raw, dict) else []):
            if key in known or not isinstance(win, dict):
                continue
            util = win.get("utilization")
            if not isinstance(util, (int, float)):
                continue
            reset = _parse_iso_ms(win.get("resets_at"))
            if float(util) <= 0.0 and reset is None:
                continue                        # placeholder of a window that is not in use
            if repeats(float(util), reset):
                continue                        # the same window under a second name
            add(DetailRow(f"kind:{key}", "other", key.replace("_", " ").title(), float(util), reset))
        return rows

    @staticmethod
    def _pick_extra(raw: dict) -> Optional[ExtraUsage]:
        ex = raw.get("extra_usage") if isinstance(raw, dict) else None
        if not isinstance(ex, dict):
            return None

        def money(value) -> Optional[float]:
            # the API counts in minor units (cents)
            return round(float(value) / 100.0, 2) if isinstance(value, (int, float)) else None

        limit, used = money(ex.get("monthly_limit")), money(ex.get("used_credits"))
        util = ex.get("utilization")
        if not isinstance(util, (int, float)):
            util = (used / limit * 100.0) if (limit and used is not None) else None
        return ExtraUsage(enabled=bool(ex.get("is_enabled")), monthly_limit=limit, used=used,
                          utilization=float(util) if util is not None else None,
                          currency=str(ex.get("currency") or "USD").upper(),
                          disabled_reason=str(ex.get("disabled_reason") or ""))

    @staticmethod
    def _pick(raw: dict) -> Tuple[Tuple[float, Optional[int]], Tuple[float, Optional[int]]]:
        """(five_hour, weekly) -> ((pct, reset_ms), (pct, reset_ms))"""
        limits = raw.get("limits") if isinstance(raw, dict) else None
        if not isinstance(limits, list):
            return (0.0, None), (0.0, None)

        five = (0.0, None)
        weekly = (0.0, None)
        weekly_scoped = (0.0, None)  # fallback if there is no model-less weekly

        for lim in limits:
            if not isinstance(lim, dict):
                continue
            kind = str(lim.get("kind", ""))
            group = str(lim.get("group", ""))
            pct = lim.get("percent")
            pct = float(pct) if isinstance(pct, (int, float)) else 0.0
            reset = _parse_iso_ms(lim.get("resets_at"))
            has_model = bool((lim.get("scope") or {}).get("model"))

            if kind == "five_hour" or group == "session":
                five = (pct, reset)
            elif kind == "seven_day" or group in ("weekly_all", "weekly"):
                if not has_model:
                    weekly = (pct, reset)
                else:
                    weekly_scoped = max(weekly_scoped, (pct, reset), key=lambda t: t[0])

        if weekly == (0.0, None) and weekly_scoped != (0.0, None):
            weekly = weekly_scoped
        return five, weekly

    @staticmethod
    def _pick_model(raw: dict, filt: str) -> Tuple[float, Optional[int], str]:
        """The model-scoped weekly limit whose name/kind matches `filt`
        (e.g. "Fable"); falls back to the first model-scoped weekly.
        Returns (pct, reset_ms, display_name) - name is "" when not found."""
        limits = raw.get("limits") if isinstance(raw, dict) else None
        if not isinstance(limits, list):
            return 0.0, None, ""
        filt = (filt or "").strip().lower()
        first: Optional[Tuple[float, Optional[int], str]] = None
        for lim in limits:
            if not isinstance(lim, dict):
                continue
            kind = str(lim.get("kind", ""))
            group = str(lim.get("group", ""))
            scope = lim.get("scope") or {}
            model = (scope.get("model") or {}).get("display_name")
            if not model:
                continue
            is_weekly = kind.startswith("seven_day") or group in ("weekly", "weekly_all", "weekly_model")
            if not is_weekly:
                continue
            pct = lim.get("percent")
            pct = float(pct) if isinstance(pct, (int, float)) else 0.0
            reset = _parse_iso_ms(lim.get("resets_at"))
            entry = (pct, reset, str(model))
            if filt and (filt in str(model).lower() or filt in kind.lower()):
                return entry
            if first is None:
                first = entry
        return first if first is not None else (0.0, None, "")

    def _append_series(self, raw: dict, now: int) -> None:
        (fh, _), (sd, _) = self._pick(raw)
        mo, _, _ = self._pick_model(raw, self.model_filter)
        if self._series and now - self._series[-1].t < 1000:
            return
        self._series.append(Sample(t=now, org="", fh=fh, sd=sd, mo=mo))
        cutoff = now - WEEK_MS
        self._series = [s for s in self._series if s.t >= cutoff][-HISTORY_MAX:]
        if time.time() - self._saved_at >= HISTORY_SAVE_EVERY_S:
            self._saved_at = time.time()
            _save_history(self._series)

    def _spark(self, attr: str, span_ms: int, points: int) -> List[float]:
        now = int(time.time() * 1000)
        vals = [getattr(s, attr) for s in self._series if s.t >= now - span_ms]
        if len(vals) <= points:
            return vals
        step = len(vals) / points
        return [vals[min(len(vals) - 1, int(i * step))] for i in range(points)]

    @staticmethod
    def _burn(series: List[Sample], attr: str, now_ms: int, window_ms: int) -> float:
        pts = [(s.t, getattr(s, attr)) for s in series if s.t >= now_ms - window_ms]
        if len(pts) < 2:
            return 0.0
        dt_h = (pts[-1][0] - pts[0][0]) / 3_600_000.0
        if dt_h <= 0:
            return 0.0
        return max(0.0, (pts[-1][1] - pts[0][1]) / dt_h)

    # ------------------------------------------------------------------ public

    def organizations(self) -> List[str]:
        return []

    def series(self, org: Optional[str] = None, since_ms: Optional[int] = None) -> List[Sample]:
        with self._lock:
            rows = list(self._series)
        if since_ms is not None:
            rows = [s for s in rows if s.t >= since_ms]
        return rows

    def read(self, org: Optional[str] = None) -> Metrics:
        self.refresh_async()
        with self._lock:
            raw = self._raw
            fetched = self._fetched_at
            err = self._error
            series = list(self._series)
            profile = self._profile

        m = Metrics()
        m.profile = profile
        if raw is None:
            m.error = err or tr("err.loading")
            return m

        (fh_val, fh_reset), (sd_val, sd_reset) = self._pick(raw)
        now = int(time.time() * 1000)
        m.ok = True
        m.updated_at = fetched
        m.sample_count = len(series)

        g = m.five_hour
        g.value = fh_val
        g.reset_at = fh_reset
        g.reset_certain = fh_reset is not None
        g.burn = self._burn(series, "fh", now, 60 * 60 * 1000) or \
            self._burn(series, "fh", now, 3 * 60 * 60 * 1000)
        if g.burn > 0.2 and g.value < 100:
            g.eta_ms = int(g.remaining / g.burn * 3_600_000)
        g.spark = self._spark("fh", FIVE_HOURS_MS, 48)

        w = m.weekly
        w.value = sd_val
        w.reset_at = sd_reset
        w.reset_certain = sd_reset is not None
        w.burn = self._burn(series, "sd", now, 6 * 60 * 60 * 1000)
        if w.burn > 0.05 and w.value < 100:
            w.eta_ms = int(w.remaining / w.burn * 3_600_000)
        if sd_reset is not None:
            elapsed = 1.0 - max(0, sd_reset - now) / WEEK_MS
            ideal = max(0.0, min(1.0, elapsed)) * 100.0
            w.pace = w.value - ideal
        w.spark = self._spark("sd", WEEK_MS, 64)

        m.rows = self._pick_rows(raw)
        m.extra = self._pick_extra(raw)

        # model-scoped weekly limit (e.g. Fable) - only when the server reports it
        mo_val, mo_reset, mo_name = self._pick_model(raw, self.model_filter)
        if mo_name:
            mg = m.model
            m.model_name = mo_name
            mg.value = mo_val
            mg.reset_at = mo_reset
            mg.reset_certain = mo_reset is not None
            mg.burn = self._burn(series, "mo", now, 6 * 60 * 60 * 1000)
            if mg.burn > 0.05 and mg.value < 100:
                mg.eta_ms = int(mg.remaining / mg.burn * 3_600_000)
            if mo_reset is not None:
                elapsed = 1.0 - max(0, mo_reset - now) / WEEK_MS
                ideal = max(0.0, min(1.0, elapsed)) * 100.0
                mg.pace = mg.value - ideal
            mg.spark = self._spark("mo", WEEK_MS, 64)

        return m
