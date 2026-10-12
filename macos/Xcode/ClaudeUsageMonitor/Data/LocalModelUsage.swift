// Per-model usage from Claude Code's own local logs (port of claude_usage/localmodels.py).
//
// Claude Code writes every assistant turn to <config>/projects/**/*.jsonl with the model id and
// the token counts. From those files this works out how this week's work on THIS machine is
// split between the models. Only the timestamp, the model id and the token counts are read;
// message contents are never kept, logged or sent anywhere.
//
// Sandbox: the folder (~/.claude by default) must be chosen once by the user in the Open panel
// (Settings -> Details). Without that grant the group simply stays hidden.

import Foundation

struct ModelShare {
    var name: String            // "Opus 4.8"
    var share: Double           // percent of the weighted tokens in the window
    var outputTokens: Int
    var totalTokens: Int
    var turns: Int
}

final class LocalModelUsage {
    static let weekS = 7.0 * 86400
    static let scanEvery = 300.0
    static let keepS = 8.0 * 86400
    static let passTimeBudget = 12.0
    static let passByteBudget = 400 * 1024 * 1024
    static let maxLineBytes = 64 * 1024 * 1024
    static let maxFilesPerPass = 5000
    static let stuckAfter = 180.0
    static let maxEntries = 400_000
    static let wInput = 1.0, wOutput = 5.0, wCacheWrite = 1.25, wCacheRead = 0.1

    typealias Entry = (ts: Double, model: String, weighted: Double, out: Int, total: Int, key: String)

    private let settings: Settings
    private let lock = NSLock()
    private let queue = DispatchQueue(label: "hu.dinorr.claudeusagemonitor.localmodels", qos: .background)
    private var running = false
    private var threadStarted = 0.0
    private var generation = 0
    private var offsets: [String: Int] = [:]
    private var entries: [Entry] = []
    private var seen = Set<String>()
    private var lastScan = 0.0
    private(set) var version = 0
    private(set) var scannedOnce = false
    private(set) var lastNote = ""
    var enabled = true

    init(settings: Settings) { self.settings = settings }

    var hasAccess: Bool { Bookmarks.resolve(settings.claudeCodeBookmark) != nil }

    var busy: Bool {
        lock.lock(); defer { lock.unlock() }
        if !running { return false }
        return Date().timeIntervalSince1970 - threadStarted <= LocalModelUsage.stuckAfter
    }

    /// Another folder was chosen -> start from scratch.
    func resetState() {
        lock.lock()
        offsets.removeAll(); entries.removeAll(); seen.removeAll()
        lastScan = 0
        lock.unlock()
    }

