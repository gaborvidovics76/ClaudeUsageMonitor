// Localization: the same keys and texts as the Windows app (claude_usage/i18n.py), compiled into
// Resources/Localizable.xcstrings by tools/gen_xcstrings.py. The language can be changed at run
// time from the menu, so the strings are read from the chosen .lproj bundle by hand instead of
// through NSLocalizedString (which is fixed to the system language for the whole process).
//
// Fallback chain: the chosen language -> its sibling variant (pt-PT <-> pt-BR, es-ES <-> es-419)
// -> English -> the key itself.  Placeholders are Python-style: "{}" (next argument) or "{0}".

import Foundation

enum L10n {
    /// The available languages in menu order (English first, then by their own name) - the codes
    /// are the ones the Windows app uses in its settings, so a translation file serves both.
    static let languages: [(code: String, name: String)] = [
        ("en", "English"), ("bg", "Български"), ("cs", "Čeština"), ("da", "Dansk"), ("de", "Deutsch"),
        ("et", "Eesti"), ("el", "Ελληνικά"), ("es-ES", "Español (España)"), ("es-419", "Español (Latinoamérica)"),
        ("fr", "Français"), ("ga", "Gaeilge"), ("hr", "Hrvatski"), ("id", "Bahasa Indonesia"), ("it", "Italiano"),
        ("lv", "Latviešu"), ("lt", "Lietuvių"), ("hu", "Magyar"), ("mt", "Malti"), ("nl", "Nederlands"),
        ("pl", "Polski"), ("pt-BR", "Português (Brasil)"), ("pt-PT", "Português (Portugal)"), ("ro", "Română"),
        ("ru", "Русский"), ("sk", "Slovenčina"), ("sl", "Slovenščina"), ("fi", "Suomi"), ("sv", "Svenska"),
        ("tr", "Türkçe"), ("vi", "Tiếng Việt"), ("ja", "日本語"), ("ko", "한국어"), ("zh-CN", "简体中文"),
        ("zh-TW", "繁體中文"),
    ]

    static let defaultLanguage = "en"

    /// A missing text falls back to the other variant of the same language. The two Chinese
    /// variants do NOT fall back on each other: the other script is foreign to the reader.
    static let siblings: [String: String] = ["pt-BR": "pt-PT", "pt-PT": "pt-BR", "es-ES": "es-419", "es-419": "es-ES"]

    /// App language code -> the .lproj folder name Apple uses.
    static let appleLocale: [String: String] = ["es-ES": "es", "zh-CN": "zh-Hans", "zh-TW": "zh-Hant"]

    /// Website folder of each language (the site has one page per app language).
    static let siteFolder: [String: String] = ["es-ES": "es", "pt-BR": "pt", "pt-PT": "pt-pt", "es-419": "es-419",
                                                "zh-CN": "zh-cn", "zh-TW": "zh-tw"]

    private(set) static var current = defaultLanguage
    private static var bundleCache: [String: Bundle?] = [:]
    private static let lock = NSLock()

    static func isSupported(_ code: String) -> Bool { languages.contains { $0.code == code } }

    static func languageName(_ code: String) -> String { languages.first { $0.code == code }?.name ?? code }

    static func setLanguage(_ code: String) {
        lock.lock(); defer { lock.unlock() }
        current = isSupported(code) ? code : defaultLanguage
    }

    /// Maps a BCP-47 tag ('zh-Hant-TW', 'pt_BR', 'es-MX', 'hr-HR', 'sr-Latn') to a supported code or "".
    static func normalizeTag(_ tag: String) -> String {
        let parts = tag.replacingOccurrences(of: "_", with: "-").split(separator: "-").map { String($0) }
        guard let first = parts.first else { return "" }
        let lang = first.lowercased()
        let rest = parts.dropFirst().map { $0.lowercased() }
        switch lang {
        case "zh":
            if rest.contains("hant") || rest.contains(where: { ["tw", "hk", "mo"].contains($0) }) { return "zh-TW" }
            return "zh-CN"
        case "pt":
            return rest.contains(where: { ["pt", "ao", "mz", "cv", "gw", "st", "tl"].contains($0) }) ? "pt-PT" : "pt-BR"
        case "es":
            return (rest.isEmpty || rest.contains("es") || rest.contains("ea") || rest.contains("ic")) ? "es-ES" : "es-419"
        case "sr", "bs":
            return ""
        default:
            return isSupported(lang) ? lang : ""
        }
    }

    /// The best supported language for the user's preferred languages (else English).
    static func systemLanguage() -> String {
        for tag in Locale.preferredLanguages {
            let code = normalizeTag(tag)
            if isSupported(code) { return code }
        }
        return defaultLanguage
    }

    /// Settings written before 2.7.0 stored the undivided "pt" / "es" codes.
    static func migrate(_ code: String) -> String {
        if code == "pt" { let s = systemLanguage(); return (s == "pt-BR" || s == "pt-PT") ? s : "pt-PT" }
        if code == "es" { let s = systemLanguage(); return (s == "es-ES" || s == "es-419") ? s : "es-ES" }
        return code
    }

    private static func bundle(for code: String) -> Bundle? {
        lock.lock(); defer { lock.unlock() }
        if let cached = bundleCache[code] { return cached }
        let folder = appleLocale[code] ?? code
        var found: Bundle? = nil
        if let url = Bundle.main.url(forResource: folder, withExtension: "lproj") {
            found = Bundle(url: url)
        }
        bundleCache[code] = found
        return found
    }

    private static let missing = "\u{1}missing\u{1}"

    /// The text of a key in a language, following the fallback chain (variant -> sibling -> English).
    static func lookup(_ key: String, lang: String? = nil) -> String {
        let want = lang ?? current
        var chain = [want]
        if let sib = siblings[want] { chain.append(sib) }
        if !chain.contains(defaultLanguage) { chain.append(defaultLanguage) }
        for code in chain {
            if let b = bundle(for: code) {
                let text = b.localizedString(forKey: key, value: missing, table: nil)
                if text != missing && !text.isEmpty { return text }
            }
        }
        return key
    }

    /// tr("panel.updated", "3 min") -> "updated: 3 min".  Arguments fill "{}" in order, "{0}" by index.
    static func tr(_ key: String, _ args: Any...) -> String {
        let text = lookup(key)
        if args.isEmpty { return text }
        return format(text, args)
    }

    static func format(_ text: String, _ args: [Any]) -> String {
        var out = ""
        var next = 0
        var i = text.startIndex
        while i < text.endIndex {
            let ch = text[i]
            if ch == "{" {
                if let close = text[i...].firstIndex(of: "}") {
                    let inner = text[text.index(after: i)..<close]
                    if inner.isEmpty {
                        if next < args.count { out += "\(args[next])" }
                        next += 1
                        i = text.index(after: close)
                        continue
                    } else if let n = Int(inner), n >= 0, n < args.count {
                        out += "\(args[n])"
                        i = text.index(after: close)
                        continue
                    }
                }
            }
            out.append(ch)
            i = text.index(after: i)
        }
        return out
    }
}

/// Short alias used throughout the UI code.
@inline(__always) func tr(_ key: String, _ args: Any...) -> String {
    L10n.trArgs(key, args)
}

extension L10n {
    /// tr() with an already-built argument array (the variadic helper above forwards here).
    static func trArgs(_ key: String, _ args: [Any]) -> String {
        let text = lookup(key)
        return args.isEmpty ? text : format(text, args)
    }
}
