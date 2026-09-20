"""macOS half of the self-update: the unit that gets replaced is the whole .app bundle.

A bundle contains symlinks and executable bits that Python's zipfile does not restore, so
unpacking is done with the system's own `ditto` (the same tool that created the package).
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile
from typing import Optional, Tuple

APP_NAME = "ClaudeUsageMonitor.app"
BINARY = os.path.join("Contents", "MacOS", "ClaudeUsageMonitor")


class MacUpdateError(Exception):
    pass


def install_dir() -> Optional[str]:
    """…/ClaudeUsageMonitor.app when running from a bundle (None when running from source)."""
    exe = os.path.abspath(sys.executable)
    marker = ".app" + os.sep + "Contents" + os.sep + "MacOS" + os.sep
    if getattr(sys, "frozen", False) and marker in exe:
        return exe[: exe.index(marker) + len(".app")]
    return None


def can_self_update() -> Tuple[bool, str]:
    bundle = install_dir()
    if not bundle:
        return False, "source"
    # "App Translocation": a quarantined app started from Downloads runs from a random
    # read-only path - it has to be moved to /Applications first.
    if "/AppTranslocation/" in bundle:
        return False, "readonly"
    parent = os.path.dirname(bundle)
    probe = os.path.join(parent, f".um_write_test_{os.getpid()}")
    try:
        with open(probe, "w") as fh:
            fh.write("x")
        os.remove(probe)
    except OSError:
        return False, "readonly"
    return True, ""


def stage(zip_path: str, target: str) -> str:
    """Unpacks ClaudeUsageMonitor.app from the package into `target` (…/ClaudeUsageMonitor.app.new)."""
    with zipfile.ZipFile(zip_path) as z:
        for name in z.namelist():
            clean = name.replace("\\", "/")
            if clean.startswith("/") or ".." in clean.split("/"):
                raise MacUpdateError("unsafe path in package")
    if os.path.exists(target):
        shutil.rmtree(target, ignore_errors=True)
    work = tempfile.mkdtemp(prefix=".um_unpack_", dir=os.path.dirname(target))   # same volume -> cheap move
    try:
        res = subprocess.run(["/usr/bin/ditto", "-x", "-k", zip_path, work],
                             capture_output=True, text=True, timeout=600)
        if res.returncode != 0:
            raise MacUpdateError("ditto: " + (res.stderr or "").strip()[:200])
        found = None
        for root, dirs, _files in os.walk(work):
            if APP_NAME in dirs:
                found = os.path.join(root, APP_NAME)
                break
            if root.count(os.sep) - work.count(os.sep) >= 2:
                dirs[:] = []
        if not found or not os.path.isfile(os.path.join(found, BINARY)):
            raise MacUpdateError("package is incomplete")
        os.rename(found, target)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    return target


_SWAP_SH = r'''#!/bin/sh
PID="$1"; APP="$2"; NEW="$3"; LOG="$4"
log() { echo "$(date '+%Y-%m-%d %H:%M:%S')  $1" >> "$LOG"; }
cd /tmp
log "update: waiting for process $PID"
i=0
while kill -0 "$PID" 2>/dev/null && [ "$i" -lt 80 ]; do sleep 0.25; i=$((i+1)); done
kill -9 "$PID" 2>/dev/null
pkill -f "$APP/Contents/MacOS/" 2>/dev/null
sleep 0.5
OLD="$APP.old"
rm -rf "$OLD"
if mv "$APP" "$OLD"; then
  if mv "$NEW" "$APP"; then
    log "update: folder swapped"
  else
    mv "$OLD" "$APP"
    log "update FAILED, old version kept: could not move the new app into place"
  fi
else
  log "update FAILED, old version kept: the app is still in use"
fi
xattr -dr com.apple.quarantine "$APP" 2>/dev/null
open "$APP"
sleep 3
rm -rf "$OLD" "$NEW"
log "update: done"
rm -f "$0"
'''


def launch_swap(new_dir: str, log_path: str) -> int:
    """Starts the detached helper; returns its pid. Raises MacUpdateError if it did not start."""
    bundle = install_dir()
    if not bundle:
        raise MacUpdateError("not a packaged build")
    fd, script = tempfile.mkstemp(prefix="um_update_", suffix=".sh")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(_SWAP_SH)
    os.chmod(script, 0o700)
    try:
        proc = subprocess.Popen(["/bin/sh", script, str(os.getpid()), bundle, new_dir, log_path],
                                stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL, start_new_session=True, cwd="/tmp")
    except OSError as e:
        raise MacUpdateError(f"could not start the update helper: {e}") from e
    time.sleep(1.2)
    if proc.poll() is not None:
        raise MacUpdateError(f"the update helper stopped at once (code {proc.returncode})")
    return proc.pid
