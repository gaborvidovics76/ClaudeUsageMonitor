#requires -Version 5.1
<#  Test-BackupKit.ps1 - health check of the Claude Backup Kit. Safe to run any time (reads only).  #>
. (Join-Path $PSScriptRoot 'Common.ps1')
$cfg = Get-BackupConfig
$script:pass = 0; $script:fail = 0
function Check($name, $cond, $detail = '') {
    if ($cond) { Write-Host "  [OK]   $name $detail" -ForegroundColor Green; $script:pass++ }
    else       { Write-Host "  [FAIL] $name $detail" -ForegroundColor Red;   $script:fail++ }
}

Write-Host "`n===== CLAUDE BACKUP KIT - STATUS =====`n" -ForegroundColor Cyan
Check 'OneDrive folder'  (Test-Path $cfg.OneDriveRoot) $cfg.OneDriveRoot
Check 'Backup folder'    (Test-Path $cfg.BackupRoot)   $cfg.BackupRoot

$last = Get-ChildItem $cfg.LogDir -Filter 'onedrive_*.log' -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
Check 'Step 1 has run' ($null -ne $last) $(if ($last) { "last: $($last.LastWriteTime)" })
if ($last) {
    $txt = Get-Content $last.FullName -Raw
    Check 'Step 1 finished successfully' ($txt -match '=+ .* KESZ =+') $(if ($txt -match 'HIBAVAL ZARULT') { '(see the log)' })
    Check 'Step 1 is younger than 48 hours' ($last.LastWriteTime -gt (Get-Date).AddHours(-48))
}
if ($cfg.VaultPath) {
    Check 'Obsidian vault found' (Test-Path $cfg.VaultPath) $cfg.VaultPath
    $snap = Get-ChildItem $cfg.SnapDir -Filter 'Vault_*.zip' -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    Check 'Vault snapshot exists' ($null -ne $snap) $(if ($snap) { "$($snap.Name)" })
}

if ($cfg.NextcloudRemote) {
    $rclone = Get-RcloneExe
    Check 'rclone installed' ($null -ne $rclone) $rclone
    if ($rclone) {
        & $rclone lsd "$($cfg.NextcloudRemote):" --max-depth 1 2>&1 | Out-Null
        Check "Cloud '$($cfg.NextcloudRemote)' reachable" ($LASTEXITCODE -eq 0)
    }
    $l2 = Get-ChildItem $cfg.LogDir -Filter 'nextcloud_*.log' -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    Check 'Step 2 has run' ($null -ne $l2) $(if ($l2) { "last: $($l2.LastWriteTime)" })
    if ($l2) { Check 'Step 2 was a real upload (not a test run)' (-not ((Get-Content $l2.FullName -Raw) -match '--dry-run')) }
}

foreach ($n in @("$($cfg.TaskPrefix) 1 - OneDrive", "$($cfg.TaskPrefix) 2 - Nextcloud")) {
    if ($n -like '* 2 - *' -and -not $cfg.NextcloudRemote) { continue }
    $t = Get-ScheduledTask -TaskName $n -ErrorAction SilentlyContinue
    Check "Scheduled task: $n" ($null -ne $t)
    if ($t) { $i = $t | Get-ScheduledTaskInfo; Write-Host "         last run: $($i.LastRunTime), result: $($i.LastTaskResult), next: $($i.NextRunTime)" }
}

$prof = Join-Path $env:APPDATA 'ClaudeUsageMonitor\backup_profile.json'
Check 'Claude Usage Monitor profile' (Test-Path $prof) $prof

Write-Host "`n  Total: $script:pass OK, $script:fail failed`n" -ForegroundColor $(if ($script:fail -eq 0) { 'Green' } else { 'Red' })
