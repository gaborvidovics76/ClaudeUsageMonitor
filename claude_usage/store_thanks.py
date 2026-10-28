"""A one-time thank-you to the people who installed the unsigned website (ZIP) version.

It thanks them for trusting a program that Windows warned them about, and tells them that the signed version
is now in the Microsoft Store. Shown once, only by the ZIP install on Windows, and only to people who installed
it before this message existed: a fresh install already picked the ZIP on a download page that offers the Store
first. Nothing is sent anywhere; the "shown" flag lives in the local settings.
"""

from __future__ import annotations

import math
import random
import sys

from PySide6.QtCore import QPointF, QRectF, Qt, QTimer, QUrl
from PySide6.QtGui import QColor, QDesktopServices, QFont, QLinearGradient, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import QDialog, QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget

from . import store, winutil
from .i18n import tr
from .settings_dialog import DIALOG_QSS

ACCENT = "#D97757"          # the Claude orange of the app icon
SEAL = "#2fa86b"            # the green "signed" stamp
STORE_APP_URL = f"ms-windows-store://pdp/?productid={store.STORE_ID}"   # opens the Store app itself

THANKS_QSS = DIALOG_QSS + f"""
QLabel#heading {{ color: #ffffff; font-size: 20px; font-weight: 800; }}
QLabel#body {{ color: #d6dbe8; font-size: 13px; }}
QFrame#tipBox {{ background: #1f232b; border: 1px solid #2c313b; border-radius: 10px; }}
QLabel#tip {{ color: #9aa3b8; font-size: 12px; }}
QLabel#signName {{ color: {ACCENT}; font-size: 24px; }}
QLabel#signRole {{ color: #79839a; font-size: 11px; }}
QPushButton#storeButton {{ background: {ACCENT}; color: #ffffff; border: none; border-radius: 9px;
                           padding: 9px 18px; font-weight: 700; }}
QPushButton#storeButton:hover {{ background: #e5896b; }}
QPushButton#stayButton {{ padding: 9px 16px; }}
"""


def due(settings) -> bool:
    """True when this install should show the thank-you now."""
    return (sys.platform.startswith("win") and not winutil.is_packaged()
            and not settings["store_thanks_shown"])


def open_store() -> None:
    """The product page in the Store app; the web page when the Store app is missing (e.g. Windows LTSC)."""
    if not QDesktopServices.openUrl(QUrl(STORE_APP_URL)):
        QDesktopServices.openUrl(QUrl(store.STORE_URL))


