// "Message to the developer" - sends the form to the project's own website over HTTPS
// (port of claude_usage/feedback.py). Nothing leaves the machine unless the user presses Send.

import Foundation

enum Feedback {
    static let consentVersion = "2026-10-06"       // bump when the privacy notice text changes
    static let maxName = 80, maxEmail = 120, maxMessage = 4000
    static let errors = ["rate", "fields", "email", "consent", "links", "server", "network", "client"]

    /// "macOS 15.1 (arm64)" - no user name, no machine name.
    static func osName() -> String {
        let v = ProcessInfo.processInfo.operatingSystemVersion
        var machine = utsname()
        uname(&machine)
        let arch = withUnsafeBytes(of: &machine.machine) { raw -> String in
            let bytes = raw.prefix { $0 != 0 }
            return String(decoding: bytes, as: UTF8.self)
        }
        return "macOS \(v.majorVersion).\(v.minorVersion).\(v.patchVersion) (\(arch))"
    }

    static func buildPayload(name: String, email: String, message: String, rating: Int, publish: Bool, lang: String) -> [String: Any] {
        let r = (1...5).contains(rating) ? rating : 0
        return [
            "client": "app",
            "version": AppInfo.version,
            "os": osName(),
            "lang": lang,
            "name": String(name.trimmingCharacters(in: .whitespacesAndNewlines).prefix(maxName)),
            "email": String(email.trimmingCharacters(in: .whitespacesAndNewlines).prefix(maxEmail)),
            "message": String(message.trimmingCharacters(in: .whitespacesAndNewlines).prefix(maxMessage)),
            "rating": r,
            "publish": (publish && r > 0) ? 1 : 0,
            "consent": 1,
            "consent_version": consentVersion,
            "website": "",                      // honeypot - a real client leaves it empty
        ]
    }

    /// Posts the form on a background queue; `done(ok, errorCode)` arrives on the main queue.
    static func send(_ payload: [String: Any], done: @escaping (Bool, String) -> Void) {
        DispatchQueue.global(qos: .userInitiated).async {
            let r = HTTP.request(AppInfo.feedbackURL, method: "POST", headers: [
                "User-Agent": "ClaudeUsageMonitor/\(AppInfo.version)",
                "X-UM-Client": "ClaudeUsageMonitor/\(AppInfo.version)",
                "Content-Type": "application/json; charset=utf-8",
                "Accept": "application/json",
                "Cache-Control": "no-cache",
            ], json: payload)
            var ok = false
            var code = ""
            if r.status == 0 { code = "network" }
            else if r.status == 429 { code = "rate" }
            else if let j = r.json, j["ok"] as? Bool == true { ok = true }
            else {
                let c = (r.json?["error"] as? String) ?? ""
                code = errors.contains(c) ? c : "server"
            }
            DispatchQueue.main.async { done(ok, code) }
        }
    }
}
