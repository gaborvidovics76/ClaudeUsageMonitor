// History window: timeline and statistics (port of claude_usage/history.py).

import SwiftUI

final class HistoryModel: ObservableObject {
    @Published var rows: [Sample] = []
    @Published var span: Int = 24 * 3600
    @Published var palette: Palette
    @Published var weeklyResetInMs: Int64? = nil
    let settings: Settings
    var provider: () -> UsageSource

    static let ranges: [(String, Int)] = [("hist.range_6h", 6 * 3600), ("hist.range_24h", 24 * 3600),
                                          ("hist.range_7d", 7 * 86400), ("hist.range_all", 0)]

    init(settings: Settings, provider: @escaping () -> UsageSource) {
        self.settings = settings
        self.provider = provider
        self.palette = Palette(theme: settings.theme, accentHex: settings.accent)
    }

    func refresh() {
        palette = Palette(theme: settings.theme, accentHex: settings.accent)
        let src = provider()
        let since: Int64? = span > 0 ? nowMs() - Int64(span) * 1000 : nil
        rows = src.series(org: settings.org.isEmpty ? nil : settings.org, sinceMs: since)
        weeklyResetInMs = src.read(org: settings.org.isEmpty ? nil : settings.org).weekly.resetInMs
    }
}

struct HistoryView: View {
    @ObservedObject var model: HistoryModel
    @ObservedObject var settings: Settings

    var body: some View {
        VStack(spacing: 10) {
            HStack {
                ForEach(HistoryModel.ranges, id: \.1) { key, span in
                    Button(tr(key)) { model.span = span; model.refresh() }
                        .buttonStyle(.bordered)
                        .tint(model.span == span ? UI.link : nil)
                }
                Spacer()
                HStack(spacing: 6) {
                    Circle().fill(Color(model.palette.ok.nsColor)).frame(width: 8, height: 8)
                    Text(tr("hist.legend_5h"))
                    Circle().fill(Color(model.palette.accent.nsColor)).frame(width: 8, height: 8).padding(.leading, 8)
                    Text(tr("hist.legend_week"))
                }.font(.system(size: 11)).foregroundColor(UI.hint)
            }
            ChartView(model: model, settings: settings).frame(minHeight: 240)
            StatsRow(model: model, settings: settings)
        }
        .padding(14)
        .frame(minWidth: 640, minHeight: 420)
        .background(UI.dialogBG)
        .preferredColorScheme(.dark)
        .onAppear { model.refresh() }
    }
}

private struct ChartView: View {
    @ObservedObject var model: HistoryModel
    @ObservedObject var settings: Settings

