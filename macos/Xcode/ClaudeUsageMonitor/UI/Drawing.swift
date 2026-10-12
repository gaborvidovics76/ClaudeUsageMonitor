// Small Core Graphics / AppKit drawing helpers shared by the panel, the status-bar icon and the
// history chart. All drawing code works in a FLIPPED coordinate system (origin top-left,
// y grows downwards), the same as the Windows app's painter, so the geometry ports 1:1.

import AppKit

/// Qt point sizes were laid out at 96 dpi (1 pt = 1.33 px); AppKit points are 1 px at 1x.
/// Multiplying keeps the proportions of the Windows panel.
let fontPointScale: CGFloat = 4.0 / 3.0

struct TextStyle {
    var size: CGFloat                   // AppKit points (already scaled)
    var weight: NSFont.Weight = .regular
    var color: NSColor
    var kern: CGFloat = 0

    /// Qt-style constructor: `size` in the Windows app's point units (scaled by 4/3).
    init(qt size: CGFloat, _ weight: NSFont.Weight = .regular, _ color: RGBA, kern: CGFloat = 0) {
        self.size = max(5, size * fontPointScale)
        self.weight = weight
        self.color = color.nsColor
        self.kern = kern
    }

    init(size: CGFloat, weight: NSFont.Weight = .regular, color: NSColor, kern: CGFloat = 0) {
        self.size = size; self.weight = weight; self.color = color; self.kern = kern
    }

    var font: NSFont { NSFont.systemFont(ofSize: size, weight: weight) }

    var attributes: [NSAttributedString.Key: Any] {
        var a: [NSAttributedString.Key: Any] = [.font: font, .foregroundColor: color]
        if kern != 0 { a[.kern] = kern }
        return a
    }
}

enum HAlign { case left, center, right }

extension CGRect {
    /// Qt's QRectF.adjusted(dx1, dy1, dx2, dy2).
    func adjusted(_ dx1: CGFloat, _ dy1: CGFloat, _ dx2: CGFloat, _ dy2: CGFloat) -> CGRect {
        CGRect(x: minX + dx1, y: minY + dy1, width: width - dx1 + dx2, height: height - dy1 + dy2)
    }
    var center: CGPoint { CGPoint(x: midX, y: midY) }
}

enum Draw {
    static var ctx: CGContext { NSGraphicsContext.current!.cgContext }

    static func textWidth(_ text: String, _ style: TextStyle) -> CGFloat {
        NSAttributedString(string: text, attributes: style.attributes).size().width
    }

    /// Shortens the text with "…" so that it fits `width` (Qt's elidedText, ElideRight).
    static func elide(_ text: String, _ style: TextStyle, width: CGFloat) -> String {
        if textWidth(text, style) <= width { return text }
        var chars = Array(text)
        while chars.count > 1 {
            chars.removeLast()
            let candidate = String(chars).trimmingCharacters(in: .whitespaces) + "…"
            if textWidth(candidate, style) <= width { return candidate }
        }
        return "…"
    }

    /// Draws one line of text vertically centred in `rect` with the given horizontal alignment.
    static func text(_ text: String, in rect: CGRect, _ style: TextStyle, align: HAlign = .left) {
        let attr = NSAttributedString(string: text, attributes: style.attributes)
        let size = attr.size()
        var x = rect.minX
        switch align {
        case .left: x = rect.minX
        case .center: x = rect.midX - size.width / 2
        case .right: x = rect.maxX - size.width
        }
        let y = rect.midY - size.height / 2
        attr.draw(at: CGPoint(x: x, y: y))
    }

    /// Draws one line so that it always fits the rectangle, in any language: first the extra letter
    /// spacing goes, then the font shrinks (down to minScale), and only then is it elided with "…".
    static func fittedText(_ text: String, in rect: CGRect, _ style: TextStyle, align: HAlign = .left, minScale: CGFloat = 0.8) {
        let width = max(1, rect.width)
        var s = style
        if textWidth(text, s) > width && s.kern != 0 { s.kern = 0 }
        let base = s.size
        let adv = textWidth(text, s)
        if adv > width && base > 0 {
            s.size = max(base * minScale, base * width / adv)
        }
        var t = text
        if textWidth(t, s) > width { t = elide(t, s, width: width) }
        self.text(t, in: rect, s, align: align)
    }

