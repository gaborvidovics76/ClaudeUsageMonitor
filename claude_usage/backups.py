"""Backup status.

Reads what a set of backup scripts leaves behind and works out how fresh each backup is:

* **OneDrive**  - step-1 logs (``<prefix>_<date>_<time>.log``) in the log folder,
* **Nextcloud** - step-2 logs (rclone upload) in the same folder,
* **Obsidian**  - vault snapshot ZIPs in the snapshot folder.

Nothing about one particular machine lives in this file. *Where* the backups are
(root folder, sub-folder names, script config, scheduled-task filter, which job writes
where) comes from a per-user profile, ``backup_profile.json`` in the app's config folder
(``%APPDATA%\\ClaudeUsageMonitor``) and from the Backups tab of the settings. Without a
configured root the feature stays hidden. See ``docs/backup_profile.example.json``.

A run only counts as a successful backup if its log ends with the script's own
"... KESZ" line; a run with "HIBAVAL ZARULT", an early exit, or an rclone dry run
does not. Everything here is plain Python that runs on a worker thread - it never
touches Qt, and it returns raw data; the UI formats and translates it.

Nothing is ever written, and no file that OneDrive keeps online-only is opened
(that would download it).
"""

from __future__ import annotations

import glob
import json
import os
import re
import subprocess
import threading
import time
import zipfile
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Tuple

KEYS = ("onedrive", "nextcloud", "obsidian")

PROFILE_FILE = "backup_profile.json"      # per-user, lives next to settings.json

CHECK_INTERVAL_S = 300          # regular re-check of the logs
STATS_TTL_S = 1800              # folder size scans are slower - cache them
TASKS_TTL_S = 900               # PowerShell task query - cache it
RUNNING_GRACE_S = 3 * 3600      # an unfinished log younger than this = "running"
MAX_LOGS_SCANNED = 60           # how far back to look for the last successful run

# OneDrive "Files On-Demand": reading such a file would download it.
_CLOUD_ONLY = 0x1000 | 0x40000 | 0x400000   # OFFLINE | RECALL_ON_OPEN | RECALL_ON_DATA_ACCESS

_PS_LINE = re.compile(r"^(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d) \[(\w+)\s*\] ?(.*)$")
_RC_LINE = re.compile(r"^\d{4}/\d\d/\d\d \d\d:\d\d:\d\d (INFO|NOTICE|ERROR|DEBUG|WARNING)\s*:\s?(.*)$")
_NAME_TS = re.compile(r"(\d{4}-\d\d-\d\d)_(\d\d)(\d\d)")


# --------------------------------------------------------------------------- data


@dataclass
class Component:
    """One thing a run backs up (a robocopy job, an rclone upload branch, ...)."""
    name: str
    status: str = "ok"                  # ok | error | skipped | pending
    code: Optional[int] = None          # robocopy / rclone exit code
    detail: str = ""                    # e.g. "ObsidianVault_...zip (2.8 MB)" or a ZIP count
    source: str = ""
    dest: str = ""
    files: Optional[int] = None         # files in the destination folder
    size: Optional[int] = None          # bytes in the destination folder


@dataclass
class LogRun:
    path: str
    kind: str                           # onedrive | nextcloud
    started: Optional[float] = None     # epoch seconds
    finished: Optional[float] = None
    result: str = "none"                # ok | error | running | interrupted
    dry_run: bool = False
    target: str = ""
    components: List[Component] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    tail: List[str] = field(default_factory=list)
    # nextcloud only
    new: int = 0
    replaced: int = 0
    rclone_errors: int = 0
    groups: List[Tuple[str, int]] = field(default_factory=list)
    files: List[str] = field(default_factory=list)
    storage: Dict[str, str] = field(default_factory=dict)

    @property
    def successful(self) -> bool:
        return self.result == "ok" and not self.dry_run

    @property
    def when(self) -> Optional[float]:
        return self.finished or self.started


