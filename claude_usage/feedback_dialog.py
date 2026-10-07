"""'Message to the developer' window: optional star rating, name, e-mail, message, consent."""

from __future__ import annotations

import html
import re
from typing import Optional

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import (
    QCheckBox,
    QDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from . import __version__, feedback
from .i18n import current_language, language_name, tr
from .settings_dialog import DIALOG_QSS

ACCENT = "#D97757"
LINK = "#8fb0ff"
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]{2,}$")

FEEDBACK_QSS = DIALOG_QSS + f"""
QLabel#title {{ color: #f0f3fa; font-size: 16px; font-weight: 700; }}
QLabel#intro {{ color: #c9cfdd; }}
QLabel#hint {{ color: #79839a; font-size: 11px; }}
QLabel#error {{ color: #ff9aa5; }}
QLabel#thanks {{ color: #7ff0c2; font-size: 18px; font-weight: 700; }}
QLabel a {{ color: #8fb0ff; }}
QPlainTextEdit {{ background: #23272f; color: #eef1f8; border: 1px solid #333944; border-radius: 7px; padding: 5px 8px;
                  selection-background-color: #4d7cff; }}
QTextBrowser#privacy {{ background: #1b1e25; color: #c9cfdd; border: 1px solid #2c313b; border-radius: 8px; padding: 6px; }}
QPushButton#send {{ background: {ACCENT}; color: #ffffff; border: none; border-radius: 9px; padding: 8px 18px; font-weight: 700; }}
QPushButton#send:hover {{ background: #e5896b; }}
QPushButton#send:disabled {{ background: #5a4a44; color: #cfc4bf; }}
QPushButton#clear {{ background: transparent; border: none; color: #79839a; padding: 0 4px; }}
QPushButton#clear:hover {{ color: #c9cfdd; }}
QFrame#ratingBox {{ background: #1f232b; border: 1px solid #3a4150; border-radius: 10px; }}
QLabel#ratingLabel {{ color: #eef1f8; font-weight: 600; }}
QFrame#consentBox {{ background: rgba(217, 119, 87, 26); border: 1px solid rgba(217, 119, 87, 160); border-radius: 9px; }}
QFrame#consentBox[error="true"] {{ background: rgba(255, 107, 107, 34); border: 2px solid #ff6b6b; }}
QLabel#consentLabel {{ color: #eef1f8; }}
"""


