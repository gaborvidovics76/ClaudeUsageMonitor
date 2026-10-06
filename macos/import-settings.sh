#!/usr/bin/env bash
# Imports the upload settings Gabor sent you into macos/release.local.env - one command, then tests them.
#
#   ./macos/import-settings.sh ~/Downloads/um-macos.local.env    import the file + test both accounts
#   ./macos/import-settings.sh --check                            only test what is configured now
#
# What it does:
#   - keeps a backup of your current macos/release.local.env (release.local.env.bak-<time>, chmod 600)
#   - takes the PRIMARY account (claudeusagemonitor.com) from the file you got
#   - LEGACY account (the old dinorr.hu address): from the file if it has one; otherwise it keeps the one
#     you already have - and if your old file had the dinorr.hu account as its primary (the setup before
#     the domain move), that account becomes the legacy one automatically
#   - writes the result with chmod 600, then logs in to each account over FTPS and lists its folder
# Passwords are never printed. Works with the bash 3.2 that ships with macOS.
set -euo pipefail
cd "$(dirname "$0")/.."

CFG="macos/release.local.env"
DEFAULT_LEGACY_URL="https://dinorr.hu/claude-usage-monitor/"
VARS="UM_FTP_HOST UM_FTP_USER UM_FTP_PASS UM_FTP_DIR UM_LEGACY_BASE_URL UM_LEGACY_FTP_HOST UM_LEGACY_FTP_USER UM_LEGACY_FTP_PASS UM_LEGACY_FTP_DIR"

say()  { printf '\033[1;36m%s\033[0m\n' "$*"; }
ok()   { printf '  \033[32mOK\033[0m  %s\n' "$*"; }
warn() { printf '  \033[33m!!\033[0m  %s\n' "$*"; }
die()  { printf '\033[31mERROR: %s\033[0m\n' "$*" >&2; exit 1; }

# read one variable from a settings file without leaking anything into this shell
get() { # $1 file  $2 name
    [ -f "$1" ] || { printf ''; return; }
    ( set +u; for v in $VARS; do unset "$v"; done; source "$1" >/dev/null 2>&1; eval "printf '%s' \"\${$2:-}\"" )
}

# log in over FTPS and list the folder: $1 label $2 host $3 user $4 pass $5 dir
test_account() {
    local label="$1" host="$2" user="$3" pass="$4" dir="${5#/}"
    [ -n "$dir" ] && dir="${dir%/}/"
    local list
    if ! list="$(curl --silent --show-error --fail --ssl-reqd --connect-timeout 30 --list-only \
                      --user "$user:$pass" "ftp://$host/$dir" 2>&1)"; then
        warn "[$label] login FAILED on $host as $user: $list"
        return 1
    fi
    if printf '%s\n' "$list" | grep -qx 'manifest.json'; then
        ok "[$label] $user@$host - login OK, the macOS folder is visible (manifest.json is there)"
    else
        ok "[$label] $user@$host - login OK"
        warn "[$label] but there is no manifest.json in that folder. Is the account's home the macos/ folder? (UM_*_DIR)"
    fi
}

check() {
    [ -f "$CFG" ] || die "$CFG does not exist yet - import the file Gabor sent you first."
    say "Testing the upload accounts in $CFG ..."
    local fail=0
    test_account primary "$(get "$CFG" UM_FTP_HOST)" "$(get "$CFG" UM_FTP_USER)" "$(get "$CFG" UM_FTP_PASS)" "$(get "$CFG" UM_FTP_DIR)" || fail=1
    if [ -n "$(get "$CFG" UM_LEGACY_FTP_USER)" ]; then
        test_account legacy "$(get "$CFG" UM_LEGACY_FTP_HOST)" "$(get "$CFG" UM_LEGACY_FTP_USER)" \
                     "$(get "$CFG" UM_LEGACY_FTP_PASS)" "$(get "$CFG" UM_LEGACY_FTP_DIR)" || fail=1
    else
        ok "[legacy] not configured - releases go to claudeusagemonitor.com only"
    fi
    [ "$fail" = 0 ] || die "an account does not work - send Gabor the lines above (they contain no password)."
    say "All set. Publish with:  ./macos/release.sh"
}

[ "${1:-}" = "--check" ] && { check; exit 0; }
SRC="${1:-}"
[ -n "$SRC" ] || die "usage: ./macos/import-settings.sh <the settings file Gabor sent you>   (or --check)"
[ -f "$SRC" ] || die "file not found: $SRC"
command -v curl >/dev/null || die "curl is missing"

