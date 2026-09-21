<#
.SYNOPSIS
  Claude Usage Monitor - installer. No admin rights needed; installs for the current user.

.DESCRIPTION
  Started by TELEPITES.bat / INSTALL.bat (double click). It:
    1. checks Windows and the package,
    2. stops a running copy,
    3. copies the program to %LOCALAPPDATA%\Programs\ClaudeUsageMonitor,
    4. creates the Start menu (and optionally desktop) shortcut,
    5. registers "start with Windows" (optional) and the entry in Installed apps,
    6. starts the program.
  Settings and the claude.ai sign-in live in %APPDATA%\ClaudeUsageMonitor and are never touched,
  so installing over an older version is an upgrade.

.PARAMETER Silent        No questions, no "press a key" (defaults: autostart yes, desktop shortcut no).
.PARAMETER TargetDir     Install somewhere else.
.PARAMETER NoAutostart   Do not register "start with Windows".
.PARAMETER DesktopShortcut  Create a desktop shortcut without asking.
.PARAMETER NoLaunch      Do not start the program at the end.
.PARAMETER LogPath       Also write the progress to this file.
#>
param(
    [switch]$Silent,
    [string]$TargetDir = "",
    [switch]$NoAutostart,
    [switch]$DesktopShortcut,
    [switch]$NoLaunch,
    [string]$LogPath = ""
)
$ErrorActionPreference = "Stop"
$AppName   = "Claude Usage Monitor"
$AppId     = "ClaudeUsageMonitor"
$ExeName   = "ClaudeUsageMonitor.exe"
$Publisher = "Vidovics Gabor"
$HomePage  = "https://claudeusagemonitor.com/"

$hu = (Get-UICulture).TwoLetterISOLanguageName -eq "hu"
function T([string]$en, [string]$huText) { if ($hu) { $huText } else { $en } }
function Say([string]$text, [string]$color = "Gray") {
    Write-Host $text -ForegroundColor $color
    if ($LogPath) { try { Add-Content -Path $LogPath -Value ("{0}  {1}" -f (Get-Date -Format "HH:mm:ss"), $text) -Encoding UTF8 } catch {} }
}
function Step([int]$n, [string]$text) { Say ("[{0}/6] {1}" -f $n, $text) "Cyan" }
function Ask([string]$question, [bool]$default) {
    if ($Silent) { return $default }
    $hint = if ($default) { T "[Y/n]" "[I/n]" } else { T "[y/N]" "[i/N]" }
    $answer = Read-Host "$question $hint"
    if ([string]::IsNullOrWhiteSpace($answer)) { return $default }
    return $answer.Trim().ToLower() -in @("y", "yes", "i", "igen")
}
function Finish([int]$code) {
    if (-not $Silent) { Write-Host ""; Read-Host (T "Press Enter to close this window" "A bezarashoz nyomj Entert") | Out-Null }
    exit $code
}
function New-Shortcut([string]$path, [string]$target, [string]$workDir) {
    $shell = New-Object -ComObject WScript.Shell
    $link = $shell.CreateShortcut($path)
    $link.TargetPath = $target
    $link.WorkingDirectory = $workDir
    $link.IconLocation = "$target,0"
    $link.Description = $AppName
    $link.Save()
}