@dataclass
class Snapshot:
    path: str
    time: float
    size: int
    count: int = 1                      # snapshots kept
    total_size: int = 0
    cloud_only: bool = False
    files: Optional[int] = None         # entries in the ZIP (None = not listed)
    notes: Optional[int] = None
    uncompressed: Optional[int] = None
    folders: List[Tuple[str, int]] = field(default_factory=list)
    recent: List[Tuple[str, float]] = field(default_factory=list)
    vault: str = ""
    vault_changed: Optional[int] = None
    uploaded_at: Optional[float] = None


@dataclass
class TaskInfo:
    name: str
    state: str
    last_run: Optional[float]
    result: int
    next_run: Optional[float]


@dataclass
class BackupItem:
    key: str
    last_ok: Optional[float] = None     # epoch seconds of the last successful backup
    run: Optional[LogRun] = None        # the most recent run (any result)
    ok_run: Optional[LogRun] = None     # the most recent successful run
    snapshot: Optional[Snapshot] = None
    tasks: List[TaskInfo] = field(default_factory=list)
    problem: str = ""                   # e.g. the vault part of the OneDrive run failed

    @property
    def state(self) -> str:
        """ok | error | running | interrupted | none - the state of the latest attempt."""
        if self.problem:
            return "error"
        if self.run is not None:
            if self.run.result == "ok" and self.run.dry_run:
                return "ok" if self.last_ok else "none"
            return self.run.result
        return "ok" if self.last_ok else "none"


@dataclass
class BackupStatus:
    root: str = ""
    root_found: bool = False
    config_path: str = ""
    config_found: bool = False
    remote: str = ""
    items: Dict[str, BackupItem] = field(default_factory=dict)
    checked_at: float = 0.0
    error: str = ""


def lamp_level(item: Optional[BackupItem], green_h: float, yellow_h: float,
               now: Optional[float] = None) -> str:
    """green (not older than green_h) | yellow (not older than yellow_h) | red | pending."""
    if item is None:
        return "pending"
    if item.last_ok is None:
        return "red"
    age_h = ((now or time.time()) - item.last_ok) / 3600.0
    if age_h <= green_h:
        return "green"
    if age_h <= yellow_h:
        return "yellow"
    return "red"


def thresholds(green, yellow) -> Tuple[float, float]:
    """Sanitised (green, yellow) hours - yellow is never below green."""
    try:
        g = max(1.0, float(green))
    except (TypeError, ValueError):
        g = 24.0
    try:
        y = float(yellow)
    except (TypeError, ValueError):
        y = 48.0
    return g, max(g, y)


# --------------------------------------------------------------------------- paths


@dataclass
class Profile:
    """Machine-specific layout of the backup system - loaded from ``backup_profile.json``.
    Paths may contain environment variables (``%OneDrive%\\...``)."""
    root: str = ""                      # the folder the step-1 script writes into
    script_config: str = ""             # optional .psd1 of the scripts (vault path, remote)
    task_filter: str = ""               # scheduled task name filter, e.g. "Backup*"
    log_dir: str = "logs"               # sub-folder of root with the run logs
    snapshot_dir: str = "snapshots"     # sub-folder of root with the vault ZIPs
    snapshot_glob: str = "*.zip"
    onedrive_log_prefix: str = "onedrive"
    nextcloud_log_prefix: str = "nextcloud"
    vault: str = ""                     # overrides VaultPath of the script config
    remote: str = ""                    # overrides the rclone remote of the script config
    # job name as logged -> {"dest": sub-folder of root, "source": source folder}
    jobs: Dict[str, Dict[str, str]] = field(default_factory=dict)


def profile_path() -> str:
    from .settings import config_dir

    return os.path.join(config_dir(), PROFILE_FILE)


def load_profile(path: Optional[str] = None) -> Profile:
    prof = Profile()
    try:
        with open(path or profile_path(), "r", encoding="utf-8-sig") as fh:
            data = json.load(fh)
    except (OSError, ValueError):
        return prof
    if not isinstance(data, dict):
        return prof
    for key, value in data.items():
        if key == "jobs" and isinstance(value, dict):
            prof.jobs = {str(n): {"dest": str((j or {}).get("dest", "")),
                                  "source": str((j or {}).get("source", ""))}
                         for n, j in value.items() if isinstance(j, dict)}
        elif hasattr(prof, key) and isinstance(value, str):
            setattr(prof, key, value)
    return prof


