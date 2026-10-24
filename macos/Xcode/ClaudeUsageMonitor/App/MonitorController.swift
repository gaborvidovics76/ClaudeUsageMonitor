// Controller: the panel, the menu bar item, the timers, the menu, notifications and the windows
// (port of claude_usage/app.py).

import AppKit
import Combine
import SwiftUI

final class MonitorController {
    let settings = Settings()
    private let localReader: LocalLogReader
    private let demo = DemoSource()
    #if CLAUDE_SIGN_IN
    private var api: ApiSource!
    #endif
    private var reader: UsageSource
    private var metrics = Metrics()

    private let panelView: PanelView
    private let panel: PanelWindow
    private let statusBar = StatusBarController()
    private let localModels: LocalModelUsage

    private var timer: Timer?
    private var pulse: Timer?
    private var busyUntil = 0.0
    private var last: [String: Double] = [:]
    private var loginNotified = false
    private var staleNotified = false
    private var localSeen = -1
    private var localWindow: Double? = nil
    private var cancellables = Set<AnyCancellable>()
    private var applyScheduled = false

    private var settingsWindow: WindowHost<SettingsView>?
    private var historyWindow: WindowHost<HistoryView>?
    private var helpWindow: WindowHost<HelpView>?
    private var feedbackWindow: WindowHost<FeedbackView>?
    private var historyModel: HistoryModel?
    #if CLAUDE_SIGN_IN
    private var signInWindow: WindowHost<SignInView>?
    #endif

    init() {
        // language: saved value (migrated), or the system language if supported, else English
        if settings.language == "pt" || settings.language == "es" { settings.language = L10n.migrate(settings.language) }
        L10n.setLanguage(settings.language.isEmpty ? L10n.systemLanguage() : settings.language)

        localReader = LocalLogReader(settings: settings)
        localModels = LocalModelUsage(settings: settings)
        reader = localReader
        #if CLAUDE_SIGN_IN
        api = ApiSource(tokens: Keychain.loadTokens(), backfill: localReader.backfillSamples()) { tokens in
            Keychain.saveTokens(tokens)          // the background worker refreshed the token - keep it
        }
        #endif
        panelView = PanelView(settings: settings)
        panel = PanelWindow(settings: settings, view: panelView)

        panelView.onMenu = { [weak self] pos in self?.showMenu(at: pos) }
        panelView.onDoubleClick = { [weak self] in self?.showHistory() }
        panelView.onFeedback = { [weak self] in self?.showFeedback() }
        panelView.onMoved = { [weak self] in self?.panel.savePosition() }
        panelView.onScaleChanged = { [weak self] in self?.panel.applySettings() }

        statusBar.onToggle = { [weak self] in self?.togglePanel() }
        statusBar.onDoubleClick = { [weak self] in self?.showHistory() }
        statusBar.onMenu = { [weak self] in self?.buildMenu() ?? NSMenu() }

        // every settings change (menu, window, scroll wheel) is applied once, on the next run-loop turn
        settings.objectWillChange.sink { [weak self] _ in self?.scheduleApply() }.store(in: &cancellables)

        applySettings()
        refresh()

        if !settings.firstRunDone {
            settings.firstRunDone = true
            Notifier.shared.notify(AppInfo.name, tr("notify.first_run"))
            // the sandbox needs the user's choice of the log file (or the demo / claude.ai source)
            showSettings()
        }
    }

    // MARK: - setup

    private func scheduleApply() {
        if applyScheduled { return }
        applyScheduled = true
        DispatchQueue.main.async {
            self.applyScheduled = false
            self.applySettings()
        }
    }

    private var usingAPI: Bool {
        #if CLAUDE_SIGN_IN
        return reader === api
        #else
        return false
        #endif
    }

