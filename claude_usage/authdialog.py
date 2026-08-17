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
        self.setWindowTitle(f"{APP_TITLE} – bejelentkezés")
        self.setWindowIcon(winutil.app_icon())
        self.setStyleSheet(QSS)
        self.setMinimumWidth(460)

        self._verifier, challenge = oauth.new_pkce()
        self._url, self._state = oauth.build_authorize(self._verifier, challenge)

        intro = QLabel("Bejelentkezés a claude.ai-fiókodba a saját böngésződben "
                       "(ott a jelszavaid és passkey-d már működnek).")
        intro.setWordWrap(True)

        s1 = QLabel("1. lépés")
        s1.setObjectName("big")
        btn_open = QPushButton("Bejelentkezés megnyitása a böngészőben")
        btn_open.setObjectName("link")
        btn_open.clicked.connect(self._open_browser)
        hint1 = QLabel("A megnyíló oldalon lépj be és engedélyezd a hozzáférést. "
                       "A végén kapsz egy kódot.")
        hint1.setObjectName("step")
        hint1.setWordWrap(True)

        s2 = QLabel("2. lépés")
        s2.setObjectName("big")
        hint2 = QLabel("Másold be ide a kapott kódot:")
        hint2.setObjectName("step")
        self.ed = QLineEdit()
        self.ed.setPlaceholderText("kód beillesztése ide")
        self.ed.returnPressed.connect(self._submit)

        self.buttons = QDialogButtonBox()
        self.btn_ok = self.buttons.addButton("Bejelentkezés", QDialogButtonBox.ButtonRole.AcceptRole)
        self.btn_cancel = self.buttons.addButton("Mégse", QDialogButtonBox.ButtonRole.RejectRole)
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
        self.btn_ok.setText("Ellenőrzés…")
        QGuiApplication.processEvents()

        tokens, err = oauth.exchange_code(pasted, self._verifier, self._state)
        self.btn_ok.setEnabled(True)
        self.btn_ok.setText("Bejelentkezés")

        if tokens and tokens.get("access_token"):
            self.succeeded.emit(tokens)
            self.accept()
        elif "429" in err or "rate_limit" in err:
            QMessageBox.warning(
                self, APP_TITLE,
                "Túl sok bejelentkezési próbálkozás rövid idő alatt.\n\n"
                "A szerver átmenetileg korlátoz. Zárd be ezt az ablakot, várj\n"
                "10–15 percet (ne próbálkozz közben), majd indíts EGYETLEN új\n"
                "böngészős bejelentkezést friss kóddal.")
        else:
            QMessageBox.warning(
                self, APP_TITLE,
                "A kód nem fogadható el.\n\n" + (err or "Ismeretlen hiba.") +
                "\n\nEllenőrizd, hogy a teljes kódot másoltad-e be, vagy próbáld újra "
                "a böngészős bejelentkezést (mindig friss kód kell).")
