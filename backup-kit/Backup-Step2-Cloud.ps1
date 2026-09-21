#requires -Version 5.1
<#
    Backup-Step2-Cloud.ps1
    STEP 2: a second, independent copy of the backup folder in another cloud (Nextcloud or any rclone remote).
    Started right after step 1 by the scheduled task "<TaskPrefix> 2 - Nextcloud".

    Never deletes anything on the remote (rclone "copy", not "sync"): a file removed
    by mistake on the PC is still there in the cloud.
#>
[CmdletBinding()]
param([switch]$DryRun)

$ErrorActionPreference = 'Continue'
. (Join-Path $PSScriptRoot 'Common.ps1')

$cfg = Get-BackupConfig
New-BackupFolders -Cfg $cfg
Start-BackupLog -LogDir $cfg.LogDir -Name 'nextcloud' | Out-Null

Write-Log "================ NEXTCLOUD FELTOLTES INDUL ================"
if (-not $cfg.NextcloudRemote) { Write-Log "Step 2 is switched off (NextcloudRemote is empty in config.psd1)." 'WARN'; exit 0 }

$rclone = Get-RcloneExe
if (-not $rclone) { Write-Log "rclone not found. Run Install-BackupKit.ps1 (or: winget install Rclone.Rclone)." 'ERROR'; exit 2 }
Write-Log "rclone: $rclone"

& $rclone lsd "$($cfg.NextcloudRemote):" --max-depth 1 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Log "Cannot reach the remote '$($cfg.NextcloudRemote)'. Check it with: rclone lsd $($cfg.NextcloudRemote):  (or run Set-CloudRemote.ps1)" 'ERROR'
    exit 3
}
Write-Log "Connection to '$($cfg.NextcloudRemote)' OK" 'OK'

$remote = "$($cfg.NextcloudRemote):$($cfg.NextcloudBasePath)"
$common = @('--retries', '3', '--low-level-retries', '10', '--transfers', "$($cfg.NextcloudTransfers)", '--checkers', '8',
            '--stats', '1m', '--stats-one-line', '--log-level', 'INFO', '--log-file', $script:LogFile)
if ("$($cfg.BandwidthLimit)" -ne '0') { $common += @('--bwlimit', "$($cfg.BandwidthLimit)") }
if ($DryRun) { $common += '--dry-run'; Write-Log "Test run (--dry-run): nothing is uploaded." 'WARN' }

$label = 'Claude backup folder'
Write-Log "Feltoltes: $label"
Write-Log "  $($cfg.BackupRoot)  ->  $remote"
# the local run logs are not uploaded
& $rclone copy $cfg.BackupRoot $remote @common --exclude "$($cfg.LogFolder)/**" 2>&1 | ForEach-Object { Write-Host "    $_" }
$ok = ($LASTEXITCODE -eq 0)
if ($ok) { Write-Log "  $label kesz" 'OK' } else { Write-Log "  $label HIBA (rclone kod: $LASTEXITCODE)" 'ERROR' }

Write-Log "Remote storage:"
& $rclone about "$($cfg.NextcloudRemote):" 2>&1 | ForEach-Object { Write-Log "  $_" }

if ($ok) { Write-Log "================ NEXTCLOUD FELTOLTES KESZ ================" 'OK'; exit 0 }
else     { Write-Log "================ NEXTCLOUD FELTOLTES HIBAVAL ZARULT ================" 'ERROR'; exit 1 }
