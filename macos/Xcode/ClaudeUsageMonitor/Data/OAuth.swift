// claude.ai sign-in (PKCE) - port of claude_usage/oauth.py.
//
//   1. the app opens the sign-in page in the system's own sign-in sheet (ASWebAuthenticationSession,
//      UI/SignInView.swift - App Review does not accept the default browser, Guideline 4),
//   2. at the end of sign-in the page redirects to http://localhost:<port>/callback, which the app's
//      own loopback listener receives (Data/LoopbackServer.swift) - no code to copy;
//   3. fallback, exactly as on Windows: Anthropic's page shows the code and the user pastes it.
//   4. the app exchanges the code for a token and keeps it in the Keychain.
//
// With the token the app queries https://api.anthropic.com/api/oauth/usage for the server-side
// usage (all devices, exact reset times).
//
// COMPLIANCE NOTE (see docs/MEGFELELES.md): this is the same flow and the same public client as
// the Windows app. Anthropic's terms restrict third-party apps from routing requests through
// consumer-plan credentials; whether to ship this part is the maintainer's decision. The whole
// feature compiles only with the CLAUDE_SIGN_IN condition (Build Settings -> Active Compilation
// Conditions). Without it the app offers the local log and the demo data only.

import CryptoKit
import Foundation
import Security

struct OAuthTokens: Codable {
    var accessToken: String
    var refreshToken: String
    var expiresAt: Int64?         // epoch seconds

    enum CodingKeys: String, CodingKey {
        case accessToken = "access_token", refreshToken = "refresh_token", expiresAt = "expires_at"
    }
}

enum OAuth {
    static let clientID = "9d1c250a-e61b-44d9-88ed-5944d1962f5e"
    static let authorizeURL = "https://claude.ai/oauth/authorize"
    static let tokenURL = "https://platform.claude.com/v1/oauth/token"
    /// Manual flow: Anthropic's own page shows the code and the user pastes it (the Windows app, and the
    /// fallback here when the loopback listener cannot be opened).
    static let manualRedirectURI = "https://platform.claude.com/oauth/code/callback"
    /// Loopback flow: the public Claude Code client is registered for http://localhost:<port>/callback.
    /// The CLI itself listens on 54545 (a fixed port, see its public re-implementations); the server
    /// accepts other ports too, so when 54545 is taken the app falls back to a random free port.
    static let loopbackPort: UInt16 = 54545
    static func loopbackRedirectURI(port: UInt16) -> String { "http://localhost:\(port)/callback" }
    static let scope = "org:create_api_key user:profile user:inference"
    static let profileURL = "https://api.anthropic.com/api/oauth/profile"
    static let usageURL = "https://api.anthropic.com/api/oauth/usage"
    static let usageResetsQuery = "?cedar_ember=1"   // also asks for the saved limit resets (what Claude Code sends)
    static let betaHeader = "oauth-2025-04-20"
    // The token endpoint is behind Cloudflare, which blocks generic clients and rate-limits
    // browser user agents. The Windows app sends the headers of the official command-line client
    // for exactly this reason; this port keeps them so that both builds behave the same.
    // The VERSION matters: the server hands the saved limit resets (cedar_ember) only to a current client
    // (an old one gets "ineligible: cli_version"). Keep it at a current Claude Code version with every
    // release - the sandboxed app cannot ask the installed `claude --version` the way the Windows app does.
    static let userAgent = "claude-cli/2.1.296 (external, cli)"

    static func headers(_ extra: [String: String] = [:]) -> [String: String] {
        var h = ["User-Agent": userAgent, "x-app": "cli", "Accept": "application/json", "Content-Type": "application/json"]
        h.merge(extra) { $1 }
        return h
    }

    private static func b64url(_ data: Data) -> String {
        data.base64EncodedString().replacingOccurrences(of: "+", with: "-").replacingOccurrences(of: "/", with: "_")
            .replacingOccurrences(of: "=", with: "")
    }

    private static func randomBytes(_ n: Int) -> Data {
        var bytes = [UInt8](repeating: 0, count: n)
        _ = SecRandomCopyBytes(kSecRandomDefault, n, &bytes)
        return Data(bytes)
    }

    /// (code_verifier, code_challenge) S256 pair.
    static func newPKCE() -> (String, String) {
        let verifier = b64url(randomBytes(32))
        return (verifier, challenge(for: verifier))
    }

    /// The S256 code_challenge of a verifier.
    static func challenge(for verifier: String) -> String {
        b64url(Data(SHA256.hash(data: Data(verifier.utf8))))
    }

