// Sign-in window (port of claude_usage/authdialog.py).
//
// The sign-in page opens in the system's own sign-in sheet (ASWebAuthenticationSession) - App Review
// does not accept sending the user to the default browser (Guideline 4). Two ways to get the code back:
//   - automatic: the page redirects to http://localhost:<port>/callback, the app's loopback listener
//     (Data/LoopbackServer.swift) receives code + state, the sheet is closed by the app;
//   - manual (fallback, the Windows way): Anthropic's page shows the code, the user copies it, closes
//     the sheet and pastes it here. Used when no loopback port could be opened, or on request.
// Closing the sheet (Cancel) is never an error: the window just returns to its first state.
// Compiled only with CLAUDE_SIGN_IN (see OAuth.swift).

import AppKit
import AuthenticationServices
import SwiftUI

#if CLAUDE_SIGN_IN

final class SignInModel: NSObject, ObservableObject, ASWebAuthenticationPresentationContextProviding {
    enum Phase { case idle, opening, waiting, checking }

    @Published var pasted = ""
    @Published var phase: Phase = .idle
    @Published var errorText: String? = nil
    /// true: the code is shown on Anthropic's page and pasted by hand (no loopback listener).
    @Published var manual = false

    private(set) var verifier = ""
    private(set) var state = ""
    private(set) var redirectURI = OAuth.manualRedirectURI
    private var session: ASWebAuthenticationSession?
    private var server: LoopbackServer?
    /// The sign-in window: anchor of the sheet (set by the controller once the window exists).
    weak var window: NSWindow?
    var onSuccess: ((OAuthTokens) -> Void)?
    var onClose: (() -> Void)?

    /// A custom scheme the API requires; never called back - the redirect goes to localhost (or to
    /// Anthropic's code page), so the sheet is closed by the app, or by the user.
    private static let callbackScheme = "claude-usage-monitor"

    var checking: Bool { phase == .checking }
    var busy: Bool { phase != .idle }

    override init() {
        super.init()
        newAttempt()
    }

    deinit { server?.stop() }

    /// Fresh PKCE verifier - every sign-in attempt starts with a new one (and a new state, see openSession).
    private func newAttempt() {
        let (v, _) = OAuth.newPKCE()
        verifier = v
        state = ""
    }

    // MARK: - the sheet

    /// "Sign in…": opens the loopback listener (unless manual), then the sign-in sheet.
    func startSignIn() {
        guard phase == .idle else { return }
        errorText = nil
        phase = .opening
        newAttempt()
        if manual {
            openSession(redirectURI: OAuth.manualRedirectURI)
            return
        }
        let server = LoopbackServer(pageTitle: tr("dlg.done_title_mac"), pageBody: tr("dlg.done_body_mac"))
        self.server = server
        server.start(preferredPort: OAuth.loopbackPort, onCallback: { [weak self] cb in
            self?.loopbackCallback(cb)
        }, completion: { [weak self] port in
            guard let self = self, self.phase == .opening else { return }
            if let port = port {
                self.openSession(redirectURI: OAuth.loopbackRedirectURI(port: port))
            } else {
                // no listening socket (ports taken, entitlement missing…): the manual way still works
                Log.api("sign-in: no loopback port, falling back to the manual code")
                self.server = nil
                self.manual = true
                self.openSession(redirectURI: OAuth.manualRedirectURI)
            }
        })
    }

    /// "Sign in with a code instead": the Windows way, no listener.
    func useManual() {
        guard phase == .idle else { return }
        manual = true
        errorText = nil
    }

