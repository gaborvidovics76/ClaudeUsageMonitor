#requires -Version 5.1
<#
    Install-BackupKit.ps1  -  one-time setup of the Claude Backup Kit. Run it AS ADMINISTRATOR.

    What it does (you see every step):
      1. reads config.psd1 and finds your OneDrive
      2. creates the backup folder structure
      3. installs rclone if needed (winget) - only if step 2 (second cloud) is on
      4. sets up the Nextcloud connection (Set-CloudRemote.ps1) - you type the app password
      5. registers two scheduled tasks: step 1 daily, step 2 right after it
      6. writes the profile of Claude Usage Monitor, so the backup lamps appear by themselves
      7. first run: step 1 for real, step 2 as a test run (uploads nothing)

    Switches:  -SkipTasks  -SkipRemote  -SkipFirstRun
               -MonitorProfile <path>   write the monitor profile somewhere else (testing)
#>
[CmdletBinding()]
param([switch]$SkipTasks, [switch]$SkipRemote, [switch]$SkipFirstRun, [string]$MonitorProfile = '')

$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'Common.ps1')
function Section($t) { Write-Host ""; Write-Host ("=" * 64) -ForegroundColor Cyan; Write-Host "  $t" -ForegroundColor Cyan; Write-Host ("=" * 64) -ForegroundColor Cyan }

