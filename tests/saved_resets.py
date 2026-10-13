# -*- coding: utf-8 -*-
"""Run:  python tests/saved_resets.py

2.8.0: the saved limit resets (cedar_ember), the "limit that applies now" marker and the
Routines (Cowork) label - parsed from synthetic server answers, no network."""
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from claude_usage import apisource, i18n, oauth  # noqa: E402
from claude_usage.datasource import detail_label  # noqa: E402

i18n.set_language("en")
P = apisource.ApiReader
now = int(time.time())


def iso(seconds_from_now: int) -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now + seconds_from_now))


LIMITS = [
    {"kind": "session", "group": "session", "percent": 40, "resets_at": iso(3600), "scope": None, "is_active": False},
    {"kind": "weekly_all", "group": "weekly", "percent": 24, "resets_at": iso(86400 * 3), "scope": None, "is_active": False},
    {"kind": "weekly_scoped", "group": "weekly", "percent": 29, "resets_at": iso(86400 * 3),
     "scope": {"model": {"id": None, "display_name": "Fable"}}, "is_active": True},
    {"kind": "seven_day_cowork", "group": "weekly", "percent": 7, "resets_at": iso(86400 * 2), "scope": None, "is_active": True},
]

# ---------------------------------------------------------------- 1) no block at all -> None, nothing shown
assert P._pick_resets({"limits": LIMITS}) is None
assert P._pick_resets({"limits": LIMITS, "cedar_ember": None}) is None
print("1) no resets block: ok")

# ---------------------------------------------------------------- 2) a grant list under the block
raw = {"limits": LIMITS, "cedar_ember": {"eligible": True, "usable_now": True, "grants": [
    {"id": "g1", "resets_left": 1, "resets_total": 1, "paused": False, "starts_at": iso(-86400), "ends_at": iso(86400 * 9)},
    {"id": "g2", "resets_left": 2, "resets_total": 2, "paused": False, "starts_at": iso(-86400), "ends_at": iso(86400 * 20)},
    {"id": "old", "resets_left": 1, "resets_total": 1, "paused": False, "starts_at": iso(-86400 * 40), "ends_at": iso(-86400)},
    {"id": "future", "resets_left": 1, "resets_total": 1, "paused": False, "starts_at": iso(86400 * 5), "ends_at": iso(86400 * 30)},
    {"id": "paused", "resets_left": 1, "resets_total": 1, "paused": True, "starts_at": iso(-86400), "ends_at": iso(86400 * 30)},
]}}
rs = P._pick_resets(raw)
assert rs is not None and rs.count == 3 and rs.total == 3 and rs.eligible, rs
assert rs.expires_at is not None and abs(rs.expires_at / 1000 - (now + 86400 * 9)) < 2, rs
assert 0 < rs.expires_in_ms <= 86400 * 9 * 1000
print("2) grant list: count=3, earliest expiry 9 days: ok")

# ---------------------------------------------------------------- 3) other shapes: a bare list, a single grant, not eligible
assert P._pick_resets({"cedar_ember": [{"resets_left": 1, "ends_at": iso(86400)}]}).count == 1
assert P._pick_resets({"cedar_ember": {"resets_left": 2, "resets_total": 3}}).count == 2
assert P._pick_resets({"cedar_ember": {"resets_left": 2, "resets_total": 3}}).total == 3
assert P._pick_resets({"cedar_ember": {"eligible": False, "grants": [{"resets_left": 1}]}}).count == 0
assert P._pick_resets({"cedar_ember": {"grants": [{"resets_left": "x"}, {"foo": 1}]}}).count == 0
assert P._pick_resets({"cedar_ember": "garbage"}).count == 0
print("3) lenient shapes: ok")

# ---------------------------------------------------------------- 4) which limit applies now
assert P._pick_active(raw, "Fable") == "mo"
assert P._pick_active(raw, "") == ""            # the active limit is a model window the app does not show
sess = dict(LIMITS[0], is_active=True)
assert P._pick_active({"limits": [sess] + LIMITS[1:]}, "Fable") == "fh"
weekly = [dict(LIMITS[0]), dict(LIMITS[1], is_active=True), dict(LIMITS[2], is_active=False)]
assert P._pick_active({"limits": weekly}, "Fable") == "sd"
assert P._pick_active({"limits": [dict(l, is_active=False) for l in LIMITS]}, "Fable") == ""
assert P._pick_active({}, "Fable") == ""
print("4) active limit -> fh / sd / mo: ok")

