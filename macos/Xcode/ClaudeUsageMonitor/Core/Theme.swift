// Colour themes (port of claude_usage/theme.py). Every colour is an RGBA with 0-255 components.

import AppKit

struct RGBA: Equatable {
    var r: Int, g: Int, b: Int, a: Int

    init(_ r: Int, _ g: Int, _ b: Int, _ a: Int = 255) { self.r = r; self.g = g; self.b = b; self.a = a }

    var nsColor: NSColor {
        NSColor(srgbRed: CGFloat(r) / 255, green: CGFloat(g) / 255, blue: CGFloat(b) / 255, alpha: CGFloat(a) / 255)
    }
    var cgColor: CGColor { nsColor.cgColor }

    func withAlpha(_ alpha: Int) -> RGBA { RGBA(r, g, b, max(0, min(255, alpha))) }

    func mix(_ other: RGBA, _ t: Double) -> RGBA {
        let t = max(0, min(1, t))
        return RGBA(Int(Double(r) + Double(other.r - r) * t), Int(Double(g) + Double(other.g - g) * t),
                    Int(Double(b) + Double(other.b - b) * t), Int(Double(a) + Double(other.a - a) * t))
    }

    var hex: String { String(format: "#%02X%02X%02X", r, g, b) }

    /// "#RRGGBB" or "#RGB" -> colour; nil when malformed.
    init?(hex: String) {
        var v = hex.trimmingCharacters(in: .whitespaces)
        if v.hasPrefix("#") { v.removeFirst() }
        if v.count == 3 { v = v.map { "\($0)\($0)" }.joined() }
        guard v.count == 6, let n = Int(v, radix: 16) else { return nil }
        self.init((n >> 16) & 0xFF, (n >> 8) & 0xFF, n & 0xFF, 255)
    }
}

struct Theme {
    let key: String
    let dark: Bool
    let bg: RGBA, bg2: RGBA, border: RGBA, text: RGBA, dim: RGBA, track: RGBA
    let accent: RGBA, ok: RGBA, warn: RGBA, danger: RGBA, shadow: RGBA
}

enum Themes {
    static let defaultKey = "midnight"

    /// In menu order.
    static let all: [Theme] = [
        Theme(key: "midnight", dark: true,
              bg: RGBA(20, 24, 36, 246), bg2: RGBA(30, 36, 55, 246), border: RGBA(255, 255, 255, 38),
              text: RGBA(238, 242, 252), dim: RGBA(150, 160, 186), track: RGBA(255, 255, 255, 26),
              accent: RGBA(120, 162, 255), ok: RGBA(74, 214, 160), warn: RGBA(255, 190, 92),
              danger: RGBA(255, 106, 106), shadow: RGBA(0, 0, 0, 150)),
        Theme(key: "claude", dark: true,
              bg: RGBA(28, 24, 22, 248), bg2: RGBA(45, 38, 34, 248), border: RGBA(255, 226, 210, 34),
              text: RGBA(245, 238, 232), dim: RGBA(176, 160, 148), track: RGBA(255, 255, 255, 26),
              accent: RGBA(217, 119, 87), ok: RGBA(122, 190, 140), warn: RGBA(233, 178, 88),
              danger: RGBA(226, 92, 76), shadow: RGBA(0, 0, 0, 150)),
        Theme(key: "graphite", dark: true,
              bg: RGBA(24, 25, 27, 248), bg2: RGBA(38, 40, 43, 248), border: RGBA(255, 255, 255, 30),
              text: RGBA(236, 237, 240), dim: RGBA(150, 153, 160), track: RGBA(255, 255, 255, 24),
              accent: RGBA(168, 176, 190), ok: RGBA(108, 200, 150), warn: RGBA(232, 184, 96),
              danger: RGBA(232, 100, 96), shadow: RGBA(0, 0, 0, 150)),
        Theme(key: "neon", dark: true,
              bg: RGBA(11, 13, 20, 246), bg2: RGBA(20, 24, 38, 246), border: RGBA(108, 240, 255, 60),
              text: RGBA(233, 250, 255), dim: RGBA(128, 168, 186), track: RGBA(108, 240, 255, 28),
              accent: RGBA(94, 234, 255), ok: RGBA(86, 240, 190), warn: RGBA(255, 214, 102),
              danger: RGBA(255, 88, 132), shadow: RGBA(0, 220, 255, 90)),
        Theme(key: "paper", dark: false,
              bg: RGBA(252, 252, 253, 250), bg2: RGBA(240, 241, 245, 250), border: RGBA(16, 20, 32, 34),
              text: RGBA(26, 30, 42), dim: RGBA(112, 120, 138), track: RGBA(16, 20, 32, 26),
              accent: RGBA(58, 110, 232), ok: RGBA(32, 158, 108), warn: RGBA(198, 128, 20),
              danger: RGBA(206, 62, 62), shadow: RGBA(16, 24, 48, 60)),
        Theme(key: "postit", dark: false,
              bg: RGBA(255, 228, 120, 248), bg2: RGBA(255, 214, 92, 248), border: RGBA(140, 106, 20, 46),
              text: RGBA(56, 42, 12), dim: RGBA(122, 96, 32), track: RGBA(90, 68, 16, 40),
              accent: RGBA(196, 92, 40), ok: RGBA(42, 128, 72), warn: RGBA(176, 108, 16),
              danger: RGBA(188, 48, 40), shadow: RGBA(90, 70, 20, 90)),
    ]

    static func theme(_ key: String) -> Theme { all.first { $0.key == key } ?? all[0] }
}

/// A palette built from a theme plus an optional custom accent colour.
struct Palette {
    let name: String
    let dark: Bool
    let bg: RGBA, bg2: RGBA, border: RGBA, text: RGBA, dim: RGBA, track: RGBA
    let accent: RGBA, ok: RGBA, warn: RGBA, danger: RGBA, shadow: RGBA

    init(theme key: String, accentHex: String = "") {
        let t = Themes.theme(key)
        name = t.key; dark = t.dark
        bg = t.bg; bg2 = t.bg2; border = t.border; text = t.text; dim = t.dim; track = t.track
        ok = t.ok; warn = t.warn; danger = t.danger; shadow = t.shadow
        if !accentHex.isEmpty, let custom = RGBA(hex: accentHex) { accent = custom } else { accent = t.accent }
    }

    func status(_ value: Double, warn w: Double, danger d: Double) -> RGBA {
        if value >= d { return danger }
        if value >= w { return warn }
        return ok
    }

    /// The two ends of a bar's gradient.
    func gaugeColors(_ value: Double, warn w: Double, danger d: Double) -> (RGBA, RGBA) {
        let end = status(value, warn: w, danger: d)
        return (accent.mix(end, 0.55), end)
    }
}
