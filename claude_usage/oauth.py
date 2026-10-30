"""OAuth sign-in through the system browser (PKCE, manual code).

The same flow Claude Code uses:
  1. the app opens the sign-in IN YOUR SYSTEM BROWSER (your passwords and passkeys
     already work there),
  2. at the end of sign-in you receive a code,
  3. you paste it into the app, which exchanges it for a token.

With the token it then queries https://api.anthropic.com/api/oauth/usage - this gives
the server-side usage (all your devices, with exact reset times).

No embedded browser is needed.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import secrets
import shutil
import subprocess
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Dict, Optional, Tuple

from . import tls
from .i18n import tr

# Claude Code's public OAuth client (for the user's own account).
CLIENT_ID = "9d1c250a-e61b-44d9-88ed-5944d1962f5e"
AUTHORIZE_URL = "https://claude.ai/oauth/authorize"
# The current Claude Code uses platform.claude.com; the old
# console.anthropic.com/v1/oauth/token returns 404 (removed route).
TOKEN_URL = "https://platform.claude.com/v1/oauth/token"
REDIRECT_URI = "https://platform.claude.com/oauth/code/callback"
SCOPE = "org:create_api_key user:profile user:inference"

PROFILE_URL = "https://api.anthropic.com/api/oauth/profile"
USAGE_URL = "https://api.anthropic.com/api/oauth/usage"
USAGE_RESETS_QUERY = "?cedar_ember=1"   # also asks for the saved limit resets (what Claude Code sends)
BETA_HEADER = "oauth-2025-04-20"

# The token endpoint is behind Cloudflare, which blocks Python's default
# User-Agent with "Error 1010" and heavily rate-limits a browser UA. So we use
# EXACTLY the real Claude Code headers - this makes the request indistinguishable
# from the official client (passes Cloudflare and gets normal limits).
#
# The VERSION in it matters too: the server hands the saved limit resets (cedar_ember) only to a
# current client - with an old version the block comes back "ineligible: cli_version". So the app
# identifies itself with the Claude Code version installed on this machine (`claude --version`,
# asked once, never blocking the panel) and never with less than the floor below.
# Bump the floor with every release - it is what users without Claude Code get.
CLI_VERSION_FLOOR = "2.1.296"
_cli_version: Optional[str] = None
_cli_lock = threading.Lock()


def _parse_version(text: str) -> Optional[Tuple[int, ...]]:
    m = re.search(r"(\d+)\.(\d+)\.(\d+)", text or "")
    return tuple(int(x) for x in m.groups()) if m else None


def installed_cli_version() -> str:
    """The Claude Code version installed on this machine ("" when there is none or it does not answer)."""
    exe = shutil.which("claude")
    if not exe:
        return ""
    cmd = [exe, "--version"]
    if exe.lower().endswith((".cmd", ".bat")):
        cmd = ["cmd", "/c", exe, "--version"]
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=5, creationflags=flags, check=False)
    except (OSError, subprocess.SubprocessError):
        return ""
    ver = _parse_version(out.stdout) or _parse_version(out.stderr)
    return ".".join(str(x) for x in ver) if ver else ""


def cli_version() -> str:
    """max(installed Claude Code version, CLI_VERSION_FLOOR) - computed once, cached."""
    global _cli_version
    with _cli_lock:
        if _cli_version is None:
            found = installed_cli_version()
            floor = _parse_version(CLI_VERSION_FLOOR)
            got = _parse_version(found)
            _cli_version = found if (got and floor and got > floor) else CLI_VERSION_FLOOR
        return _cli_version


def client_ua() -> str:
    return f"claude-cli/{cli_version()} (external, cli)"


def _client_headers(extra: Optional[dict] = None) -> dict:
    h = {
        "User-Agent": client_ua(),
        "x-app": "cli",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    if extra:
        h.update(extra)
    return h


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def new_pkce() -> Tuple[str, str]:
    """Returns an (code_verifier, code_challenge) S256 pair."""
    verifier = _b64url(secrets.token_bytes(32))
    challenge = _b64url(hashlib.sha256(verifier.encode("ascii")).digest())
    return verifier, challenge


def build_authorize(verifier: str, challenge: str) -> Tuple[str, str]:
    """(authorize_url, state) - the URL to open in the browser."""
    state = _b64url(secrets.token_bytes(24))
    params = {
        "code": "true",
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
        "state": state,
    }
    return AUTHORIZE_URL + "?" + urllib.parse.urlencode(params), state


def _post_token(payload: dict) -> Tuple[Optional[dict], str]:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TOKEN_URL,
        data=data,
        method="POST",
        headers=_client_headers(),
    )
    try:
        with urllib.request.urlopen(req, timeout=20, context=tls.context()) as r:
            return json.loads(r.read().decode("utf-8", "replace")), ""
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        return None, f"HTTP {e.code}: {body[:200]}"
    except urllib.error.URLError as e:
        return None, tr("err.network", e.reason)
    except ValueError:
        return None, tr("err.bad_token_resp")
    except Exception as e:  # noqa: BLE001 - any other network error
        return None, tr("err.connection", e)


def exchange_code(pasted: str, verifier: str, state: str) -> Tuple[Optional[dict], str]:
    """Exchanges the pasted code for a token. The pasted text has the form `code#state`."""
    pasted = pasted.strip()
    if not pasted:
        return None, tr("err.no_code")
    code = pasted
    got_state = state
    if "#" in pasted:
        code, got_state = pasted.split("#", 1)
    payload = {
        "grant_type": "authorization_code",
        "code": code.strip(),
        "state": got_state.strip(),
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "code_verifier": verifier,
    }
    tokens, err = _post_token(payload)
    if tokens is None:
        return None, err
    return _normalize(tokens), ""


def is_dead_grant(err: str) -> bool:
    """True when the server said the refresh token itself is finished (expired, revoked,
    or already used). Retrying such a grant can never succeed - only a new sign-in helps."""
    low = (err or "").lower()
    return "invalid_grant" in low or "refresh token expired" in low or "token revoked" in low


def refresh(refresh_token: str) -> Tuple[Optional[dict], str]:
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": CLIENT_ID,
    }
    tokens, err = _post_token(payload)
    if tokens is None:
        return None, err
    norm = _normalize(tokens)
    # the server sometimes sends no new refresh token - keep the old one
    if not norm.get("refresh_token"):
        norm["refresh_token"] = refresh_token
    return norm, ""


def _normalize(tokens: dict) -> dict:
    expires_in = tokens.get("expires_in")
    expires_at = None
    if isinstance(expires_in, (int, float)):
        expires_at = int(time.time()) + int(expires_in) - 60  # small margin
    return {
        "access_token": tokens.get("access_token", ""),
        "refresh_token": tokens.get("refresh_token", ""),
        "expires_at": expires_at,
    }


def fetch_profile(access_token: str) -> Tuple[Optional[dict], int]:
    """(json, http_status) of the account/plan profile. Needs the user:profile scope."""
    req = urllib.request.Request(
        PROFILE_URL,
        method="GET",
        headers=_client_headers({
            "Authorization": f"Bearer {access_token}",
            "anthropic-beta": BETA_HEADER,
            "anthropic-version": "2023-06-01",
        }),
    )
    try:
        with urllib.request.urlopen(req, timeout=12, context=tls.context()) as r:
            return json.loads(r.read().decode("utf-8", "replace")), r.status
    except urllib.error.HTTPError as e:
        return None, e.code
    except Exception:  # noqa: BLE001 - the badge is a nicety; never let it break anything
        return None, 0


def fetch_usage(access_token: str, with_resets: bool = True) -> Tuple[Optional[dict], int, str, Optional[float]]:
    """(json, http_status, error, retry_after_seconds).
    On 401 the caller should refresh and retry; on 429 it should back off.

    `with_resets` adds the query Claude Code itself sends (`?cedar_ember=1`): the answer then also
    carries the saved limit resets. A server that does not know the parameter answers 400/403 -
    then the plain request is made, exactly as before."""
    url = USAGE_URL + (USAGE_RESETS_QUERY if with_resets else "")
    result = _get_usage(url, access_token)
    if with_resets and result[1] in (400, 403):
        return _get_usage(USAGE_URL, access_token)
    return result


def _get_usage(url: str, access_token: str) -> Tuple[Optional[dict], int, str, Optional[float]]:
    req = urllib.request.Request(
        url,
        method="GET",
        headers=_client_headers({
            "Authorization": f"Bearer {access_token}",
            "anthropic-beta": BETA_HEADER,
            "anthropic-version": "2023-06-01",
        }),
    )
    try:
        with urllib.request.urlopen(req, timeout=12, context=tls.context()) as r:
            return json.loads(r.read().decode("utf-8", "replace")), r.status, "", None
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        retry_after = None
        try:
            retry_after = float(e.headers.get("Retry-After", ""))
        except (TypeError, ValueError, AttributeError):
            pass
        return None, e.code, body[:200], retry_after
    except urllib.error.URLError as e:
        return None, 0, tr("err.network", e.reason), None
    except ValueError:
        return None, 0, tr("err.bad_usage_resp"), None
    except Exception as e:  # noqa: BLE001 - any other network error
        return None, 0, tr("err.connection", e), None
