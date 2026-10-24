// Token storage: the Keychain (SecItem). The secret never touches a file. The whole token set is
// stored as one JSON string.
//
// Two places the item may live:
//   - the data-protection keychain (kSecUseDataProtectionKeychain) - preferred: per-app access, no
//     keychain prompts. On macOS it needs the com.apple.application-identifier entitlement, which only
//     a provisioning profile puts into the app (App Store / TestFlight build). A local Xcode build has
//     no profile and gets errSecMissingEntitlement (-34018) - TN3137's "no extra entitlement" holds
//     only for a profiled build;
//   - the login keychain (file-based) - the fallback for exactly that case: a sandboxed app may store
//     its own items there without any entitlement.
// Reading looks in both, in that order; clearing removes both.

import Foundation
import Security

enum Keychain {
    private static let service = "ClaudeUsageMonitor"
    private static let account = "claude.ai-oauth"

    private enum Store: CaseIterable { case dataProtection, login }

    private static func query(_ store: Store) -> [String: Any] {
        // explicit in both cases: a query targets exactly one of the two stores (TN3137)
        [kSecClass as String: kSecClassGenericPassword,
         kSecAttrService as String: service,
         kSecAttrAccount as String: account,
         kSecUseDataProtectionKeychain as String: store == .dataProtection]
    }

    private static func save(_ data: Data, to store: Store) -> OSStatus {
        var attrs: [String: Any] = [kSecValueData as String: data]
        // kSecAttrAccessible is a data-protection attribute; the file-based keychain rejects it
        if store == .dataProtection { attrs[kSecAttrAccessible as String] = kSecAttrAccessibleAfterFirstUnlock }
        var status = SecItemUpdate(query(store) as CFDictionary, attrs as CFDictionary)
        if status == errSecItemNotFound {
            var add = query(store)
            add.merge(attrs) { $1 }
            status = SecItemAdd(add as CFDictionary, nil)
        }
        return status
    }

    static func save(_ value: String) -> Bool {
        guard let data = value.data(using: .utf8) else { return false }
        var status = save(data, to: .dataProtection)
        if status == errSecMissingEntitlement {
            // no application-identifier (local build): the login keychain takes the item
            Log.api("keychain: data-protection keychain unavailable (-34018, no provisioning profile), using the login keychain")
            status = save(data, to: .login)
        } else if status == errSecSuccess {
            // housekeeping: a copy a local (unprofiled) build left in the login keychain is stale now
            SecItemDelete(query(.login) as CFDictionary)
        }
        if status != errSecSuccess { Log.api("keychain save failed: \(status)") }
        return status == errSecSuccess
    }

    static func load() -> String? {
        for store in Store.allCases {
            var q = query(store)
            q[kSecReturnData as String] = true
            q[kSecMatchLimit as String] = kSecMatchLimitOne
            var item: CFTypeRef?
            let status = SecItemCopyMatching(q as CFDictionary, &item)
            if status == errSecSuccess, let data = item as? Data, let text = String(data: data, encoding: .utf8) {
                return text
            }
            if status != errSecItemNotFound && status != errSecMissingEntitlement {
                Log.api("keychain load failed (\(store)): \(status)")
            }
        }
        return nil
    }

    static func clear() {
        for store in Store.allCases { SecItemDelete(query(store) as CFDictionary) }
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