    private func openSession(redirectURI: String) {
        self.redirectURI = redirectURI
        let challenge = OAuth.challenge(for: verifier)
        let (url, st) = OAuth.buildAuthorize(verifier: verifier, challenge: challenge, redirectURI: redirectURI)
        state = st
        let handler: (URL?, Error?) -> Void = { [weak self] callbackURL, error in
            DispatchQueue.main.async { self?.sessionFinished(callbackURL, error) }
        }
        let s: ASWebAuthenticationSession
        if #available(macOS 14.4, *) {
            s = ASWebAuthenticationSession(url: url, callback: .customScheme(Self.callbackScheme), completionHandler: handler)
        } else {
            s = ASWebAuthenticationSession(url: url, callbackURLScheme: Self.callbackScheme, completionHandler: handler)
        }
        s.presentationContextProvider = self
        s.prefersEphemeralWebBrowserSession = false   // Safari's cookies: an already signed-in user needs no password
        session = s
        guard s.canStart, s.start() else {
            session = nil
            stopServer()
            phase = .idle
            errorText = tr("dlg.err_sheet_mac", tr("dlg.unknown_err"))
            return
        }
        phase = .waiting
    }

    /// Completion of the sheet. Closing it (Cancel, or the app's own cancel after the redirect) is not an error.
    private func sessionFinished(_ callbackURL: URL?, _ error: Error?) {
        session = nil
        if phase == .checking { return }   // the loopback already delivered the code; the app closed the sheet
        if let url = callbackURL {          // not expected (custom scheme), but handle it like a pasted URL
            pasted = url.absoluteString
            phase = .idle
            submit()
            return
        }
        stopServer()
        phase = .idle
        if let err = error as? ASWebAuthenticationSessionError, err.code == .canceledLogin { return }
        if let err = error {
            errorText = tr("dlg.err_sheet_mac", err.localizedDescription)
        }
    }

    /// The loopback listener received the redirect.
    private func loopbackCallback(_ cb: LoopbackServer.Callback) {
        guard phase == .waiting else { return }
        session?.cancel()                   // closes the sheet; its completion arrives as canceledLogin and is ignored
        session = nil
        stopServer()
        if let err = cb.error {
            phase = .idle
            errorText = tr("dlg.err_badcode_mac", err)
            return
        }
        guard let code = cb.code, cb.state == state else {
            phase = .idle
            errorText = tr("dlg.err_badcode_mac", tr("dlg.err_state_mac"))
            return
        }
        exchange(code: code, state: state)
    }

    private func stopServer() {
        server?.stop()
        server = nil
    }

    // MARK: - the pasted code

    func submit() {
        guard !busy else { return }
        var text = pasted.trimmingCharacters(in: .whitespacesAndNewlines)
        if text.isEmpty { return }
        // convenience: sometimes the whole callback URL is pasted
        if text.contains("code="), let comps = URLComponents(string: text) {
            let code = comps.queryItems?.first { $0.name == "code" }?.value ?? ""
            let st = comps.queryItems?.first { $0.name == "state" }?.value ?? state
            if !code.isEmpty { text = "\(code)#\(st)" }
        }
        var code = text
        var st = state
        if let hash = text.firstIndex(of: "#") {
            code = String(text[..<hash])
            st = String(text[text.index(after: hash)...])
        }
        exchange(code: code, state: st)
    }

    private func exchange(code: String, state gotState: String) {
        phase = .checking
        errorText = nil
        let verifier = self.verifier, state = gotState, redirectURI = self.redirectURI
        DispatchQueue.global(qos: .userInitiated).async {
            let (tokens, err) = OAuth.exchange(code: "\(code)#\(state)", verifier: verifier, state: state, redirectURI: redirectURI)
            DispatchQueue.main.async {
                self.phase = .idle
                if let t = tokens, !t.accessToken.isEmpty {
                    self.onSuccess?(t)
                    self.onClose?()
                } else if err.contains("429") || err.contains("rate_limit") {
                    self.errorText = tr("dlg.err_ratelimit_mac")
                } else {
                    self.errorText = tr("dlg.err_badcode_mac", err.isEmpty ? tr("dlg.unknown_err") : err)
                }
            }
        }
    }

    /// Cancel / window closed: everything is torn down, nothing is reported.
    func close() {
        session?.cancel()
        session = nil
        stopServer()
        onClose?()
    }

    // MARK: - ASWebAuthenticationPresentationContextProviding

    func presentationAnchor(for session: ASWebAuthenticationSession) -> ASPresentationAnchor {
        window ?? NSApp.keyWindow ?? NSApp.windows.first ?? ASPresentationAnchor()
    }
}

struct SignInView: View {
    @ObservedObject var model: SignInModel

    var body: some View {
        VStack(alignment: .leading, spacing: 9) {
            Text(tr("dlg.intro_mac")).fixedSize(horizontal: false, vertical: true)
            Text(tr("dlg.step1")).font(.system(size: 15, weight: .semibold)).padding(.top, 4)
            HStack(spacing: 8) {
                Button(model.phase == .waiting ? tr("dlg.waiting_mac") : tr("dlg.open_signin_mac")) { model.startSignIn() }
                    .disabled(model.busy)
                if model.phase == .opening || model.phase == .waiting {
                    ProgressView().controlSize(.small)
                }
            }
            HintText(model.manual ? tr("dlg.hint1") : tr("dlg.hint_auto_mac"))
            if !model.manual {
                Button(tr("dlg.manual_mac")) { model.useManual() }
                    .buttonStyle(.link).font(.system(size: 11)).disabled(model.busy)
            }
            Text(tr("dlg.step2")).font(.system(size: 15, weight: .semibold)).padding(.top, 6)
            HintText(model.manual ? tr("dlg.paste_label") : tr("dlg.paste_label_mac"))
            TextField(tr("dlg.paste_placeholder"), text: $model.pasted).textFieldStyle(.roundedBorder)
                .onSubmit { model.submit() }
            if let e = model.errorText {
                Text(e).foregroundColor(UI.error).fixedSize(horizontal: false, vertical: true)
            }
            HStack {
                Spacer()
                Button(tr("dlg.cancel")) { model.close() }
                Button(model.checking ? tr("dlg.checking") : tr("dlg.signin")) { model.submit() }
                    .keyboardShortcut(.defaultAction)
                    .disabled(model.busy || model.pasted.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty)
            }
        }
        .padding(18)
        .frame(width: 480)
        .preferredColorScheme(.dark)
    }
}

#endif
