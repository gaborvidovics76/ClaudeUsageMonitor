"""Controller: tray icon, timer, menu, notifications."""

from __future__ import annotations

import os
import sys
import traceback
from datetime import datetime
from typing import Dict, Optional

from PySide6.QtCore import QPoint, QSharedMemory, QTimer, Qt
from PySide6.QtGui import QAction, QActionGroup
from PySide6.QtWidgets import QApplication, QMenu, QMessageBox, QSystemTrayIcon

from . import secretstore, winutil
from .apisource import ApiReader
from . import __version__
from .backups import BackupChecker
from .localmodels import LocalModelUsage
from .updater import Updater, run_cli_update
from .datasource import Metrics, UsageReader, detail_label, fmt_age, fmt_delta
from .i18n import (
    available_languages,
    current_language,
    language_name,
    set_language,
    system_language,
    tr,
)
from .history import HistoryWindow
from .settings import GAUGE_ORDERS, APP_TITLE, Settings, config_dir
from .settings_dialog import LAYOUTS, SettingsDialog
from .theme import THEMES, Palette, qc
from .widget import UsageWidget

MENU_QSS = """
QMenu { background: #1c1f26; color: #dfe4ee; border: 1px solid #333944; border-radius: 10px; padding: 6px; }
QMenu::item { padding: 6px 22px 6px 26px; border-radius: 6px; }
QMenu::item:selected { background: #2f3846; }
QMenu::item:disabled { color: #7b849a; }
QMenu::separator { height: 1px; background: #2c313b; margin: 5px 8px; }
QMenu::indicator { width: 14px; height: 14px; left: 8px; }
"""


def log(message: str) -> None:
    """Startup log - without it a logon-time error would be invisible."""
    try:
        path = os.path.join(config_dir(), "startup.log")
        if os.path.exists(path) and os.path.getsize(path) > 60_000:
            with open(path, "r", encoding="utf-8", errors="replace") as fh:
                tail = fh.readlines()[-200:]
            with open(path, "w", encoding="utf-8") as fh:
                fh.writelines(tail)
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(f"{datetime.now():%Y-%m-%d %H:%M:%S}  {message}\n")
    except OSError:
        pass


