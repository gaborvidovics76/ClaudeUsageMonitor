"""Settings window."""

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
from .settings import GAUGE_ORDERS, APP_TITLE, Settings, config_dir
from .i18n import tr
from .theme import THEMES, rgba_to_hex

LAYOUTS = [("postit", "Post-it card"), ("compact", "Slim bar"), ("ring", "Rings")]
TRAY_METRICS = [("five_hour", "5-hour window"), ("weekly", "Weekly limit"), ("max", "Whichever is higher")]

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
    updateRequested = Signal()
    logoutRequested = Signal()

    def __init__(self, settings: Settings, orgs, parent: Optional[QWidget] = None, rows=None):
        self._detail_rows = list(rows or [])        # (id, label) of what the server reports now
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
        tabs.addTab(self._tab_details(), tr("set.tab_details"))
        tabs.addTab(self._tab_alerts(), tr("set.tab_alerts"))
        tabs.addTab(self._tab_data(orgs), tr("set.tab_data"))
        tabs.addTab(self._tab_backup(), tr("backup.title"))
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

    # ------------------------------------------------------------- helpers

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
        form.addRow("", self._check("show_model", tr("set.show_model")))
        self.ed_model = QLineEdit(self.s["model_filter"])
        self.ed_model.setPlaceholderText("Fable")
        self.ed_model.editingFinished.connect(
            lambda: self._set("model_filter", self.ed_model.text().strip() or "Fable"))
        form.addRow(tr("set.model_filter"), self.ed_model)
        form.addRow(tr("set.model_scale"), self._slider("model_scale", 50, 200, 0.01, "\u00d7"))

        self.cb_order = QComboBox()
        mname = (self.s["model_filter"] or "Fable").upper()
        names = {"fh": tr("panel.five_hour_short"), "mo": mname, "sd": tr("panel.week_short")}
        for perm in GAUGE_ORDERS:
            self.cb_order.addItem(" \u00b7 ".join(names[g] for g in perm.split(",")), perm)
        self.cb_order.setCurrentIndex(max(0, self.cb_order.findData(self.s["gauge_order"])))
        self.cb_order.currentIndexChanged.connect(
            lambda: self._set("gauge_order", self.cb_order.currentData()))
        form.addRow(tr("set.gauge_order"), self.cb_order)
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

    def _tab_details(self) -> QWidget:
        page, form = self._page()
        hint = QLabel(tr("set.details_api_only"))
        hint.setObjectName("hint")
        hint.setWordWrap(True)
        form.addRow(hint)
        for key in ("show_plan_badge", "show_plan_name", "show_model_list", "show_surfaces",
                    "show_extra_usage"):
            form.addRow("", self._check(key, tr("set." + key)))
        form.addRow("", self._check("show_local_models", tr("set.show_local_models")))
        local_hint = QLabel(tr("set.local_models_hint"))
        local_hint.setObjectName("hint")
        local_hint.setWordWrap(True)
        form.addRow("", local_hint)

        from .localmodels import candidate_roots

        self.ed_lmpath = QLineEdit(self.s["local_models_path"])
        self.ed_lmpath.setPlaceholderText(tr("set.auto"))
        self.lbl_lmfound = QLabel()
        self.lbl_lmfound.setObjectName("hint")
        self.lbl_lmfound.setWordWrap(True)

        def lm_changed() -> None:
            self._set("local_models_path", self.ed_lmpath.text().strip())
            found = candidate_roots(self.s["local_models_path"])
            self.lbl_lmfound.setText(tr("set.backup_found", "; ".join(found)) if found
                                     else tr("set.local_models_none"))

        self.ed_lmpath.editingFinished.connect(lm_changed)
        box = QWidget()
        blay = QHBoxLayout(box)
        blay.setContentsMargins(0, 0, 0, 0)
        blay.addWidget(self.ed_lmpath, 1)
        btn = QPushButton(tr("set.browse"))

        def pick() -> None:
            start = self.ed_lmpath.text() or os.path.join(os.path.expanduser("~"), ".claude")
            path = QFileDialog.getExistingDirectory(self, tr("set.local_models_path"), start)
            if path:
                self.ed_lmpath.setText(os.path.normpath(path))
                lm_changed()

        btn.clicked.connect(pick)
        blay.addWidget(btn)
        form.addRow(tr("set.local_models_path"), box)
        form.addRow("", self.lbl_lmfound)
        found = candidate_roots(self.s["local_models_path"])
        self.lbl_lmfound.setText(tr("set.backup_found", "; ".join(found)) if found
                                 else tr("set.local_models_none"))

        sec = QLabel(tr("set.rows_available") if self._detail_rows else tr("set.rows_none"))
        sec.setObjectName("section" if self._detail_rows else "hint")
        sec.setWordWrap(True)
        form.addRow(sec)
        hidden = set(self.s["detail_hidden"] or [])
        for rid, label in self._detail_rows:
            cb = QCheckBox(label)
            cb.setChecked(rid not in hidden)
            cb.toggled.connect(lambda on, r=rid: self._toggle_detail_row(r, on))
            form.addRow("", cb)
        return page

    def _toggle_detail_row(self, rid: str, shown: bool) -> None:
        hidden = [x for x in (self.s["detail_hidden"] or []) if x != rid]
        if not shown:
            hidden.append(rid)
        self._set("detail_hidden", hidden)

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

        info = QLabel(tr("set.data_hint"))
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

    def _tab_backup(self) -> QWidget:
        from . import backups as bk

        page, form = self._page()
        form.addRow("", self._check("backup_enabled", tr("set.backup_enabled")))

        lamps = QWidget()
        lay = QHBoxLayout(lamps)
        lay.setContentsMargins(0, 0, 0, 0)
        for key in bk.KEYS:
            lay.addWidget(self._check(f"backup_show_{key}", tr(f"backup.name.{key}")))
        lay.addStretch(1)
        form.addRow(tr("set.backup_lamps"), lamps)

        self.cb_blabel = QComboBox()
        for key in ("age", "name", "none"):
            self.cb_blabel.addItem(tr(f"backup.label_{key}"), key)
        self.cb_blabel.setCurrentIndex(max(0, self.cb_blabel.findData(self.s["backup_label"])))
        self.cb_blabel.currentIndexChanged.connect(
            lambda: self._set("backup_label", self.cb_blabel.currentData()))
        form.addRow(tr("set.backup_label"), self.cb_blabel)

        def hours(key: str) -> QSpinBox:
            sp = QSpinBox()
            sp.setRange(1, 24 * 60)
            sp.setSuffix(tr("set.hours_suffix"))
            try:
                sp.setValue(int(self.s[key]))
            except (TypeError, ValueError):
                sp.setValue(24)
            sp.valueChanged.connect(lambda v, k=key: self._set(k, v))
            return sp

        self.sp_green = hours("backup_green_hours")
        self.sp_yellow = hours("backup_yellow_hours")
        # yellow can never be below green
        self.sp_green.valueChanged.connect(lambda v: self.sp_yellow.setValue(max(v, self.sp_yellow.value())))
        self.sp_yellow.valueChanged.connect(lambda v: self.sp_green.setValue(min(v, self.sp_green.value())))
        form.addRow(tr("set.backup_green"), self.sp_green)
        form.addRow(tr("set.backup_yellow"), self.sp_yellow)

        auto = bk.resolve_paths("", "", "")      # what the per-user profile provides

        self.ed_broot = QLineEdit(self.s["backup_root"])
        self.ed_broot.setPlaceholderText(auto.root or tr("set.not_set"))
        self.ed_broot.editingFinished.connect(self._backup_paths_changed)
        form.addRow(tr("set.backup_root"), self._with_browse(self.ed_broot, folder=True))

        self.ed_bcfg = QLineEdit(self.s["backup_config"])
        self.ed_bcfg.setPlaceholderText(auto.config_path or tr("set.not_set"))
        self.ed_bcfg.editingFinished.connect(self._backup_paths_changed)
        form.addRow(tr("set.backup_config"), self._with_browse(self.ed_bcfg, folder=False))

        self.ed_btask = QLineEdit(self.s["backup_task_filter"])
        self.ed_btask.setPlaceholderText(auto.task_filter or tr("set.not_set"))
        self.ed_btask.editingFinished.connect(
            lambda: self._set("backup_task_filter", self.ed_btask.text().strip()))
        form.addRow(tr("set.backup_tasks"), self.ed_btask)

        self.lbl_bfound = QLabel()
        self.lbl_bfound.setObjectName("hint")
        self.lbl_bfound.setWordWrap(True)
        form.addRow("", self.lbl_bfound)
        self._update_backup_hint()

        sec = QLabel(tr("set.backup_details"))
        sec.setObjectName("section")
        form.addRow(sec)
        for key, label in (("backup_d_components", "backup.sec_components"),
                           ("backup_d_contents", "backup.sec_contents"),
                           ("backup_d_problems", "backup.sec_problems"),
                           ("backup_d_tasks", "backup.sec_tasks"),
                           ("backup_d_log", "backup.sec_log")):
            form.addRow("", self._check(key, tr(label)))

        sec = QLabel(tr("set.backup_disclaimer_h"))
        sec.setObjectName("section")
        form.addRow(sec)
        disc = QLabel(tr("set.backup_disclaimer"))
        disc.setObjectName("hint")
        disc.setWordWrap(True)
        form.addRow(disc)
        return page

    def _with_browse(self, edit: QLineEdit, folder: bool) -> QWidget:
        box = QWidget()
        lay = QHBoxLayout(box)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(edit, 1)
        btn = QPushButton(tr("set.browse"))

        def pick() -> None:
            start = edit.text() or edit.placeholderText()
            if folder:
                path = QFileDialog.getExistingDirectory(self, tr("set.backup_root"), start)
            else:
                path, _ = QFileDialog.getOpenFileName(self, tr("set.backup_config"),
                                                      os.path.dirname(start), "PowerShell data (*.psd1)")
            if path:
                edit.setText(os.path.normpath(path))
                self._backup_paths_changed()

        btn.clicked.connect(pick)
        lay.addWidget(btn)
        return box

    def _backup_paths_changed(self) -> None:
        self._set("backup_root", self.ed_broot.text().strip())
        self._set("backup_config", self.ed_bcfg.text().strip())
        self._update_backup_hint()

    def _update_backup_hint(self) -> None:
        from . import backups as bk

        paths = bk.resolve_paths(self.s["backup_root"], self.s["backup_config"])
        if not paths.root:
            self.lbl_bfound.setText(tr("set.backup_unconfigured"))
        elif os.path.isdir(paths.root):
            self.lbl_bfound.setText(tr("set.backup_found", paths.root))
        else:
            self.lbl_bfound.setText(tr("backup.no_root", paths.root))

    def _tab_system(self) -> QWidget:
        page, form = self._page()

        self.cb_auto = QCheckBox(tr("menu.autostart"))
        self.cb_auto.setChecked(winutil.autostart_enabled())
        self.cb_auto.toggled.connect(self._toggle_autostart)
        form.addRow("", self.cb_auto)

        btn_dir = QPushButton(tr("set.open_config"))
        btn_dir.clicked.connect(lambda: winutil.open_path(config_dir()))
        form.addRow("", btn_dir)

        btn_reset = QPushButton(tr("set.restore"))
        btn_reset.clicked.connect(self._reset)
        form.addRow("", btn_reset)

        from . import __version__

        form.addRow("", self._check("update_check", tr("set.update_check")))
        ver_box = QWidget()
        vlay = QHBoxLayout(ver_box)
        vlay.setContentsMargins(0, 0, 0, 0)
        vlay.addWidget(QLabel(__version__), 1)
        btn_upd = QPushButton(tr("menu.check_update"))
        btn_upd.clicked.connect(self.updateRequested.emit)
        vlay.addWidget(btn_upd)
        form.addRow(tr("set.version"), ver_box)

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
