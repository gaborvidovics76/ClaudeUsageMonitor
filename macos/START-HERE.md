# Claude Usage Monitor – building and releasing on macOS

For whoever builds and publishes the macOS version. The project is developed by Gábor on Windows;
the source is shared, everything macOS-specific lives in this `macos/` folder.

> **Magyarul (részletesebb):** [KEZDD-ITT.md](KEZDD-ITT.md)

## Build – one command

```bash
./macos/build.sh
open dist-macos/ClaudeUsageMonitor.app
```

It finds Python, creates its own environment (`.venv-macos`), installs the dependencies, makes the
icon, builds the app, signs it ad hoc and checks that it starts. Needs macOS 12+, Python 3.10+
(<https://www.python.org/downloads/macos/> or `brew install python@3.12`) and the Xcode command line
tools (`xcode-select --install`).

Something wrong? `./macos/doctor.sh` writes `macos-doctor-report.txt` (no passwords, no tokens) –
send that file to Gábor.

## A new version arrived

```bash
git pull
./macos/release.sh
```

First time: `git clone https://github.com/gaborvidovics76/ClaudeUsageMonitor.git`

## Publish

```bash
./macos/release.sh              # build, package, upload, verify the live site
./macos/release.sh --no-upload  # package only
```

One-time setup: `cp macos/release.local.env.example macos/release.local.env`, fill in the FTP account
Gábor gave you, `chmod 600` it. The file is git-ignored; never commit or share it. The account only
reaches the server's `claude-usage-monitor/macos` folder.

## Rules that let two people work in parallel

**Gábor's Windows release is the base.**

1. Never change the version number – it comes from `claude_usage/__init__.py`. `release.sh` refuses a
   version that is not out for Windows yet (`--force` only when Gábor says so).
2. Upload only into the server's `macos/` folder. Windows and macOS use separate manifests, so the two
   releases never overwrite each other.
3. Release notes are shared: `release/notes/<version>.json`, written by Gábor.
4. Do not push to `main`. Fixes go on a branch `macos/<topic>` and reach Gábor as a Pull Request or as
   `git format-patch main --stdout > fix.patch`. He reviews and merges.
5. macOS-only files you can change freely: `macos/`, `claude_usage/macutil.py`, `secretstore_mac.py`,
   `updater_mac.py`, `i18n_mac.py`. Talk to Gábor before touching code that also runs on Windows.

## Good to know

- Not notarised: on another Mac the first start needs right-click → Open, or
  `xattr -dr com.apple.quarantine /Applications/ClaudeUsageMonitor.app`.
  With a Developer ID: `CODESIGN_IDENTITY="Developer ID Application: Name (TEAMID)" ./macos/build.sh`
- The build targets the architecture of the Mac that builds it. An Intel build also runs on Apple
  Silicon; an arm64 build is never offered to an Intel Mac.
- The sign-in token lives in the Keychain, never in a file. After a rebuild macOS may ask once more.
- Self-update only works from /Applications (App Translocation makes Downloads read-only).
- No Dock icon by design (`LSUIElement`). Logs: `~/Library/Application Support/ClaudeUsageMonitor/`.

## Honest status

The macOS parts were written on Windows without a Mac and tested in a simulated environment only.
You are the first to run them on real hardware – see the checklist at the end of
[KEZDD-ITT.md](KEZDD-ITT.md), and send the doctor report if anything is off.
