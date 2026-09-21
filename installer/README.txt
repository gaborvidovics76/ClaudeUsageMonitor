CLAUDE USAGE MONITOR - INSTALLATION
===================================

A small always-on-top panel for Windows 10/11 that shows how much of your Claude
subscription's 5-hour and weekly limits you have used.

INSTALL - 3 STEPS
-----------------
1. Unzip the WHOLE zip file into a folder
   (right-click the zip > "Extract All...").
   IMPORTANT: do not run it from inside the zip - extract it first!

2. In the extracted folder, double-click:   INSTALL.bat

3. You get two questions (Enter = the recommended answer):
   - create a desktop shortcut?
   - start together with Windows?
   The program then starts by itself. NO administrator rights are needed.

IF WINDOWS WARNS YOU
--------------------
"Windows protected your PC" (blue window): click "More info", then "Run anyway".
The program is open source but has no purchased code-signing certificate, which is
why Windows asks on the first run.

FIRST USE
---------
- The panel appears at the top right of the screen; drag it anywhere.
- Right-click the panel = menu (layout, theme, size, language, settings).
- By default it reads the log of Claude Desktop on this PC - no sign-in needed.
- To see usage across ALL your devices (browser, phone, another PC):
    right-click > Data source > claude.ai (all devices)
  Your browser opens, you sign in as usual, you get a code and paste it in.
  The program NEVER asks for or sees your password.
- The tray icon may first land behind the ^ arrow near the clock. Drag it onto the
  taskbar to keep it visible.

UPDATES
-------
The program checks for newer versions by itself and tells you. Right-click >
"Check for program updates..." > "Install now" - it downloads, verifies, replaces itself and
restarts. Your settings stay. (Switch off in Settings > System.)

UNINSTALL
---------
Settings > Apps > Installed apps > Claude Usage Monitor > Uninstall.
It asks whether to delete your settings too.

WHERE THINGS GO
---------------
Program:   %LOCALAPPDATA%\Programs\ClaudeUsageMonitor
Settings:  %APPDATA%\ClaudeUsageMonitor
(Type either into the File Explorer address bar.)

PRIVACY
-------
No telemetry, no ads, no third parties. The program only talks to Anthropic's own
server (for YOUR usage numbers) and reads a version number from the update server.
The sign-in token is stored encrypted on your PC, bound to your Windows account.

Unofficial community tool; not affiliated with Anthropic.
Download, docs, what's new:  https://claudeusagemonitor.com/
Source code:                 https://github.com/gaborvidovics76/ClaudeUsageMonitor