try {
    $version = "?"
    $versionFile = Join-Path $PSScriptRoot "..\VERSION"
    if (Test-Path $versionFile) { $version = (Get-Content $versionFile -TotalCount 1).Trim() }

    Write-Host ""
    Say ("  {0}  {1}" -f $AppName, $version) "White"
    Say ("  " + (T "Installer - no administrator rights needed." "Telepito - rendszergazdai jog nem kell.")) "DarkGray"
    Write-Host ""

    # ---------------------------------------------------------------- 1
    Step 1 (T "Checking Windows and the package..." "A Windows es a csomag ellenorzese...")
    $os = [Environment]::OSVersion.Version
    if ($os.Major -lt 10) { throw (T "Windows 10 or 11 is required." "Windows 10 vagy 11 szukseges.") }
    if (-not [Environment]::Is64BitOperatingSystem) { throw (T "A 64-bit Windows is required." "64 bites Windows szukseges.") }
    $source = Join-Path $PSScriptRoot "..\app\$AppId"
    if (-not (Test-Path $source)) { $source = Join-Path $PSScriptRoot "..\$AppId" }
    $source = (Resolve-Path $source -ErrorAction SilentlyContinue).Path
    $broken = T "The package is incomplete. Unzip the WHOLE zip file first, then run the installer from the unzipped folder." `
                "A csomag hianyos. Elobb csomagold ki a TELJES zip fajlt, es a kicsomagolt mappabol inditsd a telepitot."
    if (-not $source) { throw $broken }
    foreach ($need in @($ExeName, "_internal\base_library.zip")) {
        if (-not (Test-Path (Join-Path $source $need))) { throw $broken }
    }
    if ((Get-ChildItem (Join-Path $source "_internal") -Recurse -File | Measure-Object).Count -lt 100) { throw $broken }
    Say ("      OK - Windows {0}.{1}, build {2}" -f $os.Major, $os.Minor, $os.Build) "Green"

    if (-not $TargetDir) { $TargetDir = Join-Path $env:LOCALAPPDATA "Programs\$AppId" }
    $TargetDir = [IO.Path]::GetFullPath($TargetDir)
    $upgrade = Test-Path (Join-Path $TargetDir $ExeName)
    if ($upgrade) { Say ("      " + (T "An installed copy was found - it will be upgraded, your settings stay." "Talaltam telepitett peldanyt - frissitem, a beallitasaid megmaradnak.")) "Yellow" }

    # ---------------------------------------------------------------- 2
    Step 2 (T "Stopping a running copy..." "Futo peldany leallitasa...")
    $running = @(Get-Process -Name $AppId -ErrorAction SilentlyContinue)
    if ($running.Count -gt 0) {
        $running | Stop-Process -Force -ErrorAction SilentlyContinue
        Start-Sleep -Seconds 2
        Say ("      " + (T "stopped" "leallitva")) "Green"
    } else { Say ("      " + (T "none was running" "nem futott")) "Green" }

    # ---------------------------------------------------------------- 3
    Step 3 ((T "Copying the program to" "A program masolasa ide:") + " $TargetDir")
    New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null
    # leftovers of an interrupted self-update
    foreach ($leftover in @("$TargetDir.new", "$TargetDir.old")) {
        if (Test-Path -LiteralPath $leftover) { Remove-Item -LiteralPath $leftover -Recurse -Force -ErrorAction SilentlyContinue }
    }
    & robocopy $source $TargetDir /MIR /R:2 /W:1 /NFL /NDL /NJH /NJS /NP | Out-Null
    if ($LASTEXITCODE -ge 8) { throw ((T "Copy failed (robocopy code" "A masolas nem sikerult (robocopy kod") + " $LASTEXITCODE).") }
    foreach ($extra in @("Uninstall.ps1")) {
        Copy-Item (Join-Path $PSScriptRoot $extra) (Join-Path $TargetDir $extra) -Force
    }
    Set-Content -Path (Join-Path $TargetDir "Uninstall.bat") -Encoding ASCII -Value @(
        "@echo off",
        "powershell -NoProfile -ExecutionPolicy Bypass -File ""%~dp0Uninstall.ps1""")
    if (Test-Path $versionFile) { Copy-Item $versionFile (Join-Path $TargetDir "VERSION") -Force }
    # files from the internet carry a "blocked" mark - remove it so Windows does not nag
    Get-ChildItem $TargetDir -Recurse -File | Unblock-File -ErrorAction SilentlyContinue
    $exe = Join-Path $TargetDir $ExeName
    if (-not (Test-Path $exe)) { throw (T "The program file is missing after the copy." "A masolas utan hianyzik a programfajl.") }
    $sizeMB = [math]::Round(((Get-ChildItem $TargetDir -Recurse -File | Measure-Object Length -Sum).Sum / 1MB), 0)
    Say ("      OK - $sizeMB MB") "Green"

    # ---------------------------------------------------------------- 4
    Step 4 (T "Creating shortcuts..." "Parancsikonok letrehozasa...")
    $startMenu = Join-Path $env:APPDATA "Microsoft\Windows\Start Menu\Programs\$AppName.lnk"
    New-Shortcut $startMenu $exe $TargetDir
    Say ("      " + (T "Start menu: done" "Start menu: kesz")) "Green"
    $wantDesktop = $DesktopShortcut -or (Ask (T "      Create a desktop shortcut too?" "      Keszuljon parancsikon az Asztalra is?") $false)
    if ($wantDesktop) {
        New-Shortcut (Join-Path ([Environment]::GetFolderPath("Desktop")) "$AppName.lnk") $exe $TargetDir
        Say ("      " + (T "Desktop: done" "Asztal: kesz")) "Green"
    }

    # ---------------------------------------------------------------- 5
    Step 5 (T "Registering with Windows..." "Bejegyzes a Windowsba...")
    $key = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\$AppId"
    New-Item -Path $key -Force | Out-Null
    $uninstall = "powershell.exe -NoProfile -ExecutionPolicy Bypass -File `"$(Join-Path $TargetDir 'Uninstall.ps1')`""
    Set-ItemProperty $key -Name DisplayName     -Value $AppName
    Set-ItemProperty $key -Name DisplayVersion  -Value $version
    Set-ItemProperty $key -Name Publisher       -Value $Publisher
    Set-ItemProperty $key -Name URLInfoAbout    -Value $HomePage
    Set-ItemProperty $key -Name InstallLocation -Value $TargetDir
    Set-ItemProperty $key -Name DisplayIcon     -Value $exe
    Set-ItemProperty $key -Name UninstallString -Value $uninstall
    Set-ItemProperty $key -Name QuietUninstallString -Value "$uninstall -Silent"
    Set-ItemProperty $key -Name EstimatedSize   -Value ([int]($sizeMB * 1024)) -Type DWord
    Set-ItemProperty $key -Name NoModify        -Value 1 -Type DWord
    Set-ItemProperty $key -Name NoRepair        -Value 1 -Type DWord
    Say ("      " + (T "Listed under Settings > Apps > Installed apps" "Megjelenik itt: Gephaz > Alkalmazasok > Telepitett alkalmazasok")) "Green"

    $wantAutostart = (-not $NoAutostart) -and (Ask (T "      Start automatically with Windows?" "      Induljon el automatikusan a Windowszal?") $true)
    if ($wantAutostart) {
        $p = Start-Process -FilePath $exe -ArgumentList "--enable-autostart" -PassThru -WindowStyle Hidden
        if (-not $p.WaitForExit(30000)) { try { $p.Kill() } catch {} }
        if ($p.ExitCode -eq 0) { Say ("      " + (T "Start with Windows: on" "Indulas a Windowszal: bekapcsolva")) "Green" }
        else { Say ("      " + (T "Could not register autostart - you can switch it on later from the app's menu." "Az automatikus indulast nem sikerult beallitani - kesobb a program menujebol bekapcsolhato.")) "Yellow" }
    }

    # ---------------------------------------------------------------- 6
    if ($NoLaunch) {
        Step 6 (T "Done (the program was not started)." "Kesz (a programot nem inditottam el).")
    } else {
        Step 6 (T "Starting the program..." "A program inditasa...")
        Start-Process -FilePath $exe -WorkingDirectory $TargetDir
        Start-Sleep -Seconds 3
        if (Get-Process -Name $AppId -ErrorAction SilentlyContinue) { Say ("      " + (T "running" "fut")) "Green" }
    }

    Write-Host ""
    Say (T "INSTALLED SUCCESSFULLY." "A TELEPITES SIKERULT.") "Green"
    Write-Host ""
    Say (T "What now:" "Mi a teendo most:") "White"
    Say (T "  - The panel appears at the top right of the screen; drag it anywhere." `
           "  - A panel a kepernyo jobb felso sarkaban jelenik meg; barhova athuzhato.")
    Say (T "  - Right-click it for the menu: layout, theme, language, settings." `
           "  - Jobb gombbal kattintva jon a menu: elrendezes, tema, nyelv, beallitasok.")
    Say (T "  - For usage across ALL your devices: right-click > Data source > claude.ai, then sign in in your browser." `
           "  - Hogy MINDEN eszkozod hasznalatat lassad: jobb gomb > Adatforras > claude.ai, majd lepj be a bongeszodben.")
    Say (T "  - The tray icon may hide behind the ^ arrow near the clock - drag it out to keep it visible." `
           "  - A talcaikon az ora melletti ^ nyil moge kerulhet - huzd ki onnan, ha mindig latni szeretned.")
    Say (T "  - Updates arrive by themselves: the app tells you when a new version is out." `
           "  - A frissitesek maguktol jonnek: a program szol, ha uj verzio jelent meg.")
    Say (T "  - To remove: Settings > Apps > Installed apps > Claude Usage Monitor." `
           "  - Eltavolitas: Gephaz > Alkalmazasok > Telepitett alkalmazasok > Claude Usage Monitor.")
    Finish 0
}
catch {
    Write-Host ""
    Say ((T "INSTALLATION FAILED: " "A TELEPITES NEM SIKERULT: ") + $_.Exception.Message) "Red"
    Say (T "Nothing else was changed. Help: " "Mas nem valtozott. Segitseg: ") "Gray"
    Say "  $HomePage" "Gray"
    Finish 1
}
