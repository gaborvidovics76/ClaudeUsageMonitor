<#
.SYNOPSIS
  Puts Microsoft's signtool.exe into tools\signtool\ without installing the whole Windows SDK.

.DESCRIPTION
  Downloads the official "Microsoft.Windows.SDK.BuildTools" package from NuGet (a signed Microsoft package,
  ~100 MB), extracts the x64 signtool and the libraries next to it, and checks that it runs.
  tools\sign_release.ps1 finds it there automatically. Run once; re-run to update.

      .\tools\get_signtool.ps1
#>
param([string]$Version = "")      # "" = latest
$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$dest = Join-Path $PSScriptRoot "signtool"
$tmp = Join-Path $env:TEMP ("sdk-buildtools-" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Force -Path $tmp | Out-Null
$url = if ($Version) { "https://www.nuget.org/api/v2/package/Microsoft.Windows.SDK.BuildTools/$Version" } else { "https://www.nuget.org/api/v2/package/Microsoft.Windows.SDK.BuildTools" }
$pkg = Join-Path $tmp "buildtools.zip"
Write-Host "downloading $url ..."
Invoke-WebRequest -Uri $url -OutFile $pkg -UseBasicParsing
Add-Type -AssemblyName System.IO.Compression.FileSystem
[IO.Compression.ZipFile]::ExtractToDirectory($pkg, (Join-Path $tmp "x"))
$x64 = Get-ChildItem (Join-Path $tmp "x\bin\*\x64") -Directory | Sort-Object FullName -Descending | Select-Object -First 1
if (-not $x64) { throw "no bin\<version>\x64 folder in the package" }
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Get-ChildItem $x64.FullName -File | Where-Object {
    $_.Name -ieq "signtool.exe" -or $_.Name -imatch '^(Microsoft\.Windows\.Build\.(Signing|Appx)|mssign32|wintrust|appxsip|appxpackaging|opcservices|makecat|certmgr)' -or $_.Name -imatch '\.(manifest)$'
} | Copy-Item -Destination $dest -Force
Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue
$exe = Join-Path $dest "signtool.exe"
if (-not (Test-Path $exe)) { throw "signtool.exe was not extracted" }
$prev = $ErrorActionPreference; $ErrorActionPreference = "Continue"
$first = (& $exe 2>&1 | Select-Object -First 1); $ErrorActionPreference = $prev
Write-Host "ready: $exe"
Write-Host "  $first"
Write-Host "  (tools\signtool\ is git-ignored - every machine fetches its own copy)"
