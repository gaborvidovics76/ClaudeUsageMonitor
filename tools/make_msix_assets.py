"""Renders the MSIX / Microsoft Store images from the app's own logo (winutil.app_pixmap).

    python tools/make_msix_assets.py <Assets folder>

Writes the scale- and target-size variants Windows picks from (resolved through resources.pri), plus an
unqualified file of each name as a fallback:
  Square44x44Logo   app list, taskbar, Start - scale-100..400 and targetsize-16..256 (+ altform-unplated)
  Square150x150Logo medium Start tile        - scale-100/200/400
  Wide310x150Logo   wide Start tile          - scale-100/200/400
  StoreLogo         Store / installer        - scale-100/200/400
"""
from __future__ import annotations

import os
import sys

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PySide6.QtCore import QRectF, Qt  # noqa: E402
from PySide6.QtGui import QGuiApplication, QPainter, QPixmap  # noqa: E402

from claude_usage.winutil import app_pixmap  # noqa: E402


def canvas(w: int, h: int, logo_frac: float) -> QPixmap:
    """The logo centred on a transparent w x h canvas, its side = logo_frac of the shorter edge."""
    pm = QPixmap(w, h)
    pm.fill(Qt.GlobalColor.transparent)
    side = max(1, round(min(w, h) * logo_frac))
    logo = app_pixmap(side * 2).scaled(side, side, Qt.AspectRatioMode.KeepAspectRatio,
                                       Qt.TransformationMode.SmoothTransformation)
    p = QPainter(pm)
    p.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)
    p.drawPixmap(QRectF((w - side) / 2, (h - side) / 2, side, side), logo, QRectF(logo.rect()))
    p.end()
    return pm


def save(pm: QPixmap, folder: str, name: str) -> None:
    path = os.path.join(folder, name)
    if not pm.save(path, "PNG"):
        raise SystemExit(f"could not write {path}")


def main(folder: str) -> int:
    QGuiApplication(sys.argv[:1])
    os.makedirs(folder, exist_ok=True)
    n = 0
    scales = (100, 125, 150, 200, 400)
    # app list / taskbar icon: the rounded square nearly fills the box
    for s in scales:
        px = round(44 * s / 100)
        save(canvas(px, px, 0.92), folder, f"Square44x44Logo.scale-{s}.png"); n += 1
    for t in (16, 24, 32, 48, 256):
        pm = canvas(t, t, 1.0 if t <= 32 else 0.94)
        save(pm, folder, f"Square44x44Logo.targetsize-{t}.png")
        save(pm, folder, f"Square44x44Logo.targetsize-{t}_altform-unplated.png"); n += 2
    for s in (100, 200, 400):
        f = s / 100
        save(canvas(round(150 * f), round(150 * f), 0.66), folder, f"Square150x150Logo.scale-{s}.png")
        save(canvas(round(310 * f), round(150 * f), 0.66), folder, f"Wide310x150Logo.scale-{s}.png")
        save(canvas(round(50 * f), round(50 * f), 1.0), folder, f"StoreLogo.scale-{s}.png"); n += 3
    # unqualified fallbacks (used when no resources.pri is present)
    save(canvas(88, 88, 0.92), folder, "Square44x44Logo.png")
    save(canvas(300, 300, 0.66), folder, "Square150x150Logo.png")
    save(canvas(620, 300, 0.66), folder, "Wide310x150Logo.png")
    save(canvas(100, 100, 1.0), folder, "StoreLogo.png"); n += 4
    print(f"{n} images -> {folder}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    sys.exit(main(sys.argv[1]))
