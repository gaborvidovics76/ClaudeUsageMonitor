// Entry point. The app is an agent (LSUIElement): no Dock icon, no main menu - a floating panel
// and a menu bar item. All windows are created by the controller when needed.

import AppKit

@main
final class AppDelegate: NSObject, NSApplicationDelegate {
    private var controller: MonitorController?

    static func main() {
        let app = NSApplication.shared
        let delegate = AppDelegate()
        app.delegate = delegate
        app.setActivationPolicy(.accessory)
        app.run()
    }

    func applicationDidFinishLaunching(_ notification: Notification) {
        Log.startup("starting \(AppInfo.version) (\(AppInfo.build))")
        controller = MonitorController()
        Log.startup("started")
    }

    func applicationShouldHandleReopen(_ sender: NSApplication, hasVisibleWindows flag: Bool) -> Bool {
        // the app was opened again (Launchpad, Finder): bring the panel back
        controller?.settings.visible = true
        return false
    }

    func applicationWillTerminate(_ notification: Notification) {
        controller?.willTerminate()
        Log.startup("stopped")
    }

    func applicationSupportsSecureRestorableState(_ app: NSApplication) -> Bool { true }
}
