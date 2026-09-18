<#
.SYNOPSIS
  Makes the hand-over package for whoever builds the macOS version.

.DESCRIPTION
  Zips the COMMITTED source (git archive of HEAD) into handoff\ClaudeUsageMonitor-macOS-kit-<version>.zip.
  Going through git guarantees what a Mac needs: LF line endings and executable shell scripts,
  and that nothing local (upload accounts, builds, personal profiles) can slip in.
  Commit first - uncommitted changes are not part of the kit.

.EXAMPLE
  .\make_macos_kit.ps1
#>
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
$init = [IO.File]::ReadAllText((Join-Path $PSScriptRoot "claude_usage\__init__.py"))
$version = [regex]::Match($init, '__version__\s*=\s*"([^"]+)"').Groups[1].Value
if (-not $version) { throw "version not found" }
$dirty = (& git status --porcelain --untracked-files=no) | Where-Object { $_ }
if ($dirty) { Write-Host "NOTE: uncommitted changes are NOT in the kit:" -ForegroundColor Yellow; $dirty | ForEach-Object { Write-Host "  $_" } }

$out = Join-Path $PSScriptRoot "handoff"
New-Item -ItemType Directory -Force -Path $out | Out-Null
$kit = Join-Path $out "ClaudeUsageMonitor-macOS-kit-$version.zip"
if (Test-Path $kit) { Remove-Item $kit -Force }
& git archive --format=zip --prefix=ClaudeUsageMonitor/ "--add-file=macos/ELOSZOR-EZT-OLVASD-EL.txt" -o $kit HEAD
if ($LASTEXITCODE -ne 0) { throw "git archive failed" }
$commit = (& git rev-parse --short HEAD)
Write-Host ("KIT: {0}  ({1:N0} KB, version {2}, commit {3})" -f $kit, ((Get-Item $kit).Length / 1KB), $version, $commit) -ForegroundColor Cyan
