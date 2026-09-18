"""Update window: shows the installed / available version, the notes, and drives the install."""

from __future__ import annotations

import html
from typing import Optional

from PySide6.QtCore import QTimer, Qt, QUrl, Signal
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QPushButton,
    QTextBrowser,
    QVBoxLayout,
)

from . import __version__, winutil
from .i18n import current_language, tr
from .settings import APP_TITLE
from .updater import Updater, can_self_update

QSS = """
QDialog { background: #16181d; }
QLabel { color: #c9cfdd; }
QLabel#big { color: #f0f3fa; font-size: 14px; font-weight: 600; }
QLabel#dim { color: #79839a; }
QTextBrowser { background: #1b1e25; color: #c9cfdd; border: 1px solid #2c313b; border-radius: 8px; padding: 6px; }
QProgressBar { background: #23272f; border: 1px solid #333944; border-radius: 6px; height: 12px; text-align: center; color: #dfe4ee; }
QProgressBar::chunk { background: #6f8dff; border-radius: 5px; }
QPushButton { background: #262b34; color: #e6eaf3; border: 1px solid #343b47; border-radius: 8px; padding: 6px 14px; }
QPushButton:hover { background: #2f3540; }
QPushButton:disabled { color: #6b7385; }
QPushButton#primary { background: #3b5bdb; border-color: #4c6ef5; color: white; }
QPushButton#primary:hover { background: #4263eb; }
"""


def _mb(n: int) -> str:
    return f"{n / 1048576:.1f} MB"


class UpdateDialog(QDialog):
    skipRequested = Signal(str)
    quitRequested = Signal()

    def __init__(self, updater: Updater, parent=None):
        super().__init__(parent)
        self.up = updater
        self._seen = -1
        self._applied = False
        self.setWindowTitle(f"{APP_TITLE} – " + tr("update.title"))
        self.setWindowIcon(winutil.app_icon())
        self.setStyleSheet(QSS)
        self.resize(520, 400)

        self.lbl_state = QLabel()
        self.lbl_state.setObjectName("big")
        self.lbl_state.setWordWrap(True)
        self.lbl_installed = QLabel(tr("update.installed", __version__))
        self.lbl_installed.setObjectName("dim")
        self.notes = QTextBrowser()
        self.notes.setOpenExternalLinks(True)
        self.bar = QProgressBar()
        self.bar.setRange(0, 1000)
        self.bar.setTextVisible(False)
        self.lbl_progress = QLabel()
        self.lbl_progress.setObjectName("dim")
        self.lbl_progress.setWordWrap(True)

        self.btn_install = QPushButton(tr("update.install"))
        self.btn_install.setObjectName("primary")
        self.btn_install.clicked.connect(self._install)
        self.btn_skip = QPushButton(tr("update.skip"))
        self.btn_skip.clicked.connect(self._skip)
        self.btn_check = QPushButton(tr("update.check_now"))
        self.btn_check.clicked.connect(lambda: self.up.check())
        self.btn_page = QPushButton(tr("update.open_page"))
        self.btn_page.clicked.connect(self._open_page)
        self.btn_close = QPushButton(tr("update.later"))
        self.btn_close.clicked.connect(self.close)

        buttons = QHBoxLayout()
        buttons.addWidget(self.btn_check)
        buttons.addWidget(self.btn_page)
        buttons.addStretch(1)
        buttons.addWidget(self.btn_skip)
        buttons.addWidget(self.btn_close)
        buttons.addWidget(self.btn_install)

        root = QVBoxLayout(self)
        root.setContentsMargins(16, 16, 16, 12)
        root.setSpacing(8)
        root.addWidget(self.lbl_state)
        root.addWidget(self.lbl_installed)
        root.addWidget(self.notes, 1)
        root.addWidget(self.bar)
        root.addWidget(self.lbl_progress)
        root.addLayout(buttons)

        self.timer = QTimer(self)
        self.timer.setInterval(150)
        self.timer.timeout.connect(self.sync)
        self.timer.start()
        self.sync(force=True)

    # ------------------------------------------------------------------ actions

    def _install(self) -> None:
        if not self.up.start_install():
            self.sync(force=True)

    def _skip(self) -> None:
        if self.up.info is not None:
            self.skipRequested.emit(self.up.info.version)
        self.close()

    def _open_page(self) -> None:
        info = self.up.info
        url = (info.page if info and info.page.startswith("https://") else "") or \
            self.up.manifest_url.rsplit("/", 1)[0] + "/"
        if url.startswith("https://"):
            QDesktopServices.openUrl(QUrl(url))

    # ------------------------------------------------------------------ state

    def sync(self, force: bool = False) -> None:
        if not force and self.up.counter == self._seen:
            return
        self._seen = self.up.counter
        state, info = self.up.state, self.up.info
        can, _why = can_self_update()

        text = {
            "idle": tr("update.checking"),
            "checking": tr("update.checking"),
            "uptodate": tr("update.uptodate"),
            "error": tr("update.check_failed", self.up.error),
            "failed": tr("update.failed", self.up.error),
            "ready": tr("update.restarting"),
        }.get(state)
        if state in ("available", "downloading") and info is not None:
            text = tr("update.available", info.version)
        if state == "failed" and self.up.error in ("source", "readonly"):
            text = tr("update.manual")
        self.lbl_state.setText(text or "")

        lines = info.notes_for(current_language()) if info is not None else []
        if lines and state in ("available", "downloading", "ready", "failed", "uptodate"):
            body = "".join(f"<li>{html.escape(x)}</li>" for x in lines)
            self.notes.setHtml(f"<b>{html.escape(tr('update.whats_new'))} – {html.escape(info.version)}</b>"
                               f"<ul style='margin-left:-18px'>{body}</ul>")
            self.notes.setVisible(True)
        else:
            self.notes.setVisible(bool(lines))

        downloading = state == "downloading"
        self.bar.setVisible(downloading or state == "ready")
        self.lbl_progress.setVisible(downloading or state == "ready")
        if downloading:
            done, total = self.up.progress
            if total > 0:
                self.bar.setRange(0, 1000)
                self.bar.setValue(int(done * 1000 / total))
                self.lbl_progress.setText(tr("update.downloading", _mb(done), _mb(total))
                                          if done < total else tr("update.verifying"))
            else:
                self.bar.setRange(0, 0)
                self.lbl_progress.setText(tr("update.downloading", _mb(done), "?"))
        elif state == "ready":
            self.bar.setRange(0, 1000)
            self.bar.setValue(1000)
            self.lbl_progress.setText(tr("update.restarting"))

        available = state == "available"
        self.btn_install.setVisible(available and can)
        self.btn_skip.setVisible(available)
        self.btn_page.setVisible((available and not can) or state == "failed")
        self.btn_check.setVisible(state in ("uptodate", "error", "failed"))
        self.btn_check.setEnabled(not self.up.busy)
        self.btn_close.setEnabled(state not in ("downloading", "ready"))
        if available and not can:
            self.lbl_progress.setVisible(True)
            self.lbl_progress.setText(tr("update.manual"))

        if state == "ready" and not self._applied:
            self._applied = True
            try:
                self.up.apply_and_restart()
            except Exception as exc:  # noqa: BLE001
                self.up.state, self.up.error = "failed", str(exc)
                self._applied = False
                self.sync(force=True)
                return
            QTimer.singleShot(900, self.quitRequested.emit)

    def closeEvent(self, e) -> None:
        if self.up.state == "downloading":
            self.up.cancel()
        super().closeEvent(e)
