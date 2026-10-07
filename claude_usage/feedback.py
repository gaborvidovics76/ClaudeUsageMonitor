"""'Message to the developer' - sends the form to the project's own website over HTTPS.

Nothing leaves the machine unless the user presses Send; the panel never phones home by itself.
Transport: TLS 1.2+ with certificate verification, a JSON body, no cookies, no device id.
The server (claudeusagemonitor.com/usage-api/app-feedback.php) stores the message for the
author's admin page and - if the author switched it on - forwards it by e-mail.
"""

from __future__ import annotations

import json
import platform
import ssl
import sys
import threading
import urllib.error
import urllib.parse
import urllib.request
from typing import Callable, Dict, Optional, Tuple

from . import __version__

FEEDBACK_URL = "https://claudeusagemonitor.com/usage-api/app-feedback.php"
CONSENT_VERSION = "2026-10-06"      # bump when the privacy notice text changes
TIMEOUT_S = 20.0
MAX_NAME = 80
MAX_EMAIL = 120
MAX_MESSAGE = 4000

# set from the command line (--feedback-url=http://127.0.0.1:8765/app-feedback.php) for local tests only
override_url = ""

# error codes the dialog can show (anything else -> "server")
ERRORS = ("rate", "fields", "email", "consent", "links", "server", "network", "client")


def os_name() -> str:
    """'Windows 11 (10.0.26200)' / 'macOS 15.1 (arm64)' - no user name, no machine name."""
    try:
        if sys.platform == "darwin":
            ver = platform.mac_ver()[0] or platform.release()
            return f"macOS {ver} ({platform.machine()})"
        if sys.platform.startswith("win"):
            rel, ver = platform.release(), platform.version()
            try:
                build = int(ver.split(".")[2])
                if rel == "10" and build >= 22000:
                    rel = "11"
            except (IndexError, ValueError):
                pass
            return f"Windows {rel} ({ver})"
        return f"{platform.system()} {platform.release()}"
    except Exception:  # noqa: BLE001 - never let a metadata lookup break the form
        return sys.platform


def _is_local_test(url: str) -> bool:
    host = urllib.parse.urlparse(url).hostname or ""
    return host in ("127.0.0.1", "localhost")


def target_url() -> str:
    url = override_url or FEEDBACK_URL
    parts = urllib.parse.urlparse(url)
    if parts.scheme == "https" and parts.hostname:
        return url
    if parts.scheme == "http" and _is_local_test(url):
        return url
    return FEEDBACK_URL


def _tls_context() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    ctx.check_hostname = True
    ctx.verify_mode = ssl.CERT_REQUIRED
    return ctx


def build_payload(name: str, email: str, message: str, rating: int, publish: bool, lang: str) -> Dict:
    return {
        "client": "app",
        "version": __version__,
        "os": os_name(),
        "lang": lang,
        "name": (name or "").strip()[:MAX_NAME],
        "email": (email or "").strip()[:MAX_EMAIL],
        "message": (message or "").strip()[:MAX_MESSAGE],
        "rating": int(rating) if 1 <= int(rating) <= 5 else 0,
        "publish": 1 if (publish and 1 <= int(rating) <= 5) else 0,
        "consent": 1,
        "consent_version": CONSENT_VERSION,
        "website": "",                      # honeypot - a real client leaves it empty
    }


def send(payload: Dict, url: str = "") -> Tuple[bool, str]:
    """Posts the form. Returns (ok, error_code); error codes are listed in ERRORS."""
    url = url or target_url()
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST", headers={
        "User-Agent": f"ClaudeUsageMonitor/{__version__}",
        "X-UM-Client": f"ClaudeUsageMonitor/{__version__}",
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json",
        "Cache-Control": "no-cache",
    })
    try:
        kw = {"timeout": TIMEOUT_S}
        if url.startswith("https://"):
            kw["context"] = _tls_context()
        with urllib.request.urlopen(req, **kw) as resp:
            data = json.loads(resp.read(20000).decode("utf-8", "replace") or "{}")
    except urllib.error.HTTPError as e:
        try:
            data = json.loads(e.read(20000).decode("utf-8", "replace") or "{}")
        except Exception:  # noqa: BLE001
            data = {}
        if e.code == 429:
            return False, "rate"
        code = str(data.get("error") or "")
        return False, code if code in ERRORS else "server"
    except (urllib.error.URLError, OSError, ValueError):
        return False, "network"
    if isinstance(data, dict) and data.get("ok"):
        return True, ""
    code = str(data.get("error") or "") if isinstance(data, dict) else ""
    return False, code if code in ERRORS else "server"


class Sender:
    """Runs send() on a worker thread; `done(ok, code)` is called from that thread."""

    def __init__(self) -> None:
        self._thread: Optional[threading.Thread] = None

    @property
    def busy(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

    def start(self, payload: Dict, done: Callable[[bool, str], None]) -> bool:
        if self.busy:
            return False

        def run() -> None:
            try:
                ok, code = send(payload)
            except Exception:  # noqa: BLE001 - the dialog must always get an answer
                ok, code = False, "client"
            done(ok, code)

        self._thread = threading.Thread(target=run, name="feedback-send", daemon=True)
        self._thread.start()
        return True
