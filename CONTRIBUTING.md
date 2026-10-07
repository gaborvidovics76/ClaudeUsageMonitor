# Contributing

Thanks for taking a look. Issues and pull requests are both welcome.

## Adding a translation (easiest way to help)

The UI ships in 34 languages and adding another one takes about an hour — no Qt or
Windows knowledge needed, just a text editor.

1. Copy an existing complete module from [`claude_usage/langs/`](claude_usage/langs/) (for example
   `pt_BR.py`) to `<code>.py` (hyphens become underscores: `pt-BR` → `pt_BR.py`). Set `CODE` and `NAME`
   (the language's own name).
2. Translate every value of `STRINGS` (and the four macOS overrides in `STRINGS_MAC`). Keep the
   placeholders (`{}`, `{0}`, `{site}`) and the number of `
` line breaks exactly as in the English
   source (`docs/i18n/source.json`, created by `python tools/export_i18n.py`). Anything you skip falls
   back to English, so a partial translation is still useful.
3. Add the code to `LANG_NAMES` in [`claude_usage/i18n.py`](claude_usage/i18n.py) and to `MODULES` in
   [`claude_usage/langs/__init__.py`](claude_usage/langs/__init__.py); the Windows LANGID goes into
   `_LANGID` so the language is picked up automatically.
4. Run `python tools/check_i18n.py <code>` until it prints `check_i18n: OK` (placeholders, line breaks,
   completeness, script-specific rules). Read [docs/i18n/TRANSLATOR-BRIEF.md](docs/i18n/TRANSLATOR-BRIEF.md)
   for tone and terminology, and add a short `docs/i18n/glossary-<code>.md`.
5. Run `python main.py`, switch to your language from **right-click → Language**, and check
   that nothing overflows the panel. Short strings matter here — the panel is small.

## Reporting a bug

Please include:

- Windows version
- Whether you're on the **local log** or **claude.ai** data source
- What the panel showed vs. what you expected
- The contents of `%APPDATA%\ClaudeUsageMonitor\startup.log` if the app didn't start

Never paste OAuth tokens or the raw contents of your credential store into an issue.

## Code changes

```bash
pip install -r requirements.txt
python main.py
```

The project is plain PySide6 with no build step for development. Rough layout:

| File | Responsibility |
|---|---|
| `claude_usage/app.py` | application wiring, tray icon, menus |
| `claude_usage/widget.py` | the panel itself and its layouts |
| `claude_usage/datasource.py` | reading Claude Desktop's local usage log |
| `claude_usage/apisource.py` | claude.ai usage API |
| `claude_usage/oauth.py` | OAuth sign-in flow |
| `claude_usage/secretstore.py` | DPAPI-encrypted token storage |
| `claude_usage/history.py` | history charts and statistics |
| `claude_usage/settings.py`, `settings_dialog.py` | settings model and dialog |
| `claude_usage/theme.py` | themes and colors |
| `claude_usage/i18n.py` | translations |
| `claude_usage/winutil.py` | Windows integration (autostart, Start menu, icons) |

Please keep pull requests focused on one thing, and mention in the description how you
tested it. Comments and docstrings in the codebase are currently a mix of Hungarian and
English; new code should use English.

## License

By contributing you agree that your contributions are licensed under the
[MIT License](LICENSE).
