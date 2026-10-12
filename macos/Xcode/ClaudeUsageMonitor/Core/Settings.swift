// Settings - the same keys as the Windows app (claude_usage/settings.py), kept in UserDefaults
// (the place Apple expects an app's preferences; it lives inside the sandbox container).
//
// The `@Stored` wrapper publishes every change through `objectWillChange`, so SwiftUI views and
// the AppKit controller both follow the user's changes without any extra plumbing.

import Combine
import Foundation

@propertyWrapper
struct Stored<Value> {
    let key: String
    let defaultValue: Value

    init(_ key: String, _ defaultValue: Value) {
        self.key = key
        self.defaultValue = defaultValue
    }

    static subscript<T: ObservableObject>(
        _enclosingInstance instance: T,
        wrapped _: ReferenceWritableKeyPath<T, Value>,
        storage storageKeyPath: ReferenceWritableKeyPath<T, Self>
    ) -> Value where T.ObjectWillChangePublisher == ObservableObjectPublisher {
        get {
            let w = instance[keyPath: storageKeyPath]
            if let v = UserDefaults.standard.object(forKey: w.key) as? Value { return v }
            return w.defaultValue
        }
        set {
            let w = instance[keyPath: storageKeyPath]
            instance.objectWillChange.send()
            UserDefaults.standard.set(newValue, forKey: w.key)
        }
    }

    @available(*, unavailable, message: "@Stored only works inside an ObservableObject")
    var wrappedValue: Value {
        get { fatalError() }
        set { fatalError() }
    }
}

enum AppInfo {
    static let name = "Claude Usage Monitor"
    static var version: String {
        (Bundle.main.object(forInfoDictionaryKey: "CFBundleShortVersionString") as? String) ?? "0.0.0"
    }
    static var build: String { (Bundle.main.object(forInfoDictionaryKey: "CFBundleVersion") as? String) ?? "0" }
    static let site = "https://claudeusagemonitor.com/"
    static let repo = "https://github.com/gaborvidovics76/ClaudeUsageMonitor"
    static let author = "Vidovics Gábor"
    static let feedbackURL = "https://claudeusagemonitor.com/usage-api/app-feedback.php"
    /// Filled in once the app exists in App Store Connect (the numeric id in the store URL).
    /// Empty = the "Rate on the App Store" items stay hidden.
    static let appStoreID = ""

    static var appStoreURL: URL? {
        appStoreID.isEmpty ? nil : URL(string: "macappstore://apps.apple.com/app/id\(appStoreID)?action=write-review")
    }

    /// The website in the program's language (/ = English, /hu/, /pt-pt/, /zh-cn/ ...).
    static func siteURL(lang: String? = nil, fragment: String = "") -> URL {
        let code = lang ?? L10n.current
        var s = site
        if code != "" && code != "en" { s += (L10n.siteFolder[code] ?? code.lowercased()) + "/" }
        if !fragment.isEmpty { s += "#" + fragment }
        return URL(string: s)!
    }

    /// ~/Library/Application Support/ClaudeUsageMonitor inside the sandbox container.
    static var supportDirectory: URL {
        let base = FileManager.default.urls(for: .applicationSupportDirectory, in: .userDomainMask).first!
        let dir = base.appendingPathComponent("ClaudeUsageMonitor", isDirectory: true)
        try? FileManager.default.createDirectory(at: dir, withIntermediateDirectories: true)
        return dir
    }

    /// The user's real home folder (not the sandbox container): where Claude Desktop keeps its log.
    static var realHome: URL {
        if let pw = getpwuid(getuid()), let dir = pw.pointee.pw_dir {
            return URL(fileURLWithPath: String(cString: dir), isDirectory: true)
        }
        return FileManager.default.homeDirectoryForCurrentUser
    }

    /// ~/Library/Application Support/Claude/plan-usage-history.json (Claude Desktop's own log).
    static var defaultDesktopLog: URL {
        realHome.appendingPathComponent("Library/Application Support/Claude/plan-usage-history.json")
    }

    /// ~/.claude - Claude Code's folder (its logs live in ~/.claude/projects).
    static var defaultClaudeCodeFolder: URL { realHome.appendingPathComponent(".claude", isDirectory: true) }
}

let gaugeIDs = ["fh", "mo", "sd"]
let gaugeOrders = ["fh,mo,sd", "fh,sd,mo", "mo,fh,sd", "mo,sd,fh", "sd,fh,mo", "sd,mo,fh"]
let layouts = ["postit", "compact", "ring"]
let trayMetrics = ["five_hour", "weekly", "max"]

