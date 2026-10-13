# Code signing policy

This page is also published on the project website: <https://claudeusagemonitor.com/#code-signing-policy>

## Windows

Windows releases of Claude Usage Monitor are built from this repository by a public GitHub Actions workflow
([`.github/workflows/windows-build.yml`](.github/workflows/windows-build.yml)) and submitted for signing
from that build. The private key is never on the maintainer's machine.

Free code signing provided by [SignPath.io](https://signpath.io), certificate by
[SignPath Foundation](https://signpath.org).

**Status:** application to SignPath Foundation pending. Until it is approved, releases are signed with the
author's own Certum *Open Source Developer* certificate (see [README – Code signing](README.md#code-signing)),
or published unsigned.

## What is signed

- `ClaudeUsageMonitor.exe` (the program), the installer scripts `Install.ps1` / `Uninstall.ps1`, and the
  package published at <https://claudeusagemonitor.com/> (`versions/ClaudeUsageMonitor-Setup-<version>.zip`,
  SHA-256 in `manifest.json`).
- Only the project's own binaries, built from this source. Third-party libraries (Python, PySide6/Qt) travel
  as released by their publishers.

## Team roles

| Role | Who |
|---|---|
| Author (commits without further review) | [Vidovics Gábor](https://github.com/gaborvidovics76) |
| Reviewer (reviews every change from non-committers) | Vidovics Gábor |
| Approver (approves each signing request) | Vidovics Gábor |

Every signing request is approved by hand; nothing is signed automatically.

## macOS

The native macOS app is distributed through the Mac App Store and signed/notarized through Apple's process.

## Privacy

The program sends data only to Anthropic's servers (your own usage figures, with your own sign-in) and to
claudeusagemonitor.com (the update check, and the optional "message to the developer" form only when you
send it). No telemetry, no analytics. Details: <https://claudeusagemonitor.com/#privacy>.

## Uninstall

`Uninstall.bat` in the program folder, or Settings › Apps on Windows; everything the program stored is in
`%APPDATA%\ClaudeUsageMonitor`, which the uninstaller offers to remove.
