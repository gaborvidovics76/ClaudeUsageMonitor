"""Microsoft Store listing images, rendered from the program itself with sample data (no sign-in, no
user settings touched).

    python tools/make_store_shots.py                 -> docs/store/screenshots/{en,hu,de}/*.png + captions
    python tools/make_store_shots.py hu ja --all-langs-no   (any app language codes)
    python tools/make_store_shots.py --out D:\\x       other output folder

Store rules (learn.microsoft.com, "App screenshots, images, and trailers for MSIX app"):
  * desktop screenshots: PNG, 1366x768 or larger (4K ok), max 50 MB, up to 10 per language;
    keep the important part in the top two-thirds (overlays may cover the bottom third);
    no extra logos, icons or marketing text on the image.
  * 1:1 app tile icon 300x300 (strongly recommended), 16:9 "super hero" 1920x1080 WITHOUT text
    and WITHOUT showing the app UI (recommended).
Every screenshot here is 1920x1080: the live program UI on a plain dark background, nothing else.
"""
from __future__ import annotations

import os
import sys
import time

# the real platform renderer (true fonts - the "offscreen" platform has none and draws boxes);
# the windows are created but never shown on the screen
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from PySide6.QtCore import QPoint, QPointF, QRectF, Qt  # noqa: E402
from PySide6.QtGui import QColor, QLinearGradient, QPainter, QPixmap, QRegion  # noqa: E402
from PySide6.QtWidgets import QApplication, QTabWidget, QWidget  # noqa: E402

app = QApplication([])

from claude_usage.uistyle import checkbox_qss  # noqa: E402

app.setStyleSheet(checkbox_qss())

from claude_usage import i18n  # noqa: E402
from claude_usage import settings as settings_mod  # noqa: E402
from claude_usage.datasource import (DetailRow, ExtraUsage, Gauge, Metrics, ProductShare, ProfileInfo,  # noqa: E402
                                     ResetGrants, Sample)
from claude_usage.localmodels import ModelShare  # noqa: E402
from claude_usage.winutil import app_pixmap  # noqa: E402

W, H = 1920, 1080
HOUR = 3_600_000


class FakeSettings(settings_mod.Settings):
    def load(self) -> None:          # never the user's settings
        pass

    def save(self) -> None:
        pass


def sample_metrics(now: int) -> Metrics:
    m = Metrics(ok=True, updated_at=now - 50_000, sample_count=300)
    m.five_hour = Gauge(value=44, reset_at=now + 57 * 60_000, reset_certain=True, burn=9.5,
                        spark=[5, 9, 14, 20, 28, 33, 39, 44])
    m.weekly = Gauge(value=38, reset_at=now + (3 * 24 + 10) * HOUR, reset_certain=True, burn=0.6, pace=4.0,
                     spark=[10, 14, 18, 22, 27, 31, 35, 38])
    m.model = Gauge(value=41, reset_at=now + (3 * 24 + 10) * HOUR, reset_certain=True, burn=0.7, pace=6.0,
                    spark=[12, 16, 20, 25, 30, 34, 38, 41])
    m.model_name = "Fable"
    m.active = "fh"
    m.rows = [DetailRow("surface:oauth_apps", "surface", "@oauth_apps", 12.0, now + 5 * 24 * HOUR),
              DetailRow("kind:seven_day_cowork", "other", "@cowork", 9.0, now + 2 * 24 * HOUR)]
    m.resets = ResetGrants(count=1, total=1, expires_at=now + 9 * 24 * HOUR, eligible=True)
    m.products = [ProductShare("claude_code", "Claude Code", 68.0), ProductShare("chat", "Chats", 6.0),
                  ProductShare("cowork", "Cowork", 26.0)]
    m.extra = ExtraUsage(enabled=True, monthly_limit=20.0, used=3.25, utilization=16.25)
    m.profile = ProfileInfo(plan="max", tier="default_claude_max_5x")
    return m


LOCAL = [ModelShare("Opus 5.5", 49.0, 932_000, 2_100_000, 180), ModelShare("Sonnet 5.5", 31.0, 588_000, 1_300_000, 120),
         ModelShare("Haiku 5.5", 20.0, 377_000, 900_000, 95)]


