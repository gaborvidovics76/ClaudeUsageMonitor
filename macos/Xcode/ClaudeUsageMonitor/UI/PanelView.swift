// The floating ("post-it") panel - a fully custom-drawn view (port of claude_usage/widget.py).
// Everything is drawn in a flipped coordinate system, so the geometry is the same as on Windows.

import AppKit

let shadowMargin: CGFloat = 18
let rowHeight: CGFloat = 15          // one line of the small list under the gauges (unscaled)

/// Plan badge: gradient start / end per plan.
private let planStyle: [String: (RGBA, RGBA)] = [
    "pro": (RGBA(217, 119, 87), RGBA(242, 166, 90)),
    "max": (RGBA(124, 92, 255), RGBA(230, 107, 214)),
    "team": (RGBA(45, 140, 255), RGBA(38, 198, 190)),
    "enterprise": (RGBA(84, 96, 120), RGBA(150, 162, 186)),
]

/// Visible lines of the small list: (id, label, percent or nil, right text, reset ms or nil).
struct PanelRow {
    var id: String
    var label: String
    var value: Double?
    var right: String
    var resetMs: Int64?
}

final class PanelView: NSView {
    let settings: Settings
    var metrics = Metrics()
    var palette: Palette
    var localModels: [ModelShare] = []

    // activity feedback: a fetch is running / the last one failed
    var busy = false
    var note = ""
    var retryIn: Double? = nil

    // callbacks to the controller
    var onMenu: ((NSPoint) -> Void)?
    var onDoubleClick: (() -> Void)?
    var onFeedback: (() -> Void)?
    var onMoved: (() -> Void)?
    var onScaleChanged: (() -> Void)?

    private var dragOffset: NSPoint? = nil
    private var pressLocation: NSPoint? = nil
    private var pressFeedback = false
    private var dragging = false
    private var hovering = false
    private var hoverFeedback = false
    private var ageRect = CGRect.zero
    private var badgeRect = CGRect.zero
    private var fbRect = CGRect.zero
    private var rowsShown = 0
    private var modelShown = false
    private var trackingArea: NSTrackingArea?

    init(settings: Settings) {
        self.settings = settings
        self.palette = Palette(theme: settings.theme, accentHex: settings.accent)
        super.init(frame: .zero)
        wantsLayer = true
        layer?.backgroundColor = NSColor.clear.cgColor
        relayout()
    }

    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    override var isFlipped: Bool { true }
    override var acceptsFirstResponder: Bool { false }
    override func acceptsFirstMouse(for event: NSEvent?) -> Bool { true }

    // MARK: - setup

    func applySettings() {
        palette = Palette(theme: settings.theme, accentHex: settings.accent)
        relayout()
        needsDisplay = true
    }

    func setMetrics(_ m: Metrics) {
        metrics = m
        let shown = settings.showModel && m.hasModel
        if shown != modelShown || detailRows().count != rowsShown {
            modelShown = shown
            relayout()
        }
        needsDisplay = true
    }

    func setLocalModels(_ shares: [ModelShare]) {
        localModels = shares
        if detailRows().count != rowsShown { relayout() }
        needsDisplay = true
    }

    func setActivity(busy: Bool, note: String, retryIn: Double?) {
        let changed = busy != self.busy || note != self.note || Int(retryIn ?? -1) != Int(self.retryIn ?? -1)
        self.busy = busy; self.note = note; self.retryIn = retryIn
        if changed || busy { needsDisplay = true }
    }

    var k: CGFloat { CGFloat(settings.scale) }

    private var modelOn: Bool { settings.showModel && metrics.hasModel }
    private var modelScale: CGFloat { CGFloat(settings.clampedModelScale) }

    // MARK: - details

    private static func shortTokens(_ n: Int) -> String {
        if n >= 1_000_000 { return String(format: "%.1fM", Double(n) / 1_000_000) }
        if n >= 1_000 { return String(format: "%.0fk", Double(n) / 1_000) }
        return String(n)
    }

    func detailRows() -> [PanelRow] {
        guard metrics.ok else { return [] }
        return serverRows() + localRows()
    }

    private func serverRows() -> [PanelRow] {
        let m = metrics, s = settings
        let big = modelOn ? "model:\(m.modelName)".lowercased() : ""
        var out: [PanelRow] = []
        for row in m.rows {
            if s.isHidden(row.id) { continue }
            if row.category == "model" {
                if !s.showModelList || row.id.lowercased() == big { continue }
            } else if !s.showSurfaces { continue }
            out.append(PanelRow(id: row.id, label: row.displayLabel, value: row.value, right: "\(pct0(row.value))%", resetMs: row.resetInMs))
        }
        if let ex = m.extra, s.showExtraUsage, !s.isHidden("extra") {
            if ex.enabled {
                let limit = ex.monthlyLimit.map { num($0, 2) } ?? tr("detail.unlimited")
                out.append(PanelRow(id: "extra", label: tr("detail.extra"), value: ex.utilization,
                                    right: "\(num(ex.used ?? 0, 2)) / \(limit) \(ex.currency)", resetMs: nil))
            } else {
                out.append(PanelRow(id: "extra", label: tr("detail.extra"), value: nil, right: tr("detail.off"), resetMs: nil))
            }
        }
        return out
    }