say "Importing $SRC ..."
P_HOST="$(get "$SRC" UM_FTP_HOST)"; P_USER="$(get "$SRC" UM_FTP_USER)"; P_PASS="$(get "$SRC" UM_FTP_PASS)"; P_DIR="$(get "$SRC" UM_FTP_DIR)"
[ -n "$P_HOST" ] && [ -n "$P_USER" ] && [ -n "$P_PASS" ] || die "the file has no complete primary account (UM_FTP_HOST / UM_FTP_USER / UM_FTP_PASS)."
case "$P_HOST" in *dinorr.hu*) die "the primary account in the file points to dinorr.hu - the primary must be claudeusagemonitor.com. Ask Gabor for the new file." ;; esac

L_URL="$(get "$SRC" UM_LEGACY_BASE_URL)"; L_HOST="$(get "$SRC" UM_LEGACY_FTP_HOST)"
L_USER="$(get "$SRC" UM_LEGACY_FTP_USER)"; L_PASS="$(get "$SRC" UM_LEGACY_FTP_PASS)"; L_DIR="$(get "$SRC" UM_LEGACY_FTP_DIR)"
L_FROM="the imported file"
if [ -z "$L_USER" ] && [ -f "$CFG" ]; then
    if [ -n "$(get "$CFG" UM_LEGACY_FTP_USER)" ]; then
        L_URL="$(get "$CFG" UM_LEGACY_BASE_URL)"; L_HOST="$(get "$CFG" UM_LEGACY_FTP_HOST)"
        L_USER="$(get "$CFG" UM_LEGACY_FTP_USER)"; L_PASS="$(get "$CFG" UM_LEGACY_FTP_PASS)"; L_DIR="$(get "$CFG" UM_LEGACY_FTP_DIR)"
        L_FROM="your existing legacy account"
    else
        case "$(get "$CFG" UM_FTP_HOST)" in *dinorr.hu*)
            L_HOST="$(get "$CFG" UM_FTP_HOST)"; L_USER="$(get "$CFG" UM_FTP_USER)"
            L_PASS="$(get "$CFG" UM_FTP_PASS)"; L_DIR="$(get "$CFG" UM_FTP_DIR)"
            L_FROM="your old dinorr.hu account (it was your primary before the domain move)" ;;
        esac
    fi
fi
[ -n "$L_USER" ] && [ -z "$L_URL" ] && L_URL="$DEFAULT_LEGACY_URL"

if [ -f "$CFG" ]; then
    BAK="$CFG.bak-$(date +%Y%m%d-%H%M%S)"
    cp -p "$CFG" "$BAK"; chmod 600 "$BAK"
    ok "previous settings saved: $BAK"
fi

umask 077
{
    echo "# Upload accounts for the macOS releases - written by macos/import-settings.sh on $(date '+%Y-%m-%d %H:%M')."
    echo "# Git-ignored, never commit or send it. Test any time:  ./macos/import-settings.sh --check"
    echo
    echo "# PRIMARY - https://claudeusagemonitor.com/macos/  (the home of the project, required)"
    printf 'UM_FTP_HOST=%q\nUM_FTP_USER=%q\nUM_FTP_PASS=%q\nUM_FTP_DIR=%q\n' "$P_HOST" "$P_USER" "$P_PASS" "$P_DIR"
    echo
    echo "# LEGACY - the old address, only while copies installed before the move still ask it."
    echo "# Empty these lines when Gabor says the old channel is no longer needed."
    printf 'UM_LEGACY_BASE_URL=%q\nUM_LEGACY_FTP_HOST=%q\nUM_LEGACY_FTP_USER=%q\nUM_LEGACY_FTP_PASS=%q\nUM_LEGACY_FTP_DIR=%q\n' \
           "$L_URL" "$L_HOST" "$L_USER" "$L_PASS" "$L_DIR"
} > "$CFG"
chmod 600 "$CFG"
ok "primary: $P_USER@$P_HOST"
if [ -n "$L_USER" ]; then ok "legacy:  $L_USER@$L_HOST (from $L_FROM)"; else warn "legacy: none - only claudeusagemonitor.com will get the release"; fi
echo
check
echo
echo "  You can now delete the file you received:  rm \"$SRC\""
