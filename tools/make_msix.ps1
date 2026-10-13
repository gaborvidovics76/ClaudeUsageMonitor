<#
.SYNOPSIS
  Builds the MSIX package of Claude Usage Monitor for the Microsoft Store (next to the ZIP release).

.DESCRIPTION
  Takes the PyInstaller build in dist\ClaudeUsageMonitor (the same program as the ZIP), and makes
  release\msix\ClaudeUsageMonitor_<X.Y.Z.0>_x64.msix:

    1. layout:    build\msix\layout\ClaudeUsageMonitor\...  (the program, unchanged)
                  build\msix\layout\Assets\...             (Store / Start images, tools\make_msix_assets.py)
                  build\msix\layout\AppxManifest.xml       (packaging\msix\AppxManifest.xml.in + identity.json)
                  build\msix\layout\resources.pri          (image variants, makepri)
    2. makeappx pack (SHA-256 block map) -> the .msix, then makeappx unpack as a check.
    3. optional (-Sign): signs it with the certificate in release.local.psd1 (SignThumbprint) - only for
       installing the package on your own machine. The Store does NOT need a signed upload: it signs the
       package itself after certification.

  The tools come from tools\signtool\ (tools\get_signtool.ps1 fetches them) or an installed Windows SDK.

      .\tools\make_msix.ps1                 # package the current dist\ build
      .\tools\make_msix.ps1 -Build          # build.ps1 first
      .\tools\make_msix.ps1 -Sign           # + sign for local test installs

  For the Store, packaging\msix\identity.json must hold the values from Partner Center > Product identity.
#>
param(
    [switch]$Build,
    [switch]$Sign,
    [string]$Identity = "",
    [string]$OutDir = ""
)
$ErrorActionPreference = "Stop"
$root = Split-Path $PSScriptRoot -Parent
Set-Location $root
if (-not $Identity) { $Identity = Join-Path $root "packaging\msix\identity.json" }
if (-not $OutDir) { $OutDir = Join-Path $root "release\msix" }
function Info([string]$m) { Write-Host "  $m" -ForegroundColor Green }
function Esc([string]$s) { [Security.SecurityElement]::Escape($s) }

function Find-Tool([string]$name) {
    $local = Join-Path $root "tools\signtool\$name"
    if (Test-Path $local) { return $local }
    $kit = Get-ChildItem "C:\Program Files (x86)\Windows Kits\10\bin\*\x64\$name" -ErrorAction SilentlyContinue |
        Sort-Object FullName -Descending | Select-Object -First 1
    if ($kit) { return $kit.FullName }
    return ""
}
function Run([string]$exe, [string[]]$a) {
    $prev = $ErrorActionPreference; $ErrorActionPreference = "Continue"
    $out = & $exe @a 2>&1
    $code = $LASTEXITCODE; $ErrorActionPreference = $prev
    if ($code -ne 0) { $out | ForEach-Object { Write-Host "    $_" -ForegroundColor DarkGray }; throw "$(Split-Path $exe -Leaf) failed ($code)" }
    return $out
}

Write-Host "== Claude Usage Monitor - MSIX package ==" -ForegroundColor Cyan

# ---------------------------------------------------------------- 0. tools, version, identity
$makeappx = Find-Tool "makeappx.exe"
$makepri = Find-Tool "makepri.exe"
if (-not $makeappx) { throw "makeappx.exe not found - run tools\get_signtool.ps1 (or install the Windows SDK)." }
$src = [IO.File]::ReadAllText((Join-Path $root "claude_usage\__init__.py"))
if ($src -notmatch '__version__\s*=\s*"(\d+)\.(\d+)\.(\d+)"') { throw "no X.Y.Z version in claude_usage\__init__.py" }
$version = "$($Matches[1]).$($Matches[2]).$($Matches[3]).0"           # the Store wants the 4th part = 0
$id = Get-Content $Identity -Raw -Encoding UTF8 | ConvertFrom-Json
foreach ($k in "name", "publisher", "publisher_display_name", "display_name", "description") {
    if (-not $id.$k) { throw "identity.json: '$k' is missing" }
}
if ($id.publisher -notmatch '^CN=') { throw "identity.json: publisher must start with CN= (copy it from Partner Center)" }
$placeholder = $id.publisher -notmatch '^CN=[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}$'
Info "version $version, identity $($id.name) / $($id.publisher)$(if ($placeholder) { '  (placeholder - not the Partner Center identity yet)' })"

# ---------------------------------------------------------------- 1. program
if ($Build) {
    & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $root "build.ps1")
    if ($LASTEXITCODE -ne 0) { throw "build.ps1 failed" }
}
$dist = Join-Path $root "dist\ClaudeUsageMonitor"
if (-not (Test-Path (Join-Path $dist "ClaudeUsageMonitor.exe"))) { throw "dist\ClaudeUsageMonitor\ClaudeUsageMonitor.exe is missing - run build.ps1 (or -Build)." }

$work = Join-Path $root "build\msix"
$layout = Join-Path $work "layout"
if (Test-Path $work) { Remove-Item $work -Recurse -Force }
New-Item -ItemType Directory -Force -Path $layout | Out-Null
& robocopy $dist (Join-Path $layout "ClaudeUsageMonitor") /E /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy failed ($LASTEXITCODE)" }
Info "program copied ($((Get-ChildItem (Join-Path $layout 'ClaudeUsageMonitor') -Recurse -File).Count) files)"

