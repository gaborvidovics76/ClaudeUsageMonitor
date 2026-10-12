<#
.SYNOPSIS
  Makes the hand-over package of the native macOS (Xcode / Mac App Store) app.

.DESCRIPTION
  Zips the COMMITTED macos/Xcode tree (git archive of HEAD) plus the project-level files a Mac
  needs (CLAUDE.md, LICENSE, README.md, the Xcode CI workflow) into
  handoff\ClaudeUsageMonitor-macOS-Xcode-kit-<version>.zip, with the read-me at the root.
  Going through git guarantees LF line endings and that nothing local can slip in.
  Commit first - uncommitted changes are not part of the kit.

.EXAMPLE
  .\make_xcode_kit.ps1
#>
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
$pbx = [IO.File]::ReadAllText((Join-Path $PSScriptRoot "macos\Xcode\ClaudeUsageMonitor.xcodeproj\project.pbxproj"))
$version = [regex]::Match($pbx, 'MARKETING_VERSION\s*=\s*([0-9.]+);').Groups[1].Value
if (-not $version) { throw "MARKETING_VERSION not found" }
$dirty = (& git status --porcelain --untracked-files=no -- macos/Xcode) | Where-Object { $_ }
if ($dirty) { Write-Host "NOTE: uncommitted changes are NOT in the kit:" -ForegroundColor Yellow; $dirty | ForEach-Object { Write-Host "  $_" } }

$out = Join-Path $PSScriptRoot "handoff"
New-Item -ItemType Directory -Force -Path $out | Out-Null
$kit = Join-Path $out "ClaudeUsageMonitor-macOS-Xcode-kit-$version.zip"
if (Test-Path $kit) { Remove-Item $kit -Force }
& git archive --format=zip --prefix=ClaudeUsageMonitor/ "--add-file=macos/Xcode/ELOSZOR-EZT-OLVASD-EL.txt" -o $kit HEAD `
    macos/Xcode .github/workflows/xcode-build.yml CLAUDE.md LICENSE README.md
if ($LASTEXITCODE -ne 0) { throw "git archive failed" }
$commit = (& git rev-parse --short HEAD)
Write-Host ("KIT: {0}  ({1:N0} KB, version {2}, commit {3})" -f $kit, ((Get-Item $kit).Length / 1KB), $version, $commit) -ForegroundColor Cyan