    var body: some View {
        Canvas { ctx, size in
            let pal = model.palette
            let full = CGRect(origin: .zero, size: size)
            let r = full.adjusted(34, 12, -10, -22)
            ctx.fill(Path(full), with: .color(Color(RGBA(22, 24, 29).nsColor)))

            // grid + scale
            for (frac, label) in [(0.0, "100"), (0.25, "75"), (0.5, "50"), (0.75, "25"), (1.0, "0")] {
                let y = r.minY + r.height * frac
                var p = Path(); p.move(to: CGPoint(x: r.minX, y: y)); p.addLine(to: CGPoint(x: r.maxX, y: y))
                ctx.stroke(p, with: .color(Color.white.opacity(18.0 / 255)), lineWidth: 1)
                ctx.draw(Text(label).font(.system(size: 9)).foregroundColor(Color(RGBA(120, 128, 146).nsColor)),
                         at: CGPoint(x: 28, y: y), anchor: .trailing)
            }
            // threshold lines
            for (value, color) in [(settings.warn, pal.warn), (settings.danger, pal.danger)] {
                let y = r.maxY - r.height * CGFloat(value / 100)
                var p = Path(); p.move(to: CGPoint(x: r.minX, y: y)); p.addLine(to: CGPoint(x: r.maxX, y: y))
                ctx.stroke(p, with: .color(Color(color.withAlpha(110).nsColor)), style: StrokeStyle(lineWidth: 1, dash: [4, 3]))
            }
            let rows = model.rows
            if rows.count < 2 {
                ctx.draw(Text(tr("hist.no_data")).foregroundColor(Color(pal.dim.nsColor)), at: r.center, anchor: .center)
                return
            }
            let t0 = rows[0].t
            var t1 = max(rows[rows.count - 1].t, nowMs())
            if t1 <= t0 { t1 = t0 + 1 }
            let gapMs: Int64 = 20 * 60 * 1000

            func draw(_ series: [(Int64, Double)], _ color: RGBA, fill: Bool) {
                var segments: [[(Int64, Double)]] = [[]]
                var prev: Int64? = nil
                for (t, v) in series {
                    if let p = prev, t - p > gapMs { segments.append([]) }
                    segments[segments.count - 1].append((t, v))
                    prev = t
                }
                for seg in segments where seg.count >= 2 {
                    var path = Path(), area = Path()
                    for (i, (t, v)) in seg.enumerated() {
                        let x = r.minX + r.width * CGFloat(t - t0) / CGFloat(t1 - t0)
                        let y = r.maxY - r.height * CGFloat(max(0, min(1, v / 100)))
                        if i == 0 {
                            path.move(to: CGPoint(x: x, y: y))
                            area.move(to: CGPoint(x: x, y: r.maxY)); area.addLine(to: CGPoint(x: x, y: y))
                        } else {
                            path.addLine(to: CGPoint(x: x, y: y)); area.addLine(to: CGPoint(x: x, y: y))
                        }
                    }
                    area.addLine(to: CGPoint(x: r.minX + r.width * CGFloat(seg[seg.count - 1].0 - t0) / CGFloat(t1 - t0), y: r.maxY))
                    area.closeSubpath()
                    if fill {
                        ctx.fill(area, with: .linearGradient(Gradient(colors: [Color(color.withAlpha(80).nsColor), Color(color.withAlpha(0).nsColor)]),
                                                             startPoint: CGPoint(x: r.minX, y: r.minY), endPoint: CGPoint(x: r.minX, y: r.maxY)))
                    }
                    ctx.stroke(path, with: .color(Color(color.nsColor)), lineWidth: 1.8)
                }
            }
            if settings.showWeekly { draw(rows.map { ($0.t, $0.sd) }, pal.accent, fill: true) }
            if settings.showFiveHour { draw(rows.map { ($0.t, $0.fh) }, pal.ok, fill: false) }

            // time axis
            let f = DateFormatter()
            f.dateFormat = (t1 - t0) < 2 * 86_400_000 ? "HH:mm" : "MM.dd."
            for frac in [0.0, 0.25, 0.5, 0.75, 1.0] {
                let ts = Double(t0) + Double(t1 - t0) * frac
                let label = f.string(from: Date(timeIntervalSince1970: ts / 1000))
                ctx.draw(Text(label).font(.system(size: 9)).foregroundColor(Color(RGBA(120, 128, 146).nsColor)),
                         at: CGPoint(x: r.minX + r.width * frac, y: r.maxY + 11), anchor: .center)
            }
        }
    }
}

private struct StatsRow: View {
    @ObservedObject var model: HistoryModel
    @ObservedObject var settings: Settings

    private struct Stat { var value: String; var label: String; var color: Color? }

    private func stats() -> [Stat] {
        let rows = model.rows
        let dash = "\u{2013}"
        guard let last = rows.last else {
            return ["hist.stat_now", "hist.stat_peak", "hist.stat_burn", "hist.stat_sessions", "hist.stat_forecast"].map { Stat(value: dash, label: tr($0), color: nil) }
        }
        let peak = rows.map { $0.sd }.max() ?? 0
        let spanDays = max(0.1, Double(rows[rows.count - 1].t - rows[0].t) / 86_400_000)
        var gained = 0.0
        for (a, b) in zip(rows, rows.dropFirst()) where b.sd > a.sd { gained += b.sd - a.sd }
        let perDay = gained / spanDays
        let sessions = zip(rows, rows.dropFirst()).filter { $0.0.fh <= 0 && $0.1.fh > 0 }.count
        let daysLeft = model.weeklyResetInMs.map { Double($0) / 86_400_000 } ?? 7
        let forecast = min(999, last.sd + perDay * daysLeft)
        let pal = model.palette
        let fcColor = forecast >= 100 ? pal.danger : (forecast >= settings.warn ? pal.warn : pal.ok)
        return [
            Stat(value: "\(pct0(last.sd))%", label: tr("hist.stat_now"), color: nil),
            Stat(value: "\(pct0(peak))%", label: tr("hist.stat_peak"), color: nil),
            Stat(value: tr("panel.per_day", num(perDay, 1)), label: tr("hist.stat_burn"), color: nil),
            Stat(value: "\(sessions)", label: tr("hist.stat_sessions"), color: nil),
            Stat(value: "\(pct0(forecast))%", label: tr("hist.stat_forecast"), color: Color(fcColor.nsColor)),
        ]
    }

    var body: some View {
        HStack(alignment: .top) {
            ForEach(Array(stats().enumerated()), id: \.offset) { _, st in
                VStack(alignment: .leading, spacing: 2) {
                    Text(st.value).font(.system(size: 15, weight: .semibold)).foregroundColor(st.color ?? UI.bright)
                    Text(st.label).font(.system(size: 11)).foregroundColor(UI.hint)
                }
                Spacer()
            }
        }
    }
}
