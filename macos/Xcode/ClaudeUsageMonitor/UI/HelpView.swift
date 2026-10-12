// Help window: the guide and the author card (port of claude_usage/help_dialog.py).

import AppKit
import SwiftUI

struct HelpView: View {
    @State private var tab = 0

    var body: some View {
        VStack(spacing: 10) {
            TabView(selection: $tab) {
                GuideTab().tabItem { Text(tr("help.tab_guide")) }.tag(0)
                AuthorTab().tabItem { Text(tr("help.tab_author")) }.tag(1)
            }
        }
        .padding(14)
        .frame(minWidth: 640, minHeight: 600)
        .preferredColorScheme(.dark)
    }
}

/// The guide is shared with the Windows app as one HTML text per language. Two of its sections do
/// not apply to the App Store build (the backup lamps and the self-updater), so they are cut out
/// here by position - the section order is the same in every language.
func helpGuideHTML() -> String {
    var html = tr("help.guide")
    let site = AppInfo.siteURL().absoluteString
    html = html.replacingOccurrences(of: "{site}", with: "<a href=\"\(site)\" style=\"color:#8fb0ff;\">claudeusagemonitor.com</a>")
    html = html.replacingOccurrences(of: "{cfg}", with: AppInfo.supportDirectory.path)
    // split into sections at <h2>; drop the 5th (backups) and 6th (updates) ones
    var parts = html.components(separatedBy: "<h2>")
    if parts.count >= 7 {
        parts.remove(at: 6)
        parts.remove(at: 5)
        html = parts.joined(separator: "<h2>")
    }
    html += "<h2>\(tr("help.updates_mac_h"))</h2><p>\(tr("help.updates_mac"))</p>"
    html += "<h2>\(tr("help.sandbox_mac_h"))</h2><p>\(tr("help.sandbox_mac"))</p>"
    let style = "<style>body{font-family:-apple-system,system-ui;font-size:13px;color:#d6dbe8;background:#1b1e25;}"
        + "h2{color:#f0f3fa;font-size:15px;margin:14px 0 4px 0;} li{margin:3px 0;} code{color:#f3c9b8;} a{color:#8fb0ff;}</style>"
    return "<html><head><meta charset=\"utf-8\">\(style)</head><body>\(html)</body></html>"
}

private struct GuideTab: View {
    var body: some View {
        HTMLText(html: helpGuideHTML())
            .background(UI.cardBG)
            .cornerRadius(8)
            .padding(6)
    }
}

/// Renders simple HTML in a read-only NSTextView (links open in the browser).
struct HTMLText: NSViewRepresentable {
    let html: String

    func makeNSView(context: Context) -> NSScrollView {
        let scroll = NSTextView.scrollableTextView()
        let tv = scroll.documentView as! NSTextView
        tv.isEditable = false
        tv.isSelectable = true
        tv.drawsBackground = true
        tv.backgroundColor = NSColor(red: 0x1b / 255, green: 0x1e / 255, blue: 0x25 / 255, alpha: 1)
        tv.textContainerInset = NSSize(width: 10, height: 10)
        tv.linkTextAttributes = [.foregroundColor: NSColor(red: 0x8f / 255, green: 0xb0 / 255, blue: 1, alpha: 1), .underlineStyle: 0]
        scroll.hasVerticalScroller = true
        scroll.drawsBackground = false
        update(tv)
        return scroll
    }

    func updateNSView(_ nsView: NSScrollView, context: Context) {
        if let tv = nsView.documentView as? NSTextView { update(tv) }
    }

    private func update(_ tv: NSTextView) {
        guard let data = html.data(using: .utf8),
              let attr = try? NSAttributedString(data: data, options: [.documentType: NSAttributedString.DocumentType.html,
                                                                       .characterEncoding: String.Encoding.utf8.rawValue],
                                                 documentAttributes: nil) else {
            tv.string = html
            return
        }
        if tv.attributedString() != attr { tv.textStorage?.setAttributedString(attr) }
    }
}

private struct AuthorTab: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            VStack(alignment: .leading, spacing: 6) {
                Text(tr("help.official")).font(.system(size: 11, weight: .bold)).kerning(2).foregroundColor(UI.accent)
                Button { openURL(AppInfo.siteURL()) } label: {
                    Text("claudeusagemonitor.com").font(.system(size: 26, weight: .heavy)).foregroundColor(.white)
                }.buttonStyle(.plain)
                Text(tr("help.site_what")).foregroundColor(UI.text).fixedSize(horizontal: false, vertical: true)
                Text("\u{21aa} " + tr("help.moved")).font(.system(size: 12)).foregroundColor(Color(red: 0xf3 / 255, green: 0xc9 / 255, blue: 0xb8 / 255))
                    .fixedSize(horizontal: false, vertical: true)
                Button(tr("help.open_site")) { openURL(AppInfo.siteURL()) }
                    .buttonStyle(.borderedProminent).tint(UI.accent).padding(.top, 6)
            }
            .padding(EdgeInsets(top: 16, leading: 20, bottom: 18, trailing: 20))
            .background(LinearGradient(colors: [Color(red: 0x2a / 255, green: 0x1d / 255, blue: 0x18 / 255),
                                                Color(red: 0x1f / 255, green: 0x22 / 255, blue: 0x30 / 255)],
                                       startPoint: .topLeading, endPoint: .bottomTrailing))
            .overlay(RoundedRectangle(cornerRadius: 14).stroke(UI.accent, lineWidth: 2))
            .cornerRadius(14)

            Text("\(AppInfo.name) \u{b7} \(tr("help.version")) \(AppInfo.version)").font(.system(size: 16, weight: .bold)).foregroundColor(UI.bright)

            VStack(alignment: .leading, spacing: 4) {
                HStack(spacing: 4) { Text(tr("help.made_by") + ":"); Text(AppInfo.author).bold() }
                Text(tr("help.free"))
                HStack(spacing: 8) {
                    Link(tr("help.source_code"), destination: URL(string: AppInfo.repo)!)
                    Text("\u{b7}")
                    Link(tr("help.terms"), destination: AppInfo.siteURL(fragment: "terms"))
                    Text("\u{b7}")
                    Link(tr("help.privacy"), destination: AppInfo.siteURL(fragment: "privacy"))
                }.padding(.top, 6)
                Text(tr("help.feedback")).padding(.top, 6)
            }.foregroundColor(UI.text)

            HintText(tr("help.disclaimer"))
            Spacer()
        }
        .padding(16)
    }
}
