"""The TLS trust used by every HTTPS call of the app (sign-in, usage queries, updater, feedback form).

Python's default context trusts the Windows ROOT *and* CA (intermediate) stores. Windows caches every intermediate
it has ever seen in the CA store, and only downloads a root when it needed one itself. A machine that saw the
2024-25 Let's Encrypt ECDSA chains therefore holds an expired cross-signed "ISRG Root X2" (expired 2025-09-15)
while the self-signed ISRG Root X2 root may be missing - and then OpenSSL fails claude.ai / platform.claude.com with
"certificate has expired", although browsers and PowerShell (SChannel) work (tests/tls_trust.py reproduces it).

So the Windows stores stay (corporate proxies and antivirus roots keep working) and the Mozilla root bundle of the
`certifi` package is loaded on top: with the valid root present, OpenSSL prefers it over an expired copy.
"""

from __future__ import annotations

import ssl
import threading
from typing import Optional

_lock = threading.Lock()
_ctx: Optional[ssl.SSLContext] = None
_bundle = False


def add_bundle(ctx: ssl.SSLContext) -> bool:
    """Loads the certifi root bundle into the context. False when certifi is missing or its file is unreadable:
    the context then has the platform trust only, as before."""
    try:
        import certifi

        ctx.load_verify_locations(cafile=certifi.where())
        return True
    except (ImportError, OSError, ssl.SSLError):
        return False


def context() -> ssl.SSLContext:
    """One verified-only client context for the whole process (the bundle is read once)."""
    global _ctx, _bundle
    with _lock:
        if _ctx is None:
            ctx = ssl.create_default_context()      # platform stores; verifies the certificate and the host name
            ctx.minimum_version = ssl.TLSVersion.TLSv1_2
            _bundle = add_bundle(ctx)
            _ctx = ctx
        return _ctx


def trust_summary() -> str:
    """For the log: "platform stores + certifi" or, when the bundle is missing from the build, "platform stores only"."""
    context()
    return "platform stores + certifi" if _bundle else "platform stores only"
