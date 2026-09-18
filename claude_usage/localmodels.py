"""Per-model usage from Claude Code's own local logs.

The plan limits the server reports are per *window*, and for most accounts only one model
(e.g. Fable) has a window of its own - there simply is no server-side counter for the other
models. Claude Code, however, writes every assistant turn to ``<config>/projects/**/*.jsonl``
together with the model id and the token counts. From those files this module works out how
this week's work on THIS machine is split between the models.

What it is not: a share of a limit, and not your other devices or the claude.ai chat.

Only three things are taken from each log line: the timestamp, the model id and the token
counts. Message contents are never kept, logged or sent anywhere.

Built to never get in the way
-----------------------------
* everything runs on a daemon worker thread; the UI only reads a finished result,
* the log folder is *searched for* (env var, ~/.claude, ~/.config/claude, a folder the user
  picked) - a missing folder simply means "nothing to show", never an error,
* reading is incremental (each file continues where the last pass stopped),
* every pass has a time budget and a byte budget - what does not fit continues next pass,
* cloud-only placeholder files are skipped (opening them would download them),
* a broken line, an unreadable file or a vanished folder is skipped, not fatal,
* a pass that hangs (e.g. a dead network drive) is abandoned: it is never waited for.
"""

from __future__ import annotations

import json
import os
import re
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple

WEEK_S = 7 * 86400
SCAN_EVERY_S = 300
KEEP_S = 8 * 86400              # entries older than this are dropped from memory
PASS_TIME_BUDGET_S = 12.0       # one pass never works longer than this...
PASS_BYTE_BUDGET = 400 * 1024 * 1024   # ...or reads more than this; the rest waits for the next pass
MAX_LINE_BYTES = 64 * 1024 * 1024      # a single "line" larger than this is not a log line
MAX_FILES_PER_PASS = 5000
STUCK_AFTER_S = 180.0           # a pass running longer than this is considered hung
MAX_ENTRIES = 400_000

# rough relative cost of the token kinds (output is by far the most expensive, cached input
# the cheapest) - so the split reflects effort spent, not just bytes of cached context
W_INPUT, W_OUTPUT, W_CACHE_WRITE, W_CACHE_READ = 1.0, 5.0, 1.25, 0.1

# OneDrive & co. "Files On-Demand": reading such a file would download it
_CLOUD_ONLY = 0x1000 | 0x40000 | 0x400000

_DATE_TAIL = re.compile(r"-\d{8}$")

Entry = Tuple[float, str, float, int, int, str]      # ts, model, weighted, out, total, key


@dataclass
class ModelShare:
    name: str                   # "Opus 4.8"
    share: float                # percent of the weighted tokens in the window
    output_tokens: int
    total_tokens: int
    turns: int


def pretty_model(model_id: str) -> str:
    """claude-opus-4-8 -> Opus 4.8 · claude-3-5-sonnet-20241022 -> Sonnet 3.5"""
    mid = _DATE_TAIL.sub("", str(model_id or "").strip().lower())
    if mid.startswith("claude-"):
        mid = mid[len("claude-"):]
    words, nums = [], []
    for part in mid.split("-"):
        if part.isdigit():
            nums.append(part)
        elif part:
            words.append(part.capitalize())
    name = " ".join(words) or str(model_id)
    return f"{name} {'.'.join(nums)}".strip()


def candidate_roots(override: str = "") -> List[str]:
    """Every place Claude Code may keep its logs; only folders that exist are returned.
    `override` may point at the config folder or straight at its `projects` folder."""
    bases: List[str] = []
    picked = ""
    if override and override.strip():
        picked = os.path.expandvars(os.path.expanduser(override.strip()))
        bases.append(picked)
    env = os.environ.get("CLAUDE_CONFIG_DIR", "")
    bases += [p.strip() for p in re.split(r"[,;]", env) if p.strip()]
    home = os.path.expanduser("~")
    bases += [os.path.join(home, ".claude"), os.path.join(home, ".config", "claude")]
    xdg = os.environ.get("XDG_CONFIG_HOME", "")
    if xdg:
        bases.append(os.path.join(xdg, "claude"))

    roots: List[str] = []
    for base in bases:
        try:
            for path in (base, os.path.join(base, "projects")):
                # a folder counts if it is called "projects" or contains one
                if os.path.basename(os.path.normpath(path)).lower() != "projects":
                    continue
                real = os.path.normcase(os.path.realpath(path))
                if os.path.isdir(path) and real not in [os.path.normcase(os.path.realpath(r)) for r in roots]:
                    roots.append(path)
        except (OSError, ValueError):
            continue
    try:
        if picked and not roots and os.path.isdir(picked):
            roots.append(picked)            # the user knows best, even if it is not called "projects"
    except (OSError, ValueError):
        pass
    return roots


