"""A second start of the program asks the running instance to open its Settings window.

Only one instance runs at a time. When the panel is in click-through mode it ignores the mouse, so the right-click
menu is out of reach; the tray icon still works, but on Windows 11 it usually sits in the hidden overflow. Starting
the program again (Start menu, desktop shortcut) is what people try next - so that start leaves a marker file and
exits, and the running instance picks it up within a second and opens Settings. Nothing but the file name is
written; the file lives in the settings folder and is removed as soon as it is consumed.
"""

from __future__ import annotations

import os

from .settings import config_dir

MARKER = "open-settings"


def _path() -> str:
    return os.path.join(config_dir(), MARKER)


def request() -> bool:
    """Leaves the marker for the running instance. False when the settings folder is not writable."""
    try:
        with open(_path(), "w", encoding="utf-8") as fh:
            fh.write("open the Settings window\n")
        return True
    except OSError:
        return False


def consume() -> bool:
    """True once per request: removes the marker when it is there."""
    path = _path()
    if not os.path.exists(path):
        return False
    try:
        os.remove(path)
    except OSError:
        return False
    return True
