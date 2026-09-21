"""Help window: a detailed guide and the author card with the official website (claudeusagemonitor.com)."""

from __future__ import annotations

import html
from typing import Optional

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFrame,
    QLabel,
    QPushButton,
    QTabWidget,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from . import __version__, winutil
from .i18n import current_language, tr
from .settings import APP_TITLE, config_dir
from .settings_dialog import DIALOG_QSS

SITE = "https://claudeusagemonitor.com/"
REPO = "https://github.com/gaborvidovics76/ClaudeUsageMonitor"
AUTHOR = "Vidovics Gábor"
ACCENT = "#D97757"          # the Claude orange of the app icon

HELP_QSS = DIALOG_QSS + f"""
QTextBrowser {{ background: #1b1e25; color: #d6dbe8; border: none; }}
QFrame#siteCard {{ background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #2a1d18, stop:1 #1f2230);
                   border: 2px solid {ACCENT}; border-radius: 14px; }}
QLabel#siteKicker {{ color: {ACCENT}; font-weight: 700; letter-spacing: 2px; font-size: 11px; }}
QLabel#siteName {{ color: #ffffff; font-size: 26px; font-weight: 800; }}
QLabel#siteWhat {{ color: #d9dde8; }}
QLabel#siteMoved {{ color: #f3c9b8; font-size: 12px; }}
QPushButton#siteButton {{ background: {ACCENT}; color: #ffffff; border: none; border-radius: 9px;
                          padding: 9px 18px; font-weight: 700; }}
QPushButton#siteButton:hover {{ background: #e5896b; }}
QLabel#appName {{ color: #f0f3fa; font-size: 16px; font-weight: 700; }}
QLabel a {{ color: #8fb0ff; }}
"""


def site_url(lang: Optional[str] = None) -> str:
    """The website in the program's language (/ = English, /hu/, /de/ …)."""
    lang = lang or current_language()
    return SITE if lang in ("", "en") else f"{SITE}{lang}/"


def _link(url: str, text: str) -> str:
    return f'<a href="{html.escape(url)}" style="color:#8fb0ff;">{html.escape(text)}</a>'


class HelpDialog(QDialog):
    def __init__(self, parent: Optional[QWidget] = None, start_tab: int = 0):
        super().__init__(parent)
        self.setWindowTitle(f"{APP_TITLE} – " + tr("help.title"))
        self.setWindowIcon(winutil.app_icon())
        self.setStyleSheet(HELP_QSS)
        self.resize(640, 620)

        self.tabs = QTabWidget(self)
        self.tabs.addTab(self._tab_guide(), tr("help.tab_guide"))
        self.tabs.addTab(self._tab_author(), tr("help.tab_author"))
        self.tabs.setCurrentIndex(start_tab)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close, self)
        buttons.button(QDialogButtonBox.StandardButton.Close).setText(tr("set.close"))
        buttons.rejected.connect(self.accept)

        root = QVBoxLayout(self)
        root.setContentsMargins(14, 14, 14, 12)
        root.setSpacing(10)
        root.addWidget(self.tabs)
        root.addWidget(buttons)

    # ------------------------------------------------------------------ guide

    def _tab_guide(self) -> QWidget:
        page = QWidget()
        lay = QVBoxLayout(page)
        lay.setContentsMargins(6, 6, 6, 6)
        view = QTextBrowser(page)
        view.setOpenExternalLinks(True)
        body = (tr("help.guide")
                .replace("{site}", _link(site_url(), "claudeusagemonitor.com"))
                .replace("{cfg}", html.escape(config_dir())))
        view.setHtml('<style>h2{color:#f0f3fa;font-size:15px;margin:14px 0 4px 0;} li{margin:3px 0;} '
                     'code{color:#f3c9b8;}</style>' + body)
        lay.addWidget(view)
        return page

    # ------------------------------------------------------------------ author

    def _tab_author(self) -> QWidget:
        page = QWidget()
        lay = QVBoxLayout(page)
        lay.setContentsMargins(16, 16, 16, 16)
        lay.setSpacing(12)

        # the official website - the highlighted part of the tab
        card = QFrame(page)
        card.setObjectName("siteCard")
        c = QVBoxLayout(card)
        c.setContentsMargins(20, 16, 20, 18)
        c.setSpacing(6)
        kicker = QLabel(tr("help.official"), card)
        kicker.setObjectName("siteKicker")
        name = QLabel(f'<a href="{site_url()}" style="color:#ffffff;text-decoration:none;">claudeusagemonitor.com</a>', card)
        name.setObjectName("siteName")
        name.setOpenExternalLinks(True)
        name.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        what = QLabel(tr("help.site_what"), card)
        what.setObjectName("siteWhat")
        what.setWordWrap(True)
        moved = QLabel("↪ " + tr("help.moved"), card)
        moved.setObjectName("siteMoved")
        moved.setWordWrap(True)
        button = QPushButton(tr("help.open_site"), card)
        button.setObjectName("siteButton")
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(site_url())))
        for w in (kicker, name, what, moved):
            c.addWidget(w)
        c.addSpacing(6)
        c.addWidget(button, 0, Qt.AlignmentFlag.AlignLeft)
        lay.addWidget(card)

        app = QLabel(f"{APP_TITLE} · {tr('help.version')} {__version__}", page)
        app.setObjectName("appName")
        lay.addWidget(app)

        info = QLabel(page)
        info.setWordWrap(True)
        info.setOpenExternalLinks(True)
        info.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        info.setText(
            f"{html.escape(tr('help.made_by'))}: <b>{html.escape(AUTHOR)}</b><br>"
            f"{html.escape(tr('help.free'))}<br><br>"
            f"{_link(REPO, tr('help.source_code'))} &nbsp;·&nbsp; "
            f"{_link(site_url() + '#terms', tr('help.terms'))} &nbsp;·&nbsp; "
            f"{_link(site_url() + '#privacy', tr('help.privacy'))}<br><br>"
            f"{html.escape(tr('help.feedback'))}"
        )
        lay.addWidget(info)

        note = QLabel(tr("help.disclaimer"), page)
        note.setObjectName("hint")
        note.setWordWrap(True)
        lay.addWidget(note)
        lay.addStretch(1)
        return page
