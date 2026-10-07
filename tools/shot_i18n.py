"""Offscreen screenshots of the UI in the given languages, for a visual check of the translations.

    python tools/shot_i18n.py ja ko zh-CN          -> build-shots/<code>/*.png
    python tools/shot_i18n.py --all

Per language: the panel in all three layouts (with sample data), the right-click menu, every
Settings tab, the "Message to the developer" window (with the privacy notice open) and the Help
window. Settings are never written: a throw-away settings object is used.
"""

from __future__ import annotations

import os
import sys
import time

# the real platform renderer (true fonts); windows are kept off the screen
if "--offscreen" in sys.argv:
    os.environ["QT_QPA_PLATFORM"] = "offscreen"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from PySide6.QtCore import Qt  # noqa: E402
from PySide6.QtWidgets import QApplication, QTabWidget  # noqa: E402

app = QApplication([])

from claude_usage.uistyle import checkbox_qss  # noqa: E402

app.setStyleSheet(checkbox_qss())

from claude_usage import i18n  # noqa: E402
from claude_usage import settings as settings_mod  # noqa: E402
from claude_usage.datasource import Gauge, Metrics  # noqa: E402


class FakeSettings(settings_mod.Settings):
    def load(self) -> None:          # never read the user's settings
        pass

    def save(self) -> None:          # never write them either
        pass


def sample_metrics() -> Metrics:
    now = int(time.time() * 1000)
    m = Metrics(ok=True, updated_at=now - 50_000, sample_count=20)
    m.five_hour = Gauge(value=44, reset_at=now + 57 * 60_000, reset_certain=True, burn=9.5,
                        spark=[5, 9, 14, 20, 28, 33, 39, 44])
    m.weekly = Gauge(value=38, reset_at=now + (3 * 24 + 10) * 3_600_000, reset_certain=True, burn=0.6,
                     pace=4.0, spark=[10, 14, 18, 22, 27, 31, 35, 38])
    m.model = Gauge(value=41, reset_at=now + (3 * 24 + 10) * 3_600_000, reset_certain=True)
    m.model_name = "Fable"
    return m


def grab(widget, path: str) -> None:
    widget.setAttribute(Qt.WidgetAttribute.WA_DontShowOnScreen, True)
    widget.show()
    for _ in range(3):
        app.processEvents()
    widget.grab().save(path)


def shoot(code: str, out_root: str) -> None:
    from claude_usage.feedback_dialog import FeedbackDialog
    from claude_usage.help_dialog import HelpDialog
    from claude_usage.settings_dialog import SettingsDialog
    from claude_usage.widget import UsageWidget
    from claude_usage.app import apply_language_env

    i18n.set_language(code)
    apply_language_env(app)
    out = os.path.join(out_root, code)
    os.makedirs(out, exist_ok=True)

    s = FakeSettings()
    for layout in ("postit", "ring", "compact"):
        s["layout"] = layout
        w = UsageWidget(s)
        w.set_metrics(sample_metrics())
        w.apply_settings()
        grab(w, os.path.join(out, f"panel-{layout}.png"))
        w.close()

    try:
        dlg = SettingsDialog(s, [])
        tabs = dlg.findChild(QTabWidget)
        for i in range(tabs.count() if tabs else 0):
            tabs.setCurrentIndex(i)
            grab(dlg, os.path.join(out, f"settings-{i}.png"))
        dlg.close()
    except Exception as e:  # noqa: BLE001
        print(f"  {code}: settings failed: {e}")

    fb = FeedbackDialog()
    fb.stars.set_value(5)
    grab(fb, os.path.join(out, "feedback.png"))
    fb._toggle_privacy()
    grab(fb, os.path.join(out, "feedback-privacy.png"))
    fb.close()

    try:
        hd = HelpDialog()
        grab(hd, os.path.join(out, "help.png"))
        hd.close()
    except Exception as e:  # noqa: BLE001
        print(f"  {code}: help failed: {e}")
    print(f"{code}: {len(os.listdir(out))} images -> {out}")


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    codes = list(i18n.LANG_NAMES) if "--all" in sys.argv or not args else args
    out_root = os.path.join(ROOT, "build-shots")
    for code in codes:
        if code not in i18n.LANG_NAMES:
            print(f"unknown language: {code}")
            continue
        shoot(code, out_root)


if __name__ == "__main__":
    main()
