"""The floating ("post-it") panel - a fully custom-drawn, frameless window."""

from __future__ import annotations

import math
import sys
import time
from typing import List, Optional, Tuple

from PySide6.QtCore import QPoint, QPointF, QRectF, Qt, Signal
from PySide6.QtGui import (
    QBrush,
    QFont,
    QFontDatabase,
    QFontMetrics,
    QGuiApplication,
    QLinearGradient,
    QPainter,
    QPainterPath,
    QPen,
)
from PySide6.QtWidgets import QToolTip, QWidget

from . import backups as bk
from .backup_dialog import LAMP, level_of, short_age, tooltip_text
from .datasource import Gauge, Metrics, detail_label, fmt_age, fmt_delta
from .i18n import tr
from .settings import GAUGE_IDS, Settings
from .theme import Palette, qc, with_alpha

SHADOW_MARGIN = 18
STRIP_H = 20            # height of the backup status bar (unscaled)
ROW_H = 15              # one line of the small list under the gauges (unscaled)

# plan badge: gradient start / end per plan
PLAN_STYLE = {
    "pro": ((217, 119, 87, 255), (242, 166, 90, 255)),
    "max": ((124, 92, 255, 255), (230, 107, 214, 255)),
    "team": ((45, 140, 255, 255), (38, 198, 190, 255)),
    "enterprise": ((84, 96, 120, 255), (150, 162, 186, 255)),
}


def _font(size: float, weight: QFont.Weight = QFont.Weight.Normal, spacing: float = 0.0) -> QFont:
    if sys.platform.startswith("win"):
        f = QFont("Segoe UI Variable Display")
        if not f.exactMatch():
            f = QFont("Segoe UI")
    else:
        f = QFont(QFontDatabase.systemFont(QFontDatabase.SystemFont.GeneralFont).family())
    f.setPointSizeF(max(5.0, size))
    f.setWeight(weight)
    if spacing:
        f.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, spacing)
    return f


