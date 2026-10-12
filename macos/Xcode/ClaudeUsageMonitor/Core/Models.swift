// Data model shared by the panel, the history window and both data sources
// (port of claude_usage/datasource.py).

import Foundation

let fiveHoursMs: Int64 = 5 * 3600 * 1000
let weekMs: Int64 = 7 * 24 * 3600 * 1000

@inline(__always) func nowMs() -> Int64 { Int64(Date().timeIntervalSince1970 * 1000) }

struct Sample {
    var t: Int64            // epoch ms
    var org: String
    var fh: Double          // 5-hour window, percent
    var sd: Double          // weekly limit, percent
    var mo: Double = 0      // model-scoped weekly (claude.ai source only)
}

/// The current state of one limit (5-hour, weekly or per-model).
struct Gauge {
    var value: Double = 0
    var resetAt: Int64? = nil           // epoch ms
    var resetCertain = false
    var burn: Double = 0                // %/hour
    var etaMs: Int64? = nil             // time until it would reach 100 %
    var pace: Double? = nil             // actual - ideal consumption (%), weekly only
    var spark: [Double] = []

    var remaining: Double { max(0, 100 - value) }
    var resetInMs: Int64? {
        guard let r = resetAt else { return nil }
        return max(0, r - nowMs())
    }
}

/// A secondary limit shown in the small list under the gauges.
struct DetailRow {
    var id: String          // "model:Opus" | "surface:<name>" | "kind:<kind>"
    var category: String    // model | surface | other
    var label: String
    var value: Double = 0
    var resetAt: Int64? = nil

    var resetInMs: Int64? {
        guard let r = resetAt else { return nil }
        return max(0, r - nowMs())
    }

    /// Display name of the row (the connected-apps surface has a translated name).
    var displayLabel: String { label == "@oauth_apps" ? tr("detail.surface.oauth_apps") : label }
}

/// Pay-as-you-go usage on top of the plan ("usage credits").
struct ExtraUsage {
    var enabled = false
    var monthlyLimit: Double? = nil
    var used: Double? = nil
    var utilization: Double? = nil
    var currency = "USD"
    var disabledReason = ""
}

/// What the profile endpoint says about the plan. Never logged, never sent anywhere.
struct ProfileInfo {
    var plan = ""           // pro | max | team | enterprise | ""
    var tier = ""
    var name = ""
    var orgType = ""
    var billingType = ""
    var hasExtraUsage: Bool? = nil
    var createdAt = ""

    var multiplier: String {
        if let m = tier.range(of: #"(\d+)x"#, options: .regularExpression) {
            let digits = tier[m].dropLast()
            return "\(digits)\u{d7}"
        }
        return ""
    }

    var badge: String {
        if plan.isEmpty { return "" }
        let text = plan.uppercased()
        if plan == "max" && !multiplier.isEmpty { return "\(text) \(multiplier)" }
        return text
    }
}

struct Metrics {
    var ok = false
    var error = ""
    var org = ""
    var orgs: [String] = []
    var updatedAt: Int64? = nil
    var sampleCount = 0
    var fiveHour = Gauge()
    var weekly = Gauge()
    var model = Gauge()
    var rows: [DetailRow] = []
    var extra: ExtraUsage? = nil
    var profile: ProfileInfo? = nil
    var modelName = ""

    var hasModel: Bool { !modelName.isEmpty }

    var ageSeconds: Double? {
        guard let u = updatedAt else { return nil }
        return max(0, Date().timeIntervalSince1970 - Double(u) / 1000)
    }

    var stale: Bool {
        guard let a = ageSeconds else { return true }
        return a > 15 * 60
    }
}

// MARK: - formatting helpers

/// "{d}d {h}h" / "{h}h {m}m" / "{m}m" for a duration in ms ("?" when unknown).
func fmtDelta(_ ms: Int64?) -> String {
    guard let ms = ms else { return "?" }
    var s = max(0, ms / 1000)
    let d = s / 86400; s %= 86400
    let h = s / 3600; s %= 3600
    let m = s / 60
    if d > 0 { return tr("time.dh", d, h) }
    if h > 0 { return tr("time.hm", h, m) }
    return tr("time.m", m)
}