class MonitorApp:
    def __init__(self, app: QApplication):
        self.app = app
        self.settings = Settings()
        # language: saved value, or the system language (if supported), else English
        set_language(self.settings["language"] or system_language())
        # If the exe moved in the meantime, fix the autostart entry.
        self.settings["autostart"] = winutil.sync_autostart()
        self.settings.save()
        # Start menu shortcut (packaged exe only, if requested and not yet present)
        if self.settings["start_menu"]:
            winutil.ensure_start_menu_shortcut()
        winutil.sync_installed_version(__version__)
        self.local_reader = UsageReader(self.settings.resolved_data_path())
        self.api_reader = ApiReader(
            tokens=secretstore.load_tokens(),
            on_tokens_changed=self._on_tokens_changed,
        )
        self.reader = self.local_reader     # apply_settings sets the real one
        self.metrics = Metrics()

        self.widget = UsageWidget(self.settings)
        self.widget.menuRequested.connect(self.show_menu)
        self.widget.doubleClicked.connect(self.show_history)
        self.widget.backupClicked.connect(self.show_backups)

        # backup status (OneDrive / Nextcloud / Obsidian) - checked on a worker thread
        self.backup = BackupChecker()
        self._backup_version = -1
        self.backup_dialog = None

        self.tray = QSystemTrayIcon(winutil.app_icon())
        self.tray.setToolTip(APP_TITLE)
        self.tray.activated.connect(self._tray_activated)
        self.tray.show()

        self.dialog: Optional[SettingsDialog] = None
        self.history: Optional[HistoryWindow] = None

        self._last: Dict[str, float] = {}
        self._stale_notified = False

        # per-model split from Claude Code's local logs (works with either data source)
        self.local_models = LocalModelUsage()
        self._local_seen = -1
        self._local_window: Optional[float] = None

        # online updates: first check shortly after start, then every few hours
        self.updater = Updater(self.settings["update_url"] or "")
        self._update_seen = -1
        self._update_notified = ""
        self.update_dialog = None
        QTimer.singleShot(25_000, self._auto_update_check)

        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)
        # fast tick while a fetch is running: animates the "refreshing" indicator and
        # shows the result the moment it arrives (instead of waiting for the 10 s tick)
        self.pulse = QTimer()
        self.pulse.setInterval(120)
        self.pulse.timeout.connect(self._pulse)
        self._busy_until = 0.0          # minimum visible duration of the indicator
        self._was_busy = False
        self.apply_settings()
        self.refresh()

        if not self.settings["first_run_done"]:
            self.settings["first_run_done"] = True
            self.settings.save()
            self.notify(APP_TITLE, tr("notify.first_run"))

    # ------------------------------------------------------------ setup

    def apply_settings(self) -> None:
        s = self.settings
        self.local_reader.path = s.resolved_data_path()

        # source selection: "api" only if there is a valid sign-in
        use_api = s["source"] == "api" and self.api_reader.has_tokens()
        self.reader = self.api_reader if use_api else self.local_reader
        self.api_reader.model_filter = (s["model_filter"] or "Fable").strip()

        # We refresh the display often (age counter, picking up a completed query).
        # The actual server call is throttled to 60s inside ApiReader, so the
        # frequent tick does not burden the server.
        interval = 10 if use_api else max(2, int(s["refresh_seconds"]))

        self.backup.configure(
            enabled=bool(s["backup_enabled"]) or (self.backup_dialog is not None and self.backup_dialog.isVisible()),
            root_override=s["backup_root"] or "",
            config_path=s["backup_config"] or "",
            task_filter=s["backup_task_filter"] or "",
            want_tasks=bool(s["backup_d_tasks"]),
            want_listing=bool(s["backup_d_contents"]) or bool(s["backup_d_components"]),
        )
        self.widget.backup_expected = bool(s["backup_enabled"]) and self.backup.paths().expected
        self.backup.check()

        self.widget.apply_settings()
        self.widget.setVisible(bool(s["visible"]))
        self.timer.start(interval * 1000)
        self.refresh()

    # -------------------------------------------------------------- data

    def _is_busy(self) -> bool:
        api_busy = self.reader is self.api_reader and self.api_reader.busy
        return api_busy or datetime.now().timestamp() < self._busy_until

    def _pulse(self) -> None:
        busy = self._is_busy()
        if busy:
            self.widget.set_activity(True)
            return
        self.pulse.stop()
        self.refresh()                  # the fetch just finished - show its result now

    def _sync_activity(self) -> None:
        busy = self._is_busy()
        note, retry_in = "", None
        if self.reader is self.api_reader:
            note = self.api_reader.last_error
            retry_in = self.api_reader.retry_in
        self.widget.set_activity(busy, note, retry_in)
        if busy and not self.pulse.isActive():
            self.pulse.start()

    def refresh(self) -> None:
        self.metrics = self.reader.read(self.settings["org"] or None)
        self.widget.set_metrics(self.metrics)
        self._sync_activity()
        self._poll_backup()
        self._poll_update()
        self._poll_local_models()
        self._update_tray()
        self._check_alerts()
        if self.history is not None and self.history.isVisible():
            self.history.refresh()

    def force_refresh(self) -> None:
        """Manual 'Refresh now'.

        API mode: forces an immediate server call (queued if one is already in
        flight) and re-reads several times afterwards, so the result shows up even
        on a slow network instead of waiting for the next 10 s tick.
        Local mode: re-reads the log file even if its timestamp did not change.
        """
        # always visible for a moment, even when the answer is instant (local mode)
        self._busy_until = datetime.now().timestamp() + 0.9
        if self.reader is self.api_reader:
            self.api_reader.force_refresh()
        else:
            self.local_reader.invalidate()
        self.refresh()                  # -> _sync_activity starts the pulse timer

    def _tray_value(self) -> float:
        m, mode = self.metrics, self.settings["tray_metric"]
        if mode == "weekly":
            return m.weekly.value
        if mode == "max":
            return max(m.five_hour.value, m.weekly.value)
        return m.five_hour.value

    # ------------------------------------------------------------ local model split

    def _poll_local_models(self) -> None:
        lm = self.local_models
        lm.enabled = bool(self.settings["show_local_models"])
        lm.set_override(self.settings["local_models_path"] or "")
        if not lm.enabled:
            if self.widget.local_models:
                self.widget.set_local_models([])
            return
        lm.scan()
        # line the window up with the weekly limit's own week when the reset time is known
        reset = self.metrics.weekly.reset_at if self.metrics.ok else None
        window = (reset / 1000.0 - 7 * 86400) if reset else None
        if lm.version != self._local_seen or window != self._local_window:
            self._local_seen, self._local_window = lm.version, window
            self.widget.set_local_models(lm.shares(window))
        elif lm.busy:
            QTimer.singleShot(1500, self._poll_local_models)

    # ------------------------------------------------------------ updates

    def _auto_update_check(self) -> None:
        if self.settings["update_check"]:
            self.updater.manifest_url = self.settings["update_url"] or ""
            self.updater.check()
            QTimer.singleShot(4000, self._poll_update)

    def update_available(self) -> str:
        """Version string of an offered update ("" = none, or the user skipped it)."""
        up = self.updater
        if up.state in ("available", "downloading", "ready") and up.info is not None \
                and up.info.version != self.settings["update_skip_version"]:
            return up.info.version
        return ""

    def _poll_update(self) -> None:
        up = self.updater
        if self.settings["update_check"] and up.due() and not up.busy \
                and up.state not in ("downloading", "ready"):
            self._auto_update_check()
        if up.counter == self._update_seen:
            return
        self._update_seen = up.counter
        version = self.update_available()
        self.widget.update_version = version
        self.widget.update()
        if version and version != self._update_notified:
            self._update_notified = version
            self.notify(APP_TITLE, tr("notify.update", version))

    def show_update(self) -> None:
        from .update_dialog import UpdateDialog

        if self.update_dialog is None:
            self.update_dialog = UpdateDialog(self.updater)
            self.update_dialog.skipRequested.connect(lambda v: self._set("update_skip_version", v))
            self.update_dialog.quitRequested.connect(self.quit)
        if self.updater.state not in ("available", "downloading", "ready"):
            self.updater.manifest_url = self.settings["update_url"] or ""
            self.updater.check()
        dlg = self.update_dialog
        dlg.sync(force=True)
        dlg.show()
        dlg.raise_()
        dlg.activateWindow()

    # ------------------------------------------------------------ backups

    def _poll_backup(self) -> None:
        """Start a due check, and push a finished one to the panel / dialog / tray."""
        self.backup.check()
        busy = self.backup.busy
        if self.backup.version != self._backup_version:
            self._backup_version = self.backup.version
            self.widget.set_backup(self.backup.status, self.widget.backup_expected)
            self._update_tray()
        if self.backup_dialog is not None and self.backup_dialog.isVisible():
            if busy != self.backup_dialog.busy or self.backup_dialog.status is not self.backup.status:
                self.backup_dialog.set_status(self.backup.status, busy)

    def force_backup_check(self) -> None:
        self.backup.enabled = True
        self.backup.check(force=True)
        self._poll_backup()
        for delay_ms in (600, 1500, 3000, 6000, 12000, 25000):
            QTimer.singleShot(delay_ms, self._poll_backup)

    def show_backups(self, key: Optional[str] = None) -> None:
        from .backup_dialog import BackupDialog

        if self.backup_dialog is None:
            self.backup_dialog = BackupDialog(self.settings)
            self.backup_dialog.refreshRequested.connect(self.force_backup_check)
        dlg = self.backup_dialog
        dlg.set_status(self.backup.status, self.backup.busy)
        dlg.select(key if isinstance(key, str) else None)
        dlg.show()
        dlg.raise_()
        dlg.activateWindow()
        st = self.backup.status
        if st is None or datetime.now().timestamp() - st.checked_at > 60:
            self.force_backup_check()

    def _update_tray(self) -> None:
        pal = Palette(self.settings["theme"], self.settings["accent"])
        m = self.metrics
        if not m.ok:
            self.tray.setIcon(winutil.app_icon())
            self.tray.setToolTip(f"{APP_TITLE}\n{m.error}")
            return

        value = self._tray_value()
        color = qc(pal.status(value, self.settings["warn_threshold"], self.settings["danger_threshold"]))
        self.tray.setIcon(winutil.tray_icon(value, color))

        fh, wk = m.five_hour, m.weekly

        def line(label: str, g) -> str:
            reset = f"  ({tr('panel.reset', fmt_delta(g.reset_in_ms))})" if g.reset_in_ms is not None else ""
            return tr("tray.line", label, f"{g.value:.0f}") + reset

        lines = [APP_TITLE, line(tr("panel.five_hour"), fh)]
        if self.settings["show_model"] and m.has_model:
            lines.append(line(tr("panel.model", m.model_name.upper()), m.model))
        lines.append(line(tr("panel.weekly"), wk))
        shown = [x for x in self.widget.detail_rows() if x[0] != "@header"][:3]   # tray tips are short
        for _rid, rlabel, _val, right, _reset in shown:
            lines.append(f"{rlabel}: {right}")
        if m.profile is not None and m.profile.badge and self.settings["show_plan_badge"]:
            lines[0] = f"{APP_TITLE}  \u00b7  {m.profile.badge}"
        lines.append(tr("panel.updated", fmt_age(m.age_s)))
        if self.widget.backup_expected and self.backup.status is not None:
            from .backup_dialog import summary_text

            lines.append(tr("backup.tray", summary_text(self.backup.status, self.settings)))
        # old data is still shown after a failed fetch - say why it is not fresher
        if self.reader is self.api_reader and self.api_reader.last_error:
            lines.append("! " + self.api_reader.last_error.replace("\n", " "))
            wait = self.api_reader.retry_in
            if wait is not None:
                lines.append(tr("panel.retry_in", int(wait) + 1))
        self.tray.setToolTip("\n".join(lines))

    def _check_alerts(self) -> None:
        s, m = self.settings, self.metrics
        if not m.ok:
            return
        warn, danger = float(s["warn_threshold"]), float(s["danger_threshold"])

        gauges = [("fh", tr("panel.five_hour"), m.five_hour), ("sd", tr("panel.weekly"), m.weekly)]
        if m.has_model:
            gauges.append(("mo", tr("panel.model", m.model_name.upper()), m.model))
        for key, label, gauge in gauges:
            prev = self._last.get(key)
            self._last[key] = gauge.value
            if prev is None:
                continue
            if s["notify_enabled"]:
                for level in (danger, warn):
                    if prev < level <= gauge.value:
                        extra = f"  {tr('panel.reset', fmt_delta(gauge.reset_in_ms))}" \
                            if gauge.reset_in_ms is not None else ""
                        self.notify(label, tr("notify.threshold", label, f"{gauge.value:.0f}") + extra)
                        break
            if s["notify_on_reset"] and prev > 15 and gauge.value <= 1:
                self.notify(label, tr("notify.reset_done", label))

        if s["notify_stale"]:
            if m.stale and not self._stale_notified:
                self._stale_notified = True
                self.notify(tr("notify.stale_title"), tr("notify.stale_body", fmt_age(m.age_s)))
            elif not m.stale:
                self._stale_notified = False

    def notify(self, title: str, message: str) -> None:
        if self.tray.isSystemTrayAvailable():
            self.tray.showMessage(title, message, winutil.app_icon(), 6000)

    # ---------------------------------------------------------------- menu

    def _tray_activated(self, reason) -> None:
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.toggle_widget()
        elif reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.show_history()
        elif reason == QSystemTrayIcon.ActivationReason.Context:
            self.show_menu(None)

    def build_menu(self) -> QMenu:
        s, m = self.settings, self.metrics
        menu = QMenu()
        menu.setStyleSheet(MENU_QSS)

        head = menu.addAction(
            tr("tray.head", f"{m.five_hour.value:.0f}", f"{m.weekly.value:.0f}")
            if m.ok else tr("panel.no_data"))
        head.setEnabled(False)
        menu.addSeparator()

        def toggle(label: str, key: str, after=None) -> QAction:
            act = menu.addAction(label)
            act.setCheckable(True)
            act.setChecked(bool(s[key]))

            def handler(checked: bool) -> None:
                s[key] = checked
                s.save()
                (after or self.apply_settings)()

            act.toggled.connect(handler)
            return act

        toggle(tr("menu.panel_visible"), "visible")
        toggle(tr("set.show_spark"), "show_spark")
        toggle(tr("menu.backup_bar"), "backup_enabled")

        # per-model gauge: show / size / order, in one submenu named after the model
        m_now = getattr(self, "metrics", None)
        mname = ((m_now.model_name if (m_now is not None and m_now.model_name) else "")
                 or s["model_filter"] or "Fable").upper()
        model_menu = menu.addMenu(tr("menu.model_gauge", mname))
        in_api = self.reader is self.api_reader                 # data exists only in API mode
        model_act = model_menu.addAction(tr("set.show_model"))
        model_act.setCheckable(True)
        model_act.setChecked(bool(s["show_model"]))
        model_act.setEnabled(in_api)
        model_act.toggled.connect(lambda c: self._set("show_model", c))

        msize_menu = model_menu.addMenu(tr("menu.size"))
        msize_menu.setEnabled(in_api)
        mgroup = QActionGroup(msize_menu)
        for skey, value in (("size.small", 0.7), ("size.normal", 1.0),
                            ("size.large", 1.3), ("size.extra", 1.6)):
            act = msize_menu.addAction(tr(skey))
            act.setCheckable(True)
            act.setChecked(abs(float(s["model_scale"]) - value) < 0.01)
            mgroup.addAction(act)
            act.triggered.connect(lambda _c=False, v=value: self._set("model_scale", v))

        order_menu = model_menu.addMenu(tr("menu.order"))
        ogroup = QActionGroup(order_menu)
        names = {"fh": tr("panel.five_hour_short"), "mo": mname, "sd": tr("panel.week_short")}
        for perm in GAUGE_ORDERS:
            act = order_menu.addAction(" \u00b7 ".join(names[g] for g in perm.split(",")))
            act.setCheckable(True)
            act.setChecked(s["gauge_order"] == perm)
            ogroup.addAction(act)
            act.triggered.connect(lambda _c=False, o=perm: self._set("gauge_order", o))

        # plan badge + the small list of extra limits
        details_menu = menu.addMenu(tr("menu.details"))
        for dkey in ("show_plan_badge", "show_plan_name", "show_model_list", "show_surfaces",
                     "show_extra_usage", "show_local_models"):
            dact = details_menu.addAction(tr("set." + dkey))
            dact.setCheckable(True)
            dact.setChecked(bool(s[dkey]))
            # the server figures need the claude.ai source; the local split works either way
            dact.setEnabled(in_api or dkey == "show_local_models")
            dact.toggled.connect(lambda c, kk=dkey: self._set(kk, c))

        layout_menu = menu.addMenu(tr("menu.layout"))
        group = QActionGroup(layout_menu)
        for key, _label in LAYOUTS:
            act = layout_menu.addAction(tr("layout." + key))
            act.setCheckable(True)
            act.setChecked(s["layout"] == key)
            group.addAction(act)
            act.triggered.connect(lambda _c=False, k=key: self._set("layout", k))

        theme_menu = menu.addMenu(tr("menu.theme"))
        tgroup = QActionGroup(theme_menu)
        for key in THEMES:
            act = theme_menu.addAction(tr("theme." + key))
            act.setCheckable(True)
            act.setChecked(s["theme"] == key)
            tgroup.addAction(act)
            act.triggered.connect(lambda _c=False, k=key: self._set("theme", k))

        size_menu = menu.addMenu(tr("menu.size"))
        for skey, value in (("size.small", 0.85), ("size.normal", 1.0),
                            ("size.large", 1.25), ("size.extra", 1.5)):
            act = size_menu.addAction(tr(skey))
            act.setCheckable(True)
            act.setChecked(abs(float(s["scale"]) - value) < 0.01)
            act.triggered.connect(lambda _c=False, v=value: self._set("scale", v))

        lang_menu = menu.addMenu(tr("menu.language"))
        lgroup = QActionGroup(lang_menu)
        for code in available_languages():
            act = lang_menu.addAction(language_name(code))
            act.setCheckable(True)
            act.setChecked(current_language() == code)
            lgroup.addAction(act)
            act.triggered.connect(lambda _c=False, cc=code: self._set_language(cc))

        toggle(tr("menu.always_top"), "always_on_top")
        toggle(tr("menu.locked"), "locked")
        toggle(tr("menu.click_through"), "click_through")

        auto = menu.addAction(tr("menu.autostart"))
        auto.setCheckable(True)
        auto.setChecked(winutil.autostart_enabled())
        auto.toggled.connect(self._toggle_autostart)

        startm = menu.addAction(tr("menu.start_menu"))
        startm.setCheckable(True)
        startm.setChecked(winutil.start_menu_exists())
        startm.toggled.connect(self._toggle_start_menu)
        menu.addSeparator()

        src_menu = menu.addMenu(tr("menu.source"))
        sgroup = QActionGroup(src_menu)
        for key in ("local", "api"):
            act = src_menu.addAction(tr("source." + key))
            act.setCheckable(True)
            act.setChecked(s["source"] == key)
            sgroup.addAction(act)
            act.triggered.connect(lambda _c=False, k=key: self._set_source(k))
        if self.api_reader.has_tokens():
            src_menu.addSeparator()
            src_menu.addAction(tr("menu.logout"), self.logout)

        menu.addSeparator()
        if not self.api_reader.has_tokens():
            menu.addAction(tr("menu.login"), self.login)
        menu.addAction(tr("menu.history"), self.show_history)
        menu.addAction(tr("menu.backups"), lambda: self.show_backups(None))
        menu.addAction(tr("menu.settings"), self.show_settings)
        ref = menu.addAction(tr("menu.refresh"), self.force_refresh)
        if self._is_busy():
            ref.setText(tr("panel.refreshing") + "…")
            ref.setEnabled(False)

        # the PROGRAM update lives apart from the data refresh, so the two are never mixed up
        menu.addSeparator()
        new_version = self.update_available()
        menu.addAction(tr("menu.update_available", new_version) if new_version
                       else tr("menu.check_update"), self.show_update)
        menu.addSeparator()
        menu.addAction(tr("menu.quit"), self.quit)
        return menu

    def _set(self, key: str, value) -> None:
        self.settings[key] = value
        self.settings.save()
        self.apply_settings()

    def _set_language(self, code: str) -> None:
        set_language(code)
        self.settings["language"] = code
        self.settings.save()
        # redraw the whole UI in the new language
        self.widget.update()
        self.refresh()
        if self.dialog is not None and self.dialog.isVisible():
            self.dialog.close()
            self.dialog = None
        if self.history is not None:
            self.history.close()
            self.history = None
        if self.backup_dialog is not None:
            self.backup_dialog.close()
            self.backup_dialog = None
        if self.update_dialog is not None:
            self.update_dialog.close()
            self.update_dialog = None
        self.widget.set_backup(self.backup.status, self.widget.backup_expected)

    def _set_source(self, source: str) -> None:
        if source == "api" and not self.api_reader.has_tokens():
            if not self.login():
                return
        self.settings["source"] = source
        self.settings.save()
        self.apply_settings()

    def login(self) -> bool:
        """OAuth sign-in through the system browser. True on success."""
        from .authdialog import OAuthDialog

        dlg = OAuthDialog()
        dlg.succeeded.connect(self._on_tokens_captured)
        result = dlg.exec()
        if result and self.api_reader.has_tokens():
            self.notify(APP_TITLE, tr("notify.login_ok"))
            return True
        return False

    def _on_tokens_captured(self, tokens: dict) -> None:
        secretstore.save_tokens(tokens)
        self.api_reader.set_tokens(tokens)
        self.settings["source"] = "api"
        self.settings.save()
        self.apply_settings()

    def _on_tokens_changed(self, tokens: dict) -> None:
        # the background thread refreshed the token - save it
        secretstore.save_tokens(tokens)

    def logout(self) -> None:
        secretstore.clear_secret()
        self.api_reader.set_tokens({})
        self.settings["source"] = "local"
        self.settings.save()
        self.apply_settings()
        self.notify(APP_TITLE, tr("notify.logout"))

    def _toggle_start_menu(self, enabled: bool) -> None:
        self.settings["start_menu"] = enabled
        self.settings.save()
        if enabled:
            winutil.create_start_menu_shortcut()
        else:
            winutil.remove_start_menu_shortcut()

    def _toggle_autostart(self, enabled: bool) -> None:
        if not winutil.set_autostart(enabled):
            self.notify(APP_TITLE, tr("notify.autostart_fail"))
            return
        self.settings["autostart"] = enabled
        self.settings.save()
        self.notify(APP_TITLE, tr("notify.autostart_on") if enabled else tr("notify.autostart_off"))

    def show_menu(self, pos: Optional[QPoint]) -> None:
        menu = self.build_menu()
        menu.exec(pos if pos is not None else self._cursor_pos())

    @staticmethod
    def _cursor_pos() -> QPoint:
        from PySide6.QtGui import QCursor

        return QCursor.pos()

    # -------------------------------------------------------------- ablakok

    def toggle_widget(self) -> None:
        self.settings["visible"] = not bool(self.settings["visible"])
        self.settings.save()
        self.widget.setVisible(bool(self.settings["visible"]))
        if self.settings["visible"]:
            self.widget.raise_()

    def show_settings(self) -> None:
        if self.dialog is not None and self.dialog.isVisible():
            self.dialog.raise_()
            self.dialog.activateWindow()
            return
        orgs = self.local_reader.organizations() or self.api_reader.organizations()
        rows = [(r.id, detail_label(r)) for r in self.metrics.rows]
        if self.metrics.extra is not None:
            rows.append(("extra", tr("detail.extra")))
        rows += [("local:" + sh.name, f"{sh.name}  (Claude Code)") for sh in self.widget.local_models]
        self.dialog = SettingsDialog(self.settings, orgs, rows=rows)
        self.dialog.changed.connect(self.apply_settings)
        self.dialog.resetRequested.connect(self._reset_settings)
        self.dialog.loginRequested.connect(self.login)
        self.dialog.updateRequested.connect(self.show_update)
        self.dialog.logoutRequested.connect(self.logout)
        self.dialog.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, False)
        self.dialog.show()

    def _reset_settings(self) -> None:
        self.settings.reset()
        self.settings.save()
        self.apply_settings()

    def show_history(self) -> None:
        # always with the current source (not stale after a local/API switch)
        if self.history is None:
            self.history = HistoryWindow(self.settings, self.reader)
        else:
            self.history.reader = self.reader
        self.history.refresh()
        self.history.show()
        self.history.raise_()
        self.history.activateWindow()

    def quit(self) -> None:
        self.settings.save()
        self.tray.hide()
        self.app.quit()


