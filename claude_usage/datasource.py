"""A Claude Desktop által írt plan-usage-history.json olvasása és kiértékelése.

A fájl formátuma (v2):
    {"version":2,"samples":[{"t":<epoch ms>,"org":"<uuid>","u":{"fh":<0-100>,"sd":<0-100>}}, ...]}

    fh = az 5 órás ablak kihasználtsága százalékban
    sd = a 7 napos (heti) keret kihasználtsága százalékban
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
    """Egy keret (5 órás vagy heti) aktuális állapota."""

    value: float = 0.0
    reset_at: Optional[int] = None      # epoch ms
    reset_certain: bool = False
    burn: float = 0.0                   # %/óra
    eta_ms: Optional[int] = None        # mennyi idő múlva érné el a 100%-ot
    pace: Optional[float] = None        # tényleges - ideális fogyás (%), csak a hetinél
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
    """Fájl-alapú olvasó. Csak akkor parse-ol újra, ha változott a fájl."""

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
            self._error = "A használati fájl nem található.\nFut a Claude Desktop?"
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
            # Épp írás alatt lehet a fájl – marad az előző jó állapot.
            if not self._samples:
                self._error = "A használati fájl jelenleg nem olvasható."
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
        self._error = "" if samples else "A használati fájl üres."

        seen: Dict[str, int] = {}
        for s in samples:
            seen[s.org] = s.t
        self._orgs = [o for o, _ in sorted(seen.items(), key=lambda kv: -kv[1]) if o]

    # -------------------------------------------------------------- elemzés

    @staticmethod
    def _window_start(rows: List[Tuple[int, float]], span_ms: int) -> Tuple[Optional[int], bool]:
        """Megkeresi az aktuális keret kezdetét. (kezdet_ms, biztos-e)"""
        if not rows or rows[-1][1] <= 0:
            return None, False

        i = len(rows) - 1
        while i > 0:
            t_cur, v_cur = rows[i]
            t_prev, v_prev = rows[i - 1]
            if t_cur - t_prev > span_ms:
                # Hosszú mintavételi szünet: a keret kezdete bizonytalan.
                return t_cur, False
            if v_prev <= 0 < v_cur:
                return t_cur, True          # nulláról indult -> pontos kezdet
            if v_prev - v_cur > 5:
                return t_cur, True          # jelentős visszaesés -> új keret
            i -= 1
        return rows[0][0], False

    @staticmethod
    def _burn(rows: List[Tuple[int, float]], now_ms: int, window_ms: int) -> float:
        """Fogyás %/óra az elmúlt `window_ms` alatt."""
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

    # --------------------------------------------------------------- publikus

    def organizations(self) -> List[str]:
        self._load()
        return list(self._orgs)

    def series(self, org: Optional[str] = None, since_ms: Optional[int] = None) -> List[Sample]:
        """Nyers minták az előzmény-ablakhoz."""
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
            m.error = self._error or "Nincs használati adat."
            return m

        org = org if org in self._orgs else (self._orgs[0] if self._orgs else "")
        rows = [s for s in self._samples if not org or s.org == org]
        if not rows:
            m.error = "Ehhez a profilhoz nincs adat."
            return m

        last = rows[-1]
        now_ms = int(time.time() * 1000)
        m.ok = True
        m.org = org
        m.updated_at = last.t
        m.sample_count = len(rows)

        fh_rows = [(s.t, s.fh) for s in rows]
        sd_rows = [(s.t, s.sd) for s in rows]

        # --- 5 órás ablak
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

        # --- heti keret
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
