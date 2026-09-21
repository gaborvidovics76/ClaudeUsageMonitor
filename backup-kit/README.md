# Claude Backup Kit – free

Everything you built with Claude – your skills, `CLAUDE.md` rules, project memory, MCP settings, agent
conversation logs and your Obsidian notes – usually lives on **one disk**. One broken drive, one stolen laptop,
one wrong delete, and it is gone. This kit makes a daily backup in **two independent places**, and
**Claude Usage Monitor shows you on its panel whether the backups are fresh.**

Free, open source (MIT), for Windows 10/11. No account with us, no data to us.

> **Disclaimer – please read.** We accept **no liability** for backups, lost data or any damage. Claude Usage Monitor
> only reads and shows the backup logs; it does not make, check or guarantee a backup. This kit is a free
> **starting point offered as help**, not a finished product: you can – and may – change the scripts for your own
> computer, so the quality and completeness of a backup cannot be guaranteed. **Making sure your backups are
> complete and can be restored is your own responsibility** – check the lamps, read the log and test a restore
> from time to time. Provided "as is" under the MIT licence, without any warranty. By using the kit you accept the
> Terms of use: https://dinorr.hu/claude-usage-monitor/#terms

## What you get

| | Step 1 – OneDrive | Step 2 – second cloud |
|---|---|---|
| Claude Code (`%USERPROFILE%\.claude`): skills, settings, `CLAUDE.md`, project memory, plugins | ✔ | ✔ |
| Claude Desktop (`%APPDATA%\Claude`): settings, MCP servers | ✔ | ✔ |
| Agent (Cowork) conversation logs – one ZIP per session | ✔ | ✔ |
| Obsidian vault – a dated ZIP snapshot every run (optional) | ✔ | ✔ |
| Any extra folders you list in `config.psd1` | ✔ | ✔ |

**Never backed up:** the Claude Code sign-in token (`.credentials.json`), browser cookies of Claude Desktop,
caches and the large re-downloadable VM images.

**Step 2** copies the whole backup folder to Nextcloud – or to any other cloud rclone supports (Google Drive,
Dropbox, S3, pCloud, SFTP …). OneDrive and a second, independent provider: if one fails or locks you out,
you still have the other.

## What the monitor shows

With the backup status bar on, the panel gets three lamps: **OneDrive · Nextcloud · Obsidian**, each with the
age of the last *successful* backup.

- 🟢 green – not older than 24 h · 🟡 yellow – up to 48 h · 🔴 red – older, or no backup (hours are adjustable)
- a red ring around a lamp – the latest run failed or did not finish, even if the lamp is still green
- click a lamp for details: what is backed up (source, destination, files, size), the vault snapshot and its
  most recently edited notes, what was uploaded, the remote storage, errors, the scheduled tasks and the log

Only a run whose log ends with the script's own "… KESZ" line counts as successful – a failed, interrupted or
test run does not.

## Install – 10 minutes