class FakeReader:
    """Just enough of UsageReader for the history window: a day of samples with 5-hour sawteeth."""

    def __init__(self, now: int):
        self.now = now
        self.rows = []
        start = now - 7 * 24 * HOUR
        t = start
        while t <= now:
            day = (t - start) / (24 * HOUR)
            # four working sessions a day (5-hour sawteeth), nights flat; the week climbs to 38 %
            hour = (t // HOUR) % 24
            cycle = ((t - start) % (5 * HOUR)) / (5 * HOUR)
            # each 5-hour window starts from zero so the history window counts it as a session
            fh = 0.0 if hour < 7 or hour > 22 or cycle < 0.02 else min(100, 4 + 70 * cycle)
            sd = min(38.0, 4 + 34 * day / 6.5)
            self.rows.append(Sample(t=t, org="", fh=fh, sd=sd, mo=sd * 1.08))
            t += 2 * 60_000

    def series(self, org=None, since_ms=None):
        return [s for s in self.rows if since_ms is None or s.t >= since_ms]

    def read(self, org=None):
        return sample_metrics(self.now)

    def organizations(self):
        return []


def grab(widget, factor: float = 2.0, window_bg: bool = True) -> QPixmap:
    """Renders the widget at `factor` x its size (crisp fonts and lines, no raster upscaling).
    window_bg=False for the frameless panel: it paints its own card and shadow, the rest stays transparent."""
    widget.setAttribute(Qt.WidgetAttribute.WA_DontShowOnScreen, True)
    widget.show()
    for _ in range(4):
        app.processEvents()
    size = widget.size()
    pm = QPixmap(int(size.width() * factor), int(size.height() * factor))
    pm.fill(Qt.GlobalColor.transparent)
    p = QPainter(pm)
    p.setRenderHint(QPainter.RenderHint.Antialiasing, True)
    p.setRenderHint(QPainter.RenderHint.TextAntialiasing, True)
    p.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)
    p.scale(factor, factor)
    flags = QWidget.RenderFlag.DrawChildren
    if window_bg:
        flags |= QWidget.RenderFlag.DrawWindowBackground
    widget.render(p, QPoint(), QRegion(), flags)
    p.end()
    return pm


def canvas() -> QPixmap:
    pm = QPixmap(W, H)
    g = QLinearGradient(0, 0, W, H)
    g.setColorAt(0.0, QColor("#232733"))
    g.setColorAt(1.0, QColor("#141720"))
    p = QPainter(pm)
    p.fillRect(pm.rect(), g)
    p.end()
    return pm


def compose(parts: list, out: str) -> None:
    """Places the grabbed windows side by side, centred in the upper two-thirds of a 1920x1080 canvas."""
    pm = canvas()
    p = QPainter(pm)
    p.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)
    gap = 60
    total = sum(x.width() for x in parts) + gap * (len(parts) - 1)
    maxh = max(x.height() for x in parts)
    scale = min(1.0, (W - 160) / total, (H - 140) / maxh)     # never upscale a raster; fit with margins
    x = (W - total * scale) / 2
    for part in parts:
        w, h = part.width() * scale, part.height() * scale
        # the subject sits in the upper part of the frame (Store overlays may cover the bottom third)
        y = 70.0 if h > H * 0.55 else max(70.0, H * 0.36 - h / 2)
        # soft shadow for opaque windows; the frameless panel has transparent margins and its own shadow
        if part.toImage().pixelColor(0, 0).alpha() == 255:
            p.fillRect(QRectF(x + 10, y + 14, w, h), QColor(0, 0, 0, 90))
        p.drawPixmap(QRectF(x, y, w, h), part, QRectF(part.rect()))
        x += w + gap * scale
    p.end()
    if not pm.save(out, "PNG"):
        raise SystemExit(f"could not write {out}")


def panel(s: FakeSettings, layout: str, theme: str, scale: float, now: int, **flags):
    from claude_usage.widget import UsageWidget

    s["layout"] = layout
    s["theme"] = theme
    s["scale"] = scale
    s["show_products"] = True
    s["show_resets"] = True
    s["show_local_models"] = True
    s["show_plan_badge"] = True
    for k, v in flags.items():
        s[k] = v
    w = UsageWidget(s)
    w.set_local_models(LOCAL)
    w.set_metrics(sample_metrics(now))
    w.apply_settings()
    pm = grab(w, window_bg=False)
    w.close()
    return pm