    private func localRows() -> [PanelRow] {
        guard settings.showLocalModels else { return [] }
        let rows = localModels.filter { !settings.isHidden("local:" + $0.name) && $0.share >= 0.5 }.map {
            PanelRow(id: "local:" + $0.name, label: $0.name, value: $0.share,
                     right: "\(pct0($0.share))%  \u{b7}  \(PanelView.shortTokens($0.outputTokens))", resetMs: nil)
        }
        if rows.isEmpty { return [] }
        return [PanelRow(id: "@header", label: tr("detail.local_header"), value: nil, right: "", resetMs: nil)] + rows
    }

    private func profileTooltip() -> String {
        guard let pr = metrics.profile else { return "" }
        var lines: [String] = []
        if !pr.name.isEmpty { lines.append(pr.name) }
        var plan = "?"
        if !pr.plan.isEmpty { plan = pr.plan.prefix(1).uppercased() + pr.plan.dropFirst() + (pr.multiplier.isEmpty ? "" : " " + pr.multiplier) }
        lines.append(tr("profile.plan", plan))
        if !pr.tier.isEmpty { lines.append(tr("profile.tier", pr.tier)) }
        if let e = pr.hasExtraUsage { lines.append(tr("profile.extra", e ? tr("detail.on") : tr("detail.off"))) }
        if !pr.createdAt.isEmpty { lines.append(tr("profile.since", String(pr.createdAt.prefix(10)))) }
        return lines.joined(separator: "\n")
    }

    private func statusTooltip() -> String {
        var lines = [tr("panel.updated", fmtAge(metrics.ageSeconds))]
        if busy { lines.append(tr("panel.refreshing") + "...") }
        if !note.isEmpty {
            lines.append(note)
            if let r = retryIn { lines.append(tr("panel.retry_in", Int(ceil(r)))) }
        }
        return lines.joined(separator: "\n")
    }

    /// Visible gauges in the configured order as (id, label, gauge, hourly, scale).
    private func gaugeItems(short: Bool = false) -> [(String, String, Gauge, Bool, CGFloat)] {
        let m = metrics
        var items: [(String, String, Gauge, Bool, CGFloat)] = []
        for gid in settings.orderedGauges {
            if gid == "fh" && settings.showFiveHour {
                items.append(("fh", short ? tr("panel.five_hour_short") : tr("panel.five_hour"), m.fiveHour, true, 1))
            } else if gid == "mo" && modelOn {
                let name = m.modelName.uppercased()
                items.append(("mo", short ? name : tr("panel.model", name), m.model, false, modelScale))
            } else if gid == "sd" && settings.showWeekly {
                items.append(("sd", short ? tr("panel.week_short") : tr("panel.weekly"), m.weekly, false, 1))
            }
        }
        return items
    }

    // MARK: - sizing

    /// The size the panel wants, including the shadow margin.
    func relayout() {
        let k = self.k
        let layout = settings.layout
        let ms = modelShown ? modelScale : 1
        var units = CGFloat(settings.showFiveHour ? 1 : 0) + CGFloat(settings.showWeekly ? 1 : 0)
        units += modelShown ? ms : 0
        units = max(1, units)
        var w: CGFloat, h: CGFloat
        if layout == "compact" {
            w = 128 + 140 * units
            h = 46
        } else if layout == "ring" {
            w = 92 + 104 * units
            h = 46 + 96 * max(1, ms) + (settings.showSpark ? 26 : 0)
        } else {
            w = 300
            h = 44 + units * 52 + (settings.showSpark ? 24 : 0)
        }
        rowsShown = layout != "compact" ? detailRows().count : 0
        if rowsShown > 0 { h += CGFloat(rowsShown) * rowHeight + 8 }
        let size = NSSize(width: floor(w * k) + 2 * shadowMargin, height: floor(h * k) + 2 * shadowMargin)
        if size != frame.size {
            setFrameSize(size)
            onSizeChanged?(size)
        }
        rebuildToolTips()
    }

    var onSizeChanged: ((NSSize) -> Void)?

    // MARK: - interaction