def _ts(text) -> Optional[float]:
    if not isinstance(text, str) or not text:
        return None
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00")).astimezone(timezone.utc).timestamp()
    except (ValueError, OverflowError):
        return None


class LocalModelUsage:
    """`shares(window_start)` is cheap and never blocks; `scan()` starts a background pass."""

    def __init__(self, roots: Optional[List[str]] = None) -> None:
        self.roots = roots              # fixed list (tests); None = search
        self.override = ""              # folder picked by the user ("" = search)
        self._lock = threading.Lock()
        self._thread: Optional[threading.Thread] = None
        self._thread_started = 0.0
        self._generation = 0            # bumps when a hung pass is abandoned
        self._offsets: Dict[str, int] = {}
        self._entries: List[Entry] = []
        self._seen: set = set()
        self._last_scan = 0.0
        self.version = 0
        self.scanned_once = False
        self.last_duration = 0.0
        self.last_roots: List[str] = []
        self.last_note = ""             # short diagnostic: "no log folder", "partial", ...
        self.enabled = True

    # ------------------------------------------------------------------ control

    @property
    def busy(self) -> bool:
        t = self._thread
        if t is None or not t.is_alive():
            return False
        if time.time() - self._thread_started > STUCK_AFTER_S:
            return False                # hung (dead network path?) - do not wait for it
        return True

    def set_override(self, path: str) -> None:
        path = (path or "").strip()
        if path != self.override:
            self.override = path
            with self._lock:            # other folder -> start from scratch
                self._offsets.clear()
                self._entries = []
                self._seen = set()
            self._last_scan = 0.0

    def scan(self, force: bool = False) -> bool:
        if not self.enabled or self.busy:
            return False
        if not force and time.time() - self._last_scan < SCAN_EVERY_S:
            return False
        if self._thread is not None and self._thread.is_alive():
            self._generation += 1       # abandon the hung pass; its result will be ignored
        self._last_scan = self._thread_started = time.time()
        try:
            self._thread = threading.Thread(target=self._run, args=(self._generation,),
                                            daemon=True, name="local-models")
            self._thread.start()
        except RuntimeError:            # cannot start a thread - try again later
            return False
        return True

    # ------------------------------------------------------------------ worker

    def _run(self, generation: int) -> None:
        started = time.time()
        note = ""
        new: List[Entry] = []
        offsets = dict(self._offsets)
        try:
            roots = self.roots if self.roots is not None else candidate_roots(self.override)
            self.last_roots = list(roots)
            if not roots:
                note = "no log folder"
            cutoff = started - KEEP_S
            budget = PASS_BYTE_BUDGET
            files = 0
            for root in roots:
                for dirpath, dirnames, filenames in os.walk(root, onerror=lambda _e: None):
                    dirnames[:] = [d for d in dirnames if not d.startswith(".")]
                    for fn in filenames:
                        if not fn.endswith(".jsonl"):
                            continue
                        if time.time() - started > PASS_TIME_BUDGET_S or budget <= 0 \
                                or files >= MAX_FILES_PER_PASS:
                            note = "partial"    # the rest continues with the next pass
                            break
                        path = os.path.join(dirpath, fn)
                        try:
                            st = os.stat(path)
                            if st.st_mtime < cutoff:
                                continue
                            if getattr(st, "st_file_attributes", 0) & _CLOUD_ONLY:
                                continue        # would have to be downloaded first
                            offset = offsets.get(path, 0)
                            if st.st_size < offset:
                                offset = 0      # the file was rewritten
                            if st.st_size == offset:
                                continue
                            files += 1
                            offsets[path], used = self._read(path, offset, cutoff, new, budget, started)
                            budget -= used
                        except OSError:
                            continue
                    if note == "partial":
                        break
                if note == "partial":
                    break
        except Exception as exc:  # noqa: BLE001 - a broken log must never take the panel down
            note = f"error: {type(exc).__name__}"

        if generation != self._generation:
            return                              # this pass was abandoned as hung
        with self._lock:
            cutoff = time.time() - KEEP_S
            entries = [e for e in self._entries if e[0] >= cutoff] + new
            if len(entries) > MAX_ENTRIES:
                entries = entries[-MAX_ENTRIES:]
            self._entries = entries
            self._seen = {e[5] for e in entries if e[5]}
            self._offsets = offsets
            self.scanned_once = True
            self.last_note = note
            self.version += 1
        self.last_duration = time.time() - started
        if note == "partial":
            self._last_scan = 0.0               # more to read - go on at the next tick

    def _read(self, path: str, offset: int, cutoff: float, out: list, budget: int,
              started: float) -> Tuple[int, int]:
        """Reads new complete lines of one file. Returns (new offset, bytes read)."""
        used = 0
        try:
            with open(path, "rb") as fh:
                fh.seek(offset)
                while used < budget and time.time() - started <= PASS_TIME_BUDGET_S:
                    line = fh.readline(MAX_LINE_BYTES)
                    if not line:
                        break
                    if not line.endswith(b"\n"):
                        if len(line) >= MAX_LINE_BYTES:
                            # not a log line - skip to the end of it and go on
                            while line and not line.endswith(b"\n"):
                                offset += len(line)
                                used += len(line)
                                line = fh.readline(MAX_LINE_BYTES)
                            offset += len(line)
                            used += len(line)
                            continue
                        break                   # half-written last line: next pass
                    offset += len(line)
                    used += len(line)
                    # cheap pre-filter: only assistant turns carry usage
                    if b'"usage"' not in line or b'"assistant"' not in line:
                        continue
                    try:
                        entry = self._entry(line, cutoff)
                    except Exception:  # noqa: BLE001 - one odd line must not cost the file
                        entry = None
                    if entry is not None:
                        out.append(entry)
        except OSError:
            pass
        return offset, used

    def _entry(self, line: bytes, cutoff: float) -> Optional[Entry]:
        obj = json.loads(line)
        msg = obj.get("message") if isinstance(obj, dict) else None
        usage = msg.get("usage") if isinstance(msg, dict) else None
        if not isinstance(usage, dict):
            return None
        model = str(msg.get("model") or "")
        if not model or model.startswith("<"):
            return None                         # "<synthetic>" placeholders
        ts = _ts(obj.get("timestamp"))
        if ts is None or ts < cutoff or ts > time.time() + 86400:
            return None
        key = f"{msg.get('id') or ''}:{obj.get('requestId') or ''}"
        if key == ":":
            key = ""
        elif key in self._seen:
            return None                         # the same turn also lives in a resumed session
        else:
            self._seen.add(key)

        def n(name: str) -> int:
            v = usage.get(name)
            return int(v) if isinstance(v, (int, float)) and 0 <= v < 10 ** 12 else 0

        i, o = n("input_tokens"), n("output_tokens")
        cw, cr = n("cache_creation_input_tokens"), n("cache_read_input_tokens")
        weighted = i * W_INPUT + o * W_OUTPUT + cw * W_CACHE_WRITE + cr * W_CACHE_READ
        return ts, model, weighted, o, i + o + cw + cr, key

    # ------------------------------------------------------------------ result

    def shares(self, window_start: Optional[float] = None) -> List[ModelShare]:
        """Split of the weighted tokens since `window_start` (default: the last 7 days)."""
        now = time.time()
        start = window_start if isinstance(window_start, (int, float)) else now - WEEK_S
        start = min(max(start, now - KEEP_S), now)
        agg: Dict[str, List[float]] = {}
        with self._lock:
            entries = list(self._entries)
        for ts, model, weighted, out_tok, total, _key in entries:
            if ts < start:
                continue
            a = agg.setdefault(pretty_model(model), [0.0, 0, 0, 0])
            a[0] += weighted
            a[1] += out_tok
            a[2] += total
            a[3] += 1
        grand = sum(a[0] for a in agg.values())
        if grand <= 0:
            return []
        rows = [ModelShare(name, a[0] / grand * 100.0, int(a[1]), int(a[2]), int(a[3]))
                for name, a in agg.items()]
        return sorted(rows, key=lambda r: -r.share)