def shoot(code: str, out_root: str) -> list:
    from claude_usage.app import apply_language_env
    from claude_usage.history import HistoryWindow
    from claude_usage.settings_dialog import SettingsDialog

    i18n.set_language(code)
    apply_language_env(app)
    out = os.path.join(out_root, "screenshots", code)
    os.makedirs(out, exist_ok=True)
    now = int(time.time() * 1000)
    s = FakeSettings()
    s["source"] = "api"
    captions = []

    def shot(n: int, name: str, parts: list, caption: str) -> None:
        compose(parts, os.path.join(out, f"{n:02d}-{name}.png"))
        captions.append((f"{n:02d}-{name}.png", caption))

    shot(1, "panel", [panel(s, "postit", "midnight", 1.35, now)], _cap(code, 1))
    shot(2, "rings", [panel(s, "ring", "claude", 1.5, now, show_local_models=False, show_products=False)], _cap(code, 2))
    shot(3, "compact", [panel(s, "compact", "graphite", 1.5, now)], _cap(code, 3))

    hw = HistoryWindow(s, FakeReader(now))
    hw.resize(860, 520)
    hw.refresh()
    shot(4, "history", [grab(hw)], _cap(code, 4))
    hw.close()

    rows = [("resets", i18n.tr("detail.resets")), ("extra", i18n.tr("detail.extra"))]
    dlg = SettingsDialog(s, [], rows=rows)
    tabs = dlg.findChild(QTabWidget)
    if tabs:
        tabs.setCurrentIndex(2)             # Details
    dlg.resize(520, 470)
    shot(5, "settings", [grab(dlg)], _cap(code, 5))
    dlg.close()

    shot(6, "themes", [panel(s, "postit", "paper", 1.1, now, show_local_models=False),
                       panel(s, "postit", "neon", 1.1, now, show_local_models=False)], _cap(code, 6))

    with open(os.path.join(out_root, f"captions-{code}.txt"), "w", encoding="utf-8") as fh:
        for name, cap in captions:
            fh.write(f"{name}\t{cap}\n")
    print(f"{code}: {len(captions)} screenshots -> {out}")
    return captions


CAPTIONS = {
    "en": ["5-hour and weekly limits, the per-model limit, reset countdown and burn rate – at a glance, always on top",
           "Ring layout: the same three limits as compact dials",
           "Compact bar for a crowded desktop",
           "History: both limits over 6 hours, 24 hours or 7 days, with peak, average and end-of-week projection",
           "Every detail can be switched on or off – saved limit resets, usage credits, this week by product",
           "Six themes and three layouts; custom accent colour"],
    "hu": ["5 órás és heti keret, modellenkénti limit, visszaszámlálás és fogyási ütem – egy pillantásra, mindig felül",
           "Gyűrűs elrendezés: ugyanaz a három keret tömör órákként",
           "Vékony sáv zsúfolt asztalra",
           "Előzmények: mindkét keret 6 órás, 24 órás vagy 7 napos nézetben, csúccsal, átlaggal és hét végi előrejelzéssel",
           "Minden részlet ki-be kapcsolható – elmentett visszaállítás, használati kredit, e heti termékbontás",
           "Hat téma, három elrendezés, saját kiemelőszín"],
    "de": ["5-Stunden- und Wochenlimit, Limit je Modell, Countdown bis zum Reset und Verbrauchsrate – auf einen Blick, immer im Vordergrund",
           "Ring-Layout: dieselben drei Limits als kompakte Anzeigen",
           "Schmale Leiste für einen vollen Desktop",
           "Verlauf: beide Limits über 6 Stunden, 24 Stunden oder 7 Tage, mit Spitze, Durchschnitt und Wochenprognose",
           "Jedes Detail lässt sich ein- und ausschalten – gespeicherte Zurücksetzungen, Guthaben, Woche nach Produkt",
           "Sechs Designs, drei Layouts, eigene Akzentfarbe"],
}


def _cap(code: str, n: int) -> str:
    return CAPTIONS.get(code, CAPTIONS["en"])[n - 1]


def store_logos(out_root: str) -> None:
    """1:1 app tile icon (300x300) and the 16:9 super hero art (1920x1080, no text, no UI)."""
    tile = QPixmap(300, 300)
    tile.fill(Qt.GlobalColor.transparent)
    p = QPainter(tile)
    p.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)
    logo = app_pixmap(600)
    p.drawPixmap(QRectF(0, 0, 300, 300), logo, QRectF(logo.rect()))
    p.end()
    tile.save(os.path.join(out_root, "AppTileIcon-300x300.png"), "PNG")

    hero = canvas()
    p = QPainter(hero)
    p.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)
    p.setRenderHint(QPainter.RenderHint.Antialiasing, True)
    # three soft rings behind the logo - abstract, related to the app (the gauges), no text, no UI
    for r, a in ((520, 22), (400, 30), (290, 40)):
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QColor(217, 119, 87, a))
        p.drawEllipse(QPointF(W / 2, H / 2), r, r)
    logo = app_pixmap(800)
    side = 360
    p.drawPixmap(QRectF((W - side) / 2, (H - side) / 2, side, side), logo, QRectF(logo.rect()))
    p.end()
    hero.save(os.path.join(out_root, "SuperHero-1920x1080.png"), "PNG")
    print(f"logos -> {out_root}")


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    out_root = os.path.join(ROOT, "docs", "store")
    if "--out" in sys.argv:
        out_root = sys.argv[sys.argv.index("--out") + 1]
        args = [a for a in args if a != out_root]
    codes = args or ["en", "hu", "de"]
    os.makedirs(out_root, exist_ok=True)
    for code in codes:
        if code not in i18n.LANG_NAMES:
            print(f"unknown language: {code}")
            continue
        shoot(code, out_root)
    store_logos(out_root)


if __name__ == "__main__":
    main()
