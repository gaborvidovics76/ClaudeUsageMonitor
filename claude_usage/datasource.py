"""Reading and evaluating the plan-usage-history.json written by Claude Desktop.

File format (v2):
    {"version":2,"samples":[{"t":<epoch ms>,"org":"<uuid>","u":{"fh":<0-100>,"sd":<0-100>}}, ...]}

    fh = utilization of the 5-hour window, in percent
    sd = utilization of the 7-day (weekly) limit, in percent
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

FIVE_HOURS_MS = 5 * 3600 * 1000
WEEK_MS = 7 * 24 * 3600 * 1000


def default_data_path() -> str:
    appdata = os.environ.get("APPDATA") or os.path.expanduser("~\\AppData\\Roaming")
    return os.path.join(appdata, "Claude", "plan-usage-history.json")


@dataclass
class Sample:
    t: int
    org: str
    fh: float
    sd: float


@dataclass
class Gauge:
    """The current state of one limit (5-hour or weekly)."""

    value: float = 0.0
    reset_at: Optional[int] = None      # epoch ms
    reset_certain: bool = False
    burn: float = 0.0                   # %/hour
    eta_ms: Optional[int] = None        # time until it would reach 100%
    pace: Optional[float] = None        # actual - ideal consumption (%), weekly only
    spark: List[float] = field(default_factory=list)

    @property
    def remaining(self) -> float:
        return max(0.0, 100.0 - self.value)

    @property
    def reset_in_ms(self) -> Optional[int]:
        if self.reset_at is None:
            return None
        return max(0, self.reset_at - int(time.time() * 1000))


@dataclass
class Metrics:
    ok: bool = False
    error: str = ""
    org: str = ""
    orgs: List[str] = field(default_factory=list)
    updated_at: Optional[int] = None
    sample_count: int = 0
    five_hour: Gauge = field(default_factory=Gauge)
    weekly: Gauge = field(default_factory=Gauge)

    @property
    def age_s(self) -> Optional[float]:
        if self.updated_at is None:
            return None
        return max(0.0, time.time() - self.updated_at / 1000.0)

    @property
    def stale(self) -> bool:
        a = self.age_s
        return a is None or a > 15 * 60


def fmt_delta(ms: Optional[int]) -> str:
    from .i18n import tr

    if ms is None:
        return "?"
    s = max(0, ms // 1000)
    d, s = divmod(s, 86400)
    h, s = divmod(s, 3600)
    m = s // 60
    if d:
        return tr("time.dh", d, h)
    if h:
        return tr("time.hm", h, m)
    return tr("time.m", m)


def fmt_age(seconds: Optional[float]) -> str:
    from .i18n import tr

    if seconds is None:
        return tr("time.none")
    if seconds < 90:
        return tr("time.sec", int(seconds))
    m = int(seconds // 60)
    if m < 90:
        return tr("time.min", m)
    h = m // 60
    if h < 48:
        return tr("time.hour", h)
    return tr("time.day", h // 24)


class UsageReader:
    """File-based reader. Re-parses only when the file changed."""

    def __init__(self, path: Optional[str] = None):
        self.path = path or default_data_path()
        self._stamp: Optional[Tuple[float, int]] = None
        self._samples: List[Sample] = []
        self._orgs: List[str] = []
        self._error = ""

    # ------------------------------------------------------------------ io

    def _load(self) -> None:
        try:
            st = os.stat(self.path)
        except OSError:
            self._error = tr("err.file_not_found")
            self._samples = []
            self._stamp = None
            return

        stamp = (st.st_mtime, st.st_size)
        if stamp == self._stamp and self._samples:
            return

        try:
            with open(self.path, "r", encoding="utf-8") as fh:
                raw = json.load(fh)
        except (OSError, ValueError):
            # The file may be mid-write - keep the previous good state.
            if not self._samples:
                self._error = tr("err.file_unreadable")
            return

        samples: List[Sample] = []
        for item in raw.get("samples", []):
            try:
                u = item.get("u") or {}
                samples.append(
                    Sample(
                        t=int(item["t"]),
                        org=str(item.get("org", "")),
                        fh=float(u.get("fh", 0) or 0),
                        sd=float(u.get("sd", 0) or 0),
                    )
                )
            except (KeyError, TypeError, ValueError):
                continue

        samples.sort(key=lambda s: s.t)
        self._samples = samples
        self._stamp = stamp
        self._error = "" if samples else tr("err.file_empty")

        seen: Dict[str, int] = {}
        for s in samples:
            seen[s.org] = s.t
        self._orgs = [o for o, _ in sorted(seen.items(), key=lambda kv: -kv[1]) if o]

    # -------------------------------------------------------------- analysis

    @staticmethod
    def _window_start(rows: List[Tuple[int, float]], span_ms: int) -> Tuple[Optional[int], bool]:
        """Find the start of the current window. (start_ms, is_certain)"""
        if not rows or rows[-1][1] <= 0:
            return None, False

        i = len(rows) - 1
        while i > 0:
            t_cur, v_cur = rows[i]
            t_prev, v_prev = rows[i - 1]
            if t_cur - t_prev > span_ms:
                # Long sampling gap: the window start is uncertain.
                return t_cur, False
            if v_prev <= 0 < v_cur:
                return t_cur, True          # started from zero -> exact start
            if v_prev - v_cur > 5:
                return t_cur, True          # significant drop -> new window
            i -= 1
        return rows[0][0], False

    @staticmethod
    def _burn(rows: List[Tuple[int, float]], now_ms: int, window_ms: int) -> float:
        """Consumption in %/hour over the last `window_ms`."""
        pts = [r for r in rows if r[0] >= now_ms - window_ms]
        if len(pts) < 2:
            return 0.0
        dt_h = (pts[-1][0] - pts[0][0]) / 3_600_000.0
        if dt_h <= 0:
            return 0.0
        dv = pts[-1][1] - pts[0][1]
        return max(0.0, dv / dt_h)

    @staticmethod
    def _spark(rows: List[Tuple[int, float]], now_ms: int, span_ms: int, points: int) -> List[float]:
        pts = [v for t, v in rows if t >= now_ms - span_ms]
        if len(pts) <= points:
            return pts
        step = len(pts) / points
        return [pts[min(len(pts) - 1, int(i * step))] for i in range(points)]

    # --------------------------------------------------------------- public

    def organizations(self) -> List[str]:
        self._load()
        return list(self._orgs)

    def series(self, org: Optional[str] = None, since_ms: Optional[int] = None) -> List[Sample]:
        """Raw samples for the history window."""
        self._load()
        org = org if org in self._orgs else (self._orgs[0] if self._orgs else "")
        rows = [s for s in self._samples if not org or s.org == org]
        if since_ms is not None:
            rows = [s for s in rows if s.t >= since_ms]
        return rows

    def read(self, org: Optional[str] = None) -> Metrics:
        self._load()
        m = Metrics(orgs=list(self._orgs))

        if not self._samples:
            m.error = self._error or tr("err.no_usage_data")
            return m

        org = org if org in self._orgs else (self._orgs[0] if self._orgs else "")
        rows = [s for s in self._samples if not org or s.org == org]
        if not rows:
            m.error = tr("err.no_data_profile")
            return m

        last = rows[-1]
        now_ms = int(time.time() * 1000)
        m.ok = True
        m.org = org
        m.updated_at = last.t
        m.sample_count = len(rows)

        fh_rows = [(s.t, s.fh) for s in rows]
        sd_rows = [(s.t, s.sd) for s in rows]

        # --- 5-hour window
        g = m.five_hour
        g.value = last.fh
        start, certain = self._window_start(fh_rows, FIVE_HOURS_MS)
        if start is not None:
            g.reset_at = start + FIVE_HOURS_MS
            g.reset_certain = certain
        g.burn = self._burn(fh_rows, now_ms, 60 * 60 * 1000) or self._burn(fh_rows, now_ms, 3 * 60 * 60 * 1000)
        if g.burn > 0.2 and g.value < 100:
            g.eta_ms = int(g.remaining / g.burn * 3_600_000)
        g.spark = self._spark(fh_rows, now_ms, FIVE_HOURS_MS, 48)

        # --- weekly limit
        w = m.weekly
        w.value = last.sd
        wstart, wcertain = self._window_start(sd_rows, WEEK_MS)
        if wstart is not None:
            w.reset_at = wstart + WEEK_MS
            w.reset_certain = wcertain
        w.burn = self._burn(sd_rows, now_ms, 6 * 60 * 60 * 1000)
        if w.burn > 0.05 and w.value < 100:
            w.eta_ms = int(w.remaining / w.burn * 3_600_000)
        if w.reset_at is not None:
            elapsed = 1.0 - max(0, w.reset_at - now_ms) / WEEK_MS
            ideal = max(0.0, min(1.0, elapsed)) * 100.0
            w.pace = w.value - ideal
        w.spark = self._spark(sd_rows, now_ms, WEEK_MS, 64)

        return m
