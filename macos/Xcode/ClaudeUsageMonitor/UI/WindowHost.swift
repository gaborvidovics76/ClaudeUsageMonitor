// Hosts a SwiftUI view in an ordinary titled window. The app is an agent (no Dock icon), so a
// window has to activate the app explicitly to come to the front.

import AppKit
import SwiftUI

final class WindowHost<Content: View> {
    private(set) var window: NSWindow?
    private let title: String
    private let size: NSSize
    private let resizable: Bool
    private let make: () -> Content

    init(title: String, size: NSSize, resizable: Bool = true, make: @escaping () -> Content) {
        self.title = title
        self.size = size
        self.resizable = resizable
        self.make = make
    }

    var isVisible: Bool { window?.isVisible ?? false }

    func show() {
        if window == nil {
            var mask: NSWindow.StyleMask = [.titled, .closable, .miniaturizable]
            if resizable { mask.insert(.resizable) }
            let w = NSWindow(contentRect: NSRect(origin: .zero, size: size), styleMask: mask, backing: .buffered, defer: false)
            w.title = title
            w.isReleasedWhenClosed = false
            w.contentViewController = NSHostingController(rootView: make())
            w.setContentSize(size)
            w.center()
            window = w
        }
        NSApp.activate(ignoringOtherApps: true)
        window?.makeKeyAndOrderFront(nil)
    }

    func close() {
        window?.close()
        window = nil
    }
}

/// Shared look of the app's dialogs (dark, like the Windows app).
enum UI {
    static let dialogBG = Color(red: 0x16 / 255, green: 0x18 / 255, blue: 0x1d / 255)
    static let cardBG = Color(red: 0x1b / 255, green: 0x1e / 255, blue: 0x25 / 255)
    static let text = Color(red: 0xd6 / 255, green: 0xdb / 255, blue: 0xe8 / 255)
    static let bright = Color(red: 0xf0 / 255, green: 0xf3 / 255, blue: 0xfa / 255)
    static let hint = Color(red: 0x79 / 255, green: 0x83 / 255, blue: 0x9a / 255)
    static let accent = Color(red: 0xd9 / 255, green: 0x77 / 255, blue: 0x57 / 255)
    static let link = Color(red: 0x8f / 255, green: 0xb0 / 255, blue: 0xff / 255)
    static let error = Color(red: 0xff / 255, green: 0x9a / 255, blue: 0xa5 / 255)
}

struct HintText: View {
    let text: String
    init(_ text: String) { self.text = text }
    var body: some View {
        Text(text).font(.system(size: 11)).foregroundColor(UI.hint).fixedSize(horizontal: false, vertical: true)
    }
}

struct SectionLabel: View {
    let text: String
    init(_ text: String) { self.text = text }
    var body: some View {
        Text(text).font(.system(size: 12, weight: .semibold)).foregroundColor(UI.hint).padding(.top, 6)
    }
}

/// Opens a URL in the user's default browser.
func openURL(_ url: URL) { NSWorkspace.shared.open(url) }
func openURL(_ s: String) { if let u = URL(string: s) { openURL(u) } }