final class Settings: ObservableObject {
    // --- language
    @Stored("language", "") var language: String               // "" = system language

    // --- data source
    @Stored("source", "local") var source: String               // local | api | demo
    @Stored("org", "") var org: String
    @Stored("refresh_seconds", 5) var refreshSeconds: Int

    // --- appearance
    @Stored("visible", true) var visible: Bool
    @Stored("layout", "postit") var layout: String
    @Stored("theme", "midnight") var theme: String
    @Stored("accent", "") var accent: String
    @Stored("scale", 1.0) var scale: Double
    @Stored("opacity", 1.0) var opacity: Double
    @Stored("always_on_top", true) var alwaysOnTop: Bool
    @Stored("click_through", false) var clickThrough: Bool
    @Stored("locked", false) var locked: Bool
    @Stored("snap_edges", true) var snapEdges: Bool
    @Stored("show_in_dock", false) var showInDock: Bool
    @Stored("pos_set", false) var positionSaved: Bool
    @Stored("pos_x", 0.0) var posX: Double                      // window frame origin (AppKit coordinates)
    @Stored("pos_y", 0.0) var posY: Double

    // --- content
    @Stored("show_five_hour", true) var showFiveHour: Bool
    @Stored("show_weekly", true) var showWeekly: Bool
    @Stored("show_model", true) var showModel: Bool
    @Stored("model_filter", "Fable") var modelFilter: String
    @Stored("model_scale", 1.0) var modelScale: Double
    @Stored("gauge_order", "fh,mo,sd") var gaugeOrder: String
    @Stored("show_spark", true) var showSpark: Bool
    @Stored("show_plan_badge", true) var showPlanBadge: Bool
    @Stored("show_plan_name", false) var showPlanName: Bool
    @Stored("show_model_list", true) var showModelList: Bool
    @Stored("show_surfaces", true) var showSurfaces: Bool
    @Stored("show_extra_usage", true) var showExtraUsage: Bool
    @Stored("show_local_models", true) var showLocalModels: Bool
    @Stored("detail_hidden", [String]()) var detailHidden: [String]
    @Stored("show_burn", true) var showBurn: Bool
    @Stored("show_reset", true) var showReset: Bool
    @Stored("show_age", true) var showAge: Bool
    @Stored("show_feedback_icon", true) var showFeedbackIcon: Bool
    @Stored("tray_metric", "five_hour") var trayMetric: String

    // --- alerts
    @Stored("warn_threshold", 70) var warnThreshold: Int
    @Stored("danger_threshold", 90) var dangerThreshold: Int
    @Stored("notify_enabled", true) var notifyEnabled: Bool
    @Stored("notify_on_reset", true) var notifyOnReset: Bool
    @Stored("notify_stale", true) var notifyStale: Bool

    // --- system
    @Stored("first_run_done", false) var firstRunDone: Bool

    // --- sandbox: security-scoped bookmarks of the files the user granted access to
    @Stored("bookmark_desktop_log", Data()) var desktopLogBookmark: Data
    @Stored("bookmark_claude_code", Data()) var claudeCodeBookmark: Data

    var warn: Double { Double(warnThreshold) }
    var danger: Double { Double(dangerThreshold) }

    /// Configured gauge order; unknown or missing ids are appended in default order.
    var orderedGauges: [String] {
        var ids = gaugeOrder.split(separator: ",").map { $0.trimmingCharacters(in: .whitespaces) }.filter { gaugeIDs.contains($0) }
        for g in gaugeIDs where !ids.contains(g) { ids.append(g) }
        return ids
    }

    var clampedModelScale: Double { max(0.5, min(2.0, modelScale)) }

    func isHidden(_ rowID: String) -> Bool { detailHidden.contains(rowID) }

    func setHidden(_ rowID: String, _ hidden: Bool) {
        var list = detailHidden.filter { $0 != rowID }
        if hidden { list.append(rowID) }
        detailHidden = list
    }

    /// Restore the defaults (the bookmarks and the first-run flag are kept).
    func reset() {
        let keep = ["first_run_done", "bookmark_desktop_log", "bookmark_claude_code", "language"]
        let d = UserDefaults.standard
        for (key, _) in d.dictionaryRepresentation() where !keep.contains(key) && !key.hasPrefix("NS") && !key.hasPrefix("Apple") && !key.hasPrefix("com.apple") {
            d.removeObject(forKey: key)
        }
        objectWillChange.send()
    }
}
