<#
.SYNOPSIS
  Claude Usage Monitor - uninstaller (current user, no admin rights).
  Started from Settings > Apps > Installed apps, or by Uninstall.bat in the program folder.
.PARAMETER Silent        No questions. Settings are kept unless -RemoveSettings is given.
.PARAMETER RemoveSettings  Also delete %APPDATA%\ClaudeUsageMonitor (settings, sign-in, logs).
#>
param([switch]$Silent, [switch]$RemoveSettings, [string]$InstallDir = "", [switch]$Relaunched)
$ErrorActionPreference = "Continue"
$AppName = "Claude Usage Monitor"
$AppId   = "ClaudeUsageMonitor"
$ExeName = "ClaudeUsageMonitor.exe"

$hu = (Get-UICulture).TwoLetterISOLanguageName -eq "hu"
function T([string]$en, [string]$huText) { if ($hu) { $huText } else { $en } }
function Ask([string]$question, [bool]$default) {
    if ($Silent) { return $default }
    $hint = if ($default) { T "[Y/n]" "[I/n]" } else { T "[y/N]" "[i/N]" }
    $answer = Read-Host "$question $hint"
    if ([string]::IsNullOrWhiteSpace($answer)) { return $default }
    return $answer.Trim().ToLower() -in @("y", "yes", "i", "igen")
}

if (-not $InstallDir) { $InstallDir = $PSScriptRoot }
$InstallDir = [IO.Path]::GetFullPath($InstallDir)

# A folder cannot delete itself while a script runs from it: continue from a temp copy.
if (-not $Relaunched) {
    $copy = Join-Path $env:TEMP ("cum_uninstall_{0}.ps1" -f ([guid]::NewGuid().ToString("N").Substring(0, 8)))
    Copy-Item $MyInvocation.MyCommand.Path $copy -Force
    $argList = @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "`"$copy`"", "-Relaunched", "-InstallDir", "`"$InstallDir`"")
    if ($Silent) { $argList += "-Silent" }
    if ($RemoveSettings) { $argList += "-RemoveSettings" }
    Start-Process powershell.exe -ArgumentList $argList -WorkingDirectory $env:TEMP
    exit 0
}

Set-Location $env:TEMP
Write-Host ""
Write-Host "  $AppName - $(T 'uninstall' 'eltavolitas')" -ForegroundColor White
Write-Host ""
$exe = Join-Path $InstallDir $ExeName
if (-not (Test-Path $exe)) {
    Write-Host (T "The program was not found here: " "A program nem talalhato itt: ") $InstallDir -ForegroundColor Yellow
}
if (-not (Ask (T "Remove $AppName from this computer?" "Eltavolitod a(z) $AppName programot errol a geprol?") $true)) { exit 0 }

Write-Host (T "[1/4] Switching off 'start with Windows'..." "[1/4] Az automatikus indulas kikapcsolasa...") -ForegroundColor Cyan
if (Test-Path $exe) {
    $p = Start-Process -FilePath $exe -ArgumentList "--disable-autostart" -PassThru -WindowStyle Hidden
    if (-not $p.WaitForExit(30000)) { try { $p.Kill() } catch {} }
}
& schtasks.exe /Delete /TN $AppId /F 2>$null | Out-Null
Remove-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name $AppId -ErrorAction SilentlyContinue

Write-Host (T "[2/4] Stopping the program..." "[2/4] A program leallitasa...") -ForegroundColor Cyan
Get-Process -Name $AppId -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2

Write-Host (T "[3/4] Removing shortcuts and the Windows entry..." "[3/4] Parancsikonok es a Windows-bejegyzes torlese...") -ForegroundColor Cyan
Remove-Item (Join-Path $env:APPDATA "Microsoft\Windows\Start Menu\Programs\$AppName.lnk") -Force -ErrorAction SilentlyContinue
Remove-Item (Join-Path ([Environment]::GetFolderPath("Desktop")) "$AppName.lnk") -Force -ErrorAction SilentlyContinue
Remove-Item "HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\$AppId" -Recurse -Force -ErrorAction SilentlyContinue

Write-Host (T "[4/4] Deleting the program folder..." "[4/4] A programmappa torlese...") -ForegroundColor Cyan
# safety: only ever delete a folder that really is this program
if ((Test-Path $exe) -and (Test-Path (Join-Path $InstallDir "_internal")) -and ($InstallDir.Length -gt 10)) {
    Remove-Item -LiteralPath $InstallDir -Recurse -Force -ErrorAction SilentlyContinue
}
foreach ($leftover in @("$InstallDir.old", "$InstallDir.new")) {
    if (Test-Path $leftover) { Remove-Item -LiteralPath $leftover -Recurse -Force -ErrorAction SilentlyContinue }
}

$settings = Join-Path $env:APPDATA $AppId
if (Test-Path $settings) {
    $wipe = $RemoveSettings -or (Ask (T "Also delete your settings and the claude.ai sign-in?" "Toroljem a beallitasaidat es a claude.ai belepest is?") $false)
    if ($wipe) { Remove-Item -LiteralPath $settings -Recurse -Force -ErrorAction SilentlyContinue }
    else { Write-Host ((T "Settings kept in: " "A beallitasok megmaradtak itt: ") + $settings) -ForegroundColor DarkGray }
}

Write-Host ""
Write-Host (T "REMOVED." "ELTAVOLITVA.") -ForegroundColor Green
if (-not $Silent) { Read-Host (T "Press Enter to close this window" "A bezarashoz nyomj Entert") | Out-Null }
Remove-Item -LiteralPath $MyInvocation.MyCommand.Path -Force -ErrorAction SilentlyContinue