$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin -and -not $SkipTasks) {
    Write-Host "Please run this script AS ADMINISTRATOR (the scheduled tasks need it)." -ForegroundColor Red
    Write-Host "Win+X -> Terminal (Admin), then:  cd `"$PSScriptRoot`" ; .\Install-BackupKit.ps1" -ForegroundColor Yellow
    exit 1
}

Section '1/7  Settings'
$cfg = Get-BackupConfig
Write-Host "  OneDrive       : $($cfg.OneDriveRoot)"
Write-Host "  Backup folder  : $($cfg.BackupRoot)"
Write-Host "  Obsidian vault : $(if ($cfg.VaultPath) { $cfg.VaultPath } else { '(not used)' })"
Write-Host "  Second cloud   : $(if ($cfg.NextcloudRemote) { "$($cfg.NextcloudRemote):$($cfg.NextcloudBasePath)" } else { '(off)' })"
if ($cfg.VaultPath -and -not (Test-Path $cfg.VaultPath)) { Write-Host "  WARNING: the vault path does not exist - fix VaultPath in config.psd1." -ForegroundColor Yellow }

Section '2/7  Folders'
New-BackupFolders -Cfg $cfg
Write-Host "  OK: $($cfg.BackupRoot)" -ForegroundColor Green

Section '3/7  rclone'
if (-not $cfg.NextcloudRemote) { Write-Host "  Step 2 is off - rclone is not needed." }
else {
    $rclone = Get-RcloneExe
    if (-not $rclone) {
        Write-Host "  Installing rclone with winget..."
        winget install --id Rclone.Rclone -e --accept-source-agreements --accept-package-agreements
        $env:Path = [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' + [Environment]::GetEnvironmentVariable('Path', 'User')
        $rclone = Get-RcloneExe
    }
    if (-not $rclone) { Write-Host "  rclone could not be installed. Download it from https://rclone.org/downloads/" -ForegroundColor Red; exit 2 }
    Write-Host "  OK: $rclone" -ForegroundColor Green
}

Section '4/7  Cloud connection'
if (-not $cfg.NextcloudRemote -or $SkipRemote) { Write-Host "  skipped" }
else {
    $existing = & (Get-RcloneExe) listremotes 2>&1
    if ($existing -contains "$($cfg.NextcloudRemote):") {
        Write-Host "  The remote '$($cfg.NextcloudRemote)' already exists - kept. (Re-create it any time: .\Set-CloudRemote.ps1)" -ForegroundColor Green
    } else {
        & (Join-Path $PSScriptRoot 'Set-CloudRemote.ps1')
        if ($LASTEXITCODE -ne 0) { Write-Host "  The connection is not working yet - fix it with .\Set-CloudRemote.ps1, then run this installer again." -ForegroundColor Red; exit 3 }
    }
}

Section '5/7  Scheduled tasks'
$task1 = "$($cfg.TaskPrefix) 1 - OneDrive"
$task2 = "$($cfg.TaskPrefix) 2 - Nextcloud"
if ($SkipTasks) { Write-Host "  skipped (-SkipTasks)" }
else {
    # Step 2 starts when step 1 has FINISHED (not at a fixed time): otherwise, after a late start,
    # both could run at once and step 2 would read a half-written vault ZIP.
    # The chain needs the Task Scheduler operational log, which Windows keeps off by default.
    $evtLog = 'Microsoft-Windows-TaskScheduler/Operational'
    if (-not (Get-WinEvent -ListLog $evtLog -ErrorAction SilentlyContinue).IsEnabled) {
        wevtutil sl $evtLog /e:true
        Write-Host "  Task Scheduler history switched on (needed to chain the two steps)"
    }
    $defs = @(@{ Name = $task1; Script = 'Backup-Step1-OneDrive.ps1'; Desc = 'Claude Backup Kit - step 1: Claude files to OneDrive' })
    if ($cfg.NextcloudRemote) { $defs += @{ Name = $task2; Script = 'Backup-Step2-Cloud.ps1'; After = $task1; Desc = 'Claude Backup Kit - step 2: second copy to the cloud (rclone)' } }
    foreach ($t in $defs) {
        $scriptPath = Join-Path $PSScriptRoot $t.Script
        $act = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$scriptPath`""
        if ($t.After) {
            $q = "<QueryList><Query Id=`"0`" Path=`"$evtLog`"><Select Path=`"$evtLog`">" +
                 "*[System[Provider[@Name='Microsoft-Windows-TaskScheduler'] and EventID=102]] and " +
                 "*[EventData[Data[@Name='TaskName']='\$($t.After)']]</Select></Query></QueryList>"
            $trg = New-CimInstance -CimClass (Get-CimClass MSFT_TaskEventTrigger Root/Microsoft/Windows/TaskScheduler) -ClientOnly
            $trg.Enabled = $true; $trg.Subscription = $q; $trg.Delay = 'PT1M'
        } else {
            $trg = New-ScheduledTaskTrigger -Daily -At $cfg.DailyTime
        }
        $set = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopIfGoingOnBatteries -AllowStartIfOnBatteries `
               -ExecutionTimeLimit (New-TimeSpan -Hours 6) -MultipleInstances IgnoreNew
        $prc = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Highest
        Register-ScheduledTask -TaskName $t.Name -Action $act -Trigger $trg -Settings $set -Principal $prc -Description $t.Desc -Force | Out-Null
        Write-Host ("  OK: '{0}' - {1}" -f $t.Name, $(if ($t.After) { "right after '$($t.After)'" } else { "daily at $($cfg.DailyTime)" })) -ForegroundColor Green
    }
}

Section '6/7  Claude Usage Monitor profile'
# Tells the monitor where the backups are, so the OneDrive / Nextcloud / Obsidian lamps appear.
$profilePath = if ($MonitorProfile) { $MonitorProfile } else { Join-Path $env:APPDATA 'ClaudeUsageMonitor\backup_profile.json' }
$jobs = [ordered]@{}
foreach ($j in (Get-KitJobs -Cfg $cfg)) { $jobs[$j.Name] = [ordered]@{ dest = (Join-Path $cfg.FileFolder $j.Dest); source = $j.Src } }
if ($cfg.BackupCoworkLogs) { $jobs['@cowork'] = [ordered]@{ dest = (Join-Path $cfg.FileFolder 'cowork-logs'); source = (Join-Path $env:APPDATA 'Claude\local-agent-mode-sessions') } }
$monProfile = [ordered]@{
    _comment            = 'Written by the Claude Backup Kit installer. Paths only - no password, no token.'
    root                = $cfg.BackupRoot
    log_dir             = $cfg.LogFolder
    snapshot_dir        = $cfg.SnapshotFolder
    snapshot_glob       = 'Vault_*.zip'
    onedrive_log_prefix = 'onedrive'
    nextcloud_log_prefix = 'nextcloud'
    script_config       = $cfg.ConfigPath
    task_filter         = "$($cfg.TaskPrefix)*"
    jobs                = $jobs
}
$write = $true
if ((Test-Path $profilePath) -and -not $MonitorProfile) {
    $ans = Read-Host "  A monitor profile already exists ($profilePath). Replace it? (y/N)"
    $write = ($ans -match '^[yYiI]')
    if ($write) { Copy-Item $profilePath "$profilePath.bak" -Force; Write-Host "  old profile saved as $profilePath.bak" }
}
if ($write) {
    New-Item -ItemType Directory -Force -Path (Split-Path $profilePath) | Out-Null
    [IO.File]::WriteAllText($profilePath, ($monProfile | ConvertTo-Json -Depth 5), (New-Object Text.UTF8Encoding($false)))
    Write-Host "  OK: $profilePath" -ForegroundColor Green
    Write-Host "  The lamps appear within 5 minutes (or: right-click the panel -> Backups... -> Check now)."
}

Section '7/7  First run'
if ($SkipFirstRun) { Write-Host "  skipped" }
else {
    & (Join-Path $PSScriptRoot 'Backup-Step1-OneDrive.ps1')
    if ($cfg.NextcloudRemote) { & (Join-Path $PSScriptRoot 'Backup-Step2-Cloud.ps1') -DryRun }
}

Write-Host ""
Write-Host "DONE." -ForegroundColor Green
Write-Host "  Check the whole system any time:   .\Test-BackupKit.ps1"
Write-Host "  First real upload to the cloud:    .\Backup-Step2-Cloud.ps1"
Write-Host "  Logs: $($cfg.LogDir)"