    /// claude-opus-4-8 -> Opus 4.8 · claude-3-5-sonnet-20241022 -> Sonnet 3.5
    static func prettyModel(_ id: String) -> String {
        var mid = id.trimmingCharacters(in: .whitespaces).lowercased()
        if let r = mid.range(of: #"-\d{8}$"#, options: .regularExpression) { mid.removeSubrange(r) }
        if mid.hasPrefix("claude-") { mid.removeFirst("claude-".count) }
        var words: [String] = [], nums: [String] = []
        for part in mid.split(separator: "-") {
            if part.allSatisfy({ $0.isNumber }) { nums.append(String(part)) }
            else if !part.isEmpty { words.append(part.prefix(1).uppercased() + part.dropFirst()) }
        }
        let name = words.isEmpty ? id : words.joined(separator: " ")
        return "\(name) \(nums.joined(separator: "."))".trimmingCharacters(in: .whitespaces)
    }

    @discardableResult
    func scan(force: Bool = false) -> Bool {
        if !enabled || busy { return false }
        let now = Date().timeIntervalSince1970
        if !force && now - lastScan < LocalModelUsage.scanEvery { return false }
        lock.lock()
        if running { generation += 1 }            // abandon the hung pass; its result will be ignored
        running = true
        threadStarted = now
        let gen = generation
        lock.unlock()
        lastScan = now
        queue.async { self.run(generation: gen) }
        return true
    }

    private func run(generation gen: Int) {
        let started = Date().timeIntervalSince1970
        var note = ""
        var new: [Entry] = []
        lock.lock(); var offs = offsets; lock.unlock()
        let cutoff = started - LocalModelUsage.keepS
        var budget = LocalModelUsage.passByteBudget
        var files = 0

        let scanned: Bool? = Bookmarks.withAccess(settings.claudeCodeBookmark) { root in
            var roots: [URL] = []
            let fm = FileManager.default
            var isDir: ObjCBool = false
            // a folder counts if it is called "projects" or contains one
            if root.lastPathComponent.lowercased() == "projects" { roots.append(root) }
            else if fm.fileExists(atPath: root.appendingPathComponent("projects").path, isDirectory: &isDir), isDir.boolValue {
                roots.append(root.appendingPathComponent("projects"))
            } else { roots.append(root) }      // the user knows best
            outer: for r in roots {
                guard let en = fm.enumerator(at: r, includingPropertiesForKeys: [.contentModificationDateKey, .fileSizeKey, .isRegularFileKey],
                                             options: [.skipsHiddenFiles, .skipsPackageDescendants]) else { continue }
                for case let url as URL in en {
                    guard url.pathExtension == "jsonl" else { continue }
                    if Date().timeIntervalSince1970 - started > LocalModelUsage.passTimeBudget || budget <= 0 || files >= LocalModelUsage.maxFilesPerPass {
                        note = "partial"; break outer
                    }
                    guard let vals = try? url.resourceValues(forKeys: [.contentModificationDateKey, .fileSizeKey, .isRegularFileKey]),
                          vals.isRegularFile == true, let mtime = vals.contentModificationDate, let size = vals.fileSize else { continue }
                    if mtime.timeIntervalSince1970 < cutoff { continue }
                    var offset = offs[url.path] ?? 0
                    if size < offset { offset = 0 }           // the file was rewritten
                    if size == offset { continue }
                    files += 1
                    let (newOffset, used, truncated) = self.readFile(url, offset: offset, cutoff: cutoff, out: &new, budget: budget, started: started)
                    offs[url.path] = newOffset
                    budget -= used
                    if truncated { note = "partial"; break outer }
                }
            }
            return true
        }
        if scanned == nil { note = "no log folder" }

        lock.lock()
        if gen != generation { lock.unlock(); return }
        let cut = Date().timeIntervalSince1970 - LocalModelUsage.keepS
        var all = entries.filter { $0.ts >= cut } + new
        if all.count > LocalModelUsage.maxEntries { all = Array(all.suffix(LocalModelUsage.maxEntries)) }
        entries = all
        seen = Set(all.map { $0.key }.filter { !$0.isEmpty })
        offsets = offs
        scannedOnce = true
        lastNote = note
        version += 1
        running = false
        lock.unlock()
        if note == "partial" { lastScan = 0 }     // more to read - go on at the next tick
    }

    /// Reads new complete lines of one file. Returns (new offset, bytes read, stopped before the end).
    private func readFile(_ url: URL, offset: Int, cutoff: Double, out: inout [Entry], budget: Int, started: Double) -> (Int, Int, Bool) {
        guard let handle = try? FileHandle(forReadingFrom: url) else { return (offset, 0, false) }
        defer { try? handle.close() }
        var pos = offset
        var used = 0
        var truncated = false
        handle.seek(toFileOffset: UInt64(offset))
        var carry = Data()
        while true {
            if used >= budget || Date().timeIntervalSince1970 - started > LocalModelUsage.passTimeBudget {
                truncated = true; break
            }
            let chunk = handle.readData(ofLength: 1 << 20)
            if chunk.isEmpty { break }
            carry.append(chunk)
            while let nl = carry.firstIndex(of: 0x0A) {
                let line = carry.subdata(in: carry.startIndex..<nl)
                carry.removeSubrange(carry.startIndex...nl)
                pos += line.count + 1
                used += line.count + 1
                if let e = entry(line, cutoff: cutoff) { out.append(e) }
            }
            if carry.count > LocalModelUsage.maxLineBytes {   // not a log line - skip it
                pos += carry.count; used += carry.count; carry.removeAll()
            }
        }
        // a half-written last line stays for the next pass (pos does not include it)
        return (pos, used, truncated)
    }

    private static let usageMarker = Data("\"usage\"".utf8)
    private static let assistantMarker = Data("\"assistant\"".utf8)

    private func entry(_ line: Data, cutoff: Double) -> Entry? {
        // cheap pre-filter: only assistant turns carry usage
        guard line.range(of: LocalModelUsage.usageMarker) != nil, line.range(of: LocalModelUsage.assistantMarker) != nil else { return nil }
        guard let obj = (try? JSONSerialization.jsonObject(with: line)) as? [String: Any],
              let msg = obj["message"] as? [String: Any], let usage = msg["usage"] as? [String: Any] else { return nil }
        let model = msg["model"] as? String ?? ""
        if model.isEmpty || model.hasPrefix("<") { return nil }
        guard let tsText = obj["timestamp"] as? String, let tsMs = parseIsoMs(tsText) else { return nil }
        let ts = Double(tsMs) / 1000
        if ts < cutoff || ts > Date().timeIntervalSince1970 + 86400 { return nil }
        var key = "\(msg["id"] as? String ?? ""):\(obj["requestId"] as? String ?? "")"
        if key == ":" { key = "" }
        else {
            lock.lock()
            let dup = seen.contains(key)
            if !dup { seen.insert(key) }
            lock.unlock()
            if dup { return nil }
        }
        func n(_ name: String) -> Int {
            if let v = usage[name] as? Int, v >= 0, v < 1_000_000_000_000 { return v }
            if let v = usage[name] as? Double, v >= 0, v < 1e12 { return Int(v) }
            return 0
        }
        let i = n("input_tokens"), o = n("output_tokens")
        let cw = n("cache_creation_input_tokens"), cr = n("cache_read_input_tokens")
        let weighted = Double(i) * LocalModelUsage.wInput + Double(o) * LocalModelUsage.wOutput
            + Double(cw) * LocalModelUsage.wCacheWrite + Double(cr) * LocalModelUsage.wCacheRead
        return (ts, model, weighted, o, i + o + cw + cr, key)
    }

    /// Split of the weighted tokens since `windowStart` (default: the last 7 days).
    func shares(windowStart: Double?) -> [ModelShare] {
        let now = Date().timeIntervalSince1970
        var start = windowStart ?? (now - LocalModelUsage.weekS)
        start = min(max(start, now - LocalModelUsage.keepS), now)
        lock.lock(); let rows = entries; lock.unlock()
        var agg: [String: (Double, Int, Int, Int)] = [:]
        for e in rows where e.ts >= start {
            let name = LocalModelUsage.prettyModel(e.model)
            var a = agg[name] ?? (0, 0, 0, 0)
            a.0 += e.weighted; a.1 += e.out; a.2 += e.total; a.3 += 1
            agg[name] = a
        }
        let grand = agg.values.reduce(0) { $0 + $1.0 }
        if grand <= 0 { return [] }
        return agg.map { ModelShare(name: $0.key, share: $0.value.0 / grand * 100, outputTokens: $0.value.1, totalTokens: $0.value.2, turns: $0.value.3) }
            .sorted { $0.share > $1.share }
    }
}
