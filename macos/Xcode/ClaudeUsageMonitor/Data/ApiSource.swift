// Server-side usage from the https://api.anthropic.com/api/oauth/usage endpoint with an OAuth
// Bearer token (port of claude_usage/apisource.py). The network runs on a background queue;
// read() never blocks and answers from the last result. Compiled only with CLAUDE_SIGN_IN.

import Foundation

#if CLAUDE_SIGN_IN

final class ApiSource: UsageSource {
    // Polling cadence: the usage endpoint rate-limits, so the interval stretches on 429 and
    // shrinks again while the server answers.
    static let baseInterval = 120.0
    static let maxInterval = 600.0
    static let manualRetries = 5
    static let autoRetries = 1
    static let retryDelays: [Double] = [8, 15, 25, 40, 60]
    static let refreshMargin = 15.0 * 60           // renew the access token this long BEFORE expiry
    static let profileEvery = 6.0 * 3600
    static let profileRetry = 30.0 * 60
    static let planNames = ["claude_pro": "pro", "claude_max": "max", "claude_team": "team", "claude_enterprise": "enterprise"]
    static let legacyRows: [(String, String, String, String)] = [
        ("seven_day_opus", "model:Opus", "model", "Opus"),
        ("seven_day_sonnet", "model:Sonnet", "model", "Sonnet"),
        ("seven_day_oauth_apps", "surface:oauth_apps", "surface", "@oauth_apps"),
        ("seven_day_cowork", "kind:seven_day_cowork", "other", "@cowork"),
        ("seven_day_routines", "kind:seven_day_routines", "other", "@cowork"),
        ("cinder_cove", "kind:cinder_cove", "other", "Cinder Cove"),
    ]
    /// the saved limit resets travel under a server code name
    static let resetsKey = "cedar_ember"

    /// A window kind that contains one of these words is the Routines (Cowork) window.
    static func isCoworkKind(_ kind: String) -> Bool {
        let k = kind.lowercased()
        return k.contains("cowork") || k.contains("routine")
    }
    static let historyMax = 4000
    static let historySaveEvery = 60.0

    private let lock = NSLock()
    private let queue = DispatchQueue(label: "hu.dinorr.claudeusagemonitor.api", qos: .utility)
    private var tokens: OAuthTokens?
    private let onTokensChanged: (OAuthTokens) -> Void
    private var raw: [String: Any]? = nil
    private var fetchedAt: Int64? = nil
    private var error = ""
    private var inflight = false
    private var forcePending = false
    private var lastFetch = 0.0
    private var interval = ApiSource.baseInterval
    private var retryAt: Double? = nil
    private var retriesLeft = 0
    private var retryNo = 0
    private var lastStatus = 0
    private var series: [Sample] = []
    private var savedAt = 0.0
    private var limitsLogged = false
    private var profile: ProfileInfo? = nil
    private var profileNext = 0.0
    private var needsLoginFlag = false

    var modelFilter = "Fable"

    init(tokens: OAuthTokens?, backfill: [Sample], onTokensChanged: @escaping (OAuthTokens) -> Void) {
        self.tokens = tokens
        self.onTokensChanged = onTokensChanged
        self.series = ApiSource.merge(ApiSource.loadHistory(), backfill)
    }

    // MARK: - history on disk (survives restarts and updates)

    private static var historyURL: URL { AppInfo.supportDirectory.appendingPathComponent("api-history.json") }

    private static func loadHistory() -> [Sample] {
        guard let data = try? Data(contentsOf: historyURL),
              let raw = (try? JSONSerialization.jsonObject(with: data)) as? [String: Any],
              let rows = raw["samples"] as? [[Double]] else { return [] }
        let cutoff = nowMs() - weekMs
        var out = rows.compactMap { r -> Sample? in
            guard r.count >= 3, Int64(r[0]) >= cutoff else { return nil }
            return Sample(t: Int64(r[0]), org: "", fh: r[1], sd: r[2], mo: r.count > 3 ? r[3] : 0)
        }
        out.sort { $0.t < $1.t }
        return Array(out.suffix(historyMax))
    }