def _handle_cli(argv) -> Optional[int]:
    """A few switches available from the command line, without a window."""
    if "--enable-autostart" in argv or "--disable-autostart" in argv:
        want = "--enable-autostart" in argv
        ok = winutil.set_autostart(want)
        log(f"CLI autostart={want} ok={ok} mode={winutil.autostart_method() or 'none'}")
        return 0 if ok else 1
    if "--autostart-status" in argv:
        log(f"CLI status: mode={winutil.autostart_method() or 'none'}")
        return 0
    if "--version" in argv:
        log(f"CLI version: {__version__}")
        return 0
    if "--check-update" in argv or "--update-now" in argv:
        # no window; the outcome is written to update.log in the config folder
        url = next((a.split("=", 1)[1] for a in argv if a.startswith("--manifest-url=")), "")
        return run_cli_update(url or Settings()["update_url"] or "", apply="--update-now" in argv)
    return None


def run() -> int:
    code = _handle_cli(sys.argv[1:])
    if code is not None:
        return code

    log(f"starting {__version__} - exe={sys.executable} frozen={getattr(sys, 'frozen', False)}")
    try:
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_DontShowIconsInMenus, False)
        app = QApplication(sys.argv)
        app.setApplicationName(APP_TITLE)
        app.setQuitOnLastWindowClosed(False)
        app.setWindowIcon(winutil.app_icon())

        # language first, so even the "already running" message is localized
        set_language(Settings()["language"] or system_language())

        # only one instance at a time
        lock = QSharedMemory("ClaudeUsageMonitor-single-instance")
        if lock.attach():
            log("another instance is already running, exiting")
            QMessageBox.information(None, APP_TITLE, tr("err.already_running"))
            return 0
        lock.create(1)
        app._lock = lock

        if not QSystemTrayIcon.isSystemTrayAvailable():
            log("warning: no system tray")

        monitor = MonitorApp(app)
        app._monitor = monitor  # keep a reference
        log(f"started - autostart={winutil.autostart_method() or 'none'}")
        return app.exec()
    except BaseException:
        log("ERROR:\n" + traceback.format_exc())
        raise
