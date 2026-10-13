// Entry point. The app is an agent (LSUIElement): no Dock icon, a hidden main menu - a floating panel
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
        app.mainMenu = makeMainMenu()
        app.run()
    }

    /// The menu bar stays hidden for an agent, but its key equivalents still work: without an Edit
    /// menu, Cmd+V / Cmd+C / Cmd+A do nothing in text fields (sign-in code, message form).
    private static func makeMainMenu() -> NSMenu {
        let main = NSMenu()
        let appItem = NSMenuItem()
        appItem.submenu = NSMenu()
        appItem.submenu?.addItem(withTitle: "Quit \(AppInfo.name)", action: #selector(NSApplication.terminate(_:)), keyEquivalent: "q")
        main.addItem(appItem)

        let edit = NSMenu(title: "Edit")
        edit.addItem(withTitle: "Undo", action: Selector(("undo:")), keyEquivalent: "z")
        edit.addItem(withTitle: "Redo", action: Selector(("redo:")), keyEquivalent: "Z")
        edit.addItem(.separator())
        edit.addItem(withTitle: "Cut", action: #selector(NSText.cut(_:)), keyEquivalent: "x")
        edit.addItem(withTitle: "Copy", action: #selector(NSText.copy(_:)), keyEquivalent: "c")
        edit.addItem(withTitle: "Paste", action: #selector(NSText.paste(_:)), keyEquivalent: "v")
        edit.addItem(withTitle: "Select All", action: #selector(NSText.selectAll(_:)), keyEquivalent: "a")
        let editItem = NSMenuItem()
        editItem.submenu = edit
        main.addItem(editItem)
        return main
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