/// How old a reading is, in the shortest sensible unit.
func fmtAge(_ seconds: Double?) -> String {
    guard let seconds = seconds else { return tr("time.none") }
    if seconds < 90 { return tr("time.sec", Int(seconds)) }
    let m = Int(seconds / 60)
    if m < 90 { return tr("time.min", m) }
    let h = m / 60
    if h < 48 { return tr("time.hour", h) }
    return tr("time.day", h / 24)
}

/// Python's f"{x:.0f}" (rounds half to even like printf does).
func pct0(_ x: Double) -> String { String(format: "%.0f", x) }
func num(_ x: Double, _ decimals: Int) -> String { String(format: "%.\(decimals)f", x) }

/// Shared analysis used by both data sources.
enum Analysis {
    /// Start of the current window (startMs, isCertain) from a (t, value) series.
    static func windowStart(_ rows: [(Int64, Double)], spanMs: Int64) -> (Int64?, Bool) {
        guard let last = rows.last, last.1 > 0 else { return (nil, false) }
        var i = rows.count - 1
        while i > 0 {
            let (tCur, vCur) = rows[i]
            let (tPrev, vPrev) = rows[i - 1]
            if tCur - tPrev > spanMs { return (tCur, false) }
            if vPrev <= 0 && vCur > 0 { return (tCur, true) }
            if vPrev - vCur > 5 { return (tCur, true) }
            i -= 1
        }
        return (rows[0].0, false)
    }

    /// Consumption in %/hour over the last `windowMs`.
    static func burn(_ rows: [(Int64, Double)], nowMs now: Int64, windowMs: Int64) -> Double {
        let pts = rows.filter { $0.0 >= now - windowMs }
        guard pts.count >= 2, let f = pts.first, let l = pts.last else { return 0 }
        let dtH = Double(l.0 - f.0) / 3_600_000
        if dtH <= 0 { return 0 }
        return max(0, (l.1 - f.1) / dtH)
    }

    static func spark(_ rows: [(Int64, Double)], nowMs now: Int64, spanMs: Int64, points: Int) -> [Double] {
        let pts = rows.filter { $0.0 >= now - spanMs }.map { $0.1 }
        if pts.count <= points { return pts }
        let step = Double(pts.count) / Double(points)
        return (0..<points).map { pts[min(pts.count - 1, Int(Double($0) * step))] }
    }

    static func weeklyPace(value: Double, resetAt: Int64?, nowMs now: Int64) -> Double? {
        guard let reset = resetAt else { return nil }
        let elapsed = 1.0 - Double(max(0, reset - now)) / Double(weekMs)
        let ideal = max(0, min(1, elapsed)) * 100
        return value - ideal
    }
}

/// Parses "2026-10-12T08:42:01Z" / "...+00:00" / fractional seconds into epoch ms.
func parseIsoMs(_ value: Any?) -> Int64? {
    if let n = value as? Double { return Int64(n * 1000) }
    if let n = value as? Int { return Int64(n) * 1000 }
    guard let s = (value as? String)?.trimmingCharacters(in: .whitespaces), !s.isEmpty else { return nil }
    let iso = ISO8601DateFormatter()
    iso.formatOptions = [.withInternetDateTime, .withFractionalSeconds]
    if let d = iso.date(from: s) { return Int64(d.timeIntervalSince1970 * 1000) }
    iso.formatOptions = [.withInternetDateTime]
    if let d = iso.date(from: s) { return Int64(d.timeIntervalSince1970 * 1000) }
    // "2026-10-12T08:42:01" without a zone -> treat as UTC
    let f = DateFormatter()
    f.locale = Locale(identifier: "en_US_POSIX")
    f.timeZone = TimeZone(secondsFromGMT: 0)
    for fmt in ["yyyy-MM-dd'T'HH:mm:ss.SSSSSS", "yyyy-MM-dd'T'HH:mm:ss", "yyyy-MM-dd HH:mm:ss"] {
        f.dateFormat = fmt
        if let d = f.date(from: s) { return Int64(d.timeIntervalSince1970 * 1000) }
    }
    return nil
}
