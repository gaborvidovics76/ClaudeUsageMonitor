// Loopback HTTP listener for the OAuth redirect (http://localhost:<port>/callback).
//
// Network.framework only, no third-party code. Bound to the loopback interface (127.0.0.1, and ::1
// when it is free, because the sign-in sheet may resolve "localhost" to either), so nothing from
// another machine can reach it. It accepts one redirect - the /callback request whose `state` is the
// one this sign-in attempt issued - answers it with a small "done" page and closes; anything else
// (another path, a /callback with a foreign or missing state) gets an error page and the listener
// stays open, so a stray local request cannot cancel the sign-in. The listener lives while the
// sign-in window is open. In the App Sandbox a listening socket needs the
// com.apple.security.network.server entitlement (see ClaudeUsageMonitor.entitlements).

import Foundation
import Network

#if CLAUDE_SIGN_IN

final class LoopbackServer {
    /// What the redirect carried. `error` is the OAuth error the server sent instead of a code
    /// (e.g. the user denied access), or the reason the request was unusable.
    struct Callback {
        var code: String?
        var state: String?
        var error: String?
    }

    private let queue = DispatchQueue(label: "ClaudeUsageMonitor.loopback")
    private var listeners: [NWListener] = []
    private var connections: [NWConnection] = []
    private var delivered = false
    private var onCallback: ((Callback) -> Void)?
    private let pageTitle: String
    private let pageBody: String
    private let expectedState: String
    private(set) var port: UInt16 = 0

    /// `expectedState`: the `state` of this sign-in attempt - only a redirect carrying it is accepted.
    /// `pageTitle` / `pageBody`: the texts of the page shown in place of the redirect (localized by the caller).
    init(expectedState: String, pageTitle: String, pageBody: String) {
        self.expectedState = expectedState
        self.pageTitle = pageTitle
        self.pageBody = pageBody
    }

    deinit {
        // no dispatch here: the object is going away, cancel directly (cancel() is thread-safe)
        listeners.forEach { $0.cancel() }
        connections.forEach { $0.cancel() }
    }

    /// Opens the listener on `preferredPort`; when that port is taken (or refused), on a random free port.
    /// `completion` runs on the main queue with the listening port, or nil when no port could be opened.
    /// `onCallback` runs on the main queue, once, with the first /callback request.
    func start(preferredPort: UInt16, onCallback: @escaping (Callback) -> Void, completion: @escaping (UInt16?) -> Void) {
        self.onCallback = onCallback
        open(port: preferredPort) { [weak self] ok in
            guard let self = self else { DispatchQueue.main.async { completion(nil) }; return }
            if ok {
                DispatchQueue.main.async { completion(self.port) }
                return
            }
            Log.api("loopback: port \(preferredPort) not available, trying a random port")
            self.open(port: 0) { ok2 in
                DispatchQueue.main.async { completion(ok2 ? self.port : nil) }
            }
        }
    }

    /// Closes everything. Safe to call more than once and from any queue.
    func stop() {
        queue.async { [self] in
            listeners.forEach { $0.cancel() }
            listeners.removeAll()
            connections.forEach { $0.cancel() }
            connections.removeAll()
        }
    }

    // MARK: - listening

    /// Opens the IPv4 listener on `port` (0 = any free port); `done(true)` once it is ready. The IPv6
    /// loopback listener on the same port is best effort: WebKit may resolve "localhost" to ::1 first.
    private func open(port: UInt16, done: @escaping (Bool) -> Void) {
        queue.async { [self] in
            var finished = false
            let finish: (Bool) -> Void = { ok in
                guard !finished else { return }
                finished = true
                done(ok)
            }
            guard let v4 = makeListener(host: .ipv4(.loopback), port: port) else { finish(false); return }
            v4.stateUpdateHandler = { [weak self, weak v4] state in
                guard let self = self else { return }
                switch state {
                case .ready:
                    guard let p = v4?.port?.rawValue, p != 0 else { finish(false); return }
                    self.port = p
                    if let v6 = self.makeListener(host: .ipv6(.loopback), port: p) {
                        v6.stateUpdateHandler = { [weak v6] st in
                            if case .failed = st { v6?.cancel() }   // ::1 taken: IPv4 alone is enough
                        }
                        v6.newConnectionHandler = { [weak self] c in self?.accept(c) }
                        v6.start(queue: self.queue)
                        self.listeners.append(v6)
                    }
                    finish(true)
                case .failed(let err):
                    Log.api("loopback: listener on \(port) failed: \(err)")
                    v4?.cancel()
                    self.listeners.removeAll { $0 === v4 }
                    finish(false)
                case .cancelled:
                    finish(false)
                default:
                    break
                }
            }
            v4.newConnectionHandler = { [weak self] c in self?.accept(c) }
            listeners.append(v4)
            v4.start(queue: queue)
        }
    }

