"""Click-through mode leaves the panel deaf to the mouse - the ways back to the menu must work.

    python tests/click_through_escape.py

1) switching click-through on (menu or Settings - both go through apply_settings) raises the notification once,
   and switching it on again later raises it again; switching it off never does;
2) a second start leaves the wake-up marker and the running instance consumes it within its 1 s poll and opens
   Settings; a stale marker from before the start is dropped without opening anything;
3) the texts exist in all 34 languages and the Settings page carries the hint under the checkbox.
Settings are never written: a throw-away settings object is used, and the marker goes to a temporary folder.
"""

from __future__ import annotations

import os
import sys
import tempfile

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from PySide6.QtWidgets import QApplication, QCheckBox, QLabel  # noqa: E402

app = QApplication([])

from claude_usage import i18n, wakeup  # noqa: E402
from claude_usage import settings as settings_mod  # noqa: E402

TMP = tempfile.mkdtemp(prefix="cum-wakeup-")
wakeup.config_dir = lambda: TMP      # the marker never touches the real settings folder


class FakeSettings(settings_mod.Settings):
    def load(self) -> None:
        pass

    def save(self) -> None:
        pass


def fail(msg: str) -> None:
    print("FAIL:", msg)
    sys.exit(1)


# --- 3) texts and the Settings hint
for key in ("notify.click_through", "err.already_running_settings"):
    missing = [c for c in i18n.LANG_NAMES if not i18n.STRINGS.get(key, {}).get(c)]
    if missing:
        fail(f"{key} missing in: {missing}")
from claude_usage.settings_dialog import SettingsDialog  # noqa: E402

i18n.set_language("en")
dlg = SettingsDialog(FakeSettings(), [])
page = dlg._tab_appearance()
labels = [lb.text() for lb in page.findChildren(QLabel)]
checks = [cb.text() for cb in page.findChildren(QCheckBox)]
if i18n.tr("set.click_through") not in checks or i18n.tr("notify.click_through") not in labels:
    fail("the Settings page lacks the click-through checkbox or its hint")
print("3) texts in all 34 languages; the hint sits under the click-through checkbox in Settings: ok")

# --- 1) + 2) on the real MonitorApp (offscreen, throw-away settings)
from claude_usage import app as app_mod  # noqa: E402

app_mod.Settings = FakeSettings
wakeup.request()                     # a stale marker from an earlier start
mon = app_mod.MonitorApp(app)
if os.path.exists(os.path.join(TMP, wakeup.MARKER)):
    fail("the stale marker survived the start")

shown: list = []
mon.notify = lambda title, body: shown.append(body)
opened: list = []
mon.show_settings = lambda: opened.append(1)

mon.settings["click_through"] = True
mon.apply_settings()
mon.apply_settings()                 # a second pass (slider move, theme change) must not repeat it
mon.settings["click_through"] = False
mon.apply_settings()
mon.settings["click_through"] = True
mon.apply_settings()
texts = [i18n.tr("notify.click_through")]
if shown != texts * 2:
    fail(f"notification count/text wrong: {shown}")
print("1) click-through on -> one notification; repeated apply -> none; off -> none; on again -> one: ok")

if not wakeup.request():
    fail("wakeup.request() could not write the marker")
mon._poll_wakeup()
mon._poll_wakeup()                   # consumed once
if opened != [1] or os.path.exists(os.path.join(TMP, wakeup.MARKER)):
    fail(f"wake-up: opened={opened}, marker left={os.path.exists(os.path.join(TMP, wakeup.MARKER))}")
if mon.wake.interval() > 1500 or not mon.wake.isActive():
    fail(f"the wake-up poll must run about every second (interval {mon.wake.interval()}, active {mon.wake.isActive()})")
print("2) second start -> marker -> the running instance opens Settings once, marker removed, 1 s poll active: ok")
print("ALL CLICK-THROUGH ESCAPE TESTS OK")