@dataclass
class Paths:
    root: str
    log_dir: str
    snap_dir: str
    config_path: str
    config_found: bool
    vault: str
    remote: str
    task_filter: str
    profile: Profile

    @property
    def expected(self) -> bool:
        """Should the status bar be shown at all? Only once a backup root is configured
        (profile file or settings) - everybody else never sees the feature."""
        return bool(self.root)


def read_psd1(path: str) -> Dict[str, str]:
    """The simple ``Key = 'value'`` lines of a PowerShell data file."""
    out: Dict[str, str] = {}
    if not path:
        return out
    try:
        with open(path, "r", encoding="utf-8-sig", errors="replace") as fh:
            text = fh.read()
    except OSError:
        return out
    for m in re.finditer(r"^\s*(\w+)\s*=\s*'([^']*)'", text, re.MULTILINE):
        out.setdefault(m.group(1), m.group(2))
    return out


def _expand(path: str) -> str:
    return os.path.normpath(os.path.expandvars(path.strip())) if path and path.strip() else ""


def resolve_paths(root_override: str = "", config_path: str = "", task_filter: str = "",
                  profile: Optional[Profile] = None) -> Paths:
    """Settings win over the profile; nothing is guessed."""
    prof = profile if profile is not None else load_profile()
    root = _expand(root_override) or _expand(prof.root)
    cfg_path = _expand(config_path) or _expand(prof.script_config)
    cfg = read_psd1(cfg_path)
    remote = prof.remote
    if not remote and cfg.get("NextcloudRemote"):
        remote = f"{cfg['NextcloudRemote']}:{cfg.get('NextcloudBasePath', '')}"
    return Paths(
        root=root,
        log_dir=os.path.join(root, prof.log_dir) if root else "",
        snap_dir=os.path.join(root, prof.snapshot_dir) if root else "",
        config_path=cfg_path,
        config_found=bool(cfg),
        vault=_expand(prof.vault) or cfg.get("VaultPath", ""),
        remote=remote,
        task_filter=(task_filter or "").strip() or prof.task_filter,
        profile=prof,
    )


# --------------------------------------------------------------------------- helpers


def _is_cloud_only(path: str) -> bool:
    try:
        return bool(getattr(os.stat(path), "st_file_attributes", 0) & _CLOUD_ONLY)
    except OSError:
        return False


def _ts(text: str) -> Optional[float]:
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(text, fmt).timestamp()
        except ValueError:
            continue
    return None


def _name_time(path: str) -> Optional[float]:
    m = _NAME_TS.search(os.path.basename(path))
    if not m:
        return None
    try:
        return datetime.strptime(f"{m.group(1)} {m.group(2)}:{m.group(3)}", "%Y-%m-%d %H:%M").timestamp()
    except ValueError:
        return None


def _sorted_logs(log_dir: str, prefix: str) -> List[str]:
    files = glob.glob(os.path.join(glob.escape(log_dir), f"{prefix}_*.log"))

    def key(p: str) -> float:
        t = _name_time(p)
        if t is not None:
            return t
        try:
            return os.path.getmtime(p)
        except OSError:
            return 0.0

    return sorted(files, key=key, reverse=True)


def dir_stats(path: str, limit: int = 250_000) -> Tuple[int, int]:
    """(files, bytes) under a folder. Uses only directory metadata, so OneDrive
    online-only files are not downloaded. Junctions/symlinks are not followed."""
    files = size = 0
    stack = [path]
    while stack and files < limit:
        current = stack.pop()
        try:
            with os.scandir(current) as it:
                for entry in it:
                    try:
                        if entry.is_symlink():
                            continue
                        if entry.is_dir(follow_symlinks=False):
                            stack.append(entry.path)
                        elif entry.is_file(follow_symlinks=False):
                            files += 1
                            size += entry.stat(follow_symlinks=False).st_size
                    except OSError:
                        continue
        except OSError:
            continue
    return files, size