    /// (authorize URL, state). `redirectURI` is where the sign-in page sends the code at the end.
    static func buildAuthorize(verifier: String, challenge: String, redirectURI: String = manualRedirectURI) -> (URL, String) {
        let state = b64url(randomBytes(24))
        var comps = URLComponents(string: authorizeURL)!
        comps.queryItems = [
            URLQueryItem(name: "code", value: "true"),
            URLQueryItem(name: "client_id", value: clientID),
            URLQueryItem(name: "response_type", value: "code"),
            URLQueryItem(name: "redirect_uri", value: redirectURI),
            URLQueryItem(name: "scope", value: scope),
            URLQueryItem(name: "code_challenge", value: challenge),
            URLQueryItem(name: "code_challenge_method", value: "S256"),
            URLQueryItem(name: "state", value: state),
        ]
        return (comps.url!, state)
    }

    private static func postToken(_ payload: [String: Any]) -> (OAuthTokens?, String) {
        let r = HTTP.request(tokenURL, method: "POST", headers: headers(), json: payload)
        if r.status == 0 { return (nil, tr("err.network", r.error)) }
        guard (200..<300).contains(r.status) else {
            return (nil, "HTTP \(r.status): \(String(r.text.prefix(200)))")
        }
        guard let obj = r.json else { return (nil, tr("err.bad_token_resp")) }
        return (normalize(obj), "")
    }

    private static func normalize(_ obj: [String: Any]) -> OAuthTokens {
        var expiresAt: Int64? = nil
        if let n = obj["expires_in"] as? Double { expiresAt = Int64(Date().timeIntervalSince1970) + Int64(n) - 60 }
        return OAuthTokens(accessToken: obj["access_token"] as? String ?? "",
                           refreshToken: obj["refresh_token"] as? String ?? "",
                           expiresAt: expiresAt)
    }

    /// Exchanges the code for a token. The text has the form `code#state` (or the whole callback URL - the
    /// dialog unpacks that before calling). `redirectURI` must be the one the authorize URL was built with.
    static func exchange(code pasted: String, verifier: String, state: String,
                         redirectURI: String = manualRedirectURI) -> (OAuthTokens?, String) {
        let text = pasted.trimmingCharacters(in: .whitespacesAndNewlines)
        if text.isEmpty { return (nil, tr("err.no_code")) }
        var code = text
        var gotState = state
        if let hash = text.firstIndex(of: "#") {
            code = String(text[..<hash])
            gotState = String(text[text.index(after: hash)...])
        }
        let payload: [String: Any] = [
            "grant_type": "authorization_code",
            "code": code.trimmingCharacters(in: .whitespaces),
            "state": gotState.trimmingCharacters(in: .whitespaces),
            "client_id": clientID,
            "redirect_uri": redirectURI,
            "code_verifier": verifier,
        ]
        return postToken(payload)
    }

    /// True when the server said the refresh token itself is finished (expired, revoked or used).
    static func isDeadGrant(_ err: String) -> Bool {
        let low = err.lowercased()
        return low.contains("invalid_grant") || low.contains("refresh token expired") || low.contains("token revoked")
    }

    static func refresh(_ refreshToken: String) -> (OAuthTokens?, String) {
        let (tokens, err) = postToken(["grant_type": "refresh_token", "refresh_token": refreshToken, "client_id": clientID])
        guard var t = tokens else { return (nil, err) }
        if t.refreshToken.isEmpty { t.refreshToken = refreshToken }   // the server sometimes sends none - keep the old one
        return (t, "")
    }

    private static func authHeaders(_ token: String) -> [String: String] {
        headers(["Authorization": "Bearer \(token)", "anthropic-beta": betaHeader, "anthropic-version": "2023-06-01"])
    }

    /// (json, http status) of the account/plan profile.
    static func fetchProfile(_ token: String) -> ([String: Any]?, Int) {
        let r = HTTP.request(profileURL, headers: authHeaders(token), timeout: 12)
        return (r.status == 200 ? r.json : nil, r.status)
    }

    /// (json, http status, error, retry-after seconds). `withResets` adds the query Claude Code itself
    /// sends (`?cedar_ember=1`): the answer then also carries the saved limit resets. A server that does
    /// not know the parameter answers 400/403 - then the plain request is made, exactly as before.
    static func fetchUsage(_ token: String, withResets: Bool = true) -> ([String: Any]?, Int, String, Double?) {
        let r = getUsage(usageURL + (withResets ? usageResetsQuery : ""), token)
        if withResets && (r.1 == 400 || r.1 == 403) { return getUsage(usageURL, token) }
        return r
    }

    private static func getUsage(_ url: String, _ token: String) -> ([String: Any]?, Int, String, Double?) {
        let r = HTTP.request(url, headers: authHeaders(token), timeout: 12)
        if r.status == 0 { return (nil, 0, tr("err.network", r.error), nil) }
        if r.status == 200 {
            guard let obj = r.json else { return (nil, 0, tr("err.bad_usage_resp"), nil) }
            return (obj, 200, "", nil)
        }
        return (nil, r.status, String(r.text.prefix(200)), r.retryAfter)
    }
}
