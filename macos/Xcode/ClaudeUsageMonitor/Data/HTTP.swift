// A tiny synchronous HTTPS helper for the background workers (the data sources run on their own
// dispatch queues exactly like the Python threads did; the UI never waits on the network).

import Foundation

struct HTTPResult {
    var status: Int              // 0 = no response (network error)
    var body: Data
    var error: String            // "" when a response arrived
    var retryAfter: Double?      // the Retry-After header in seconds, when present

    var text: String { String(data: body, encoding: .utf8) ?? "" }

    var json: [String: Any]? {
        (try? JSONSerialization.jsonObject(with: body)) as? [String: Any]
    }
}

enum HTTP {
    private static let session: URLSession = {
        let cfg = URLSessionConfiguration.ephemeral        // no cookies, no cache, nothing on disk
        cfg.timeoutIntervalForRequest = 20
        cfg.timeoutIntervalForResource = 40
        cfg.httpCookieAcceptPolicy = .never
        cfg.httpShouldSetCookies = false
        cfg.tlsMinimumSupportedProtocolVersion = .TLSv12
        return URLSession(configuration: cfg)
    }()

    /// Blocking request. Only call this from a background queue.
    static func request(_ url: String, method: String = "GET", headers: [String: String] = [:],
                        json: [String: Any]? = nil, timeout: TimeInterval = 20) -> HTTPResult {
        guard let u = URL(string: url) else { return HTTPResult(status: 0, body: Data(), error: "bad url", retryAfter: nil) }
        var req = URLRequest(url: u, cachePolicy: .reloadIgnoringLocalCacheData, timeoutInterval: timeout)
        req.httpMethod = method
        for (k, v) in headers { req.setValue(v, forHTTPHeaderField: k) }
        if let json = json {
            req.httpBody = try? JSONSerialization.data(withJSONObject: json)
            if req.value(forHTTPHeaderField: "Content-Type") == nil {
                req.setValue("application/json", forHTTPHeaderField: "Content-Type")
            }
        }
        let sem = DispatchSemaphore(value: 0)
        var result = HTTPResult(status: 0, body: Data(), error: "", retryAfter: nil)
        let task = session.dataTask(with: req) { data, resp, err in
            if let err = err {
                result = HTTPResult(status: 0, body: Data(), error: err.localizedDescription, retryAfter: nil)
            } else if let http = resp as? HTTPURLResponse {
                var retry: Double? = nil
                if let ra = http.value(forHTTPHeaderField: "Retry-After"), let n = Double(ra) { retry = n }
                result = HTTPResult(status: http.statusCode, body: data ?? Data(), error: "", retryAfter: retry)
            } else {
                result = HTTPResult(status: 0, body: data ?? Data(), error: "no response", retryAfter: nil)
            }
            sem.signal()
        }
        task.resume()
        sem.wait()
        return result
    }
}
