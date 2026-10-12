// "Message to the developer" window (port of claude_usage/feedback_dialog.py).

import SwiftUI

final class FeedbackModel: ObservableObject {
    @Published var rating = 0
    @Published var name = ""
    @Published var email = ""
    @Published var message = ""
    @Published var consent = false
    @Published var consentError = false
    @Published var publish = false
    @Published var showPrivacy = false
    @Published var sending = false
    @Published var sent = false
    @Published var errorText = ""
    var onClose: (() -> Void)?

    private static let emailRegex = try! NSRegularExpression(pattern: #"^[^@\s]+@[^@\s]+\.[^@\s]{2,}$"#)

    func send() {
        errorText = ""
        let msg = message.trimmingCharacters(in: .whitespacesAndNewlines)
        let mail = email.trimmingCharacters(in: .whitespaces)
        if msg.count < 5 && rating == 0 { errorText = tr("fb.err_empty"); return }
        if !mail.isEmpty && FeedbackModel.emailRegex.firstMatch(in: mail, range: NSRange(mail.startIndex..., in: mail)) == nil {
            errorText = tr("fb.err_email"); return
        }
        let links = msg.lowercased().components(separatedBy: "http://").count - 1 + msg.lowercased().components(separatedBy: "https://").count - 1
        if links > 3 { errorText = tr("fb.err_links"); return }
        if !consent { errorText = tr("fb.err_consent"); consentError = true; return }
        let payload = Feedback.buildPayload(name: name, email: mail, message: msg, rating: rating, publish: publish, lang: L10n.current)
        sending = true
        Feedback.send(payload) { ok, code in
            self.sending = false
            if ok { self.sent = true; return }
            let key = ["rate": "fb.err_rate", "network": "fb.err_network", "email": "fb.err_email", "fields": "fb.err_empty",
                       "consent": "fb.err_consent", "links": "fb.err_links"][code] ?? "fb.err_server"
            self.errorText = tr(key)
        }
    }
}

struct FeedbackView: View {
    @ObservedObject var model: FeedbackModel

    var body: some View {
        Group {
            if model.sent { thanks } else { form }
        }
        .padding(18)
        .frame(width: 560)
        .preferredColorScheme(.dark)
    }

    private var thanks: some View {
        VStack(spacing: 10) {
            Text("\u{2713}  " + tr("fb.sent")).font(.system(size: 18, weight: .bold)).foregroundColor(Color(red: 0x7f / 255, green: 0xf0 / 255, blue: 0xc2 / 255))
            Text(tr("fb.sent_sub")).multilineTextAlignment(.center).foregroundColor(UI.text)
            Button(tr("fb.close")) { model.onClose?() }
        }.padding(.vertical, 24)
    }

    private var form: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text(tr("fb.title")).font(.system(size: 16, weight: .bold)).foregroundColor(UI.bright)
            Text(tr("fb.intro")).foregroundColor(UI.text).fixedSize(horizontal: false, vertical: true)