class _Banner(QWidget):
    """The header: the app logo, confetti falling into place, and a green 'signed' seal stamped on the logo."""

    DURATION_MS = 1800

    def __init__(self, parent=None, animate: bool = True) -> None:
        super().__init__(parent)
        self.setFixedHeight(150)
        self._logo = winutil.app_pixmap(176)
        rng = random.Random(9)                      # the same confetti every time
        colors = ["#D97757", "#f2b134", "#4d7cff", "#2fa86b", "#e5596b", "#b07cff", "#f0f3fa"]
        self._confetti = [(rng.random(), rng.uniform(0.08, 0.95), rng.uniform(4, 9), rng.uniform(0, 180),
                           rng.choice(colors), rng.uniform(0.0, 0.35), rng.random() < 0.3) for _ in range(46)]
        self._t = 0.0 if animate else 1.0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self._elapsed = 0
        if animate:
            self._timer.start(16)

    def _tick(self) -> None:
        self._elapsed += 16
        self._t = min(1.0, self._elapsed / self.DURATION_MS)
        if self._t >= 1.0:
            self._timer.stop()
        self.update()

    def paintEvent(self, _event) -> None:
        w, h = self.width(), self.height()
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        card = QPainterPath()
        card.addRoundedRect(QRectF(0.5, 0.5, w - 1, h - 1), 14, 14)
        grad = QLinearGradient(0, 0, w, h)
        grad.setColorAt(0, QColor("#2a1d18"))
        grad.setColorAt(1, QColor("#1f2230"))
        p.fillPath(card, grad)
        p.setPen(QPen(QColor(ACCENT), 2))
        p.drawPath(card)
        p.setClipPath(card)

        # confetti: each piece falls from above the card to its resting place (ease-out), with a little sway
        cx = w / 2
        for fx, fy, size, angle, color, delay, round_ in self._confetti:
            x, rest = fx * w, fy * h
            if abs(x - cx) < 62 and rest > 22:      # keep the logo clear
                x += 62 if x >= cx else -62
            k = max(0.0, min(1.0, (self._t - delay) / (1.0 - delay))) if self._t < 1.0 else 1.0
            ease = 1 - (1 - k) ** 3
            y = -20 + (rest + 20) * ease
            sway = math.sin(k * 9 + fx * 6) * 6 * (1 - ease)
            p.save()
            p.translate(x + sway, y)
            p.rotate(angle + 360 * (1 - ease))
            p.setPen(Qt.PenStyle.NoPen)
            p.setBrush(QColor(color))
            if round_:
                p.drawEllipse(QPointF(0, 0), size / 2.6, size / 2.6)
            else:
                p.drawRect(QRectF(-size / 2, -size / 5, size, size / 2.5))
            p.restore()

        # the logo
        side = 88
        lx, ly = cx - side / 2, (h - side) / 2
        p.drawPixmap(QRectF(lx, ly, side, side).toRect(), self._logo)

        # the seal, stamped in during the last third of the animation
        k = max(0.0, min(1.0, (self._t - 0.62) / 0.38))
        if k > 0:
            scale = 1.7 - 0.7 * (1 - (1 - k) ** 3)
            r = 19 * scale
            sx, sy = lx + side - 6, ly + side - 8
            p.setOpacity(min(1.0, k * 1.6))
            p.setPen(QPen(QColor("#16181d"), 3))
            p.setBrush(QColor(SEAL))
            p.drawEllipse(QPointF(sx, sy), r, r)
            tick = QPainterPath()
            tick.moveTo(sx - r * 0.42, sy + r * 0.02)
            tick.lineTo(sx - r * 0.1, sy + r * 0.34)
            tick.lineTo(sx + r * 0.46, sy - r * 0.32)
            p.setPen(QPen(QColor("#ffffff"), max(2.0, r * 0.2), Qt.PenStyle.SolidLine,
                          Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
            p.setBrush(Qt.BrushStyle.NoBrush)
            p.drawPath(tick)
        p.end()


class StoreThanksDialog(QDialog):
    def __init__(self, parent=None, animate: bool = True) -> None:
        super().__init__(parent)
        self.setWindowTitle(tr("thanks.title"))
        self.setWindowIcon(winutil.app_icon())
        self.setStyleSheet(THANKS_QSS)
        self.setFixedWidth(480)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(20, 20, 20, 18)
        lay.setSpacing(12)
        lay.addWidget(_Banner(self, animate))

        heading = QLabel(tr("thanks.heading"))
        heading.setObjectName("heading")
        heading.setWordWrap(True)
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lay.addSpacing(4)
        lay.addWidget(heading)

        for key in ("thanks.p1", "thanks.p2"):
            # the Store name is what people search for: keep it on one line
            body = QLabel(tr(key).replace(store.STORE_NAME, store.STORE_NAME.replace(" ", " ")))
            body.setObjectName("body")
            body.setWordWrap(True)
            lay.addWidget(body)

        tip_box = QFrame()
        tip_box.setObjectName("tipBox")
        tip_lay = QVBoxLayout(tip_box)
        tip_lay.setContentsMargins(12, 9, 12, 9)
        tip = QLabel(tr("thanks.tip"))
        tip.setObjectName("tip")
        tip.setWordWrap(True)
        tip_lay.addWidget(tip)
        lay.addWidget(tip_box)

        # the signature: the name in a handwriting font, the role under it
        sign = QVBoxLayout()
        sign.setSpacing(0)
        name = QLabel("– Gábor")
        name.setObjectName("signName")
        name.setFont(QFont(["Segoe Script", "Ink Free", "Segoe Print"]))
        name.setAlignment(Qt.AlignmentFlag.AlignRight)
        role = QLabel(tr("thanks.role"))
        role.setObjectName("signRole")
        role.setAlignment(Qt.AlignmentFlag.AlignRight)
        sign.addWidget(name)
        sign.addWidget(role)
        lay.addLayout(sign)

        buttons = QHBoxLayout()
        buttons.setSpacing(8)
        stay = QPushButton(tr("thanks.btn_stay"))
        stay.setObjectName("stayButton")
        stay.clicked.connect(self.accept)
        go = QPushButton(tr("thanks.btn_store"))
        go.setObjectName("storeButton")
        go.setDefault(True)
        go.clicked.connect(self._go)
        buttons.addStretch(1)
        buttons.addWidget(stay)
        buttons.addWidget(go)
        lay.addSpacing(2)
        lay.addLayout(buttons)

        # wrapped labels: size the window to the text at its fixed width (no stray gaps between the paragraphs)
        self.ensurePolished()
        self.setFixedHeight(lay.totalHeightForWidth(self.width()))

    def _go(self) -> None:
        open_store()
        self.accept()