# ---------------------------------------------------------------- 5) the Routines (Cowork) window gets its name
rows = {r.id: r for r in P._pick_rows(raw)}
cw = rows.get("kind:seven_day_cowork")
assert cw is not None and cw.label == "@cowork" and detail_label(cw) == "Routines (Cowork)", rows.keys()
legacy = P._pick_rows({"limits": [], "seven_day_routines": {"utilization": 12, "resets_at": iso(3600)}})
assert legacy and legacy[0].label == "@cowork"
i18n.set_language("hu")
assert detail_label(cw) == "Rutinok (Cowork)"
i18n.set_language("en")
print("5) Routines (Cowork) label: ok")

# ---------------------------------------------------------------- 6) the request: resets query first, plain on 400/403
calls = []


def fake_get(url, token):
    calls.append(url)
    if url.endswith(oauth.USAGE_RESETS_QUERY):
        return None, 400, "unknown parameter", None
    return {"limits": []}, 200, "", None


orig = oauth._get_usage
oauth._get_usage = fake_get
try:
    raw2, status, _, _ = oauth.fetch_usage("tok")
    assert status == 200 and raw2 == {"limits": []}
    assert calls == [oauth.USAGE_URL + oauth.USAGE_RESETS_QUERY, oauth.USAGE_URL], calls
    calls.clear()
    oauth._get_usage = lambda url, token: ({"limits": [], "cedar_ember": None}, 200, "", None)
    assert oauth.fetch_usage("tok")[1] == 200
finally:
    oauth._get_usage = orig
print("6) cedar_ember query with plain fallback: ok")

# ---------------------------------------------------------------- 6b) the client identity: a current Claude Code version
import re  # noqa: E402

ua = oauth.client_ua()
assert re.fullmatch(r"claude-cli/\d+\.\d+\.\d+ \(external, cli\)", ua), ua
assert oauth._parse_version(oauth.cli_version()) >= oauth._parse_version(oauth.CLI_VERSION_FLOOR)
assert oauth._client_headers()["User-Agent"] == ua
assert oauth._parse_version("claude 2.1.296 (Claude Code)") == (2, 1, 296)
assert oauth._parse_version("garbage") is None
print("6b) client identity %s (installed: %s): ok" % (ua, oauth.installed_cli_version() or "-"))

# ---------------------------------------------------------------- 6c) this week by product (2.9.0)
from claude_usage.datasource import product_label  # noqa: E402

bd = {"seven_day_breakdown": {"as_of": iso(0), "window_started_at": iso(-86400 * 3), "rows": [
    {"key": "claude_code", "display_name": "Claude Code", "percent": 68},
    {"key": "chat", "display_name": "Chats", "percent": 6},
    {"key": "cowork", "display_name": "Cowork", "percent": 26},
    {"key": "other", "display_name": "Other", "percent": 0},
]}}
prods = P._pick_products(bd)
assert [(p.key, p.percent) for p in prods] == [("claude_code", 68.0), ("chat", 6.0), ("cowork", 26.0)], prods
assert product_label(prods[0]) == "Claude Code" and product_label(prods[1]) == "Chats"
i18n.set_language("hu")
assert product_label(prods[1]) == "Csevegések"
i18n.set_language("en")
assert P._pick_products({}) == [] and P._pick_products({"seven_day_breakdown": None}) == []
assert P._pick_products({"seven_day_breakdown": {"rows": [{"percent": "x"}, "junk", {"key": "", "display_name": ""}]}}) == []
print("6c) this week by product: ok")

# ---------------------------------------------------------------- 7) every new text exists in every language
for key in ("detail.resets", "detail.surface.cowork", "set.show_resets", "set.notify_resets",
            "notify.reset_available", "notify.reset_expiring", "detail.products_header", "detail.product.chat",
            "detail.product.other", "detail.product.group", "set.show_products"):
    for code in i18n.LANG_NAMES:
        text = i18n.lookup(key, code)
        assert text and text != key, (key, code)
    assert i18n.lookup("notify.reset_expiring", "hu").count("{}") == 1
print("7) texts in all %d languages: ok" % len(i18n.LANG_NAMES))

print("ALL SAVED-RESET TESTS OK")
