// The borderless, non-activating floating window that hosts the panel view.

import AppKit

final class PanelWindow: NSPanel {
    let panelView: PanelView
    private let settings: Settings

    init(settings: Settings, view: PanelView) {
        self.settings = settings
        self.panelView = view
        super.init(contentRect: NSRect(origin: .zero, size: view.frame.size),
                   styleMask: [.borderless, .nonactivatingPanel], backing: .buffered, defer: false)
        isFloatingPanel = true
        isOpaque = false
        backgroundColor = .clear
        hasShadow = false                  // the view draws its own soft shadow
        hidesOnDeactivate = false
        isMovableByWindowBackground = false
        isReleasedWhenClosed = false
        animationBehavior = .none
        collectionBehavior = [.canJoinAllSpaces, .stationary, .fullScreenAuxiliary]
        title = AppInfo.name
        contentView = view
        view.onSizeChanged = { [weak self] size in self?.resize(to: size) }
        applySettings(initial: true)
    }

    override var canBecomeKey: Bool { false }
    override var canBecomeMain: Bool { false }

    func applySettings(initial: Bool = false) {
        level = settings.alwaysOnTop ? .floating : .normal
        ignoresMouseEvents = settings.clickThrough
        alphaValue = CGFloat(settings.opacity)
        panelView.applySettings()
        if initial { restorePosition() }
    }

    /// Keep the top-left corner where it is when the content grows or shrinks.
    private func resize(to size: NSSize) {
        var f = frame
        let topLeft = NSPoint(x: f.minX, y: f.maxY)
        f.size = size
        f.origin = NSPoint(x: topLeft.x, y: topLeft.y - size.height)
        setFrame(f, display: true)
    }

    func restorePosition() {
        if settings.positionSaved {
            let origin = NSPoint(x: settings.posX, y: settings.posY)
            let center = NSPoint(x: origin.x + frame.width / 2, y: origin.y + frame.height / 2)
            if NSScreen.screens.contains(where: { $0.frame.contains(center) }) {
                setFrameOrigin(origin)
                return
            }
        }
        defaultPosition()
    }

    /// Top-right corner of the main screen (the shadow margin hangs over the edge).
    func defaultPosition() {
        guard let scr = NSScreen.main else { return }
        let a = scr.visibleFrame
        setFrameOrigin(NSPoint(x: a.maxX - frame.width + shadowMargin - 8, y: a.maxY - frame.height + shadowMargin - 24))
    }

    func savePosition() {
        settings.posX = frame.origin.x
        settings.posY = frame.origin.y
        settings.positionSaved = true
    }
}
