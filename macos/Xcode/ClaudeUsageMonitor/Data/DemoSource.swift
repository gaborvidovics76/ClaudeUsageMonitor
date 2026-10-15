// Built-in demo data (App Store Review Guideline 2.1(a): a demo mode in lieu of a demo account).
// It lets anyone - including App Review - see every part of the panel without a Claude account
// or the Claude desktop app. The figures are generated locally; nothing is fetched or sent.

import Foundation

final class DemoSource: UsageSource {
    private let start = Date().timeIntervalSince1970 - 6 * 86400 - 3 * 3600   // the "week" began 6 days ago
    private var cache: [Sample] = []
    private var cachedAt: Int64 = 0

    private func generate() -> [Sample] {
        let now = nowMs()
        if now - cachedAt < 60_000 && !cache.isEmpty { return cache }
        var rows: [Sample] = []
        let startMs = Int64(start * 1000)
        var t = startMs
        let step: Int64 = 15 * 60 * 1000
        var fh = 0.0, sd = 0.0, mo = 0.0
        var seed: UInt64 = 0x9E3779B97F4A7C15
        let tz = Int64(TimeZone.current.secondsFromGMT())
        func rnd() -> Double {              // deterministic, so the demo looks the same every time
            seed = seed &* 6364136223846793005 &+ 1442695040888963407
            return Double((seed >> 33) % 1000) / 1000
        }
        while t <= now {
            let hourOfDay = Double((t / 1000 + tz) % 86400) / 3600     // local time, so the day looks right
            let working = hourOfDay > 8 && hourOfDay < 22
            let sessionPos = Double((t - startMs) % fiveHoursMs) / Double(fiveHoursMs)
            if sessionPos < 0.03 { fh = 0 }
            if working {
                // kept below the limits, so the panel shows a typical week instead of everything at 100 %
                fh = min(100, fh + 0.8 + rnd() * 2.5)
                sd = min(100, sd + 0.08 + rnd() * 0.15)
                mo = min(100, mo + 0.12 + rnd() * 0.2)
            }
            rows.append(Sample(t: t, org: "demo", fh: fh, sd: sd, mo: mo))
            t += step
        }
        cache = rows
        cachedAt = now
        return rows
    }

    func organizations() -> [String] { ["demo"] }

    func series(org: String?, sinceMs: Int64?) -> [Sample] {
        let rows = generate()
        if let since = sinceMs { return rows.filter { $0.t >= since } }
        return rows
    }

    func read(org: String?) -> Metrics {
        let rows = generate()
        guard let last = rows.last else { return Metrics() }
        let now = nowMs()
        var m = Metrics()
        m.ok = true
        m.org = "demo"
        m.orgs = ["demo"]
        m.updatedAt = now - 40_000
        m.sampleCount = rows.count

        let fhRows = rows.map { ($0.t, $0.fh) }, sdRows = rows.map { ($0.t, $0.sd) }, moRows = rows.map { ($0.t, $0.mo) }
        var g = Gauge()
        g.value = last.fh
        let sessionStart = now - (now - Int64(start * 1000)) % fiveHoursMs
        g.resetAt = sessionStart + fiveHoursMs
        g.resetCertain = true
        g.burn = Analysis.burn(fhRows, nowMs: now, windowMs: 3_600_000)
        if g.burn > 0.2 && g.value < 100 { g.etaMs = Int64(g.remaining / g.burn * 3_600_000) }
        g.spark = Analysis.spark(fhRows, nowMs: now, spanMs: fiveHoursMs, points: 48)
        m.fiveHour = g

        var w = Gauge()
        w.value = last.sd
        w.resetAt = Int64(start * 1000) + weekMs
        w.resetCertain = true
        w.burn = Analysis.burn(sdRows, nowMs: now, windowMs: 6 * 3_600_000)
        if w.burn > 0.05 && w.value < 100 { w.etaMs = Int64(w.remaining / w.burn * 3_600_000) }
        w.pace = Analysis.weeklyPace(value: w.value, resetAt: w.resetAt, nowMs: now)
        w.spark = Analysis.spark(sdRows, nowMs: now, spanMs: weekMs, points: 64)
        m.weekly = w

        var mg = Gauge()
        m.modelName = "Fable"
        mg.value = last.mo
        mg.resetAt = w.resetAt
        mg.resetCertain = true
        mg.burn = Analysis.burn(moRows, nowMs: now, windowMs: 6 * 3_600_000)
        mg.pace = Analysis.weeklyPace(value: mg.value, resetAt: mg.resetAt, nowMs: now)
        mg.spark = Analysis.spark(moRows, nowMs: now, spanMs: weekMs, points: 64)
        m.model = mg

        m.rows = [
            DetailRow(id: "model:Opus", category: "model", label: "Opus", value: min(100, last.mo * 0.55), resetAt: w.resetAt),
            DetailRow(id: "model:Sonnet", category: "model", label: "Sonnet", value: min(100, last.mo * 0.3), resetAt: w.resetAt),
            DetailRow(id: "surface:oauth_apps", category: "surface", label: "@oauth_apps", value: 12, resetAt: w.resetAt),
        ]
        m.extra = ExtraUsage(enabled: true, monthlyLimit: 50, used: 7.5, utilization: 15, currency: "USD")
        var p = ProfileInfo()
        p.plan = "max"; p.tier = "default_claude_max_5x"; p.name = "Demo User"; p.orgType = "claude_max"
        p.hasExtraUsage = true; p.createdAt = "2025-03-01T00:00:00Z"
        m.profile = p
        return m
    }
}
