"""Builds Resources/Localizable.xcstrings (Apple String Catalog) from the Windows app's translations.

    python macos/Xcode/tools/gen_xcstrings.py          # from the repository root
    python macos/Xcode/tools/gen_xcstrings.py --check  # only report, do not write

Sources, in this order (later ones override):
  1. claude_usage/i18n*.py + claude_usage/langs/*.py  - the shared translations (macOS wording applied)
  2. tools/extra_strings.json                         - keys that exist only in the macOS/App Store app

Only the keys the Swift sources actually use are emitted (every quoted literal in the .swift files is
matched against the key set), plus whole key families that are built at run time ("theme.*",
"layout.*", "size.*", "source.*", "set.show_*"). Keep the "{}" placeholders: the app fills them itself.
"""
from __future__ import annotations

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
XCODE = os.path.abspath(os.path.join(HERE, ".."))
ROOT = os.path.abspath(os.path.join(XCODE, "..", ".."))
SRC = os.path.join(XCODE, "ClaudeUsageMonitor")
OUT = os.path.join(SRC, "Resources", "Localizable.xcstrings")
EXTRA = os.path.join(HERE, "extra_strings.json")

sys.path.insert(0, ROOT)
from claude_usage import i18n  # noqa: E402
from claude_usage.langs import load_into  # noqa: E402
from claude_usage.i18n_mac import STRINGS_MAC  # noqa: E402

# app language code -> Apple locale identifier (.lproj folder name)
APPLE = {"es-ES": "es", "zh-CN": "zh-Hans", "zh-TW": "zh-Hant"}
# keys built at run time from a prefix + a value
DYNAMIC_PREFIXES = ("theme.", "layout.", "size.", "source.", "set.show_", "fb.err_")


def load_strings() -> dict:
    load_into(i18n.STRINGS, darwin=True)
    strings = {k: dict(v) for k, v in i18n.STRINGS.items()}
    for key, table in STRINGS_MAC.items():
        strings.setdefault(key, {}).update(table)
    if os.path.exists(EXTRA):
        with open(EXTRA, encoding="utf-8") as fh:
            for key, table in json.load(fh).items():
                if key.startswith("_"):
                    continue
                strings.setdefault(key, {}).update(table)
    # the undivided "pt"/"es" columns were the old base texts: they only serve as a fallback
    for key, table in strings.items():
        for old, variants in (("pt", ("pt-PT", "pt-BR")), ("es", ("es-ES", "es-419"))):
            if old in table:
                for v in variants:
                    table.setdefault(v, table[old])
                del table[old]
    return strings


def used_keys(strings: dict) -> set:
    keys = set()
    literal = re.compile(r'"([a-z][a-z0-9_]*(?:\.[a-z0-9_]+)+)"')
    for dirpath, _dirs, files in os.walk(SRC):
        for fn in files:
            if not fn.endswith(".swift"):
                continue
            with open(os.path.join(dirpath, fn), encoding="utf-8") as fh:
                for m in literal.finditer(fh.read()):
                    if m.group(1) in strings:
                        keys.add(m.group(1))
    for key in strings:
        if key.startswith(DYNAMIC_PREFIXES):
            keys.add(key)
    return keys


def build(strings: dict, keys: set) -> dict:
    langs = [code for code in i18n.LANG_NAMES]
    out = {"sourceLanguage": "en", "version": "1.0", "strings": {}}
    for key in sorted(keys):
        table = strings[key]
        if not table.get("en"):
            raise SystemExit(f"{key}: no English text")
        locs = {}
        for code in langs:
            text = table.get(code)
            if not text:
                continue
            locs[APPLE.get(code, code)] = {"stringUnit": {"state": "translated", "value": text}}
        out["strings"][key] = {"extractionState": "manual", "localizations": locs}
    return out


def main() -> int:
    check = "--check" in sys.argv
    strings = load_strings()
    keys = used_keys(strings)
    missing = sorted(k for k in keys if k not in strings)
    if missing:
        print("keys used by the Swift sources but unknown:", missing)
        return 1
    catalog = build(strings, keys)
    n_lang = {}
    for entry in catalog["strings"].values():
        for code in entry["localizations"]:
            n_lang[code] = n_lang.get(code, 0) + 1
    total = len(catalog["strings"])
    print(f"{total} keys; coverage: " + ", ".join(f"{c}={n}" for c, n in sorted(n_lang.items())))
    incomplete = [c for c, n in n_lang.items() if n < total]
    if incomplete:
        print("languages that fall back to English for some keys:", ", ".join(sorted(incomplete)))
    if check:
        return 0
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(catalog, fh, ensure_ascii=False, indent=2, sort_keys=True)
        fh.write("\n")
    print("wrote", os.path.relpath(OUT, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
