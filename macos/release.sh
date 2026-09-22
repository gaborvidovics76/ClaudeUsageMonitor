#!/bin/bash
# Claude Usage Monitor - build and publish the macOS version.  Usage:
#     ./macos/release.sh              build, package, upload to every configured channel, verify
#     ./macos/release.sh --no-upload  build and package only (nothing leaves this Mac)
#     ./macos/release.sh --skip-build reuse dist-macos/ClaudeUsageMonitor.app
#     ./macos/release.sh --no-pull    do not run `git pull` first
#     ./macos/release.sh --force      publish although this version is not out for Windows yet
#
# Where it publishes (both are configured in macos/release.local.env):
#   PRIMARY  https://claudeusagemonitor.com/macos/   <- the home of the project, always required
#   LEGACY   the old address, optional: only so copies installed before the move keep updating.
#            Leave it empty once those installs have moved over - the future is the primary site.
#
# The rule of the project: Gabor's Windows release is the base. The version number comes from
# the source (claude_usage/__init__.py) - never change it here. A macOS release is only made for
# a version already published for Windows, and it only ever writes into the macos/ folder.
set -euo pipefail
cd "$(dirname "$0")/.."

say()  { printf '\033[1;36m%s\033[0m\n' "$*"; }
ok()   { printf '\033[1;32m  %s\033[0m\n' "$*"; }
warn() { printf '\033[1;33m  %s\033[0m\n' "$*"; }
die()  { printf '\033[1;31mERROR: %s\033[0m\n' "$*" >&2; exit 1; }

UPLOAD=1; BUILD=1; FORCE=0; PULL=1
for arg in "$@"; do
    case "$arg" in
        --no-upload)  UPLOAD=0 ;;
        --skip-build) BUILD=0 ;;
        --no-pull)    PULL=0 ;;
        --force)      FORCE=1 ;;
        *) die "unknown option: $arg" ;;
    esac
done
[ "$(uname -s)" = "Darwin" ] || die "this script has to run on a Mac."

PRIMARY_URL="https://claudeusagemonitor.com/"

# ---------------------------------------------------------------- 0. latest source
if [ "$PULL" = 1 ] && [ -d .git ]; then
    say "[0/5] Fetching the latest source ..."
    if [ -n "$(git status --porcelain --untracked-files=no)" ]; then
        warn "there are local modifications - skipping git pull (commit or stash them first)"
    else
        BRANCH="$(git rev-parse --abbrev-ref HEAD)"
        git pull --ff-only || die "git pull failed - resolve it, or run with --no-pull"
        ok "$BRANCH at $(git rev-parse --short HEAD)"
    fi
fi

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

# ---------------------------------------------------------------- 1. package
say "[1/5] Packaging $ZIP_NAME ..."
rm -rf dist-macos/package "$SITE"; mkdir -p "$PKG" "$SITE/versions"
ditto "$APP" "$PKG/ClaudeUsageMonitor.app"
cp macos/package/OLVASS-EL.txt macos/package/README.txt "$PKG/"
cp LICENSE "$PKG/LICENSE.txt"
echo "$VERSION" > "$PKG/VERSION"
# ditto keeps the symlinks and permissions a bundle needs (a plain zip tool would break the app)
ditto -c -k --keepParent "$PKG" "$SITE/versions/$ZIP_NAME"
ok "$(du -h "$SITE/versions/$ZIP_NAME" | cut -f1)  $SITE/versions/$ZIP_NAME"

# ---------------------------------------------------------------- 2. config + manifests
CFG="macos/release.local.env"
LEGACY_URL=""
if [ -f "$CFG" ]; then
    # shellcheck disable=SC1090
    source "$CFG"
    LEGACY_URL="${UM_LEGACY_BASE_URL:-}"
fi

say "[2/5] Manifests ..."
COMMIT="$( (command -v git >/dev/null && [ -d .git ] && git rev-parse --short HEAD) || echo "")"
ARGS=(--version "$VERSION" --arch "$ARCH" --zip "$SITE/versions/$ZIP_NAME" --site "$SITE"
      --base-url "$PRIMARY_URL" --commit "$COMMIT")
[ -n "$LEGACY_URL" ] && ARGS+=(--legacy-base-url "$LEGACY_URL")
[ "$FORCE" = 1 ] && ARGS+=(--force)
python macos/make_manifest.py "${ARGS[@]}"

if [ "$UPLOAD" = 0 ]; then
    echo; say "DONE (not uploaded): $SITE/versions/$ZIP_NAME"; exit 0
fi

# ---------------------------------------------------------------- 3. upload
[ -f "$CFG" ] || die "$CFG is missing. Copy macos/release.local.env.example to that name and fill in the upload accounts Gabor gave you."
: "${UM_FTP_HOST:?set UM_FTP_HOST in $CFG}" "${UM_FTP_USER:?set UM_FTP_USER in $CFG}" "${UM_FTP_PASS:?set UM_FTP_PASS in $CFG}"

# upload one channel:  $1 host  $2 user  $3 pass  $4 remote subfolder  $5 local site dir  $6 label
upload_channel() {
    local host="$1" user="$2" pass="$3" dir="$4" src="$5" label="$6"
    local remote="${dir#/}"; [ -n "$remote" ] && remote="${remote%/}/"
    put() {
        curl --silent --show-error --fail --ssl-reqd --ftp-create-dirs --connect-timeout 30 \
             --user "$user:$pass" -T "$1" "ftp://$host/$remote$2" \
          || die "[$label] upload of $2 failed (check the account in $CFG; the server must offer FTP over TLS)"
        ok "[$label] uploaded $2"
    }
    # order matters: the manifest goes last, so it never points at a package that is not there yet
    put "$SITE/versions/$ZIP_NAME" "versions/$ZIP_NAME"
    put "$src/versions.json" "versions.json"
    put "$src/CHANGELOG.md" "CHANGELOG.md"
    put "$src/manifest.json" "manifest.json"
}

say "[3/5] Uploading to the primary site (claudeusagemonitor.com) ..."
upload_channel "$UM_FTP_HOST" "$UM_FTP_USER" "$UM_FTP_PASS" "${UM_FTP_DIR:-}" "$SITE" "primary"

say "[4/5] Uploading to the legacy site ..."
if [ -n "$LEGACY_URL" ] && [ -n "${UM_LEGACY_FTP_HOST:-}" ] && [ -n "${UM_LEGACY_FTP_USER:-}" ] && [ -n "${UM_LEGACY_FTP_PASS:-}" ]; then
    upload_channel "$UM_LEGACY_FTP_HOST" "$UM_LEGACY_FTP_USER" "$UM_LEGACY_FTP_PASS" \
                   "${UM_LEGACY_FTP_DIR:-}" "$SITE/legacy" "legacy"
elif [ -n "$LEGACY_URL" ]; then
    warn "UM_LEGACY_BASE_URL is set but the legacy account is not - skipped."
else
    ok "no legacy channel configured - skipped (this is the normal state once everyone has moved over)"
fi

# ---------------------------------------------------------------- 5. verify
say "[5/5] Checking the live sites ..."
VARGS=(--verify --site "$SITE" --base-url "$PRIMARY_URL")
[ -n "$LEGACY_URL" ] && VARGS+=(--legacy-base-url "$LEGACY_URL")
python macos/make_manifest.py "${VARGS[@]}"
echo
say "PUBLISHED: ${PRIMARY_URL}macos/versions/$ZIP_NAME"
echo "  Installed copies on macOS will offer this version by themselves within a few hours."
