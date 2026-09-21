CLAUDE USAGE MONITOR - macOS
============================

A small always-on-top panel that shows how much of your Claude subscription's 5-hour and
weekly limits you have used.

INSTALL
-------
1. Drag ClaudeUsageMonitor into your Applications folder.
   IMPORTANT: do not run it from Downloads - from there the app cannot update itself.

2. FIRST START: right-click (or Control-click) the app > Open > Open.
   This is needed because the app is open source but not signed with a paid Apple developer
   certificate. From the second start on a normal double-click is enough.

   If macOS says the app "is damaged" or "cannot be opened", open Terminal and run once:
       xattr -dr com.apple.quarantine /Applications/ClaudeUsageMonitor.app

3. The panel appears at the top right of the screen, plus a small icon in the menu bar.
   There is deliberately no Dock icon.

FIRST USE
---------
- Right-click (two-finger tap) the panel = menu: layout, theme, language, settings.
- To see usage across ALL your devices: menu > Data source > claude.ai (all devices).
  Your browser opens, you sign in as usual, you get a code and paste it in.
  The app NEVER asks for your password. The sign-in token lives in the macOS Keychain.
- Start at login: menu > "Start with the system".

UPDATES
-------
The app checks for new versions by itself and tells you. Menu > "Check for program
updates..." > "Install now" - it downloads, verifies, replaces itself and restarts.
After an update macOS may ask once more whether the app may use its Keychain item:
choose "Always Allow".

UNINSTALL
---------
Quit the app, then drag it from Applications to the Trash.
Settings:     ~/Library/Application Support/ClaudeUsageMonitor   (may be deleted)
Start at login: ~/Library/LaunchAgents/hu.dinorr.claudeusagemonitor.plist   (may be deleted)

Unofficial community tool; not affiliated with Anthropic.
Download, what's new: https://claudeusagemonitor.com/
Source code:          https://github.com/gaborvidovics76/ClaudeUsageMonitor
