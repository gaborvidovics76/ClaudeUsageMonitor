# Claude Usage Monitor – exe készítése
# Használat:  powershell -ExecutionPolicy Bypass -File build.ps1

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

# FONTOS: fordulas elott allitsuk le a futo peldanyokat, kulonben a futo app
# fogva tartja a dist\_internal DLL-jeit -> a torles/ujrairas nem sikerul, es
# HIANYOS (serult) csomag keszul ("Failed to start embedded python interpreter").
Write-Host "[0/3] Futo peldanyok leallitasa..." -ForegroundColor Cyan
Get-Process ClaudeUsageMonitor,QtWebEngineProcess -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2
Remove-Item dist,build -Recurse -Force -ErrorAction SilentlyContinue

Write-Host "[1/3] Ikon generálása..." -ForegroundColor Cyan
python -c "from claude_usage.winutil import write_ico; import PySide6.QtWidgets as w, sys; a=w.QApplication(sys.argv); print(write_ico('app.ico'))"

Write-Host "[2/3] PyInstaller..." -ForegroundColor Cyan
# FONTOS: onedir (nem onefile). Az onefile minden indulasnal ~110 MB-ot csomagol
# ki a TEMP-be; ez a Feladatutemezobol / bejelentkezeskor elakad, es a program
# elindul ugyan folyamatkent, de a kod soha nem fut le. Az onedir azonnal indul.
# A bejelentkezes a RENDSZERBONGESZOBEN tortenik (OAuth), ezert NINCS szukseg
# beagyazott bongeszore. A QtWebEngine-t es a nagy, nem hasznalt modulokat kizarjuk
# -> a csomag ~90 MB (a ~430 MB helyett).
python -m PyInstaller --noconfirm --clean `
    --onedir --windowed `
    --name ClaudeUsageMonitor `
    --icon app.ico `
    --exclude-module PySide6.QtWebEngineCore `
    --exclude-module PySide6.QtWebEngineWidgets `
    --exclude-module PySide6.QtWebEngineQuick `
    --exclude-module PySide6.QtWebChannel `
    --exclude-module PySide6.QtQml `
    --exclude-module PySide6.QtQuick `
    --exclude-module PySide6.QtQuick3D `
    --exclude-module PySide6.QtQuickWidgets `
    --exclude-module PySide6.Qt3DCore `
    --exclude-module PySide6.QtMultimedia `
    --exclude-module PySide6.QtSql `
    --exclude-module PySide6.QtTest `
    --exclude-module PySide6.QtPdf `
    --exclude-module PySide6.QtOpenGL `
    --exclude-module PySide6.QtCharts `
    --exclude-module PySide6.QtDataVisualization `
    --exclude-module tkinter `
    --exclude-module unittest `
    --exclude-module pydoc `
    main.py

Write-Host "[3/3] Csomag ellenorzese..." -ForegroundColor Cyan
# Epsegellenorzes: enelkul egy hianyos build eszrevetlen maradhat.
$need = @(
    "dist\ClaudeUsageMonitor\ClaudeUsageMonitor.exe",
    "dist\ClaudeUsageMonitor\_internal\base_library.zip",
    "dist\ClaudeUsageMonitor\_internal\python312.dll"
)
$missing = $need | Where-Object { -not (Test-Path $_) }
$count = (Get-ChildItem dist\ClaudeUsageMonitor\_internal -Recurse -File | Measure-Object).Count
if ($missing -or $count -lt 100) {
    Write-Host "HIBA: a csomag HIANYOS!" -ForegroundColor Red
    $missing | ForEach-Object { "  hianyzik: $_" }
    "  _internal fajlszam: $count (elvart: 100+)"
    exit 1
}
Write-Host "Kesz - a csomag ep." -ForegroundColor Green
Get-Item dist\ClaudeUsageMonitor\ClaudeUsageMonitor.exe | Select-Object FullName, @{n='MB';e={[math]::Round($_.Length/1MB,1)}}
"Mappa merete: " + [math]::Round(((Get-ChildItem dist\ClaudeUsageMonitor -Recurse | Measure-Object Length -Sum).Sum/1MB),1) + " MB  |  _internal fajlszam: $count"
