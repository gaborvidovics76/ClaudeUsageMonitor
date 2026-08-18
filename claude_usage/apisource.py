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
from .datasource import FIVE_HOURS_MS, WEEK_MS, Metrics, Sample


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
        self._last_fetch = 0.0        # time of the last network attempt (s)
        self._min_interval = 60.0     # do not call the server more often than this
        self._series: List[Sample] = []

    # ------------------------------------------------------------------ token

    def set_tokens(self, tokens: dict) -> None:
        with self._lock:
            self._tokens = tokens or {}
            self._raw = None
            self._error = ""

    def has_tokens(self) -> bool:
        with self._lock:
            return bool(self._tokens.get("access_token"))

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
                return
            if not force and (now - self._last_fetch) < self._min_interval:
                return          # too soon - do not burden the server
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

            raw, status, ferr = oauth.fetch_usage(access)
            if status == 401 and self._tokens.get("refresh_token"):
                _dbg("401 -> token refresh and retry")
                new, rerr = oauth.refresh(self._tokens["refresh_token"])
                if new and new.get("access_token"):
                    with self._lock:
                        self._tokens = new
                    if self._on_tokens_changed:
                        self._on_tokens_changed(new)
                    raw, status, ferr = oauth.fetch_usage(new["access_token"])
                else:
                    _dbg(f"token refresh failed: {rerr}")

            now = int(time.time() * 1000)
            with self._lock:
                if raw is not None and status == 200:
                    self._raw = raw
                    self._fetched_at = now
                    self._error = ""
                    self._append_series(raw, now)
                    _dbg("OK 200")
                elif status in (401, 403):
                    self._error = tr("err.session_expired_nl")
                    _dbg(f"{status} auth hiba")
                else:
                    self._error = ferr or tr("err.query_http", status)
                    _dbg(f"hiba: status={status} ferr={ferr}")
        except Exception as e:  # noqa: BLE001 - the thread must never die silently
            import traceback
            with self._lock:
                self._error = tr("err.unexpected", e)
            _dbg("EXCEPTION:\n" + traceback.format_exc())
        finally:
            with self._lock:
                self._inflight = False

    # ------------------------------------------------------------------ analysis

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

    def _append_series(self, raw: dict, now: int) -> None:
        (fh, _), (sd, _) = self._pick(raw)
        if self._series and now - self._series[-1].t < 1000:
            return
        self._series.append(Sample(t=now, org="", fh=fh, sd=sd))
        cutoff = now - WEEK_MS
        self._series = [s for s in self._series if s.t >= cutoff][-4000:]

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

        m = Metrics()
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

        return m
