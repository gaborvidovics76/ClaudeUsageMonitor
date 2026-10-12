// "Start at login" with SMAppService (macOS 13+). Off by default; registered only when the user
// asks for it (App Store Review Guideline 2.4.5(iii)), and the user's own change in
// System Settings > General > Login Items is respected (the app never re-registers by itself).

import Foundation
import ServiceManagement

enum StartAtLogin {
    static var isEnabled: Bool { SMAppService.mainApp.status == .enabled }

    static var requiresApproval: Bool { SMAppService.mainApp.status == .requiresApproval }

    /// Returns false when the system refused; `requiresApproval` then tells whether the user has to
    /// allow it in System Settings.
    @discardableResult
    static func set(_ enabled: Bool) -> Bool {
        do {
            if enabled { try SMAppService.mainApp.register() } else { try SMAppService.mainApp.unregister() }
            return true
        } catch {
            Log.startup("login item change failed: \(error.localizedDescription)")
            return false
        }
    }

    static func openSystemSettings() { SMAppService.openSystemSettingsLoginItems() }
}
