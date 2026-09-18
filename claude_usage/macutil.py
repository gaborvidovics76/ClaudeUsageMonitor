"""macOS counterparts of the Windows helpers in winutil.py.

winutil imports these names at its end when running on macOS, so every call site keeps
saying ``winutil.something`` and the Windows code path stays exactly as it was.

* start with the system  -> a per-user LaunchAgent (~/Library/LaunchAgents)
* Start menu shortcut    -> does not exist on macOS (the .app in /Applications is the entry)
* "Installed apps" entry -> does not exist on macOS
"""

from __future__ import annotations

import os
import plistlib
import subprocess
import sys
from typing import Optional

BUNDLE_ID = "hu.dinorr.claudeusagemonitor"
AGENT_FILE = BUNDLE_ID + ".plist"


def agent_path() -> str:
    return os.path.join(os.path.expanduser("~"), "Library", "LaunchAgents", AGENT_FILE)


def app_bundle_path() -> Optional[str]:
    """…/ClaudeUsageMonitor.app when running from a bundle, else None."""
    exe = os.path.abspath(sys.executable)
    marker = ".app" + os.sep + "Contents" + os.sep + "MacOS" + os.sep
    if getattr(sys, "frozen", False) and marker in exe:
        return exe[: exe.index(marker) + len(".app")]
    return None


def launch_arguments() -> list:
    if getattr(sys, "frozen", False):
        return [os.path.abspath(sys.executable)]
    script = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "main.py"))
    return [os.path.abspath(sys.executable), script]


def launch_command() -> str:
    return " ".join(f'"{a}"' for a in launch_arguments())


def exe_path() -> str:
    return os.path.abspath(sys.executable)


# --------------------------------------------------------------------------- autostart


def _read_agent() -> Optional[dict]:
    try:
        with open(agent_path(), "rb") as fh:
            data = plistlib.load(fh)
        return data if isinstance(data, dict) else None
    except (OSError, ValueError, plistlib.InvalidFileException):
        return None


def autostart_command() -> Optional[str]:
    data = _read_agent()
    if not data:
        return None
    args = data.get("ProgramArguments")
    return " ".join(f'"{a}"' for a in args) if isinstance(args, list) else None


def autostart_method() -> str:
    return "launchagent" if _read_agent() else ""


def autostart_enabled() -> bool:
    return bool(_read_agent())


def set_autostart(enabled: bool) -> bool:
    path = agent_path()
    if not enabled:
        try:
            if os.path.exists(path):
                os.remove(path)
            return True
        except OSError:
            return False
    data = {
        "Label": BUNDLE_ID,
        "ProgramArguments": launch_arguments(),
        "RunAtLoad": True,              # "load" happens at login; we never load it by hand,
        "ProcessType": "Interactive",   # otherwise a second copy would start right now
        "LimitLoadToSessionType": "Aqua",
    }
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + ".tmp"
        with open(tmp, "wb") as fh:
            plistlib.dump(data, fh)
        os.replace(tmp, path)
        return True
    except OSError:
        return False


def sync_autostart() -> bool:
    """If the app was moved (e.g. from Downloads to /Applications), point the agent at it."""
    data = _read_agent()
    if not data:
        return False
    if data.get("ProgramArguments") != launch_arguments():
        set_autostart(True)
    return True


# --------------------------------------------------------------------------- things macOS does not have


def start_menu_path() -> str:
    return ""


def start_menu_exists() -> bool:
    return False


def create_start_menu_shortcut() -> bool:
    return False


def remove_start_menu_shortcut() -> None:
    return None


def ensure_start_menu_shortcut() -> None:
    return None


def sync_installed_version(version: str) -> None:
    return None


# --------------------------------------------------------------------------- misc


def open_path(path: str) -> None:
    """Show a file or folder with the default application (Finder for folders)."""
    try:
        subprocess.Popen(["/usr/bin/open", path], stdin=subprocess.DEVNULL,
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except OSError:
        pass
