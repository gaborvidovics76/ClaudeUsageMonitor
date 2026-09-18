"""Settings: a simple JSON file in %APPDATA%\\ClaudeUsageMonitor."""

from __future__ import annotations

import json
import os
import sys
from typing import Any, Dict

from .datasource import default_data_path

APP_NAME = "ClaudeUsageMonitor"
APP_TITLE = "Claude Usage Monitor"


def user_data_root() -> str:
    """Per-user application data: %APPDATA% on Windows, ~/Library/Application Support on macOS,
    $XDG_CONFIG_HOME (~/.config) elsewhere."""
    if sys.platform == "darwin":
        return os.path.join(os.path.expanduser("~"), "Library", "Application Support")
    if sys.platform.startswith("win"):
        return os.environ.get("APPDATA") or os.path.expanduser("~\\AppData\\Roaming")
    return os.environ.get("XDG_CONFIG_HOME") or os.path.join(os.path.expanduser("~"), ".config")


def config_dir() -> str:
    path = os.path.join(user_data_root(), APP_NAME)
    os.makedirs(path, exist_ok=True)
    return path


def config_path() -> str:
    return os.path.join(config_dir(), "settings.json")


# all possible left-to-right / top-to-bottom orders of the three gauges
GAUGE_IDS = ("fh", "mo", "sd")
GAUGE_ORDERS = ["fh,mo,sd", "fh,sd,mo", "mo,fh,sd", "mo,sd,fh", "sd,fh,mo", "sd,mo,fh"]

DEFAULTS: Dict[str, Any] = {
    # --- language
    "language": "",                  # empty = system language (if supported), else English

    # --- profile / data source
    "source": "local",               # local = Claude Desktop log | api = claude.ai server
    "org": "",                       # empty = the most recently used profile
    "data_path": "",                 # empty = default Claude path
    "refresh_seconds": 5,

    # --- appearance
    "visible": True,                 # whether the floating panel is shown (False = tray only)
    "layout": "postit",              # postit | compact | ring
    "theme": "midnight",             # see theme.THEMES
    "accent": "",                    # custom accent color (#RRGGBB), empty = theme default
    "scale": 1.0,                    # 0.7 - 2.0
    "opacity": 1.0,
    "always_on_top": True,
    "click_through": False,
    "locked": False,                 # locked in place (not draggable)
    "pos_x": None,
    "pos_y": None,
    "snap_edges": True,
    "show_in_taskbar": False,

    # --- content
    "show_five_hour": True,
    "show_weekly": True,
    "show_model": True,              # model-scoped weekly limit (claude.ai source only)
    "model_filter": "Fable",         # which model's weekly limit to show (name substring)
    "model_scale": 1.0,              # size of the model gauge relative to the others (0.5 - 2.0)
    "gauge_order": "fh,mo,sd",       # fh = 5-hour, mo = model weekly, sd = weekly
    "show_spark": True,
    # --- details: plan badge + the small list under the gauges (claude.ai source only)
    "show_plan_badge": True,
    "show_plan_name": False,         # the name stays off the always-on-top panel unless asked for
    "show_model_list": True,         # weekly windows of the other models
    "show_surfaces": True,           # per-surface windows and kinds we do not know yet
    "show_extra_usage": True,        # pay-as-you-go credit
    "show_local_models": True,       # this week's split between the models, from Claude Code's local logs
    "local_models_path": "",         # "" = find Claude Code's log folder automatically
    "detail_hidden": [],             # ids of single rows the user unticked
    "show_burn": True,
    "show_reset": True,
    "show_age": True,
    "tray_metric": "five_hour",      # five_hour | weekly | max

    # --- backups: status of the OneDrive / Nextcloud / Obsidian backup scripts
    "backup_enabled": True,          # the bar only appears where the backup system exists
    "backup_show_onedrive": True,
    "backup_show_nextcloud": True,
    "backup_show_obsidian": True,
    "backup_label": "age",           # age | name | none
    "backup_green_hours": 24,        # green: not older than this
    "backup_yellow_hours": 48,       # yellow: not older than this, red: older
    "backup_root": "",               # "" = the root from backup_profile.json (no root = feature hidden)
    "backup_config": "",             # "" = script_config from backup_profile.json
    "backup_task_filter": "",        # "" = task_filter from backup_profile.json
    "backup_d_components": True,     # details window sections
    "backup_d_contents": True,
    "backup_d_problems": True,
    "backup_d_tasks": True,
    "backup_d_log": False,

    # --- alerts
    "warn_threshold": 70,
    "danger_threshold": 90,
    "notify_enabled": True,
    "notify_on_reset": True,
    "notify_stale": True,

    # --- system
    "autostart": False,
    "start_menu": True,              # shortcut in the Start menu
    "update_check": True,            # look for a newer version on the release server
    "update_url": "",                # "" = the default release manifest
    "update_skip_version": "",       # "Skip this version" in the update window
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

    # ------------------------------------------------------------ access

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

    # ------------------------------------------------------ derived

    def resolved_data_path(self) -> str:
        return self["data_path"] or default_data_path()
