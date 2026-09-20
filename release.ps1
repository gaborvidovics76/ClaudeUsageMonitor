<#
.SYNOPSIS
  Claude Usage Monitor - one-command release.

.DESCRIPTION
  1. writes the version into claude_usage\__init__.py,
  2. builds the exe (build.ps1),
  3. assembles the installable package (program + installer + read-me),
  4. zips it (forward-slash entries) into release\site\versions\,
  5. updates manifest.json / versions.json / CHANGELOG.md (SHA-256 included),
  6. optionally mirrors the site folder and uploads it (-Upload), then verifies it over HTTPS.

  Machine-specific things (where the local web mirror is, which rclone remote to use) are NOT
  in this file. They come from release.local.psd1 next to it, which is git-ignored:

      @{
          MirrorDir    = 'D:\path\to\local\webroot\claude-usage-monitor'   # optional
          RcloneExe    = 'rclone.exe'
          RcloneTarget = 'myremote:httpdocs/claude-usage-monitor'
      }

.EXAMPLE
  .\release.ps1 -Version 2.3.0 -NotesFile release\notes\2.3.0.json -Upload
  The notes file is UTF-8 JSON: { "en": ["..."], "hu": ["..."] }
#>
param(
    [Parameter(Mandatory = $true)][string]$Version,
    [string]$NotesFile = "",
    [string]$BaseUrl = "https://dinorr.hu/claude-usage-monitor/",
    [switch]$SkipBuild,
    [switch]$Upload
)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
function Read-Utf8([string]$p) { [IO.File]::ReadAllText($p, [Text.Encoding]::UTF8) }
function Write-Utf8([string]$p, [string]$c) { [IO.File]::WriteAllText($p, $c, $Utf8NoBom) }
function Info([string]$m) { Write-Host "  $m" -ForegroundColor Green }
# PowerShell 5.1 turns a native program's stderr into a terminating error when
# $ErrorActionPreference is 'Stop' (PyInstaller and rclone both log to stderr).
# Run such tools through cmd with stderr merged, and judge them by exit code only.
function Invoke-Native([string]$commandLine) {
    $prev = $ErrorActionPreference; $ErrorActionPreference = "Continue"
    try { & cmd.exe /d /c "`"$commandLine 2>&1`"" | ForEach-Object { Write-Host "    $_" -ForegroundColor DarkGray } }
    finally { $ErrorActionPreference = $prev }
    return $LASTEXITCODE
}

if ($Version -notmatch '^\d+\.\d+\.\d+$') { throw "Version must be X.Y.Z - got: $Version" }
$AppId   = "ClaudeUsageMonitor"
$Site    = Join-Path $PSScriptRoot "release\site"
$VerDir  = Join-Path $Site "versions"
$Stage   = Join-Path $PSScriptRoot "build\package"
$ZipName = "$AppId-Setup-$Version.zip"
$ZipPath = Join-Path $VerDir $ZipName
Write-Host "== Claude Usage Monitor - release $Version ==" -ForegroundColor Cyan

# ---------------------------------------------------------------- notes
$notes = [ordered]@{ en = @(); hu = @() }
if (-not $NotesFile) { $NotesFile = Join-Path $PSScriptRoot "release\notes\$Version.json" }
if (Test-Path $NotesFile) {
    $n = (Read-Utf8 $NotesFile) | ConvertFrom-Json
    foreach ($lang in @($n.PSObject.Properties.Name)) { $notes[$lang] = @($n.$lang) }
} else { Write-Host "  (no notes file: $NotesFile)" -ForegroundColor Yellow }

# ---------------------------------------------------------------- 1. version
$init = Join-Path $PSScriptRoot "claude_usage\__init__.py"
$src = Read-Utf8 $init
$src = [regex]::Replace($src, '(__version__\s*=\s*")\d+\.\d+\.\d+(")', ('${1}' + $Version + '${2}'))
Write-Utf8 $init $src
Info "version written: $Version"

# ---------------------------------------------------------------- 2. build
if (-not $SkipBuild) {
    $code = Invoke-Native ('powershell.exe -NoProfile -ExecutionPolicy Bypass -File "{0}"' -f (Join-Path $PSScriptRoot "build.ps1"))
    if ($code -ne 0) { throw "build.ps1 failed ($code)" }
}
$dist = Join-Path $PSScriptRoot "dist\$AppId"
if (-not (Test-Path (Join-Path $dist "$AppId.exe"))) { throw "dist\$AppId\$AppId.exe is missing - build first." }

# ---------------------------------------------------------------- 3. package
if (Test-Path $Stage) { Remove-Item $Stage -Recurse -Force }
$appOut = Join-Path $Stage "app\$AppId"
New-Item -ItemType Directory -Force -Path $appOut, (Join-Path $Stage "installer") | Out-Null
& robocopy $dist $appOut /E /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy failed ($LASTEXITCODE)" }
$inst = Join-Path $PSScriptRoot "installer"
Copy-Item (Join-Path $inst "Install.ps1"), (Join-Path $inst "Uninstall.ps1") (Join-Path $Stage "installer")
foreach ($f in @("INSTALL.bat", "TELEPITES.bat", "README.txt", "OLVASS-EL.txt")) { Copy-Item (Join-Path $inst $f) $Stage }
Copy-Item (Join-Path $PSScriptRoot "LICENSE") (Join-Path $Stage "LICENSE.txt")
Write-Utf8 (Join-Path $Stage "VERSION") "$Version`n"
# The uninstaller and the version travel INSIDE the program folder, so they survive a
# self-update (which replaces that folder as a whole).
Copy-Item (Join-Path $inst "Uninstall.ps1") $appOut
Write-Utf8 (Join-Path $appOut "VERSION") "$Version`n"
[IO.File]::WriteAllText((Join-Path $appOut "Uninstall.bat"),
    "@echo off`r`npowershell -NoProfile -ExecutionPolicy Bypass -File ""%~dp0Uninstall.ps1""`r`n", [Text.Encoding]::ASCII)
Info "package staged"

# ---------------------------------------------------------------- 4. zip (forward slashes)
Add-Type -AssemblyName System.IO.Compression | Out-Null
Add-Type -AssemblyName System.IO.Compression.FileSystem | Out-Null
New-Item -ItemType Directory -Force -Path $VerDir | Out-Null
if (Test-Path $ZipPath) { Remove-Item $ZipPath -Force }
$base = (Resolve-Path $Stage).Path.TrimEnd('\')
$fs  = [IO.File]::Open($ZipPath, [IO.FileMode]::Create)
$zip = New-Object IO.Compression.ZipArchive($fs, [IO.Compression.ZipArchiveMode]::Create)
$count = 0
try {
    foreach ($file in (Get-ChildItem $Stage -Recurse -File | Sort-Object FullName)) {
        $rel = $file.FullName.Substring($base.Length + 1).Replace('\', '/')
        $entry = $zip.CreateEntry($rel, [IO.Compression.CompressionLevel]::Optimal)
        $out = $entry.Open(); $in = [IO.File]::OpenRead($file.FullName)
        try { $in.CopyTo($out) } finally { $in.Dispose(); $out.Dispose() }
        $count++
    }
} finally { $zip.Dispose(); $fs.Dispose() }
$zipInfo = Get-Item $ZipPath
$sha = (Get-FileHash $ZipPath -Algorithm SHA256).Hash.ToLower()
Info ("zip: {0} ({1:N1} MB, {2} files)" -f $ZipName, ($zipInfo.Length / 1MB), $count)

# ---------------------------------------------------------------- 5. manifest / versions / changelog
$now = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
$url = "$BaseUrl" + "versions/$ZipName"
$manifest = [ordered]@{
    name = "Claude Usage Monitor"; slug = "claude-usage-monitor"; version = $Version
    download_url = $url; sha256 = $sha; bytes = $zipInfo.Length
    requires = "Windows 10/11 64-bit"; author = "Vidovics Gabor"
    homepage = $BaseUrl; last_updated = $now; notes = $notes
}
Write-Utf8 (Join-Path $Site "manifest.json") ($manifest | ConvertTo-Json -Depth 6)

$vfile = Join-Path $Site "versions.json"
$all = @()
if (Test-Path $vfile) {
    $ex = (Read-Utf8 $vfile) | ConvertFrom-Json
    if ($ex.versions) { $all = @($ex.versions | Where-Object { $_.version -ne $Version }) }
}
$all += [pscustomobject]@{ version = $Version; download_url = $url; sha256 = $sha; released = $now; bytes = $zipInfo.Length }
$sorted = @($all | Sort-Object -Property @{ Expression = { [version]$_.version } } -Descending)
Write-Utf8 $vfile ([ordered]@{ slug = "claude-usage-monitor"; latest = $sorted[0].version; versions = $sorted } | ConvertTo-Json -Depth 6)
Info "manifest.json + versions.json ($($sorted.Count) versions)"

$clPath = Join-Path $Site "CHANGELOG.md"
$marker = "<!-- newer-versions-here -->"
$sec = @("## [$Version] - $((Get-Date).ToString('yyyy-MM-dd'))", "")
foreach ($line in $notes.en) { $sec += "- $line" }
if ($notes.hu.Count -gt 0) { $sec += ""; $sec += "*Magyarul:*"; $sec += ""; foreach ($line in $notes.hu) { $sec += "- $line" } }
$sec += ""
if (Test-Path $clPath) { $cl = Read-Utf8 $clPath } else { $cl = "# Claude Usage Monitor - changelog`n`n$marker`n" }
if ($cl -notmatch [regex]::Escape("## [$Version]")) {
    $cl = $cl.Replace($marker, $marker + "`n`n" + ($sec -join "`n"))
    Write-Utf8 $clPath $cl
}
Info "CHANGELOG.md"

# ---------------------------------------------------------------- 6. mirror + upload + verify
$localCfg = Join-Path $PSScriptRoot "release.local.psd1"
if ($Upload) {
    if (-not (Test-Path $localCfg)) { throw "release.local.psd1 is missing - see the header of this script." }
    $cfg = Import-PowerShellDataFile $localCfg
    # The website has one pre-rendered page per language with the version, date and release notes baked in
    # (search and AI crawlers do not run scripts). Rebuild them from the manifest written above, upload them,
    # and copy them into release\site so the rclone step below ships exactly the same pages. Optional.
    if ($cfg.SiteDeploy -and (Test-Path $cfg.SiteDeploy)) {
        $code = Invoke-Native ('powershell.exe -NoProfile -ExecutionPolicy Bypass -File "{0}" -Sync' -f $cfg.SiteDeploy)
        if ($code -ne 0) { Write-Host "  WARNING: website rebuild failed ($code) - the pages keep the previous version text" -ForegroundColor Yellow }
        else { Info "website pages rebuilt for $Version" }
    }
    if ($cfg.MirrorDir) {
        New-Item -ItemType Directory -Force -Path $cfg.MirrorDir | Out-Null
        & robocopy $Site $cfg.MirrorDir /E /NFL /NDL /NJH /NJS /NP | Out-Null
        if ($LASTEXITCODE -ge 8) { throw "mirror copy failed ($LASTEXITCODE)" }
        Info "mirrored to the local web mirror"
    }
    $code = Invoke-Native ('"{0}" copy "{1}" "{2}" --transfers 4 --stats-one-line' -f $cfg.RcloneExe, $Site, $cfg.RcloneTarget)
    if ($code -ne 0) { throw "rclone upload failed ($code)" }
    Info "uploaded"

    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    $bust = [guid]::NewGuid().ToString("N")
    $live = Invoke-RestMethod -Uri ($BaseUrl + "manifest.json?" + $bust) -TimeoutSec 30
    if ($live.version -ne $Version -or $live.sha256 -ne $sha) { throw "LIVE manifest mismatch: $($live.version) / $($live.sha256)" }
    $head = Invoke-WebRequest -Uri $url -Method Head -UseBasicParsing -TimeoutSec 60
    if ([int64]$head.Headers["Content-Length"] -ne $zipInfo.Length) { throw "LIVE zip size mismatch" }
    $phpStatus = 0
    try { Invoke-WebRequest -Uri ($BaseUrl + "index.php") -UseBasicParsing -TimeoutSec 30 | Out-Null; $phpStatus = 200 }
    catch { $phpStatus = [int]$_.Exception.Response.StatusCode }
    $page = Invoke-WebRequest -Uri $BaseUrl -UseBasicParsing -TimeoutSec 30
    Info "LIVE OK: manifest $($live.version), zip $($zipInfo.Length) bytes, index.php -> $phpStatus, page -> $($page.StatusCode)"
    if ($phpStatus -eq 200) { Write-Host "  WARNING: index.php answered 200 - PHP is not blocked!" -ForegroundColor Red }

    # Release newsletter: the website backend notices the new manifest by itself on the next page visit.
    # Nudging it here sends the e-mails right away (small batches; never fatal for the release).
    try {
        $mailed = 0
        for ($i = 0; $i -lt 40; $i++) {
            $tick = Invoke-RestMethod -Uri "https://dinorr.hu/usage-api/stats.php?drain=1&$([guid]::NewGuid().ToString('N'))" -TimeoutSec 60
            $mailed += [int]$tick.sent_now
            if (-not $tick.ok -or [int]$tick.queue_left -eq 0) { break }
            Start-Sleep -Seconds 2
        }
        Info "release newsletter: $mailed e-mail(s) sent, $([int]$tick.queue_left) left in the queue"
    } catch { Write-Host "  (newsletter nudge skipped: $($_.Exception.Message))" -ForegroundColor Yellow }
}

Write-Host ""
Write-Host "DONE  $ZipPath" -ForegroundColor Cyan
Write-Host "SHA-256: $sha" -ForegroundColor DarkGray
