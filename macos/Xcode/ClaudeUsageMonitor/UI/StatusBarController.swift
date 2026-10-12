// The menu bar item: a progress ring with the percentage, a tooltip with the full breakdown,
// left click = show/hide the panel, right click (or any click when there is no data) = menu.

import AppKit

final class StatusBarController {
    private let item: NSStatusItem
    var onToggle: (() -> Void)?
    var onMenu: (() -> NSMenu)?
    var onDoubleClick: (() -> Void)?

    init() {
        item = NSStatusBar.system.statusItem(withLength: NSStatusItem.variableLength)
        if let button = item.button {
            button.image = Icons.statusPlaceholder()
            button.imagePosition = .imageOnly
            button.target = self
            button.action = #selector(clicked(_:))
            button.sendAction(on: [.leftMouseUp, .rightMouseUp])
            button.toolTip = AppInfo.name
        }
    }

    func update(value: Double?, color: RGBA?, tooltip: String) {
        guard let button = item.button else { return }
        if let v = value, let c = color {
            button.image = Icons.statusImage(value: v, color: c)
        } else {
            button.image = Icons.statusPlaceholder()
        }
        button.toolTip = tooltip
    }

    @objc private func clicked(_ sender: Any?) {
        guard let event = NSApp.currentEvent else { return }
        if event.type == .rightMouseUp || event.modifierFlags.contains(.control) {
            showMenu()
        } else if event.clickCount >= 2 {
            onDoubleClick?()
        } else {
            onToggle?()
        }
    }

    func showMenu() {
        guard let menu = onMenu?() else { return }
        item.menu = menu
        item.button?.performClick(nil)
        item.menu = nil                 // otherwise every later click would open the menu
    }

    func remove() { NSStatusBar.system.removeStatusItem(item) }
}

/// NSMenuItem with a closure instead of target/action plumbing.
final class ActionItem: NSMenuItem {
    private var handler: (() -> Void)?

    convenience init(_ title: String, checked: Bool = false, enabled: Bool = true, handler: @escaping () -> Void) {
        self.init(title: title, action: #selector(fire), keyEquivalent: "")
        self.handler = handler
        self.target = self
        self.state = checked ? .on : .off
        self.isEnabled = enabled
    }

    @objc private func fire() { handler?() }
}

extension NSMenu {
    @discardableResult
    func add(_ title: String, checked: Bool = false, enabled: Bool = true, handler: @escaping () -> Void) -> NSMenuItem {
        let it = ActionItem(title, checked: checked, enabled: enabled, handler: handler)
        addItem(it)
        return it
    }

    func addDisabled(_ title: String) {
        let it = NSMenuItem(title: title, action: nil, keyEquivalent: "")
        it.isEnabled = false
        addItem(it)
    }

    func submenu(_ title: String, enabled: Bool = true) -> NSMenu {
        let it = NSMenuItem(title: title, action: nil, keyEquivalent: "")
        let sub = NSMenu(title: title)
        it.submenu = sub
        it.isEnabled = enabled
        addItem(it)
        return sub
    }
}