    func applySettings() {
        let s = settings
        switch s.source {
        case "demo":
            reader = demo
        case "api":
            #if CLAUDE_SIGN_IN
            api.modelFilter = s.modelFilter.trimmingCharacters(in: .whitespaces).isEmpty ? "Fable" : s.modelFilter.trimmingCharacters(in: .whitespaces)
            reader = api.hasTokens ? api : localReader
            #else
            reader = localReader
            #endif
        default:
            reader = localReader
        }
        NSApp.setActivationPolicy(s.showInDock ? .regular : .accessory)
        panel.applySettings()
        if s.visible { panel.orderFrontRegardless() } else { panel.orderOut(nil) }
        let interval = (usingAPI || reader === demo) ? 10 : max(2, s.refreshSeconds)
        timer?.invalidate()
        timer = Timer.scheduledTimer(withTimeInterval: TimeInterval(interval), repeats: true) { [weak self] _ in self?.refresh() }
        refresh()
    }

    // MARK: - data

    private func isBusy() -> Bool {
        var apiBusy = false
        #if CLAUDE_SIGN_IN
        apiBusy = usingAPI && api.busy
        #endif
        return apiBusy || Date().timeIntervalSince1970 < busyUntil
    }

    private func pulseTick() {
        if isBusy() {
            panelView.setActivity(busy: true, note: panelView.note, retryIn: panelView.retryIn)
            return
        }
        pulse?.invalidate()
        pulse = nil
        refresh()
    }

    private func syncActivity() {
        let busy = isBusy()
        var note = "", retryIn: Double? = nil
        #if CLAUDE_SIGN_IN
        if usingAPI {
            note = api.lastError
            retryIn = api.retryIn
            if api.needsLogin && !loginNotified {
                loginNotified = true
                Notifier.shared.notify(AppInfo.name, tr("notify.signin_needed"))
            } else if !api.needsLogin {
                loginNotified = false
            }
        }
        #endif
        panelView.setActivity(busy: busy, note: note, retryIn: retryIn)
        if busy && pulse == nil {
            pulse = Timer.scheduledTimer(withTimeInterval: 0.12, repeats: true) { [weak self] _ in self?.pulseTick() }
        }
    }

    func refresh() {
        metrics = reader.read(org: settings.org.isEmpty ? nil : settings.org)
        panelView.setMetrics(metrics)
        syncActivity()
        pollLocalModels()
        updateStatusBar()
        checkAlerts()
        if let h = historyWindow, h.isVisible { historyModel?.refresh() }
    }

    func forceRefresh() {
        busyUntil = Date().timeIntervalSince1970 + 0.9
        #if CLAUDE_SIGN_IN
        if usingAPI { api.forceRefresh() } else { localReader.invalidate() }
        #else
        localReader.invalidate()
        #endif
        refresh()
    }

    private func trayValue() -> Double {
        switch settings.trayMetric {
        case "weekly": return metrics.weekly.value
        case "max": return max(metrics.fiveHour.value, metrics.weekly.value)
        default: return metrics.fiveHour.value
        }
    }

    // MARK: - local model split