# --------------------------------------------------------------------------- log parsing


def parse_log(path: str, kind: str, now: Optional[float] = None) -> LogRun:
    run = LogRun(path=path, kind=kind)
    now = now or time.time()
    if _is_cloud_only(path):
        run.started = _name_time(path)
        run.result = "interrupted"
        return run
    try:
        with open(path, "r", encoding="utf-8-sig", errors="replace") as fh:
            lines = fh.read().splitlines()
    except OSError:
        run.started = _name_time(path)
        run.result = "interrupted"
        return run

    ended = None
    pending: Optional[Component] = None
    files: List[str] = []
    groups: Dict[str, int] = {}

    for raw in lines:
        line = raw.rstrip()
        if "--dry-run" in line:
            run.dry_run = True
        m = _PS_LINE.match(line)
        if m:
            stamp, level, msg = _ts(m.group(1)), m.group(2).upper(), m.group(3)
            body = msg.strip()
            if "INDUL ====" in msg and run.started is None:
                run.started = stamp
            if re.search(r"=+ .* KESZ =+", msg):
                ended, run.finished = "ok", stamp
            elif "HIBAVAL ZARULT" in msg:
                ended, run.finished = "error", stamp
            if level == "ERROR":
                run.errors.append(body)
            elif level == "WARN":
                run.warnings.append(body)

            if kind == "onedrive":
                pending = _onedrive_line(run, body, pending)
            else:
                pending = _nextcloud_line(run, body, pending)
            continue

        r = _RC_LINE.match(line)
        if r and kind == "nextcloud":
            level, msg = r.group(1), r.group(2)
            if msg.endswith(": Copied (new)"):
                run.new += 1
                files.append(msg[: -len(": Copied (new)")])
            elif msg.endswith(": Copied (replaced existing)"):
                run.replaced += 1
                files.append(msg[: -len(": Copied (replaced existing)")])
            elif level == "ERROR":
                run.rclone_errors += 1
                if len(run.errors) < 40:
                    run.errors.append(msg)
            continue

    for f in files:
        parts = f.replace("\\", "/").split("/")
        g = "/".join(parts[:2]) if len(parts) > 2 else (parts[0] if len(parts) > 1 else "/")
        groups[g] = groups.get(g, 0) + 1
    run.groups = sorted(groups.items(), key=lambda kv: -kv[1])
    run.files = files
    run.tail = [ln for ln in lines if _PS_LINE.match(ln)][-18:]

    if run.started is None:
        run.started = _name_time(path)
    if ended:
        run.result = ended
    elif run.errors:
        run.result = "error"               # the script exited early (e.g. no rclone / no remote)
    else:
        try:
            young = now - os.path.getmtime(path) < RUNNING_GRACE_S
        except OSError:
            young = False
        run.result = "running" if young else "interrupted"
    return run


def _onedrive_line(run: LogRun, body: str, pending: Optional[Component]) -> Optional[Component]:
    m = re.match(r"^Cel: (.+)$", body)
    if m:
        run.target = m.group(1)
        return pending
    m = re.match(r"^Masolas: (.+)$", body)
    if m:
        comp = Component(name=m.group(1), status="pending")
        run.components.append(comp)
        return comp
    m = re.match(r"^(.+) - (rendben|HIBA) \(robocopy kod: (\d+)\)$", body)
    if m:
        comp = _find(run, m.group(1))
        comp.status = "ok" if m.group(2) == "rendben" else "error"
        comp.code = int(m.group(3))
        return None
    m = re.match(r"^Kihagyva \(nincs ilyen mappa\): (.+)$", body)
    if m:
        comp = _find(run, m.group(1))
        comp.status = "skipped"
        return None
    m = re.match(r"^Vault pillanatkep kesz: (\S+) \((.+)\)$", body)
    if m:
        comp = Component(name="@vault", status="ok", detail=f"{m.group(1)} ({m.group(2)})")
        run.components.insert(0, comp)
        return None
    if body.startswith("HIBA a vault mentesenel") or body.startswith("Nem talalhato a vault"):
        run.components.insert(0, Component(name="@vault", status="error", detail=body))
        return None
    m = re.match(r"^Cowork naplok rendben \((\d+)", body)
    if m:
        run.components.append(Component(name="@cowork", status="ok", detail=m.group(1)))
        return None
    if body.startswith("HIBA a ZIP-elesnel"):
        run.components.append(Component(name="@cowork", status="error", detail=body))
    return pending


