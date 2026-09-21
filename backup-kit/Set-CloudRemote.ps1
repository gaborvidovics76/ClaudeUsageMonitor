#requires -Version 5.1
<#
    Set-CloudRemote.ps1
    Creates / updates the rclone remote for Nextcloud (step 2). You type the data in yourself.

    You need:
      * the address of your Nextcloud, e.g. https://cloud.example.com
      * your Nextcloud user name
      * an APP PASSWORD - NOT your account password.
        Nextcloud -> your avatar (top right) -> Personal settings -> Security ->
        "Devices & sessions" -> app name: rclone-backup -> "Create new app password"

    The password is typed hidden, never written to any log or script, and stored only
    in rclone's own config (%APPDATA%\rclone\rclone.conf) in obscured form.
    You can revoke the app password in Nextcloud at any time without touching your account.

    Another cloud instead of Nextcloud? Run "rclone config" and create a remote with the
    name given in config.psd1 (NextcloudRemote) - Google Drive, Dropbox, OneDrive for
    Business, S3, pCloud, SFTP ... all work.
#>
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'Common.ps1')

$cfg = Import-PowerShellDataFile -Path (Join-Path $PSScriptRoot 'config.psd1')
$rclone = Get-RcloneExe
if (-not $rclone) { Write-Host "rclone not found. Install it first:  winget install Rclone.Rclone" -ForegroundColor Red; exit 2 }
$remoteName = $cfg.NextcloudRemote
if (-not $remoteName) { Write-Host "NextcloudRemote is empty in config.psd1 - step 2 is switched off." -ForegroundColor Yellow; exit 0 }

Write-Host ""
Write-Host "  Setting up the rclone remote '$remoteName' (Nextcloud, WebDAV)" -ForegroundColor Cyan
Write-Host "  Use an APP PASSWORD, not your account password (see the top of this script)." -ForegroundColor Yellow
Write-Host ""
$ncUrl  = (Read-Host "  Nextcloud address (e.g. https://cloud.example.com)").Trim().TrimEnd('/')
$ncUser = (Read-Host "  Nextcloud user name").Trim()
$ncSec  = Read-Host "  App password" -AsSecureString
$bstr   = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($ncSec)
$ncPass = [Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr)
[Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)

$davUrl = "$ncUrl/remote.php/dav/files/$ncUser"
$obscured = $null
try { $obscured = ($ncPass | & $rclone obscure -) } catch { }
if ($obscured) {
    & $rclone config create $remoteName webdav url=$davUrl vendor=nextcloud user=$ncUser pass=$obscured --no-obscure | Out-Null
} else {
    & $rclone config create $remoteName webdav url=$davUrl vendor=nextcloud user=$ncUser pass=$ncPass --obscure | Out-Null
}
$ncPass = $null; $obscured = $null; [GC]::Collect()

Write-Host ""
Write-Host "  Testing the connection..." -ForegroundColor Cyan
& $rclone lsd "$remoteName`:" --max-depth 1
if ($LASTEXITCODE -eq 0) {
    & $rclone mkdir "$remoteName`:$($cfg.NextcloudBasePath)" 2>&1 | Out-Null
    Write-Host "  OK - the connection works. Target folder: $($cfg.NextcloudBasePath)" -ForegroundColor Green
    exit 0
}
Write-Host "  NOT WORKING. Check the address, the user name and the app password, then run this script again." -ForegroundColor Red
exit 3
