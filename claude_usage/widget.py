"""A lebegő ("post-it") panel – teljesen saját rajzolású, keret nélküli ablak."""

from __future__ import annotations

from typing import Optional

from PySide6.QtCore import QPoint, QPointF, QRectF, Qt, Signal
from PySide6.QtGui import (
    QBrush,
    QFont,
    QGuiApplication,
    QLinearGradient,
    QPainter,
    QPainterPath,
    QPen,
)
from PySide6.QtWidgets import QWidget

from .datasource import Gauge, Metrics, fmt_age, fmt_delta
from .i18n import tr
from .settings import Settings
from .theme import Palette, qc, with_alpha

SHADOW_MARGIN = 18


def _font(size: float, weight: QFont.Weight = QFont.Weight.Normal, spacing: float = 0.0) -> QFont:
    f = QFont("Segoe UI Variable Display")
    if not f.exactMatch():
        f = QFont("Segoe UI")
    f.setPointSizeF(max(5.0, size))
    f.setWeight(weight)
    if spacing:
        f.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, spacing)
    return f


class UsageWidget(QWidget):
    menuRequested = Signal(QPoint)
    doubleClicked = Signal()

    def __init__(self, settings: Settings):
        super().__init__(None)
        self.s = settings
        self.metrics: Metrics = Metrics()
        self.palette_: Palette = Palette(self.s["theme"], self.s["accent"])
        self._drag_offset: Optional[QPoint] = None
        self._hover = False

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_AlwaysShowToolTips, True)
        self.setMouseTracking(True)
        # Az árnyékot kézzel rajzoljuk: a QGraphicsDropShadowEffect áttetsző,
        # keret nélküli ablakon gyorsítótárazza a képet, és az update() után is
        # a régi tartalom maradt a képernyőn.
        self.apply_settings()

    # ------------------------------------------------------------- beállítás

    def apply_settings(self) -> None:
        self.palette_ = Palette(self.s["theme"], self.s["accent"])

        flags = Qt.WindowType.FramelessWindowHint
        flags |= Qt.WindowType.Window if self.s["show_in_taskbar"] else Qt.WindowType.Tool
        if self.s["always_on_top"]:
            flags |= Qt.WindowType.WindowStaysOnTopHint
        if self.s["click_through"]:
            flags |= Qt.WindowType.WindowTransparentForInput
        was_visible = self.isVisible()
        # A setWindowFlags elrejti az ablakot, ezért csak tényleges változáskor hívjuk
        # (különben minden csúszkamozgatásnál villogna a panel).
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
            # Nincs mentett pozíció, vagy az a monitor már nem létezik.
            self._default_position()
        if flags_changed and (was_visible or self.s["visible"]):
            self.show()
        self.update()

    def _on_any_screen(self, x: int, y: int) -> bool:
        """A panel közepe rajta van-e még valamelyik csatlakoztatott monitoron?"""
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
        self.update()

    # ------------------------------------------------------------- méretezés

    @property
    def k(self) -> float:
        return float(self.s["scale"])

    def _relayout(self) -> None:
        k = self.k
        layout = self.s["layout"]
        gauges = int(bool(self.s["show_five_hour"])) + int(bool(self.s["show_weekly"]))
        gauges = max(1, gauges)

        if layout == "compact":
            w = 128 + 132 * gauges
            h = 46
        elif layout == "ring":
            w = 92 + 104 * gauges
            h = 142 + (26 if self.s["show_spark"] else 0)
        else:  # postit
            w = 300
            h = 44 + gauges * 52 + (24 if self.s["show_spark"] else 0)
        self.setFixedSize(int(w * k) + 2 * SHADOW_MARGIN, int(h * k) + 2 * SHADOW_MARGIN)

    # ------------------------------------------------------------- interakció

    def mousePressEvent(self, e) -> None:
        if e.button() == Qt.MouseButton.LeftButton and not self.s["locked"]:
            self._drag_offset = e.globalPosition().toPoint() - self.frameGeometry().topLeft()
            e.accept()

    def mouseMoveEvent(self, e) -> None:
        if self._drag_offset is not None and e.buttons() & Qt.MouseButton.LeftButton:
            self.move(e.globalPosition().toPoint() - self._drag_offset)
            e.accept()

    def mouseReleaseEvent(self, e) -> None:
        if self._drag_offset is not None:
            self._drag_offset = None
            if self.s["snap_edges"]:
                self._snap()
            self.s["pos_x"], self.s["pos_y"] = self.x(), self.y()
            self.s.save()
            e.accept()

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
        if e.button() == Qt.MouseButton.LeftButton:
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
        self.update()

    # ---------------------------------------------------------------- rajzolás

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

        # felső fényvonal
        p.setPen(QPen(qc(with_alpha((255, 255, 255, 255), 26 if pal.dark else 120)), 1.0))
        p.drawLine(body.left() + radius, body.top() + 1.4, body.right() - radius, body.top() + 1.4)

        inner = body.adjusted(16 * k, 12 * k, -16 * k, -12 * k)
        if not self.metrics.ok:
            self._paint_error(p, inner)
            return

        layout = self.s["layout"]
        if layout == "compact":
            self._paint_compact(p, body.adjusted(12 * k, 0, -12 * k, 0))
        elif layout == "ring":
            self._paint_rings(p, inner)
        else:
            self._paint_postit(p, inner)

    # ---- részek

    def _paint_shadow(self, p: QPainter, body: QRectF, radius: float) -> None:
        """Lágy vetett árnyék egymásra rétegzett, halvány lekerekített téglalapokból."""
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
        worst = max(m.five_hour.value, m.weekly.value)
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(qc(pal.status(worst, self.s["warn_threshold"], self.s["danger_threshold"])))
        p.drawEllipse(dot)

        p.setPen(QPen(qc(pal.dim)))
        p.setFont(_font(6.8 * k, QFont.Weight.DemiBold, 1.4 * k))
        p.drawText(QRectF(r.left() + 14 * k, r.top(), r.width() * 0.6, 14 * k),
                   Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, "CLAUDE USAGE")

        if self.s["show_age"]:
            txt = fmt_age(m.age_s)
            p.setPen(QPen(qc(pal.danger if m.stale else with_alpha(pal.dim, 190))))
            p.setFont(_font(6.6 * k, QFont.Weight.Normal))
            p.drawText(QRectF(r.left() + r.width() * 0.5, r.top(), r.width() * 0.5, 14 * k),
                       Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight,
                       ("! " if m.stale else "") + tr("panel.updated", txt))
        return r.top() + 20 * k

    def _paint_postit(self, p: QPainter, r: QRectF) -> None:
        k = self.k
        y = self._paint_header(p, r)
        if self.s["show_five_hour"]:
            y = self._paint_block(p, QRectF(r.left(), y, r.width(), 60 * k), tr("panel.five_hour"),
                                  self.metrics.five_hour, hourly=True)
        if self.s["show_weekly"]:
            y = self._paint_block(p, QRectF(r.left(), y, r.width(), 60 * k), tr("panel.weekly"),
                                  self.metrics.weekly, hourly=False)
        if self.s["show_spark"]:
            g = self.metrics.weekly if self.s["show_weekly"] else self.metrics.five_hour
            self._paint_spark(p, QRectF(r.left(), y + 2 * k, r.width(), 22 * k), g)

    def _paint_block(self, p: QPainter, r: QRectF, title: str, g: Gauge, hourly: bool) -> float:
        k, pal = self.k, self.palette_
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

        # ütem-jelölés a heti sávon (hol tartanál egyenletes fogyasztással)
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
        items = []
        if self.s["show_five_hour"]:
            items.append((tr("panel.five_hour_short"), self.metrics.five_hour))
        if self.s["show_weekly"]:
            items.append((tr("panel.week_short"), self.metrics.weekly))
        if not items:
            return
        w = r.width() / len(items)
        for i, (label, g) in enumerate(items):
            self._paint_ring(p, QRectF(r.left() + i * w, y, w, 96 * k), label, g)
        if self.s["show_spark"]:
            self._paint_spark(p, QRectF(r.left(), y + 100 * k, r.width(), 20 * k), items[-1][1])

    def _paint_ring(self, p: QPainter, r: QRectF, label: str, g: Gauge) -> None:
        k, pal = self.k, self.palette_
        d = min(r.width() - 12 * k, r.height() - 22 * k)
        box = QRectF(r.center().x() - d / 2, r.top(), d, d)
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
        items = []
        if self.s["show_five_hour"]:
            items.append((tr("panel.five_hour_short"), self.metrics.five_hour))
        if self.s["show_weekly"]:
            items.append((tr("panel.week_short"), self.metrics.weekly))
        if not items:
            return

        x = r.left()
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(qc(pal.status(max(g.value for _, g in items),
                                self.s["warn_threshold"], self.s["danger_threshold"])))
        p.drawEllipse(QRectF(x, r.center().y() - 4 * k, 8 * k, 8 * k))
        x += 16 * k

        seg = (r.right() - x) / len(items)
        for label, g in items:
            p.setPen(QPen(qc(pal.dim)))
            p.setFont(_font(6.8 * k, QFont.Weight.DemiBold, 0.8 * k))
            p.drawText(QRectF(x, r.top(), 26 * k, r.height()),
                       Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, label)
            p.setPen(QPen(qc(pal.status(g.value, self.s["warn_threshold"], self.s["danger_threshold"]))))
            p.setFont(_font(10 * k, QFont.Weight.Bold))
            p.drawText(QRectF(x + 26 * k, r.top(), 38 * k, r.height()),
                       Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, f"{g.value:.0f}%")
            self._paint_bar(p, QRectF(x + 66 * k, r.center().y() - 3 * k, seg - 78 * k, 6 * k), g.value)
            x += seg
