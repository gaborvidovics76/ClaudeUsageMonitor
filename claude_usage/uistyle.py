"""Shared widget styling that plain QSS cannot do on its own.

Checkboxes: the platform's default indicator is almost invisible on the dark dialogs, and once QSS styles
the indicator Qt stops drawing the tick itself. So the indicator images are drawn here (QPainter, no
image files shipped) into the settings folder, and the QSS points at them. If that folder cannot be
written, the native look stays - never a missing checkbox.
"""

from __future__ import annotations

import os
from typing import Dict

from .settings import config_dir

ACCENT = "#D97757"           # the Claude orange of the app icon
_VERSION = "2"               # bump when the drawings change (old files are redrawn)
_SIZE = 36                   # drawn at 2x, shown at 18 px


def _draw(path: str, checked: bool, state: str) -> None:
    from PySide6.QtCore import QPointF, QRectF, Qt
    from PySide6.QtGui import QColor, QImage, QPainter, QPainterPath, QPen

    img = QImage(_SIZE, _SIZE, QImage.Format.Format_ARGB32_Premultiplied)
    img.fill(Qt.GlobalColor.transparent)
    p = QPainter(img)
    p.setRenderHint(QPainter.RenderHint.Antialiasing, True)
    box = QRectF(2.5, 2.5, _SIZE - 5, _SIZE - 5)
    dim = state == "disabled"
    if checked:
        fill = QColor(ACCENT)
        if state == "hover":
            fill = QColor("#e5896b")
        if dim:
            fill = QColor("#5a4a44")
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(fill)
        p.drawRoundedRect(box, 7, 7)
        pen = QPen(QColor("#ffffff") if not dim else QColor("#b9aea9"), 4.2)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
        p.setPen(pen)
        tick = QPainterPath(QPointF(_SIZE * 0.27, _SIZE * 0.52))
        tick.lineTo(QPointF(_SIZE * 0.44, _SIZE * 0.69))
        tick.lineTo(QPointF(_SIZE * 0.75, _SIZE * 0.33))
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.drawPath(tick)
    else:
        border = {"hover": QColor(ACCENT), "disabled": QColor("#454b57")}.get(state, QColor("#aab3c5"))
        p.setPen(QPen(border, 3.0))
        p.setBrush(QColor("#2a2f39") if not dim else QColor("#20242b"))
        p.drawRoundedRect(box, 7, 7)
    p.end()
    img.save(path, "PNG")


def _images() -> Dict[str, str]:
    folder = os.path.join(config_dir(), "ui")
    os.makedirs(folder, exist_ok=True)
    stamp = os.path.join(folder, "checkbox.version")
    fresh = not (os.path.exists(stamp) and open(stamp, encoding="utf-8").read().strip() == _VERSION)
    out = {}
    for checked in (False, True):
        for state in ("normal", "hover", "disabled"):
            name = f"cb-{'on' if checked else 'off'}-{state}.png"
            path = os.path.join(folder, name)
            if fresh or not os.path.exists(path):
                _draw(path, checked, state)
            out[f"{'on' if checked else 'off'}-{state}"] = path.replace("\\", "/")
    if fresh:
        with open(stamp, "w", encoding="utf-8") as fh:
            fh.write(_VERSION)
    return out


_cache = None


def checkbox_qss() -> str:
    """QSS for clearly visible checkboxes on the dark dialogs ("" = keep the native look)."""
    global _cache
    if _cache is not None:
        return _cache
    try:
        im = _images()
        _cache = f"""
QCheckBox::indicator {{ width: 18px; height: 18px; }}
QCheckBox::indicator:unchecked {{ image: url("{im['off-normal']}"); }}
QCheckBox::indicator:unchecked:hover {{ image: url("{im['off-hover']}"); }}
QCheckBox::indicator:unchecked:disabled {{ image: url("{im['off-disabled']}"); }}
QCheckBox::indicator:checked {{ image: url("{im['on-normal']}"); }}
QCheckBox::indicator:checked:hover {{ image: url("{im['on-hover']}"); }}
QCheckBox::indicator:checked:disabled {{ image: url("{im['on-disabled']}"); }}
QCheckBox:disabled {{ color: #6b7385; }}
"""
    except Exception:  # noqa: BLE001 - styling must never break a dialog
        _cache = ""
    return _cache
