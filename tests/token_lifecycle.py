# -*- coding: utf-8 -*-
"""Run:  python tests/token_lifecycle.py

The sign-in lifecycle: a finished refresh token must stop the polling, must never show
raw HTTP/JSON, and must let the user back in; the access token is renewed BEFORE it expires."""
import os, sys, time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from claude_usage import apisource, oauth, i18n

i18n.set_language("hu")
logged = []
apisource._dbg = logged.append
USAGE = ({"limits": [{"kind": "session", "group": "session", "percent": 7, "resets_at": None, "scope": {}}]}, 200, "", None)
DEAD = 'HTTP 400: {"error": "invalid_grant", "error_description": "Refresh token expired"}'

def ascii(s):
    return s.encode("ascii", "replace").decode()

# ---------------------------------------------------------------- 0) the classifier
assert oauth.is_dead_grant(DEAD)
assert oauth.is_dead_grant('HTTP 400: {"error":"invalid_grant"}')
assert not oauth.is_dead_grant("halozati hiba: [Errno 11001] getaddrinfo failed")
assert not oauth.is_dead_grant("HTTP 500: server error")
assert not oauth.is_dead_grant("")
print("0) dead-grant classifier: ok")

# ---------------------------------------------------------------- 1) THE LIVE BUG
calls = {"refresh": 0, "usage": 0}
def dead_refresh(rt):
    calls["refresh"] += 1
    return None, DEAD
def usage(tok):
    calls["usage"] += 1
    return USAGE
oauth.refresh, oauth.fetch_usage = dead_refresh, usage

r = apisource.ApiReader(tokens={"access_token": "old", "refresh_token": "rt", "expires_at": time.time() - 10})
m = r.read()                      # first tick: discovers the sign-in is finished
while r.busy: time.sleep(0.02)
for _ in range(40):               # the panel keeps ticking for ~80 minutes' worth of polls
    r.read(); time.sleep(0.01)
    while r.busy: time.sleep(0.01)
print(f"1) refresh attempts after the token died: {calls['refresh']}  (before the fix: one every 2 min, forever)")
assert calls["refresh"] == 1, calls
assert calls["usage"] == 0
assert r.needs_login is True
msg = r.read().error
print("   panel text:", ascii(msg))
assert "HTTP" not in msg and "invalid_grant" not in msg and "{" not in msg, "raw server answer must never reach the panel"
assert "claude.ai" in msg and "jelentkez" in msg.lower()
assert any("sign-in finished" in x for x in logged), "the raw answer must still be in api.log"
assert any(DEAD in x for x in logged)
print("   api.log keeps the technical detail: ok")

# a manual 'refresh now' must not start hammering either
r.force_refresh(); time.sleep(0.05)
while r.busy: time.sleep(0.01)
assert calls["refresh"] == 1, "even a forced refresh must not retry a finished grant"
print("   forced refresh does not retry: ok")

# ---------------------------------------------------------------- 2) signing in again clears it
r.set_tokens({"access_token": "new", "refresh_token": "rt2", "expires_at": time.time() + 3600})
assert r.needs_login is False
m = r.read()
while r.busy: time.sleep(0.02)
m = r.read()
print(f"2) after a new sign-in: usage calls={calls['usage']}, ok={m.ok}, error={ascii(m.error)!r}")
assert m.ok and calls["usage"] >= 1

# ---------------------------------------------------------------- 3) proactive refresh
renewed = {"n": 0}
def good_refresh(rt):
    renewed["n"] += 1
    return {"access_token": "fresh", "refresh_token": "rt3", "expires_at": time.time() + 3600}, ""
oauth.refresh = good_refresh
saved = []
r2 = apisource.ApiReader(tokens={"access_token": "a", "refresh_token": "rt", "expires_at": time.time() + 10 * 60},
                         on_tokens_changed=saved.append)
r2.read()                          # token still valid for 10 minutes -> the old code did nothing
while r2.busy: time.sleep(0.02)
print(f"3) token with 10 minutes left -> refreshed: {renewed['n'] == 1}, persisted: {len(saved) == 1}")
assert renewed["n"] == 1 and saved and saved[0]["refresh_token"] == "rt3"
r3 = apisource.ApiReader(tokens={"access_token": "a", "refresh_token": "rt", "expires_at": time.time() + 3600})
r3.read()
while r3.busy: time.sleep(0.02)
assert renewed["n"] == 1, "a token with an hour left must not be refreshed"
print("   token with an hour left: not touched: ok")

# ---------------------------------------------------------------- 4) offline early refresh keeps working
oauth.refresh = lambda rt: (None, "halozati hiba: [Errno 11001] getaddrinfo failed")
calls["usage"] = 0
r4 = apisource.ApiReader(tokens={"access_token": "still-valid", "refresh_token": "rt", "expires_at": time.time() + 5 * 60})
m = r4.read()
while r4.busy: time.sleep(0.02)
m = r4.read()
print(f"4) early refresh fails but the token is still valid -> usage calls={calls['usage']}, needs_login={r4.needs_login}")
assert calls["usage"] == 1 and r4.needs_login is False and m.ok

# ---------------------------------------------------------------- 5) genuinely expired + no network = plain error, still retryable
r5 = apisource.ApiReader(tokens={"access_token": "old", "refresh_token": "rt", "expires_at": time.time() - 10})
r5.read()
while r5.busy: time.sleep(0.02)
e = r5.read().error
print("5) expired token, no network:", ascii(e), "| needs_login:", r5.needs_login)
assert r5.needs_login is False and "HTTP" not in e
print("ALL TOKEN-LIFECYCLE TESTS OK")