    /// Multi-line, centred paragraph (the error state of the panel).
    static func paragraph(_ text: String, in rect: CGRect, _ style: TextStyle) {
        let ps = NSMutableParagraphStyle()
        ps.alignment = .center
        ps.lineBreakMode = .byWordWrapping
        var attrs = style.attributes
        attrs[.paragraphStyle] = ps
        let attr = NSAttributedString(string: text, attributes: attrs)
        let bounds = attr.boundingRect(with: CGSize(width: rect.width, height: .greatestFiniteMagnitude),
                                       options: [.usesLineFragmentOrigin, .usesFontLeading])
        let y = max(rect.minY, rect.midY - bounds.height / 2)
        attr.draw(with: CGRect(x: rect.minX, y: y, width: rect.width, height: min(rect.height, bounds.height)),
                  options: [.usesLineFragmentOrigin, .usesFontLeading])
    }

    static func roundedPath(_ rect: CGRect, _ radius: CGFloat) -> CGPath {
        let r = max(0, min(radius, min(rect.width, rect.height) / 2))
        return CGPath(roundedRect: rect, cornerWidth: r, cornerHeight: r, transform: nil)
    }

    static func fill(_ path: CGPath, _ color: RGBA) {
        let c = ctx
        c.saveGState()
        c.addPath(path)
        c.setFillColor(color.cgColor)
        c.fillPath()
        c.restoreGState()
    }

    static func fillRounded(_ rect: CGRect, _ radius: CGFloat, _ color: RGBA) {
        fill(roundedPath(rect, radius), color)
    }

    static func stroke(_ path: CGPath, _ color: RGBA, width: CGFloat, cap: CGLineCap = .butt, join: CGLineJoin = .miter) {
        let c = ctx
        c.saveGState()
        c.addPath(path)
        c.setStrokeColor(color.cgColor)
        c.setLineWidth(width)
        c.setLineCap(cap)
        c.setLineJoin(join)
        c.strokePath()
        c.restoreGState()
    }

    static func line(_ a: CGPoint, _ b: CGPoint, _ color: RGBA, width: CGFloat = 1) {
        let p = CGMutablePath()
        p.move(to: a)
        p.addLine(to: b)
        stroke(p, color, width: width)
    }

    static func ellipse(_ rect: CGRect, _ color: RGBA) {
        fill(CGPath(ellipseIn: rect, transform: nil), color)
    }

    static func circle(_ center: CGPoint, _ radius: CGFloat, _ color: RGBA) {
        ellipse(CGRect(x: center.x - radius, y: center.y - radius, width: 2 * radius, height: 2 * radius), color)
    }

    /// Fills `path` with a linear gradient from `start` to `end` (in the flipped view coordinates).
    static func gradient(_ path: CGPath, from start: CGPoint, to end: CGPoint, _ c0: RGBA, _ c1: RGBA) {
        guard let grad = CGGradient(colorsSpace: CGColorSpace(name: CGColorSpace.sRGB),
                                    colors: [c0.cgColor, c1.cgColor] as CFArray, locations: [0, 1]) else { return }
        let c = ctx
        c.saveGState()
        c.addPath(path)
        c.clip()
        c.drawLinearGradient(grad, start: start, end: end, options: [.drawsBeforeStartLocation, .drawsAfterEndLocation])
        c.restoreGState()
    }

    /// An arc path running visually clockwise from 12 o'clock (flipped coordinates).
    static func arc(center: CGPoint, radius: CGFloat, fraction: CGFloat, startDeg: CGFloat = -90) -> CGPath {
        let p = CGMutablePath()
        let start = startDeg * .pi / 180
        p.addArc(center: center, radius: radius, startAngle: start, endAngle: start + 2 * .pi * fraction, clockwise: false)
        return p
    }

    /// A pie-slice-free arc that starts at `startDeg` and sweeps `sweepDeg` (positive = clockwise visually).
    static func arcSweep(center: CGPoint, radius: CGFloat, startDeg: CGFloat, sweepDeg: CGFloat) -> CGPath {
        let p = CGMutablePath()
        let s = startDeg * .pi / 180
        p.addArc(center: center, radius: radius, startAngle: s, endAngle: s + sweepDeg * .pi / 180, clockwise: sweepDeg < 0)
        return p
    }

    /// Eight-point sparkle (the plan badge).
    static func sparkle(_ cx: CGFloat, _ cy: CGFloat, _ r: CGFloat, points: Int = 8, inner: CGFloat = 0.34) -> CGPath {
        let p = CGMutablePath()
        for i in 0..<points {
            let rad = i % 2 == 0 ? r : r * inner
            let ang = (2 * CGFloat.pi / CGFloat(points)) * CGFloat(i) - .pi / 2
            let pt = CGPoint(x: cx + rad * cos(ang), y: cy + rad * sin(ang))
            if i == 0 { p.move(to: pt) } else { p.addLine(to: pt) }
        }
        p.closeSubpath()
        return p
    }
}