    /// Fills the gaps of the saved series from Claude Desktop's log, where no own sample lies within 5 minutes.
    private static func merge(_ series: [Sample], _ extra: [Sample]) -> [Sample] {
        if extra.isEmpty { return series }
        let have = series.map { $0.t }.sorted()
        let near: Int64 = 5 * 60 * 1000
        func covered(_ t: Int64) -> Bool {
            var lo = 0, hi = have.count
            while lo < hi { let mid = (lo + hi) / 2; if have[mid] < t { lo = mid + 1 } else { hi = mid } }
            for j in [lo - 1, lo] where j >= 0 && j < have.count { if abs(have[j] - t) <= near { return true } }
            return false
        }
        let added = extra.filter { !covered($0.t) }
        if added.isEmpty { return series }
        Log.api("history: \(added.count) sample(s) filled in from the Claude Desktop log")
        return Array((series + added).sorted { $0.t < $1.t }.suffix(historyMax))
    }

    private static func saveHistory(_ series: [Sample]) {
        let rows = series.map { [Double($0.t), $0.fh, $0.sd, $0.mo] }
        guard let data = try? JSONSerialization.data(withJSONObject: ["v": 1, "samples": rows]) else { return }
        do { try data.write(to: historyURL, options: .atomic) } catch { Log.api("history save failed: \(error)") }
    }

    // MARK: - token

    func setTokens(_ t: OAuthTokens?) {
        lock.lock(); defer { lock.unlock() }
        tokens = t
        raw = nil
        error = ""
        needsLoginFlag = false
        lastFetch = 0
        retryAt = nil
        retriesLeft = 0
        interval = ApiSource.baseInterval
        profile = nil
        profileNext = 0
    }

    var hasTokens: Bool { lock.lock(); defer { lock.unlock() }; return !(tokens?.accessToken ?? "").isEmpty }
    var needsLogin: Bool { lock.lock(); defer { lock.unlock() }; return needsLoginFlag }
    var lastError: String { lock.lock(); defer { lock.unlock() }; return error }
    var busy: Bool { lock.lock(); defer { lock.unlock() }; return inflight || forcePending }
    var rateLimited: Bool { lock.lock(); defer { lock.unlock() }; return lastStatus == 429 }
    var retryIn: Double? {
        lock.lock(); defer { lock.unlock() }
        guard let r = retryAt else { return nil }
        return max(0, r - Date().timeIntervalSince1970)
    }

    private func validAccessToken() -> (String, String) {
        lock.lock(); let t = tokens; lock.unlock()
        let access = t?.accessToken ?? ""
        let now = Date().timeIntervalSince1970
        var due = false
        if let exp = t?.expiresAt { due = Double(exp) - ApiSource.refreshMargin <= now }
        let needRefresh = access.isEmpty || due
        if needRefresh, let rt = t?.refreshToken, !rt.isEmpty {
            let (new, err) = OAuth.refresh(rt)
            if let new = new, !new.accessToken.isEmpty {
                lock.lock(); tokens = new; lock.unlock()
                onTokensChanged(new)
                return (new.accessToken, "")
            }
            if OAuth.isDeadGrant(err) {
                lock.lock(); needsLoginFlag = true; lock.unlock()
                Log.api("sign-in finished, no more attempts until a new login: \(err)")
                return ("", tr("err.signin_needed"))
            }
            if !access.isEmpty, !(t?.expiresAt.map { Double($0) <= now } ?? false) {
                Log.api("early refresh failed, the current token is still valid: \(err)")
                return (access, "")
            }
            Log.api("token refresh failed: \(err)")
            return ("", tr("err.session_expired"))
        }
        if access.isEmpty { return ("", tr("err.not_signed_in")) }
        return (access, "")
    }

    // MARK: - network

    func refreshAsync(force: Bool = false) {
        let now = Date().timeIntervalSince1970
        lock.lock()
        if needsLoginFlag { lock.unlock(); return }
        if inflight {
            if force { forcePending = true }
            lock.unlock(); return
        }
        let retryDue = retryAt != nil && now >= retryAt!
        if !force && !retryDue && (now - lastFetch) < interval { lock.unlock(); return }
        if !retryDue || force {
            retriesLeft = force ? ApiSource.manualRetries : ApiSource.autoRetries
            retryNo = 0
        }
        retryAt = nil
        inflight = true
        lastFetch = now
        lock.unlock()
        queue.async { self.worker() }
    }