class UsageWidget(QWidget):
    menuRequested = Signal(QPoint)
    doubleClicked = Signal()
    backupClicked = Signal(str)

    def __init__(self, settings: Settings):
        super().__init__(None)
        self.s = settings
        self.metrics: Metrics = Metrics()
        self.palette_: Palette = Palette(self.s["theme"], self.s["accent"])
        self._drag_offset: Optional[QPoint] = None
        self._press_global: Optional[QPoint] = None
        self._press_key: Optional[str] = None
        self._dragging = False
        self._hover = False
        self.update_version = ""        # a newer version is offered -> small marker in the header
        # activity feedback: a fetch is running / the last one failed
        self.busy = False
        self.note = ""                  # short reason why the data is not fresher
        self.retry_in: Optional[float] = None
        # backup status bar
        self.backup: Optional[bk.BackupStatus] = None
        self.backup_expected = False
        self._backup_shown = False
        self._backup_hits: List[Tuple[QRectF, str]] = []
        self._hover_key: Optional[str] = None
        self._age_rect = QRectF()       # header status text - hover shows the details
        self._badge_rect = QRectF()     # plan badge - hover shows the profile card
        self._hover_badge = False
        self._rows_shown = 0
        self.local_models: list = []    # ModelShare rows from Claude Code's local logs
        self._hover_age = False

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_AlwaysShowToolTips, True)
        if sys.platform == "darwin":
            # a Tool window normally hides whenever the application is not the active one
            self.setAttribute(Qt.WidgetAttribute.WA_MacAlwaysShowToolWindow, True)
        self.setMouseTracking(True)
        # We draw the shadow by hand: QGraphicsDropShadowEffect caches the image on
        # a translucent, frameless window, so the old content stayed on screen even
        # after update().
        self.apply_settings()

    # ------------------------------------------------------------- setup

    def apply_settings(self) -> None:
        self.palette_ = Palette(self.s["theme"], self.s["accent"])

        flags = Qt.WindowType.FramelessWindowHint
        flags |= Qt.WindowType.Window if self.s["show_in_taskbar"] else Qt.WindowType.Tool
        if self.s["always_on_top"]:
            flags |= Qt.WindowType.WindowStaysOnTopHint
        if self.s["click_through"]:
            flags |= Qt.WindowType.WindowTransparentForInput
        was_visible = self.isVisible()
        # setWindowFlags hides the window, so we call it only on an actual change
        # (otherwise the panel would flicker on every slider move).
        flags_changed = flags != getattr(self, "_flags", None)
        if flags_changed:
            self._flags = flags
            self.setWindowFlags(flags)
        self.setWindowOpacity(float(self.s["opacity"]))

        self._relayout()
        x, y = self.s["pos_x"], self.s["pos_y"]
        if x is not None and y is not None and self._on_any_screen(int(x), int(y)):
            self.move(int(x), int(y))
        else:
            # No saved position, or that monitor no longer exists.
            self._default_position()
        if flags_changed and (was_visible or self.s["visible"]):
            self.show()
        self.update()

    def _on_any_screen(self, x: int, y: int) -> bool:
        """Is the panel's center still on one of the connected monitors?"""
        center = QPoint(x + self.width() // 2, y + self.height() // 2)
        return any(s.geometry().contains(center) for s in QGuiApplication.screens())

    def _default_position(self) -> None:
        scr = self.screen() or self.window().screen()
        if scr is None:
            return
        area = scr.availableGeometry()
        self.move(area.right() - self.width() - 8, area.top() + 24)

    def set_metrics(self, metrics: Metrics) -> None:
        self.metrics = metrics
        # the model gauge appears/disappears with the data -> re-measure the panel
        shown = bool(self.s["show_model"]) and metrics.has_model
        if shown != getattr(self, "_model_shown", False) or len(self.detail_rows()) != self._rows_shown:
            self._model_shown = shown
            self._relayout()
        self.update()

    # ------------------------------------------------------------- details

    def set_local_models(self, shares: list) -> None:
        self.local_models = list(shares or [])
        if len(self.detail_rows()) != self._rows_shown:
            self._relayout()
        self.update()

    @staticmethod
    def _short_tokens(n: int) -> str:
        if n >= 1_000_000:
            return f"{n / 1_000_000:.1f}M"
        if n >= 1_000:
            return f"{n / 1_000:.0f}k"
        return str(n)

    def _local_rows(self, hidden: set) -> list:
        """This week's split between the models on this machine. A share, not a limit -
        so it gets its own header and neutral colours."""
        if not self.s["show_local_models"]:
            return []
        rows = [("local:" + sh.name, sh.name, sh.share,
                 f"{sh.share:.0f}%  \u00b7  {self._short_tokens(sh.output_tokens)}", None)
                for sh in self.local_models if ("local:" + sh.name) not in hidden and sh.share >= 0.5]
        if not rows:
            return []
        return [("@header", tr("detail.local_header"), None, "", None)] + rows

    def detail_rows(self) -> list:
        """Visible lines of the small list: (id, label, percent|None, right text, reset ms|None).
        Every category and every single row can be switched off."""
        m, s = self.metrics, self.s
        if not m.ok:
            return []
        hidden = set(s["detail_hidden"] or [])
        return self._server_rows(hidden) + self._local_rows(hidden)

    def _server_rows(self, hidden: set) -> list:
        m, s = self.metrics, self.s
        big = f"model:{m.model_name}".lower() if self._model_on() else ""
        out = []
        for row in m.rows:
            if row.id in hidden:
                continue
            if row.category == "model":
                if not s["show_model_list"] or row.id.lower() == big:
                    continue            # that model already has its own gauge
            elif not s["show_surfaces"]:
                continue
            out.append((row.id, detail_label(row), row.value, f"{row.value:.0f}%", row.reset_in_ms))
        ex = m.extra
        if ex is not None and s["show_extra_usage"] and "extra" not in hidden:
            if ex.enabled:
                limit = f"{ex.monthly_limit:.2f}" if ex.monthly_limit is not None else tr("detail.unlimited")
                out.append(("extra", tr("detail.extra"), ex.utilization,
                            f"{ex.used or 0.0:.2f} / {limit} {ex.currency}", None))
            else:
                out.append(("extra", tr("detail.extra"), None, tr("detail.off"), None))
        return out

    def _profile_tooltip(self) -> str:
        pr = self.metrics.profile
        if pr is None:
            return ""
        lines = []
        if pr.name:
            lines.append(pr.name)
        plan = (pr.plan.capitalize() + (" " + pr.multiplier if pr.multiplier else "")) if pr.plan else "?"
        lines.append(tr("profile.plan", plan))
        if pr.tier:
            lines.append(tr("profile.tier", pr.tier))
        if pr.has_extra_usage is not None:
            lines.append(tr("profile.extra", tr("detail.on") if pr.has_extra_usage else tr("detail.off")))
        if pr.created_at:
            lines.append(tr("profile.since", pr.created_at[:10]))
        return "\n".join(lines)

    def _paint_badge(self, p: QPainter, x: float, top: float) -> float:
        """The plan as a little gradient pill with a sparkle. Returns its width (0 = none)."""
        pr = self.metrics.profile
        self._badge_rect = QRectF()
        if pr is None or not pr.badge or not self.s["show_plan_badge"]:
            return 0.0
        k = self.k
        text = pr.badge
        if self.s["show_plan_name"] and pr.name:
            text += "  \u00b7  " + pr.name.split()[0]
        font = _font(6.0 * k, QFont.Weight.Bold, 0.7 * k)
        tw = QFontMetrics(font).horizontalAdvance(text)
        h = 12.5 * k
        w = tw + 23 * k
        rect = QRectF(x, top + 0.8 * k, w, h)
        c0, c1 = PLAN_STYLE.get(pr.plan, PLAN_STYLE["enterprise"])

        p.setPen(Qt.PenStyle.NoPen)
        glow = QPainterPath()
        glow.addRoundedRect(rect.adjusted(-1.6 * k, -1.6 * k, 1.6 * k, 1.6 * k), h / 2 + 1.6 * k, h / 2 + 1.6 * k)
        p.fillPath(glow, qc(with_alpha(c1, 46)))

        pill = QPainterPath()
        pill.addRoundedRect(rect, h / 2, h / 2)
        grad = QLinearGradient(rect.topLeft(), rect.bottomRight())
        grad.setColorAt(0.0, qc(c0))
        grad.setColorAt(1.0, qc(c1))
        p.fillPath(pill, QBrush(grad))
        shine = QPainterPath()
        shine.addRoundedRect(QRectF(rect.left() + 2 * k, rect.top() + 1.2 * k, rect.width() - 4 * k, h * 0.42),
                             h * 0.21, h * 0.21)
        p.fillPath(shine, qc((255, 255, 255, 46)))

        def sparkle(cx: float, cy: float, r: float, alpha: int) -> None:
            star = QPainterPath()
            for i in range(8):
                rad = r if i % 2 == 0 else r * 0.34
                ang = math.pi / 4 * i - math.pi / 2
                pt = QPointF(cx + rad * math.cos(ang), cy + rad * math.sin(ang))
                star.moveTo(pt) if i == 0 else star.lineTo(pt)
            star.closeSubpath()
            p.fillPath(star, qc((255, 255, 255, alpha)))

        cy = rect.center().y()
        sparkle(rect.left() + 8.2 * k, cy + 0.4 * k, 3.6 * k, 255)
        sparkle(rect.left() + 12.6 * k, cy - 2.9 * k, 1.5 * k, 215)

        p.setPen(QPen(qc((255, 255, 255, 255))))
        p.setFont(font)
        p.drawText(QRectF(rect.left() + 16.5 * k, rect.top(), tw + 4 * k, h),
                   Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, text)
        self._badge_rect = rect
        return w

    def _paint_rows(self, p: QPainter, r: QRectF) -> float:
        """The small list (other models, surfaces, extra usage). Returns the y below it."""
        rows = self.detail_rows()
        if not rows:
            return r.top()
        k, pal = self.k, self.palette_
        warn, danger = self.s["warn_threshold"], self.s["danger_threshold"]
        y = r.top() + 3 * k
        p.setPen(QPen(qc(with_alpha(pal.dim, 40)), 1.0))
        p.drawLine(QPointF(r.left() + 2 * k, y), QPointF(r.right() - 2 * k, y))
        y += 4 * k
        label_font = _font(6.5 * k, QFont.Weight.DemiBold, 0.3 * k)
        value_font = _font(6.9 * k, QFont.Weight.Bold)
        sub_font = _font(6.0 * k)
        lfm, vfm, sfm = QFontMetrics(label_font), QFontMetrics(value_font), QFontMetrics(sub_font)
        label_w = min(r.width() * 0.42,
                      max([lfm.horizontalAdvance(x[1]) for x in rows if x[0] != "@header"] or [0]) + 4 * k)

        for rid, label, value, right, reset_ms in rows:
            line = QRectF(r.left(), y, r.width(), ROW_H * k)
            if rid == "@header":
                p.setFont(_font(5.6 * k, QFont.Weight.DemiBold, 0.9 * k))
                p.setPen(QPen(qc(with_alpha(pal.dim, 210))))
                p.drawText(QRectF(line.left() + 1 * k, line.top() + 2 * k, line.width(), line.height() - 2 * k),
                           Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, label)
                y += ROW_H * k
                continue
            local = rid.startswith("local:")
            if local:
                color = pal.accent          # a share of your own work - nothing to warn about
            else:
                color = pal.status(value, warn, danger) if value is not None else with_alpha(pal.dim, 170)
            p.setPen(Qt.PenStyle.NoPen)
            p.setBrush(qc(color))
            p.drawEllipse(QPointF(line.left() + 3.5 * k, line.center().y()), 2.1 * k, 2.1 * k)

            p.setFont(label_font)
            p.setPen(QPen(qc(with_alpha(pal.text, 215))))
            text = lfm.elidedText(label, Qt.TextElideMode.ElideRight, int(label_w))
            p.drawText(QRectF(line.left() + 10 * k, line.top(), label_w, line.height()),
                       Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, text)

            sub = fmt_delta(reset_ms) if (self.s["show_reset"] and reset_ms is not None) else ""
            rw = vfm.horizontalAdvance(right) + 2 * k
            sw = (sfm.horizontalAdvance(sub) + 8 * k) if sub else 0.0
            p.setFont(value_font)
            p.setPen(QPen(qc(color if value is not None else with_alpha(pal.dim, 220))))
            p.drawText(QRectF(line.right() - rw, line.top(), rw, line.height()),
                       Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight, right)
            bar_left = line.left() + 10 * k + label_w + 6 * k
            bar_right = line.right() - rw - sw - 6 * k
            if sub and bar_right - bar_left > -2 * k:
                p.setFont(sub_font)
                p.setPen(QPen(qc(with_alpha(pal.dim, 200))))
                p.drawText(QRectF(line.right() - rw - sw, line.top(), sw - 4 * k, line.height()),
                           Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight, sub)
            if value is not None and bar_right - bar_left >= 22 * k:
                bar = QRectF(bar_left, line.center().y() - 1.6 * k, bar_right - bar_left, 3.2 * k)
                if local:
                    track = QPainterPath()
                    track.addRoundedRect(bar, bar.height() / 2, bar.height() / 2)
                    p.fillPath(track, qc(pal.track))
                    fill = QPainterPath()
                    fw = max(bar.height(), bar.width() * max(0.0, min(1.0, value / 100.0)))
                    fill.addRoundedRect(QRectF(bar.left(), bar.top(), fw, bar.height()), bar.height() / 2, bar.height() / 2)
                    p.fillPath(fill, qc(with_alpha(pal.accent, 225)))
                else:
                    self._paint_bar(p, bar, value)
            y += ROW_H * k
        return y + 1 * k

    def set_activity(self, busy: bool, note: str = "", retry_in: Optional[float] = None) -> None:
        """Shown in the header (or on the status dot in the slim layout), so a refresh
        is never silent: spinning ring + "refreshing..." while busy, the reason otherwise."""
        changed = (busy, note, None if retry_in is None else int(retry_in)) != \
                  (self.busy, self.note, None if self.retry_in is None else int(self.retry_in))
        self.busy, self.note, self.retry_in = busy, note, retry_in
        if changed or busy:
            self.update()

    def _paint_status_dot(self, p: QPainter, rect: QRectF, color) -> None:
        """Status dot; while a refresh is running it becomes a spinning ring."""
        if not self.busy:
            p.setPen(Qt.PenStyle.NoPen)
            p.setBrush(qc(color))
            p.drawEllipse(rect)
            return
        pal = self.palette_
        ring = rect.adjusted(-1.2 * self.k, -1.2 * self.k, 1.2 * self.k, 1.2 * self.k)
        width = max(1.6, 2.0 * self.k)
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.setPen(QPen(qc(with_alpha(pal.dim, 70)), width))
        p.drawEllipse(ring)
        pen = QPen(qc(pal.accent), width, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)
        p.setPen(pen)
        start = int((time.time() * 360.0 * 1.4) % 360.0)
        p.drawArc(ring, -start * 16, -110 * 16)

    def _activity_text(self) -> Tuple[str, Optional[tuple]]:
        """(text, color) for the header's right side, or ("", None) for the normal age."""
        pal = self.palette_
        if self.busy:
            dots = "." * (1 + int(time.time() * 2.5) % 3)
            return tr("panel.refreshing") + dots, pal.accent
        if self.note:
            if self.retry_in is not None:
                return "! " + tr("panel.retry_in", int(math.ceil(self.retry_in))), pal.warn
            return "", None
        return "", None

    # ------------------------------------------------------------- backups

    def set_backup(self, status: Optional[bk.BackupStatus], expected: bool) -> None:
        self.backup, self.backup_expected = status, expected
        if self._backup_on() != self._backup_shown:
            self._relayout()
        self.update()

    def _backup_keys(self) -> List[str]:
        return [k for k in bk.KEYS if self.s[f"backup_show_{k}"]]

    def _backup_on(self) -> bool:
        return bool(self.s["backup_enabled"]) and self.backup_expected and bool(self._backup_keys())

    def _backup_hit(self, pos) -> Optional[str]:
        pt = QPointF(pos)
        for rect, key in self._backup_hits:
            if rect.contains(pt):
                return key
        return None

    def _model_on(self) -> bool:
        return bool(self.s["show_model"]) and self.metrics.has_model

    def _model_scale(self) -> float:
        """Size of the model gauge relative to the other two (clamped)."""
        try:
            return max(0.5, min(2.0, float(self.s["model_scale"])))
        except (TypeError, ValueError):
            return 1.0

    def _order(self) -> list:
        """Configured gauge order; unknown/missing ids are appended in default order."""
        raw = str(self.s["gauge_order"] or "")
        ids = [x.strip() for x in raw.split(",") if x.strip() in GAUGE_IDS]
        for gid in GAUGE_IDS:
            if gid not in ids:
                ids.append(gid)
        return ids

    def _gauge_items(self, short: bool = False) -> list:
        """Visible gauges in the configured order as (id, label, gauge, hourly, scale)."""
        m = self.metrics
        items = []
        for gid in self._order():
            if gid == "fh" and self.s["show_five_hour"]:
                items.append(("fh", tr("panel.five_hour_short") if short else tr("panel.five_hour"),
                              m.five_hour, True, 1.0))
            elif gid == "mo" and self._model_on():
                name = m.model_name.upper()
                items.append(("mo", name if short else tr("panel.model", name),
                              m.model, False, self._model_scale()))
            elif gid == "sd" and self.s["show_weekly"]:
                items.append(("sd", tr("panel.week_short") if short else tr("panel.weekly"),
                              m.weekly, False, 1.0))
        return items

    # ------------------------------------------------------------- sizing

    @property
    def k(self) -> float:
        return float(self.s["scale"])

    def _relayout(self) -> None:
        k = self.k
        layout = self.s["layout"]
        # each gauge takes 1 "unit" of space; the model gauge takes model_scale units
        model_on = bool(getattr(self, "_model_shown", False))
        ms = self._model_scale() if model_on else 1.0
        units = float(bool(self.s["show_five_hour"])) + float(bool(self.s["show_weekly"]))
        units += ms if model_on else 0.0
        units = max(1.0, units)

        if layout == "compact":
            w = 128 + 140 * units
            h = 46
        elif layout == "ring":
            w = 92 + 104 * units
            h = 46 + 96 * max(1.0, ms) + (26 if self.s["show_spark"] else 0)
        else:  # postit
            w = 300
            h = 44 + units * 52 + (24 if self.s["show_spark"] else 0)
        self._rows_shown = len(self.detail_rows()) if layout != "compact" else 0
        if self._rows_shown:
            h += self._rows_shown * ROW_H + 8
        self._backup_shown = self._backup_on()
        if self._backup_shown:
            h += STRIP_H
        else:
            self._backup_hits = []
        self.setFixedSize(int(w * k) + 2 * SHADOW_MARGIN, int(h * k) + 2 * SHADOW_MARGIN)

    # ------------------------------------------------------------- interaction

    def mousePressEvent(self, e) -> None:
        if e.button() != Qt.MouseButton.LeftButton:
            return
        self._press_global = e.globalPosition().toPoint()
        self._press_key = self._backup_hit(e.position())
        self._dragging = False
        if not self.s["locked"]:
            self._drag_offset = self._press_global - self.frameGeometry().topLeft()
        e.accept()

    def mouseMoveEvent(self, e) -> None:
        if self._drag_offset is not None and e.buttons() & Qt.MouseButton.LeftButton:
            gp = e.globalPosition().toPoint()
            # a few pixels of jitter is still a click (so a lamp click does not nudge the panel)
            if not self._dragging and self._press_global is not None \
                    and (gp - self._press_global).manhattanLength() < 4:
                return
            self._dragging = True
            self.move(gp - self._drag_offset)
            e.accept()
            return
        if not e.buttons():
            self._update_hover(e)

    def mouseReleaseEvent(self, e) -> None:
        if e.button() != Qt.MouseButton.LeftButton:
            return
        was_drag = self._dragging
        self._drag_offset = None
        self._dragging = False
        if was_drag:
            if self.s["snap_edges"]:
                self._snap()
            self.s["pos_x"], self.s["pos_y"] = self.x(), self.y()
            self.s.save()
        elif self._press_key and self._press_key == self._backup_hit(e.position()):
            self.backupClicked.emit(self._press_key)
        self._press_key = None
        e.accept()

    def _status_tooltip(self) -> str:
        m = self.metrics
        lines = [tr("panel.updated", fmt_age(m.age_s))]
        if self.busy:
            lines.append(tr("panel.refreshing") + "...")
        if self.note:
            lines.append(self.note)
            if self.retry_in is not None:
                lines.append(tr("panel.retry_in", int(math.ceil(self.retry_in))))
        return "\n".join(lines)

    def _update_hover(self, e) -> None:
        over_age = self.s["layout"] != "compact" and self._age_rect.contains(QPointF(e.position()))
        if over_age != self._hover_age:
            self._hover_age = over_age
            if over_age:
                QToolTip.showText(e.globalPosition().toPoint(), self._status_tooltip(), self)
        over_badge = self._badge_rect.contains(QPointF(e.position()))
        if over_badge != self._hover_badge:
            self._hover_badge = over_badge
            if over_badge:
                QToolTip.showText(e.globalPosition().toPoint(), self._profile_tooltip(), self)
        key = self._backup_hit(e.position())
        if key == self._hover_key:
            return
        self._hover_key = key
        if key:
            self.setCursor(Qt.CursorShape.PointingHandCursor)
            QToolTip.showText(e.globalPosition().toPoint(), tooltip_text(key, self.backup, self.s), self)
        else:
            self.unsetCursor()
            QToolTip.hideText()

    def _snap(self) -> None:
        scr = self.screen()
        if scr is None:
            return
        a = scr.availableGeometry()
        g = self.frameGeometry()
        thr, pad = 28, 0
        x, y = g.x(), g.y()
        if abs(g.left() - a.left()) < thr:
            x = a.left() - SHADOW_MARGIN + pad
        elif abs(g.right() - a.right()) < thr:
            x = a.right() - g.width() + SHADOW_MARGIN + 1 - pad
        if abs(g.top() - a.top()) < thr:
            y = a.top() - SHADOW_MARGIN + pad
        elif abs(g.bottom() - a.bottom()) < thr:
            y = a.bottom() - g.height() + SHADOW_MARGIN + 1 - pad
        self.move(x, y)

    def mouseDoubleClickEvent(self, e) -> None:
        if e.button() == Qt.MouseButton.LeftButton and not self._backup_hit(e.position()):
            self.doubleClicked.emit()

    def contextMenuEvent(self, e) -> None:
        self.menuRequested.emit(e.globalPos())

    def wheelEvent(self, e) -> None:
        if e.modifiers() & Qt.KeyboardModifier.ControlModifier:
            step = 0.05 if e.angleDelta().y() > 0 else -0.05
            self.s["scale"] = round(max(0.7, min(2.0, self.k + step)), 2)
            self._relayout()
            self.s.save()
            self.update()
            e.accept()

    def enterEvent(self, e) -> None:
        self._hover = True
        self.update()

    def leaveEvent(self, e) -> None:
        self._hover = False
        if self._hover_key:
            self._hover_key = None
            self.unsetCursor()
        self.update()

    # ---------------------------------------------------------------- drawing

    def paintEvent(self, _e) -> None:
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        p.setRenderHint(QPainter.RenderHint.TextAntialiasing, True)

        k = self.k
        pal = self.palette_
        body = QRectF(self.rect().adjusted(SHADOW_MARGIN, SHADOW_MARGIN, -SHADOW_MARGIN, -SHADOW_MARGIN))
        radius = 18 * k if self.s["layout"] != "compact" else 14 * k

        self._paint_shadow(p, body, radius)

        grad = QLinearGradient(body.topLeft(), body.bottomRight())
        grad.setColorAt(0.0, qc(pal.bg2))
        grad.setColorAt(1.0, qc(pal.bg))
        path = QPainterPath()
        path.addRoundedRect(body, radius, radius)
        p.fillPath(path, QBrush(grad))

        pen = QPen(qc(pal.border))
        pen.setWidthF(1.2)
        p.setPen(pen)
        p.drawPath(path)

        # top highlight line
        p.setPen(QPen(qc(with_alpha((255, 255, 255, 255), 26 if pal.dark else 120)), 1.0))
        p.drawLine(body.left() + radius, body.top() + 1.4, body.right() - radius, body.top() + 1.4)

        strip = STRIP_H * k if self._backup_shown else 0.0
        content = body.adjusted(0, 0, 0, -strip)
        inner = content.adjusted(16 * k, 12 * k, -16 * k, -12 * k if not strip else -2 * k)
        if strip:
            self._paint_backup(p, body)
        if not self.metrics.ok:
            self._paint_error(p, inner)
            return

        layout = self.s["layout"]
        if layout == "compact":
            self._paint_compact(p, content.adjusted(12 * k, 0, -12 * k, 0))
        elif layout == "ring":
            self._paint_rings(p, inner)
        else:
            self._paint_postit(p, inner)

    def _paint_backup(self, p: QPainter, body: QRectF) -> None:
        """A discreet row of traffic-light lamps: OneDrive / Nextcloud / Obsidian."""
        k, pal = self.k, self.palette_
        keys = self._backup_keys()
        if not keys:
            return
        h = STRIP_H * k
        area = QRectF(body.left() + 12 * k, body.bottom() - h, body.width() - 24 * k, h - 3 * k)

        p.setPen(QPen(qc(with_alpha(pal.dim, 40)), 1.0))
        p.drawLine(QPointF(area.left() + 4 * k, area.top()), QPointF(area.right() - 4 * k, area.top()))

        font = _font(6.4 * k, QFont.Weight.DemiBold, 0.3 * k)
        fm = QFontMetrics(font)
        p.setFont(font)
        now = time.time()
        slot = area.width() / len(keys)
        dot = 6.5 * k
        gap = 6.5 * k           # leaves room for the error ring around the lamp
        hits: List[Tuple[QRectF, str]] = []

        for i, key in enumerate(keys):
            item = self.backup.items.get(key) if self.backup else None
            level = level_of(self.backup, key, self.s, now)
            if self.backup is not None and (self.backup.error or not self.backup.root_found):
                level = "red"
            label = self._backup_label(key, item, now)
            cell = QRectF(area.left() + i * slot, area.top() + 1 * k, slot, area.height())
            room = slot - dot - gap - 6 * k
            if label and fm.horizontalAdvance(label) > room:
                label = fm.elidedText(label, Qt.TextElideMode.ElideRight, int(max(0.0, room)))
            tw = fm.horizontalAdvance(label) if label else 0
            total = dot + (gap + tw if label else 0)
            x0 = cell.center().x() - total / 2
            c = QPointF(x0 + dot / 2, cell.center().y())
            color = LAMP[level]

            p.setPen(Qt.PenStyle.NoPen)
            p.setBrush(qc(with_alpha(color, 60)))
            p.drawEllipse(c, dot * 0.85, dot * 0.85)
            p.setBrush(qc(color))
            p.drawEllipse(c, dot / 2, dot / 2)
            state = item.state if item is not None else ""
            if state in ("error", "interrupted", "running"):
                ring = LAMP["red"] if state != "running" else pal.accent
                p.setPen(QPen(qc(ring), max(1.0, 1.1 * k)))
                p.setBrush(Qt.BrushStyle.NoBrush)
                p.drawEllipse(c, dot * 0.88, dot * 0.88)

            if label:
                hover = key == self._hover_key
                p.setPen(QPen(qc(pal.text if hover else with_alpha(pal.dim, 235))))
                p.drawText(QRectF(x0 + dot + gap, cell.top(), tw + 2, cell.height()),
                           Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, label)
            hits.append((cell, key))
        self._backup_hits = hits

    def _backup_label(self, key: str, item, now: float) -> str:
        mode = self.s["backup_label"]
        if mode == "none":
            return ""
        name = tr(f"backup.name.{key}")
        if mode == "name":
            return name
        if self.backup is None:
            return f"{name} …"
        if item is None or item.last_ok is None:
            return f"{name} –"
        return f"{name} {short_age(now - item.last_ok)}"

    # ---- parts

    def _paint_shadow(self, p: QPainter, body: QRectF, radius: float) -> None:
        """A soft drop shadow made of stacked, faint rounded rectangles."""
        pal = self.palette_
        steps = 9
        layer = max(3, int(pal.shadow[3] / (steps * 1.8)))
        drop = 4.0
        for i in range(steps, 0, -1):
            grow = i * (SHADOW_MARGIN - 2) / steps
            rect = body.adjusted(-grow, -grow + drop, grow, grow + drop)
            path = QPainterPath()
            path.addRoundedRect(rect, radius + grow, radius + grow)
            p.fillPath(path, qc(with_alpha(pal.shadow, layer)))

    def _paint_error(self, p: QPainter, r: QRectF) -> None:
        pal = self.palette_
        p.setPen(QPen(qc(pal.danger)))
        p.setFont(_font(9.5 * self.k, QFont.Weight.DemiBold))
        p.drawText(QRectF(r), Qt.AlignmentFlag.AlignCenter | Qt.TextFlag.TextWordWrap,
                   self.metrics.error or tr("panel.no_data"))

    def _paint_header(self, p: QPainter, r: QRectF) -> float:
        k, pal, m = self.k, self.palette_, self.metrics
        dot = QRectF(r.left(), r.top() + 3 * k, 8 * k, 8 * k)
        worst = max(m.five_hour.value, m.weekly.value, m.model.value if self._model_on() else 0.0)
        self._paint_status_dot(p, dot, pal.status(worst, self.s["warn_threshold"], self.s["danger_threshold"]))

        p.setPen(QPen(qc(pal.dim)))
        p.setFont(_font(6.8 * k, QFont.Weight.DemiBold, 1.4 * k))
        p.drawText(QRectF(r.left() + 14 * k, r.top(), r.width() * 0.6, 14 * k),
                   Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, "CLAUDE USAGE")
        tx = r.left() + 14 * k + QFontMetrics(p.font()).horizontalAdvance("CLAUDE USAGE") + 9 * k
        badge_w = self._paint_badge(p, tx, r.top())
        if badge_w:
            tx += badge_w + 7 * k
        if self.update_version:
            # discreet "update available" marker after the title / badge
            p.setPen(QPen(qc(pal.accent)))
            p.setFont(_font(6.6 * k, QFont.Weight.Bold))
            p.drawText(QRectF(tx, r.top(), 60 * k, 14 * k),
                       Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft,
                       "\u2191 " + self.update_version)

        act, act_color = self._activity_text()
        if act or self.s["show_age"]:
            # activity (refreshing / retrying) always shows, even if the age is switched off
            if act:
                text, color = act, act_color
            else:
                failing = bool(self.note)
                text = ("! " if (m.stale or failing) else "") + tr("panel.updated", fmt_age(m.age_s))
                color = pal.danger if m.stale else (pal.warn if failing else with_alpha(pal.dim, 190))
            p.setPen(QPen(qc(color)))
            p.setFont(_font(6.6 * k, QFont.Weight.DemiBold if act else QFont.Weight.Normal))
            self._age_rect = QRectF(r.left() + r.width() * 0.55, r.top() - 2 * k, r.width() * 0.45, 18 * k)
            p.drawText(QRectF(r.left() + r.width() * 0.4, r.top(), r.width() * 0.6, 14 * k),
                       Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight, text)
        return r.top() + 20 * k

    def _paint_postit(self, p: QPainter, r: QRectF) -> None:
        k = self.k
        y = self._paint_header(p, r)
        for _gid, label, g, hourly, sc in self._gauge_items():
            y = self._paint_block(p, QRectF(r.left(), y, r.width(), 60 * k * sc), label, g, hourly, sc)
        y = self._paint_rows(p, QRectF(r.left(), y, r.width(), 0))
        if self.s["show_spark"]:
            g = self.metrics.weekly if self.s["show_weekly"] else self.metrics.five_hour
            self._paint_spark(p, QRectF(r.left(), y + 2 * k, r.width(), 22 * k), g)

    def _paint_block(self, p: QPainter, r: QRectF, title: str, g: Gauge, hourly: bool,
                     sc: float = 1.0) -> float:
        k, pal = self.k * sc, self.palette_      # sc: per-gauge size factor
        warn, danger = self.s["warn_threshold"], self.s["danger_threshold"]

        p.setPen(QPen(qc(pal.dim)))
        p.setFont(_font(7.0 * k, QFont.Weight.DemiBold, 1.0 * k))
        p.drawText(QRectF(r.left(), r.top(), r.width() * 0.6, 18 * k),
                   Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, title)

        p.setPen(QPen(qc(pal.status(g.value, warn, danger))))
        p.setFont(_font(15.0 * k, QFont.Weight.Bold))
        p.drawText(QRectF(r.left() + r.width() * 0.4, r.top() - 3 * k, r.width() * 0.6, 24 * k),
                   Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight, f"{g.value:.0f}%")

        self._paint_bar(p, QRectF(r.left(), r.top() + 22 * k, r.width(), 8 * k), g.value)

        parts = []
        if self.s["show_reset"] and g.reset_in_ms is not None:
            prefix = "" if g.reset_certain else "~"
            parts.append(tr("panel.reset", prefix + fmt_delta(g.reset_in_ms)))
        if self.s["show_burn"]:
            if hourly and g.burn > 0.2:
                parts.append(tr("panel.per_hour", f"{g.burn:.0f}"))
            elif not hourly and g.burn > 0.02:
                parts.append(tr("panel.per_day", f"{g.burn * 24:.0f}"))
        if not hourly and g.pace is not None and abs(g.pace) >= 3:
            parts.append(tr("panel.pace", ("+" if g.pace > 0 else "") + f"{g.pace:.0f}%"))
        elif hourly and g.eta_ms is not None and g.value < 100:
            parts.append(tr("panel.full_in", fmt_delta(g.eta_ms)))

        if parts:
            p.setPen(QPen(qc(with_alpha(pal.dim, 210))))
            p.setFont(_font(6.6 * k))
            p.drawText(QRectF(r.left(), r.top() + 32 * k, r.width(), 14 * k),
                       Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, " · ".join(parts))
        return r.top() + 52 * k

    def _paint_bar(self, p: QPainter, r: QRectF, value: float) -> None:
        pal = self.palette_
        rad = r.height() / 2
        track = QPainterPath()
        track.addRoundedRect(r, rad, rad)
        p.fillPath(track, qc(pal.track))

        frac = max(0.0, min(1.0, value / 100.0))
        if frac > 0.001:
            w = max(r.height(), r.width() * frac)
            fr = QRectF(r.left(), r.top(), w, r.height())
            c0, c1 = pal.gauge_colors(value, self.s["warn_threshold"], self.s["danger_threshold"])
            grad = QLinearGradient(fr.topLeft(), fr.topRight())
            grad.setColorAt(0.0, qc(c0))
            grad.setColorAt(1.0, qc(c1))
            fill = QPainterPath()
            fill.addRoundedRect(fr, rad, rad)
            p.fillPath(fill, QBrush(grad))

        # pace marks on the weekly bar (where you'd be at even consumption)
        p.setPen(QPen(qc(with_alpha(pal.text, 38)), 1.0))
        for q in (0.25, 0.5, 0.75):
            x = r.left() + r.width() * q
            p.drawLine(QPointF(x, r.top() + 1.5), QPointF(x, r.bottom() - 1.5))

    def _paint_spark(self, p: QPainter, r: QRectF, g: Gauge) -> None:
        pal = self.palette_
        pts = g.spark
        if len(pts) < 2:
            return
        top = max(10.0, max(pts))
        path = QPainterPath()
        area = QPainterPath()
        n = len(pts)
        for i, v in enumerate(pts):
            x = r.left() + r.width() * (i / (n - 1))
            y = r.bottom() - (r.height() - 2) * (v / top)
            if i == 0:
                path.moveTo(x, y)
                area.moveTo(x, r.bottom())
                area.lineTo(x, y)
            else:
                path.lineTo(x, y)
                area.lineTo(x, y)
        area.lineTo(r.right(), r.bottom())
        area.closeSubpath()

        grad = QLinearGradient(r.topLeft(), r.bottomLeft())
        grad.setColorAt(0.0, qc(with_alpha(pal.accent, 90)))
        grad.setColorAt(1.0, qc(with_alpha(pal.accent, 0)))
        p.fillPath(area, QBrush(grad))
        p.setPen(QPen(qc(with_alpha(pal.accent, 220)), 1.4 * self.k))
        p.drawPath(path)

    def _paint_rings(self, p: QPainter, r: QRectF) -> None:
        k = self.k
        y = self._paint_header(p, r)
        items = self._gauge_items(short=True)
        if not items:
            return
        total = sum(it[4] for it in items)
        row_h = 96 * k * max(1.0, max(it[4] for it in items))
        x = r.left()
        for _gid, label, g, _hourly, sc in items:
            w = r.width() * sc / total          # slot width proportional to the gauge size
            self._paint_ring(p, QRectF(x, y, w, row_h), label, g, sc)
            x += w
        y2 = self._paint_rows(p, QRectF(r.left(), y + row_h + 1 * k, r.width(), 0))
        if self.s["show_spark"]:
            y2 = max(y2, y + row_h + 4 * k)
            self._paint_spark(p, QRectF(r.left(), y2, r.width(), 20 * k), items[-1][2])

    def _paint_ring(self, p: QPainter, r: QRectF, label: str, g: Gauge, sc: float = 1.0) -> None:
        k, pal = self.k * sc, self.palette_      # sc: per-gauge size factor
        d = min(r.width() - 12 * k, r.height() - 22 * k, 74 * k)
        top = r.top() + max(0.0, (r.height() - 22 * k - d) / 2)   # centre smaller rings vertically
        box = QRectF(r.center().x() - d / 2, top, d, d)
        thick = max(5.0, 7 * k)

        pen = QPen(qc(pal.track), thick, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)
        p.setPen(pen)
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.drawArc(box.adjusted(thick, thick, -thick, -thick), 90 * 16, -360 * 16)

        c0, c1 = pal.gauge_colors(g.value, self.s["warn_threshold"], self.s["danger_threshold"])
        pen.setColor(qc(c1))
        p.setPen(pen)
        span = int(-360 * 16 * max(0.0, min(1.0, g.value / 100.0)))
        p.drawArc(box.adjusted(thick, thick, -thick, -thick), 90 * 16, span)

        p.setPen(QPen(qc(pal.text)))
        p.setFont(_font(13 * k, QFont.Weight.Bold))
        p.drawText(box, Qt.AlignmentFlag.AlignCenter, f"{g.value:.0f}%")

        sub = fmt_delta(g.reset_in_ms) if (self.s["show_reset"] and g.reset_in_ms is not None) else ""
        p.setPen(QPen(qc(pal.dim)))
        p.setFont(_font(6.6 * k, QFont.Weight.DemiBold, 1.0 * k))
        p.drawText(QRectF(r.left(), box.bottom() + 2 * k, r.width(), 12 * k),
                   Qt.AlignmentFlag.AlignCenter, label + (f"  ·  {sub}" if sub else ""))

    def _paint_compact(self, p: QPainter, r: QRectF) -> None:
        k, pal = self.k, self.palette_
        items = self._gauge_items(short=True)
        if not items:
            return

        x = r.left()
        dot_color = pal.status(max(it[2].value for it in items),
                               self.s["warn_threshold"], self.s["danger_threshold"])
        if self.note and not self.busy:
            dot_color = pal.warn        # the last fetch failed - the numbers may be old
        self._paint_status_dot(p, QRectF(x, r.center().y() - 4 * k, 8 * k, 8 * k), dot_color)
        x += 16 * k

        total = sum(it[4] for it in items)
        avail = r.right() - x
        for gid, label, g, _hourly, sc in items:
            if gid == "mo":
                label = label[:6]
            kk = k * sc                          # per-gauge size factor
            seg = avail * sc / total             # segment width proportional to the gauge size
            label_font = _font(6.8 * kk, QFont.Weight.DemiBold, 0.8 * kk)
            fm = QFontMetrics(label_font)
            # measure the label so longer names (e.g. "FABLE") never get clipped
            lw = max(26 * kk, fm.horizontalAdvance(label) + 6 * kk)
            p.setPen(QPen(qc(pal.dim)))
            p.setFont(label_font)
            p.drawText(QRectF(x, r.top(), lw, r.height()),
                       Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, label)
            p.setPen(QPen(qc(pal.status(g.value, self.s["warn_threshold"], self.s["danger_threshold"]))))
            p.setFont(_font(10 * kk, QFont.Weight.Bold))
            p.drawText(QRectF(x + lw, r.top(), 38 * kk, r.height()),
                       Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, f"{g.value:.0f}%")
            bar_x = x + lw + 40 * kk
            self._paint_bar(p, QRectF(bar_x, r.center().y() - 3 * kk, max(20 * k, x + seg - 12 * k - bar_x), 6 * kk),
                            g.value)
            x += seg
