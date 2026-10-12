// App Sandbox: the app may only read files the user has chosen in an Open panel. The choice is
// remembered as a security-scoped bookmark (Settings), and every read happens inside a
// start/stopAccessingSecurityScopedResource pair.

import AppKit
import Foundation
import UniformTypeIdentifiers

enum Bookmarks {
    /// Opens the system file chooser and returns a security-scoped bookmark of the chosen item.
    static func pick(directory: Bool, startAt: URL, title: String, message: String, allowedExtensions: [String] = []) -> (URL, Data)? {
        let panel = NSOpenPanel()
        panel.title = title
        panel.message = message
        panel.prompt = tr("set.grant_access_btn")
        panel.canChooseFiles = !directory
        panel.canChooseDirectories = directory
        panel.canCreateDirectories = false
        panel.allowsMultipleSelection = false
        panel.showsHiddenFiles = true          // ~/.claude is a hidden folder
        panel.directoryURL = directory ? startAt : startAt.deletingLastPathComponent()
        if !directory && !allowedExtensions.isEmpty {
            panel.allowedContentTypes = allowedExtensions.compactMap { UTTypeFor($0) }
            panel.allowsOtherFileTypes = true
        }
        NSApp.activate(ignoringOtherApps: true)
        guard panel.runModal() == .OK, let url = panel.url else { return nil }
        guard let data = try? url.bookmarkData(options: .withSecurityScope, includingResourceValuesForKeys: nil, relativeTo: nil) else {
            return nil
        }
        return (url, data)
    }

    /// Resolves a stored bookmark; nil when empty, missing or no longer valid.
    static func resolve(_ data: Data) -> URL? {
        guard !data.isEmpty else { return nil }
        var stale = false
        guard let url = try? URL(resolvingBookmarkData: data, options: [.withSecurityScope, .withoutUI],
                                 relativeTo: nil, bookmarkDataIsStale: &stale) else { return nil }
        return url
    }

    /// Runs `body` with access to the bookmarked item. Returns nil when there is no usable bookmark.
    static func withAccess<T>(_ data: Data, _ body: (URL) -> T) -> T? {
        guard let url = resolve(data) else { return nil }
        let granted = url.startAccessingSecurityScopedResource()
        defer { if granted { url.stopAccessingSecurityScopedResource() } }
        return body(url)
    }

    /// A short, human-readable path for the Settings window ("~/Library/Application Support/Claude/…").
    static func display(_ data: Data) -> String {
        guard let url = resolve(data) else { return "" }
        let home = AppInfo.realHome.path
        let p = url.path
        return p.hasPrefix(home) ? "~" + p.dropFirst(home.count) : p
    }
}

private func UTTypeFor(_ ext: String) -> UTType? { UTType(filenameExtension: ext) }
