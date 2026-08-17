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
        self.setWindowTitle(f"{APP_TITLE} – beállítások")
        self.setWindowIcon(winutil.app_icon())
        self.setStyleSheet(DIALOG_QSS)
        self.setMinimumWidth(430)

        tabs = QTabWidget(self)
        tabs.addTab(self._tab_appearance(), "Megjelenés")
        tabs.addTab(self._tab_content(), "Tartalom")
        tabs.addTab(self._tab_alerts(), "Riasztások")
        tabs.addTab(self._tab_data(orgs), "Adatforrás")
        tabs.addTab(self._tab_system(), "Rendszer")

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close, self)
        buttons.button(QDialogButtonBox.StandardButton.Close).setText("Bezárás")
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
        for key, data in THEMES.items():
            self.cb_theme.addItem(str(data["label"]), key)
        idx = self.cb_theme.findData(self.s["theme"])
        self.cb_theme.setCurrentIndex(max(0, idx))
        self.cb_theme.currentIndexChanged.connect(
            lambda: self._set("theme", self.cb_theme.currentData()))
        form.addRow("Téma", self.cb_theme)

        accent_box = QWidget()
        alay = QHBoxLayout(accent_box)
        alay.setContentsMargins(0, 0, 0, 0)
        self.btn_accent = QPushButton("Szín választása…")
        self.btn_accent.clicked.connect(self._pick_accent)
        btn_clear = QPushButton("Alap")
        btn_clear.setFixedWidth(56)
        btn_clear.clicked.connect(lambda: (self._set("accent", ""), self._refresh_accent()))
        alay.addWidget(self.btn_accent, 1)
        alay.addWidget(btn_clear)
        form.addRow("Kiemelőszín", accent_box)
        self._refresh_accent()

        self.cb_layout = QComboBox()
        for key, label in LAYOUTS:
            self.cb_layout.addItem(label, key)
        self.cb_layout.setCurrentIndex(max(0, self.cb_layout.findData(self.s["layout"])))
        self.cb_layout.currentIndexChanged.connect(
            lambda: self._set("layout", self.cb_layout.currentData()))
        form.addRow("Elrendezés", self.cb_layout)

        form.addRow("Méret", self._slider("scale", 70, 200, 0.01, "×"))
        form.addRow("Átlátszatlanság", self._slider("opacity", 25, 100, 0.01, ""))

        form.addRow("", self._check("visible", "Lebegő panel látszik"))
        form.addRow("", self._check("always_on_top", "Mindig a többi ablak felett"))
        form.addRow("", self._check("locked", "Pozíció rögzítése (nem húzható)"))
        form.addRow("", self._check("snap_edges", "Tapadás a képernyő széléhez"))
        form.addRow("", self._check("show_in_taskbar", "Megjelenés a tálcán (ablakként)"))
        ct = self._check("click_through", "Kattintás-átengedés (csak dísz, nem fogad egeret)")
        form.addRow("", ct)

        hint = QLabel("Tipp: a panelt bal gombbal húzhatod, Ctrl+görgő méretez,\n"
                      "jobb gomb = menü, dupla kattintás = előzmények.")
        hint.setObjectName("hint")
        form.addRow("", hint)
        return page

    def _refresh_accent(self) -> None:
        value = self.s["accent"]
        self.btn_accent.setText(value.upper() if value else "Téma szerinti")

    def _pick_accent(self) -> None:
        current = QColor(self.s["accent"] or "#7AA2FF")
        color = QColorDialog.getColor(current, self, "Kiemelőszín")
        if color.isValid():
            self._set("accent", color.name())
            self._refresh_accent()

    def _tab_content(self) -> QWidget:
        page, form = self._page()
        form.addRow("", self._check("show_five_hour", "5 órás ablak mutatása"))
        form.addRow("", self._check("show_weekly", "Heti keret mutatása"))
        form.addRow("", self._check("show_spark", "Trendgörbe (sparkline)"))
        form.addRow("", self._check("show_burn", "Fogyási ütem (%/óra, %/nap)"))
        form.addRow("", self._check("show_reset", "Visszaszámlálás a resetig"))
        form.addRow("", self._check("show_age", "Adat frissessége"))

        self.cb_tray = QComboBox()
        for key, label in TRAY_METRICS:
            self.cb_tray.addItem(label, key)
        self.cb_tray.setCurrentIndex(max(0, self.cb_tray.findData(self.s["tray_metric"])))
        self.cb_tray.currentIndexChanged.connect(
            lambda: self._set("tray_metric", self.cb_tray.currentData()))
        form.addRow("Tálcaikon értéke", self.cb_tray)
        return page

    def _tab_alerts(self) -> QWidget:
        page, form = self._page()

        self.sp_warn = QSpinBox()
        self.sp_warn.setRange(1, 99)
        self.sp_warn.setSuffix(" %")
        self.sp_warn.setValue(int(self.s["warn_threshold"]))
        self.sp_warn.valueChanged.connect(lambda v: self._set("warn_threshold", v))
        form.addRow("Figyelmeztetés", self.sp_warn)

        self.sp_danger = QSpinBox()
        self.sp_danger.setRange(2, 100)
        self.sp_danger.setSuffix(" %")
        self.sp_danger.setValue(int(self.s["danger_threshold"]))
        self.sp_danger.valueChanged.connect(lambda v: self._set("danger_threshold", v))
        form.addRow("Vészjelzés", self.sp_danger)

        form.addRow("", self._check("notify_enabled", "Értesítés a küszöbök átlépésekor"))
        form.addRow("", self._check("notify_on_reset", "Értesítés, ha egy keret lenullázódott"))
        form.addRow("", self._check("notify_stale", "Értesítés, ha elavul az adat"))

        hint = QLabel("A színek a küszöbök szerint váltanak: zöld → sárga → piros.")
        hint.setObjectName("hint")
        form.addRow("", hint)
        return page

    def _tab_data(self, orgs) -> QWidget:
        page, form = self._page()

        from . import secretstore

        self.cb_source = QComboBox()
        self.cb_source.addItem("Helyi napló – csak ez a gép", "local")
        self.cb_source.addItem("claude.ai – minden eszköz (bejelentkezés kell)", "api")
        self.cb_source.setCurrentIndex(max(0, self.cb_source.findData(self.s["source"])))
        self.cb_source.currentIndexChanged.connect(self._on_source_changed)
        form.addRow("Mérés forrása", self.cb_source)

        login_box = QWidget()
        llay = QHBoxLayout(login_box)
        llay.setContentsMargins(0, 0, 0, 0)
        self.btn_login = QPushButton()
        self.btn_login.clicked.connect(self._on_login_clicked)
        llay.addWidget(self.btn_login, 1)
        form.addRow("claude.ai", login_box)
        self._refresh_login_button()

        self.cb_org = QComboBox()
        self.cb_org.addItem("Automatikus (legutóbb használt)", "")
        for i, org in enumerate(orgs):
            label = f"Profil {i + 1} – …{org[-8:]}" if org else org
            self.cb_org.addItem(label, org)
        self.cb_org.setCurrentIndex(max(0, self.cb_org.findData(self.s["org"])))
        self.cb_org.currentIndexChanged.connect(lambda: self._set("org", self.cb_org.currentData()))
        form.addRow("Profil / fiók", self.cb_org)

        self.sp_refresh = QSpinBox()
        self.sp_refresh.setRange(2, 120)
        self.sp_refresh.setSuffix(" mp")
        self.sp_refresh.setValue(int(self.s["refresh_seconds"]))
        self.sp_refresh.valueChanged.connect(lambda v: self._set("refresh_seconds", v))
        form.addRow("Frissítés", self.sp_refresh)

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
        form.addRow("Adatfájl", path_box)

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
            self.btn_login.setText("Kijelentkezés a claude.ai-ról")
        else:
            self.btn_login.setText("Bejelentkezés a claude.ai-ra…")

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
        path, _ = QFileDialog.getOpenFileName(self, "Használati napló kiválasztása",
                                              start, "JSON (*.json);;Minden fájl (*.*)")
        if path:
            self.ed_path.setText(path)
            self._set("data_path", path)

    def _tab_system(self) -> QWidget:
        page, form = self._page()

        self.cb_auto = QCheckBox("Induljon a Windowsszal")
        self.cb_auto.setChecked(winutil.autostart_enabled())
        self.cb_auto.toggled.connect(self._toggle_autostart)
        form.addRow("", self.cb_auto)

        btn_dir = QPushButton("Beállítások mappa megnyitása")
        btn_dir.clicked.connect(lambda: os.startfile(config_dir()))
        form.addRow("", btn_dir)

        btn_reset = QPushButton("Alapértelmezések visszaállítása")
        btn_reset.clicked.connect(self._reset)
        form.addRow("", btn_reset)

        about = QLabel(f"{APP_TITLE}\nHelyi adatokból dolgozik, semmit nem küld sehova.")
        about.setObjectName("hint")
        form.addRow("", about)
        return page

    def _toggle_autostart(self, value: bool) -> None:
        if not winutil.set_autostart(value):
            QMessageBox.warning(self, APP_TITLE, "Az automatikus indítást nem sikerült beállítani.")
            return
        self._set("autostart", value)

    def _reset(self) -> None:
        if QMessageBox.question(self, APP_TITLE, "Biztosan visszaállítod az alapértelmezett beállításokat?") \
                == QMessageBox.StandardButton.Yes:
            self.resetRequested.emit()
            self.accept()