class StarBar(QWidget):
    """Five clickable stars; 0 = no rating. Hover previews the value."""

    changed = Signal(int)

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.value = 0
        self._hover = 0
        self._size = 30
        self.setMouseTracking(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedSize(self._size * 5 + 8, self._size + 6)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    def set_value(self, v: int) -> None:
        v = max(0, min(5, int(v)))
        if v != self.value:
            self.value = v
            self.changed.emit(v)
        self.update()

    def _index_at(self, x: float) -> int:
        return max(0, min(5, int(x // self._size) + 1))

    def mouseMoveEvent(self, e) -> None:
        self._hover = self._index_at(e.position().x())
        self.setToolTip(tr("fb.rating_tip", self._hover))
        self.update()

    def leaveEvent(self, e) -> None:
        self._hover = 0
        self.update()

    def mousePressEvent(self, e) -> None:
        if e.button() == Qt.MouseButton.LeftButton:
            self.set_value(self._index_at(e.position().x()))

    @staticmethod
    def _star(cx: float, cy: float, r: float) -> QPainterPath:
        import math

        path = QPainterPath()
        for i in range(10):
            rad = r if i % 2 == 0 else r * 0.46
            ang = -math.pi / 2 + i * math.pi / 5
            pt = (cx + rad * math.cos(ang), cy + rad * math.sin(ang))
            if i == 0:
                path.moveTo(*pt)
            else:
                path.lineTo(*pt)
        path.closeSubpath()
        return path

    def paintEvent(self, _e) -> None:
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        shown = self._hover or self.value
        for i in range(5):
            cx = 4 + self._size * i + self._size / 2
            cy = self.height() / 2
            path = self._star(cx, cy, self._size * 0.44)
            if i < shown:
                color = QColor("#f5b83d") if not self._hover or self._hover == self.value else QColor("#f9cf74")
                p.fillPath(path, color)
                pen = QPen(QColor("#c98a12"), 1.4)
            else:
                # an empty star must still be clearly visible on the dark background
                p.fillPath(path, QColor("#3a404d"))
                pen = QPen(QColor("#b4bccb") if not self._hover else QColor("#f9cf74"), 1.6)
            pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
            p.setPen(pen)
            p.drawPath(path)


class ConsentLabel(QLabel):
    """The consent text: a click on the words ticks the box, a click on the link opens the notice."""

    clicked = Signal()

    def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
        super().__init__(text, parent)
        self._over_link = False
        self.linkHovered.connect(self._hovered)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def _hovered(self, href: str) -> None:
        self._over_link = bool(href)

    def mouseReleaseEvent(self, e) -> None:
        super().mouseReleaseEvent(e)
        if e.button() == Qt.MouseButton.LeftButton and not self._over_link:
            self.clicked.emit()


class FeedbackDialog(QDialog):
    _done = Signal(bool, str)       # worker thread -> GUI thread

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setWindowTitle(tr("fb.title"))
        self.setStyleSheet(FEEDBACK_QSS)
        self.setMinimumWidth(520)
        self.sender = feedback.Sender()
        self._done.connect(self._on_done)

        root = QVBoxLayout(self)
        root.setContentsMargins(18, 16, 18, 14)
        root.setSpacing(8)

        # ---- form page
        self.form = QWidget()
        f = QVBoxLayout(self.form)
        f.setContentsMargins(0, 0, 0, 0)
        f.setSpacing(8)

        title = QLabel(tr("fb.title"))
        title.setObjectName("title")
        f.addWidget(title)
        intro = QLabel(tr("fb.intro"))
        intro.setObjectName("intro")
        intro.setWordWrap(True)
        f.addWidget(intro)

        rating_box = QFrame()
        rating_box.setObjectName("ratingBox")
        rating_row = QHBoxLayout(rating_box)
        rating_row.setContentsMargins(12, 8, 12, 8)
        rating_row.setSpacing(10)
        lab = QLabel(tr("fb.rating"))
        lab.setObjectName("ratingLabel")
        rating_row.addWidget(lab)
        self.stars = StarBar()
        self.stars.changed.connect(self._rating_changed)
        rating_row.addWidget(self.stars)
        self.btn_clear = QPushButton(tr("fb.rating_clear"))
        self.btn_clear.setObjectName("clear")
        self.btn_clear.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_clear.clicked.connect(lambda: self.stars.set_value(0))
        self.btn_clear.setVisible(False)
        rating_row.addWidget(self.btn_clear)
        self.rating_hint = QLabel(tr("fb.rating_hint"))
        self.rating_hint.setObjectName("hint")
        rating_row.addWidget(self.rating_hint)
        rating_row.addStretch(1)
        f.addWidget(rating_box)

        self.ed_name = QLineEdit()
        self.ed_name.setMaxLength(feedback.MAX_NAME)
        self.ed_name.setPlaceholderText(tr("fb.optional"))
        f.addWidget(self._labelled(tr("fb.name"), self.ed_name))
        self.ed_email = QLineEdit()
        self.ed_email.setMaxLength(feedback.MAX_EMAIL)
        self.ed_email.setPlaceholderText(tr("fb.email_hint"))
        f.addWidget(self._labelled(tr("fb.email"), self.ed_email))
        self.ed_msg = QPlainTextEdit()
        self.ed_msg.setPlaceholderText(tr("fb.message_ph"))
        self.ed_msg.setMinimumHeight(110)
        self.ed_msg.textChanged.connect(self._limit_message)
        f.addWidget(self._labelled(tr("fb.message"), self.ed_msg))

        # consent (required) with a link that opens the privacy notice right here
        self.consent_box = QFrame()
        self.consent_box.setObjectName("consentBox")
        consent_row = QHBoxLayout(self.consent_box)
        consent_row.setContentsMargins(10, 8, 10, 8)
        consent_row.setSpacing(8)
        self.cb_consent = QCheckBox()
        self.cb_consent.setCursor(Qt.CursorShape.PointingHandCursor)
        self.cb_consent.toggled.connect(lambda _on: self._mark_consent(False))
        consent_row.addWidget(self.cb_consent, 0, Qt.AlignmentFlag.AlignTop)
        link = (f'<a href="privacy" style="color:{LINK}; text-decoration:underline;">'
                f'{html.escape(tr("fb.privacy_title"))}</a>')
        text = html.escape(tr("fb.consent", "\u0000")).replace("\u0000", link)
        # the required mark makes it obvious that the box must be ticked
        self.lab_consent = ConsentLabel(text + ' <span style="color:#ff8a8a;">*</span>')
        self.lab_consent.setObjectName("consentLabel")
        self.lab_consent.setTextFormat(Qt.TextFormat.RichText)
        self.lab_consent.setWordWrap(True)
        self.lab_consent.setOpenExternalLinks(False)
        self.lab_consent.linkActivated.connect(lambda _h: self._toggle_privacy())
        self.lab_consent.clicked.connect(self.cb_consent.toggle)
        consent_row.addWidget(self.lab_consent, 1)
        f.addWidget(self.consent_box)

        self.privacy = QTextBrowser()
        self.privacy.setObjectName("privacy")
        self.privacy.setOpenExternalLinks(True)
        self.privacy.document().setDefaultStyleSheet(f"a {{ color: {LINK}; text-decoration: none; }} p {{ margin: 0 0 7px 0; }}")
        paras = [html.escape(x) for x in tr("fb.privacy_text").split("\n\n")]
        # the URL ends at the first character a URL of this site cannot contain (works for CJK text too)
        paras = [re.sub(r"(https://[A-Za-z0-9.\-/#?=&_%]+[A-Za-z0-9/#])", r'<a href="\1">\1</a>', x) for x in paras]
        self.privacy.setHtml("".join(f"<p>{x}</p>" for x in paras))
        self.privacy.setFixedHeight(190)
        self.privacy.setVisible(False)
        f.addWidget(self.privacy)
        self.btn_hide_privacy = QPushButton(tr("fb.privacy_hide"))
        self.btn_hide_privacy.setObjectName("clear")
        self.btn_hide_privacy.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_hide_privacy.clicked.connect(self._toggle_privacy)
        self.btn_hide_privacy.setVisible(False)
        f.addWidget(self.btn_hide_privacy, 0, Qt.AlignmentFlag.AlignLeft)

        self.cb_publish = QCheckBox(tr("fb.publish"))
        self.cb_publish.setEnabled(False)
        f.addWidget(self.cb_publish)

        meta = QLabel(tr("fb.meta", __version__, feedback.os_name(), language_name(current_language())))
        meta.setObjectName("hint")
        meta.setWordWrap(True)
        f.addWidget(meta)
        secure = QLabel("\U0001f512 " + tr("fb.secure"))
        secure.setObjectName("hint")
        f.addWidget(secure)

        self.lab_error = QLabel("")
        self.lab_error.setObjectName("error")
        self.lab_error.setWordWrap(True)
        self.lab_error.setVisible(False)
        f.addWidget(self.lab_error)

        buttons = QHBoxLayout()
        buttons.addStretch(1)
        self.btn_cancel = QPushButton(tr("fb.cancel"))
        self.btn_cancel.clicked.connect(self.reject)
        buttons.addWidget(self.btn_cancel)
        self.btn_send = QPushButton(tr("fb.send"))
        self.btn_send.setObjectName("send")
        self.btn_send.setDefault(True)
        self.btn_send.clicked.connect(self._send)
        buttons.addWidget(self.btn_send)
        f.addLayout(buttons)
        root.addWidget(self.form)

        # ---- thanks page
        self.thanks = QWidget()
        t = QVBoxLayout(self.thanks)
        t.setContentsMargins(0, 24, 0, 12)
        t.setSpacing(10)
        big = QLabel("✓  " + tr("fb.sent"))
        big.setObjectName("thanks")
        big.setAlignment(Qt.AlignmentFlag.AlignCenter)
        t.addWidget(big)
        sub = QLabel(tr("fb.sent_sub"))
        sub.setObjectName("intro")
        sub.setWordWrap(True)
        sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        t.addWidget(sub)
        close = QPushButton(tr("fb.close"))
        close.clicked.connect(self.accept)
        t.addWidget(close, 0, Qt.AlignmentFlag.AlignCenter)
        self.thanks.setVisible(False)
        root.addWidget(self.thanks)

    # ------------------------------------------------------------ helpers

    @staticmethod
    def _labelled(text: str, field: QWidget) -> QWidget:
        box = QWidget()
        lay = QVBoxLayout(box)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(3)
        lab = QLabel(text)
        lab.setObjectName("hint")
        lay.addWidget(lab)
        lay.addWidget(field)
        return box

    def _rating_changed(self, v: int) -> None:
        self.btn_clear.setVisible(v > 0)
        self.rating_hint.setVisible(v == 0)      # the "clear" button takes its place
        self.cb_publish.setEnabled(v > 0)
        if v == 0:
            self.cb_publish.setChecked(False)

    def _limit_message(self) -> None:
        text = self.ed_msg.toPlainText()
        if len(text) > feedback.MAX_MESSAGE:
            cur = self.ed_msg.textCursor()
            self.ed_msg.setPlainText(text[:feedback.MAX_MESSAGE])
            cur.setPosition(min(cur.position(), feedback.MAX_MESSAGE))
            self.ed_msg.setTextCursor(cur)

    def _mark_consent(self, error: bool) -> None:
        self.consent_box.setProperty("error", "true" if error else "false")
        self.consent_box.style().unpolish(self.consent_box)
        self.consent_box.style().polish(self.consent_box)
        if not error and self.lab_error.text() == tr("fb.err_consent"):
            self._error("")

    def _toggle_privacy(self) -> None:
        show = not self.privacy.isVisible()
        self.privacy.setVisible(show)
        self.btn_hide_privacy.setVisible(show)
        # grow / shrink the window with the notice instead of squeezing the form
        self.layout().activate()
        self.resize(self.width(), self.sizeHint().height())

    def _error(self, text: str) -> None:
        self.lab_error.setText(text)
        self.lab_error.setVisible(bool(text))

    # ------------------------------------------------------------ sending

    def _send(self) -> None:
        self._error("")
        msg = self.ed_msg.toPlainText().strip()
        rating = self.stars.value
        email = self.ed_email.text().strip()
        if len(msg) < 5 and rating == 0:
            self._error(tr("fb.err_empty"))
            return
        if email and not _EMAIL_RE.match(email):
            self._error(tr("fb.err_email"))
            self.ed_email.setFocus()
            return
        if len(re.findall(r"https?://", msg, re.I)) > 3:
            self._error(tr("fb.err_links"))
            return
        if not self.cb_consent.isChecked():
            self._error(tr("fb.err_consent"))
            self._mark_consent(True)
            self.cb_consent.setFocus()
            return
        payload = feedback.build_payload(self.ed_name.text(), email, msg, rating,
                                         self.cb_publish.isChecked(), current_language())
        self.btn_send.setEnabled(False)
        self.btn_send.setText(tr("fb.sending"))
        self.sender.start(payload, lambda ok, code: self._done.emit(ok, code))

    def _on_done(self, ok: bool, code: str) -> None:
        self.btn_send.setEnabled(True)
        self.btn_send.setText(tr("fb.send"))
        if ok:
            self.form.setVisible(False)
            self.thanks.setVisible(True)
            self.layout().activate()
            self.resize(self.width(), self.sizeHint().height())
            return
        key = {"rate": "fb.err_rate", "network": "fb.err_network", "email": "fb.err_email",
               "fields": "fb.err_empty", "consent": "fb.err_consent", "links": "fb.err_links"}.get(code, "fb.err_server")
        self._error(tr(key))

    def closeEvent(self, e) -> None:
        # a send in flight finishes on its own thread; the dialog just goes away
        super().closeEvent(e)
