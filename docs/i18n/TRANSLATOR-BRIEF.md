# Translator brief – Claude Usage Monitor UI (read fully before writing anything)

Project root: `C:\Users\gabor\Claude\ClaudeUsageMonitor`. Python 3 + PySide6 desktop panel (Windows + macOS)
showing how much of the user's own Claude subscription is used. Free, open source, no telemetry.

The goal: a native speaker must believe the program was written in their language. Not a word-for-word
translation – localisation, the way an experienced native software localiser works for a top software company
of that country. English is authoritative; Hungarian is the second source (it shows the intent). If they differ,
follow the English and note the difference in your REVIEW file.

## Files you work with

| File | What |
|---|---|
| `docs/i18n/source.json` | the source: `keys` = {key: {en, hu, where}}, `mac` = macOS-only overrides, `legacy` = old pt / es texts |
| `docs/i18n/glossary-<code>.md` | **you write it first**: 40–60 fixed terms + tone of the language |
| `claude_usage/langs/<module>.py` | **your output**: the language module (format below) |
| `docs/i18n/REVIEW-<code>.md` | **you write it last**: at most 10 texts you are least sure about, with reasons |
| `tools/check_i18n.py` | run `python tools/check_i18n.py <code>` – must end with `check_i18n: OK` |

Module name = code with `-` replaced by `_` (`pt-BR` → `pt_BR.py`, `es-419` → `es_419.py`, `zh-TW` → `zh_TW.py`).

**Write files only with the Write tool** (never with shell heredocs – they corrupt accents and `\n`). Set
`PYTHONIOENCODING=utf-8` when running Python. Do not touch any other file of the project.

## Module format (exactly this)

```python
# -*- coding: utf-8 -*-
"""<Language name in that language> – UI strings of Claude Usage Monitor."""

CODE = "ja"
NAME = "日本語"

STRINGS = {
    "panel.five_hour": "…",
    # … one entry for EVERY key of source.json "keys" (358 keys), in the same order
}

# macOS wording (the four keys of source.json "mac"): "start at login" instead of "start with Windows", menu bar instead of tray
STRINGS_MAC = {
    "menu.autostart": "…",
    "notify.autostart_on": "…",
    "notify.autostart_off": "…",
    "notify.first_run": "…",
}
```

Plain Python string literals. Use `\n` for line breaks and `\"` for a double quote inside; or use single-quoted
strings. Long texts (help.guide is HTML) may be written as implicit concatenation of several literals
in parentheses. No f-strings, no variables.

## Rules

1. **Placeholders.** The number of `{}` must equal the English. If your grammar needs another order, use
   `{0}`, `{1}` (then all placeholders of that text are numbered – Python's `str.format` rule). Named
   placeholders (`{site}`, `{cfg}`, `{d}`, `{h}`, `{m}`) stay as they are. `%` goes where your language puts it
   (Turkish writes `%{}`).
2. **Line breaks.** The count of `\n` stays the same as in the English; the position may follow your language.
3. **Special strings.** File filters keep `;;` and `*.json` / `*.*`. HTML in `help.*` keeps its tags; translate
   only the text. Keep `…` (one character) for the ellipsis.
4. **Length.** `panel.*`, `time.*`, `*_short`, `tray.head`: not longer than the English (tight space on a small
   always-on-top panel). Menu items and buttons: at most ~30 % longer. Time units: the usual abbreviations of
   your language.
5. **UPPERCASE panel labels** (`where` says so): Latin and Cyrillic scripts write them in capitals as the
   English does; Greek capitals without tonos; Turkish `İ`/`I` per its rule; CJK has no case – do not try to
   emphasise otherwise.
6. **Do not translate**: Claude, Claude Desktop, Claude Code, claude.ai, Anthropic, model names (Fable, Opus,
   Sonnet, Haiku), plan badges (PRO, MAX, TEAM, ENTERPRISE), OneDrive, Nextcloud, Obsidian, rclone, PowerShell,
   HTTP(S), JSON, OAuth, SHA-256, DPAPI, GDPR (use the local official name where one exists, e.g. DSGVO, RGPD,
   AVG, RODO), NAIH, file/folder names, paths, `*.json`, Windows task names (`ClaudeBackup*`), the name
   Vidovics Gábor, claudeusagemonitor.com, GitHub. Inflect / attach them per your grammar.
7. **Platform words.** Use the Microsoft terminology of your language for Windows things (taskbar, notification
   area, Settings, sign in / sign out, Start menu) and Apple's for the four `STRINGS_MAC` texts (menu bar,
   login items). The user expects the words their OS uses.
8. **Tone.** Friendly, short, confident – like the English. Address the user the way the best consumer software
   of your country does (see the per-language notes). Be consistent: one form of address everywhere.
9. **Natural text.** No calques. For a help or error text ask: how would the best software company of my country
   write this? Notifications stay short and friendly.
10. **Legal text (`fb.privacy_text`, `fb.privacy_title`, `fb.consent`).** `fb.privacy_title` must be the name a
    privacy notice has in your country's software and websites (the term the big platforms and the data
    protection authority use – e.g. de "Datenschutzerklärung", fr "Politique de confidentialité",
    pl "Polityka prywatności", ja "プライバシーポリシー"). Translate `fb.privacy_text` precisely and completely
    (it is the actual GDPR notice shown to the user): keep every fact, article number, retention period, right
    and the URL; use the legal register of your language; keep the paragraph breaks (`\n\n`). Name the local
    supervisory authority only if you are sure; otherwise keep "the authority of your own country".
11. **The `where` field** tells where a text appears – let length and style follow it.
12. Keys ending in `_short`, and `time.*`: abbreviations the user of your country understands instantly.

## Workflow

1. Read this file, then `docs/i18n/source.json` completely (all 358 keys + mac + legacy if yours).
2. Write `docs/i18n/glossary-<code>.md` (40–60 terms with ONE fixed translation each: 5-hour session, weekly
   limit, per-model limit, reset, pace, burn rate, usage, panel, tray / menu bar, sign in / sign out,
   notification, alert, threshold, backup, lamp, data source, local log, profile, theme, layout, settings,
   update, history, projection, message to the developer, rating, privacy notice, consent …; plus the tone and
   form of address you chose, and the name of the privacy document and why).
3. Write the module. Every key. Follow the glossary.
4. Run `python tools/check_i18n.py <code>`; fix until it prints `check_i18n: OK` (warnings are allowed only when
   they are right, e.g. a product name).
5. Write `docs/i18n/REVIEW-<code>.md`: ≤ 10 texts you are least sure about, why, and any en/hu difference you
   noticed.
6. Report back in a few lines: key count, checker result, the form of address and the privacy-document name.