def _nextcloud_line(run: LogRun, body: str, pending: Optional[Component]) -> Optional[Component]:
    m = re.match(r"^Feltoltes: (.+)$", body)
    if m:
        comp = Component(name=m.group(1), status="pending")
        run.components.append(comp)
        return comp
    m = re.match(r"^(\S.*?)\s+->\s+(\S.*)$", body)
    if m and pending is not None and not pending.source:
        pending.source, pending.dest = m.group(1), m.group(2)
        if not run.target:
            run.target = m.group(2)
        return pending
    m = re.match(r"^(.+) HIBA \(rclone kod: (\d+)\)$", body)
    if m:
        comp = _find(run, m.group(1))
        comp.status, comp.code = "error", int(m.group(2))
        return None
    m = re.match(r"^(.+) kesz$", body)
    if m:
        comp = _find(run, m.group(1))
        comp.status = "ok"
        return None
    m = re.match(r"^(Total|Used|Free|Trashed|Other|Objects):\s+(.+)$", body)
    if m:
        run.storage[m.group(1)] = m.group(2).strip()
    return pending


def _find(run: LogRun, name: str) -> Component:
    for comp in reversed(run.components):
        if comp.name == name:
            return comp
    comp = Component(name=name)
    run.components.append(comp)
    return comp


def scan_logs(log_dir: str, kind: str, now: Optional[float] = None,
              prefix: str = "") -> Tuple[Optional[LogRun], Optional[LogRun]]:
    """(latest run, latest successful run)."""
    logs = _sorted_logs(log_dir, prefix or kind)
    latest = ok = None
    for i, path in enumerate(logs[:MAX_LOGS_SCANNED]):
        run = parse_log(path, kind, now)
        if i == 0:
            latest = run
        if run.successful:
            ok = run
            break
    return latest, ok


# --------------------------------------------------------------------------- snapshots


def scan_snapshots(snap_dir: str, vault: str, want_listing: bool,
                   pattern: str = "*.zip") -> Optional[Snapshot]:
    zips = glob.glob(os.path.join(glob.escape(snap_dir), pattern or "*.zip")) if snap_dir else []
    if not zips:
        return None
    entries = []
    for path in zips:
        try:
            st = os.stat(path)
        except OSError:
            continue
        entries.append((_name_time(path) or st.st_mtime, path, st.st_size))
    if not entries:
        return None
    entries.sort(reverse=True)
    t, path, size = entries[0]
    snap = Snapshot(path=path, time=t, size=size, count=len(entries),
                    total_size=sum(e[2] for e in entries), vault=vault)
    snap.cloud_only = _is_cloud_only(path)

    if want_listing and not snap.cloud_only:
        try:
            with zipfile.ZipFile(path) as z:
                infos = z.infolist()
            files = notes = unc = 0
            folders: Dict[str, int] = {}
            recent: List[Tuple[float, str]] = []
            for info in infos:
                name = info.filename.replace("\\", "/")
                if name.endswith("/"):
                    continue
                files += 1
                unc += info.file_size
                top = name.split("/", 1)[0] if "/" in name else "/"
                folders[top] = folders.get(top, 0) + 1
                if name.lower().endswith(".md"):
                    notes += 1
                    try:
                        recent.append((datetime(*info.date_time).timestamp(), name))
                    except (ValueError, OverflowError):
                        pass
            recent.sort(reverse=True)
            snap.files, snap.notes, snap.uncompressed = files, notes, unc
            snap.folders = sorted(folders.items(), key=lambda kv: -kv[1])
            snap.recent = [(n, ts) for ts, n in recent[:10]]
        except (OSError, zipfile.BadZipFile, RuntimeError):
            pass

    if vault and os.path.isdir(vault):
        changed = 0
        for dirpath, dirnames, filenames in os.walk(vault):
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            for fn in filenames:
                if fn.lower().endswith(".md"):
                    try:
                        if os.stat(os.path.join(dirpath, fn)).st_mtime > t + 60:
                            changed += 1
                    except OSError:
                        pass
        snap.vault_changed = changed
    return snap


