@{
    # =====================================================================
    #  Claude Backup Kit - settings. Everything is in this one file.
    #  Paths may use environment variables: %USERPROFILE%, %APPDATA% ...
    #  NO password or token belongs here. The cloud password lives only in
    #  rclone's own config file (%APPDATA%\rclone\rclone.conf), obscured.
    #
    #  DISCLAIMER: a free starting point, AS IS, without warranty (MIT).
    #  NO LIABILITY for backups, lost data or any damage. You may change
    #  anything here - making sure your backups are complete and can be
    #  restored is your own responsibility. Test a restore now and then.
    # =====================================================================

    # ---- STEP 1: the backup folder (inside your OneDrive) ----------------
    # The backup lands in  <your OneDrive>\<OneDriveSubFolder>  and OneDrive
    # takes it to the cloud. Folder names below are read by Claude Usage
    # Monitor too - the installer writes them into its profile for you.
    OneDriveSubFolder   = 'ClaudeBackup'
    LogFolder           = 'logs'
    SnapshotFolder      = 'vault-snapshots'
    FileFolder          = 'files'

    # ---- What to back up --------------------------------------------------
    # Claude Code: skills, settings, CLAUDE.md, project memory, plugins.
    # The sign-in token (.credentials.json) is ALWAYS left out.
    BackupClaudeCode    = $true
    # Claude Desktop: settings and MCP server configuration.
    # Caches, cookies and the large re-downloadable VM images are left out.
    # NOTE: claude_desktop_config.json can contain API keys of MCP servers.
    BackupClaudeDesktop = $true
    # Conversation logs of Claude agent (Cowork) sessions, one ZIP per session.
    BackupCoworkLogs    = $true

    # Obsidian vault (optional): a dated ZIP snapshot every run.
    # Leave empty if you do not use Obsidian.   Example: 'C:\Users\you\Documents\MyVault'
    VaultPath           = ''
    KeepSnapshotDays    = 30          # older vault ZIPs are deleted from the backup folder

    # Any other folders. Name = how it appears in the log and in the monitor.
    ExtraFolders        = @(
        # @{ Name = 'Documents'; Path = '%USERPROFILE%\Documents' }
        # @{ Name = 'Projects';  Path = 'D:\Projects' }
    )
    MaxFileMB           = 2048        # larger single files are skipped

    # ---- STEP 2: a second copy in another cloud (rclone) ----------------
    # Name of the rclone remote. The installer creates one for Nextcloud;
    # any rclone target works (Google Drive, Dropbox, S3, pCloud, SFTP...).
    # Leave empty to switch step 2 off.
    NextcloudRemote     = 'nextcloud'
    NextcloudBasePath   = 'Backups/ClaudePC'
    NextcloudTransfers  = 4           # parallel transfers: 2 for big files, 4-8 for many small ones
    BandwidthLimit      = '0'         # e.g. '8M' = 8 MB/s ; '0' = unlimited

    # ---- Schedule (used by the installer) -----------------------------------
    DailyTime           = '20:00'     # step 1 runs daily at this time; step 2 starts right after it
    TaskPrefix          = 'ClaudeBackup'
}
