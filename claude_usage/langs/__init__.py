"""Per-language string modules, one file per language (`ja.py`, `pt_BR.py`, …).

Each module has
    CODE        the language code as used in settings ("pt-BR")
    STRINGS     {key: text}          - the Windows wording
    STRINGS_MAC {key: text}          - optional: keys worded differently on macOS

`load_into()` merges them into i18n.STRINGS. A broken or missing module never stops the
program: that language simply falls back (variant -> sibling -> English) for the missing keys.
The imports are written out one by one so that PyInstaller bundles every module.
"""

from __future__ import annotations

import importlib
import unicodedata
from typing import Dict, List

# code -> module name (hyphens are not allowed in module names)
MODULES: Dict[str, str] = {
    # the ten core languages: only their extra keys live here (the rest is inline in i18n*.py)
    "de": "de", "fr": "fr", "it": "it", "pl": "pl", "nl": "nl", "cs": "cs", "ru": "ru", "tr": "tr",
    # the European Portuguese / Spanish variants and their siblings
    "pt-PT": "pt_PT", "pt-BR": "pt_BR", "es-ES": "es_ES", "es-419": "es_419",
    # Asia
    "ja": "ja", "ko": "ko", "zh-TW": "zh_TW", "zh-CN": "zh_CN", "id": "id", "vi": "vi",
    # the remaining official EU languages
    "ro": "ro", "el": "el", "bg": "bg", "sk": "sk", "hr": "hr", "sv": "sv", "fi": "fi", "da": "da",
    "lt": "lt", "sl": "sl", "lv": "lv", "et": "et", "mt": "mt", "ga": "ga",
}

# languages whose texts must be NFC-normalised (precomposed accents) to render cleanly
NFC_LANGS = ("vi",)

loaded: List[str] = []
failed: Dict[str, str] = {}


def _merge(strings: Dict[str, Dict[str, str]], code: str, table: Dict[str, str]) -> int:
    n = 0
    nfc = code in NFC_LANGS
    for key, text in table.items():
        if not isinstance(key, str) or not isinstance(text, str) or not text:
            continue
        if nfc:
            text = unicodedata.normalize("NFC", text)
        strings.setdefault(key, {})[code] = text
        n += 1
    return n


def load_into(strings: Dict[str, Dict[str, str]], darwin: bool = False) -> None:
    for code, mod_name in MODULES.items():
        try:
            mod = importlib.import_module(f"{__name__}.{mod_name}")
        except Exception as e:  # noqa: BLE001 - a missing/broken language must not stop the app
            failed[code] = f"{type(e).__name__}: {e}"
            continue
        try:
            _merge(strings, code, getattr(mod, "STRINGS", {}) or {})
            if darwin:
                _merge(strings, code, getattr(mod, "STRINGS_MAC", {}) or {})
            loaded.append(code)
        except Exception as e:  # noqa: BLE001
            failed[code] = f"{type(e).__name__}: {e}"


# Static imports for PyInstaller's analysis (the modules are loaded above through importlib;
# this block only makes sure they are packaged). Missing ones are fine.
try:
    from . import de, fr, it, pl, nl, cs, ru, tr  # noqa: F401,E402
    from . import pt_PT, pt_BR, es_ES, es_419  # noqa: F401,E402
    from . import ja, ko, zh_TW, zh_CN, id, vi  # noqa: F401,E402
    from . import ro, el, bg, sk, hr, sv, fi, da, lt, sl, lv, et, mt, ga  # noqa: F401,E402
except Exception:  # noqa: BLE001
    pass
