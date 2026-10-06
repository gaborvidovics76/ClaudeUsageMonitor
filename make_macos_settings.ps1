<#
.SYNOPSIS
  Makes the upload-settings file for whoever publishes the macOS version - so they can import it
  with ONE command (./macos/import-settings.sh <file>) instead of filling in release.local.env by hand.

.DESCRIPTION
  Asks for the FTP account(s) here, on your machine (the password is typed hidden and never leaves
  this script except into the output file), tests every account over FTPS with curl.exe, and writes
  handoff\um-macos.local.env (handoff\ is git-ignored, and *.local.env is unreadable for Claude Code
  by the project's deny rules).

  PRIMARY  = the account on claudeusagemonitor.com whose home is /httpdocs/macos   (required)
  LEGACY   = the old dinorr.hu account whose home is /httpdocs/claude-usage-monitor/macos (optional:
             leave the user empty and the colleague's import keeps the old account they already have)

  Send the file over a private channel (e.g. a Bitwarden Send / 1Password share that expires), then
  delete it here:  Remove-Item handoff\um-macos.local.env

.EXAMPLE
  .\make_macos_settings.ps1
.EXAMPLE
  .\make_macos_settings.ps1 -PrimaryUser um-macos -SkipTest
#>
param(
    [string]$PrimaryHost = "claudeusagemonitor.com",
    [string]$PrimaryUser = "",
    [string]$PrimaryDir  = "",
    [string]$LegacyHost  = "dinorr.hu",
    [string]$LegacyUser  = "",
    [string]$LegacyDir   = "",
    [string]$LegacyUrl   = "https://dinorr.hu/claude-usage-monitor/",
    [switch]$SkipTest
)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

function Read-Plain([string]$prompt) {
    $s = Read-Host -Prompt $prompt -AsSecureString
    $b = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($s)
    try { return [Runtime.InteropServices.Marshal]::PtrToStringBSTR($b) } finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($b) }
}
# bash single-quote: '...' with ' -> '\''
function Q([string]$v) { return "'" + $v.Replace("'", "'\''") + "'" }

function Test-Ftps([string]$label, [string]$h, [string]$u, [string]$p, [string]$d) {
    $dir = $d.Trim('/'); if ($dir) { $dir += "/" }
    $out = & curl.exe --silent --show-error --fail --ssl-reqd --connect-timeout 30 --list-only --user "${u}:${p}" "ftp://$h/$dir" 2>&1
    if ($LASTEXITCODE -ne 0) { Write-Host "  [$label] login FAILED: $out" -ForegroundColor Red; return $false }
    if (($out | Out-String) -match '(?m)^manifest\.json\s*$') {
        Write-Host "  [$label] $u@$h - OK, the macOS folder is visible" -ForegroundColor Green
    } else {
        Write-Host "  [$label] $u@$h - login OK, but no manifest.json in that folder - is the home the macos/ folder?" -ForegroundColor Yellow
    }
    return $true
}

Write-Host "== PRIMARY: $PrimaryHost (home: /httpdocs/macos) ==" -ForegroundColor Cyan
if (-not $PrimaryUser) { $PrimaryUser = Read-Host "FTP user" }
if (-not $PrimaryUser) { throw "The primary account is required. Create it first: Plesk -> claudeusagemonitor.com -> FTP Access -> Create Additional FTP Account, home /httpdocs/macos." }
$PrimaryPass = Read-Plain "FTP password for $PrimaryUser (hidden)"

Write-Host ""
Write-Host "== LEGACY: $LegacyHost (optional - Enter = the colleague keeps the old account they have) ==" -ForegroundColor Cyan
if (-not $LegacyUser) { $LegacyUser = Read-Host "FTP user (empty = skip)" }
$LegacyPass = ""
if ($LegacyUser) { $LegacyPass = Read-Plain "FTP password for $LegacyUser (hidden)" }

if (-not $SkipTest) {
    Write-Host ""
    Write-Host "== Testing over FTPS ==" -ForegroundColor Cyan
    $okP = Test-Ftps "primary" $PrimaryHost $PrimaryUser $PrimaryPass $PrimaryDir
    $okL = $true
    if ($LegacyUser) { $okL = Test-Ftps "legacy" $LegacyHost $LegacyUser $LegacyPass $LegacyDir }
    if (-not ($okP -and $okL)) { throw "An account does not work - nothing written. Fix it in Plesk and run again." }
}

$lines = @(
    "# Claude Usage Monitor - macOS upload settings from Gabor ($(Get-Date -Format 'yyyy-MM-dd'))",
    "# Import on the Mac, in the project folder:   ./macos/import-settings.sh <this file>",
    "# Then delete this file. SECRET - never commit, never paste into a chat.",
    "",
    "UM_FTP_HOST=$(Q $PrimaryHost)",
    "UM_FTP_USER=$(Q $PrimaryUser)",
    "UM_FTP_PASS=$(Q $PrimaryPass)",
    "UM_FTP_DIR=$(Q $PrimaryDir)"
)
if ($LegacyUser) {
    $lines += @(
        "",
        "UM_LEGACY_BASE_URL=$(Q $LegacyUrl)",
        "UM_LEGACY_FTP_HOST=$(Q $LegacyHost)",
        "UM_LEGACY_FTP_USER=$(Q $LegacyUser)",
        "UM_LEGACY_FTP_PASS=$(Q $LegacyPass)",
        "UM_LEGACY_FTP_DIR=$(Q $LegacyDir)"
    )
}
$out = Join-Path $PSScriptRoot "handoff"
New-Item -ItemType Directory -Force -Path $out | Out-Null
$file = Join-Path $out "um-macos.local.env"
# LF line endings and no BOM - it is read by bash on the Mac
[IO.File]::WriteAllText($file, (($lines -join "`n") + "`n"), (New-Object Text.UTF8Encoding($false)))
$PrimaryPass = $null; $LegacyPass = $null

Write-Host ""
Write-Host "WRITTEN: $file" -ForegroundColor Cyan
Write-Host "Send it over a private channel together with the kit (.\make_macos_kit.ps1), then delete it here." -ForegroundColor Cyan
