"""Színtémák. Minden szín (r, g, b, a) tuple."""

from __future__ import annotations

from typing import Dict, Tuple

from PySide6.QtGui import QColor

RGBA = Tuple[int, int, int, int]


def qc(c: RGBA) -> QColor:
    return QColor(c[0], c[1], c[2], c[3])


def mix(a: RGBA, b: RGBA, t: float) -> RGBA:
    t = max(0.0, min(1.0, t))
    return (
        int(a[0] + (b[0] - a[0]) * t),
        int(a[1] + (b[1] - a[1]) * t),
        int(a[2] + (b[2] - a[2]) * t),
        int(a[3] + (b[3] - a[3]) * t),
    )


def with_alpha(c: RGBA, a: int) -> RGBA:
    return (c[0], c[1], c[2], max(0, min(255, a)))


def hex_to_rgba(value: str, alpha: int = 255) -> RGBA:
    v = value.strip().lstrip("#")
    if len(v) == 3:
        v = "".join(ch * 2 for ch in v)
    if len(v) != 6:
        raise ValueError(value)
    return (int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16), alpha)


def rgba_to_hex(c: RGBA) -> str:
    return "#%02X%02X%02X" % (c[0], c[1], c[2])


THEMES: Dict[str, Dict[str, object]] = {
    "midnight": {
        "label": "Éjkék üveg",
        "dark": True,
        "bg": (20, 24, 36, 246),
        "bg2": (30, 36, 55, 246),
        "border": (255, 255, 255, 38),
        "text": (238, 242, 252, 255),
        "dim": (150, 160, 186, 255),
        "track": (255, 255, 255, 26),
        "accent": (120, 162, 255, 255),
        "ok": (74, 214, 160, 255),
        "warn": (255, 190, 92, 255),
        "danger": (255, 106, 106, 255),
        "shadow": (0, 0, 0, 150),
    },
    "claude": {
        "label": "Claude (meleg sötét)",
        "dark": True,
        "bg": (28, 24, 22, 248),
        "bg2": (45, 38, 34, 248),
        "border": (255, 226, 210, 34),
        "text": (245, 238, 232, 255),
        "dim": (176, 160, 148, 255),
        "track": (255, 255, 255, 26),
        "accent": (217, 119, 87, 255),
        "ok": (122, 190, 140, 255),
        "warn": (233, 178, 88, 255),
        "danger": (226, 92, 76, 255),
        "shadow": (0, 0, 0, 150),
    },
    "graphite": {
        "label": "Grafit",
        "dark": True,
        "bg": (24, 25, 27, 248),
        "bg2": (38, 40, 43, 248),
        "border": (255, 255, 255, 30),
        "text": (236, 237, 240, 255),
        "dim": (150, 153, 160, 255),
        "track": (255, 255, 255, 24),
        "accent": (168, 176, 190, 255),
        "ok": (108, 200, 150, 255),
        "warn": (232, 184, 96, 255),
        "danger": (232, 100, 96, 255),
        "shadow": (0, 0, 0, 150),
    },
    "neon": {
        "label": "Neon",
        "dark": True,
        "bg": (11, 13, 20, 246),
        "bg2": (20, 24, 38, 246),
        "border": (108, 240, 255, 60),
        "text": (233, 250, 255, 255),
        "dim": (128, 168, 186, 255),
        "track": (108, 240, 255, 28),
        "accent": (94, 234, 255, 255),
        "ok": (86, 240, 190, 255),
        "warn": (255, 214, 102, 255),
        "danger": (255, 88, 132, 255),
        "shadow": (0, 220, 255, 90),
    },
    "paper": {
        "label": "Világos papír",
        "dark": False,
        "bg": (252, 252, 253, 250),
        "bg2": (240, 241, 245, 250),
        "border": (16, 20, 32, 34),
        "text": (26, 30, 42, 255),
        "dim": (112, 120, 138, 255),
        "track": (16, 20, 32, 26),
        "accent": (58, 110, 232, 255),
        "ok": (32, 158, 108, 255),
        "warn": (198, 128, 20, 255),
        "danger": (206, 62, 62, 255),
        "shadow": (16, 24, 48, 60),
    },
    "postit": {
        "label": "Post-it sárga",
        "dark": False,
        "bg": (255, 228, 120, 248),
        "bg2": (255, 214, 92, 248),
        "border": (140, 106, 20, 46),
        "text": (56, 42, 12, 255),
        "dim": (122, 96, 32, 255),
        "track": (90, 68, 16, 40),
        "accent": (196, 92, 40, 255),
        "ok": (42, 128, 72, 255),
        "warn": (176, 108, 16, 255),
        "danger": (188, 48, 40, 255),
        "shadow": (90, 70, 20, 90),
    },
}

DEFAULT_THEME = "midnight"


class Palette:
    """Egy témából + egyedi kiemelőszínből összeállított paletta."""

    def __init__(self, name: str, accent_hex: str = ""):
        data = THEMES.get(name) or THEMES[DEFAULT_THEME]
        self.name = name if name in THEMES else DEFAULT_THEME
        self.label = str(data["label"])
        self.dark = bool(data["dark"])
        for key in ("bg", "bg2", "border", "text", "dim", "track", "accent", "ok", "warn", "danger", "shadow"):
            setattr(self, key, data[key])
        if accent_hex:
            try:
                self.accent = hex_to_rgba(accent_hex)
            except ValueError:
                pass

    def status(self, value: float, warn: float, danger: float) -> RGBA:
        if value >= danger:
            return self.danger
        if value >= warn:
            return self.warn
        return self.ok

    def gauge_colors(self, value: float, warn: float, danger: float) -> Tuple[RGBA, RGBA]:
        """A sáv színátmenetének két vége."""
        end = self.status(value, warn, danger)
        start = mix(self.accent, end, 0.55)
        return start, end
