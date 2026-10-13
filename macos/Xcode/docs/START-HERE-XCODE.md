# Claude Usage Monitor – native macOS app (Xcode) for the Mac App Store

This folder (`macos/Xcode/`) holds the native Swift/AppKit/SwiftUI version of the app as an Xcode
project, built for the Mac App Store. It mirrors the Windows (Python/PySide6) app: same panel,
same data sources, same 34 languages (the translations are generated from the shared source).

Hungarian, more detailed: [../README.md](../README.md), [APP-STORE-BEADAS.md](APP-STORE-BEADAS.md)
(submission, step by step), [MEGFELELES.md](MEGFELELES.md) (compliance research and risks).

## Build

1. Xcode 26 or newer (Mac App Store).
2. `git clone https://github.com/gaborvidovics76/ClaudeUsageMonitor.git`
3. `open macos/Xcode/ClaudeUsageMonitor.xcodeproj`
4. Target → Signing & Capabilities → pick your **Team** (the only manual setting; `DEVELOPMENT_TEAM`
   is deliberately empty in the repository). Automatic signing stays on.
5. ⌘R. The app is a menu bar item plus a floating panel. On first launch the Settings window opens on
   the *Data source* tab: grant access to Claude Desktop's log (sandbox: pick the file once), or pick
   **Demo data**, or sign in to claude.ai.

The GitHub Actions workflow "Xcode build" compiles the same project on GitHub's Mac runner, so a
broken build is visible without a Mac.

## Versions

- `MARKETING_VERSION` = the Windows version (`claude_usage/__init__.py`, now 2.8.1) – the maintainer sets it.
- `CURRENT_PROJECT_VERSION` = build number, +1 for every App Store upload – you set it (General → Build).

## The claude.ai sign-in switch

The claude.ai source (OAuth with Claude Code's public client, as on Windows) compiles only with the
`CLAUDE_SIGN_IN` compilation condition (Build Settings → Active Compilation Conditions). It is ON by
default. Removing it gives a "store-safe" build with the local log and the demo data only. Why this
matters: Anthropic's terms restrict third-party apps from routing requests through consumer-plan
credentials – see MEGFELELES.md §1 (Hungarian; the sources are in English).

## Regenerating

```bash
python macos/Xcode/tools/gen_xcstrings.py   # Localizable.xcstrings from the shared translations
python macos/Xcode/tools/make_icon.py       # the icon set (needs PySide6)
```

Both outputs are committed, so nothing has to be run on the Mac.

## What is intentionally missing compared with Windows

Self-update (App Store rule 2.4.5(vii)), the backup status bar (Windows-only scripts), Start menu /
taskbar items, free-text file paths (sandbox: files are chosen in the Open panel).

## App Store submission – the short list

Developer Program membership (paid) · App record in App Store Connect (name, bundle id
`hu.dinorr.claudeusagemonitor`) · metadata (no "Claude"/"Anthropic" in keywords; support and privacy
URLs on claudeusagemonitor.com) · age rating questionnaire (4+) · App Privacy: Data Not Collected ·
screenshots 16:10 (e.g. 2880×1800, no alpha) · App Review notes describing the **demo mode** · EU DSA
trader declaration by the account holder · Product → Archive → Distribute → App Store Connect → Upload.
Full checklist with the review-notes template: APP-STORE-BEADAS.md.