    private func makeListener(host: NWEndpoint.Host, port: UInt16) -> NWListener? {
        let params = NWParameters.tcp
        params.allowLocalEndpointReuse = true
        let p: NWEndpoint.Port = port == 0 ? .any : (NWEndpoint.Port(rawValue: port) ?? .any)
        params.requiredLocalEndpoint = NWEndpoint.hostPort(host: host, port: p)
        return try? NWListener(using: params)
    }

    // MARK: - one HTTP request

    private func accept(_ conn: NWConnection) {
        connections.append(conn)
        conn.stateUpdateHandler = { [weak self, weak conn] state in
            switch state {
            case .failed, .cancelled:
                if let c = conn { self?.connections.removeAll { $0 === c } }
            default:
                break
            }
        }
        conn.start(queue: queue)
        receive(conn, buffer: Data())
    }

    private func receive(_ conn: NWConnection, buffer: Data) {
        conn.receive(minimumIncompleteLength: 1, maximumLength: 16 * 1024) { [weak self] data, _, isComplete, error in
            guard let self = self else { return }
            var buf = buffer
            if let d = data { buf.append(d) }
            if let end = buf.range(of: Data("\r\n\r\n".utf8)) {
                self.respond(conn, requestHead: String(decoding: buf[..<end.lowerBound], as: UTF8.self))
            } else if isComplete || error != nil || buf.count > 64 * 1024 {
                conn.cancel()
            } else {
                self.receive(conn, buffer: buf)
            }
        }
    }

    private func respond(_ conn: NWConnection, requestHead: String) {
        let requestLine = requestHead.split(separator: "\r\n", maxSplits: 1).first.map(String.init) ?? ""
        let parts = requestLine.split(separator: " ")
        let method = parts.count > 0 ? String(parts[0]) : ""
        let target = parts.count > 1 ? String(parts[1]) : ""
        guard method == "GET", target == "/callback" || target.hasPrefix("/callback?"),
              let comps = URLComponents(string: "http://localhost" + target) else {
            send(conn, status: "404 Not Found", html: page(title: "404", body: "Not found"))
            return
        }
        let items = comps.queryItems ?? []
        func q(_ name: String) -> String? { items.first { $0.name == name }?.value }
        var cb = Callback(code: q("code"), state: q("state"), error: nil)
        guard !delivered, cb.state == expectedState else {
            // not this sign-in's redirect (a stray local request, a reload): refuse it and keep listening
            send(conn, status: "400 Bad Request",
                 html: page(title: "400", body: "This request does not belong to the current sign-in."))
            return
        }
        if let err = q("error") {
            cb.error = [err, q("error_description")].compactMap { $0 }.joined(separator: ": ")
        } else if (cb.code ?? "").isEmpty {
            cb.error = "no code in the callback"
        }
        send(conn, status: "200 OK", html: page(title: pageTitle, body: pageBody))
        // one callback only - later connections (favicon, a reload) are refused
        listeners.forEach { $0.cancel() }
        listeners.removeAll()
        delivered = true
        let handler = onCallback
        DispatchQueue.main.async { handler?(cb) }
    }

    private func send(_ conn: NWConnection, status: String, html: String) {
        let body = Data(html.utf8)
        let head = "HTTP/1.1 \(status)\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: \(body.count)\r\n"
            + "Cache-Control: no-store\r\nConnection: close\r\n\r\n"
        conn.send(content: Data(head.utf8) + body, isComplete: true, completion: .contentProcessed { _ in
            conn.cancel()
        })
    }

    private func page(title: String, body: String) -> String {
        let t = Self.escape(title), b = Self.escape(body)
        return """
        <!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
        <title>\(t)</title><style>
        body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
        background:#16181d;color:#d6dbe8;font:15px/1.5 -apple-system,system-ui,sans-serif}
        main{max-width:28em;padding:2em;text-align:center}h1{font-size:1.3em;color:#f0f3fa;margin:0 0 .5em}
        p{margin:0;color:#79839a}
        </style></head><body><main><h1>\(t)</h1><p>\(b)</p></main></body></html>
        """
    }

    private static func escape(_ s: String) -> String {
        s.replacingOccurrences(of: "&", with: "&amp;").replacingOccurrences(of: "<", with: "&lt;")
            .replacingOccurrences(of: ">", with: "&gt;").replacingOccurrences(of: "\"", with: "&quot;")
    }
}

#endif