# ---------------------------------------------------------------- 2. images
$assets = Join-Path $layout "Assets"
$env:QT_QPA_PLATFORM = "offscreen"
$prev = $ErrorActionPreference; $ErrorActionPreference = "Continue"
$out = & python (Join-Path $root "tools\make_msix_assets.py") $assets 2>&1
$code = $LASTEXITCODE; $ErrorActionPreference = $prev
if ($code -ne 0) { $out | ForEach-Object { Write-Host "    $_" }; throw "make_msix_assets.py failed" }
Info ($out | Select-Object -Last 1)

# ---------------------------------------------------------------- 3. manifest
$langs = @($id.languages | Where-Object { $_ })
if (-not $langs) { $langs = @("en-US") }
$res = ($langs | ForEach-Object { "    <Resource Language=`"$(Esc $_)`" />" }) -join "`r`n"
$short = if ($id.short_name) { [string]$id.short_name } else { [string]$id.display_name }
$xml = [IO.File]::ReadAllText((Join-Path $root "packaging\msix\AppxManifest.xml.in"), [Text.Encoding]::UTF8)
$xml = $xml.Replace("{{NAME}}", (Esc $id.name)).Replace("{{PUBLISHER}}", (Esc $id.publisher)).Replace("{{VERSION}}", $version)
$xml = $xml.Replace("{{DISPLAY_NAME}}", (Esc $id.display_name)).Replace("{{PUBLISHER_DISPLAY_NAME}}", (Esc $id.publisher_display_name))
$xml = $xml.Replace("{{SHORT_NAME}}", (Esc $short)).Replace("{{DESCRIPTION}}", (Esc $id.description)).Replace("{{RESOURCES}}", $res)
if ($xml -match '\{\{[A-Z_]+\}\}') { throw "manifest still has an unfilled field: $($Matches[0])" }
$manifest = Join-Path $layout "AppxManifest.xml"
[IO.File]::WriteAllText($manifest, $xml, (New-Object Text.UTF8Encoding($false)))
[xml]$null = $xml                                           # well-formed?
Info "AppxManifest.xml ($($langs.Count) languages)"

# ---------------------------------------------------------------- 4. resources.pri (image variants)
if ($makepri) {
    # index ONLY the images (a separate root with the same relative paths), not the program's files
    $priRoot = Join-Path $work "priroot"
    New-Item -ItemType Directory -Force -Path $priRoot | Out-Null
    Copy-Item $assets (Join-Path $priRoot "Assets") -Recurse
    Copy-Item $manifest $priRoot
    $cfg = Join-Path $work "priconfig.xml"
    Run $makepri @("createconfig", "/cf", $cfg, "/dq", "en-US", "/pv", "10.0.0", "/o") | Out-Null
    Run $makepri @("new", "/pr", $priRoot, "/cf", $cfg, "/mn", (Join-Path $priRoot "AppxManifest.xml"), "/of", (Join-Path $layout "resources.pri"), "/o") | Out-Null
    Info "resources.pri"
} else {
    Write-Host "  (makepri.exe not found - packaging without resources.pri; the unqualified images are used)" -ForegroundColor Yellow
}

# ---------------------------------------------------------------- 5. pack + check
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$msix = Join-Path $OutDir "ClaudeUsageMonitor_$($version)_x64.msix"
if (Test-Path $msix) { Remove-Item $msix -Force }
Run $makeappx @("pack", "/o", "/h", "SHA256", "/d", $layout, "/p", $msix) | Out-Null
$check = Join-Path $work "unpacked"
Run $makeappx @("unpack", "/o", "/p", $msix, "/d", $check) | Out-Null
foreach ($f in "AppxManifest.xml", "ClaudeUsageMonitor\ClaudeUsageMonitor.exe", "Assets\StoreLogo.png", "AppxBlockMap.xml") {
    if (-not (Test-Path (Join-Path $check $f))) { throw "unpack check: $f is missing from the package" }
}
$size = (Get-Item $msix).Length
$sha = (Get-FileHash $msix -Algorithm SHA256).Hash.ToLower()
Info ("packed and verified: {0:N1} MB" -f ($size / 1MB))

# ---------------------------------------------------------------- 6. optional: sign for local test installs
if ($Sign) {
    $cfgPath = Join-Path $root "release.local.psd1"
    $tp = if (Test-Path $cfgPath) { [string](Import-PowerShellDataFile $cfgPath).SignThumbprint } else { "" }
    if (-not $tp) { throw "-Sign: no SignThumbprint in release.local.psd1" }
    $cert = Get-ChildItem Cert:\CurrentUser\My | Where-Object Thumbprint -eq ($tp -replace '[^0-9A-Fa-f]', '').ToUpper() | Select-Object -First 1
    if (-not $cert) { throw "-Sign: certificate $tp not in Cert:\CurrentUser\My" }
    if ($cert.Subject -ne $id.publisher) {
        throw "-Sign: the certificate subject '$($cert.Subject)' must equal the manifest Publisher '$($id.publisher)' - otherwise Windows refuses the package"
    }
    & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $root "tools\sign_release.ps1") -Thumbprint $tp -Path $msix
    if ($LASTEXITCODE -ne 0) { throw "signing the package failed" }
}

Write-Host ""
Write-Host "DONE  $msix" -ForegroundColor Cyan
Write-Host "SHA-256: $sha" -ForegroundColor DarkGray
if ($placeholder) {
    Write-Host "NOTE: placeholder identity - fill packaging\msix\identity.json from Partner Center before uploading to the Store." -ForegroundColor Yellow
}
Write-Host "Store upload: Partner Center > your app > Packages - the unsigned .msix is fine, the Store signs it." -ForegroundColor DarkGray
