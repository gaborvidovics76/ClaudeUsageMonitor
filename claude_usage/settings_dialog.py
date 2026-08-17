"""Beállítások ablak."""

from __future__ import annotations

import os
from typing import Optional

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QCheckBox,
    QColorDialog,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QSlider,
    QSpinBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from . import winutil
from .datasource import default_data_path
from .settings import APP_TITLE, Settings, config_dir
from .i18n import tr
from .theme import THEMES, rgba_to_hex

LAYOUTS = [("postit", "Post-it kártya"), ("compact", "Vékony sáv"), ("ring", "Körgyűrűk")]
TRAY_METRICS = [("five_hour", "5 órás ablak"), ("weekly", "Heti keret"), ("max", "Amelyik magasabb")]

DIALOG_QSS = """
QDialog { background: #16181d; }
QTabWidget::pane { border: 1px solid #2c313b; border-radius: 10px; top: -1px; background: #1b1e25; }
QTabBar::tab { background: transparent; color: #99a1b3; padding: 7px 14px; margin-right: 2px;
               border-top-left-radius: 8px; border-top-right-radius: 8px; }
QTabBar::tab:selected { background: #1b1e25; color: #f0f3fa; border: 1px solid #2c313b; border-bottom: none; }
QLabel { color: #c9cfdd; }
QLabel#hint { color: #79839a; }
QLabel#section { color: #7f8aa3; font-weight: 600; }
QCheckBox { color: #d6dbe8; spacing: 8px; }
QComboBox, QLineEdit, QSpinBox { background: #23272f; color: #eef1f8; border: 1px solid #333944;
                                 border-radius: 7px; padding: 5px 8px; selection-background-color: #4d7cff; }
QComboBox::drop-down { border: none; width: 18px; }
QComboBox QAbstractItemView { background: #23272f; color: #eef1f8; selection-background-color: #38414f;
                              border: 1px solid #333944; outline: none; }
QPushButton { background: #262b34; color: #e6eaf3; border: 1px solid #343b47; border-radius: 8px; padding: 6px 14px; }
QPushButton:hover { background: #2f3540; }
QPushButton:pressed { background: #232830; }
QSlider::groove:horizontal { height: 4px; background: #333944; border-radius: 2px; }
QSlider::handle:horizontal { background: #d0d6e4; width: 14px; margin: -6px 0; border-radius: 7px; }
QSlider::sub-page:horizontal { background: #6f8dff; border-radius: 2px; }
"""


