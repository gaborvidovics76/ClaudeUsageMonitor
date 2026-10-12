// Settings window (port of claude_usage/settings_dialog.py), as a SwiftUI form in tabs.

import AppKit
import SwiftUI

/// What the controller offers the settings window.
struct SettingsActions {
    var login: () -> Void
    var logout: () -> Void
    var isSignedIn: () -> Bool
    var signInAvailable: Bool
    var grantDesktopLog: () -> Void
    var grantClaudeCode: () -> Void
    var reset: () -> Void
    var openConfigFolder: () -> Void
    var detailRows: () -> [(String, String)]
    var orgs: () -> [String]
}

struct SettingsView: View {
    @ObservedObject var s: Settings
    let actions: SettingsActions
    @State private var tab = 0

    var body: some View {
        VStack(spacing: 10) {
            TabView(selection: $tab) {
                AppearanceTab(s: s).tabItem { Text(tr("set.tab_appearance")) }.tag(0)
                ContentTab(s: s).tabItem { Text(tr("set.tab_content")) }.tag(1)
                DetailsTab(s: s, actions: actions).tabItem { Text(tr("set.tab_details")) }.tag(2)
                AlertsTab(s: s).tabItem { Text(tr("set.tab_alerts")) }.tag(3)
                DataTab(s: s, actions: actions).tabItem { Text(tr("set.tab_data")) }.tag(4)
                SystemTab(s: s, actions: actions).tabItem { Text(tr("set.tab_system")) }.tag(5)
            }
        }
        .padding(14)
        .frame(minWidth: 520, minHeight: 440)
        .preferredColorScheme(.dark)
    }
}

// MARK: - helpers

private struct SliderRow: View {
    let label: String
    @Binding var value: Double
    let range: ClosedRange<Double>
    let suffix: String

    var body: some View {
        HStack {
            Text(label).frame(width: 150, alignment: .trailing)
            Slider(value: $value, in: range, step: 0.01)
            Text(format(value) + suffix).frame(width: 52, alignment: .trailing).font(.system(size: 11)).foregroundColor(UI.hint)
        }
    }

    private func format(_ v: Double) -> String {
        var s = String(format: "%.2f", v)
        while s.hasSuffix("0") { s.removeLast() }
        if s.hasSuffix(".") { s.removeLast() }
        return s
    }
}

private struct Row<Content: View>: View {
    let label: String
    let content: Content
    init(_ label: String, @ViewBuilder content: () -> Content) { self.label = label; self.content = content() }
    var body: some View {
        HStack(alignment: .firstTextBaseline) {
            Text(label).frame(width: 150, alignment: .trailing)
            content
            Spacer(minLength: 0)
        }
    }
}

private struct Check: View {
    let label: String
    @Binding var on: Bool
    var body: some View {
        HStack {
            Spacer().frame(width: 150)
            Toggle(label, isOn: $on).toggleStyle(.checkbox)
            Spacer(minLength: 0)
        }
    }
}

// MARK: - tabs

private struct AppearanceTab: View {
    @ObservedObject var s: Settings

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 9) {
                Row(tr("set.theme")) {
                    Picker("", selection: $s.theme) {
                        ForEach(Themes.all, id: \.key) { t in Text(tr("theme." + t.key)).tag(t.key) }
                    }.labelsHidden().frame(width: 220)
                }
                Row(tr("set.accent")) {
                    ColorPicker("", selection: accentBinding, supportsOpacity: false).labelsHidden()
                    Text(s.accent.isEmpty ? tr("set.theme_default") : s.accent.uppercased()).foregroundColor(UI.hint)
                    Button(tr("set.default")) { s.accent = "" }
                }
                Row(tr("set.layout")) {
                    Picker("", selection: $s.layout) {
                        ForEach(layouts, id: \.self) { key in Text(tr("layout." + key)).tag(key) }
                    }.labelsHidden().frame(width: 220)
                }
                SliderRow(label: tr("set.size"), value: $s.scale, range: 0.7...2.0, suffix: "\u{d7}")
                SliderRow(label: tr("set.opacity"), value: $s.opacity, range: 0.25...1.0, suffix: "")
                Check(label: tr("set.visible"), on: $s.visible)
                Check(label: tr("set.always_top"), on: $s.alwaysOnTop)
                Check(label: tr("set.lock"), on: $s.locked)
                Check(label: tr("set.snap"), on: $s.snapEdges)
                Check(label: tr("set.dock"), on: $s.showInDock)
                Check(label: tr("set.click_through"), on: $s.clickThrough)
                HStack { Spacer().frame(width: 150); HintText(tr("set.tip_mac")) }
            }.padding(14)
        }
    }

    private var accentBinding: Binding<Color> {
        Binding(get: {
            let rgba = RGBA(hex: s.accent) ?? Themes.theme(s.theme).accent
            return Color(rgba.nsColor)
        }, set: { color in
            if let ns = NSColor(color).usingColorSpace(.sRGB) {
                s.accent = RGBA(Int(ns.redComponent * 255), Int(ns.greenComponent * 255), Int(ns.blueComponent * 255)).hex
            }
        })
    }
}

