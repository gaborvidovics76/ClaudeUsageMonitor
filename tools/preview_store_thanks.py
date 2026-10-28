"""Preview of the one-time "thank you, the signed version is in the Store" window (claude_usage/store_thanks.py).

    python tools/preview_store_thanks.py hu            -> the real, animated window in Hungarian
    python tools/preview_store_thanks.py --shots --all -> build-shots/store-thanks/<code>.png + _all.png

Settings are never read or written, so the real "already shown" flag stays untouched.
"""

from __future__ import annotations

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from PySide6.QtCore import Qt  # noqa: E402
from PySide6.QtGui import QColor, QFont, QPainter, QPixmap  # noqa: E402
from PySide6.QtWidgets import QApplication  # noqa: E402

app = QApplication([])

from claude_usage import i18n  # noqa: E402
from claude_usage.app import apply_language_env  # noqa: E402
from claude_usage.store_thanks import StoreThanksDialog  # noqa: E402
from claude_usage.uistyle import checkbox_qss  # noqa: E402

app.setStyleSheet(checkbox_qss())


def grab(code: str, out: str) -> QPixmap:
    i18n.set_language(code)
    apply_language_env(app)
    dlg = StoreThanksDialog(animate=False)
    dlg.setAttribute(Qt.WidgetAttribute.WA_DontShowOnScreen, True)
    dlg.show()
    for _ in range(3):
        app.processEvents()
    pm = dlg.grab()
    pm.save(os.path.join(out, f"{code}.png"))
    dlg.close()
    return pm


def contact_sheet(shots: dict, path: str, cols: int = 6) -> None:
    """All languages on one image, each labelled with its code."""
    w = max(p.width() for p in shots.values())
    h = max(p.height() for p in shots.values()) + 26
    rows = (len(shots) + cols - 1) // cols
    sheet = QPixmap(cols * w, rows * h)
    sheet.fill(QColor("#0e1014"))
    p = QPainter(sheet)
    p.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
    p.setPen(QColor("#D97757"))
    for i, (code, pm) in enumerate(shots.items()):
        x, y = (i % cols) * w, (i // cols) * h
        p.drawText(x + 8, y + 19, f"{code} – {i18n.LANG_NAMES[code]}")
        p.drawPixmap(x, y + 26, pm)
    p.end()
    sheet.save(path)


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if "--shots" in sys.argv:
        codes = list(i18n.LANG_NAMES) if "--all" in sys.argv or not args else args
        out = os.path.join(ROOT, "build-shots", "store-thanks")
        os.makedirs(out, exist_ok=True)
        shots = {c: grab(c, out) for c in codes if c in i18n.LANG_NAMES}
        if len(shots) > 1:
            contact_sheet(shots, os.path.join(out, "_all.png"))
        print(f"{len(shots)} images -> {out}")
        return 0
    code = args[0] if args else (i18n.system_language() or "en")
    i18n.set_language(code)
    apply_language_env(app)
    dlg = StoreThanksDialog()
    dlg.finished.connect(app.quit)
    dlg.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
