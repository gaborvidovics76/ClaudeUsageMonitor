// Status-bar icon (percentage with a progress ring) and the in-app logo used by notifications.

import AppKit

enum Icons {
    /// Menu-bar icon: the percentage as a number inside a progress ring, coloured by status.
    static func statusImage(value: Double, color: RGBA, size: CGFloat = 18) -> NSImage {
        let img = NSImage(size: NSSize(width: size, height: size), flipped: true) { rect in
            let c = Draw.ctx
            c.setAllowsAntialiasing(true)
            let ringW = size * 0.11
            let box = rect.insetBy(dx: ringW / 2 + 0.5, dy: ringW / 2 + 0.5)
            let center = box.center
            let radius = box.width / 2
            Draw.stroke(Draw.arc(center: center, radius: radius, fraction: 1), color.withAlpha(70), width: ringW, cap: .round)
            let frac = CGFloat(max(0, min(1, value / 100)))
            if frac > 0.001 {
                Draw.stroke(Draw.arc(center: center, radius: radius, fraction: frac), color, width: ringW, cap: .round)
            }
            let text = value >= 99.5 ? "!" : pct0(value)
            var style = TextStyle(size: size * 0.5, weight: .bold, color: color.nsColor)
            while style.size > 5 && Draw.textWidth(text, style) > size * 0.62 {
                style.size -= 0.5
            }
            Draw.text(text, in: rect, style, align: .center)
            return true
        }
        img.isTemplate = false
        return img
    }

    /// The app's own icon from the asset catalogue (for the "no data" state of the status item).
    static var appIcon: NSImage {
        if let img = NSImage(named: "AppIcon") { return img }
        return NSApp.applicationIconImage
    }

    static func statusPlaceholder(size: CGFloat = 18) -> NSImage {
        let img = appIcon.copy() as! NSImage
        img.size = NSSize(width: size, height: size)
        return img
    }
}
