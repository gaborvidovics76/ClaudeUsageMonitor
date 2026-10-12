// claude.ai sign-in through the system browser (PKCE, manual code) - port of claude_usage/oauth.py.
//
//   1. the app opens the sign-in page in the user's own browser,
//   2. at the end of sign-in the page shows a code,
//   3. the user pastes it into the app, which exchanges it for a token.
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
    static let redirectURI = "https://platform.claude.com/oauth/code/callback"
    static let scope = "org:create_api_key user:profile user:inference"
    static let profileURL = "https://api.anthropic.com/api/oauth/profile"
    static let usageURL = "https://api.anthropic.com/api/oauth/usage"
    static let betaHeader = "oauth-2025-04-20"
    // The token endpoint is behind Cloudflare, which blocks generic clients and rate-limits
    // browser user agents. The Windows app sends the headers of the official command-line client
    // for exactly this reason; this port keeps them so that both builds behave the same.
    static let userAgent = "claude-cli/2.1.229 (external)"

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
        let digest = SHA256.hash(data: Data(verifier.utf8))
        return (verifier, b64url(Data(digest)))
    }

    /// (authorize URL, state).
    static func buildAuthorize(verifier: String, challenge: String) -> (URL, String) {
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

    /// Exchanges the pasted code for a token. The pasted text has the form `code#state`
    /// (or the whole callback URL - the dialog unpacks that before calling).
    static func exchange(code pasted: String, verifier: String, state: String) -> (OAuthTokens?, String) {
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

    /// (json, http status, error, retry-after seconds).
    static func fetchUsage(_ token: String) -> ([String: Any]?, Int, String, Double?) {
        let r = HTTP.request(usageURL, headers: authHeaders(token), timeout: 12)
        if r.status == 0 { return (nil, 0, tr("err.network", r.error), nil) }
        if r.status == 200 {
            guard let obj = r.json else { return (nil, 0, tr("err.bad_usage_resp"), nil) }
            return (obj, 200, "", nil)
        }
        return (nil, r.status, String(r.text.prefix(200)), r.retryAfter)
    }
}
