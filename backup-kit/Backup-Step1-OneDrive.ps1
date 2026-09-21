#requires -Version 5.1
<#
    Backup-Step1-OneDrive.ps1
    STEP 1: Claude files (+ optional Obsidian vault, + your extra folders) -> your OneDrive folder.
    OneDrive then uploads them to the cloud. Run daily by the scheduled task "<TaskPrefix> 1 - OneDrive".

    Safety rules of this script:
      * never mirrors (no /MIR): a file you delete from the source stays in the backup
      * never backs up the Claude Code sign-in token (.credentials.json)
      * the vault goes into a dated ZIP, so a later bad copy cannot overwrite an older state
#>
[CmdletBinding()]
param([switch]$WhatIfOnly)

$ErrorActionPreference = 'Continue'
. (Join-Path $PSScriptRoot 'Common.ps1')

$cfg = Get-BackupConfig
New-BackupFolders -Cfg $cfg
Start-BackupLog -LogDir $cfg.LogDir -Name 'onedrive' | Out-Null

Write-Log "================ ONEDRIVE MENTES INDUL ================"
Write-Log "Cel: $($cfg.BackupRoot)"

$stamp = Get-Date -Format 'yyyy-MM-dd_HHmm'
$ok = $true

# ---------- 1) OBSIDIAN VAULT SNAPSHOT (optional) ----------
if ($cfg.VaultPath) {
    if (Test-Path $cfg.VaultPath) {
        try {
            Add-Type -AssemblyName System.IO.Compression.FileSystem
            $tmp = Join-Path $env:TEMP "kit_vault_$stamp"
            if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue }
            Write-Log "Copying the vault to a temporary folder first (Obsidian may hold files open)..."
            robocopy $cfg.VaultPath $tmp /E /R:1 /W:1 /NFL /NDL /NJH /NJS /XD '.trash' | Out-Null
            $zip = Join-Path $cfg.SnapDir "Vault_$stamp.zip"
            if (Test-Path $zip) { Remove-Item $zip -Force }
            if (-not $WhatIfOnly) { [System.IO.Compression.ZipFile]::CreateFromDirectory($tmp, $zip) }
            Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue
            $mb = if (Test-Path $zip) { [math]::Round((Get-Item $zip).Length / 1MB, 1) } else { 0 }
            Write-Log "Vault pillanatkep kesz: $(Split-Path $zip -Leaf) ($mb MB)" 'OK'
        } catch {
            Write-Log "HIBA a vault mentesenel: $($_.Exception.Message)" 'ERROR'
            $ok = $false
        }
    } else {
        Write-Log "Nem talalhato a vault: $($cfg.VaultPath)" 'ERROR'
        $ok = $false
    }
}

# ---------- 2) FOLDERS ----------
# /E  = with sub-folders   /XO = never overwrite with an older file   /XJD = skip junctions
$rc = @('/E', '/XO', '/XJD', '/R:1', '/W:1', '/NP', '/NFL', '/NDL', "/MAX:$([int64]$cfg.MaxFileMB * 1MB)")
foreach ($j in (Get-KitJobs -Cfg $cfg)) {
    if (-not (Test-Path $j.Src)) { Write-Log "Kihagyva (nincs ilyen mappa): $($j.Name)" 'WARN'; continue }
    $dst = Join-Path $cfg.FileDir $j.Dest
    Write-Log "Masolas: $($j.Name)"
    if ($WhatIfOnly) { Write-Log "  [WhatIf] $($j.Src) -> $dst"; continue }
    $rbArgs = @($j.Src, $dst) + $rc + $j.Extra
    & robocopy @rbArgs | Out-Null
    if (-not (Test-RobocopyResult -ExitCode $LASTEXITCODE -What $j.Name)) { $ok = $false }
}

# ---------- 3) AGENT (COWORK) CONVERSATION LOGS: one ZIP per session ----------
# Their original paths are too long for OneDrive (>400 characters), a short ZIP name solves it.
if ($cfg.BackupCoworkLogs) {
    $src = Join-Path $env:APPDATA 'Claude\local-agent-mode-sessions'
    $dst = Join-Path $cfg.FileDir 'cowork-logs'
    if (Test-Path $src) {
        Write-Log "Zipping agent session logs..."
        if (-not (Test-Path $dst)) { New-Item -ItemType Directory -Path $dst -Force | Out-Null }
        $zipped = 0
        Get-ChildItem $src -Directory -Recurse -Depth 2 -Filter 'local_*' -ErrorAction SilentlyContinue | ForEach-Object {
            $claudeDir = Join-Path $_.FullName '.claude'
            if (-not (Test-Path (Join-Path $claudeDir 'projects'))) { return }
            $newest = Get-ChildItem -LiteralPath "\\?\$claudeDir\projects" -Recurse -File -Force -ErrorAction SilentlyContinue |
                      Sort-Object LastWriteTime -Descending | Select-Object -First 1
            if (-not $newest) { return }
            $zip = Join-Path $dst "$($_.Name).zip"
            if ((Test-Path $zip) -and (Get-Item $zip).LastWriteTime -ge $newest.LastWriteTime) { return }
            if ($WhatIfOnly) { return }
            $tmpZip = Join-Path $env:TEMP "kit_cowork_$($_.Name).zip"
            Remove-Item $tmpZip -Force -ErrorAction SilentlyContinue
            & tar.exe -a -c -f $tmpZip -C $claudeDir projects 2>&1 | Out-Null
            if ($LASTEXITCODE -eq 0 -and (Test-Path $tmpZip)) { Move-Item $tmpZip $zip -Force; $zipped++ }
            else { Write-Log "  HIBA a ZIP-elesnel: $($_.Name) (tar code: $LASTEXITCODE)" 'ERROR'; $script:ok = $false }
        }
        Write-Log "Cowork naplok rendben ($zipped new/updated ZIP)" 'OK'
    }
}

# ---------- 4) HOUSEKEEPING ----------
Get-ChildItem $cfg.SnapDir -Filter 'Vault_*.zip' -ErrorAction SilentlyContinue |
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-[int]$cfg.KeepSnapshotDays) } |
    ForEach-Object { Write-Log "  deleting old snapshot: $($_.Name)"; Remove-Item $_.FullName -Force }
Get-ChildItem $cfg.LogDir -Filter '*.log' -ErrorAction SilentlyContinue |
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-90) } | Remove-Item -Force -ErrorAction SilentlyContinue

if ($ok) { Write-Log "================ ONEDRIVE MENTES KESZ ================" 'OK'; exit 0 }
else     { Write-Log "================ ONEDRIVE MENTES HIBAVAL ZARULT ================" 'ERROR'; exit 1 }
