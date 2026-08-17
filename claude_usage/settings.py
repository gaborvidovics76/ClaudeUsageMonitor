"""Beállítások: egyszerű JSON fájl a %APPDATA%\\ClaudeUsageMonitor mappában."""

from __future__ import annotations

import json
import os
from typing import Any, Dict

from .datasource import default_data_path

APP_NAME = "ClaudeUsageMonitor"
APP_TITLE = "Claude Usage Monitor"


def config_dir() -> str:
    appdata = os.environ.get("APPDATA") or os.path.expanduser("~\\AppData\\Roaming")
    path = os.path.join(appdata, APP_NAME)
    os.makedirs(path, exist_ok=True)
    return path


def config_path() -> str:
    return os.path.join(config_dir(), "settings.json")


DEFAULTS: Dict[str, Any] = {
    # --- nyelv
    "language": "",                  # üres = a rendszer nyelve (ha támogatott), különben angol

    # --- profil / adatforrás
    "source": "local",               # local = Claude Desktop napló | api = claude.ai szerver
    "org": "",                       # üres = a legutóbb használt profil
    "data_path": "",                 # üres = alapértelmezett Claude útvonal
    "refresh_seconds": 5,

    # --- megjelenés
    "visible": True,                 # látszik-e a lebegő panel (False = csak tálca)
    "layout": "postit",              # postit | compact | ring
    "theme": "midnight",             # lásd theme.THEMES
    "accent": "",                    # egyedi kiemelőszín (#RRGGBB), üres = téma szerinti
    "scale": 1.0,                    # 0.7 – 2.0
    "opacity": 1.0,
    "always_on_top": True,
    "click_through": False,
    "locked": False,                 # helyben rögzítve (nem mozgatható)
    "pos_x": None,
    "pos_y": None,
    "snap_edges": True,
    "show_in_taskbar": False,

    # --- tartalom
    "show_five_hour": True,
    "show_weekly": True,
    "show_spark": True,
    "show_burn": True,
    "show_reset": True,
    "show_age": True,
    "tray_metric": "five_hour",      # five_hour | weekly | max

    # --- riasztások
    "warn_threshold": 70,
    "danger_threshold": 90,
    "notify_enabled": True,
    "notify_on_reset": True,
    "notify_stale": True,

    # --- rendszer
    "autostart": False,
    "start_menu": True,              # parancsikon a Start menüben
    "first_run_done": False,
}


class Settings:
    def __init__(self) -> None:
        self._data: Dict[str, Any] = dict(DEFAULTS)
        self.load()

    # ---------------------------------------------------------------- io

    def load(self) -> None:
        try:
            with open(config_path(), "r", encoding="utf-8") as fh:
                stored = json.load(fh)
            if isinstance(stored, dict):
                for k, v in stored.items():
                    if k in DEFAULTS:
                        self._data[k] = v
        except (OSError, ValueError):
            pass

    def save(self) -> None:
        try:
            tmp = config_path() + ".tmp"
            with open(tmp, "w", encoding="utf-8") as fh:
                json.dump(self._data, fh, indent=2, ensure_ascii=False)
            os.replace(tmp, config_path())
        except OSError:
            pass

    # ------------------------------------------------------------ elérés

    def __getitem__(self, key: str) -> Any:
        return self._data.get(key, DEFAULTS.get(key))

    def __setitem__(self, key: str, value: Any) -> None:
        self._data[key] = value

    def get(self, key: str, fallback: Any = None) -> Any:
        return self._data.get(key, DEFAULTS.get(key, fallback))

    def update(self, values: Dict[str, Any]) -> None:
        self._data.update(values)

    def as_dict(self) -> Dict[str, Any]:
        return dict(self._data)

    def reset(self) -> None:
        self._data = dict(DEFAULTS)
        self._data["first_run_done"] = True

    # ------------------------------------------------------ származtatott

    def resolved_data_path(self) -> str:
        return self["data_path"] or default_data_path()
