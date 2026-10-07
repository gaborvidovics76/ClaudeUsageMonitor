"""Checks every language of the UI strings. Exit code 1 when something is wrong.

    python tools/check_i18n.py            # all languages
    python tools/check_i18n.py ja ko      # only these

Checks (per key and language):
  - every language code of LANG_NAMES has a text for every key (after the fallback-free lookup)
  - the format placeholders match the English ({} count, named fields, numbered fields)
  - str.format runs with sample arguments
  - the number of "\\n" line breaks matches the English
  - no empty text; no text identical to the English (except the NO_TRANSLATE list / pure symbols)
  - vi: NFC-normalised; ro: no cedilla s/t; el: no accented capitals in UPPERCASE panel labels;
    bg: no Russian-only letters; CJK: Latin words only from the NO_TRANSLATE list;
    zh-TW: unchanged by OpenCC s2twp; zh-CN: unchanged by OpenCC t2s (when opencc is installed)
  - every claude_usage/langs module imports cleanly
"""

from __future__ import annotations

import os
import re
import string
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]

from claude_usage import i18n  # noqa: E402
from claude_usage import langs  # noqa: E402

# words that may stay as they are in any language (product names, formats, units, protocols)
NO_TRANSLATE = {
    "claude", "claude desktop", "claude code", "claude.ai", "anthropic", "fable", "opus", "sonnet", "haiku",
    "pro", "max", "team", "enterprise", "onedrive", "nextcloud", "obsidian", "rclone", "powershell", "http",
    "https", "json", "oauth", "sha-256", "sha256", "dpapi", "github", "mit", "claudeusagemonitor.com", "windows",
    "macos", "api", "utc", "url", "id", "ok", "pdf", "csv", "html", "css", "tls", "gdpr", "naih", "naih.hu",
    "keychain", "smartscreen", "fable 5.1", "claude usage monitor", "usage monitor", "monitor", "backup kit",
    "claude backup kit", "e-mail", "email", "wi-fi", "cpu", "ram", "ui", "cli", "exe", "zip", "log", "app",
    "python", "pyside6", "qt", "ctrl", "alt", "shift", "esc", "tab", "x", "min", "hu", "en", "de", "nimbus quill",
}
SYMBOL_ONLY = re.compile(r"^[\s\d%{}:.,;/\-–—+×·•…()\[\]!?°\"'’‘“”«»|_*#&=<>→←↑↓✓✗⚠🔒]*$")
CJK_RANGE = re.compile(r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af\uf900-\ufaff]")
LATIN_WORD = re.compile(r"[A-Za-z][A-Za-z0-9.\-']*")
HTML_TAG = re.compile(r"<[^>]+>|&[a-z]+;|\{[a-z_0-9]*\}")

SAMPLE = {"": "X", "site": "https://example.com", "cfg": "C:/x", "d": "1", "h": "2", "m": "3", "s": "4"}


def fields(text: str):
    """(positional_count, named_set, numbered_set) from str.Formatter."""
    pos, named, numbered = 0, set(), set()
    try:
        for _lit, fname, _spec, _conv in string.Formatter().parse(text):
            if fname is None:
                continue
            if fname == "":
                pos += 1
            elif fname.isdigit():
                numbered.add(int(fname))
            else:
                named.add(fname.split(".")[0].split("[")[0])
    except ValueError:
        return None
    return pos, named, numbered


def format_ok(text: str, pos: int, named: set, numbered: set) -> bool:
    args = ["X"] * max(pos, (max(numbered) + 1) if numbered else 0)
    kw = {n: SAMPLE.get(n, "X") for n in named}
    try:
        text.format(*args, **kw)
        return True
    except (IndexError, KeyError, ValueError):
        return False


def latin_words(text: str):
    text = HTML_TAG.sub(" ", text)
    for w in LATIN_WORD.findall(text):
        yield w


