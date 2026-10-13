# Fallback for release.ps1 -Upload when SFTP (port 22) is unreachable: uploads the staged release
# (release\site\versions\<zip>, manifest.json, versions.json, CHANGELOG.md) through the website's
# HTTPS bridge (DCB-Native, chunked file.upload), verifies the live files exactly like release.ps1
# does, and nudges the release newsletter. The legacy dinorr.hu channel is NOT covered (SFTP only).
#
#   .\tools\upload_release_bridge.ps1 -Version 2.8.0
#
# Prerequisite: release.ps1 -Version X.Y.Z already ran (the zip and the manifests are staged), and the
# website pages were rebuilt with S:\WEB\claudeusagemonitor.com\deploy.ps1 -Sync.
param([Parameter(Mandatory = $true)][string]$Version)
$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
if ($Version -notmatch '^\d+\.\d+\.\d+$') { throw "Version must be X.Y.Z - got: $Version" }
$Site = Join-Path (Split-Path $PSScriptRoot -Parent) "release\site"
$BaseUrl = "https://claudeusagemonitor.com/"
$cfg = Get-Content "S:\WEB\claudeusagemonitor.com\deploy.local.json" -Raw -Encoding UTF8 | ConvertFrom-Json
$headers = @{ "X-DCBN-Sig" = $cfg.sig; "X-DCBN-Token" = $cfg.token }

function Send([string]$do, [hashtable]$body, [int]$timeout = 300) {
    $json = [Text.Encoding]::UTF8.GetBytes(($body | ConvertTo-Json -Compress -Depth 4))
    $r = Invoke-RestMethod -Uri ($cfg.api + "?do=" + $do) -Method Post -Headers $headers -ContentType "application/json; charset=utf-8" -Body $json -TimeoutSec $timeout
    if (-not $r.ok) { throw "$do failed: $($r | ConvertTo-Json -Compress)" }
    return $r
}
function Sha([byte[]]$b) { ([BitConverter]::ToString([Security.Cryptography.SHA256]::Create().ComputeHash($b)) -replace '-', '').ToLower() }

# 1) the zip, in 8 MB pieces (start -> append -> final_sha256)
$zipName = "ClaudeUsageMonitor-Setup-$Version.zip"
$zipPath = Join-Path $Site "versions\$zipName"
if (-not (Test-Path $zipPath)) { throw "$zipPath is missing - run release.ps1 -Version $Version first." }
$bytes = [IO.File]::ReadAllBytes($zipPath)
$total = Sha $bytes
$chunk = 8MB
$n = [math]::Ceiling($bytes.Length / $chunk)
Write-Host ("zip: {0} bytes, {1} piece(s), sha256 {2}" -f $bytes.Length, $n, $total)
for ($i = 0; $i -lt $n; $i++) {
    $len = [math]::Min($chunk, $bytes.Length - $i * $chunk)
    $part = New-Object byte[] $len
    [Array]::Copy($bytes, $i * $chunk, $part, 0, $len)
    $body = @{ path = "versions/$zipName"; content_b64 = [Convert]::ToBase64String($part); sha256 = (Sha $part);
               mode = $(if ($i -eq 0) { "start" } else { "append" }); doc = "Claude Usage Monitor release $Version (bridge upload)" }
    if ($i -eq $n - 1) { $body.final_sha256 = $total }
    $r = Send "file.upload" $body
    Write-Host ("  piece {0}/{1}: {2} bytes, total on server {3}" -f ($i + 1), $n, $r.chunk_bytes, $r.total_bytes)
}

# 2) the three text files release.ps1 owns
foreach ($f in @("manifest.json", "versions.json", "CHANGELOG.md")) {
    $text = ([IO.File]::ReadAllText((Join-Path $Site $f), [Text.Encoding]::UTF8)).TrimStart([char]0xFEFF)
    Send "file.write" @{ path = $f; content = $text; doc = "Claude Usage Monitor release $Version (bridge upload)" } | Out-Null
    Write-Host "  up  $f"
}

# 3) verify LIVE, like release.ps1 (plus a full download of the zip, hash compared)
$local = Get-Content (Join-Path $Site "manifest.json") -Raw -Encoding UTF8 | ConvertFrom-Json
$bust = [guid]::NewGuid().ToString("N")
$live = Invoke-RestMethod -Uri ($BaseUrl + "manifest.json?" + $bust) -TimeoutSec 30
if ($live.version -ne $Version -or $live.sha256 -ne $local.sha256) { throw "LIVE manifest mismatch: $($live.version) / $($live.sha256)" }
$head = Invoke-WebRequest -Uri ($BaseUrl + "versions/$zipName") -Method Head -UseBasicParsing -TimeoutSec 60
if ([int64]$head.Headers["Content-Length"] -ne $bytes.Length) { throw "LIVE zip size mismatch: $($head.Headers['Content-Length'])" }
$dl = Invoke-WebRequest -Uri ($BaseUrl + "versions/$zipName?" + $bust) -UseBasicParsing -TimeoutSec 300
$liveSha = Sha $dl.Content
if ($liveSha -ne $total) { throw "LIVE zip sha256 mismatch: $liveSha" }
$page = Invoke-WebRequest -Uri $BaseUrl -UseBasicParsing -TimeoutSec 30
Write-Host ("LIVE OK: manifest {0}, zip {1} bytes, sha256 matches, page -> {2}" -f $live.version, $bytes.Length, $page.StatusCode) -ForegroundColor Green

# 4) release newsletter nudge (never fatal)
try {
    $mailed = 0
    for ($i = 0; $i -lt 40; $i++) {
        $tick = Invoke-RestMethod -Uri "https://claudeusagemonitor.com/usage-api/stats.php?drain=1&$([guid]::NewGuid().ToString('N'))" -TimeoutSec 60
        $mailed += [int]$tick.sent_now
        if (-not $tick.ok -or [int]$tick.queue_left -eq 0) { break }
        Start-Sleep -Seconds 2
    }
    Write-Host "release newsletter: $mailed e-mail(s) sent, $([int]$tick.queue_left) left in the queue"
} catch { Write-Host "  (newsletter nudge skipped: $($_.Exception.Message))" -ForegroundColor Yellow }
Write-Host "NOTE: the legacy dinorr.hu channel still needs SFTP: rerun release.ps1 -Version $Version -SkipBuild -Upload once port 22 works." -ForegroundColor Yellow