    override func updateTrackingAreas() {
        super.updateTrackingAreas()
        if let t = trackingArea { removeTrackingArea(t) }
        let t = NSTrackingArea(rect: bounds, options: [.mouseEnteredAndExited, .mouseMoved, .activeAlways, .inVisibleRect], owner: self, userInfo: nil)
        addTrackingArea(t)
        trackingArea = t
    }

    override func mouseDown(with event: NSEvent) {
        guard let win = window else { return }
        pressLocation = NSEvent.mouseLocation
        let p = convert(event.locationInWindow, from: nil)
        pressFeedback = fbHit(p)
        dragging = false
        if !settings.locked {
            let m = NSEvent.mouseLocation
            dragOffset = NSPoint(x: m.x - win.frame.origin.x, y: m.y - win.frame.origin.y)
        } else {
            dragOffset = nil
        }
    }

    override func mouseDragged(with event: NSEvent) {
        guard let off = dragOffset, let win = window else { return }
        let m = NSEvent.mouseLocation
        if !dragging, let p = pressLocation, abs(m.x - p.x) + abs(m.y - p.y) < 4 { return }
        dragging = true
        win.setFrameOrigin(NSPoint(x: m.x - off.x, y: m.y - off.y))
    }

    override func mouseUp(with event: NSEvent) {
        let wasDrag = dragging
        dragOffset = nil
        dragging = false
        let p = convert(event.locationInWindow, from: nil)
        if wasDrag {
            if settings.snapEdges { snap() }
            onMoved?()
        } else if event.clickCount == 2 && !fbHit(p) {
            onDoubleClick?()
        } else if pressFeedback && fbHit(p) {
            onFeedback?()
        }
        pressFeedback = false
    }

    override func rightMouseDown(with event: NSEvent) {
        onMenu?(NSEvent.mouseLocation)
    }

    override func scrollWheel(with event: NSEvent) {
        guard event.modifierFlags.contains(.control) || event.modifierFlags.contains(.command) else { return }
        let dy = event.scrollingDeltaY
        if abs(dy) < 0.5 { return }
        let step = dy > 0 ? 0.05 : -0.05
        settings.scale = (max(0.7, min(2.0, settings.scale + step)) * 100).rounded() / 100
        relayout()
        onScaleChanged?()
        needsDisplay = true
    }

    override func mouseEntered(with event: NSEvent) { hovering = true; needsDisplay = true }

    override func mouseExited(with event: NSEvent) {
        hovering = false
        if hoverFeedback { hoverFeedback = false; NSCursor.arrow.set() }
        needsDisplay = true
    }

    override func mouseMoved(with event: NSEvent) {
        let p = convert(event.locationInWindow, from: nil)
        let over = fbHit(p)
        if over != hoverFeedback {
            hoverFeedback = over
            if over { NSCursor.pointingHand.set() } else { NSCursor.arrow.set() }
            needsDisplay = true
        }
    }

    private func fbHit(_ p: CGPoint) -> Bool {
        settings.showFeedbackIcon && !fbRect.isEmpty && fbRect.contains(p)
    }

    /// Snap the window to the nearest screen edges (the shadow margin stays off-screen).
    private func snap() {
        guard let win = window, let scr = win.screen ?? NSScreen.main else { return }
        let a = scr.visibleFrame
        var f = win.frame
        let thr: CGFloat = 28
        let body = f.insetBy(dx: shadowMargin, dy: shadowMargin)
        if abs(body.minX - a.minX) < thr { f.origin.x = a.minX - shadowMargin }
        else if abs(body.maxX - a.maxX) < thr { f.origin.x = a.maxX - f.width + shadowMargin }
        if abs(body.maxY - a.maxY) < thr { f.origin.y = a.maxY - f.height + shadowMargin }
        else if abs(body.minY - a.minY) < thr { f.origin.y = a.minY - shadowMargin }
        win.setFrameOrigin(f.origin)
    }

    // tool tips: the header status text, the plan badge and the message icon
    private func rebuildToolTips() {
        removeAllToolTips()
        if settings.layout != "compact" && !ageRect.isEmpty { addToolTip(ageRect, owner: self, userData: nil) }
        if !badgeRect.isEmpty { addToolTip(badgeRect, owner: self, userData: nil) }
        if !fbRect.isEmpty { addToolTip(fbRect, owner: self, userData: nil) }
    }

