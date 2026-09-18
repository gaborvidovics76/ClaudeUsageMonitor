"""Backup details window + the formatting helpers shared with the panel's status bar."""

from __future__ import annotations

import html
import os
import time
from datetime import datetime
from typing import Dict, Optional

from PySide6.QtCore import QPointF, Qt, QUrl, Signal
from PySide6.QtGui import QColor, QIcon, QPainter, QPixmap
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTabWidget,
    QTextBrowser,
    QVBoxLayout,
)

from . import backups as bk
from . import winutil
from .datasource import fmt_delta
from .i18n import tr
from .settings import APP_TITLE, Settings

# traffic-light colors (deliberately theme-independent: green / yellow / red must read as such)
LAMP = {
    "green": (52, 199, 120, 255),
    "yellow": (240, 190, 50, 255),
    "red": (235, 77, 75, 255),
    "pending": (130, 136, 150, 255),
}

QSS = """
QDialog { background: #16181d; }
QTabWidget::pane { border: 1px solid #2c313b; border-radius: 10px; top: -1px; background: #1b1e25; }
QTabBar::tab { background: transparent; color: #99a1b3; padding: 7px 16px; margin-right: 2px;
               border-top-left-radius: 8px; border-top-right-radius: 8px; }
QTabBar::tab:selected { background: #1b1e25; color: #f0f3fa; border: 1px solid #2c313b; border-bottom: none; }
QTextBrowser { background: #1b1e25; color: #c9cfdd; border: none; padding: 6px; }
QLabel { color: #79839a; }
QPushButton { background: #262b34; color: #e6eaf3; border: 1px solid #343b47; border-radius: 8px; padding: 6px 14px; }
QPushButton:hover { background: #2f3540; }
QPushButton:disabled { color: #6b7385; }
"""

DOC_CSS = """
body, p, td, b { color: #c9cfdd; }
body { font-family: 'Segoe UI'; font-size: 10pt; }
b { color: #eef1f8; }
h3 { color: #eef1f8; font-size: 10.5pt; margin-top: 14px; margin-bottom: 4px; }
td { padding: 2px 10px 2px 0; vertical-align: top; }
.dim { color: #7f889c; }
.ok { color: #34c778; }
.warn { color: #f0be32; }
.err { color: #eb4d4b; }
.mono { font-family: Consolas, 'Cascadia Mono', monospace; font-size: 8.5pt; color: #aab2c3; }
a { color: #8fb0ff; text-decoration: none; }
"""


# --------------------------------------------------------------------------- helpers


def rgb_hex(rgba) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgba[:3])


def fmt_time(t: Optional[float]) -> str:
    return datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M") if t else "–"


def fmt_size(n: Optional[int]) -> str:
    if n is None:
        return "–"
    size = float(n)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024 or unit == "TB":
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024
    return f"{n} B"


