// The interface both measurement sources (and the demo data) offer to the controller.

import Foundation

protocol UsageSource: AnyObject {
    /// Current figures. Never blocks: the network sources answer from their last result.
    func read(org: String?) -> Metrics
    /// Raw samples for the history window.
    func series(org: String?, sinceMs: Int64?) -> [Sample]
    /// Profiles seen in the local log ("" = none / not applicable).
    func organizations() -> [String]
}
