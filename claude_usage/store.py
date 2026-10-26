"""Microsoft Store (MSIX) package: detection and the product name the Store knows the app by.

Kept free of Qt and of the rest of the package, so settings.py and i18n.py can use it at import time.
The ZIP install from the website keeps its own name; inside the Store package the program shows the name
reserved in Partner Center everywhere (window titles, tray, notifications, texts), so the Store listing,
the Start menu entry and the running program all say the same.
"""

from __future__ import annotations

import os
import sys
from typing import Optional

BRAND = "Claude Usage Monitor"                  # the website / ZIP install
STORE_NAME = "Usage Monitor for Claude AI"      # = packaging\msix\identity.json "display_name" (Partner Center)

_PACKAGED: Optional[bool] = None
_FAMILY: Optional[str] = None


def package_family_name() -> str:
    """The MSIX package family name when running from a package, else ""."""
    global _FAMILY
    if _FAMILY is not None:
        return _FAMILY
    _FAMILY = ""
    if sys.platform.startswith("win"):
        try:
            import ctypes
            from ctypes import wintypes

            fn = ctypes.windll.kernel32.GetCurrentPackageFamilyName
            length = wintypes.UINT(0)
            rc = fn(ctypes.byref(length), None)
            if rc != 15700 and length.value:          # 15700 = APPMODEL_ERROR_NO_PACKAGE
                buf = ctypes.create_unicode_buffer(length.value)
                if fn(ctypes.byref(length), buf) == 0:
                    _FAMILY = buf.value
        except (AttributeError, OSError):
            pass
    return _FAMILY


def is_packaged() -> bool:
    """True when running from the Microsoft Store (MSIX) package. CLAUDE_USAGE_MONITOR_PACKAGED=1 forces it
    on for testing the packaged behaviour from a normal install."""
    global _PACKAGED
    if _PACKAGED is None:
        _PACKAGED = os.environ.get("CLAUDE_USAGE_MONITOR_PACKAGED") == "1" or bool(package_family_name())
    return _PACKAGED


def app_title() -> str:
    return STORE_NAME if is_packaged() else BRAND


def rebrand(text: str) -> str:
    """Texts that name the program (privacy notice, backup disclaimer ...) use the Store name in the package."""
    if text and BRAND in text and is_packaged():
        return text.replace(BRAND, STORE_NAME)
    return text
