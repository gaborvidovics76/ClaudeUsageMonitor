# Contributing

Thanks for taking a look. Issues and pull requests are both welcome.

## Adding a translation (easiest way to help)

The UI ships in 12 languages and adding another one takes about 20 minutes — no Qt or
Windows knowledge needed, just a text editor.

1. Open [`claude_usage/i18n.py`](claude_usage/i18n.py).
2. Add your language to `LANG_NAMES`, using the language's own name:

   ```python
   LANG_NAMES: Dict[str, str] = {
       "en": "English",
       ...
       "sv": "Svenska",   # <- your addition
   }
   ```

3. In the `STRINGS` dict, add a `"<code>": "..."` entry next to the existing ones for each
   key. Anything you skip falls back to English, so a partial translation is still useful
   and still mergeable.
4. Keep the placeholders (`{}`) exactly as they appear in the English string, in the same
   order.
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