**You need:** Windows 10/11, OneDrive signed in, [Claude Usage Monitor](https://dinorr.hu/claude-usage-monitor/)
installed. For step 2: a Nextcloud account (or another cloud rclone supports).

1. **Nextcloud app password** (only for step 2). In your browser: Nextcloud → your avatar → *Personal settings*
   → *Security* → *Devices & sessions* → app name `rclone-backup` → *Create new app password*. Copy it – you see
   it only once. It is **not** your account password, and you can revoke it any time.
2. **Unpack** this kit to a permanent folder, e.g. `C:\Tools\ClaudeBackup`.
3. **Edit `config.psd1`** in Notepad: what to back up (`VaultPath` for Obsidian, `ExtraFolders`), the second cloud
   (`NextcloudRemote`, `NextcloudBasePath` – leave `NextcloudRemote` empty to skip step 2) and the time (`DailyTime`).
4. **Run the installer as administrator.** Win+X → *Terminal (Admin)*:
   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
   cd C:\Tools\ClaudeBackup
   Unblock-File *.ps1
   .\Install-BackupKit.ps1
   ```
   It installs rclone if needed, asks for the Nextcloud address, user name and app password (typed hidden),
   registers the two scheduled tasks, writes the monitor's profile and makes a first run.
5. **First real upload:** `.\Backup-Step2-Cloud.ps1` (the installer's step 2 was only a test run).
6. **Check:** `.\Test-BackupKit.ps1` – every line should be `[OK]`. On the panel the three lamps appear within
   5 minutes (or right-click the panel → *Backups…* → *Check now*).

## Settings in Claude Usage Monitor (Settings → Backups)

| Setting | What it does |
|---|---|
| Show backup status bar on the panel | switches the three lamps on or off |
| Lamps | which of OneDrive / Nextcloud / Obsidian to show (no Obsidian? untick it) |
| Label next to the lamp | name and age · name only · lamps only |
| Green up to / Yellow up to | the age limits in hours (default 24 / 48) |
| Backup folder | the folder step 1 writes into – empty = taken from the profile the installer wrote |
| Backup script config | this kit's `config.psd1` – from here the monitor reads the vault path and the cloud target |
| Scheduled task filter | e.g. `ClaudeBackup*` – which scheduled tasks to list in the details window |
| Details window shows | what is backed up · contents · errors and warnings · scheduled tasks · log |

The profile the installer writes is `%APPDATA%\ClaudeUsageMonitor\backup_profile.json` – paths only,
no password, no token. Values set on the settings tab take priority over the profile (the file itself is not changed).

## Already have your own backup script?

The monitor does not need this kit – it needs the logs. Make your script write

- one log file per run into `<backup folder>\logs`, named `onedrive_YYYY-MM-DD_HHMMSS.log` (step 1) and
  `nextcloud_YYYY-MM-DD_HHMMSS.log` (step 2),
- every line as `yyyy-MM-dd HH:mm:ss [LEVEL] message`,
- a last line containing `KESZ` for success, or `HIBAVAL ZARULT` for failure (all the other words the monitor
  understands are listed at the top of `Common.ps1`).

Different names or folders? Put them into `%APPDATA%\ClaudeUsageMonitor\backup_profile.json` (every key is optional):

```json
{
  "root": "%OneDrive%\\MyBackup",
  "log_dir": "logs",
  "snapshot_dir": "vault-snapshots",
  "snapshot_glob": "Vault_*.zip",
  "onedrive_log_prefix": "onedrive",
  "nextcloud_log_prefix": "nextcloud",
  "vault": "%USERPROFILE%\\Documents\\Obsidian Vault",
  "remote": "nextcloud:Backups/MyPC",
  "task_filter": "MyBackup*"
}
```

No password, no token belongs in this file – the monitor never needs one.

## Security – how it is built

- **No password anywhere in the kit.** The app password is typed hidden and stored only in rclone's own
  config (`%APPDATA%\rclone\rclone.conf`), obscured. Revoke it in Nextcloud whenever you like.
- **The Claude Code sign-in token is never copied.** Nor are Claude Desktop's cookies.
- **No mirroring.** Step 1 uses `robocopy /E /XO`, step 2 `rclone copy` – a file you delete on the PC stays in
  both backups. (Mirroring would faithfully copy a mistake.)
- **The vault goes into dated ZIPs**, so a later bad copy cannot overwrite an older state (kept 30 days).
- **Note:** `claude_desktop_config.json` and `.claude\settings.json` can contain API keys of MCP servers or
  environment variables. They are backed up (you need them to restore), into your own OneDrive and your own
  cloud – keep those accounts protected with two-factor sign-in.
- The two steps are chained: step 2 starts when step 1 has finished, never in the middle of it. For this the
  installer switches on Windows' Task Scheduler history.

## Restore

| Lost | From where |
|---|---|
| An older version of a note | onedrive.com → right-click the file → *Version history* |
| A deleted file | onedrive.com → *Recycle bin* (30 days), or Nextcloud → *Deleted files* |
| The whole vault from a given day | `ClaudeBackup\vault-snapshots\Vault_YYYY-MM-DD_HHMM.zip` – unpack into an **empty** folder, open it with Obsidian → *Open folder as vault* |
| Claude Code skills / settings | copy `ClaudeBackup\files\claude-code\*` back to `%USERPROFILE%\.claude\`, then sign in to Claude Code again |
| Claude Desktop settings | close Claude Desktop, copy `ClaudeBackup\files\claude-desktop\*` back to `%APPDATA%\Claude\` |

## Files

| File | Role |
|---|---|
| `config.psd1` | all settings |
| `Install-BackupKit.ps1` | one-time setup (as administrator) |
| `Backup-Step1-OneDrive.ps1` | step 1 – run daily by the task *ClaudeBackup 1 - OneDrive* |
| `Backup-Step2-Cloud.ps1` | step 2 – run right after it by *ClaudeBackup 2 - Nextcloud* (`-DryRun` = test) |
| `Set-CloudRemote.ps1` | (re)creates the Nextcloud connection |
| `Test-BackupKit.ps1` | health check |
| `Common.ps1` | shared functions and the log format the monitor reads – please do not change the log words |

Logs: `<OneDrive>\ClaudeBackup\logs\onedrive_*.log` and `nextcloud_*.log` (kept 90 days).

Remove: `Unregister-ScheduledTask 'ClaudeBackup*'` and delete this folder. Your backups stay where they are.

---
Made by Vidovics Gábor · part of Claude Usage Monitor · MIT licence · no warranty – check your backups
(that is exactly what the lamps are for).