def short_age(seconds: float) -> str:
    seconds = max(0.0, seconds)
    if seconds < 3600:
        return tr("backup.age_m", max(1, int(seconds // 60)))
    if seconds < 48 * 3600:
        return tr("backup.age_h", int(seconds // 3600))
    return tr("backup.age_d", int(seconds // 86400))


def thresholds_of(s: Settings):
    return bk.thresholds(s["backup_green_hours"], s["backup_yellow_hours"])


def level_of(status: Optional[bk.BackupStatus], key: str, s: Settings, now: Optional[float] = None) -> str:
    if status is None:
        return "pending"
    g, y = thresholds_of(s)
    return bk.lamp_level(status.items.get(key), g, y, now)


def level_text(level: str) -> str:
    return {
        "green": tr("backup.level_green"),
        "yellow": tr("backup.level_yellow"),
        "red": tr("backup.level_red"),
        "pending": tr("backup.checking"),
    }[level]


def state_text(state: str) -> str:
    return tr({
        "ok": "backup.state_ok",
        "error": "backup.state_error",
        "running": "backup.state_running",
        "interrupted": "backup.state_interrupted",
    }.get(state, "backup.level_none"))


def component_name(name: str) -> str:
    if name == "@vault":
        return tr("backup.comp.vault")
    if name == "@cowork":
        return tr("backup.comp.cowork")
    return name


def lamp_icon(level: str, size: int = 14) -> QIcon:
    pm = QPixmap(size, size)
    pm.fill(Qt.GlobalColor.transparent)
    p = QPainter(pm)
    p.setRenderHint(QPainter.RenderHint.Antialiasing, True)
    p.setPen(Qt.PenStyle.NoPen)
    p.setBrush(QColor(*LAMP[level]))
    p.drawEllipse(QPointF(size / 2, size / 2), size * 0.36, size * 0.36)
    p.end()
    return QIcon(pm)


def tooltip_text(key: str, status: Optional[bk.BackupStatus], s: Settings) -> str:
    name = tr(f"backup.name.{key}")
    if status is None:
        return f"{name}: {tr('backup.checking')}"
    item = status.items.get(key)
    now = time.time()
    level = level_of(status, key, s, now)
    lines = [f"{name} – {level_text(level)}"]
    if item is None or item.last_ok is None:
        lines.append(tr("backup.level_none"))
    else:
        lines.append(tr("backup.last_ok", fmt_time(item.last_ok),
                        fmt_delta(int((now - item.last_ok) * 1000))))
    if item is not None and item.run is not None and item.state not in ("ok", "none"):
        lines.append(tr("backup.last_run", fmt_time(item.run.started), state_text(item.state)))
    lines.append(tr("backup.tip_click"))
    return "\n".join(lines)


def summary_text(status: Optional[bk.BackupStatus], s: Settings) -> str:
    """One short line for the tray tooltip."""
    if status is None:
        return tr("backup.checking")
    now = time.time()
    parts = []
    for key in bk.KEYS:
        item = status.items.get(key)
        age = short_age(now - item.last_ok) if (item and item.last_ok) else "–"
        mark = {"green": "✓", "yellow": "!", "red": "✗", "pending": "…"}[level_of(status, key, s, now)]
        parts.append(f"{mark} {tr('backup.name.' + key)} {age}")
    return "  ".join(parts)


def _link(path: str, label: Optional[str] = None) -> str:
    path = os.path.expandvars(path)
    text = html.escape(label if label is not None else path)
    if path and os.path.exists(path):
        return f'<a href="{QUrl.fromLocalFile(path).toString()}">{text}</a>'
    return text


def _esc(text) -> str:
    return html.escape(str(text))


# --------------------------------------------------------------------------- rendering


def render(key: str, status: Optional[bk.BackupStatus], s: Settings, busy: bool = False) -> str:
    now = time.time()
    out = []
    if status is None:
        return f"<p class='dim'>{_esc(tr('backup.checking'))}</p>"
    if status.error:
        out.append(f"<p class='err'>{_esc(status.error)}</p>")
    if not status.root_found:
        out.append(f"<p class='err'>{_esc(tr('backup.no_root', status.root or '?'))}</p>")
        return "".join(out)

    item = status.items.get(key) or bk.BackupItem(key=key)
    level = level_of(status, key, s, now)
    color = rgb_hex(LAMP[level])
    out.append(f"<p style='font-size:15pt; font-weight:600; color:{color}; margin-bottom:2px'>"
               f"● {_esc(level_text(level))}</p>")
    if item.last_ok:
        out.append(f"<p style='margin-top:0'>{_esc(tr('backup.last_ok', fmt_time(item.last_ok), fmt_delta(int((now - item.last_ok) * 1000))))}</p>")
    else:
        out.append(f"<p class='err' style='margin-top:0'>{_esc(tr('backup.level_none'))}</p>")

    run = item.run
    rows = []
    if run is not None:
        cls = {"ok": "ok", "error": "err", "running": "warn", "interrupted": "err"}.get(run.result, "dim")
        extra = f" <span class='warn'>{_esc(tr('backup.dry_run'))}</span>" if run.dry_run else ""
        rows.append((tr("backup.last_run", fmt_time(run.started), "").rstrip(" –"),
                     f"<span class='{cls}'>{_esc(state_text(run.result))}</span>{extra}"))
        rows.append((tr("backup.log_file"), _link(run.path, os.path.basename(run.path))))

    if key == "onedrive":
        rows.append((tr("backup.target"), _link((run.target if run and run.target else status.root))))
    elif key == "nextcloud":
        target = (run.target if run and run.target else status.remote) or "–"
        rows.append((tr("backup.target"), _esc(target)))
        st = (item.ok_run or run).storage if (item.ok_run or run) else {}
        if st.get("Total"):
            rows.append(("", _esc(tr("backup.storage", st.get("Used", "?"), st.get("Total", "?"), st.get("Free", "?")))))
    elif key == "obsidian":
        snap = item.snapshot
        if snap is not None:
            rows.append((tr("backup.snapshot"), _link(snap.path, os.path.basename(snap.path)) + f" · {fmt_size(snap.size)}"))
            rows.append(("", _esc(tr("backup.snap_kept", snap.count, fmt_size(snap.total_size)))
                         + " · " + _link(os.path.dirname(snap.path), tr("backup.open"))))
            if snap.vault:
                rows.append((tr("backup.vault"), _link(snap.vault)))
            up = tr("backup.uploaded_yes", fmt_time(snap.uploaded_at)) if snap.uploaded_at else tr("backup.uploaded_no")
            rows.append(("", f"<span class='{'ok' if snap.uploaded_at else 'warn'}'>{_esc(up)}</span>"))
            if snap.vault_changed:
                rows.append(("", f"<span class='warn'>{_esc(tr('backup.vault_changed', snap.vault_changed))}</span>"))
        if item.problem:
            rows.append(("", f"<span class='err'>{_esc(item.problem)}</span>"))
    out.append(_table(rows))

    # ---- what is backed up
    if s["backup_d_components"]:
        comp_rows = []
        if key == "onedrive" and run is not None:
            for c in run.components:
                comp_rows.append(_component_row(c, status.root))
        elif key == "nextcloud" and run is not None:
            for c in run.components:
                res = _status_span(c.status, tr("backup.done") if c.status == "ok" else
                                   (tr("backup.rc_failed", c.code) if c.code is not None else tr("backup.failed")))
                src = _link(c.source) if c.source else ""
                comp_rows.append(f"<tr><td>{res}</td><td><b>{_esc(component_name(c.name))}</b><br>"
                                 f"<span class='dim'>{src} → {_esc(c.dest)}</span></td></tr>")
        elif key == "obsidian" and item.snapshot is not None:
            snap = item.snapshot
            if snap.cloud_only:
                comp_rows.append(f"<tr><td class='dim'>{_esc(tr('backup.cloud_only'))}</td></tr>")
            elif snap.files is not None:
                comp_rows.append(f"<tr><td>{_esc(tr('backup.zip_summary', snap.files, snap.notes, fmt_size(snap.uncompressed)))}</td></tr>")
        if comp_rows:
            out.append(f"<h3>{_esc(tr('backup.sec_components'))}</h3>")
            out.append("<table cellspacing='0'>" + "".join(comp_rows) + "</table>")

    # ---- contents
    if s["backup_d_contents"]:
        if key == "nextcloud":
            src = item.ok_run if (run is None or not run.successful) and item.ok_run else run
            if src is not None:
                out.append(f"<h3>{_esc(tr('backup.sec_contents'))}</h3>")
                out.append(f"<p>{_esc(tr('backup.uploaded', src.new, src.replaced, src.rclone_errors))}</p>")
                if src.groups:
                    out.append(f"<p class='dim'>{_esc(tr('backup.uploaded_groups'))}</p>")
                    out.append(_table([(str(n), g) for g, n in src.groups[:14]], raw_right=False, right_first=True))
                if src.files:
                    out.append(f"<p class='dim'>{_esc(tr('backup.uploaded_files'))}</p>")
                    shown = src.files[:40]
                    body = "<br>".join(_esc(f) for f in shown)
                    if len(src.files) > len(shown):
                        body += "<br>" + _esc(tr("backup.and_more", len(src.files) - len(shown)))
                    out.append(f"<p class='mono'>{body}</p>")
        elif key == "obsidian" and item.snapshot is not None and item.snapshot.files is not None:
            snap = item.snapshot
            out.append(f"<h3>{_esc(tr('backup.sec_contents'))}</h3>")
            if snap.folders:
                out.append(f"<p class='dim'>{_esc(tr('backup.folders'))}</p>")
                out.append(_table([(str(n), f) for f, n in snap.folders[:16]], raw_right=False, right_first=True))
            if snap.recent:
                out.append(f"<p class='dim'>{_esc(tr('backup.recent_notes'))}</p>")
                out.append(_table([(fmt_time(t), n) for n, t in snap.recent], raw_right=False))

    # ---- problems
    if s["backup_d_problems"] and run is not None:
        out.append(f"<h3>{_esc(tr('backup.sec_problems'))}</h3>")
        lines = [f"<span class='err'>✗ {_esc(e)}</span>" for e in run.errors[:25]]
        lines += [f"<span class='warn'>! {_esc(w)}</span>" for w in run.warnings[:25]]
        out.append("<p>" + ("<br>".join(lines) if lines else f"<span class='ok'>{_esc(tr('backup.none_found'))}</span>") + "</p>")

    # ---- scheduled tasks
    if s["backup_d_tasks"] and item.tasks:
        out.append(f"<h3>{_esc(tr('backup.sec_tasks'))}</h3>")
        trows = []
        for t in item.tasks:
            res = "0" if t.result == 0 else f"0x{t.result:X}"
            cls = "ok" if t.result == 0 else ("warn" if t.result in (0x41301, 0x41303) else "err")
            nxt = fmt_time(t.next_run) if t.next_run else tr("backup.task_event")
            trows.append((t.name, f"{_esc(t.state)} · " + _esc(tr("backup.task_row", fmt_time(t.last_run), "§", nxt))
                          .replace("§", f"<span class='{cls}'>{res}</span>")))
        out.append(_table(trows))

    # ---- log tail
    if s["backup_d_log"] and run is not None and run.tail:
        out.append(f"<h3>{_esc(tr('backup.sec_log'))}</h3>")
        out.append("<p class='mono'>" + "<br>".join(_esc(ln) for ln in run.tail) + "</p>")

    return "".join(out)


def _status_span(status: str, text: str) -> str:
    cls = {"ok": "ok", "error": "err", "skipped": "warn", "pending": "warn"}.get(status, "dim")
    mark = {"ok": "●", "error": "✗", "skipped": "○", "pending": "…"}.get(status, "●")
    return f"<span class='{cls}'>{mark}</span>&nbsp;<span class='{cls}'>{_esc(text)}</span>"


def _component_row(c: bk.Component, root: str) -> str:
    if c.status == "skipped":
        res = tr("backup.skipped")
    elif c.status == "error":
        res = tr("backup.rc_failed", c.code) if c.code is not None else tr("backup.failed")
    elif c.name == "@cowork":
        res = tr("backup.zip_new", c.detail or 0)
    elif c.name == "@vault":
        res = c.detail
    elif c.code is not None:
        res = tr("backup.rc_copied") if c.code & 1 else tr("backup.rc_nochange")
    else:
        res = tr("backup.done")
    dest = os.path.join(root, c.dest) if c.dest else ""
    sub = []
    if c.source:
        sub.append(f"{_esc(tr('backup.source'))}: {_link(c.source)}")
    if dest:
        size = f" · {_esc(tr('backup.files_size', c.files, fmt_size(c.size)))}" if c.files is not None else ""
        sub.append(f"{_esc(tr('backup.target'))}: {_link(dest, c.dest)}{size}")
    return (f"<tr><td>{_status_span(c.status, '')}</td><td><b>{_esc(component_name(c.name))}</b> – "
            f"<span class='dim'>{_esc(res)}</span><br><span class='dim'>{'<br>'.join(sub)}</span></td></tr>")


def _table(rows, raw_right: bool = True, right_first: bool = False) -> str:
    if not rows:
        return ""
    cells = []
    for left, right in rows:
        r = right if raw_right else _esc(right)
        if right_first:
            cells.append(f"<tr><td align='right' class='dim'>{_esc(left)}</td><td>{r}</td></tr>")
        else:
            cells.append(f"<tr><td class='dim'>{_esc(left)}</td><td>{r}</td></tr>")
    return "<table cellspacing='0'>" + "".join(cells) + "</table>"


# --------------------------------------------------------------------------- window


class BackupDialog(QDialog):
    refreshRequested = Signal()

    def __init__(self, settings: Settings, parent=None):
        super().__init__(parent)
        self.s = settings
        self.status: Optional[bk.BackupStatus] = None
        self.busy = False
        self.setWindowTitle(f"{APP_TITLE} – " + tr("backup.title"))
        self.setWindowIcon(winutil.app_icon())
        self.setStyleSheet(QSS)
        self.resize(640, 600)

        self.tabs = QTabWidget(self)
        self.views: Dict[str, QTextBrowser] = {}
        for key in bk.KEYS:
            view = QTextBrowser()
            view.setOpenLinks(False)
            view.anchorClicked.connect(self._open)
            view.document().setDefaultStyleSheet(DOC_CSS)
            self.views[key] = view
            self.tabs.addTab(view, lamp_icon("pending"), tr(f"backup.name.{key}"))

        self.legend = QLabel()
        self.legend.setWordWrap(True)
        self.checked = QLabel()
        self.btn_refresh = QPushButton(tr("backup.refresh"))
        self.btn_refresh.clicked.connect(self.refreshRequested.emit)
        btn_close = QPushButton(tr("set.close"))
        btn_close.clicked.connect(self.close)

        bottom = QHBoxLayout()
        bottom.addWidget(self.checked, 1)
        bottom.addWidget(self.btn_refresh)
        bottom.addWidget(btn_close)

        root = QVBoxLayout(self)
        root.setContentsMargins(14, 14, 14, 12)
        root.setSpacing(8)
        root.addWidget(self.tabs, 1)
        root.addWidget(self.legend)
        root.addLayout(bottom)

    def select(self, key: Optional[str]) -> None:
        if key in bk.KEYS:
            self.tabs.setCurrentIndex(bk.KEYS.index(key))

    def set_status(self, status: Optional[bk.BackupStatus], busy: bool = False) -> None:
        self.status, self.busy = status, busy
        now = time.time()
        for i, key in enumerate(bk.KEYS):
            view = self.views[key]
            bar = view.verticalScrollBar()
            pos = bar.value()
            view.setHtml(render(key, status, self.s, busy))
            bar.setValue(pos)
            self.tabs.setTabIcon(i, lamp_icon(level_of(status, key, self.s, now)))
            item = status.items.get(key) if status else None
            age = f" · {short_age(now - item.last_ok)}" if (item and item.last_ok) else ""
            self.tabs.setTabText(i, tr(f"backup.name.{key}") + age)
        g, y = thresholds_of(self.s)
        self.legend.setText(tr("backup.legend", f"{g:g}", f"{y:g}"))
        if busy:
            self.checked.setText(tr("backup.checking"))
        elif status is not None:
            self.checked.setText(tr("backup.checked_at", datetime.fromtimestamp(status.checked_at).strftime("%H:%M:%S")))
        else:
            self.checked.setText("")
        self.btn_refresh.setEnabled(not busy)

    @staticmethod
    def _open(url: QUrl) -> None:
        path = url.toLocalFile()
        if path and os.path.exists(path):
            winutil.open_path(path)
