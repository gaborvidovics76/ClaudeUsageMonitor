@echo off
rem Claude Usage Monitor - installer launcher (double click). No admin rights needed.
title Claude Usage Monitor - Install / Telepites
if not exist "%~dp0installer\Install.ps1" (
  echo.
  echo  The installer files are missing. Unzip the WHOLE zip first, then run this file
  echo  from the unzipped folder.
  echo.
  echo  A telepito fajljai hianyoznak. Elobb csomagold ki a TELJES zip fajlt, es a
  echo  kicsomagolt mappabol inditsd ezt a fajlt.
  echo.
  pause
  exit /b 1
)
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0installer\Install.ps1" %*
