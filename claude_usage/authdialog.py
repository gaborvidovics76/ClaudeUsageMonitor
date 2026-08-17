"""Bejelentkező párbeszéd: rendszerböngésző + kód visszamásolása."""

from __future__ import annotations

import webbrowser
from typing import Optional

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QDesktopServices, QGuiApplication
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)

from . import oauth, winutil
from .i18n import tr
from .settings import APP_TITLE

QSS = """
QDialog { background: #16181d; }
QLabel { color: #d3d8e4; font-size: 13px; }
QLabel#step { color: #9aa3b6; font-size: 12px; }
QLabel#big { color: #f0f3fa; font-size: 15px; font-weight: 600; }
QLineEdit { background: #23272f; color: #eef1f8; border: 1px solid #38414f;
            border-radius: 8px; padding: 8px 10px; font-size: 13px; }
QPushButton { background: #33405e; color: #eaf0ff; border: 1px solid #4c6296;
              border-radius: 8px; padding: 8px 16px; font-size: 13px; }
QPushButton:hover { background: #3c4a6e; }
QPushButton#link { background: #262b34; border-color: #343b47; }
"""


class OAuthDialog(QDialog):
    """Sikeres belépéskor a `succeeded` jel a token-szótárat adja."""

    succeeded = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"{APP_TITLE} – " + tr("dlg.login_title"))
        self.setWindowIcon(winutil.app_icon())
        self.setStyleSheet(QSS)
        self.setMinimumWidth(460)

        self._verifier, challenge = oauth.new_pkce()
        self._url, self._state = oauth.build_authorize(self._verifier, challenge)

        intro = QLabel(tr("dlg.intro"))
        intro.setWordWrap(True)

        s1 = QLabel(tr("dlg.step1"))
        s1.setObjectName("big")
        btn_open = QPushButton(tr("dlg.open_browser"))
        btn_open.setObjectName("link")
        btn_open.clicked.connect(self._open_browser)
        hint1 = QLabel(tr("dlg.hint1"))
        hint1.setObjectName("step")
        hint1.setWordWrap(True)

        s2 = QLabel(tr("dlg.step2"))
        s2.setObjectName("big")
        hint2 = QLabel(tr("dlg.paste_label"))
        hint2.setObjectName("step")
        self.ed = QLineEdit()
        self.ed.setPlaceholderText(tr("dlg.paste_placeholder"))
        self.ed.returnPressed.connect(self._submit)

        self.buttons = QDialogButtonBox()
        self.btn_ok = self.buttons.addButton(tr("dlg.signin"), QDialogButtonBox.ButtonRole.AcceptRole)
        self.btn_cancel = self.buttons.addButton(tr("dlg.cancel"), QDialogButtonBox.ButtonRole.RejectRole)
        self.btn_ok.clicked.connect(self._submit)
        self.btn_cancel.clicked.connect(self.reject)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(18, 16, 18, 14)
        lay.setSpacing(9)
        lay.addWidget(intro)
        lay.addSpacing(4)
        lay.addWidget(s1)
        lay.addWidget(btn_open)
        lay.addWidget(hint1)
        lay.addSpacing(6)
        lay.addWidget(s2)
        lay.addWidget(hint2)
        lay.addWidget(self.ed)
        lay.addWidget(self.buttons)

    def _open_browser(self) -> None:
        if not QDesktopServices.openUrl(QUrl(self._url)):
            webbrowser.open(self._url)
        self.ed.setFocus()

    def _submit(self) -> None:
        pasted = self.ed.text().strip()
        # kényelmi másolás: néha a teljes URL-t másolják be
        if "code=" in pasted:
            import urllib.parse

            q = urllib.parse.urlparse(pasted).query
            params = urllib.parse.parse_qs(q)
            code = (params.get("code") or [""])[0]
            state = (params.get("state") or [self._state])[0]
            pasted = f"{code}#{state}" if code else pasted

        self.btn_ok.setEnabled(False)
        self.btn_ok.setText(tr("dlg.checking"))
        QGuiApplication.processEvents()

        tokens, err = oauth.exchange_code(pasted, self._verifier, self._state)
        self.btn_ok.setEnabled(True)
        self.btn_ok.setText(tr("dlg.signin"))

        if tokens and tokens.get("access_token"):
            self.succeeded.emit(tokens)
            self.accept()
        elif "429" in err or "rate_limit" in err:
            QMessageBox.warning(self, APP_TITLE, tr("dlg.err_ratelimit"))
        else:
            QMessageBox.warning(self, APP_TITLE,
                                tr("dlg.err_badcode", err or tr("dlg.unknown_err")))
