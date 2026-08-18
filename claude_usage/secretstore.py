"""Encrypted storage of the session key with Windows DPAPI.

DPAPI binds the secret to the signed-in user's account: another user or
another machine cannot decrypt it. No external dependency (ctypes).
"""

from __future__ import annotations

import ctypes
import os
from ctypes import wintypes
from typing import Optional

from .settings import config_dir

SECRET_FILE = "session.bin"


class _BLOB(ctypes.Structure):
    _fields_ = [("cbData", wintypes.DWORD), ("pbData", ctypes.POINTER(ctypes.c_char))]


def _blob(data: bytes) -> _BLOB:
    buf = ctypes.create_string_buffer(data, len(data))
    return _BLOB(len(data), ctypes.cast(buf, ctypes.POINTER(ctypes.c_char)))


def _crypt(func, data: bytes, entropy: bytes) -> Optional[bytes]:
    in_blob = _blob(data)
    ent_blob = _blob(entropy)
    out_blob = _BLOB()
    ok = func(ctypes.byref(in_blob), None, ctypes.byref(ent_blob),
              None, None, 0, ctypes.byref(out_blob))
    if not ok:
        return None
    try:
        return ctypes.string_at(out_blob.pbData, out_blob.cbData)
    finally:
        ctypes.windll.kernel32.LocalFree(out_blob.pbData)


_ENTROPY = b"ClaudeUsageMonitor.sessionKey.v1"


def _path() -> str:
    return os.path.join(config_dir(), SECRET_FILE)


def save_secret(value: str) -> bool:
    try:
        enc = _crypt(ctypes.windll.crypt32.CryptProtectData, value.encode("utf-8"), _ENTROPY)
        if enc is None:
            return False
        tmp = _path() + ".tmp"
        with open(tmp, "wb") as fh:
            fh.write(enc)
        os.replace(tmp, _path())
        return True
    except OSError:
        return False


def load_secret() -> Optional[str]:
    try:
        with open(_path(), "rb") as fh:
            enc = fh.read()
    except OSError:
        return None
    dec = _crypt(ctypes.windll.crypt32.CryptUnprotectData, enc, _ENTROPY)
    if dec is None:
        return None
    try:
        return dec.decode("utf-8")
    except UnicodeDecodeError:
        return None


def clear_secret() -> None:
    try:
        os.remove(_path())
    except OSError:
        pass


def has_secret() -> bool:
    return os.path.exists(_path())


# --- convenience layer: store a token dict (access/refresh/expiry) ---

def save_tokens(tokens: dict) -> bool:
    import json

    return save_secret(json.dumps(tokens))


def load_tokens() -> Optional[dict]:
    import json

    raw = load_secret()
    if not raw:
        return None
    try:
        data = json.loads(raw)
        return data if isinstance(data, dict) else None
    except ValueError:
        return None