    override func view(_ view: NSView, stringForToolTip tag: NSView.ToolTipTag, point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String {
        if fbRect.contains(point) { return tr("fb.title") }
        if badgeRect.contains(point) { return profileTooltip() }
        if ageRect.contains(point) { return statusTooltip() }
        return ""
    }

    // MARK: - drawing

    override func draw(_ dirtyRect: NSRect) {
        let c = Draw.ctx
        c.setAllowsAntialiasing(true)
        c.setShouldAntialias(true)
        let k = self.k
        let pal = palette
        let body = bounds.insetBy(dx: shadowMargin, dy: shadowMargin)
        let radius = settings.layout != "compact" ? 18 * k : 14 * k

        paintShadow(body, radius)

        let path = Draw.roundedPath(body, radius)
        Draw.gradient(path, from: CGPoint(x: body.minX, y: body.minY), to: CGPoint(x: body.maxX, y: body.maxY), pal.bg2, pal.bg)
        Draw.stroke(path, pal.border, width: 1.2)
        // top highlight line
        Draw.line(CGPoint(x: body.minX + radius, y: body.minY + 1.4), CGPoint(x: body.maxX - radius, y: body.minY + 1.4),
                  RGBA(255, 255, 255, pal.dark ? 26 : 120), width: 1)

        let inner = body.adjusted(16 * k, 12 * k, -16 * k, -12 * k)
        let oldAge = ageRect, oldBadge = badgeRect, oldFb = fbRect
        if !metrics.ok {
            paintError(inner)
        } else {
            switch settings.layout {
            case "compact": paintCompact(body.adjusted(12 * k, 0, -12 * k, 0))
            case "ring": paintRings(inner)
            default: paintPostit(inner)
            }
        }
        if oldAge != ageRect || oldBadge != badgeRect || oldFb != fbRect { rebuildToolTips() }
    }

    /// A soft drop shadow made of stacked, faint rounded rectangles.
    private func paintShadow(_ body: CGRect, _ radius: CGFloat) {
        let pal = palette
        let steps = 9
        let layer = max(3, pal.shadow.a / Int(Double(steps) * 1.8))
        let drop: CGFloat = 4
        for i in stride(from: steps, to: 0, by: -1) {
            let grow = CGFloat(i) * (shadowMargin - 2) / CGFloat(steps)
            let rect = body.adjusted(-grow, -grow + drop, grow, grow + drop)
            Draw.fillRounded(rect, radius + grow, pal.shadow.withAlpha(layer))
        }
    }

    private func paintError(_ r0: CGRect) {
        let pal = palette, k = self.k
        var r = r0
        let text = metrics.error.isEmpty ? tr("panel.no_data") : metrics.error
        if settings.showFeedbackIcon {
            if settings.layout == "compact" {
                paintFbIcon(r.maxX - 11 * k, r.midY - 5.5 * k, 11 * k)
                r = r.adjusted(0, 0, -15 * k, 0)
            } else {
                paintFbIcon(r.maxX - 12 * k, r.minY + 1 * k, 12 * k)
                r = r.adjusted(0, 0, -16 * k, 0)
            }
        } else {
            fbRect = .zero
        }
        ageRect = .zero; badgeRect = .zero
        if settings.layout == "compact" {
            let style = TextStyle(qt: 7.4 * k, .semibold, pal.danger)
            let first = text.split(separator: "\n").first.map { String($0).trimmingCharacters(in: .whitespaces) } ?? ""
            Draw.text(Draw.elide(first, style, width: max(0, r.width)), in: r, style, align: .center)
            return
        }
        Draw.paragraph(text, in: r, TextStyle(qt: 9.5 * k, .semibold, pal.danger))
    }

    private func paintStatusDot(_ rect: CGRect, _ color: RGBA) {
        if !busy {
            Draw.ellipse(rect, color)
            return
        }
        let pal = palette
        let ring = rect.insetBy(dx: -1.2 * k, dy: -1.2 * k)
        let width = max(1.6, 2 * k)
        let radius = ring.width / 2
        Draw.stroke(Draw.arc(center: ring.center, radius: radius, fraction: 1), pal.dim.withAlpha(70), width: width)
        let start = CGFloat((Date().timeIntervalSince1970 * 360 * 1.4).truncatingRemainder(dividingBy: 360))
        Draw.stroke(Draw.arcSweep(center: ring.center, radius: radius, startDeg: start, sweepDeg: 110), pal.accent, width: width, cap: .round)
    }

    private func activityText() -> (String, RGBA?) {
        let pal = palette
        if busy {
            let dots = String(repeating: ".", count: 1 + Int(Date().timeIntervalSince1970 * 2.5) % 3)
            return (tr("panel.refreshing") + dots, pal.accent)
        }
        if !note.isEmpty, let r = retryIn {
            return ("! " + tr("panel.retry_in", Int(ceil(r))), pal.warn)
        }
        return ("", nil)
    }

    private func paintHeader(_ r: CGRect) -> CGFloat {
        let k = self.k, pal = palette, m = metrics
        let dot = CGRect(x: r.minX, y: r.minY + 3 * k, width: 8 * k, height: 8 * k)
        let worst = max(m.fiveHour.value, m.weekly.value, modelOn ? m.model.value : 0)
        paintStatusDot(dot, pal.status(worst, warn: settings.warn, danger: settings.danger))

        let titleStyle = TextStyle(qt: 6.8 * k, .semibold, pal.dim, kern: 1.4 * k)
        let title = "CLAUDE USAGE"
        Draw.text(title, in: CGRect(x: r.minX + 14 * k, y: r.minY, width: r.width * 0.6, height: 14 * k), titleStyle)
        var tx = r.minX + 14 * k + Draw.textWidth(title, titleStyle) + 9 * k
        let badgeW = paintBadge(tx, r.minY)
        if badgeW > 0 { tx += badgeW + 7 * k }

        var right = r.maxX
        if settings.showFeedbackIcon {
            paintFbIcon(r.maxX - 12 * k, r.minY + 1 * k, 12 * k)
            right -= 16 * k
        } else {
            fbRect = .zero
        }

        let (act, actColor) = activityText()
        if !act.isEmpty || settings.showAge {
            var text: String, color: RGBA
            if !act.isEmpty {
                text = act; color = actColor ?? pal.accent
            } else {
                let failing = !note.isEmpty
                text = ((m.stale || failing) ? "! " : "") + tr("panel.updated", fmtAge(m.ageSeconds))
                color = m.stale ? pal.danger : (failing ? pal.warn : pal.dim.withAlpha(190))
            }
            let style = TextStyle(qt: 6.6 * k, act.isEmpty ? .regular : .semibold, color)
            ageRect = CGRect(x: r.minX + r.width * 0.55, y: r.minY - 2 * k, width: right - r.minX - r.width * 0.55, height: 18 * k)
            Draw.text(text, in: CGRect(x: r.minX + r.width * 0.4, y: r.minY, width: right - r.minX - r.width * 0.4, height: 14 * k), style, align: .right)
        } else {
            ageRect = .zero
        }
        return r.minY + 20 * k
    }

    /// The plan as a little gradient pill with a sparkle. Returns its width (0 = none).
    private func paintBadge(_ x: CGFloat, _ top: CGFloat) -> CGFloat {
        badgeRect = .zero
        guard let pr = metrics.profile, !pr.badge.isEmpty, settings.showPlanBadge else { return 0 }
        let k = self.k
        var text = pr.badge
        if settings.showPlanName, let first = pr.name.split(separator: " ").first { text += "  \u{b7}  " + first }
        let style = TextStyle(qt: 6.0 * k, .bold, RGBA(255, 255, 255), kern: 0.7 * k)
        let tw = Draw.textWidth(text, style)
        let h = 12.5 * k
        let w = tw + 23 * k
        let rect = CGRect(x: x, y: top + 0.8 * k, width: w, height: h)
        let (c0, c1) = planStyle[pr.plan] ?? planStyle["enterprise"]!

        Draw.fillRounded(rect.insetBy(dx: -1.6 * k, dy: -1.6 * k), h / 2 + 1.6 * k, c1.withAlpha(46))
        Draw.gradient(Draw.roundedPath(rect, h / 2), from: CGPoint(x: rect.minX, y: rect.minY), to: CGPoint(x: rect.maxX, y: rect.maxY), c0, c1)
        Draw.fillRounded(CGRect(x: rect.minX + 2 * k, y: rect.minY + 1.2 * k, width: rect.width - 4 * k, height: h * 0.42), h * 0.21, RGBA(255, 255, 255, 46))
        let cy = rect.midY
        Draw.fill(Draw.sparkle(rect.minX + 8.2 * k, cy + 0.4 * k, 3.6 * k), RGBA(255, 255, 255, 255))
        Draw.fill(Draw.sparkle(rect.minX + 12.6 * k, cy - 2.9 * k, 1.5 * k), RGBA(255, 255, 255, 215))
        Draw.text(text, in: CGRect(x: rect.minX + 16.5 * k, y: rect.minY, width: tw + 4 * k, height: h), style)
        badgeRect = rect
        return w
    }

    /// A small speech bubble: click = message to the developer.
    private func paintFbIcon(_ x: CGFloat, _ y: CGFloat, _ size: CGFloat) {
        let pal = palette
        let rect = CGRect(x: x, y: y, width: size, height: size)
        fbRect = rect.insetBy(dx: -3, dy: -3)
        let color = hoverFeedback ? pal.accent : pal.dim.withAlpha(150)
        let bodyRect = CGRect(x: x, y: y + size * 0.08, width: size, height: size * 0.68)
        let path = CGMutablePath()
        path.addPath(Draw.roundedPath(bodyRect, size * 0.26))
        path.move(to: CGPoint(x: x + size * 0.26, y: bodyRect.maxY - 1))
        path.addLine(to: CGPoint(x: x + size * 0.18, y: y + size * 0.98))
        path.addLine(to: CGPoint(x: x + size * 0.48, y: bodyRect.maxY - 1))
        Draw.stroke(path, color, width: max(1, size * 0.1), join: .round)
        if hoverFeedback {
            for i in 0..<3 {
                let cx = x + size * (0.32 + 0.18 * CGFloat(i))
                Draw.circle(CGPoint(x: cx, y: bodyRect.midY), size * 0.05, color)
            }
        }
    }

    // MARK: layouts

    private func paintPostit(_ r: CGRect) {
        let k = self.k
        var y = paintHeader(r)
        for (_, label, g, hourly, sc) in gaugeItems() {
            y = paintBlock(CGRect(x: r.minX, y: y, width: r.width, height: 60 * k * sc), label, g, hourly, sc)
        }
        y = paintRows(CGRect(x: r.minX, y: y, width: r.width, height: 0))
        if settings.showSpark {
            let g = settings.showWeekly ? metrics.weekly : metrics.fiveHour
            paintSpark(CGRect(x: r.minX, y: y + 2 * k, width: r.width, height: 22 * k), g)
        }
    }

    private func paintBlock(_ r: CGRect, _ title: String, _ g: Gauge, _ hourly: Bool, _ sc: CGFloat) -> CGFloat {
        let k = self.k * sc, pal = palette
        let pctStyle = TextStyle(qt: 15 * k, .bold, pal.status(g.value, warn: settings.warn, danger: settings.danger))
        let pctText = "\(pct0(g.value))%"
        let pctW = Draw.textWidth(pctText, pctStyle)
        Draw.fittedText(title, in: CGRect(x: r.minX, y: r.minY, width: max(10, r.width - pctW - 8 * k), height: 18 * k),
                        TextStyle(qt: 7 * k, .semibold, pal.dim, kern: 1 * k))
        Draw.text(pctText, in: CGRect(x: r.minX + r.width * 0.4, y: r.minY - 3 * k, width: r.width * 0.6, height: 24 * k), pctStyle, align: .right)
        paintBar(CGRect(x: r.minX, y: r.minY + 22 * k, width: r.width, height: 8 * k), g.value)

        var parts: [String] = []
        if settings.showReset, let reset = g.resetInMs {
            parts.append(tr("panel.reset", (g.resetCertain ? "" : "~") + fmtDelta(reset)))
        }
        if settings.showBurn {
            if hourly && g.burn > 0.2 { parts.append(tr("panel.per_hour", pct0(g.burn))) }
            else if !hourly && g.burn > 0.02 { parts.append(tr("panel.per_day", pct0(g.burn * 24))) }
        }
        if !hourly, let pace = g.pace, abs(pace) >= 3 {
            parts.append(tr("panel.pace", (pace > 0 ? "+" : "") + pct0(pace) + "%"))
        } else if hourly, let eta = g.etaMs, g.value < 100 {
            parts.append(tr("panel.full_in", fmtDelta(eta)))
        }
        if !parts.isEmpty {
            Draw.fittedText(parts.joined(separator: " \u{b7} "), in: CGRect(x: r.minX, y: r.minY + 32 * k, width: r.width, height: 14 * k),
                            TextStyle(qt: 6.6 * k, .regular, pal.dim.withAlpha(210)))
        }
        return r.minY + 52 * k
    }

    private func paintBar(_ r: CGRect, _ value: Double) {
        let pal = palette
        let rad = r.height / 2
        Draw.fillRounded(r, rad, pal.track)
        let frac = CGFloat(max(0, min(1, value / 100)))
        if frac > 0.001 {
            let w = max(r.height, r.width * frac)
            let fr = CGRect(x: r.minX, y: r.minY, width: w, height: r.height)
            let (c0, c1) = pal.gaugeColors(value, warn: settings.warn, danger: settings.danger)
            Draw.gradient(Draw.roundedPath(fr, rad), from: CGPoint(x: fr.minX, y: fr.minY), to: CGPoint(x: fr.maxX, y: fr.minY), c0, c1)
        }
        // pace marks (where you'd be at even consumption)
        for q in [0.25, 0.5, 0.75] {
            let x = r.minX + r.width * CGFloat(q)
            Draw.line(CGPoint(x: x, y: r.minY + 1.5), CGPoint(x: x, y: r.maxY - 1.5), pal.text.withAlpha(38), width: 1)
        }
    }

    private func paintSpark(_ r: CGRect, _ g: Gauge) {
        let pal = palette
        let pts = g.spark
        guard pts.count >= 2 else { return }
        let top = max(10, pts.max() ?? 10)
        let path = CGMutablePath(), area = CGMutablePath()
        let n = pts.count
        for (i, v) in pts.enumerated() {
            let x = r.minX + r.width * CGFloat(i) / CGFloat(n - 1)
            let y = r.maxY - (r.height - 2) * CGFloat(v / top)
            if i == 0 {
                path.move(to: CGPoint(x: x, y: y))
                area.move(to: CGPoint(x: x, y: r.maxY))
                area.addLine(to: CGPoint(x: x, y: y))
            } else {
                path.addLine(to: CGPoint(x: x, y: y))
                area.addLine(to: CGPoint(x: x, y: y))
            }
        }
        area.addLine(to: CGPoint(x: r.maxX, y: r.maxY))
        area.closeSubpath()
        Draw.gradient(area, from: CGPoint(x: r.minX, y: r.minY), to: CGPoint(x: r.minX, y: r.maxY), pal.accent.withAlpha(90), pal.accent.withAlpha(0))
        Draw.stroke(path, pal.accent.withAlpha(220), width: 1.4 * k, cap: .round, join: .round)
    }

    /// The small list (other models, surfaces, usage credits). Returns the y below it.
    private func paintRows(_ r: CGRect) -> CGFloat {
        let rows = detailRows()
        if rows.isEmpty { return r.minY }
        let k = self.k, pal = palette
        var y = r.minY + 3 * k
        Draw.line(CGPoint(x: r.minX + 2 * k, y: y), CGPoint(x: r.maxX - 2 * k, y: y), pal.dim.withAlpha(40), width: 1)
        y += 4 * k
        let labelStyle = TextStyle(qt: 6.5 * k, .semibold, pal.text.withAlpha(215), kern: 0.3 * k)
        let valueStyle = TextStyle(qt: 6.9 * k, .bold, pal.text)
        let subStyle = TextStyle(qt: 6.0 * k, .regular, pal.dim.withAlpha(200))
        let widest = rows.filter { $0.id != "@header" }.map { Draw.textWidth($0.label, labelStyle) }.max() ?? 0
        let labelW = min(r.width * 0.42, widest + 4 * k)

        for row in rows {
            let line = CGRect(x: r.minX, y: y, width: r.width, height: rowHeight * k)
            if row.id == "@header" {
                Draw.text(row.label, in: CGRect(x: line.minX + 1 * k, y: line.minY + 2 * k, width: line.width, height: line.height - 2 * k),
                          TextStyle(qt: 5.6 * k, .semibold, pal.dim.withAlpha(210), kern: 0.9 * k))
                y += rowHeight * k
                continue
            }
            let local = row.id.hasPrefix("local:")
            let color: RGBA
            if local { color = pal.accent }
            else if let v = row.value { color = pal.status(v, warn: settings.warn, danger: settings.danger) }
            else { color = pal.dim.withAlpha(170) }
            Draw.circle(CGPoint(x: line.minX + 3.5 * k, y: line.midY), 2.1 * k, color)

            let text = Draw.elide(row.label, labelStyle, width: labelW)
            Draw.text(text, in: CGRect(x: line.minX + 10 * k, y: line.minY, width: labelW, height: line.height), labelStyle)

            let sub = (settings.showReset && row.resetMs != nil) ? fmtDelta(row.resetMs) : ""
            let rw = Draw.textWidth(row.right, valueStyle) + 2 * k
            let sw = sub.isEmpty ? 0 : Draw.textWidth(sub, subStyle) + 8 * k
            var vs = valueStyle
            vs.color = (row.value != nil ? color : pal.dim.withAlpha(220)).nsColor
            Draw.text(row.right, in: CGRect(x: line.maxX - rw, y: line.minY, width: rw, height: line.height), vs, align: .right)
            let barLeft = line.minX + 10 * k + labelW + 6 * k
            let barRight = line.maxX - rw - sw - 6 * k
            if !sub.isEmpty && barRight - barLeft > -2 * k {
                Draw.text(sub, in: CGRect(x: line.maxX - rw - sw, y: line.minY, width: sw - 4 * k, height: line.height), subStyle, align: .right)
            }
            if let v = row.value, barRight - barLeft >= 22 * k {
                let bar = CGRect(x: barLeft, y: line.midY - 1.6 * k, width: barRight - barLeft, height: 3.2 * k)
                if local {
                    Draw.fillRounded(bar, bar.height / 2, pal.track)
                    let fw = max(bar.height, bar.width * CGFloat(max(0, min(1, v / 100))))
                    Draw.fillRounded(CGRect(x: bar.minX, y: bar.minY, width: fw, height: bar.height), bar.height / 2, pal.accent.withAlpha(225))
                } else {
                    paintBar(bar, v)
                }
            }
            y += rowHeight * k
        }
        return y + 1 * k
    }

    private func paintRings(_ r: CGRect) {
        let k = self.k
        let y = paintHeader(r)
        let items = gaugeItems(short: true)
        guard !items.isEmpty else { return }
        let total = items.reduce(0) { $0 + $1.4 }
        let rowH = 96 * k * max(1, items.map { $0.4 }.max() ?? 1)
        var x = r.minX
        for (_, label, g, _, sc) in items {
            let w = r.width * sc / total
            paintRing(CGRect(x: x, y: y, width: w, height: rowH), label, g, sc)
            x += w
        }
        var y2 = paintRows(CGRect(x: r.minX, y: y + rowH + 1 * k, width: r.width, height: 0))
        if settings.showSpark {
            y2 = max(y2, y + rowH + 4 * k)
            paintSpark(CGRect(x: r.minX, y: y2, width: r.width, height: 20 * k), items[items.count - 1].2)
        }
    }

    private func paintRing(_ r: CGRect, _ label: String, _ g: Gauge, _ sc: CGFloat) {
        let k = self.k * sc, pal = palette
        let d = min(r.width - 12 * k, r.height - 22 * k, 74 * k)
        let top = r.minY + max(0, (r.height - 22 * k - d) / 2)
        let box = CGRect(x: r.midX - d / 2, y: top, width: d, height: d)
        let thick = max(5, 7 * k)
        let inner = box.insetBy(dx: thick, dy: thick)
        let radius = inner.width / 2
        Draw.stroke(Draw.arc(center: inner.center, radius: radius, fraction: 1), pal.track, width: thick, cap: .round)
        let (_, c1) = pal.gaugeColors(g.value, warn: settings.warn, danger: settings.danger)
        let frac = CGFloat(max(0, min(1, g.value / 100)))
        if frac > 0.001 {
            Draw.stroke(Draw.arc(center: inner.center, radius: radius, fraction: frac), c1, width: thick, cap: .round)
        }
        Draw.text("\(pct0(g.value))%", in: box, TextStyle(qt: 13 * k, .bold, pal.text), align: .center)
        let sub = (settings.showReset && g.resetInMs != nil) ? fmtDelta(g.resetInMs) : ""
        Draw.fittedText(label + (sub.isEmpty ? "" : "  \u{b7}  \(sub)"), in: CGRect(x: r.minX, y: box.maxY + 2 * k, width: r.width, height: 12 * k),
                        TextStyle(qt: 6.6 * k, .semibold, pal.dim, kern: 1 * k), align: .center)
    }

    private func paintCompact(_ r: CGRect) {
        let k = self.k, pal = palette
        let items = gaugeItems(short: true)
        guard !items.isEmpty else { return }
        ageRect = .zero; badgeRect = .zero
        var x = r.minX
        var dotColor = pal.status(items.map { $0.2.value }.max() ?? 0, warn: settings.warn, danger: settings.danger)
        if !note.isEmpty && !busy { dotColor = pal.warn }
        paintStatusDot(CGRect(x: x, y: r.midY - 4 * k, width: 8 * k, height: 8 * k), dotColor)
        x += 16 * k

        var right = r.maxX
        if settings.showFeedbackIcon {
            paintFbIcon(r.maxX - 11 * k, r.midY - 5.5 * k, 11 * k)
            right -= 15 * k
        } else {
            fbRect = .zero
        }
        let total = items.reduce(0) { $0 + $1.4 }
        let avail = right - x
        for (gid, label0, g, _, sc) in items {
            var label = label0
            if gid == "mo" { label = String(label.prefix(6)) }
            let kk = k * sc
            let seg = avail * sc / total
            let labelStyle = TextStyle(qt: 6.8 * kk, .semibold, pal.dim, kern: 0.8 * kk)
            let lw = max(26 * kk, Draw.textWidth(label, labelStyle) + 6 * kk)
            Draw.text(label, in: CGRect(x: x, y: r.minY, width: lw, height: r.height), labelStyle)
            Draw.text("\(pct0(g.value))%", in: CGRect(x: x + lw, y: r.minY, width: 38 * kk, height: r.height),
                      TextStyle(qt: 10 * kk, .bold, pal.status(g.value, warn: settings.warn, danger: settings.danger)))
            let barX = x + lw + 40 * kk
            paintBar(CGRect(x: barX, y: r.midY - 3 * kk, width: max(20 * k, x + seg - 12 * k - barX), height: 6 * kk), g.value)
            x += seg
        }
    }
}
