"""Online update.

The release server publishes a small ``manifest.json`` (version, download URL, SHA-256,
notes). The app compares it with its own version, and on request downloads the package,
verifies the checksum, unpacks the new program folder next to the installed one and hands
over to a tiny helper script that swaps the folders once this process has exited, then
starts the new version. If anything fails the old folder is put back.

Privacy: the check is a plain HTTPS GET of a static JSON file. Nothing about the user or
the machine is sent (the User-Agent carries only the app version). It can be switched off.

Safety rules enforced here:
* HTTPS only, and the download must come from the same host as the manifest,
* the SHA-256 from the manifest must match the downloaded file,
* ZIP entries are only extracted below the staging folder (no path traversal),
* self-update only runs for the packaged exe in a folder the user can write to.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Tuple

from . import __version__

IS_MAC = sys.platform == "darwin"
# every platform has its own manifest, so the Windows and the macOS releases never touch each other
DEFAULT_MANIFEST_URL = ("https://dinorr.hu/claude-usage-monitor/macos/manifest.json" if IS_MAC
                        else "https://dinorr.hu/claude-usage-monitor/manifest.json")
EXE_NAME = "ClaudeUsageMonitor.exe"
APP_DIR_IN_ZIP = ("app/ClaudeUsageMonitor/", "ClaudeUsageMonitor/")   # accepted package layouts
MAX_PACKAGE_BYTES = 600 * 1024 * 1024
CHECK_EVERY_S = 6 * 3600


class UpdateError(Exception):
    pass


@dataclass
class UpdateInfo:
    version: str
    url: str
    sha256: str
    size: int = 0
    released: str = ""
    page: str = ""
    arch: str = ""                      # macOS builds: arm64 | x86_64 ("" = any)
    notes: Dict[str, List[str]] = field(default_factory=dict)   # language code -> lines

    def notes_for(self, lang: str) -> List[str]:
        return self.notes.get(lang) or self.notes.get("en") or next(iter(self.notes.values()), [])


# --------------------------------------------------------------------------- versions


def parse_version(text: str) -> Tuple[int, ...]:
    nums = re.findall(r"\d+", str(text or ""))
    return tuple(int(n) for n in nums[:4]) or (0,)


def is_newer(candidate: str, current: str) -> bool:
    a, b = parse_version(candidate), parse_version(current)
    n = max(len(a), len(b))
    return a + (0,) * (n - len(a)) > b + (0,) * (n - len(b))


# --------------------------------------------------------------------------- network


def _is_local_test(url: str) -> bool:
    host = urllib.parse.urlparse(url).hostname or ""
    return host in ("127.0.0.1", "localhost")


def _check_url(url: str) -> None:
    parts = urllib.parse.urlparse(url)
    if parts.scheme == "https" and parts.hostname:
        return
    if parts.scheme == "http" and _is_local_test(url):
        return
    raise UpdateError(f"insecure or invalid URL: {url}")


def _open(url: str, timeout: float):
    _check_url(url)
    req = urllib.request.Request(url, headers={
        "User-Agent": f"ClaudeUsageMonitor/{__version__}",
        "Accept": "application/json, application/zip, */*",
        "Cache-Control": "no-cache",
    })
    return urllib.request.urlopen(req, timeout=timeout)


def fetch_manifest(url: str = "", timeout: float = 12.0) -> UpdateInfo:
    url = (url or "").strip() or DEFAULT_MANIFEST_URL
    try:
        with _open(url, timeout) as r:
            data = json.loads(r.read(512 * 1024).decode("utf-8-sig", "replace"))
    except UpdateError:
        raise
    except urllib.error.HTTPError as e:
        raise UpdateError(f"HTTP {e.code}") from e
    except (urllib.error.URLError, OSError) as e:
        raise UpdateError(str(getattr(e, "reason", e))) from e
    except ValueError as e:
        raise UpdateError("invalid manifest") from e
    if not isinstance(data, dict):
        raise UpdateError("invalid manifest")

    version = str(data.get("version", "")).strip()
    dl = str(data.get("download_url", "")).strip()
    sha = str(data.get("sha256", "")).strip().lower()
    if not re.fullmatch(r"\d+(\.\d+){1,3}", version):
        raise UpdateError("manifest: bad version")
    if not re.fullmatch(r"[0-9a-f]{64}", sha):
        raise UpdateError("manifest: bad sha256")
    _check_url(dl)
    if urllib.parse.urlparse(dl).hostname != urllib.parse.urlparse(url).hostname:
        raise UpdateError("manifest: download host differs from the manifest host")

    notes: Dict[str, List[str]] = {}
    raw_notes = data.get("notes")
    if isinstance(raw_notes, dict):
        for lang, lines in raw_notes.items():
            if isinstance(lines, list):
                notes[str(lang)] = [str(x) for x in lines][:40]
    elif isinstance(raw_notes, list):
        notes["en"] = [str(x) for x in raw_notes][:40]

    try:
        size = int(data.get("bytes") or 0)
    except (TypeError, ValueError):
        size = 0
    return UpdateInfo(version=version, url=dl, sha256=sha, size=size,
                      released=str(data.get("last_updated", "")),
                      page=str(data.get("homepage", "")), arch=str(data.get("arch", "")), notes=notes)


def arch_ok(info: UpdateInfo) -> bool:
    """An Intel build also runs on Apple Silicon (Rosetta); an arm64 build does not run on Intel."""
    if not info.arch:
        return True
    import platform

    machine = platform.machine().lower()
    return info.arch.lower() in (machine, "x86_64", "universal2") if machine == "arm64" \
        else info.arch.lower() in (machine, "universal2")


def download(info: UpdateInfo, dest: str,
             progress: Optional[Callable[[int, int], None]] = None,
             cancelled: Optional[Callable[[], bool]] = None) -> str:
    """Downloads to `dest`, verifies the SHA-256. Returns `dest`."""
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    tmp = dest + ".part"
    digest = hashlib.sha256()
    done = 0
    try:
        with _open(info.url, 30.0) as r, open(tmp, "wb") as fh:
            total = int(r.headers.get("Content-Length") or info.size or 0)
            if total > MAX_PACKAGE_BYTES:
                raise UpdateError("package too large")
            while True:
                if cancelled and cancelled():
                    raise UpdateError("cancelled")
                chunk = r.read(256 * 1024)
                if not chunk:
                    break
                done += len(chunk)
                if done > MAX_PACKAGE_BYTES:
                    raise UpdateError("package too large")
                digest.update(chunk)
                fh.write(chunk)
                if progress:
                    progress(done, total)
    except UpdateError:
        _silent_remove(tmp)
        raise
    except (urllib.error.URLError, OSError) as e:
        _silent_remove(tmp)
        raise UpdateError(str(getattr(e, "reason", e))) from e
    if digest.hexdigest().lower() != info.sha256:
        _silent_remove(tmp)
        raise UpdateError("checksum mismatch")
    os.replace(tmp, dest)
    return dest


def _silent_remove(path: str) -> None:
    try:
        os.remove(path)
    except OSError:
        pass


# --------------------------------------------------------------------------- install


def install_dir() -> Optional[str]:
    """Folder of the packaged exe (None when running from source)."""
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return None


def can_self_update() -> Tuple[bool, str]:
    folder = install_dir()
    if not folder:
        return False, "source"
    parent = os.path.dirname(folder)
    for where in (folder, parent):
        probe = os.path.join(where, f".cum_write_test_{os.getpid()}")
        try:
            with open(probe, "w") as fh:
                fh.write("x")
            os.remove(probe)
        except OSError:
            return False, "readonly"
    return True, ""


def stage(zip_path: str, target: str) -> str:
    """Unpacks the program folder of the package into `target` (must not exist yet)."""
    if os.path.exists(target):
        shutil.rmtree(target, ignore_errors=True)
    os.makedirs(target)
    root = os.path.realpath(target)
    count = 0
    with zipfile.ZipFile(zip_path) as z:
        names = [i.filename.replace("\\", "/") for i in z.infolist()]
        prefix = next((p for p in APP_DIR_IN_ZIP if any(n.startswith(p) for n in names)), None)
        if prefix is None:
            raise UpdateError("package layout not recognised")
        for info in z.infolist():
            name = info.filename.replace("\\", "/")
            if not name.startswith(prefix) or name.endswith("/"):
                continue
            rel = name[len(prefix):]
            out = os.path.realpath(os.path.join(root, *rel.split("/")))
            if not (out == root or out.startswith(root + os.sep)):
                raise UpdateError("unsafe path in package")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with z.open(info) as src, open(out, "wb") as dst:
                shutil.copyfileobj(src, dst, 1024 * 1024)
            count += 1
    if not os.path.isfile(os.path.join(target, EXE_NAME)) or \
            not os.path.isdir(os.path.join(target, "_internal")) or count < 50:
        raise UpdateError("package is incomplete")
    return target


_SWAP_PS1 = r'''
param([int]$ProcId, [string]$Install, [string]$New, [string]$Exe, [string]$Log)
$ErrorActionPreference = 'Stop'
function W($m) { try { Add-Content -Path $Log -Value ("{0}  {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $m) -Encoding UTF8 } catch {} }
Set-Location $env:TEMP
W "update: waiting for process $ProcId"
for ($i = 0; $i -lt 80; $i++) {
    if (-not (Get-Process -Id $ProcId -ErrorAction SilentlyContinue)) { break }
    Start-Sleep -Milliseconds 250
}
Get-Process -Id $ProcId -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
# started from the command line while the panel is running: stop that copy too
Get-Process -ErrorAction SilentlyContinue |
    Where-Object { $_.Path -and $_.Path.StartsWith($Install + '\', [StringComparison]::OrdinalIgnoreCase) } |
    Stop-Process -Force -ErrorAction SilentlyContinue
Start-Sleep -Milliseconds 400
$old = "$Install.old"
try {
    if (Test-Path -LiteralPath $old) { Remove-Item -LiteralPath $old -Recurse -Force }
    $moved = $false
    for ($i = 0; $i -lt 20 -and -not $moved; $i++) {
        try { Rename-Item -LiteralPath $Install -NewName (Split-Path $old -Leaf); $moved = $true }
        catch { Start-Sleep -Milliseconds 500 }
    }
    if (-not $moved) { throw "the program folder is still in use" }
    try {
        Rename-Item -LiteralPath $New -NewName (Split-Path $Install -Leaf)
    } catch {
        Rename-Item -LiteralPath $old -NewName (Split-Path $Install -Leaf)
        throw
    }
    W "update: folder swapped"
} catch {
    W ("update FAILED, old version kept: " + $_.Exception.Message)
}
$target = Join-Path $Install $Exe
if (Test-Path -LiteralPath $target) { Start-Process -FilePath $target -WorkingDirectory $Install }
Start-Sleep -Seconds 3
if (Test-Path -LiteralPath $old) { Remove-Item -LiteralPath $old -Recurse -Force -ErrorAction SilentlyContinue }
if (Test-Path -LiteralPath $New) { Remove-Item -LiteralPath $New -Recurse -Force -ErrorAction SilentlyContinue }
W "update: done"
Remove-Item -LiteralPath $MyInvocation.MyCommand.Path -Force -ErrorAction SilentlyContinue
'''


def launch_swap(new_dir: str, log_path: str) -> None:
    """Starts the detached helper that swaps the folders after this process exits."""
    folder = install_dir()
    if not folder:
        raise UpdateError("not a packaged build")
    fd, script = tempfile.mkstemp(prefix="cum_update_", suffix=".ps1")
    with os.fdopen(fd, "w", encoding="utf-8-sig") as fh:
        fh.write(_SWAP_PS1)
    args = ["powershell.exe", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
            "-WindowStyle", "Hidden", "-File", script,
            "-ProcId", str(os.getpid()), "-Install", folder, "-New", new_dir,
            "-Exe", EXE_NAME, "-Log", log_path]
    # NOT DETACHED_PROCESS: powershell.exe does not start without a console (that silently
    # broke the swap in 2.3.0/2.3.1). CREATE_NO_WINDOW gives it a hidden one.
    # CREATE_BREAKAWAY_FROM_JOB keeps the helper alive if we run inside a job object
    # (Task Scheduler); where that is not permitted we start it without.
    no_window, new_group, breakaway = 0x08000000, 0x00000200, 0x01000000
    proc = None
    for flags in (no_window | new_group | breakaway, no_window | new_group):
        try:
            proc = subprocess.Popen(args, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                                    stderr=subprocess.DEVNULL, creationflags=flags,
                                    close_fds=True, cwd=tempfile.gettempdir())
            break
        except OSError:
            continue
    if proc is None:
        raise UpdateError("could not start the update helper")
    time.sleep(1.2)
    if proc.poll() is not None:        # it must still be waiting for us to exit
        raise UpdateError(f"the update helper stopped at once (code {proc.returncode})")
    log(f"helper started (pid {proc.pid})")


if IS_MAC:
    # macOS: the unit that gets replaced is the .app bundle; unpacking and the swap differ
    from . import updater_mac as _mac

    install_dir = _mac.install_dir          # noqa: F811
    can_self_update = _mac.can_self_update  # noqa: F811

    def stage(zip_path: str, target: str) -> str:    # noqa: F811
        try:
            return _mac.stage(zip_path, target)
        except _mac.MacUpdateError as e:
            raise UpdateError(str(e)) from e

    def launch_swap(new_dir: str, log_path: str) -> None:    # noqa: F811
        try:
            pid = _mac.launch_swap(new_dir, log_path)
        except _mac.MacUpdateError as e:
            raise UpdateError(str(e)) from e
        log(f"helper started (pid {pid})")


def update_log_path() -> str:
    from .settings import config_dir

    return os.path.join(config_dir(), "update.log")


def log(message: str) -> None:
    try:
        with open(update_log_path(), "a", encoding="utf-8") as fh:
            fh.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}  {message}\n")
    except OSError:
        pass


# --------------------------------------------------------------------------- controller


class Updater:
    """Thread-based; the Qt side polls `state` / `version_counter` from its timer.

    state: idle | checking | uptodate | available | error | downloading | ready | failed
    """

    def __init__(self, manifest_url: str = "") -> None:
        self.manifest_url = manifest_url or ""
        self._lock = threading.Lock()
        self._thread: Optional[threading.Thread] = None
        self.state = "idle"
        self.info: Optional[UpdateInfo] = None
        self.error = ""
        self.progress = (0, 0)
        self.staged_dir = ""
        self.last_check = 0.0
        self.counter = 0
        self._cancel = False

    # -- helpers
    def _set(self, **kw) -> None:
        with self._lock:
            for k, v in kw.items():
                setattr(self, k, v)
            self.counter += 1

    @property
    def busy(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

    def due(self) -> bool:
        return time.time() - self.last_check > CHECK_EVERY_S

    # -- check
    def check(self) -> bool:
        if self.busy:
            return False
        self.last_check = time.time()
        self._set(state="checking", error="")
        self._thread = threading.Thread(target=self._check, daemon=True, name="update-check")
        self._thread.start()
        return True

    def _check(self) -> None:
        try:
            info = fetch_manifest(self.manifest_url)
            if is_newer(info.version, __version__) and not arch_ok(info):
                self._set(state="uptodate", info=info)
                log(f"check: {info.version} is for {info.arch}, not for this machine")
            elif is_newer(info.version, __version__):
                self._set(state="available", info=info)
                log(f"check: {info.version} available (installed {__version__})")
            else:
                self._set(state="uptodate", info=info)
        except UpdateError as e:
            self._set(state="error", error=str(e))
            log(f"check failed: {e}")
        except Exception as e:  # noqa: BLE001 - the worker must never die silently
            self._set(state="error", error=f"{type(e).__name__}: {e}")

    # -- download + stage
    def start_install(self) -> bool:
        if self.busy or self.info is None:
            return False
        ok, why = can_self_update()
        if not ok:
            self._set(state="failed", error=why)
            return False
        self._cancel = False
        self._set(state="downloading", progress=(0, self.info.size), error="")
        self._thread = threading.Thread(target=self._install, daemon=True, name="update-install")
        self._thread.start()
        return True

    def cancel(self) -> None:
        self._cancel = True

    def _install(self) -> None:
        info = self.info
        folder = install_dir()
        try:
            from .settings import config_dir

            cache = os.path.join(config_dir(), "updates")
            zip_path = os.path.join(cache, f"ClaudeUsageMonitor-{info.version}.zip")

            def on_progress(done: int, total: int) -> None:
                with self._lock:
                    self.progress = (done, total)
                    self.counter += 1

            download(info, zip_path, on_progress, lambda: self._cancel)
            new_dir = folder + ".new"
            stage(zip_path, new_dir)
            _silent_remove(zip_path)
            self._set(state="ready", staged_dir=new_dir)
            log(f"staged {info.version} -> {new_dir}")
        except UpdateError as e:
            self._set(state="failed", error=str(e))
            log(f"install failed: {e}")
        except Exception as e:  # noqa: BLE001
            self._set(state="failed", error=f"{type(e).__name__}: {e}")
            log(f"install failed: {type(e).__name__}: {e}")

    def apply_and_restart(self) -> None:
        """Call once state == 'ready'; the caller must quit the application right after."""
        launch_swap(self.staged_dir, update_log_path())


def run_cli_update(manifest_url: str = "", apply: bool = False) -> int:
    """`--check-update` / `--update-now`: no UI, result goes to update.log. Exit code:
    0 = up to date / updated, 10 = update available (check only), 1 = error."""
    try:
        info = fetch_manifest(manifest_url)
    except UpdateError as e:
        log(f"cli: check failed: {e}")
        return 1
    if not is_newer(info.version, __version__):
        log(f"cli: up to date ({__version__}, server {info.version})")
        return 0
    if not apply:
        log(f"cli: {info.version} available (installed {__version__})")
        return 10
    up = Updater(manifest_url)
    up.info = info
    if not up.start_install():
        log(f"cli: cannot self-update: {up.error}")
        return 1
    while up.busy:
        time.sleep(0.2)
    if up.state != "ready":
        return 1
    try:
        up.apply_and_restart()
    except UpdateError as e:
        log(f"cli: {e}")
        return 1
    return 0