    func forceRefresh() { refreshAsync(force: true) }

    private func worker() {
        defer {
            lock.lock()
            inflight = false
            let again = forcePending
            forcePending = false
            lock.unlock()
            if again { refreshAsync(force: true) }
        }
        let (access, err) = validAccessToken()
        if access.isEmpty {
            lock.lock(); error = err; lock.unlock()
            Log.api("no access token: \(err)")
            return
        }
        var (raw, status, ferr, retryAfter) = OAuth.fetchUsage(access)
        lock.lock(); let refreshToken = tokens?.refreshToken ?? ""; lock.unlock()
        if status == 401 && !refreshToken.isEmpty {
            Log.api("401 -> token refresh and retry")
            let (new, rerr) = OAuth.refresh(refreshToken)
            if let new = new, !new.accessToken.isEmpty {
                lock.lock(); tokens = new; lock.unlock()
                onTokensChanged(new)
                (raw, status, ferr, retryAfter) = OAuth.fetchUsage(new.accessToken)
            } else if OAuth.isDeadGrant(rerr) {
                lock.lock(); needsLoginFlag = true; error = tr("err.signin_needed"); lock.unlock()
                Log.api("sign-in finished after 401: \(rerr)")
                return
            } else {
                Log.api("token refresh failed: \(rerr)")
            }
        }
        let now = nowMs()
        lock.lock()
        lastStatus = status
        if let raw = raw, status == 200 {
            self.raw = raw
            fetchedAt = now
            error = ""
            retriesLeft = 0
            interval = max(ApiSource.baseInterval, interval * 0.75)
            appendSeries(raw, now: now)
            Log.api("OK 200")
            if !limitsLogged {
                limitsLogged = true
                logShape(raw)
            }
        } else if status == 401 || status == 403 {
            error = tr("err.session_expired_nl")
            Log.api("\(status) auth error")
        } else {
            if status == 429 {
                interval = min(ApiSource.maxInterval, interval * 1.5)
                error = tr("err.rate_limited")
            } else {
                error = ferr.isEmpty ? tr("err.query_http", status) : ferr
            }
            if retriesLeft > 0 {
                retriesLeft -= 1
                var delay = ApiSource.retryDelays[min(retryNo, ApiSource.retryDelays.count - 1)]
                retryNo += 1
                if let ra = retryAfter { delay = max(delay, min(ra, 300)) }
                retryAt = Date().timeIntervalSince1970 + delay
                Log.api("status=\(status) -> retry in \(Int(delay))s (left \(retriesLeft), interval \(Int(interval))s)")
            } else {
                Log.api("status=\(status) -> giving up until the next poll (interval \(Int(interval))s) \(String(ferr.prefix(80)))")
            }
        }
        lock.unlock()
        if status == 200 { maybeFetchProfile() }
    }

    /// Once per run: which limits the server reports (field NAMES only, never values that identify anyone).
    private func logShape(_ raw: [String: Any]) {
        var shape: [String] = []
        for (key, val) in raw {
            if let d = val as? [String: Any] { shape.append("\(key){\(d.keys.sorted().joined(separator: ","))}") }
            else if let a = val as? [Any] {
                let inner = Set(a.compactMap { $0 as? [String: Any] }.flatMap { $0.keys }).sorted()
                shape.append("\(key)[\(a.count)]{\(inner.joined(separator: ","))}")
            } else { shape.append("\(key):\(type(of: val))") }
        }
        Log.api("response shape: " + String(shape.joined(separator: " | ").prefix(900)))
        for lim in (raw["limits"] as? [[String: Any]]) ?? [] {
            let sc = lim["scope"] as? [String: Any] ?? [:]
            let model = (sc["model"] as? [String: Any])?["display_name"] ?? "-"
            Log.api("limit kind=\(lim["kind"] ?? "-") group=\(lim["group"] ?? "-") model=\(model) percent=\(lim["percent"] ?? "-") active=\(lim["is_active"] ?? "-")")
        }
        if let rs = ApiSource.pickResets(raw) {
            Log.api("saved resets: count=\(rs.count) total=\(rs.total) eligible=\(rs.eligible) expires_at=\(rs.expiresAt.map { String($0) } ?? "-")")
        } else {
            Log.api("saved resets: no block in the answer")
        }
    }

