// Reading and evaluating the plan-usage-history.json written by Claude Desktop
// (port of claude_usage/datasource.py).
//
// File format (v2):
//     {"version":2,"samples":[{"t":<epoch ms>,"org":"<uuid>","u":{"fh":<0-100>,"sd":<0-100>}}, ...]}
//
// The file lives in ~/Library/Application Support/Claude/ - outside this app's sandbox, so it can
// only be read after the user has chosen it once in the Open panel (Settings -> Data source).

import Foundation

final class LocalLogReader: UsageSource {
    private let settings: Settings
    private var stamp: (Date, Int)? = nil
    private var samples: [Sample] = []
    private var orgs: [String] = []
    private var error = ""
    private var lastAccessOK = false

    init(settings: Settings) { self.settings = settings }

    /// True when a usable bookmark of the log exists.
    var hasAccess: Bool { Bookmarks.resolve(settings.desktopLogBookmark) != nil }

    /// Force a re-read on the next read() even if the file stamp is unchanged.
    func invalidate() { stamp = nil }

    // MARK: - io

    private func load() {
        let result: ([Sample], String)? = Bookmarks.withAccess(settings.desktopLogBookmark) { url in
            self.loadFrom(url)
        }
        guard let found = result else {
            // no bookmark: tell the user how to grant access (sandbox)
            samples = []
            stamp = nil
            orgs = []
            error = tr("err.no_access_mac")
            return
        }
        let (rows, err) = found
        if !rows.isEmpty || !err.isEmpty {
            samples = rows
            error = err
        }
        var seen: [String: Int64] = [:]
        for s in samples { seen[s.org] = s.t }
        orgs = seen.sorted { $0.value > $1.value }.map { $0.key }.filter { !$0.isEmpty }
    }

    /// (samples, error) - samples empty + error empty means "unchanged, keep what we have".
    private func loadFrom(_ url: URL) -> ([Sample], String) {
        guard let attrs = try? FileManager.default.attributesOfItem(atPath: url.path),
              let mtime = attrs[.modificationDate] as? Date, let size = attrs[.size] as? Int else {
            stamp = nil
            return ([], tr("err.file_not_found"))
        }
        if let s = stamp, s.0 == mtime, s.1 == size, !samples.isEmpty { return ([], "") }
        guard let data = try? Data(contentsOf: url),
              let raw = (try? JSONSerialization.jsonObject(with: data)) as? [String: Any] else {
            // the file may be mid-write - keep the previous good state
            return samples.isEmpty ? ([], tr("err.file_unreadable")) : ([], "")
        }
        var rows: [Sample] = []
        for item in (raw["samples"] as? [[String: Any]]) ?? [] {
            guard let t = item["t"] as? Double else { continue }
            let u = item["u"] as? [String: Any] ?? [:]
            rows.append(Sample(t: Int64(t), org: item["org"] as? String ?? "",
                               fh: (u["fh"] as? Double) ?? 0, sd: (u["sd"] as? Double) ?? 0))
        }
        rows.sort { $0.t < $1.t }
        stamp = (mtime, size)
        return (rows, rows.isEmpty ? tr("err.file_empty") : "")
    }

    // MARK: - public

    func organizations() -> [String] {
        load()
        return orgs
    }

    func series(org: String?, sinceMs: Int64?) -> [Sample] {
        load()
        let o = pickOrg(org)
        var rows = samples.filter { o.isEmpty || $0.org == o }
        if let since = sinceMs { rows = rows.filter { $0.t >= since } }
        return rows
    }

    private func pickOrg(_ org: String?) -> String {
        if let o = org, orgs.contains(o) { return o }
        return orgs.first ?? ""
    }

    func read(org: String?) -> Metrics {
        load()
        var m = Metrics()
        m.orgs = orgs
        if samples.isEmpty {
            m.error = error.isEmpty ? tr("err.no_usage_data") : error
            return m
        }
        let o = pickOrg(org)
        let rows = samples.filter { o.isEmpty || $0.org == o }
        guard let last = rows.last else {
            m.error = tr("err.no_data_profile")
            return m
        }
        let now = nowMs()
        m.ok = true
        m.org = o
        m.updatedAt = last.t
        m.sampleCount = rows.count

        let fhRows = rows.map { ($0.t, $0.fh) }
        let sdRows = rows.map { ($0.t, $0.sd) }

        var g = Gauge()
        g.value = last.fh
        let (start, certain) = Analysis.windowStart(fhRows, spanMs: fiveHoursMs)
        if let s = start { g.resetAt = s + fiveHoursMs; g.resetCertain = certain }
        g.burn = Analysis.burn(fhRows, nowMs: now, windowMs: 3_600_000)
        if g.burn == 0 { g.burn = Analysis.burn(fhRows, nowMs: now, windowMs: 3 * 3_600_000) }
        if g.burn > 0.2 && g.value < 100 { g.etaMs = Int64(g.remaining / g.burn * 3_600_000) }
        g.spark = Analysis.spark(fhRows, nowMs: now, spanMs: fiveHoursMs, points: 48)
        m.fiveHour = g

        var w = Gauge()
        w.value = last.sd
        let (wstart, wcertain) = Analysis.windowStart(sdRows, spanMs: weekMs)
        if let s = wstart { w.resetAt = s + weekMs; w.resetCertain = wcertain }
        w.burn = Analysis.burn(sdRows, nowMs: now, windowMs: 6 * 3_600_000)
        if w.burn > 0.05 && w.value < 100 { w.etaMs = Int64(w.remaining / w.burn * 3_600_000) }
        w.pace = Analysis.weeklyPace(value: w.value, resetAt: w.resetAt, nowMs: now)
        w.spark = Analysis.spark(sdRows, nowMs: now, spanMs: weekMs, points: 64)
        m.weekly = w
        return m
    }

    /// Samples of the last week from the log, only when it holds a single account (used by the
    /// claude.ai source to backfill its own history after a restart).
    func backfillSamples() -> [Sample] {
        let rows: [Sample]? = Bookmarks.withAccess(settings.desktopLogBookmark) { url in
            guard let data = try? Data(contentsOf: url),
                  let raw = (try? JSONSerialization.jsonObject(with: data)) as? [String: Any],
                  let items = raw["samples"] as? [[String: Any]] else { return [] }
            let orgs = Set(items.map { ($0["org"] as? String) ?? "" })
            if orgs.count != 1 { return [] }
            let cutoff = nowMs() - weekMs
            return items.compactMap { item -> Sample? in
                guard let t = item["t"] as? Double, Int64(t) >= cutoff else { return nil }
                let u = item["u"] as? [String: Any] ?? [:]
                return Sample(t: Int64(t), org: "", fh: (u["fh"] as? Double) ?? 0, sd: (u["sd"] as? Double) ?? 0)
            }
        }
        return rows ?? []
    }
}