private struct ContentTab: View {
    @ObservedObject var s: Settings

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 9) {
                Check(label: tr("set.show_five_hour"), on: $s.showFiveHour)
                Check(label: tr("set.show_model"), on: $s.showModel)
                Row(tr("set.model_filter")) {
                    TextField("Fable", text: $s.modelFilter).frame(width: 220)
                }
                SliderRow(label: tr("set.model_scale"), value: $s.modelScale, range: 0.5...2.0, suffix: "\u{d7}")
                Row(tr("set.gauge_order")) {
                    Picker("", selection: $s.gaugeOrder) {
                        ForEach(gaugeOrders, id: \.self) { perm in Text(orderLabel(perm)).tag(perm) }
                    }.labelsHidden().frame(width: 220)
                }
                Check(label: tr("set.show_weekly"), on: $s.showWeekly)
                Check(label: tr("set.show_spark"), on: $s.showSpark)
                Check(label: tr("set.show_burn"), on: $s.showBurn)
                Check(label: tr("set.show_reset"), on: $s.showReset)
                Check(label: tr("set.show_age"), on: $s.showAge)
                Check(label: tr("set.show_feedback_icon"), on: $s.showFeedbackIcon)
                Row(tr("set.tray_value")) {
                    Picker("", selection: $s.trayMetric) {
                        Text(tr("set.tray_five")).tag("five_hour")
                        Text(tr("set.tray_weekly")).tag("weekly")
                        Text(tr("set.tray_max")).tag("max")
                    }.labelsHidden().frame(width: 220)
                }
            }.padding(14)
        }
    }

    private func orderLabel(_ perm: String) -> String {
        let mname = (s.modelFilter.isEmpty ? "Fable" : s.modelFilter).uppercased()
        let names = ["fh": tr("panel.five_hour_short"), "mo": mname, "sd": tr("panel.week_short")]
        return perm.split(separator: ",").map { names[String($0)] ?? String($0) }.joined(separator: " \u{b7} ")
    }
}

private struct DetailsTab: View {
    @ObservedObject var s: Settings
    let actions: SettingsActions
    @State private var rows: [(String, String)] = []

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 9) {
                HintText(tr("set.details_api_only"))
                Check(label: tr("set.show_plan_badge"), on: $s.showPlanBadge)
                Check(label: tr("set.show_plan_name"), on: $s.showPlanName)
                Check(label: tr("set.show_model_list"), on: $s.showModelList)
                Check(label: tr("set.show_surfaces"), on: $s.showSurfaces)
                Check(label: tr("set.show_extra_usage"), on: $s.showExtraUsage)
                Check(label: tr("set.show_local_models"), on: $s.showLocalModels)
                HStack { Spacer().frame(width: 150); HintText(tr("set.local_models_hint")) }
                Row(tr("set.local_models_path")) {
                    Text(Bookmarks.display(s.claudeCodeBookmark).isEmpty ? tr("set.not_set") : Bookmarks.display(s.claudeCodeBookmark))
                        .foregroundColor(UI.hint).lineLimit(1).truncationMode(.middle)
                    Button(tr("set.grant_access_btn")) { actions.grantClaudeCode() }
                }
                HStack { Spacer().frame(width: 150); HintText(tr("set.claude_code_hint_mac")) }

                SectionLabel(rows.isEmpty ? tr("set.rows_none") : tr("set.rows_available"))
                ForEach(rows, id: \.0) { pair in
                    let (rid, label) = pair
                    HStack {
                        Spacer().frame(width: 150)
                        Toggle(label, isOn: Binding(get: { !s.isHidden(rid) }, set: { s.setHidden(rid, !$0) })).toggleStyle(.checkbox)
                        Spacer(minLength: 0)
                    }
                }
            }.padding(14)
        }
        .onAppear { rows = actions.detailRows() }
    }
}

private struct AlertsTab: View {
    @ObservedObject var s: Settings