    private func maybeFetchProfile() {
        let now = Date().timeIntervalSince1970
        lock.lock()
        if now < profileNext { lock.unlock(); return }
        profileNext = now + ApiSource.profileRetry
        let access = tokens?.accessToken ?? ""
        lock.unlock()
        if access.isEmpty { return }
        let (raw, status) = OAuth.fetchProfile(access)
        guard let raw = raw else { Log.api("profile: status=\(status)"); return }
        let org = raw["organization"] as? [String: Any] ?? [:]
        let acc = raw["account"] as? [String: Any] ?? [:]
        let orgType = org["organization_type"] as? String ?? ""
        var info = ProfileInfo()
        info.plan = ApiSource.planNames[orgType] ?? ""
        info.tier = org["rate_limit_tier"] as? String ?? ""
        info.name = (acc["display_name"] as? String) ?? (acc["full_name"] as? String) ?? ""
        info.orgType = orgType
        info.billingType = org["billing_type"] as? String ?? ""
        info.hasExtraUsage = org["has_extra_usage_enabled"] as? Bool
        info.createdAt = acc["created_at"] as? String ?? ""
        lock.lock()
        profile = info
        profileNext = now + ApiSource.profileEvery
        lock.unlock()
        Log.api("profile: plan=\(info.plan.isEmpty ? "?" : info.plan) tier=\(info.tier.isEmpty ? "?" : info.tier) org_type=\(orgType.isEmpty ? "?" : orgType)")
    }

    // MARK: - analysis

    private static func percent(_ v: Any?) -> Double { (v as? Double) ?? ((v as? Int).map(Double.init) ?? 0) }
    private static func isNumber(_ v: Any?) -> Bool { v is Double || v is Int }

    /// Every limit besides the 5-hour window and the overall weekly one.
    static func pickRows(_ raw: [String: Any]) -> [DetailRow] {
        var rows: [DetailRow] = []
        var seen = Set<String>()
        func add(_ r: DetailRow) {
            let key = r.id.lowercased()
            if !seen.contains(key) { seen.insert(key); rows.append(r) }
        }
        let limits = (raw["limits"] as? [[String: Any]]) ?? []
        for lim in limits {
            let kind = lim["kind"] as? String ?? "", group = lim["group"] as? String ?? ""
            if kind == "five_hour" || group == "session" { continue }
            if let active = lim["is_active"] as? Bool, !active { continue }
            let scope = lim["scope"] as? [String: Any] ?? [:]
            let model = (scope["model"] as? [String: Any])?["display_name"] as? String
            var surface: String? = nil
            if let s = scope["surface"] as? [String: Any] {
                surface = (s["display_name"] as? String) ?? (s["name"] as? String) ?? (s["id"] as? String)
            } else if let s = scope["surface"] as? String { surface = s }
            let pct = percent(lim["percent"])
            let reset = parseIsoMs(lim["resets_at"])
            if let m = model, !m.isEmpty {
                add(DetailRow(id: "model:\(m)", category: "model", label: m, value: pct, resetAt: reset))
            } else if let s = surface, !s.isEmpty {
                add(DetailRow(id: "surface:\(s)", category: "surface", label: s, value: pct, resetAt: reset))
            } else if kind == "seven_day" || kind == "weekly_all" || group == "weekly_all" {
                continue
            } else if isCoworkKind(kind) {
                add(DetailRow(id: "kind:\(kind)", category: "other", label: "@cowork", value: pct, resetAt: reset))
            } else {
                var label = kind.replacingOccurrences(of: "_", with: " ").trimmingCharacters(in: .whitespaces).capitalized
                if label.isEmpty { label = group }
                add(DetailRow(id: "kind:\(kind.isEmpty ? group : kind)", category: "other", label: label, value: pct, resetAt: reset))
            }
        }
        let hasSurface = rows.contains { $0.category == "surface" }
        for (key, rid, category, label) in legacyRows {
            guard let win = raw[key] as? [String: Any], isNumber(win["utilization"]) else { continue }
            if category == "surface" && hasSurface { continue }
            add(DetailRow(id: rid, category: category, label: label, value: percent(win["utilization"]), resetAt: parseIsoMs(win["resets_at"])))
        }
        // any other filled top-level window (server code names)
        var known: Set<String> = ["five_hour", "seven_day", "extra_usage", "limits"]
        for (k, _, _, _) in legacyRows { known.insert(k) }
        var taken: [(Double, Int64?)] = rows.map { ($0.value, $0.resetAt) }
        for base in ["five_hour", "seven_day"] {
            if let win = raw[base] as? [String: Any], isNumber(win["utilization"]) {
                taken.append((percent(win["utilization"]), parseIsoMs(win["resets_at"])))
            }
        }
        for lim in limits where isNumber(lim["percent"]) { taken.append((percent(lim["percent"]), parseIsoMs(lim["resets_at"]))) }
        func repeats(_ value: Double, _ reset: Int64?) -> Bool {
            for (v, rs) in taken {
                let sameReset = (rs == nil && reset == nil) || (rs != nil && reset != nil && abs(rs! - reset!) < 120_000)
                if abs(v - value) < 0.75 && sameReset { return true }
            }
            return false
        }
        for (key, val) in raw {
            guard !known.contains(key), let win = val as? [String: Any], isNumber(win["utilization"]) else { continue }
            let util = percent(win["utilization"])
            let reset = parseIsoMs(win["resets_at"])
            if util <= 0 && reset == nil { continue }
            if repeats(util, reset) { continue }
            let label = isCoworkKind(key) ? "@cowork" : key.replacingOccurrences(of: "_", with: " ").capitalized
            add(DetailRow(id: "kind:\(key)", category: "other", label: label, value: util, resetAt: reset))
        }
        return rows
    }

