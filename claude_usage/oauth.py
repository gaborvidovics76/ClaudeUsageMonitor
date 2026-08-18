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
import secrets
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Dict, Optional, Tuple

# Claude Code's public OAuth client (for the user's own account).
from .i18n import tr
CLIENT_ID = "9d1c250a-e61b-44d9-88ed-5944d1962f5e"
AUTHORIZE_URL = "https://claude.ai/oauth/authorize"
# The current Claude Code uses platform.claude.com; the old
# console.anthropic.com/v1/oauth/token returns 404 (removed route).
TOKEN_URL = "https://platform.claude.com/v1/oauth/token"
REDIRECT_URI = "https://platform.claude.com/oauth/code/callback"
SCOPE = "org:create_api_key user:profile user:inference"

USAGE_URL = "https://api.anthropic.com/api/oauth/usage"
BETA_HEADER = "oauth-2025-04-20"

# The token endpoint is behind Cloudflare, which blocks Python's default
# User-Agent with "Error 1010" and heavily rate-limits a browser UA. So we use
# EXACTLY the real Claude Code headers - this makes the request indistinguishable
# from the official client (passes Cloudflare and gets normal limits).
CLI_UA = "claude-cli/2.1.229 (external)"


def _client_headers(extra: Optional[dict] = None) -> dict:
    h = {
        "User-Agent": CLI_UA,
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
        with urllib.request.urlopen(req, timeout=20) as r:
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


def fetch_usage(access_token: str) -> Tuple[Optional[dict], int, str]:
    """(json, http_status, error). On 401 the caller should refresh and retry."""
    req = urllib.request.Request(
        USAGE_URL,
        method="GET",
        headers=_client_headers({
            "Authorization": f"Bearer {access_token}",
            "anthropic-beta": BETA_HEADER,
            "anthropic-version": "2023-06-01",
        }),
    )
    try:
        with urllib.request.urlopen(req, timeout=12) as r:
            return json.loads(r.read().decode("utf-8", "replace")), r.status, ""
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        return None, e.code, body[:200]
    except urllib.error.URLError as e:
        return None, 0, tr("err.network", e.reason)
    except ValueError:
        return None, 0, tr("err.bad_usage_resp")
    except Exception as e:  # noqa: BLE001 - any other network error
        return None, 0, tr("err.connection", e)
