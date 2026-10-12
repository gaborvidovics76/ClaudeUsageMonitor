// Sign-in window: system browser + pasting the code back (port of claude_usage/authdialog.py).
// Compiled only with CLAUDE_SIGN_IN (see OAuth.swift).

import AppKit
import SwiftUI

#if CLAUDE_SIGN_IN

final class SignInModel: ObservableObject {
    @Published var pasted = ""
    @Published var checking = false
    @Published var errorText: String? = nil
    let verifier: String
    let url: URL
    let state: String
    var onSuccess: ((OAuthTokens) -> Void)?
    var onClose: (() -> Void)?

    init() {
        let (v, challenge) = OAuth.newPKCE()
        verifier = v
        let (u, st) = OAuth.buildAuthorize(verifier: v, challenge: challenge)
        url = u
        state = st
    }

    func openBrowser() { openURL(url) }

    func submit() {
        var text = pasted.trimmingCharacters(in: .whitespacesAndNewlines)
        // convenience: sometimes the whole callback URL is pasted
        if text.contains("code="), let comps = URLComponents(string: text) {
            let code = comps.queryItems?.first { $0.name == "code" }?.value ?? ""
            let st = comps.queryItems?.first { $0.name == "state" }?.value ?? state
            if !code.isEmpty { text = "\(code)#\(st)" }
        }
        checking = true
        errorText = nil
        let verifier = self.verifier, state = self.state
        DispatchQueue.global(qos: .userInitiated).async {
            let (tokens, err) = OAuth.exchange(code: text, verifier: verifier, state: state)
            DispatchQueue.main.async {
                self.checking = false
                if let t = tokens, !t.accessToken.isEmpty {
                    self.onSuccess?(t)
                    self.onClose?()
                } else if err.contains("429") || err.contains("rate_limit") {
                    self.errorText = tr("dlg.err_ratelimit")
                } else {
                    self.errorText = tr("dlg.err_badcode", err.isEmpty ? tr("dlg.unknown_err") : err)
                }
            }
        }
    }
}

struct SignInView: View {
    @ObservedObject var model: SignInModel

    var body: some View {
        VStack(alignment: .leading, spacing: 9) {
            Text(tr("dlg.intro")).fixedSize(horizontal: false, vertical: true)
            Text(tr("dlg.step1")).font(.system(size: 15, weight: .semibold)).padding(.top, 4)
            Button(tr("dlg.open_browser")) { model.openBrowser() }
            HintText(tr("dlg.hint1"))
            Text(tr("dlg.step2")).font(.system(size: 15, weight: .semibold)).padding(.top, 6)
            HintText(tr("dlg.paste_label"))
            TextField(tr("dlg.paste_placeholder"), text: $model.pasted).textFieldStyle(.roundedBorder)
                .onSubmit { model.submit() }
            if let e = model.errorText {
                Text(e).foregroundColor(UI.error).fixedSize(horizontal: false, vertical: true)
            }
            HStack {
                Spacer()
                Button(tr("dlg.cancel")) { model.onClose?() }
                Button(model.checking ? tr("dlg.checking") : tr("dlg.signin")) { model.submit() }
                    .keyboardShortcut(.defaultAction).disabled(model.checking)
            }
        }
        .padding(18)
        .frame(width: 480)
        .preferredColorScheme(.dark)
    }
}

#endif
