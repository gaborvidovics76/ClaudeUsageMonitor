// Token storage: the data-protection Keychain (SecItem). The secret never touches a file.
// In a sandboxed app the item belongs to the app's own keychain access group, so no extra
// entitlement is needed (TN3137). The whole token set is stored as one JSON string.

import Foundation
import Security

enum Keychain {
    private static let service = "ClaudeUsageMonitor"
    private static let account = "claude.ai-oauth"

    private static var baseQuery: [String: Any] {
        [kSecClass as String: kSecClassGenericPassword,
         kSecAttrService as String: service,
         kSecAttrAccount as String: account,
         kSecUseDataProtectionKeychain as String: true]
    }

    static func save(_ value: String) -> Bool {
        guard let data = value.data(using: .utf8) else { return false }
        let attrs: [String: Any] = [kSecValueData as String: data,
                                    kSecAttrAccessible as String: kSecAttrAccessibleAfterFirstUnlock]
        var status = SecItemUpdate(baseQuery as CFDictionary, attrs as CFDictionary)
        if status == errSecItemNotFound {
            var add = baseQuery
            add.merge(attrs) { $1 }
            status = SecItemAdd(add as CFDictionary, nil)
        }
        if status != errSecSuccess { Log.api("keychain save failed: \(status)") }
        return status == errSecSuccess
    }

    static func load() -> String? {
        var query = baseQuery
        query[kSecReturnData as String] = true
        query[kSecMatchLimit as String] = kSecMatchLimitOne
        var item: CFTypeRef?
        let status = SecItemCopyMatching(query as CFDictionary, &item)
        guard status == errSecSuccess, let data = item as? Data else { return nil }
        return String(data: data, encoding: .utf8)
    }

    static func clear() {
        SecItemDelete(baseQuery as CFDictionary)
    }

    // MARK: tokens

    static func loadTokens() -> OAuthTokens? {
        guard let text = load(), let data = text.data(using: .utf8) else { return nil }
        return try? JSONDecoder().decode(OAuthTokens.self, from: data)
    }

    @discardableResult
    static func saveTokens(_ tokens: OAuthTokens) -> Bool {
        guard let data = try? JSONEncoder().encode(tokens), let text = String(data: data, encoding: .utf8) else { return false }
        return save(text)
    }

    static var hasTokens: Bool { !(loadTokens()?.accessToken ?? "").isEmpty }
}