    private func pollLocalModels() {
        let lm = localModels
        lm.enabled = settings.showLocalModels && lm.hasAccess
        if !lm.enabled {
            if !panelView.localModels.isEmpty { panelView.setLocalModels([]) }
            return
        }
        lm.scan()
        let reset = metrics.ok ? metrics.weekly.resetAt : nil
        let window: Double? = reset.map { Double($0) / 1000 - 7 * 86400 }
        if lm.version != localSeen || window != localWindow {
            localSeen = lm.version
            localWindow = window
            panelView.setLocalModels(lm.shares(windowStart: window))
        } else if lm.busy {
            DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) { [weak self] in self?.pollLocalModels() }
        }
    }

    // MARK: - status bar

    private func updateStatusBar() {
        let pal = Palette(theme: settings.theme, accentHex: settings.accent)
        let m = metrics
        guard m.ok else {
            statusBar.update(value: nil, color: nil, tooltip: "\(AppInfo.name)\n\(m.error)")
            return
        }
        let value = trayValue()
        let color = pal.status(value, warn: settings.warn, danger: settings.danger)
        func line(_ label: String, _ g: Gauge) -> String {
            let reset = g.resetInMs.map { "  (\(tr("panel.reset", fmtDelta($0))))" } ?? ""
            return tr("tray.line", label, pct0(g.value)) + reset
        }
        var lines = [AppInfo.name, line(tr("panel.five_hour"), m.fiveHour)]
        if settings.showModel && m.hasModel { lines.append(line(tr("panel.model", m.modelName.uppercased()), m.model)) }
        lines.append(line(tr("panel.weekly"), m.weekly))
        for row in panelView.detailRows().filter({ $0.id != "@header" }).prefix(3) { lines.append("\(row.label): \(row.right)") }
        if let p = m.profile, !p.badge.isEmpty, settings.showPlanBadge { lines[0] = "\(AppInfo.name)  \u{b7}  \(p.badge)" }
        lines.append(tr("panel.updated", fmtAge(m.ageSeconds)))
        #if CLAUDE_SIGN_IN
        if usingAPI && !api.lastError.isEmpty {
            lines.append("! " + api.lastError.replacingOccurrences(of: "\n", with: " "))
            if let wait = api.retryIn { lines.append(tr("panel.retry_in", Int(wait) + 1)) }
        }
        #endif
        statusBar.update(value: value, color: color, tooltip: lines.joined(separator: "\n"))
    }

    private func checkAlerts() {
        let s = settings, m = metrics
        guard m.ok else { return }
        var gauges: [(String, String, Gauge)] = [("fh", tr("panel.five_hour"), m.fiveHour), ("sd", tr("panel.weekly"), m.weekly)]
        if m.hasModel { gauges.append(("mo", tr("panel.model", m.modelName.uppercased()), m.model)) }
        let rs = m.resets
        let hasReset = s.notifyResets && (rs?.count ?? 0) > 0
        for (key, label, gauge) in gauges {
            let prev = last[key]
            last[key] = gauge.value
            guard let prev = prev else { continue }
            if s.notifyEnabled {
                for level in [s.danger, s.warn] where prev < level && level <= gauge.value {
                    let extra = gauge.resetInMs.map { "  " + tr("panel.reset", fmtDelta($0)) } ?? ""
                    Notifier.shared.notify(label, tr("notify.threshold", label, pct0(gauge.value)) + extra)
                    break
                }
            }
            if s.notifyOnReset && prev > 15 && gauge.value <= 1 {
                Notifier.shared.notify(label, tr("notify.reset_done", label))
            }
            if hasReset && prev < 99.5 && gauge.value >= 99.5 {
                // the limit is full - and there is a saved reset the user may redeem right now
                Notifier.shared.notify(label, tr("notify.reset_available", label))
            }
        }
        // a saved reset that is about to expire unused: one reminder per grant, 3 days ahead
        if hasReset, let rs = rs, let left = rs.expiresInMs, left <= 3 * 86_400_000,
           let at = rs.expiresAt, s.resetsWarned != Double(at) {
            s.resetsWarned = Double(at)
            Notifier.shared.notify(tr("detail.resets"), tr("notify.reset_expiring", fmtDelta(left)))
        }
        if s.notifyStale {
            if m.stale && !staleNotified {
                staleNotified = true
                Notifier.shared.notify(tr("notify.stale_title"), tr("notify.stale_body", fmtAge(m.ageSeconds)))
            } else if !m.stale {
                staleNotified = false
            }
        }
    }

    // MARK: - menu

    func buildMenu() -> NSMenu {
        let s = settings, m = metrics
        let menu = NSMenu()
        menu.autoenablesItems = false
        menu.addDisabled(m.ok ? tr("tray.head", pct0(m.fiveHour.value), pct0(m.weekly.value)) : tr("panel.no_data"))
        menu.addItem(.separator())

        menu.add(tr("menu.panel_visible"), checked: s.visible) { s.visible.toggle() }
        menu.add(tr("set.show_spark"), checked: s.showSpark) { s.showSpark.toggle() }

        // per-model gauge: show / size / order, in one submenu named after the model
        let mname = (m.modelName.isEmpty ? (s.modelFilter.isEmpty ? "Fable" : s.modelFilter) : m.modelName).uppercased()
        let inAPI = usingAPI || reader === demo
        let modelMenu = menu.submenu(tr("menu.model_gauge", mname))
        modelMenu.add(tr("set.show_model"), checked: s.showModel, enabled: inAPI) { s.showModel.toggle() }
        let msize = modelMenu.submenu(tr("menu.size"), enabled: inAPI)
        for (key, value) in [("size.small", 0.7), ("size.normal", 1.0), ("size.large", 1.3), ("size.extra", 1.6)] {
            msize.add(tr(key), checked: abs(s.modelScale - value) < 0.01) { s.modelScale = value }
        }
        let order = modelMenu.submenu(tr("menu.order"))
        let names = ["fh": tr("panel.five_hour_short"), "mo": mname, "sd": tr("panel.week_short")]
        for perm in gaugeOrders {
            let label = perm.split(separator: ",").map { names[String($0)] ?? String($0) }.joined(separator: " \u{b7} ")
            order.add(label, checked: s.gaugeOrder == perm) { s.gaugeOrder = perm }
        }

        let details = menu.submenu(tr("menu.details"))
        let toggles: [(String, ReferenceWritableKeyPath<Settings, Bool>)] = [
            ("show_plan_badge", \.showPlanBadge), ("show_plan_name", \.showPlanName), ("show_model_list", \.showModelList),
            ("show_surfaces", \.showSurfaces), ("show_extra_usage", \.showExtraUsage), ("show_resets", \.showResets),
            ("show_products", \.showProducts), ("show_local_models", \.showLocalModels),
        ]
        for (key, path) in toggles {
            details.add(tr("set." + key), checked: s[keyPath: path], enabled: inAPI || key == "show_local_models") {
                s[keyPath: path].toggle()
            }
        }

        let layoutMenu = menu.submenu(tr("menu.layout"))
        for key in layouts { layoutMenu.add(tr("layout." + key), checked: s.layout == key) { s.layout = key } }
        let themeMenu = menu.submenu(tr("menu.theme"))
        for t in Themes.all { themeMenu.add(tr("theme." + t.key), checked: s.theme == t.key) { s.theme = t.key } }
        let sizeMenu = menu.submenu(tr("menu.size"))
        for (key, value) in [("size.small", 0.85), ("size.normal", 1.0), ("size.large", 1.25), ("size.extra", 1.5)] {
            sizeMenu.add(tr(key), checked: abs(s.scale - value) < 0.01) { s.scale = value }
        }
        let langMenu = menu.submenu(tr("menu.language"))
        for lang in L10n.languages {
            langMenu.add(lang.name, checked: L10n.current == lang.code) { [weak self] in self?.setLanguage(lang.code) }
        }

        menu.add(tr("menu.always_top"), checked: s.alwaysOnTop) { s.alwaysOnTop.toggle() }
        menu.add(tr("menu.locked"), checked: s.locked) { s.locked.toggle() }
        menu.add(tr("menu.click_through"), checked: s.clickThrough) { s.clickThrough.toggle() }
        menu.add(tr("menu.autostart"), checked: StartAtLogin.isEnabled) { [weak self] in self?.toggleAutostart() }
        menu.addItem(.separator())

        let srcMenu = menu.submenu(tr("menu.source"))
        srcMenu.add(tr("source.local"), checked: s.source == "local") { [weak self] in self?.setSource("local") }
        #if CLAUDE_SIGN_IN
        srcMenu.add(tr("source.api"), checked: s.source == "api") { [weak self] in self?.setSource("api") }
        #endif
        srcMenu.add(tr("source.demo"), checked: s.source == "demo") { [weak self] in self?.setSource("demo") }
        #if CLAUDE_SIGN_IN
        if api.hasTokens {
            srcMenu.addItem(.separator())
            srcMenu.add(tr("menu.logout")) { [weak self] in self?.logout() }
        }
        #endif
        menu.addItem(.separator())
        #if CLAUDE_SIGN_IN
        if !api.hasTokens || api.needsLogin {
            menu.add(tr("menu.login")) { [weak self] in self?.login() }
        }
        #endif
        if s.source == "local" && !localReader.hasAccess {
            menu.add(tr("menu.grant_access")) { [weak self] in self?.grantDesktopLog() }
        }
        menu.add(tr("menu.history")) { [weak self] in self?.showHistory() }
        menu.add(tr("menu.settings")) { [weak self] in self?.showSettings() }
        menu.add(tr("menu.help")) { [weak self] in self?.showHelp() }
        menu.add(tr("menu.feedback")) { [weak self] in self?.showFeedback() }
        if isBusy() {
            menu.addDisabled(tr("panel.refreshing") + "\u{2026}")
        } else {
            menu.add(tr("menu.refresh")) { [weak self] in self?.forceRefresh() }
        }
        if let url = AppInfo.appStoreURL {
            menu.addItem(.separator())
            menu.add(tr("set.rate_app_store")) { openURL(url) }
        }
        menu.addItem(.separator())
        menu.add(tr("menu.quit")) { [weak self] in self?.quit() }
        return menu
    }

    func showMenu(at point: NSPoint) {
        let menu = buildMenu()
        menu.popUp(positioning: nil, at: point, in: nil)
    }

    private func setLanguage(_ code: String) {
        L10n.setLanguage(code)
        settings.language = code
        // redraw the whole UI in the new language (the windows are rebuilt on their next opening)
        closeAllWindows()
        panelView.needsDisplay = true
        refresh()
    }

    private func closeAllWindows() {
        settingsWindow?.close(); settingsWindow = nil
        historyWindow?.close(); historyWindow = nil
        helpWindow?.close(); helpWindow = nil
        feedbackWindow?.close(); feedbackWindow = nil
        #if CLAUDE_SIGN_IN
        signInWindow?.close(); signInWindow = nil
        #endif
    }

    private func setSource(_ source: String) {
        #if CLAUDE_SIGN_IN
        if source == "api" && !api.hasTokens {
            login()
            return
        }
        #endif
        settings.source = source
    }

    private func toggleAutostart() {
        let enable = !StartAtLogin.isEnabled
        if !StartAtLogin.set(enable) {
            Notifier.shared.notify(AppInfo.name, tr("notify.autostart_fail"))
            return
        }
        if enable && StartAtLogin.requiresApproval { StartAtLogin.openSystemSettings() }
        Notifier.shared.notify(AppInfo.name, enable ? tr("notify.autostart_on") : tr("notify.autostart_off"))
    }

    // MARK: - sign-in

    var signInAvailable: Bool {
        #if CLAUDE_SIGN_IN
        return true
        #else
        return false
        #endif
    }

    var isSignedIn: Bool {
        #if CLAUDE_SIGN_IN
        return api.hasTokens
        #else
        return false
        #endif
    }

    func login() {
        #if CLAUDE_SIGN_IN
        let model = SignInModel()
        model.onSuccess = { [weak self] tokens in
            guard let self = self else { return }
            Keychain.saveTokens(tokens)
            self.api.setTokens(tokens)
            self.settings.source = "api"
            Notifier.shared.notify(AppInfo.name, tr("notify.login_ok"))
        }
        model.onClose = { [weak self] in self?.signInWindow?.close(); self?.signInWindow = nil }
        let host = WindowHost(title: "\(AppInfo.name) \u{2013} \(tr("dlg.login_title"))", size: NSSize(width: 480, height: 400), resizable: false) {
            SignInView(model: model)
        }
        host.onClose = { model.windowDidClose() }   // title-bar close too: cancel the sheet, stop the listener
        signInWindow = host
        host.show()
        model.window = host.window   // the system sign-in sheet is attached to this window
        #endif
    }

    func logout() {
        #if CLAUDE_SIGN_IN
        Keychain.clear()
        api.setTokens(nil)
        settings.source = "local"
        Notifier.shared.notify(AppInfo.name, tr("notify.logout"))
        #endif
    }

    // MARK: - sandbox grants

    func grantDesktopLog() {
        let start = AppInfo.defaultDesktopLog
        if let (_, data) = Bookmarks.pick(directory: false, startAt: start, title: tr("set.pick_file_title"),
                                          message: tr("set.datafile_hint_mac"), allowedExtensions: ["json"]) {
            settings.desktopLogBookmark = data
            localReader.invalidate()
            refresh()
        }
    }

    func grantClaudeCode() {
        if let (_, data) = Bookmarks.pick(directory: true, startAt: AppInfo.defaultClaudeCodeFolder,
                                          title: tr("set.local_models_path"), message: tr("set.claude_code_hint_mac")) {
            settings.claudeCodeBookmark = data
            localModels.resetState()
            localModels.scan(force: true)
            refresh()
        }
    }

    // MARK: - windows

    func togglePanel() {
        settings.visible.toggle()
    }

    func showSettings() {
        if let w = settingsWindow, w.isVisible { w.show(); return }
        let actions = SettingsActions(
            login: { [weak self] in self?.login() },
            logout: { [weak self] in self?.logout() },
            isSignedIn: { [weak self] in self?.isSignedIn ?? false },
            signInAvailable: signInAvailable,
            grantDesktopLog: { [weak self] in self?.grantDesktopLog() },
            grantClaudeCode: { [weak self] in self?.grantClaudeCode() },
            reset: { [weak self] in self?.settings.reset() },
            openConfigFolder: { NSWorkspace.shared.activateFileViewerSelecting([AppInfo.supportDirectory]) },
            detailRows: { [weak self] in self?.settingsDetailRows() ?? [] },
            orgs: { [weak self] in self?.localReader.organizations() ?? [] }
        )
        let s = settings
        let host = WindowHost(title: "\(AppInfo.name) \u{2013} \(tr("set.title"))", size: NSSize(width: 560, height: 520)) {
            SettingsView(s: s, actions: actions)
        }
        settingsWindow = host
        host.show()
    }

    private func settingsDetailRows() -> [(String, String)] {
        var rows = metrics.rows.map { ($0.id, $0.displayLabel) }
        if let rs = metrics.resets, rs.count > 0 { rows.append(("resets", tr("detail.resets"))) }
        if metrics.extra != nil { rows.append(("extra", tr("detail.extra"))) }
        rows += metrics.products.filter { $0.percent >= 0.5 }.map { ("product:" + $0.key, "\($0.displayLabel)  (\(tr("detail.product.group")))") }
        rows += panelView.localModels.map { ("local:" + $0.name, "\($0.name)  (Claude Code)") }
        return rows
    }

    func showHistory() {
        if historyModel == nil {
            historyModel = HistoryModel(settings: settings) { [weak self] in self?.reader ?? (DemoSource() as UsageSource) }
        }
        if historyWindow == nil {
            let model = historyModel!, s = settings
            historyWindow = WindowHost(title: "\(AppInfo.name) \u{2013} \(tr("hist.title"))", size: NSSize(width: 660, height: 440)) {
                HistoryView(model: model, settings: s)
            }
        }
        historyModel?.refresh()
        historyWindow?.show()
    }

    func showHelp() {
        if helpWindow == nil {
            helpWindow = WindowHost(title: "\(AppInfo.name) \u{2013} \(tr("help.title"))", size: NSSize(width: 660, height: 640)) { HelpView() }
        }
        helpWindow?.show()
    }

    func showFeedback() {
        if let w = feedbackWindow, w.isVisible { w.show(); return }
        let model = FeedbackModel()
        model.onClose = { [weak self] in self?.feedbackWindow?.close(); self?.feedbackWindow = nil }
        let host = WindowHost(title: tr("fb.title"), size: NSSize(width: 560, height: 600), resizable: false) { FeedbackView(model: model) }
        feedbackWindow = host
        host.show()
    }

    func quit() {
        if panel.isVisible { panel.savePosition() }
        NSApp.terminate(nil)
    }

    func willTerminate() {
        timer?.invalidate()
        pulse?.invalidate()
        statusBar.remove()
    }
}