    /// The saved limit resets. The block is not documented, so this reads it leniently: a grant is
    /// any object with `resets_left`; it counts when it is not paused, has started and has not
    /// expired. nil when the server sent no such block at all.
    static func pickResets(_ raw: [String: Any]) -> ResetGrants? {
        guard let block = raw[resetsKey], !(block is NSNull) else { return nil }
        let now = nowMs()
        func grants(_ obj: Any) -> [[String: Any]] {
            if let list = obj as? [Any] { return list.flatMap { grants($0) } }
            guard let dict = obj as? [String: Any] else { return [] }
            if dict["resets_left"] != nil { return [dict] }
            return dict.values.flatMap { grants($0) }
        }
        var eligible = true
        if let d = block as? [String: Any], let e = d["eligible"] as? Bool { eligible = e }
        var count = 0, total = 0
        var expires: Int64? = nil
        for g in grants(block) {
            guard isNumber(g["resets_left"]) else { continue }
            if (g["paused"] as? Bool) == true { continue }
            let start = parseIsoMs(g["starts_at"]), end = parseIsoMs(g["ends_at"])
            if let s = start, s > now { continue }
            if let e = end, e <= now { continue }
            let left = max(0, Int(percent(g["resets_left"])))
            count += left
            total += isNumber(g["resets_total"]) ? max(left, Int(percent(g["resets_total"]))) : left
            if left > 0, let e = end, expires == nil || e < expires! { expires = e }
        }
        if !eligible { count = 0 }
        return ResetGrants(count: count, total: total, expiresAt: expires, eligible: eligible)
    }

    /// This week's usage split by product (`seven_day_breakdown`): every device of the account.
    /// Rows with a 0 % share are left out; an absent or malformed block gives [].
    static func pickProducts(_ raw: [String: Any]) -> [ProductShare] {
        guard let block = raw["seven_day_breakdown"] as? [String: Any], let rows = block["rows"] as? [[String: Any]] else { return [] }
        var out: [ProductShare] = []
        for row in rows {
            guard isNumber(row["percent"]) else { continue }
            let pct = percent(row["percent"])
            if pct <= 0 { continue }
            let key = (row["key"] as? String ?? "").trimmingCharacters(in: .whitespaces)
            let label = (row["display_name"] as? String ?? "").trimmingCharacters(in: .whitespaces)
            if key.isEmpty && label.isEmpty { continue }
            out.append(ProductShare(key: key.isEmpty ? label.lowercased() : key, label: label, percent: pct))
        }
        return out
    }

