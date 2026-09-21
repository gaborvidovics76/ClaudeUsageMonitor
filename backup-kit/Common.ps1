# ============================================================
#  Common.ps1 - shared functions of the Claude Backup Kit
#
#  LOG FORMAT - please do not change it.
#  Claude Usage Monitor reads these log files. Every line is
#      yyyy-MM-dd HH:mm:ss [LEVEL] message
#  and a few fixed words mark the events (they are ASCII Hungarian,
#  because the kit comes from a Hungarian original):
#      "... INDUL ====="       run started
#      "===== ... KESZ ====="  run finished successfully
#      "... HIBAVAL ZARULT"    run finished with errors
#      "Cel: <folder>"         destination
#      "Masolas: <name>"       a folder is being copied (step 1)
#      "<name> - rendben (robocopy kod: N)" / "<name> - HIBA (robocopy kod: N)"
#      "Kihagyva (nincs ilyen mappa): <name>"   source folder missing
#      "Vault pillanatkep kesz: <zip> (<n> MB)" vault snapshot created
#      "Feltoltes: <name>"     upload started (step 2)
#      "<name> kesz" / "<name> HIBA (rclone kod: N)"
# ============================================================

function Expand-KitPath([string]$Path) {
    if ([string]::IsNullOrWhiteSpace($Path)) { return '' }
    return [Environment]::ExpandEnvironmentVariables($Path.Trim())
}

function Get-OneDriveRoot {
    foreach ($c in @($env:OneDrive, $env:OneDriveConsumer, $env:OneDriveCommercial, (Join-Path $env:USERPROFILE 'OneDrive'))) {
        if (-not [string]::IsNullOrWhiteSpace($c) -and (Test-Path $c)) { return $c }
    }
    return $null
}

function Get-BackupConfig {
    $cfgPath = Join-Path $PSScriptRoot 'config.psd1'
    if (-not (Test-Path $cfgPath)) { throw "config.psd1 is missing: $cfgPath" }
    $cfg = Import-PowerShellDataFile -Path $cfgPath

    $od = Get-OneDriveRoot
    if (-not $od) { throw "OneDrive folder not found. Is OneDrive installed and signed in?" }

    $cfg['ConfigPath']   = $cfgPath
    $cfg['OneDriveRoot'] = $od
    $cfg['BackupRoot']   = Join-Path $od $cfg.OneDriveSubFolder
    $cfg['SnapDir']      = Join-Path $cfg['BackupRoot'] $cfg.SnapshotFolder
    $cfg['FileDir']      = Join-Path $cfg['BackupRoot'] $cfg.FileFolder
    $cfg['LogDir']       = Join-Path $cfg['BackupRoot'] $cfg.LogFolder
    $cfg['VaultPath']    = Expand-KitPath $cfg.VaultPath
    return $cfg
}

function New-BackupFolders {
    param([hashtable]$Cfg)
    foreach ($d in @($Cfg.BackupRoot, $Cfg.SnapDir, $Cfg.FileDir, $Cfg.LogDir)) {
        if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d -Force | Out-Null }
    }
}

$script:LogFile = $null
function Start-BackupLog {
    param([string]$LogDir, [string]$Name)
    $stamp = Get-Date -Format 'yyyy-MM-dd_HHmmss'   # seconds: two runs in the same minute must not share one log
    $script:LogFile = Join-Path $LogDir "$Name`_$stamp.log"
    $n = 2
    while (Test-Path $script:LogFile) { $script:LogFile = Join-Path $LogDir "$Name`_$stamp`_$n.log"; $n++ }   # never append to an older run
    return $script:LogFile
}

function Write-Log {
    param([string]$Message, [ValidateSet('INFO','WARN','ERROR','OK')][string]$Level = 'INFO')
    $line = "{0} [{1,-5}] {2}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Level, $Message
    switch ($Level) {
        'ERROR' { Write-Host $line -ForegroundColor Red }
        'WARN'  { Write-Host $line -ForegroundColor Yellow }
        'OK'    { Write-Host $line -ForegroundColor Green }
        default { Write-Host $line }
    }
    if ($script:LogFile) { Add-Content -Path $script:LogFile -Value $line -Encoding UTF8 }
}

function Test-RobocopyResult {
    param([int]$ExitCode, [string]$What)
    # robocopy: 0-7 = success (1 = files copied, 0 = nothing to do), 8+ = failure
    if ($ExitCode -lt 8) { Write-Log "$What - rendben (robocopy kod: $ExitCode)" 'OK'; return $true }
    Write-Log "$What - HIBA (robocopy kod: $ExitCode)" 'ERROR'
    return $false
}

function Get-RcloneExe {
    $c = Get-Command rclone.exe -ErrorAction SilentlyContinue
    if ($c) { return $c.Source }
    $candidates = @("$env:ProgramFiles\rclone\rclone.exe", "$env:LOCALAPPDATA\Microsoft\WinGet\Links\rclone.exe", "C:\rclone\rclone.exe")
    $candidates += @(Get-ChildItem "$env:LOCALAPPDATA\Microsoft\WinGet\Packages\Rclone.Rclone*" -Recurse -Filter rclone.exe -ErrorAction SilentlyContinue | ForEach-Object FullName)
    foreach ($p in $candidates) { if ($p -and (Test-Path $p)) { return $p } }
    return $null
}

function Get-KitJobs {
    # The folders step 1 copies. Name = what appears in the log and in Claude Usage Monitor.
    param([hashtable]$Cfg)
    $jobs = @()
    if ($Cfg.BackupClaudeCode) {
        $jobs += @{ Name = 'Claude Code (.claude)'; Dest = 'claude-code'
                    Src  = (Join-Path $env:USERPROFILE '.claude')
                    # the sign-in token never goes into a backup
                    Extra = @('/XF', '.credentials.json', '*.token', '/XD', 'shell-snapshots', 'statsig', 'todos') }
    }
    if ($Cfg.BackupClaudeDesktop) {
        $jobs += @{ Name = 'Claude Desktop'; Dest = 'claude-desktop'
                    Src  = (Join-Path $env:APPDATA 'Claude')
                    # caches rebuild themselves; cookies hold a session token; vm_bundles is a re-downloadable VM image
                    Extra = @('/XD', 'Cache', 'GPUCache', 'Code Cache', 'logs', 'vm_bundles', 'DawnGraphiteCache', 'DawnWebGPUCache',
                              'Crashpad', 'sentry', 'blob_storage', 'VideoDecodeStats', 'shared_proto_db', 'Shared Dictionary',
                              'local-agent-mode-sessions',
                              '/XF', 'Cookies', 'Cookies-journal', 'lockfile', '*.lock') }
    }
    foreach ($x in @($Cfg.ExtraFolders)) {
        if (-not $x -or -not $x.Name -or -not $x.Path) { continue }
        $safe = ($x.Name -replace '[^\w\-. ]', '_').Trim()
        $jobs += @{ Name = $x.Name; Dest = $safe; Src = (Expand-KitPath $x.Path); Extra = @() }
    }
    return $jobs
}