def main() -> int:
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    codes = only or [c for c in i18n.LANG_NAMES if c != "en"]
    problems = []
    warn = []

    def bad(code, key, what):
        problems.append(f"{code:7} {key:34} {what}")

    for code, err in langs.failed.items():
        if code in codes:
            bad(code, "<module>", f"langs module failed: {err}")

    try:
        import opencc  # type: ignore

        s2twp = opencc.OpenCC("s2twp")
        t2s = opencc.OpenCC("t2s")
    except Exception:  # noqa: BLE001
        s2twp = t2s = None
        warn.append("opencc not installed - the zh-TW / zh-CN script checks were skipped")

    uppercase_keys = {k for k, e in i18n.STRINGS.items() if e.get("en", "") and e["en"] == e["en"].upper()
                      and re.search(r"[A-Z]{3,}", e["en"])}

    for key, entry in sorted(i18n.STRINGS.items()):
        en = entry.get("en", "")
        if not en:
            bad("en", key, "missing English text")
            continue
        en_f = fields(en)
        en_nl = en.count("\n")
        for code in codes:
            text = entry.get(code)
            if text is None:
                bad(code, key, "MISSING")
                continue
            if not text.strip():
                bad(code, key, "empty")
                continue
            f = fields(text)
            if f is None:
                bad(code, key, "unparsable { } placeholder")
                continue
            if en_f is not None and f != en_f:
                # numbered placeholders may replace the positional ones (same count)
                pos, named, numbered = f
                if not (pos == 0 and numbered == set(range(en_f[0])) and named == en_f[1] and en_f[2] == set()):
                    bad(code, key, f"placeholders differ: en={en_f} vs {f}")
                    continue
            if not format_ok(text, *f):
                bad(code, key, "str.format fails")
            if text.count("\n") != en_nl:
                bad(code, key, f"line breaks: en={en_nl} vs {text.count(chr(10))}")
            if text == en and not SYMBOL_ONLY.match(en) and en.strip().lower() not in NO_TRANSLATE:
                words = [w.lower() for w in latin_words(en)]
                if words and not all(w in NO_TRANSLATE for w in words):
                    # one or two words often coincide ("Normal", "Version") - a warning; longer texts are an error
                    (warn.append if len(words) <= 2 else lambda s: bad(code, key, "identical to English"))(
                        f"{code:7} {key:34} identical to English: {en!r}")
            if code == "vi" and not unicodedata.is_normalized("NFC", text):
                bad(code, key, "not NFC")
            if code == "ro" and re.search("[şţŞŢ]", text):
                bad(code, key, "cedilla s/t (use ș ț with comma below)")
            if code == "el" and key in uppercase_keys and re.search("[ΆΈΉΊΌΎΏ]", text):
                bad(code, key, "accented capital in an UPPERCASE label")
            if code == "bg" and re.search("[ыэЫЭ]", text):
                bad(code, key, "Russian-only letter (ы/э) in Bulgarian")
            if code in i18n.CJK:
                if not CJK_RANGE.search(text) and not SYMBOL_ONLY.match(text) and text.strip().lower() not in NO_TRANSLATE:
                    words = [w.lower() for w in latin_words(text)]
                    if words and not all(w in NO_TRANSLATE for w in words):
                        bad(code, key, "no CJK characters in the text")
                for w in latin_words(text):
                    wl = w.lower().strip(".'-")
                    if wl and wl not in NO_TRANSLATE and not re.match(r"^(v?\d|[a-z]$)", wl) \
                            and wl not in ("fable", "opus", "sonnet", "haiku", "claude"):
                        if wl not in {x for n in NO_TRANSLATE for x in n.split()}:
                            warn.append(f"{code:7} {key:34} Latin word in CJK text: {w}")
                if code == "zh-TW" and s2twp and s2twp.convert(text) != text:
                    bad(code, key, f"zh-TW: simplified char / mainland term -> {s2twp.convert(text)!r}")
                if code == "zh-CN" and t2s and t2s.convert(text) != text:
                    bad(code, key, f"zh-CN: traditional char -> {t2s.convert(text)!r}")
            if "pt" in entry or "es" in entry:
                bad(code, key, "old 'pt'/'es' key still present")

    for code in codes:
        n = sum(1 for e in i18n.STRINGS.values() if code in e)
        print(f"{code:7} {n:4} / {len(i18n.STRINGS)} texts")
    for w in sorted(set(warn)):
        print("warn  " + w)
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print("  " + p)
        return 1
    print("\ncheck_i18n: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
