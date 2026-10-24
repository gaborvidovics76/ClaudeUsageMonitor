# -*- coding: utf-8 -*-
"""Run:  python tests/review_fixes.py

Regression tests for the 2.9.2 review fixes (Windows side):
  1) local source without a Claude Desktop log shows the empty-state text instead of crashing,
  2) a fetch that is refreshing while the user logs out (or signs in again) cannot write tokens back,
  3) samples filled in from the Claude Desktop log do not drag the model gauge's burn rate,
  4) the saved history keeps "no model figure" across a restart,
  5) the Start menu / scheduled-task commands survive ' and & in paths."""
import json, os, sys, tempfile, threading, time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ["APPDATA"] = tempfile.mkdtemp(prefix="um_test_")      # never touch the real config folder

from claude_usage import apisource, datasource, i18n, oauth, winutil

i18n.set_language("en")
apisource._dbg = lambda _m: None

# ---------------------------------------------------------------- 1) empty state, local source
r = datasource.UsageReader(os.path.join(os.environ["APPDATA"], "missing", "plan-usage-history.json"))
m = r.read()
assert not m.ok and "Claude Desktop" in m.error, m.error
print("1) no Claude Desktop log -> empty-state text, no crash: ok")

# ---------------------------------------------------------------- 2) logout while refreshing
release = threading.Event()
saved = []


def slow_refresh(rt):
    release.wait(5)
    return {"access_token": "new", "refresh_token": "rt2", "expires_at": time.time() + 3600}, ""


oauth.refresh = slow_refresh
oauth.fetch_usage = lambda tok, with_resets=True: ({"limits": []}, 200, "", None)
oauth.fetch_profile = lambda tok: (None, 0)
reader = apisource.ApiReader(tokens={"access_token": "old", "refresh_token": "rt", "expires_at": time.time() - 10},
                             on_tokens_changed=saved.append)
reader.read()                       # the worker starts and blocks inside the refresh
time.sleep(0.1)
reader.set_tokens({})               # the user logs out meanwhile
release.set()
while reader.busy:
    time.sleep(0.02)
assert saved == [], f"tokens written back after logout: {saved}"
assert not reader.has_tokens(), "the old fetch restored the sign-in"
print("2) logout during a token refresh: nothing written back: ok")

# ---------------------------------------------------------------- 3) backfill vs. model burn
now = int(time.time() * 1000)
H = 3_600_000
series = [datasource.Sample(t=now - 5 * H + i * 15 * 60_000, org="", fh=10, sd=40, mo_known=False) for i in range(16)]
series += [datasource.Sample(t=now - H + i * 120_000, org="", fh=12, sd=41, mo=50.0) for i in range(30)]
burn = apisource.ApiReader._burn(series, "mo", now, 6 * H)
assert burn < 1.0, f"model burn {burn:.1f}%/h - the backfilled zeros were counted"
assert apisource.ApiReader._burn(series, "sd", now, 6 * H) > 0, "the weekly figure must still use them"
print(f"3) backfilled samples skipped for the model gauge (burn {burn:.2f}%/h): ok")

# ---------------------------------------------------------------- 4) history round trip
apisource._save_history(series)
with open(apisource._history_path(), encoding="utf-8") as fh:
    rows = json.load(fh)["samples"]
assert rows[0][3] is None and rows[-1][3] == 50.0
back = apisource._load_history()
assert not back[0].mo_known and back[-1].mo_known and back[-1].mo == 50.0
print("4) 'no model figure' survives a restart: ok")

# ---------------------------------------------------------------- 5) quoting
assert winutil._ps_quote("C:\\Users\\O'Brien\\x.lnk") == "'C:\\Users\\O''Brien\\x.lnk'"
from xml.dom.minidom import parseString
from xml.sax.saxutils import escape, unescape

xml = winutil.TASK_XML.format(name="T", user=escape("PC\\Tom & Jerry"), command=escape("C:\\A&B\\x.exe"),
                              workdir=escape("C:\\A&B"))
doc = parseString(xml.replace('encoding="UTF-16"', 'encoding="UTF-8"'))
assert doc.getElementsByTagName("Command")[0].firstChild.data == "C:\\A&B\\x.exe"
assert unescape(escape("C:\\A&B\\x.exe")) == "C:\\A&B\\x.exe"
print("5) ' and & in paths: PowerShell and task XML stay valid: ok")

print("ALL REVIEW-FIX TESTS OK")