            HStack(spacing: 10) {
                Text(tr("fb.rating")).fontWeight(.semibold)
                StarBar(value: $model.rating)
                if model.rating > 0 {
                    Button(tr("fb.rating_clear")) { model.rating = 0 }.buttonStyle(.plain).foregroundColor(UI.hint)
                } else {
                    HintText(tr("fb.rating_hint"))
                }
                Spacer()
            }
            .padding(EdgeInsets(top: 8, leading: 12, bottom: 8, trailing: 12))
            .background(RoundedRectangle(cornerRadius: 10).fill(Color(red: 0x1f / 255, green: 0x23 / 255, blue: 0x2b / 255)))
            .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color(red: 0x3a / 255, green: 0x41 / 255, blue: 0x50 / 255)))

            labelled(tr("fb.name")) { TextField(tr("fb.optional"), text: $model.name).textFieldStyle(.roundedBorder) }
            labelled(tr("fb.email")) { TextField(tr("fb.email_hint"), text: $model.email).textFieldStyle(.roundedBorder) }
            labelled(tr("fb.message")) {
                ZStack(alignment: .topLeading) {
                    TextEditor(text: $model.message).frame(minHeight: 110).font(.system(size: 13))
                        .onChange(of: model.message) { v in if v.count > Feedback.maxMessage { model.message = String(v.prefix(Feedback.maxMessage)) } }
                    if model.message.isEmpty {
                        Text(tr("fb.message_ph")).foregroundColor(UI.hint).padding(EdgeInsets(top: 8, leading: 5, bottom: 0, trailing: 0)).allowsHitTesting(false)
                    }
                }
                .overlay(RoundedRectangle(cornerRadius: 7).stroke(Color(red: 0x33 / 255, green: 0x39 / 255, blue: 0x44 / 255)))
            }

            // consent (required) with a link that opens the privacy notice right here
            HStack(alignment: .top, spacing: 8) {
                Toggle("", isOn: $model.consent).toggleStyle(.checkbox).labelsHidden()
                    .onChange(of: model.consent) { _ in model.consentError = false }
                consentText
            }
            .padding(EdgeInsets(top: 8, leading: 10, bottom: 8, trailing: 10))
            .background(RoundedRectangle(cornerRadius: 9).fill(model.consentError ? Color(red: 1, green: 0.42, blue: 0.42).opacity(0.13) : UI.accent.opacity(0.1)))
            .overlay(RoundedRectangle(cornerRadius: 9).stroke(model.consentError ? Color(red: 1, green: 0.42, blue: 0.42) : UI.accent.opacity(0.63), lineWidth: model.consentError ? 2 : 1))

            if model.showPrivacy {
                ScrollView {
                    Text(tr("fb.privacy_text")).font(.system(size: 12)).foregroundColor(UI.text).textSelection(.enabled)
                        .fixedSize(horizontal: false, vertical: true).padding(8)
                }
                .frame(height: 190)
                .background(UI.cardBG).cornerRadius(8)
                Button(tr("fb.privacy_hide")) { model.showPrivacy = false }.buttonStyle(.plain).foregroundColor(UI.hint)
            }

            Toggle(tr("fb.publish"), isOn: $model.publish).toggleStyle(.checkbox).disabled(model.rating == 0)

            HintText(tr("fb.meta", AppInfo.version, Feedback.osName(), L10n.languageName(L10n.current)))
            HintText("\u{1f512} " + tr("fb.secure"))
            if !model.errorText.isEmpty { Text(model.errorText).foregroundColor(UI.error).fixedSize(horizontal: false, vertical: true) }

            HStack {
                Spacer()
                Button(tr("fb.cancel")) { model.onClose?() }
                Button(model.sending ? tr("fb.sending") : tr("fb.send")) { model.send() }
                    .buttonStyle(.borderedProminent).tint(UI.accent).disabled(model.sending).keyboardShortcut(.defaultAction)
            }
        }
    }

    private var consentText: some View {
        // "I have read and accept the {}." - the placeholder becomes a clickable link
        let template = tr("fb.consent", "\u{0}")
        let parts = template.components(separatedBy: "\u{0}")
        return HStack(spacing: 0) {
            Text(parts.first ?? "")
            Button(tr("fb.privacy_title")) { model.showPrivacy.toggle() }.buttonStyle(.plain).foregroundColor(UI.link).underline()
            Text(parts.count > 1 ? parts[1] : "")
            Text(" *").foregroundColor(Color(red: 1, green: 0.54, blue: 0.54))
        }
        .foregroundColor(UI.bright)
        .contentShape(Rectangle())
        .onTapGesture { model.consent.toggle() }
    }

    private func labelled<Content: View>(_ label: String, @ViewBuilder content: () -> Content) -> some View {
        VStack(alignment: .leading, spacing: 3) {
            HintText(label)
            content()
        }
    }
}

/// Five clickable stars; 0 = no rating.
struct StarBar: View {
    @Binding var value: Int
    @State private var hover = 0

    var body: some View {
        HStack(spacing: 2) {
            ForEach(1...5, id: \.self) { i in
                let shown = hover > 0 ? hover : value
                Image(systemName: i <= shown ? "star.fill" : "star")
                    .font(.system(size: 24))
                    .foregroundColor(i <= shown ? Color(red: 0xf5 / 255, green: 0xb8 / 255, blue: 0x3d / 255) : Color(red: 0xb4 / 255, green: 0xbc / 255, blue: 0xcb / 255))
                    .onHover { inside in hover = inside ? i : 0 }
                    .onTapGesture { value = i }
                    .help(tr("fb.rating_tip", i))
            }
        }
    }
}
