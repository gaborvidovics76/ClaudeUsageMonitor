"""Token storage on macOS: the login Keychain.

First choice is the `keyring` package (talks to the Keychain through the Security framework;
the secret never appears on a command line). If it is not available in this build, the
system's own `/usr/bin/security` tool is used instead. The secret is never written to a file.

Note for rebuilt / self-updated apps: an ad-hoc signed build gets a new code signature with
every build, so macOS may ask once more whether the app may read its Keychain item.
"""

from __future__ import annotations

import getpass
import subprocess
from typing import Optional

SERVICE = "ClaudeUsageMonitor"


def _account() -> str:
    try:
        return getpass.getuser() or "default"
    except Exception:  # noqa: BLE001
        return "default"


def _keyring():
    try:
        import keyring
        from keyring.backends import macOS

        backend = macOS.Keyring()
        keyring.set_keyring(backend)      # explicit: entry-point discovery does not work when frozen
        return keyring
    except Exception:  # noqa: BLE001 - not installed / not usable -> CLI fallback
        return None


def _security(*args: str, secret_in_args: bool = False) -> Optional[str]:
    try:
        res = subprocess.run(["/usr/bin/security", *args], capture_output=True, text=True, timeout=20,
                             stdin=subprocess.DEVNULL)
    except (OSError, subprocess.SubprocessError):
        return None
    return res.stdout if res.returncode == 0 else None


def save_secret(value: str) -> bool:
    kr = _keyring()
    if kr is not None:
        try:
            kr.set_password(SERVICE, _account(), value)
            return True
        except Exception:  # noqa: BLE001
            pass
    return _security("add-generic-password", "-U", "-a", _account(), "-s", SERVICE,
                     "-w", value, secret_in_args=True) is not None


def load_secret() -> Optional[str]:
    kr = _keyring()
    if kr is not None:
        try:
            got = kr.get_password(SERVICE, _account())
            if got:
                return got
        except Exception:  # noqa: BLE001
            pass
    out = _security("find-generic-password", "-a", _account(), "-s", SERVICE, "-w")
    return out.rstrip("\n") if out else None


def clear_secret() -> None:
    kr = _keyring()
    if kr is not None:
        try:
            kr.delete_password(SERVICE, _account())
        except Exception:  # noqa: BLE001
            pass
    _security("delete-generic-password", "-a", _account(), "-s", SERVICE)


def has_secret() -> bool:
    return bool(load_secret())