# --------------------------------------------------------------------------- scheduled tasks

_PS_TASKS = r"""
$ErrorActionPreference = 'SilentlyContinue'
try { [Console]::OutputEncoding = [Text.Encoding]::UTF8 } catch {}
$r = @(Get-ScheduledTask -TaskName '__FILTER__' | ForEach-Object {
    $i = $_ | Get-ScheduledTaskInfo
    [pscustomobject]@{
        n = $_.TaskName
        s = [string]$_.State
        l = $(if ($i.LastRunTime) { $i.LastRunTime.ToString('s') } else { '' })
        r = [int64]$i.LastTaskResult
        x = $(if ($i.NextRunTime) { $i.NextRunTime.ToString('s') } else { '' })
    }
})
ConvertTo-Json -InputObject $r -Compress
"""


def query_tasks(name_filter: str) -> List[TaskInfo]:
    flt = re.sub(r"[^\w \-*?.()áéíóöőúüűÁÉÍÓÖŐÚÜŰ]", "", name_filter or "").strip()
    if not flt:
        return []
    script = _PS_TASKS.replace("__FILTER__", flt.replace("'", "''"))
    try:
        proc = subprocess.run(
            ["powershell.exe", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
             "-Command", script],
            capture_output=True, stdin=subprocess.DEVNULL, timeout=40,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000),
        )
        text = proc.stdout.decode("utf-8", errors="replace").strip()
        data = json.loads(text) if text else []
    except (OSError, subprocess.SubprocessError, ValueError):
        return []
    if isinstance(data, dict):
        data = [data]
    out: List[TaskInfo] = []
    for d in data if isinstance(data, list) else []:
        def when(v):
            t = _ts(str(v or ""))
            return t if (t is not None and datetime.fromtimestamp(t).year >= 2000) else None
        try:
            result = int(d.get("r") or 0) & 0xFFFFFFFF
        except (TypeError, ValueError):
            result = 0
        out.append(TaskInfo(name=str(d.get("n", "")), state=str(d.get("s", "")),
                            last_run=when(d.get("l")), result=result, next_run=when(d.get("x"))))
    return sorted(out, key=lambda t: t.name)


# --------------------------------------------------------------------------- collector


