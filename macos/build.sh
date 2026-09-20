#!/bin/bash
# Claude Usage Monitor - macOS build.  Usage:  ./macos/build.sh
#
# Builds dist-macos/ClaudeUsageMonitor.app from the sources in this folder. Safe to run again
# and again; everything it creates lives in .venv-macos/, build-macos/ and dist-macos/.
set -euo pipefail
cd "$(dirname "$0")/.."

say()  { printf '\033[1;36m%s\033[0m\n' "$*"; }
ok()   { printf '\033[1;32m  %s\033[0m\n' "$*"; }
die()  { printf '\033[1;31mERROR: %s\033[0m\n' "$*" >&2; exit 1; }

[ "$(uname -s)" = "Darwin" ] || die "this script builds the macOS app and has to run on a Mac."

say "[1/6] Looking for Python 3.10+ ..."
PY=""
for cand in python3.12 python3.13 python3.11 python3.10 python3; do
    if command -v "$cand" >/dev/null 2>&1 && "$cand" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)' 2>/dev/null; then
        PY="$(command -v "$cand")"; break
    fi
done
[ -n "$PY" ] || die "Python 3.10 or newer is needed. Install it from https://www.python.org/downloads/macos/  (or: brew install python@3.12), then run this script again."
ok "$("$PY" --version) at $PY"

say "[2/6] Preparing the build environment (.venv-macos) ..."
[ -d .venv-macos ] || "$PY" -m venv .venv-macos
# shellcheck disable=SC1091
source .venv-macos/bin/activate
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements.txt "pyinstaller>=6.6"
ok "dependencies installed"

VERSION="$(python -c 'import re; print(re.search(r"__version__\s*=\s*\"([^\"]+)\"", open("claude_usage/__init__.py").read()).group(1))')"
ARCH="$(uname -m)"
say "[3/6] Version $VERSION for $ARCH"
if command -v git >/dev/null 2>&1 && [ -d .git ]; then
    if [ -n "$(git status --porcelain --untracked-files=no)" ]; then
        printf '\033[1;33m  NOTE: there are local modifications - this build is not exactly the published source.\033[0m\n'
    fi
    ok "source: $(git rev-parse --short HEAD) ($(git describe --tags --always 2>/dev/null || true))"
fi

say "[4/6] Icon ..."
mkdir -p build-macos
QT_QPA_PLATFORM=offscreen python macos/make_icon.py build-macos/app.icns
ok "build-macos/app.icns"

say "[5/6] PyInstaller (this takes a few minutes the first time) ..."
pkill -f "dist-macos/ClaudeUsageMonitor.app/Contents/MacOS/" 2>/dev/null || true
rm -rf dist-macos/ClaudeUsageMonitor.app dist-macos/ClaudeUsageMonitor
UM_VERSION="$VERSION" python -m PyInstaller --noconfirm --clean \
    --distpath dist-macos --workpath build-macos/work macos/ClaudeUsageMonitor.spec >build-macos/pyinstaller.log 2>&1 \
    || { tail -30 build-macos/pyinstaller.log; die "PyInstaller failed - full log: build-macos/pyinstaller.log"; }
APP="dist-macos/ClaudeUsageMonitor.app"
[ -x "$APP/Contents/MacOS/ClaudeUsageMonitor" ] || die "the app bundle is incomplete (see build-macos/pyinstaller.log)"
ok "$APP"

say "[6/6] Signing (ad-hoc) and smoke test ..."
# Ad-hoc signature: needed on Apple Silicon to run at all. It is NOT notarisation - on another
# Mac the first start needs right-click > Open (see KEZDD-ITT.md). With an Apple Developer ID:
#   CODESIGN_IDENTITY="Developer ID Application: Name (TEAMID)" ./macos/build.sh
codesign --force --deep --sign "${CODESIGN_IDENTITY:--}" "$APP" 2>build-macos/codesign.log \
    || { cat build-macos/codesign.log; die "codesign failed"; }
codesign --verify --deep "$APP" || die "the signature does not verify"
"$APP/Contents/MacOS/ClaudeUsageMonitor" --version || die "the built app does not start (exit code $?). Run ./macos/doctor.sh and send the result to Gabor."
ok "the app starts"

echo
say "DONE: $APP  (version $VERSION, $ARCH)"
echo "  Try it:        open $APP"
echo "  Install it:    drag it into /Applications"
echo "  Publish it:    ./macos/release.sh"