    /// Which gauge's limit applies right now (the server marks it with `is_active`):
    /// "fh" (5-hour), "sd" (weekly), "mo" (the model gauge) or "" when it does not say.
    static func pickActive(_ raw: [String: Any], modelName: String) -> String {
        guard let limits = raw["limits"] as? [[String: Any]] else { return "" }
        for lim in limits where (lim["is_active"] as? Bool) == true {
            let kind = lim["kind"] as? String ?? "", group = lim["group"] as? String ?? ""
            let model = ((lim["scope"] as? [String: Any])?["model"] as? [String: Any])?["display_name"] as? String
            if kind == "five_hour" || group == "session" || kind == "session" { return "fh" }
            if let m = model, !m.isEmpty {
                return (!modelName.isEmpty && m.lowercased() == modelName.lowercased()) ? "mo" : ""
            }
            if kind == "seven_day" || kind == "weekly_all" || group == "weekly_all" || group == "weekly" { return "sd" }
        }
        return ""
    }

    static func pickExtra(_ raw: [String: Any]) -> ExtraUsage? {
        guard let ex = raw["extra_usage"] as? [String: Any] else { return nil }
        func money(_ v: Any?) -> Double? {
            if let d = v as? Double { return (d / 100 * 100).rounded() / 100 }
            if let i = v as? Int { return Double(i) / 100 }
            return nil
        }
        let limit = money(ex["monthly_limit"]), used = money(ex["used_credits"])
        var util: Double? = nil
        if isNumber(ex["utilization"]) { util = percent(ex["utilization"]) }
        else if let l = limit, l > 0, let u = used { util = u / l * 100 }
        return ExtraUsage(enabled: ex["is_enabled"] as? Bool ?? false, monthlyLimit: limit, used: used, utilization: util,
                          currency: (ex["currency"] as? String ?? "USD").uppercased(),
                          disabledReason: ex["disabled_reason"] as? String ?? "")
    }

    /// (five_hour, weekly) -> ((pct, reset), (pct, reset))
    static func pick(_ raw: [String: Any]) -> ((Double, Int64?), (Double, Int64?)) {
        guard let limits = raw["limits"] as? [[String: Any]] else { return ((0, nil), (0, nil)) }
        var five: (Double, Int64?) = (0, nil)
        var weekly: (Double, Int64?) = (0, nil)
        var weeklyScoped: (Double, Int64?) = (0, nil)
        for lim in limits {
            let kind = lim["kind"] as? String ?? "", group = lim["group"] as? String ?? ""
            let pct = percent(lim["percent"])
            let reset = parseIsoMs(lim["resets_at"])
            let hasModel = ((lim["scope"] as? [String: Any])?["model"]) != nil
            if kind == "five_hour" || group == "session" {
                five = (pct, reset)
            } else if kind == "seven_day" || group == "weekly_all" || group == "weekly" {
                if !hasModel { weekly = (pct, reset) }
                else if pct > weeklyScoped.0 { weeklyScoped = (pct, reset) }
            }
        }
        if weekly.0 == 0 && weekly.1 == nil && !(weeklyScoped.0 == 0 && weeklyScoped.1 == nil) { weekly = weeklyScoped }
        return (five, weekly)
    }

    /// The model-scoped weekly limit whose name/kind matches `filter`, else the first one; name "" when none.
    static func pickModel(_ raw: [String: Any], filter: String) -> (Double, Int64?, String) {
        guard let limits = raw["limits"] as? [[String: Any]] else { return (0, nil, "") }
        let filt = filter.trimmingCharacters(in: .whitespaces).lowercased()
        var first: (Double, Int64?, String)? = nil
        for lim in limits {
            let kind = lim["kind"] as? String ?? "", group = lim["group"] as? String ?? ""
            guard let model = ((lim["scope"] as? [String: Any])?["model"] as? [String: Any])?["display_name"] as? String, !model.isEmpty else { continue }
            let isWeekly = kind.hasPrefix("seven_day") || ["weekly", "weekly_all", "weekly_model"].contains(group)
            if !isWeekly { continue }
            let entry = (percent(lim["percent"]), parseIsoMs(lim["resets_at"]), model)
            if !filt.isEmpty && (model.lowercased().contains(filt) || kind.lowercased().contains(filt)) { return entry }
            if first == nil { first = entry }
        }
        return first ?? (0, nil, "")
    }

