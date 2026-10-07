# Reviewer brief – independent native review (lektor)

You are an experienced native software-localisation reviewer of the language you were given. You did NOT write
the translation. Your job: make it read as if it had been written in your language by a top software company of
your country.

## Read first
1. [TRANSLATOR-BRIEF.md](TRANSLATOR-BRIEF.md) – the rules (placeholders, line breaks, length, platform words, legal text).
2. The section of your language in [LANGUAGE-NOTES.md](LANGUAGE-NOTES.md) if there is one, and the tone notes in
   `glossary-<code>.md`.
3. `docs/i18n/source.json` – `keys` (en + hu + `where` = where the text appears).
4. The module `claude_usage/langs/<module>.py` (module = code with `-` → `_`).

## What to fix (directly in the module; keep the format: CODE, NAME, STRINGS in the same key order, STRINGS_MAC)
- anything that sounds machine-translated, foreign, or like a calque of the English/Hungarian;
- not the Microsoft (Windows) / Apple (`STRINGS_MAC`) term of your language;
- inconsistent with the glossary or the chosen form of address (if the glossary is wrong and you are right,
  fix the glossary and make the whole file consistent);
- leakage from the other variant (pt-BR ↔ pt-PT, es-ES ↔ es-419, zh-TW ↔ zh-CN);
- spelling, diacritics, punctuation and typography rules of your language;
- too long for its place (`where` = panel label / short) – shorten.

Back-translate the longer texts (`help.guide`, `err.*`, `notify.*`, `fb.privacy_text`, `fb.intro`,
`set.backup_disclaimer`, `backup.disclaimer_short`) into English in your head and compare with the source: fix any
shift of meaning, omission or addition. The privacy notice must keep every fact, article number, retention period,
right and the URL.

## Finish
- `cd /c/Users/gabor/Claude/ClaudeUsageMonitor && PYTHONIOENCODING=utf-8 python tools/check_i18n.py <code>` must print
  `check_i18n: OK`.
- Append a `## Lektor` section to `docs/i18n/REVIEW-<code>.md` (create the file if missing): every change as
  `key: old → new – reason (3–6 words)`, then anything you still doubt.
- Use the Write/Edit tools only (never shell heredocs). Touch only the module, the glossary and the REVIEW file of
  your language.
- Report back in 4–6 lines: number of changes, the most important ones, checker result.