    var body: some View {
        VStack(alignment: .leading, spacing: 9) {
            Row(tr("set.warn")) {
                Stepper(value: $s.warnThreshold, in: 1...99) { Text("\(s.warnThreshold) %") }
            }
            Row(tr("set.danger")) {
                Stepper(value: $s.dangerThreshold, in: 2...100) { Text("\(s.dangerThreshold) %") }
            }
            Check(label: tr("set.notify_enabled"), on: $s.notifyEnabled)
            Check(label: tr("set.notify_reset"), on: $s.notifyOnReset)
            Check(label: tr("set.notify_stale"), on: $s.notifyStale)
            HStack { Spacer().frame(width: 150); HintText(tr("set.color_hint")) }
            Spacer()
        }.padding(14)
    }
}

private struct DataTab: View {
    @ObservedObject var s: Settings
    let actions: SettingsActions
    @State private var signedIn = false

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 9) {
                Row(tr("set.source_label")) {
                    Picker("", selection: sourceBinding) {
                        Text(tr("set.source_local")).tag("local")
                        if actions.signInAvailable { Text(tr("set.source_api")).tag("api") }
                        Text(tr("set.source_demo")).tag("demo")
                    }.labelsHidden().frame(width: 300)
                }
                if actions.signInAvailable {
                    Row("claude.ai") {
                        Button(signedIn ? tr("set.login_btn_in") : tr("set.login_btn_out")) {
                            if signedIn { actions.logout() } else { actions.login() }
                            signedIn = actions.isSignedIn()
                        }
                    }
                }
                Row(tr("set.profile")) {
                    Picker("", selection: $s.org) {
                        Text(tr("set.profile_auto")).tag("")
                        ForEach(Array(actions.orgs().enumerated()), id: \.element) { item in
                            Text(tr("set.profile_n", item.offset + 1, String(item.element.suffix(8)))).tag(item.element)
                        }
                    }.labelsHidden().frame(width: 300)
                }
                Row(tr("set.refresh")) {
                    Stepper(value: $s.refreshSeconds, in: 2...120) { Text("\(s.refreshSeconds)" + tr("set.sec_suffix")) }
                }
                Row(tr("set.datafile")) {
                    Text(Bookmarks.display(s.desktopLogBookmark).isEmpty ? tr("set.not_set") : Bookmarks.display(s.desktopLogBookmark))
                        .foregroundColor(UI.hint).lineLimit(1).truncationMode(.middle)
                    Button(tr("set.grant_access_btn")) { actions.grantDesktopLog() }
                }
                HStack { Spacer().frame(width: 150); HintText(tr("set.datafile_hint_mac")) }
                HStack { Spacer().frame(width: 150); HintText(tr("set.data_hint")) }
                HStack { Spacer().frame(width: 150); HintText(tr("set.demo_hint")) }
            }.padding(14)
        }
        .onAppear { signedIn = actions.isSignedIn() }
    }

    private var sourceBinding: Binding<String> {
        Binding(get: { s.source }, set: { newValue in
            if newValue == "api" && !actions.isSignedIn() {
                actions.login()
                signedIn = actions.isSignedIn()
                if !signedIn { return }
            }
            s.source = newValue
        })
    }
}

private struct SystemTab: View {
    @ObservedObject var s: Settings
    let actions: SettingsActions
    @State private var autostart = StartAtLogin.isEnabled
    @State private var confirmReset = false
    @State private var loginFailed = false

    var body: some View {
        VStack(alignment: .leading, spacing: 9) {
            HStack {
                Spacer().frame(width: 150)
                Toggle(tr("menu.autostart"), isOn: Binding(get: { autostart }, set: { on in
                    if StartAtLogin.set(on) { autostart = StartAtLogin.isEnabled || (on && StartAtLogin.requiresApproval) }
                    else { loginFailed = true }
                    if on && StartAtLogin.requiresApproval { StartAtLogin.openSystemSettings() }
                })).toggleStyle(.checkbox)
                Spacer(minLength: 0)
            }
            HStack { Spacer().frame(width: 150); Button(tr("set.open_config")) { actions.openConfigFolder() } }
            HStack { Spacer().frame(width: 150); Button(tr("set.restore")) { confirmReset = true } }
            Row(tr("set.version")) {
                Text("\(AppInfo.version) (\(AppInfo.build))")
            }
            HStack { Spacer().frame(width: 150); HintText(tr("set.about_mac", AppInfo.name)) }
            if let url = AppInfo.appStoreURL {
                HStack { Spacer().frame(width: 150); Button(tr("set.rate_app_store")) { openURL(url) } }
            }
            Spacer()
        }
        .padding(14)
        .alert(tr("set.reset_confirm"), isPresented: $confirmReset) {
            Button(tr("dlg.cancel"), role: .cancel) {}
            Button(tr("set.restore"), role: .destructive) { actions.reset() }
        }
        .alert(tr("notify.autostart_fail"), isPresented: $loginFailed) { Button("OK") {} }
    }
}