    private func appendSeries(_ raw: [String: Any], now: Int64) {
        let ((fh, _), (sd, _)) = ApiSource.pick(raw)
        let (mo, _, _) = ApiSource.pickModel(raw, filter: modelFilter)
        if let last = series.last, now - last.t < 1000 { return }
        series.append(Sample(t: now, org: "", fh: fh, sd: sd, mo: mo))
        let cutoff = now - weekMs
        series = Array(series.filter { $0.t >= cutoff }.suffix(ApiSource.historyMax))
        let t = Date().timeIntervalSince1970
        if t - savedAt >= ApiSource.historySaveEvery {
            savedAt = t
            ApiSource.saveHistory(series)
        }
    }

    private func spark(_ attr: KeyPath<Sample, Double>, spanMs: Int64, points: Int, series: [Sample]) -> [Double] {
        Analysis.spark(series.map { ($0.t, $0[keyPath: attr]) }, nowMs: nowMs(), spanMs: spanMs, points: points)
    }

    // MARK: - public

    func organizations() -> [String] { [] }

    func series(org: String?, sinceMs: Int64?) -> [Sample] {
        lock.lock(); let rows = series; lock.unlock()
        if let since = sinceMs { return rows.filter { $0.t >= since } }
        return rows
    }

    func read(org: String?) -> Metrics {
        refreshAsync()
        lock.lock()
        let raw = self.raw, fetched = fetchedAt, err = error, rows = series, prof = profile
        lock.unlock()
        var m = Metrics()
        m.profile = prof
        guard let raw = raw else {
            m.error = err.isEmpty ? tr("err.loading") : err
            return m
        }
        let ((fhVal, fhReset), (sdVal, sdReset)) = ApiSource.pick(raw)
        let now = nowMs()
        m.ok = true
        m.updatedAt = fetched
        m.sampleCount = rows.count

        var g = Gauge()
        g.value = fhVal; g.resetAt = fhReset; g.resetCertain = fhReset != nil
        let fhRows = rows.map { ($0.t, $0.fh) }
        g.burn = Analysis.burn(fhRows, nowMs: now, windowMs: 3_600_000)
        if g.burn == 0 { g.burn = Analysis.burn(fhRows, nowMs: now, windowMs: 3 * 3_600_000) }
        if g.burn > 0.2 && g.value < 100 { g.etaMs = Int64(g.remaining / g.burn * 3_600_000) }
        g.spark = spark(\.fh, spanMs: fiveHoursMs, points: 48, series: rows)
        m.fiveHour = g

        var w = Gauge()
        w.value = sdVal; w.resetAt = sdReset; w.resetCertain = sdReset != nil
        let sdRows = rows.map { ($0.t, $0.sd) }
        w.burn = Analysis.burn(sdRows, nowMs: now, windowMs: 6 * 3_600_000)
        if w.burn > 0.05 && w.value < 100 { w.etaMs = Int64(w.remaining / w.burn * 3_600_000) }
        w.pace = Analysis.weeklyPace(value: w.value, resetAt: sdReset, nowMs: now)
        w.spark = spark(\.sd, spanMs: weekMs, points: 64, series: rows)
        m.weekly = w

        m.rows = ApiSource.pickRows(raw)
        m.extra = ApiSource.pickExtra(raw)
        m.resets = ApiSource.pickResets(raw)
        m.products = ApiSource.pickProducts(raw)

        let (moVal, moReset, moName) = ApiSource.pickModel(raw, filter: modelFilter)
        m.active = ApiSource.pickActive(raw, modelName: moName)
        if !moName.isEmpty {
            var mg = Gauge()
            m.modelName = moName
            mg.value = moVal; mg.resetAt = moReset; mg.resetCertain = moReset != nil
            let moRows = rows.map { ($0.t, $0.mo) }
            mg.burn = Analysis.burn(moRows, nowMs: now, windowMs: 6 * 3_600_000)
            if mg.burn > 0.05 && mg.value < 100 { mg.etaMs = Int64(mg.remaining / mg.burn * 3_600_000) }
            mg.pace = Analysis.weeklyPace(value: mg.value, resetAt: moReset, nowMs: now)
            mg.spark = spark(\.mo, spanMs: weekMs, points: 64, series: rows)
            m.model = mg
        }
        return m
    }
}

#endif
