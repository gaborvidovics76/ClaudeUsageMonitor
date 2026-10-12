// Small rolling text logs in the app's own Application Support folder (startup.log, api.log).
// No secrets are ever written: the API log records status codes and field NAMES only.

import Foundation

enum Log {
    private static let queue = DispatchQueue(label: "hu.dinorr.claudeusagemonitor.log")

    static func startup(_ message: String) { write("startup.log", message, limit: 60_000) }
    static func api(_ message: String) { write("api.log", message, limit: 80_000) }

    private static func write(_ file: String, _ message: String, limit: Int) {
        let line = "\(stamp())  \(message)\n"
        queue.async {
            let url = AppInfo.supportDirectory.appendingPathComponent(file)
            let fm = FileManager.default
            if let attrs = try? fm.attributesOfItem(atPath: url.path), let size = attrs[.size] as? Int, size > limit,
               let text = try? String(contentsOf: url, encoding: .utf8) {
                let tail = text.split(separator: "\n", omittingEmptySubsequences: false).suffix(200).joined(separator: "\n")
                try? (tail + "\n").write(to: url, atomically: true, encoding: .utf8)
            }
            if let handle = try? FileHandle(forWritingTo: url) {
                handle.seekToEndOfFile()
                handle.write(line.data(using: .utf8)!)
                try? handle.close()
            } else {
                try? line.write(to: url, atomically: true, encoding: .utf8)
            }
        }
    }

    private static func stamp() -> String {
        let f = DateFormatter()
        f.locale = Locale(identifier: "en_US_POSIX")
        f.dateFormat = "yyyy-MM-dd HH:mm:ss"
        return f.string(from: Date())
    }
}