def collect(paths: Paths, want_listing: bool = True, want_stats: bool = True,
            tasks: Optional[List[TaskInfo]] = None, stats_cache: Optional[dict] = None,
            now: Optional[float] = None) -> BackupStatus:
    now = now or time.time()
    st = BackupStatus(root=paths.root, root_found=bool(paths.root) and os.path.isdir(paths.root),
                      config_path=paths.config_path, config_found=paths.config_found,
                      remote=paths.remote, checked_at=now)
    items = {k: BackupItem(key=k) for k in KEYS}
    st.items = items
    if not st.root_found:
        return st

    prof = paths.profile
    od_run, od_ok = scan_logs(paths.log_dir, "onedrive", now, prof.onedrive_log_prefix)
    nc_run, nc_ok = scan_logs(paths.log_dir, "nextcloud", now, prof.nextcloud_log_prefix)

    # where each logged job writes to comes from the profile, never from this file
    for run in (od_run, od_ok):
        for comp in (run.components if run is not None else []):
            if comp.name == "@vault":
                comp.dest = comp.dest or prof.snapshot_dir
            job = prof.jobs.get(comp.name)
            if job:
                comp.dest = comp.dest or job.get("dest", "")
                comp.source = comp.source or job.get("source", "")

    od = items["onedrive"]
    od.run, od.ok_run = od_run, od_ok
    od.last_ok = od_ok.when if od_ok else None

    nc = items["nextcloud"]
    nc.run, nc.ok_run = nc_run, nc_ok
    nc.last_ok = nc_ok.when if nc_ok else None

    # destination folder sizes for the OneDrive components (cached - slow on big trees)
    if want_stats and od_run is not None:
        cache = stats_cache if stats_cache is not None else {}
        for comp in od_run.components:
            if not comp.dest:
                continue
            folder = os.path.join(paths.root, comp.dest)
            hit = cache.get(folder)
            if hit and now - hit[0] < STATS_TTL_S:
                comp.files, comp.size = hit[1], hit[2]
            elif os.path.isdir(folder):
                files, size = dir_stats(folder)
                cache[folder] = (now, files, size)
                comp.files, comp.size = files, size

    ob = items["obsidian"]
    snap = scan_snapshots(paths.snap_dir, paths.vault, want_listing, prof.snapshot_glob)
    ob.snapshot = snap
    if snap is not None:
        ob.last_ok = snap.time
        if nc_ok is not None and nc_ok.started is not None and nc_ok.started >= snap.time - 60:
            snap.uploaded_at = nc_ok.when
    if od_run is not None:
        vault_parts = [c for c in od_run.components if c.name == "@vault"]
        if vault_parts and vault_parts[0].status == "error":
            ob.problem = vault_parts[0].detail or "vault"

    for task in tasks or []:
        low = task.name.lower()
        if "nextcloud" in low:
            nc.tasks.append(task)
        elif "onedrive" in low:
            od.tasks.append(task)
            ob.tasks.append(task)
        else:
            for it in items.values():
                it.tasks.append(task)
    return st


class BackupChecker:
    """Runs :func:`collect` on a worker thread. The Qt side polls :attr:`status`
    and :attr:`version` from its own timer."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._status: Optional[BackupStatus] = None
        self._thread: Optional[threading.Thread] = None
        self._last_start = 0.0
        self._stats_cache: dict = {}
        self._tasks: Tuple[float, List[TaskInfo]] = (0.0, [])
        self.version = 0
        self.root_override = ""
        self.config_path = ""
        self.task_filter = ""
        self.want_tasks = True
        self.want_listing = True
        self.enabled = True

    def configure(self, *, enabled: bool, root_override: str, config_path: str,
                  task_filter: str, want_tasks: bool, want_listing: bool) -> None:
        changed = (root_override, config_path, task_filter) != \
                  (self.root_override, self.config_path, self.task_filter)
        turned_on = enabled and not self.enabled
        self.enabled = enabled
        self.root_override, self.config_path = root_override or "", config_path or ""
        self.task_filter = task_filter or ""
        self.want_tasks, self.want_listing = want_tasks, want_listing
        if changed:
            self._tasks = (0.0, [])
        if changed or turned_on:
            self._last_start = 0.0

    def paths(self) -> Paths:
        return resolve_paths(self.root_override, self.config_path, self.task_filter)

    @property
    def status(self) -> Optional[BackupStatus]:
        with self._lock:
            return self._status

    @property
    def busy(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

    def check(self, force: bool = False) -> bool:
        """Start a background check if due (or forced). True if one was started."""
        if not self.enabled or self.busy:
            return False
        if not force and time.time() - self._last_start < CHECK_INTERVAL_S:
            return False
        self._last_start = time.time()
        self._thread = threading.Thread(target=self._run, args=(force,), daemon=True,
                                        name="backup-check")
        self._thread.start()
        return True

    def _run(self, force: bool) -> None:
        try:
            if force:
                self._stats_cache.clear()
            paths = self.paths()
            tasks: List[TaskInfo] = []
            if self.want_tasks:
                ts, cached = self._tasks
                if force or time.time() - ts > TASKS_TTL_S:
                    cached = query_tasks(paths.task_filter)
                    self._tasks = (time.time(), cached)
                tasks = cached
            status = collect(paths, want_listing=self.want_listing, tasks=tasks,
                             stats_cache=self._stats_cache)
        except Exception as exc:  # never let the worker die silently
            status = BackupStatus(error=f"{type(exc).__name__}: {exc}", checked_at=time.time())
        with self._lock:
            self._status = status
            self.version += 1