class SettingsDialog(QDialog):
    changed = Signal()
    resetRequested = Signal()
    loginRequested = Signal()
    logoutRequested = Signal()

    def __init__(self, settings: Settings, orgs, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.s = settings
        self._loading = True
        self.setWindowTitle(f"{APP_TITLE} – " + tr("set.title"))
        self.setWindowIcon(winutil.app_icon())
        self.setStyleSheet(DIALOG_QSS)
        self.setMinimumWidth(430)

        tabs = QTabWidget(self)
        tabs.addTab(self._tab_appearance(), tr("set.tab_appearance"))
        tabs.addTab(self._tab_content(), tr("set.tab_content"))
        tabs.addTab(self._tab_alerts(), tr("set.tab_alerts"))
        tabs.addTab(self._tab_data(orgs), tr("set.tab_data"))
        tabs.addTab(self._tab_system(), tr("set.tab_system"))

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close, self)
        buttons.button(QDialogButtonBox.StandardButton.Close).setText(tr("set.close"))
        buttons.rejected.connect(self.accept)
        buttons.accepted.connect(self.accept)

        root = QVBoxLayout(self)
        root.setContentsMargins(14, 14, 14, 12)
        root.setSpacing(10)
        root.addWidget(tabs)
        root.addWidget(buttons)

        self._loading = False

    # ------------------------------------------------------------- segédek

    @staticmethod
    def _page():
        page = QWidget()
        form = QFormLayout(page)
        form.setContentsMargins(14, 14, 14, 14)
        form.setSpacing(9)
        form.setLabelAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        return page, form

    def _check(self, key: str, text: str) -> QCheckBox:
        cb = QCheckBox(text)
        cb.setChecked(bool(self.s[key]))
        cb.toggled.connect(lambda v, k=key: self._set(k, v))
        return cb

    def _slider(self, key: str, lo: int, hi: int, factor: float, suffix: str):
        box = QWidget()
        lay = QHBoxLayout(box)
        lay.setContentsMargins(0, 0, 0, 0)
        sl = QSlider(Qt.Orientation.Horizontal)
        sl.setRange(lo, hi)
        sl.setValue(int(round(float(self.s[key]) / factor)))
        lbl = QLabel()
        lbl.setMinimumWidth(46)
        lbl.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        def on_change(v: int) -> None:
            lbl.setText(f"{v * factor:.2f}".rstrip("0").rstrip(".") + suffix)
            self._set(key, round(v * factor, 2))

        sl.valueChanged.connect(on_change)
        on_change(sl.value())
        lay.addWidget(sl, 1)
        lay.addWidget(lbl)
        return box

    def _set(self, key: str, value) -> None:
        if self._loading:
            return
        self.s[key] = value
        self.s.save()
        self.changed.emit()

    # --------------------------------------------------------------- lapok

    def _tab_appearance(self) -> QWidget:
        page, form = self._page()

        self.cb_theme = QComboBox()
        for key in THEMES:
            self.cb_theme.addItem(tr("theme." + key), key)
        idx = self.cb_theme.findData(self.s["theme"])
        self.cb_theme.setCurrentIndex(max(0, idx))
        self.cb_theme.currentIndexChanged.connect(
            lambda: self._set("theme", self.cb_theme.currentData()))
        form.addRow(tr("set.theme"), self.cb_theme)

        accent_box = QWidget()
        alay = QHBoxLayout(accent_box)
        alay.setContentsMargins(0, 0, 0, 0)
        self.btn_accent = QPushButton(tr("set.pick_color"))
        self.btn_accent.clicked.connect(self._pick_accent)
        btn_clear = QPushButton(tr("set.default"))
        btn_clear.clicked.connect(lambda: (self._set("accent", ""), self._refresh_accent()))
        alay.addWidget(self.btn_accent, 1)
        alay.addWidget(btn_clear)
        form.addRow(tr("set.accent"), accent_box)
        self._refresh_accent()

        self.cb_layout = QComboBox()
        for key, _label in LAYOUTS:
            self.cb_layout.addItem(tr("layout." + key), key)
        self.cb_layout.setCurrentIndex(max(0, self.cb_layout.findData(self.s["layout"])))
        self.cb_layout.currentIndexChanged.connect(
            lambda: self._set("layout", self.cb_layout.currentData()))
        form.addRow(tr("set.layout"), self.cb_layout)

        form.addRow(tr("set.size"), self._slider("scale", 70, 200, 0.01, "×"))
        form.addRow(tr("set.opacity"), self._slider("opacity", 25, 100, 0.01, ""))

        form.addRow("", self._check("visible", tr("set.visible")))
        form.addRow("", self._check("always_on_top", tr("set.always_top")))
        form.addRow("", self._check("locked", tr("set.lock")))
        form.addRow("", self._check("snap_edges", tr("set.snap")))
        form.addRow("", self._check("show_in_taskbar", tr("set.taskbar")))
        ct = self._check("click_through", tr("set.click_through"))
        form.addRow("", ct)

        hint = QLabel(tr("set.tip"))
        hint.setObjectName("hint")
        form.addRow("", hint)
        return page

    def _refresh_accent(self) -> None:
        value = self.s["accent"]
        self.btn_accent.setText(value.upper() if value else tr("set.theme_default"))

    def _pick_accent(self) -> None:
        current = QColor(self.s["accent"] or "#7AA2FF")
        color = QColorDialog.getColor(current, self, tr("set.accent"))
        if color.isValid():
            self._set("accent", color.name())
            self._refresh_accent()

    def _tab_content(self) -> QWidget:
        page, form = self._page()
        form.addRow("", self._check("show_five_hour", tr("set.show_five_hour")))
        form.addRow("", self._check("show_weekly", tr("set.show_weekly")))
        form.addRow("", self._check("show_spark", tr("set.show_spark")))
        form.addRow("", self._check("show_burn", tr("set.show_burn")))
        form.addRow("", self._check("show_reset", tr("set.show_reset")))
        form.addRow("", self._check("show_age", tr("set.show_age")))

        self.cb_tray = QComboBox()
        _tm = {"five_hour": "five", "weekly": "weekly", "max": "max"}
        for key, _label in TRAY_METRICS:
            self.cb_tray.addItem(tr("set.tray_" + _tm[key]), key)
        self.cb_tray.setCurrentIndex(max(0, self.cb_tray.findData(self.s["tray_metric"])))
        self.cb_tray.currentIndexChanged.connect(
            lambda: self._set("tray_metric", self.cb_tray.currentData()))
        form.addRow(tr("set.tray_value"), self.cb_tray)
        return page

    def _tab_alerts(self) -> QWidget:
        page, form = self._page()

        self.sp_warn = QSpinBox()
        self.sp_warn.setRange(1, 99)
        self.sp_warn.setSuffix(" %")
        self.sp_warn.setValue(int(self.s["warn_threshold"]))
        self.sp_warn.valueChanged.connect(lambda v: self._set("warn_threshold", v))
        form.addRow(tr("set.warn"), self.sp_warn)

        self.sp_danger = QSpinBox()
        self.sp_danger.setRange(2, 100)
        self.sp_danger.setSuffix(" %")
        self.sp_danger.setValue(int(self.s["danger_threshold"]))
        self.sp_danger.valueChanged.connect(lambda v: self._set("danger_threshold", v))
        form.addRow(tr("set.danger"), self.sp_danger)

        form.addRow("", self._check("notify_enabled", tr("set.notify_enabled")))
        form.addRow("", self._check("notify_on_reset", tr("set.notify_reset")))
        form.addRow("", self._check("notify_stale", tr("set.notify_stale")))

        hint = QLabel(tr("set.color_hint"))
        hint.setObjectName("hint")
        form.addRow("", hint)
        return page

    def _tab_data(self, orgs) -> QWidget:
        page, form = self._page()

        from . import secretstore

        self.cb_source = QComboBox()
        self.cb_source.addItem(tr("set.source_local"), "local")
        self.cb_source.addItem(tr("set.source_api"), "api")
        self.cb_source.setCurrentIndex(max(0, self.cb_source.findData(self.s["source"])))
        self.cb_source.currentIndexChanged.connect(self._on_source_changed)
        form.addRow(tr("set.source_label"), self.cb_source)

        login_box = QWidget()
        llay = QHBoxLayout(login_box)
        llay.setContentsMargins(0, 0, 0, 0)
        self.btn_login = QPushButton()
        self.btn_login.clicked.connect(self._on_login_clicked)
        llay.addWidget(self.btn_login, 1)
        form.addRow("claude.ai", login_box)
        self._refresh_login_button()

        self.cb_org = QComboBox()
        self.cb_org.addItem(tr("set.profile_auto"), "")
        for i, org in enumerate(orgs):
            label = tr("set.profile_n", i + 1, org[-8:]) if org else org
            self.cb_org.addItem(label, org)
        self.cb_org.setCurrentIndex(max(0, self.cb_org.findData(self.s["org"])))
        self.cb_org.currentIndexChanged.connect(lambda: self._set("org", self.cb_org.currentData()))
        form.addRow(tr("set.profile"), self.cb_org)

        self.sp_refresh = QSpinBox()
        self.sp_refresh.setRange(2, 120)
        self.sp_refresh.setSuffix(tr("set.sec_suffix"))
        self.sp_refresh.setValue(int(self.s["refresh_seconds"]))
        self.sp_refresh.valueChanged.connect(lambda v: self._set("refresh_seconds", v))
        form.addRow(tr("set.refresh"), self.sp_refresh)

        path_box = QWidget()
        play = QHBoxLayout(path_box)
        play.setContentsMargins(0, 0, 0, 0)
        self.ed_path = QLineEdit(self.s["data_path"])
        self.ed_path.setPlaceholderText(default_data_path())
        self.ed_path.editingFinished.connect(lambda: self._set("data_path", self.ed_path.text().strip()))
        btn = QPushButton("…")
        btn.setFixedWidth(34)
        btn.clicked.connect(self._pick_path)
        play.addWidget(self.ed_path, 1)
        play.addWidget(btn)
        form.addRow(tr("set.datafile"), path_box)

        info = QLabel(
            "Helyi napló: a Claude Desktop plan-usage-history.json fájlja. Nem kell\n"
            "bejelentkezés, de csak ezt a gépet méri, és kb. 5 percenként frissül.\n\n"
            "claude.ai: a beépített bejelentkezés után a szerverről kérdez le. Minden\n"
            "eszközöd használatát látod, pontos reset-időkkel, gyakoribb frissítéssel."
        )
        info.setObjectName("hint")
        form.addRow("", info)
        return page

    def _refresh_login_button(self) -> None:
        from . import secretstore

        if secretstore.has_secret():
            self.btn_login.setText(tr("set.login_btn_in"))
        else:
            self.btn_login.setText(tr("set.login_btn_out"))

    def _on_login_clicked(self) -> None:
        from . import secretstore

        if secretstore.has_secret():
            self.logoutRequested.emit()
        else:
            self.loginRequested.emit()
        self._refresh_login_button()
        idx = max(0, self.cb_source.findData(self.s["source"]))
        self.cb_source.setCurrentIndex(idx)

    def _on_source_changed(self) -> None:
        from . import secretstore

        source = self.cb_source.currentData()
        if source == "api" and not secretstore.has_secret():
            self.loginRequested.emit()
            self._refresh_login_button()
            if not secretstore.has_secret():
                self.cb_source.setCurrentIndex(self.cb_source.findData("local"))
                return
        self._set("source", source)

    def _pick_path(self) -> None:
        start = self.s["data_path"] or default_data_path()
        path, _ = QFileDialog.getOpenFileName(self, tr("set.pick_file_title"),
                                              start, tr("set.file_filter"))
        if path:
            self.ed_path.setText(path)
            self._set("data_path", path)

    def _tab_system(self) -> QWidget:
        page, form = self._page()

        self.cb_auto = QCheckBox(tr("menu.autostart"))
        self.cb_auto.setChecked(winutil.autostart_enabled())
        self.cb_auto.toggled.connect(self._toggle_autostart)
        form.addRow("", self.cb_auto)

        btn_dir = QPushButton(tr("set.open_config"))
        btn_dir.clicked.connect(lambda: os.startfile(config_dir()))
        form.addRow("", btn_dir)

        btn_reset = QPushButton(tr("set.restore"))
        btn_reset.clicked.connect(self._reset)
        form.addRow("", btn_reset)

        about = QLabel(tr("set.about", APP_TITLE))
        about.setObjectName("hint")
        form.addRow("", about)
        return page

    def _toggle_autostart(self, value: bool) -> None:
        if not winutil.set_autostart(value):
            QMessageBox.warning(self, APP_TITLE, tr("notify.autostart_fail"))
            return
        self._set("autostart", value)

    def _reset(self) -> None:
        if QMessageBox.question(self, APP_TITLE, tr("set.reset_confirm")) \
                == QMessageBox.StandardButton.Yes:
            self.resetRequested.emit()
            self.accept()
