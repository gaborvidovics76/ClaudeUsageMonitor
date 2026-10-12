"""Renders the App Store icon set (PNG, every macOS size) with Qt - run on Windows or macOS:

    python macos/Xcode/tools/make_icon.py

Design note: the icon is deliberately NOT the Windows app's orange starburst. The starburst is the
shape of Anthropic's Claude logo, and App Store Review Guideline 5.2.1 (plus Anthropic's trademark
guidelines) forbid third-party apps from using a rights-holder's logo or a copycat of it. This icon
is a neutral gauge: a dark rounded square with a three-quarter progress ring and a percent sign.
"""
from __future__ import annotations

import math
import os
import sys

from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QColor, QConicalGradient, QLinearGradient, QPainter, QPainterPath, QPen, QPixmap
from PySide6.QtWidgets import QApplication

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "ClaudeUsageMonitor", "Resources", "Assets.xcassets", "AppIcon.appiconset")
SIZES = (16, 32, 64, 128, 256, 512, 1024)


def render(size: int) -> QPixmap:
    pm = QPixmap(size, size)
    pm.fill(Qt.GlobalColor.transparent)
    p = QPainter(pm)
    p.setRenderHint(QPainter.RenderHint.Antialiasing, True)
    s = float(size)

    # macOS icons leave a transparent margin around the rounded square (about 10 % each side)
    m = s * 0.10
    box = QRectF(m, m, s - 2 * m, s - 2 * m)
    radius = box.width() * 0.225
    body = QPainterPath()
    body.addRoundedRect(box, radius, radius)
    bg = QLinearGradient(box.topLeft(), box.bottomRight())
    bg.setColorAt(0.0, QColor(36, 44, 70))
    bg.setColorAt(1.0, QColor(16, 20, 34))
    p.fillPath(body, bg)
    # soft inner highlight at the top
    hi = QPainterPath()
    hi.addRoundedRect(QRectF(box.left(), box.top(), box.width(), box.height() * 0.5), radius, radius)
    hg = QLinearGradient(box.topLeft(), QPointF(box.left(), box.top() + box.height() * 0.5))
    hg.setColorAt(0.0, QColor(255, 255, 255, 38))
    hg.setColorAt(1.0, QColor(255, 255, 255, 0))
    p.fillPath(hi, hg)

    # the gauge: a three-quarter ring, open at the bottom
    c = box.center()
    r = box.width() * 0.33
    thick = max(1.5, box.width() * 0.105)
    ring = QRectF(c.x() - r, c.y() - r, 2 * r, 2 * r)
    start_deg, span_deg = 225.0, -270.0          # Qt: 0° = 3 o'clock, counter-clockwise positive
    track = QPen(QColor(255, 255, 255, 40), thick, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)
    p.setPen(track)
    p.setBrush(Qt.BrushStyle.NoBrush)
    p.drawArc(ring, int(start_deg * 16), int(span_deg * 16))
    # the filled part (about 70 %), green -> amber -> coral along the sweep
    grad = QConicalGradient(c, start_deg)
    grad.setColorAt(0.00, QColor(74, 214, 160))
    grad.setColorAt(0.38, QColor(255, 190, 92))
    grad.setColorAt(0.70, QColor(255, 106, 106))
    grad.setColorAt(0.75, QColor(255, 106, 106))
    grad.setColorAt(1.00, QColor(74, 214, 160))
    fill = QPen(grad, thick, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)
    p.setPen(fill)
    p.drawArc(ring, int(start_deg * 16), int(span_deg * 0.72 * 16))

    # percent sign in the middle, drawn geometrically (no font dependence, same on every OS)
    if size >= 32:
        ink = QColor(240, 244, 255)
        d = box.width() * 0.30            # the sign's bounding square
        cx, cy = c.x(), c.y() + box.height() * 0.01
        stroke = max(1.2, d * 0.17)
        p.setPen(QPen(ink, stroke, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.drawLine(QPointF(cx - d * 0.36, cy + d * 0.42), QPointF(cx + d * 0.36, cy - d * 0.42))
        ring_r = d * 0.19
        p.setPen(QPen(ink, max(1.0, d * 0.13)))
        p.drawEllipse(QPointF(cx - d * 0.30, cy - d * 0.30), ring_r, ring_r)
        p.drawEllipse(QPointF(cx + d * 0.30, cy + d * 0.30), ring_r, ring_r)
    else:
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QColor(240, 244, 255))
        p.drawEllipse(c, s * 0.08, s * 0.08)
    p.end()
    return pm


def main() -> int:
    app = QApplication.instance() or QApplication(sys.argv)  # noqa: F841 - Qt needs it for painting
    os.makedirs(OUT, exist_ok=True)
    for size in SIZES:
        path = os.path.join(OUT, f"icon_{size}.png")
        if not render(size).save(path, "PNG"):
            print("failed:", path)
            return 1
        print("wrote", os.path.relpath(path, os.path.join(HERE, "..")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
