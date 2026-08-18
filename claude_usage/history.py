"""History window: timeline and statistics - to keep usage under control."""

from __future__ import annotations

import time
from datetime import datetime
from typing import List, Tuple

from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QBrush, QFont, QLinearGradient, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import (
    QButtonGroup,
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from . import winutil
from .datasource import Sample, UsageReader
from .i18n import tr
from .settings import APP_TITLE, Settings
from .theme import Palette, qc, rgba_to_hex, with_alpha

RANGES = [("hist.range_6h", 6 * 3600), ("hist.range_24h", 24 * 3600),
          ("hist.range_7d", 7 * 86400), ("hist.range_all", 0)]

QSS = """
QDialog { background: #16181d; }
QLabel { color: #c9cfdd; }
QLabel#stat { color: #f0f3fa; font-size: 15px; font-weight: 600; }
QLabel#statlabel { color: #79839a; font-size: 11px; }
QPushButton { background: #23272f; color: #c9cfdd; border: 1px solid #333944;
              border-radius: 7px; padding: 5px 12px; }
QPushButton:checked { background: #33405e; color: #eaf0ff; border-color: #4c6296; }
"""


class Chart(QWidget):
    def __init__(self, palette: Palette, settings: Settings):
        super().__init__()
        self.pal = palette
        self.s = settings
        self.rows: List[Sample] = []
        self.span = 24 * 3600
        self.setMinimumHeight(240)

    def set_data(self, rows: List[Sample], span: int) -> None:
        self.rows, self.span = rows, span
        self.update()

    def paintEvent(self, _e) -> None:
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        pal = self.pal
        r = QRectF(self.rect()).adjusted(34, 12, -10, -22)

        p.fillRect(self.rect(), qc((22, 24, 29, 255)))

        # grid + scale
        p.setFont(QFont("Segoe UI", 7))
        for frac, label in ((0.0, "100"), (0.25, "75"), (0.5, "50"), (0.75, "25"), (1.0, "0")):
            y = r.top() + r.height() * frac
            p.setPen(QPen(qc((255, 255, 255, 18)), 1))
            p.drawLine(QPointF(r.left(), y), QPointF(r.right(), y))
            p.setPen(QPen(qc((120, 128, 146, 255))))
            p.drawText(QRectF(0, y - 8, 28, 16),
                       Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter, label)

        # threshold lines
        for value, color in ((self.s["warn_threshold"], pal.warn), (self.s["danger_threshold"], pal.danger)):
            y = r.bottom() - r.height() * (float(value) / 100.0)
            pen = QPen(qc(with_alpha(color, 110)), 1, Qt.PenStyle.DashLine)
            p.setPen(pen)
            p.drawLine(QPointF(r.left(), y), QPointF(r.right(), y))

        if len(self.rows) < 2:
            p.setPen(QPen(qc(pal.dim)))
            p.drawText(r, Qt.AlignmentFlag.AlignCenter, tr("hist.no_data"))
            return

        t0, t1 = self.rows[0].t, max(self.rows[-1].t, int(time.time() * 1000))
        if t1 <= t0:
            t1 = t0 + 1

        gap_ms = 20 * 60 * 1000     # a gap larger than this = a broken measurement

        def draw(series: List[Tuple[int, float]], color, fill: bool) -> None:
            segments: List[List[Tuple[int, float]]] = [[]]
            prev_t = None
            for t, v in series:
                if prev_t is not None and t - prev_t > gap_ms:
                    segments.append([])
                segments[-1].append((t, v))
                prev_t = t

            for seg in segments:
                if len(seg) < 2:
                    continue
                path = QPainterPath()
                area = QPainterPath()
                for i, (t, v) in enumerate(seg):
                    x = r.left() + r.width() * (t - t0) / (t1 - t0)
                    y = r.bottom() - r.height() * max(0.0, min(1.0, v / 100.0))
                    if i == 0:
                        path.moveTo(x, y)
                        area.moveTo(x, r.bottom())
                        area.lineTo(x, y)
                    else:
                        path.lineTo(x, y)
                        area.lineTo(x, y)
                area.lineTo(r.left() + r.width() * (seg[-1][0] - t0) / (t1 - t0), r.bottom())
                area.closeSubpath()
                if fill:
                    grad = QLinearGradient(r.topLeft(), r.bottomLeft())
                    grad.setColorAt(0.0, qc(with_alpha(color, 80)))
                    grad.setColorAt(1.0, qc(with_alpha(color, 0)))
                    p.fillPath(area, QBrush(grad))
                p.setPen(QPen(qc(color), 1.8))
                p.drawPath(path)

        if self.s["show_weekly"]:
            draw([(s.t, s.sd) for s in self.rows], pal.accent, True)
        if self.s["show_five_hour"]:
            draw([(s.t, s.fh) for s in self.rows], pal.ok, False)

        # time axis
        p.setPen(QPen(qc((120, 128, 146, 255))))
        p.setFont(QFont("Segoe UI", 7))
        for frac in (0.0, 0.25, 0.5, 0.75, 1.0):
            ts = t0 + (t1 - t0) * frac
            dt = datetime.fromtimestamp(ts / 1000)
            label = dt.strftime("%H:%M") if (t1 - t0) < 2 * 86400_000 else dt.strftime("%m.%d.")
            x = r.left() + r.width() * frac
            align = Qt.AlignmentFlag.AlignCenter
            p.drawText(QRectF(x - 30, r.bottom() + 3, 60, 16), align, label)


class HistoryWindow(QDialog):
    def __init__(self, settings: Settings, reader: UsageReader, parent=None):
        super().__init__(parent)
        self.s = settings
        self.reader = reader
        self.pal = Palette(settings["theme"], settings["accent"])
        self.setWindowTitle(f"{APP_TITLE} – " + tr("hist.title"))
        self.setWindowIcon(winutil.app_icon())
        self.setStyleSheet(QSS)
        self.resize(640, 420)

        top = QHBoxLayout()
        self.group = QButtonGroup(self)
        self.group.setExclusive(True)
        for i, (label, span) in enumerate(RANGES):
            b = QPushButton(tr(label))
            b.setCheckable(True)
            b.setChecked(span == 24 * 3600)
            self.group.addButton(b, i)
            top.addWidget(b)
        top.addStretch(1)
        legend = QLabel()
        legend.setStyleSheet(f"color: {self.pal.dim[0]:02x};")
        legend.setText(
            f'<span style="color:rgb{self.pal.ok[:3]}">●</span> ' + tr("hist.legend_5h") + ' &nbsp;&nbsp;'
            f'<span style="color:rgb{self.pal.accent[:3]}">●</span> ' + tr("hist.legend_week")
        )
        top.addWidget(legend)
        self.group.idClicked.connect(self.refresh)

        self.chart = Chart(self.pal, settings)

        self.stats = QHBoxLayout()
        self.stat_labels = {}
        for key, lkey in (("now", "hist.stat_now"), ("peak", "hist.stat_peak"),
                          ("burn", "hist.stat_burn"), ("sessions", "hist.stat_sessions"),
                          ("forecast", "hist.stat_forecast")):
            box = QVBoxLayout()
            value = QLabel("–")
            value.setObjectName("stat")
            cap = QLabel(tr(lkey))
            cap.setObjectName("statlabel")
            box.addWidget(value)
            box.addWidget(cap)
            self.stats.addLayout(box)
            self.stat_labels[key] = value

        root = QVBoxLayout(self)
        root.setContentsMargins(14, 12, 14, 12)
        root.setSpacing(10)
        root.addLayout(top)
        root.addWidget(self.chart, 1)
        root.addLayout(self.stats)

        self.refresh()

    def refresh(self, *_args) -> None:
        span = RANGES[max(0, self.group.checkedId())][1]
        since = int((time.time() - span) * 1000) if span else None
        rows = self.reader.series(self.s["org"] or None, since)
        self.chart.set_data(rows, span)
        self._update_stats(rows)

    def _update_stats(self, rows: List[Sample]) -> None:
        if not rows:
            for lbl in self.stat_labels.values():
                lbl.setText("–")
            return

        last = rows[-1]
        self.stat_labels["now"].setText(f"{last.sd:.0f}%")
        self.stat_labels["peak"].setText(f"{max(s.sd for s in rows):.0f}%")

        span_days = max(0.1, (rows[-1].t - rows[0].t) / 86_400_000)
        gained = 0.0
        for a, b in zip(rows, rows[1:]):
            if b.sd > a.sd:
                gained += b.sd - a.sd
        per_day = gained / span_days
        self.stat_labels["burn"].setText(tr("panel.per_day", f"{per_day:.1f}"))

        sessions = sum(1 for a, b in zip(rows, rows[1:]) if a.fh <= 0 < b.fh)
        self.stat_labels["sessions"].setText(str(sessions))

        metrics = self.reader.read(self.s["org"] or None)
        left_ms = metrics.weekly.reset_in_ms
        days_left = (left_ms / 86_400_000) if left_ms is not None else 7.0
        forecast = min(999.0, last.sd + per_day * days_left)
        lbl = self.stat_labels["forecast"]
        lbl.setText(f"{forecast:.0f}%")
        color = self.pal.danger if forecast >= 100 else (
            self.pal.warn if forecast >= float(self.s["warn_threshold"]) else self.pal.ok)
        lbl.setStyleSheet(f"color: {rgba_to_hex(color)}; font-size: 15px; font-weight: 600;")
