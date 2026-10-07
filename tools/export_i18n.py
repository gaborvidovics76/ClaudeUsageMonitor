"""Exports the translation source for the translators: docs/i18n/source.json

    {
      "keys":   {key: {"en": ..., "hu": ..., "where": "…"}},      # Windows wording
      "mac":    {key: {"en": ..., "hu": ...}},                    # macOS-only overrides
      "legacy": {"pt-PT": {key: text}, "es-ES": {key: text}}     # the old pt / es texts (starting points)
    }

Run from the project root:  python tools/export_i18n.py
"""

from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from claude_usage import i18n  # noqa: E402
from claude_usage.i18n_mac import STRINGS_MAC  # noqa: E402

WHERE = [
    ("panel.", "panel label on the floating widget - very tight space; Latin scripts use UPPERCASE"),
    ("time.", "time unit / short time format on the panel - keep it as short as the English"),
    ("tray.", "tray icon tooltip / menu head - short"),
    ("menu.", "context-menu item (may end with …)"),
    ("layout.", "menu option (layout name)"),
    ("theme.", "menu option (theme name)"),
    ("size.", "menu option (size)"),
    ("source.", "menu option (data source)"),
    ("set.", "Settings window: tab name, label, checkbox or hint"),
    ("notify.", "desktop notification - short and friendly"),
    ("err.", "error message shown on the panel or in a dialog"),
    ("auth.", "sign-in dialog"),
    ("hist.", "History window"),
    ("backup.", "backup status bar / details window"),
    ("upd.", "update window"),
    ("help.", "Help window (HTML allowed where the English has it)"),
    ("fb.", "'Message to the developer' window (form, consent, privacy notice)"),
    ("det.", "small detail rows under the gauges"),
]


def where_of(key: str) -> str:
    for prefix, text in WHERE:
        if key.startswith(prefix):
            return text
    return "general"


def main() -> None:
    keys = {}
    legacy = {"pt-PT": {}, "es-ES": {}}
    for key, entry in sorted(i18n.STRINGS.items()):
        keys[key] = {"en": entry.get("en", ""), "hu": entry.get("hu", ""), "where": where_of(key)}
        for code in legacy:
            if entry.get(code):
                legacy[code][key] = entry[code]
    mac = {k: {"en": v.get("en", ""), "hu": v.get("hu", "")} for k, v in STRINGS_MAC.items()}
    out = {"keys": keys, "mac": mac, "legacy": legacy}
    path = os.path.join(ROOT, "docs", "i18n", "source.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print(f"{len(keys)} keys + {len(mac)} mac keys -> {path}")


if __name__ == "__main__":
    main()
