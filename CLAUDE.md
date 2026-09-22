# Claude Usage Monitor - project context

An always-on-top desktop panel (Windows + macOS) that shows how much of the user's own Claude
subscription is used. Python 3 + PySide6, packaged with PyInstaller. MIT licence, public source.

## Who owns what

| Thing | Owner |
|---|---|
| Source code | Vidovics Gábor - <https://github.com/gaborvidovics76/ClaudeUsageMonitor> |
| Website, downloads and update manifests | the same person: <https://claudeusagemonitor.com/> |
| Old address (transitional) | `https://dinorr.hu/claude-usage-monitor/` - redirects to the new site; only the update channel of already-installed copies still lives there |

**claudeusagemonitor.com is this project's own website**, registered and run by the maintainer for
exactly this program. The link goes both ways and either direction can be checked: this repository
(README, release notes and the app's own updater) points at the site, and the site's pages link
back to this repository. Publishing a release there is the normal,
intended operation of this project - the same thing the Windows `release.ps1` does on the
maintainer's machine.

## Who does what

**The maintainer develops on Windows and is the starting point of every change.** A second person
builds and publishes the **macOS** version from the same source. That is the only reason the
`macos/` folder exists.

### Rules for the macOS side (please keep them)

1. **Never change the version number.** It comes from `claude_usage/__init__.py` and is the
   maintainer's. `macos/release.sh` only reads it.
2. **A macOS release is only made for a version already published for Windows.**
   `macos/make_manifest.py` checks the live Windows `versions.json` and refuses otherwise
   (`--force` only when the maintainer says so).
3. **Only ever write into the `macos/` folder of a site.** The upload accounts are confined to
   that folder; the Windows manifest, the pages and the backend are not touched.
4. **Do not push to `main`.** Fixes go on a `macos/<topic>` branch as a Pull Request, or as
   `git format-patch main --stdout > fix.patch` sent to the maintainer, who reviews and merges.
5. **Platform-specific files that are safe to change on the macOS side:** `macos/`,
   `claude_usage/macutil.py`, `secretstore_mac.py`, `updater_mac.py`, `i18n_mac.py`. Anything else
   also runs on Windows - discuss before touching it.

## How a macOS release is published

```bash
./macos/release.sh          # git pull -> build -> package -> upload -> verify over HTTPS
```

- Uploads with **curl over FTPS** (`--ssl-reqd`) using an account from `macos/release.local.env`
  (git-ignored, never committed). No other credential is needed.
- **The DCB-Native bridge is NOT used and NOT needed for releases.** That is a different tool for
  editing websites. A macOS release is only: build a zip, upload it and three small JSON/MD files
  into the `macos/` folder, then verify over HTTPS.
- Two channels, both are just static files:
  - **primary** `https://claudeusagemonitor.com/macos/` - the home of the project, always used;
  - **legacy** the old address - optional, only so copies installed before the move keep updating.
    It disappears once those installs have moved over.

## Good to know

- No telemetry in the app; it talks to Anthropic's own API for the user's own usage and reads a
  version number from the update manifest.
- Secrets never belong in the repository: upload accounts live in git-ignored `*.local.*` files,
  the app's sign-in token lives in the OS keychain.
- Everything published is reproducible from this source; packages are verified by SHA-256 recorded
  in the manifest.
