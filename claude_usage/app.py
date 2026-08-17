"""Vezérlő: tálcaikon, időzítő, menü, értesítések."""

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
from .datasource import Metrics, UsageReader, fmt_age, fmt_delta
from .i18n import (
    available_languages,
    current_language,
    language_name,
    set_language,
    system_language,
    tr,
)
from .history import HistoryWindow
from .settings import APP_TITLE, Settings, config_dir
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
    """Indítási napló – enélkül egy bejelentkezéskori hiba láthatatlan marad."""
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
        # nyelv: mentett érték, vagy a rendszer nyelve (ha támogatott), különben angol
        set_language(self.settings["language"] or system_language())
        # Ha az exe időközben átkerült máshova, igazítsuk az indítóbejegyzést.
        self.settings["autostart"] = winutil.sync_autostart()
        self.settings.save()
        # Start menü parancsikon (csak a csomagolt exe-nél, ha kérve van és még nincs)
        if self.settings["start_menu"]:
            winutil.ensure_start_menu_shortcut()
        self.local_reader = UsageReader(self.settings.resolved_data_path())
        self.api_reader = ApiReader(
            tokens=secretstore.load_tokens(),
            on_tokens_changed=self._on_tokens_changed,
        )
        self.reader = self.local_reader     # apply_settings állítja be a valósat
        self.metrics = Metrics()

        self.widget = UsageWidget(self.settings)
        self.widget.menuRequested.connect(self.show_menu)
        self.widget.doubleClicked.connect(self.show_history)

        self.tray = QSystemTrayIcon(winutil.app_icon())
        self.tray.setToolTip(APP_TITLE)
        self.tray.activated.connect(self._tray_activated)
        self.tray.show()

        self.dialog: Optional[SettingsDialog] = None
        self.history: Optional[HistoryWindow] = None

        self._last: Dict[str, float] = {}
        self._stale_notified = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)
        self.apply_settings()
        self.refresh()

        if not self.settings["first_run_done"]:
            self.settings["first_run_done"] = True
            self.settings.save()
            self.notify(APP_TITLE, tr("notify.first_run"))

    # ------------------------------------------------------------ beállítás

    def apply_settings(self) -> None:
        s = self.settings
        self.local_reader.path = s.resolved_data_path()

        # forrásválasztás: "api" csak akkor, ha van érvényes bejelentkezés
        use_api = s["source"] == "api" and self.api_reader.has_tokens()
        self.reader = self.api_reader if use_api else self.local_reader

        # A kijelzőt sűrűn frissítjük (age-számláló, kész lekérdezés felszedése).
        # A tényleges szerverhívást az ApiReader belül fojtja 60 mp-re, tehát a
        # sűrű tick nem terheli a szervert.
        interval = 10 if use_api else max(2, int(s["refresh_seconds"]))

        self.widget.apply_settings()
        self.widget.setVisible(bool(s["visible"]))
        self.timer.start(interval * 1000)
        self.refresh()

    # -------------------------------------------------------------- adatok

    def refresh(self) -> None:
        self.metrics = self.reader.read(self.settings["org"] or None)
        self.widget.set_metrics(self.metrics)
        self._update_tray()
        self._check_alerts()
        if self.history is not None and self.history.isVisible():
            self.history.refresh()

    def force_refresh(self) -> None:
        """Kézi 'Frissítés most' – API-módban azonnali szerverhívást kényszerít."""
        if self.reader is self.api_reader:
            self.api_reader.force_refresh()
            # a fetch aszinkron; szedjük fel az eredményt kis késleltetéssel
            QTimer.singleShot(1500, self.refresh)
            QTimer.singleShot(3500, self.refresh)
        self.refresh()

    def _tray_value(self) -> float:
        m, mode = self.metrics, self.settings["tray_metric"]
        if mode == "weekly":
            return m.weekly.value
        if mode == "max":
            return max(m.five_hour.value, m.weekly.value)
        return m.five_hour.value

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
        lines = [
            APP_TITLE,
            tr("tray.line", tr("panel.five_hour"), f"{fh.value:.0f}")
            + (f"  ({tr('panel.reset', fmt_delta(fh.reset_in_ms))})" if fh.reset_in_ms is not None else ""),
            tr("tray.line", tr("panel.weekly"), f"{wk.value:.0f}")
            + (f"  ({tr('panel.reset', fmt_delta(wk.reset_in_ms))})" if wk.reset_in_ms is not None else ""),
            tr("panel.updated", fmt_age(m.age_s)),
        ]
        self.tray.setToolTip("\n".join(lines))

    def _check_alerts(self) -> None:
        s, m = self.settings, self.metrics
        if not m.ok:
            return
        warn, danger = float(s["warn_threshold"]), float(s["danger_threshold"])

        for key, lkey, gauge in (("fh", "panel.five_hour", m.five_hour),
                                 ("sd", "panel.weekly", m.weekly)):
            label = tr(lkey)
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

    # ---------------------------------------------------------------- menü

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
        menu.addAction(tr("menu.settings"), self.show_settings)
        menu.addAction(tr("menu.refresh"), self.force_refresh)
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
        # az egész felület újrarajzolása az új nyelvvel
        self.widget.update()
        self.refresh()
        if self.dialog is not None and self.dialog.isVisible():
            self.dialog.close()
            self.dialog = None
        if self.history is not None:
            self.history.close()
            self.history = None

    def _set_source(self, source: str) -> None:
        if source == "api" and not self.api_reader.has_tokens():
            if not self.login():
                return
        self.settings["source"] = source
        self.settings.save()
        self.apply_settings()

    def login(self) -> bool:
        """OAuth bejelentkezés a rendszerböngészőn keresztül. True, ha sikerült."""
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
        # a háttérszál frissítette a tokent – mentsük el
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
        self.dialog = SettingsDialog(self.settings, orgs)
        self.dialog.changed.connect(self.apply_settings)
        self.dialog.resetRequested.connect(self._reset_settings)
        self.dialog.loginRequested.connect(self.login)
        self.dialog.logoutRequested.connect(self.logout)
        self.dialog.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, False)
        self.dialog.show()

    def _reset_settings(self) -> None:
        self.settings.reset()
        self.settings.save()
        self.apply_settings()

    def show_history(self) -> None:
        # mindig az aktuális forrással (helyi/API váltás után se legyen elavult)
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
    """Néhány kapcsoló ablak nélkül, parancssorból is elérhető."""
    if "--enable-autostart" in argv or "--disable-autostart" in argv:
        want = "--enable-autostart" in argv
        ok = winutil.set_autostart(want)
        log(f"CLI autostart={want} siker={ok} mód={winutil.autostart_method() or 'nincs'}")
        return 0 if ok else 1
    if "--autostart-status" in argv:
        log(f"CLI állapot: mód={winutil.autostart_method() or 'nincs'}")
        return 0
    return None


def run() -> int:
    code = _handle_cli(sys.argv[1:])
    if code is not None:
        return code

    log(f"indul – exe={sys.executable} frozen={getattr(sys, 'frozen', False)}")
    try:
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_DontShowIconsInMenus, False)
        app = QApplication(sys.argv)
        app.setApplicationName(APP_TITLE)
        app.setQuitOnLastWindowClosed(False)
        app.setWindowIcon(winutil.app_icon())

        # egyszerre csak egy példány fusson
        lock = QSharedMemory("ClaudeUsageMonitor-single-instance")
        if lock.attach():
            log("már fut egy példány, kilépés")
            QMessageBox.information(None, APP_TITLE, tr("err.already_running"))
            return 0
        lock.create(1)
        app._lock = lock

        if not QSystemTrayIcon.isSystemTrayAvailable():
            log("figyelmeztetés: nincs rendszertálca")

        monitor = MonitorApp(app)
        app._monitor = monitor  # referencia megtartása
        log(f"elindult – autostart={winutil.autostart_method() or 'nincs'}")
        return app.exec()
    except BaseException:
        log("HIBA:\n" + traceback.format_exc())
        raise
