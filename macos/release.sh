#!/bin/bash
# Claude Usage Monitor - publish the macOS build.  Usage:
#     ./macos/release.sh              build, package, upload, verify
#     ./macos/release.sh --no-upload  build and package only (nothing leaves this Mac)
#     ./macos/release.sh --skip-build reuse dist-macos/ClaudeUsageMonitor.app
#     ./macos/release.sh --force      publish although this version is not out for Windows yet
#
# The rule of the project: Gabor's Windows release is the base. The version number comes from
# the source (claude_usage/__init__.py) - never change it here. A macOS release is only made
# for a version that is already published for Windows, and it only ever writes into the
# server's macos/ folder.
set -euo pipefail
cd "$(dirname "$0")/.."

say()  { printf '\033[1;36m%s\033[0m\n' "$*"; }
ok()   { printf '\033[1;32m  %s\033[0m\n' "$*"; }
die()  { printf '\033[1;31mERROR: %s\033[0m\n' "$*" >&2; exit 1; }

UPLOAD=1; BUILD=1; FORCE=0
for arg in "$@"; do
    case "$arg" in
        --no-upload)  UPLOAD=0 ;;
        --skip-build) BUILD=0 ;;
        --force)      FORCE=1 ;;
        *) die "unknown option: $arg" ;;
    esac
done
[ "$(uname -s)" = "Darwin" ] || die "this script has to run on a Mac."

BASE_URL="https://claudeusagemonitor.com/"
[ "$BUILD" = 1 ] && ./macos/build.sh
# shellcheck disable=SC1091
source .venv-macos/bin/activate
APP="dist-macos/ClaudeUsageMonitor.app"
[ -d "$APP" ] || die "$APP is missing - run ./macos/build.sh first."

VERSION="$(python -c 'import re; print(re.search(r"__version__\s*=\s*\"([^\"]+)\"", open("claude_usage/__init__.py").read()).group(1))')"
ARCH="$(uname -m)"
ZIP_NAME="ClaudeUsageMonitor-macOS-$VERSION-$ARCH.zip"
SITE="dist-macos/site"
PKG="dist-macos/package/ClaudeUsageMonitor-macOS"

say "[1/4] Packaging $ZIP_NAME ..."
rm -rf dist-macos/package "$SITE"; mkdir -p "$PKG" "$SITE/versions"
ditto "$APP" "$PKG/ClaudeUsageMonitor.app"
cp macos/package/OLVASS-EL.txt macos/package/README.txt "$PKG/"
cp LICENSE "$PKG/LICENSE.txt"
echo "$VERSION" > "$PKG/VERSION"
# ditto keeps the symlinks and permissions a bundle needs (a plain zip tool would break the app)
ditto -c -k --keepParent "$PKG" "$SITE/versions/$ZIP_NAME"
ok "$(du -h "$SITE/versions/$ZIP_NAME" | cut -f1)  $SITE/versions/$ZIP_NAME"

say "[2/4] Manifest ..."
COMMIT="$( (command -v git >/dev/null && [ -d .git ] && git rev-parse --short HEAD) || echo "")"
FORCE_FLAG=""; [ "$FORCE" = 1 ] && FORCE_FLAG="--force"
python macos/make_manifest.py --version "$VERSION" --arch "$ARCH" --zip "$SITE/versions/$ZIP_NAME" \
    --site "$SITE" --base-url "$BASE_URL" --commit "$COMMIT" $FORCE_FLAG
ok "manifest.json + versions.json"

if [ "$UPLOAD" = 0 ]; then
    echo; say "DONE (not uploaded): $SITE/versions/$ZIP_NAME"; exit 0
fi

say "[3/4] Uploading to the server's macos/ folder ..."
CFG="macos/release.local.env"
[ -f "$CFG" ] || die "$CFG is missing. Copy macos/release.local.env.example to that name and fill in the FTP account Gabor gave you."
# shellcheck disable=SC1090
source "$CFG"
: "${UM_FTP_HOST:?set UM_FTP_HOST in $CFG}" "${UM_FTP_USER:?set UM_FTP_USER in $CFG}" "${UM_FTP_PASS:?set UM_FTP_PASS in $CFG}"
REMOTE="${UM_FTP_DIR:-}"; REMOTE="${REMOTE#/}"; [ -n "$REMOTE" ] && REMOTE="${REMOTE%/}/"
put() {   # local file, remote path relative to the account's folder
    curl --silent --show-error --fail --ssl-reqd --ftp-create-dirs --connect-timeout 30 \
         --user "$UM_FTP_USER:$UM_FTP_PASS" -T "$1" "ftp://$UM_FTP_HOST/$REMOTE$2" \
      || die "upload of $2 failed (check the account in $CFG; the server must offer FTP over TLS)"
    ok "uploaded $2"
}
# order matters: the manifest goes last, so it never points at a package that is not there yet
put "$SITE/versions/$ZIP_NAME" "versions/$ZIP_NAME"
put "$SITE/versions.json" "versions.json"
put "$SITE/CHANGELOG.md" "CHANGELOG.md"
put "$SITE/manifest.json" "manifest.json"

say "[4/4] Checking the live site ..."
python macos/make_manifest.py --verify --site "$SITE" --base-url "$BASE_URL"
echo
say "PUBLISHED: ${BASE_URL}macos/versions/$ZIP_NAME"
echo "  Installed copies on macOS will offer this version by themselves within a few hours."
