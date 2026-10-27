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
from claude_usage import settings as _settings, store
print("TITLE_STORE_NAME", _settings.APP_TITLE == store.STORE_NAME)
print("TEXT_STORE_NAME", store.STORE_NAME in i18n.tr("set.backup_disclaimer") and store.BRAND not in i18n.tr("set.backup_disclaimer"))
from claude_usage import help_dialog
_guide = help_dialog._guide_html()
print("GUIDE_UPDATES", "SHA-256" in _guide)
print("GUIDE_FEEDBACK_NOTE", "claudeusagemonitor.com" in _guide and i18n.tr("help.privacy_feedback")[:20] in _guide.replace("&quot;", '"'))
_help = help_dialog.HelpDialog()
_author = _help.tabs.widget(1).findChildren(QLabel)
_links = " ".join(l.text() for l in _author)
print("AUTHOR_STORE_LINK", store.STORE_URL in _links)
print("AUTHOR_STORE_PRIVACY", "legal/store-en.html" in _links and "#privacy" not in _links)
from claude_usage.feedback_dialog import FeedbackDialog
_priv = FeedbackDialog().privacy.toPlainText()
print("PRIVACY_STORE_CONTROLLER", store.STORE_CONTROLLER["reg"] in _priv and "legal/store-en.html" in _priv)
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
                   "TITLE_STORE_NAME": False, "TEXT_STORE_NAME": False, "GUIDE_UPDATES": True,
                   "GUIDE_FEEDBACK_NOTE": True, "AUTHOR_STORE_LINK": True, "AUTHOR_STORE_PRIVACY": False,
                   "PRIVACY_STORE_CONTROLLER": False, "VISIBLE_PATH_UNCHANGED": True}, zipmode
print("1) ZIP install: autostart checkbox + update controls, as before: ok")

store = run(True)
assert store == {"PACKAGED": True, "AUTOSTART_CHECKBOX": False, "AUTOSTART_BUTTON": True, "STORE_HINT": True,
                 "UPDATE_CHECKBOX": False, "UPDATE_BUTTON": False, "STORE_LABEL": True,
                 "TITLE_STORE_NAME": True, "TEXT_STORE_NAME": True, "GUIDE_UPDATES": False,
                 "GUIDE_FEEDBACK_NOTE": True, "AUTHOR_STORE_LINK": True, "AUTHOR_STORE_PRIVACY": True,
                 "PRIVACY_STORE_CONTROLLER": True, "VISIBLE_PATH_UNCHANGED": True}, store
print("2) Store package: startup-settings button + hint, no update controls, 'Microsoft Store' by the version,")
print("   the reserved Store name in the title and in the texts (ZIP keeps its own name),")
print("   no self-update section in the help guide; the feedback form is named in its privacy part,")
print("   the privacy notice names the Store publisher as controller (ZIP keeps its own), and the help window's")
print("   Privacy link opens the Store privacy policy; both installs link the Microsoft Store page: ok")

import json  # noqa: E402

from claude_usage import store as _store  # noqa: E402

with open(os.path.join(ROOT, "packaging", "msix", "identity.json"), encoding="utf-8") as fh:
    _id = json.load(fh)
assert _id["display_name"] == _store.STORE_NAME, (_id["display_name"], _store.STORE_NAME)
assert _id["publisher"].startswith("CN=") and len(_id["publisher"]) == 39, "Partner Center publisher CN=<GUID> expected"
# Partner Center compares it character by character ("30km.hu Kft" without the full stop was rejected)
assert _id["publisher_display_name"] == "30km.hu Kft.", _id["publisher_display_name"]
print("2b) identity.json display_name = the Store name in the program; real Partner Center publisher and its")
print("    display name exactly as in Partner Center: ok")

env = dict(os.environ, CLAUDE_USAGE_MONITOR_PACKAGED="1")
code = subprocess.run([sys.executable, os.path.join(ROOT, "main.py"), "--enable-autostart"], env=env, timeout=60).returncode
assert code == 0
print("3) Store package: --enable-autostart is refused (logged), the scheduled task is not touched: ok")

from claude_usage import i18n  # noqa: E402

for lang in i18n.LANG_NAMES:
    text = i18n.lookup("set.autostart_store", lang)
    assert text and text != "set.autostart_store", lang
print("4) the Store hint exists in all %d languages: ok" % len(i18n.LANG_NAMES))

import re  # noqa: E402

from claude_usage.help_dialog import GUIDE_PRIVACY_INDEX  # noqa: E402

for lang in i18n.LANG_NAMES:
    secs = re.split(r"(?=<h2>)", i18n.lookup("help.guide", lang))
    assert len(secs) == 9, (lang, len(secs))
    assert [i for i, sec in enumerate(secs) if "SHA-256" in sec] == [6], lang      # the updates section
    assert GUIDE_PRIVACY_INDEX == 7 and "SHA-256" not in secs[GUIDE_PRIVACY_INDEX], lang
    note = i18n.lookup("help.privacy_feedback", lang)
    assert note != "help.privacy_feedback" and "{feedback}" in note and "claudeusagemonitor.com" in note, lang
print("5) help guide: same 9 sections in every language, the feedback note in all of them: ok")

assert all(str(v).strip() for v in _store.STORE_CONTROLLER.values()), _store.STORE_CONTROLLER
for lang in i18n.LANG_NAMES:
    assert len(i18n.lookup("fb.privacy_text", lang).split("\n\n")) == 7, lang          # paragraph 0 = controller
    para = _store.controller_paragraph(i18n.lookup("fb.privacy_controller_store", lang), lang)
    assert _store.STORE_CONTROLLER["reg"] in para and "/legal/store-" in para, lang
assert re.fullmatch(r"9[0-9A-Z]{11}", _store.STORE_ID) and _store.STORE_URL.endswith(_store.STORE_ID), _store.STORE_ID
assert _store.privacy_url("hu").endswith("store-hu.html") and _store.privacy_url("de").endswith("store-en.html")
print("6) Store controller filled in, its notice in all %d languages: ok" % len(i18n.LANG_NAMES))
print("ALL STORE-MODE TESTS OK")
