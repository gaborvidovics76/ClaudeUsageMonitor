# -*- coding: utf-8 -*-
"""Run:  python tests/store_mode.py

The Microsoft Store (MSIX) mode: forced on with CLAUDE_USAGE_MONITOR_PACKAGED=1, then the System tab of the
settings dialog must offer the Windows startup settings instead of the autostart checkbox and no update
controls, the CLI must refuse autostart/update switches, and visible_path must leave paths alone when there
is no real package. Without the variable everything stays as in the ZIP install."""
import os
import subprocess
import sys

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

CHILD = r"""
import os, sys
sys.path.insert(0, %r)
from PySide6.QtWidgets import QApplication, QCheckBox, QPushButton, QLabel
from claude_usage import winutil, i18n
from claude_usage.settings import Settings
from claude_usage.settings_dialog import SettingsDialog
i18n.set_language("en")
app = QApplication([])
dlg = SettingsDialog(Settings(), [])
page = dlg._tab_system()
checks = [c.text() for c in page.findChildren(QCheckBox)]
buttons = [b.text() for b in page.findChildren(QPushButton)]
labels = [l.text() for l in page.findChildren(QLabel)]
print("PACKAGED", winutil.is_packaged())
print("AUTOSTART_CHECKBOX", any(t == i18n.tr("menu.autostart") for t in checks))
print("AUTOSTART_BUTTON", any(t == i18n.tr("menu.autostart") + "\u2026" for t in buttons))
print("STORE_HINT", any(t == i18n.tr("set.autostart_store") for t in labels))
print("UPDATE_CHECKBOX", any(t == i18n.tr("set.update_check") for t in checks))
print("UPDATE_BUTTON", any(t == i18n.tr("menu.check_update") for t in buttons))
print("STORE_LABEL", any("Microsoft Store" in t for t in labels))
print("VISIBLE_PATH_UNCHANGED", winutil.visible_path(os.environ.get("APPDATA", "C:\\x")) == os.environ.get("APPDATA", "C:\\x"))
""" % ROOT


def run(packaged: bool) -> dict:
    env = dict(os.environ)
    env.pop("CLAUDE_USAGE_MONITOR_PACKAGED", None)
    if packaged:
        env["CLAUDE_USAGE_MONITOR_PACKAGED"] = "1"
    out = subprocess.run([sys.executable, "-c", CHILD], capture_output=True, text=True, env=env, timeout=120)
    if out.returncode != 0:
        raise SystemExit(out.stderr[-2000:])
    return {k: v == "True" for k, v in (ln.split(" ", 1) for ln in out.stdout.splitlines() if " " in ln)}


zipmode = run(False)
assert zipmode == {"PACKAGED": False, "AUTOSTART_CHECKBOX": True, "AUTOSTART_BUTTON": False, "STORE_HINT": False,
                   "UPDATE_CHECKBOX": True, "UPDATE_BUTTON": True, "STORE_LABEL": False,
                   "VISIBLE_PATH_UNCHANGED": True}, zipmode
print("1) ZIP install: autostart checkbox + update controls, as before: ok")

store = run(True)
assert store == {"PACKAGED": True, "AUTOSTART_CHECKBOX": False, "AUTOSTART_BUTTON": True, "STORE_HINT": True,
                 "UPDATE_CHECKBOX": False, "UPDATE_BUTTON": False, "STORE_LABEL": True,
                 "VISIBLE_PATH_UNCHANGED": True}, store
print("2) Store package: startup-settings button + hint, no update controls, 'Microsoft Store' by the version: ok")

env = dict(os.environ, CLAUDE_USAGE_MONITOR_PACKAGED="1")
code = subprocess.run([sys.executable, os.path.join(ROOT, "main.py"), "--enable-autostart"], env=env, timeout=60).returncode
assert code == 0
print("3) Store package: --enable-autostart is refused (logged), the scheduled task is not touched: ok")

from claude_usage import i18n  # noqa: E402

for lang in i18n.LANG_NAMES:
    text = i18n.lookup("set.autostart_store", lang)
    assert text and text != "set.autostart_store", lang
print("4) the Store hint exists in all %d languages: ok" % len(i18n.LANG_NAMES))
print("ALL STORE-MODE TESTS OK")
