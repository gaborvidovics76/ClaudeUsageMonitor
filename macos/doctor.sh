#!/bin/bash
# Collects everything Gabor needs to help when the build or the app misbehaves.
# Usage:  ./macos/doctor.sh      -> writes macos-doctor-report.txt (no passwords, no tokens)
cd "$(dirname "$0")/.." || exit 1
OUT="macos-doctor-report.txt"
{
    echo "=== Claude Usage Monitor - macOS doctor  $(date)"
    echo "--- system";      sw_vers 2>&1; echo "arch: $(uname -m)"
    echo "--- python";      for p in python3.12 python3.13 python3.11 python3.10 python3; do command -v "$p" >/dev/null && echo "$p -> $($p --version 2>&1) $(command -v "$p")"; done
    echo "--- tools";       for t in git curl ditto codesign iconutil xattr; do printf '%s: ' "$t"; command -v "$t" || echo "MISSING"; done
    echo "--- xcode clt";   xcode-select -p 2>&1
    echo "--- source";      grep __version__ claude_usage/__init__.py; [ -d .git ] && { git rev-parse --short HEAD; git status --short | head -20; }
    echo "--- venv";        [ -d .venv-macos ] && .venv-macos/bin/python -m pip list 2>/dev/null | grep -iE "pyside|pyinstaller|keyring|shiboken"
    echo "--- app";         APP="dist-macos/ClaudeUsageMonitor.app"; ls -ld "$APP" 2>&1; [ -d "$APP" ] && { codesign -dv "$APP" 2>&1 | head -8; du -sh "$APP"; }
    echo "--- app --version"; [ -x "$APP/Contents/MacOS/ClaudeUsageMonitor" ] && { "$APP/Contents/MacOS/ClaudeUsageMonitor" --version; echo "exit code: $?"; }
    echo "--- pyinstaller log (tail)"; tail -40 build-macos/pyinstaller.log 2>/dev/null
    echo "--- pyinstaller warnings";   grep -iE "error|missing module named (PySide6|keyring)|not found" build-macos/work/ClaudeUsageMonitor/warn-*.txt 2>/dev/null | head -20
    CFG="$HOME/Library/Application Support/ClaudeUsageMonitor"
    echo "--- config folder"; ls -la "$CFG" 2>&1
    echo "--- startup.log";   tail -15 "$CFG/startup.log" 2>/dev/null
    echo "--- update.log";    tail -15 "$CFG/update.log" 2>/dev/null
    echo "--- api.log (no secrets are ever written there)"; tail -25 "$CFG/api.log" 2>/dev/null
    echo "--- launch agent";  ls -l "$HOME/Library/LaunchAgents/hu.dinorr.claudeusagemonitor.plist" 2>&1
    echo "--- crash reports"; ls -t "$HOME/Library/Logs/DiagnosticReports/" 2>/dev/null | grep -i claudeusage | head -3
    echo "--- live manifests"; curl -s --max-time 15 https://claudeusagemonitor.com/manifest.json | head -5; curl -s --max-time 15 https://claudeusagemonitor.com/macos/manifest.json | head -6
} > "$OUT" 2>&1
echo "Written: $OUT  - send this file to Gabor."
