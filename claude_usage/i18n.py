"""Simple, dependency-free localization.

`tr(key, *args)` returns the text in the current language (falling back to English
for a missing translation). The language is stored in settings; `set_language` switches it.

Adding a language: add the code to LANG_NAMES, and add a `"<code>": "..."` entry to
every key in STRINGS. Anything missing shows in English.
"""

from __future__ import annotations

import locale
from typing import Dict, List

# The available languages - shown in their own name.
LANG_NAMES: Dict[str, str] = {
    "en": "English",
    "hu": "Magyar",
    "de": "Deutsch",
    "fr": "Français",
    "es": "Español",
    "it": "Italiano",
    "pt": "Português",
    "pl": "Polski",
    "nl": "Nederlands",
    "ru": "Русский",
    "cs": "Čeština",
    "tr": "Türkçe",
}

DEFAULT_LANG = "en"
_current = DEFAULT_LANG


def available_languages() -> List[str]:
    return list(LANG_NAMES.keys())


def language_name(code: str) -> str:
    return LANG_NAMES.get(code, code)


def system_language() -> str:
    """Guesses a supported code from the Windows language (else English)."""
    try:
        code = (locale.getdefaultlocale()[0] or "").split("_")[0].lower()
    except Exception:  # noqa: BLE001
        code = ""
    return code if code in LANG_NAMES else DEFAULT_LANG


def set_language(code: str) -> None:
    global _current
    _current = code if code in LANG_NAMES else DEFAULT_LANG


def current_language() -> str:
    return _current


def tr(key: str, *args) -> str:
    entry = STRINGS.get(key, {})
    text = entry.get(_current) or entry.get("en") or key
    if args:
        try:
            return text.format(*args)
        except (IndexError, KeyError):
            return text
    return text


# ---------------------------------------------------------------------------
# Translations.  key -> { lang code: text }.  "en" is always required (fallback).
# The {} placeholders are filled with tr()'s arguments.
# ---------------------------------------------------------------------------

STRINGS: Dict[str, Dict[str, str]] = {
    # ---- panel ----
    "panel.five_hour": {
        "en": "5-HOUR WINDOW", "hu": "5 ÓRÁS ABLAK", "de": "5-STUNDEN-FENSTER",
        "fr": "FENÊTRE 5 HEURES", "es": "VENTANA DE 5 HORAS", "it": "FINESTRA 5 ORE",
        "pt": "JANELA DE 5 HORAS", "pl": "OKNO 5-GODZINNE", "nl": "5-UURS VENSTER",
        "ru": "ОКНО 5 ЧАСОВ", "cs": "5HODINOVÉ OKNO", "tr": "5 SAATLİK PENCERE",
    },
    "panel.weekly": {
        "en": "WEEKLY LIMIT", "hu": "HETI KERET", "de": "WOCHENLIMIT",
        "fr": "QUOTA HEBDO", "es": "LÍMITE SEMANAL", "it": "LIMITE SETTIMANALE",
        "pt": "LIMITE SEMANAL", "pl": "LIMIT TYGODNIOWY", "nl": "WEEKLIMIET",
        "ru": "НЕДЕЛЬНЫЙ ЛИМИТ", "cs": "TÝDENNÍ LIMIT", "tr": "HAFTALIK KOTA",
    },
    "panel.five_hour_short": {
        "en": "5H", "hu": "5 ÓRA", "de": "5 STD", "fr": "5 H", "es": "5 H",
        "it": "5 ORE", "pt": "5 H", "pl": "5 GODZ", "nl": "5 UUR", "ru": "5 Ч",
        "cs": "5 HOD", "tr": "5 SA",
    },
    "panel.week_short": {
        "en": "WEEK", "hu": "HÉT", "de": "WOCHE", "fr": "SEM.", "es": "SEM.",
        "it": "SETT.", "pt": "SEM.", "pl": "TYDZ.", "nl": "WEEK", "ru": "НЕД.",
        "cs": "TÝDEN", "tr": "HAFTA",
    },
    "panel.updated": {
        "en": "updated: {}", "hu": "frissítve: {}", "de": "aktualisiert: {}",
        "fr": "mis à jour : {}", "es": "actualizado: {}", "it": "aggiornato: {}",
        "pt": "atualizado: {}", "pl": "zaktualizowano: {}", "nl": "bijgewerkt: {}",
        "ru": "обновлено: {}", "cs": "aktualizováno: {}", "tr": "güncellendi: {}",
    },
    "panel.reset": {
        "en": "reset {}", "hu": "reset {}", "de": "Reset {}", "fr": "reset {}",
        "es": "reinicio {}", "it": "reset {}", "pt": "reinício {}", "pl": "reset {}",
        "nl": "reset {}", "ru": "сброс {}", "cs": "reset {}", "tr": "sıfırlama {}",
    },
    "panel.per_hour": {
        "en": "{}%/h", "hu": "{}%/óra", "de": "{}%/Std", "fr": "{} %/h",
        "es": "{}%/h", "it": "{}%/h", "pt": "{}%/h", "pl": "{}%/godz",
        "nl": "{}%/u", "ru": "{}%/ч", "cs": "{}%/h", "tr": "%{}/sa",
    },
    "panel.per_day": {
        "en": "{}%/day", "hu": "{}%/nap", "de": "{}%/Tag", "fr": "{} %/j",
        "es": "{}%/día", "it": "{}%/g", "pt": "{}%/dia", "pl": "{}%/dzień",
        "nl": "{}%/dag", "ru": "{}%/день", "cs": "{}%/den", "tr": "%{}/gün",
    },
    "panel.full_in": {
        "en": "full: {}", "hu": "tele: {}", "de": "voll: {}", "fr": "plein : {}",
        "es": "lleno: {}", "it": "pieno: {}", "pt": "cheio: {}", "pl": "pełne: {}",
        "nl": "vol: {}", "ru": "заполнится: {}", "cs": "plné: {}", "tr": "dolum: {}",
    },
    "panel.pace": {
        "en": "{} vs pace", "hu": "{} a tempóhoz", "de": "{} zum Tempo",
        "fr": "{} vs rythme", "es": "{} vs ritmo", "it": "{} vs ritmo",
        "pt": "{} vs ritmo", "pl": "{} do tempa", "nl": "{} vs tempo",
        "ru": "{} к темпу", "cs": "{} k tempu", "tr": "{} tempoya göre",
    },
    "panel.no_data": {
        "en": "No data", "hu": "Nincs adat", "de": "Keine Daten", "fr": "Aucune donnée",
        "es": "Sin datos", "it": "Nessun dato", "pt": "Sem dados", "pl": "Brak danych",
        "nl": "Geen gegevens", "ru": "Нет данных", "cs": "Žádná data", "tr": "Veri yok",
    },

    # ---- time (fmt_age / fmt_delta) ----
    "time.none": {
        "en": "no data", "hu": "nincs adat", "de": "keine Daten", "fr": "aucune donnée",
        "es": "sin datos", "it": "nessun dato", "pt": "sem dados", "pl": "brak danych",
        "nl": "geen gegevens", "ru": "нет данных", "cs": "žádná data", "tr": "veri yok",
    },
    "time.sec": {
        "en": "{} sec", "hu": "{} mp", "de": "{} Sek", "fr": "{} s", "es": "{} s",
        "it": "{} s", "pt": "{} s", "pl": "{} s", "nl": "{} sec", "ru": "{} с",
        "cs": "{} s", "tr": "{} sn",
    },
    "time.min": {
        "en": "{} min", "hu": "{} perc", "de": "{} Min", "fr": "{} min", "es": "{} min",
        "it": "{} min", "pt": "{} min", "pl": "{} min", "nl": "{} min", "ru": "{} мин",
        "cs": "{} min", "tr": "{} dk",
    },
    "time.hour": {
        "en": "{} h", "hu": "{} óra", "de": "{} Std", "fr": "{} h", "es": "{} h",
        "it": "{} h", "pt": "{} h", "pl": "{} godz", "nl": "{} uur", "ru": "{} ч",
        "cs": "{} h", "tr": "{} sa",
    },
    "time.day": {
        "en": "{} d", "hu": "{} nap", "de": "{} T", "fr": "{} j", "es": "{} d",
        "it": "{} g", "pt": "{} d", "pl": "{} dni", "nl": "{} d", "ru": "{} дн",
        "cs": "{} dní", "tr": "{} gün",
    },
    # short compound forms: "{d}{d} {h}{h}" etc.
    "time.dh": {
        "en": "{}d {}h", "hu": "{}n {}ó", "de": "{}T {}Std", "fr": "{}j {}h",
        "es": "{}d {}h", "it": "{}g {}h", "pt": "{}d {}h", "pl": "{}d {}g",
        "nl": "{}d {}u", "ru": "{}д {}ч", "cs": "{}d {}h", "tr": "{}g {}sa",
    },
    "time.hm": {
        "en": "{}h {}m", "hu": "{}ó {}p", "de": "{}Std {}Min", "fr": "{}h {}m",
        "es": "{}h {}m", "it": "{}h {}m", "pt": "{}h {}m", "pl": "{}g {}m",
        "nl": "{}u {}m", "ru": "{}ч {}м", "cs": "{}h {}m", "tr": "{}sa {}dk",
    },
    "time.m": {
        "en": "{}m", "hu": "{}p", "de": "{}Min", "fr": "{}m", "es": "{}m",
        "it": "{}m", "pt": "{}m", "pl": "{}m", "nl": "{}m", "ru": "{}м",
        "cs": "{}m", "tr": "{}dk",
    },

    # ---- menu ----
    "menu.panel_visible": {
        "en": "Show panel", "hu": "Panel látszik", "de": "Panel anzeigen",
        "fr": "Afficher le panneau", "es": "Mostrar panel", "it": "Mostra pannello",
        "pt": "Mostrar painel", "pl": "Pokaż panel", "nl": "Paneel tonen",
        "ru": "Показать панель", "cs": "Zobrazit panel", "tr": "Paneli göster",
    },
    "menu.layout": {
        "en": "Layout", "hu": "Elrendezés", "de": "Layout", "fr": "Disposition",
        "es": "Diseño", "it": "Layout", "pt": "Layout", "pl": "Układ",
        "nl": "Indeling", "ru": "Вид", "cs": "Rozvržení", "tr": "Düzen",
    },
    "layout.postit": {
        "en": "Post-it card", "hu": "Post-it kártya", "de": "Post-it-Karte",
        "fr": "Carte post-it", "es": "Tarjeta post-it", "it": "Scheda post-it",
        "pt": "Cartão post-it", "pl": "Karteczka post-it", "nl": "Post-it-kaart",
        "ru": "Карточка", "cs": "Kartička post-it", "tr": "Post-it kart",
    },
    "layout.compact": {
        "en": "Slim bar", "hu": "Vékony sáv", "de": "Schmale Leiste",
        "fr": "Barre fine", "es": "Barra fina", "it": "Barra sottile",
        "pt": "Barra fina", "pl": "Wąski pasek", "nl": "Smalle balk",
        "ru": "Тонкая полоса", "cs": "Úzký pruh", "tr": "İnce çubuk",
    },
    "layout.ring": {
        "en": "Rings", "hu": "Körgyűrűk", "de": "Ringe", "fr": "Anneaux",
        "es": "Anillos", "it": "Anelli", "pt": "Anéis", "pl": "Pierścienie",
        "nl": "Ringen", "ru": "Кольца", "cs": "Prstence", "tr": "Halkalar",
    },
    "menu.theme": {
        "en": "Theme", "hu": "Téma", "de": "Design", "fr": "Thème", "es": "Tema",
        "it": "Tema", "pt": "Tema", "pl": "Motyw", "nl": "Thema", "ru": "Тема",
        "cs": "Motiv", "tr": "Tema",
    },
    "theme.midnight": {
        "en": "Midnight glass", "hu": "Éjkék üveg", "de": "Mitternachtsglas",
        "fr": "Verre nuit", "es": "Cristal medianoche", "it": "Vetro notte",
        "pt": "Vidro meia-noite", "pl": "Nocne szkło", "nl": "Middernachtglas",
        "ru": "Ночное стекло", "cs": "Půlnoční sklo", "tr": "Gece camı",
    },
    "theme.claude": {
        "en": "Claude (warm dark)", "hu": "Claude (meleg sötét)", "de": "Claude (warm dunkel)",
        "fr": "Claude (sombre chaud)", "es": "Claude (oscuro cálido)", "it": "Claude (scuro caldo)",
        "pt": "Claude (escuro quente)", "pl": "Claude (ciepły ciemny)", "nl": "Claude (warm donker)",
        "ru": "Claude (тёплый тёмный)", "cs": "Claude (teplá tmavá)", "tr": "Claude (sıcak koyu)",
    },
    "theme.graphite": {
        "en": "Graphite", "hu": "Grafit", "de": "Graphit", "fr": "Graphite",
        "es": "Grafito", "it": "Grafite", "pt": "Grafite", "pl": "Grafit",
        "nl": "Grafiet", "ru": "Графит", "cs": "Grafit", "tr": "Grafit",
    },
    "theme.neon": {
        "en": "Neon", "hu": "Neon", "de": "Neon", "fr": "Néon", "es": "Neón",
        "it": "Neon", "pt": "Néon", "pl": "Neon", "nl": "Neon", "ru": "Неон",
        "cs": "Neon", "tr": "Neon",
    },
    "theme.paper": {
        "en": "Light paper", "hu": "Világos papír", "de": "Helles Papier",
        "fr": "Papier clair", "es": "Papel claro", "it": "Carta chiara",
        "pt": "Papel claro", "pl": "Jasny papier", "nl": "Licht papier",
        "ru": "Светлая бумага", "cs": "Světlý papír", "tr": "Açık kâğıt",
    },
    "theme.postit": {
        "en": "Post-it yellow", "hu": "Post-it sárga", "de": "Post-it-Gelb",
        "fr": "Jaune post-it", "es": "Amarillo post-it", "it": "Giallo post-it",
        "pt": "Amarelo post-it", "pl": "Żółty post-it", "nl": "Post-it-geel",
        "ru": "Жёлтый post-it", "cs": "Post-it žlutá", "tr": "Post-it sarısı",
    },
    "menu.size": {
        "en": "Size", "hu": "Méret", "de": "Größe", "fr": "Taille", "es": "Tamaño",
        "it": "Dimensione", "pt": "Tamanho", "pl": "Rozmiar", "nl": "Grootte",
        "ru": "Размер", "cs": "Velikost", "tr": "Boyut",
    },
    "size.small": {
        "en": "Small", "hu": "Kicsi", "de": "Klein", "fr": "Petit", "es": "Pequeño",
        "it": "Piccolo", "pt": "Pequeno", "pl": "Mały", "nl": "Klein", "ru": "Маленький",
        "cs": "Malý", "tr": "Küçük",
    },
    "size.normal": {
        "en": "Normal", "hu": "Normál", "de": "Normal", "fr": "Normal", "es": "Normal",
        "it": "Normale", "pt": "Normal", "pl": "Normalny", "nl": "Normaal", "ru": "Обычный",
        "cs": "Normální", "tr": "Normal",
    },
    "size.large": {
        "en": "Large", "hu": "Nagy", "de": "Groß", "fr": "Grand", "es": "Grande",
        "it": "Grande", "pt": "Grande", "pl": "Duży", "nl": "Groot", "ru": "Большой",
        "cs": "Velký", "tr": "Büyük",
    },
    "size.extra": {
        "en": "Extra", "hu": "Extra", "de": "Extra", "fr": "Extra", "es": "Extra",
        "it": "Extra", "pt": "Extra", "pl": "Ekstra", "nl": "Extra", "ru": "Огромный",
        "cs": "Extra", "tr": "Ekstra",
    },
    "menu.always_top": {
        "en": "Always on top", "hu": "Mindig felül", "de": "Immer im Vordergrund",
        "fr": "Toujours au-dessus", "es": "Siempre visible", "it": "Sempre in primo piano",
        "pt": "Sempre no topo", "pl": "Zawsze na wierzchu", "nl": "Altijd bovenop",
        "ru": "Поверх окон", "cs": "Vždy navrchu", "tr": "Her zaman üstte",
    },
    "menu.locked": {
        "en": "Lock position", "hu": "Pozíció rögzítve", "de": "Position sperren",
        "fr": "Verrouiller la position", "es": "Fijar posición", "it": "Blocca posizione",
        "pt": "Fixar posição", "pl": "Zablokuj pozycję", "nl": "Positie vergrendelen",
        "ru": "Зафиксировать", "cs": "Zamknout pozici", "tr": "Konumu kilitle",
    },
    "menu.click_through": {
        "en": "Click-through", "hu": "Kattintás-átengedés", "de": "Klick-durchlass",
        "fr": "Clic traversant", "es": "Clic transparente", "it": "Clic passante",
        "pt": "Clique passante", "pl": "Przezroczysty klik", "nl": "Klik doorlaten",
        "ru": "Прозрачно для мыши", "cs": "Průchozí klik", "tr": "Tıklama geçişi",
    },
    "menu.autostart": {
        "en": "Start with Windows", "hu": "Induljon a Windowsszal", "de": "Mit Windows starten",
        "fr": "Démarrer avec Windows", "es": "Iniciar con Windows", "it": "Avvia con Windows",
        "pt": "Iniciar com o Windows", "pl": "Uruchamiaj z Windows", "nl": "Starten met Windows",
        "ru": "Запуск с Windows", "cs": "Spouštět s Windows", "tr": "Windows ile başlat",
    },
    "menu.source": {
        "en": "Data source", "hu": "Adatforrás", "de": "Datenquelle", "fr": "Source des données",
        "es": "Origen de datos", "it": "Origine dati", "pt": "Fonte de dados",
        "pl": "Źródło danych", "nl": "Gegevensbron", "ru": "Источник данных",
        "cs": "Zdroj dat", "tr": "Veri kaynağı",
    },
    "source.local": {
        "en": "Local (this PC only)", "hu": "Helyi (csak ez a gép)", "de": "Lokal (nur dieser PC)",
        "fr": "Local (ce PC uniquement)", "es": "Local (solo este PC)", "it": "Locale (solo questo PC)",
        "pt": "Local (só este PC)", "pl": "Lokalnie (tylko ten PC)", "nl": "Lokaal (alleen deze pc)",
        "ru": "Локально (только этот ПК)", "cs": "Místní (jen tento PC)", "tr": "Yerel (yalnızca bu PC)",
    },
    "source.api": {
        "en": "claude.ai (all devices)", "hu": "claude.ai (minden eszköz)", "de": "claude.ai (alle Geräte)",
        "fr": "claude.ai (tous appareils)", "es": "claude.ai (todos los dispositivos)",
        "it": "claude.ai (tutti i dispositivi)", "pt": "claude.ai (todos os dispositivos)",
        "pl": "claude.ai (wszystkie urządzenia)", "nl": "claude.ai (alle apparaten)",
        "ru": "claude.ai (все устройства)", "cs": "claude.ai (všechna zařízení)",
        "tr": "claude.ai (tüm cihazlar)",
    },
    "menu.logout": {
        "en": "Sign out", "hu": "Kijelentkezés", "de": "Abmelden", "fr": "Se déconnecter",
        "es": "Cerrar sesión", "it": "Esci", "pt": "Sair", "pl": "Wyloguj",
        "nl": "Afmelden", "ru": "Выйти", "cs": "Odhlásit", "tr": "Çıkış yap",
    },
    "menu.login": {
        "en": "Sign in (claude.ai, browser)…", "hu": "Bejelentkezés (claude.ai, böngésző)…",
        "de": "Anmelden (claude.ai, Browser)…", "fr": "Se connecter (claude.ai, navigateur)…",
        "es": "Iniciar sesión (claude.ai, navegador)…", "it": "Accedi (claude.ai, browser)…",
        "pt": "Entrar (claude.ai, navegador)…", "pl": "Zaloguj (claude.ai, przeglądarka)…",
        "nl": "Aanmelden (claude.ai, browser)…", "ru": "Войти (claude.ai, браузер)…",
        "cs": "Přihlásit (claude.ai, prohlížeč)…", "tr": "Giriş yap (claude.ai, tarayıcı)…",
    },
    "menu.history": {
        "en": "History & stats…", "hu": "Előzmények és statisztika…", "de": "Verlauf & Statistik…",
        "fr": "Historique et stats…", "es": "Historial y estadísticas…", "it": "Cronologia e statistiche…",
        "pt": "Histórico e estatísticas…", "pl": "Historia i statystyki…", "nl": "Geschiedenis & stats…",
        "ru": "История и статистика…", "cs": "Historie a statistiky…", "tr": "Geçmiş ve istatistik…",
    },
    "menu.settings": {
        "en": "Settings…", "hu": "Beállítások…", "de": "Einstellungen…", "fr": "Paramètres…",
        "es": "Ajustes…", "it": "Impostazioni…", "pt": "Configurações…", "pl": "Ustawienia…",
        "nl": "Instellingen…", "ru": "Настройки…", "cs": "Nastavení…", "tr": "Ayarlar…",
    },
    "menu.refresh": {
        "en": "Refresh now", "hu": "Frissítés most", "de": "Jetzt aktualisieren",
        "fr": "Actualiser", "es": "Actualizar ahora", "it": "Aggiorna ora",
        "pt": "Atualizar agora", "pl": "Odśwież teraz", "nl": "Nu vernieuwen",
        "ru": "Обновить сейчас", "cs": "Obnovit nyní", "tr": "Şimdi yenile",
    },
    "menu.quit": {
        "en": "Quit", "hu": "Kilépés", "de": "Beenden", "fr": "Quitter", "es": "Salir",
        "it": "Esci", "pt": "Sair", "pl": "Zakończ", "nl": "Afsluiten", "ru": "Выход",
        "cs": "Ukončit", "tr": "Çıkış",
    },
    "menu.start_menu": {
        "en": "Show in Start menu", "hu": "Start menüben megjelenítés", "de": "Im Startmenü anzeigen",
        "fr": "Afficher dans le menu Démarrer", "es": "Mostrar en el menú Inicio",
        "it": "Mostra nel menu Start", "pt": "Mostrar no menu Iniciar",
        "pl": "Pokaż w menu Start", "nl": "In Startmenu tonen",
        "ru": "Показывать в меню «Пуск»", "cs": "Zobrazit v nabídce Start",
        "tr": "Başlat menüsünde göster",
    },
    "menu.language": {
        "en": "Language", "hu": "Nyelv", "de": "Sprache", "fr": "Langue", "es": "Idioma",
        "it": "Lingua", "pt": "Idioma", "pl": "Język", "nl": "Taal", "ru": "Язык",
        "cs": "Jazyk", "tr": "Dil",
    },

    # ---- tray / notifications ----
    "tray.head": {
        "en": "5h: {}%   ·   Week: {}%", "hu": "5 óra: {}%   ·   Hét: {}%",
        "de": "5 Std: {}%   ·   Woche: {}%", "fr": "5 h : {} %   ·   Sem. : {} %",
        "es": "5 h: {}%   ·   Sem.: {}%", "it": "5h: {}%   ·   Sett.: {}%",
        "pt": "5h: {}%   ·   Sem.: {}%", "pl": "5 godz: {}%   ·   Tydz.: {}%",
        "nl": "5u: {}%   ·   Week: {}%", "ru": "5ч: {}%   ·   Нед.: {}%",
        "cs": "5h: {}%   ·   Týden: {}%", "tr": "5sa: %{}   ·   Hafta: %{}",
    },
    "tray.line": {
        "en": "{}: {}%", "hu": "{}: {}%", "de": "{}: {}%", "fr": "{} : {} %",
        "es": "{}: {}%", "it": "{}: {}%", "pt": "{}: {}%", "pl": "{}: {}%",
        "nl": "{}: {}%", "ru": "{}: {}%", "cs": "{}: {}%", "tr": "{}: %{}",
    },
    "notify.threshold": {
        "en": "{}: {}% used.", "hu": "{}: {}% elfogyott.", "de": "{}: {}% verbraucht.",
        "fr": "{} : {} % utilisés.", "es": "{}: {}% usado.", "it": "{}: {}% usato.",
        "pt": "{}: {}% usado.", "pl": "{}: zużyto {}%.", "nl": "{}: {}% gebruikt.",
        "ru": "{}: использовано {}%.", "cs": "{}: využito {}%.", "tr": "{}: %{} kullanıldı.",
    },
    "notify.reset_done": {
        "en": "{}: reset — a new window has started.", "hu": "{}: lenullázódott — új keret indult.",
        "de": "{}: zurückgesetzt — neues Fenster gestartet.", "fr": "{} : réinitialisé — nouvelle fenêtre.",
        "es": "{}: reiniciado — nueva ventana.", "it": "{}: azzerato — nuova finestra.",
        "pt": "{}: reiniciado — nova janela.", "pl": "{}: wyzerowano — nowe okno.",
        "nl": "{}: gereset — nieuw venster gestart.", "ru": "{}: сброшено — новое окно.",
        "cs": "{}: vynulováno — nové okno.", "tr": "{}: sıfırlandı — yeni pencere başladı.",
    },
    "notify.stale_title": {
        "en": "Stale data", "hu": "Elavult adat", "de": "Veraltete Daten", "fr": "Données périmées",
        "es": "Datos obsoletos", "it": "Dati obsoleti", "pt": "Dados desatualizados",
        "pl": "Nieaktualne dane", "nl": "Verouderde gegevens", "ru": "Устаревшие данные",
        "cs": "Zastaralá data", "tr": "Eski veri",
    },
    "notify.stale_body": {
        "en": "Last reading is {} old. Is Claude Desktop running?",
        "hu": "Az utolsó mérés {} régi. Fut a Claude Desktop?",
        "de": "Letzte Messung ist {} alt. Läuft Claude Desktop?",
        "fr": "Dernière mesure il y a {}. Claude Desktop est-il lancé ?",
        "es": "La última lectura tiene {}. ¿Claude Desktop está abierto?",
        "it": "Ultima lettura di {} fa. Claude Desktop è in esecuzione?",
        "pt": "Última leitura há {}. O Claude Desktop está aberto?",
        "pl": "Ostatni odczyt sprzed {}. Czy Claude Desktop działa?",
        "nl": "Laatste meting is {} oud. Draait Claude Desktop?",
        "ru": "Последнее измерение {} назад. Claude Desktop запущен?",
        "cs": "Poslední měření před {}. Běží Claude Desktop?",
        "tr": "Son ölçüm {} önce. Claude Desktop çalışıyor mu?",
    },
    "notify.login_ok": {
        "en": "Signed in – server data incoming.", "hu": "Sikeres bejelentkezés – a szerveradatok érkeznek.",
        "de": "Angemeldet – Serverdaten kommen.", "fr": "Connecté – données du serveur en cours.",
        "es": "Sesión iniciada – llegan los datos del servidor.", "it": "Accesso riuscito – dati dal server in arrivo.",
        "pt": "Conectado – dados do servidor a chegar.", "pl": "Zalogowano – dane z serwera nadchodzą.",
        "nl": "Aangemeld – servergegevens onderweg.", "ru": "Вход выполнен – данные с сервера загружаются.",
        "cs": "Přihlášeno – data ze serveru přicházejí.", "tr": "Giriş yapıldı – sunucu verileri geliyor.",
    },
    "notify.logout": {
        "en": "Signed out. Switched to local source.", "hu": "Kijelentkeztél. A panel a helyi forrásra váltott.",
        "de": "Abgemeldet. Auf lokale Quelle umgestellt.", "fr": "Déconnecté. Passage à la source locale.",
        "es": "Sesión cerrada. Cambiado a origen local.", "it": "Disconnesso. Passato all'origine locale.",
        "pt": "Sessão terminada. Mudou para fonte local.", "pl": "Wylogowano. Przełączono na źródło lokalne.",
        "nl": "Afgemeld. Overgeschakeld naar lokale bron.", "ru": "Выход выполнен. Переключено на локальный источник.",
        "cs": "Odhlášeno. Přepnuto na místní zdroj.", "tr": "Çıkış yapıldı. Yerel kaynağa geçildi.",
    },
    "notify.first_run": {
        "en": "The panel appeared in the top-right corner.\nRight-click the panel or the tray icon = menu.",
        "hu": "A panel a képernyő jobb felső sarkában jelent meg.\nJobb gomb a panelen vagy a tálcaikonon = menü.",
        "de": "Das Panel erscheint oben rechts.\nRechtsklick auf Panel oder Tray-Symbol = Menü.",
        "fr": "Le panneau est apparu en haut à droite.\nClic droit sur le panneau ou l'icône = menu.",
        "es": "El panel apareció arriba a la derecha.\nClic derecho en el panel o el icono = menú.",
        "it": "Il pannello è in alto a destra.\nClic destro sul pannello o sull'icona = menu.",
        "pt": "O painel apareceu no canto superior direito.\nClique direito no painel ou ícone = menu.",
        "pl": "Panel pojawił się w prawym górnym rogu.\nPrawy przycisk na panelu lub ikonie = menu.",
        "nl": "Het paneel staat rechtsboven.\nRechtsklik op paneel of pictogram = menu.",
        "ru": "Панель появилась в правом верхнем углу.\nПравый клик по панели или значку = меню.",
        "cs": "Panel se objevil vpravo nahoře.\nPravý klik na panel nebo ikonu = menu.",
        "tr": "Panel sağ üst köşede belirdi.\nPanele veya simgeye sağ tık = menü.",
    },
    "notify.autostart_on": {
        "en": "Enabled: the app starts with Windows.", "hu": "Bekapcsolva: a program elindul a Windowsszal.",
        "de": "Aktiviert: Die App startet mit Windows.", "fr": "Activé : l'appli démarre avec Windows.",
        "es": "Activado: la app se inicia con Windows.", "it": "Attivato: l'app si avvia con Windows.",
        "pt": "Ativado: o app inicia com o Windows.", "pl": "Włączono: aplikacja startuje z Windows.",
        "nl": "Ingeschakeld: de app start met Windows.", "ru": "Включено: запуск вместе с Windows.",
        "cs": "Zapnuto: aplikace se spustí s Windows.", "tr": "Açık: uygulama Windows ile başlar.",
    },
    "notify.autostart_off": {
        "en": "Disabled: the app won't start with Windows.", "hu": "Kikapcsolva: a program nem indul a Windowsszal.",
        "de": "Deaktiviert: Kein Start mit Windows.", "fr": "Désactivé : pas de démarrage avec Windows.",
        "es": "Desactivado: no se inicia con Windows.", "it": "Disattivato: non si avvia con Windows.",
        "pt": "Desativado: não inicia com o Windows.", "pl": "Wyłączono: brak startu z Windows.",
        "nl": "Uitgeschakeld: start niet met Windows.", "ru": "Выключено: без запуска с Windows.",
        "cs": "Vypnuto: nespustí se s Windows.", "tr": "Kapalı: Windows ile başlamaz.",
    },
    "notify.autostart_fail": {
        "en": "Could not set up automatic start.", "hu": "Az automatikus indítást nem sikerült beállítani.",
        "de": "Autostart konnte nicht eingerichtet werden.", "fr": "Impossible de configurer le démarrage auto.",
        "es": "No se pudo configurar el inicio automático.", "it": "Impossibile impostare l'avvio automatico.",
        "pt": "Não foi possível configurar o início automático.", "pl": "Nie udało się ustawić autostartu.",
        "nl": "Kon automatisch starten niet instellen.", "ru": "Не удалось настроить автозапуск.",
        "cs": "Nepodařilo se nastavit automatické spuštění.", "tr": "Otomatik başlatma ayarlanamadı.",
    },
    "err.no_tray": {
        "en": "System tray not available; the tray icon is skipped.",
        "hu": "A rendszertálca nem érhető el, a tálcaikon kimarad.",
        "de": "Kein System-Tray verfügbar; Tray-Symbol entfällt.",
        "fr": "Barre d'état non disponible ; icône ignorée.",
        "es": "Bandeja no disponible; se omite el icono.",
        "it": "Area di notifica non disponibile; icona omessa.",
        "pt": "Bandeja indisponível; ícone ignorado.",
        "pl": "Zasobnik niedostępny; pomijam ikonę.",
        "nl": "Systeemvak niet beschikbaar; pictogram overgeslagen.",
        "ru": "Системный лоток недоступен; значок пропущен.",
        "cs": "Systémová lišta není dostupná; ikona vynechána.",
        "tr": "Sistem tepsisi yok; simge atlandı.",
    },
    "err.already_running": {
        "en": "The app is already running (check the tray).", "hu": "A program már fut (nézd meg a tálcán).",
        "de": "Die App läuft bereits (siehe Tray).", "fr": "L'appli est déjà lancée (voir la barre).",
        "es": "La app ya está en ejecución (mira la bandeja).", "it": "L'app è già in esecuzione (guarda il tray).",
        "pt": "O app já está em execução (veja a bandeja).", "pl": "Aplikacja już działa (sprawdź zasobnik).",
        "nl": "De app draait al (kijk in het systeemvak).", "ru": "Приложение уже запущено (см. лоток).",
        "cs": "Aplikace už běží (viz lišta).", "tr": "Uygulama zaten çalışıyor (tepsiye bakın).",
    },

    # ===================== sign-in window (authdialog) =====================
    "dlg.login_title": {
        "en": "sign in", "hu": "bejelentkezés", "de": "Anmeldung", "fr": "connexion",
        "es": "iniciar sesión", "it": "accesso", "pt": "entrar", "pl": "logowanie",
        "nl": "aanmelden", "ru": "вход", "cs": "přihlášení", "tr": "giriş",
    },
    "dlg.intro": {
        "en": "Sign in to your claude.ai account in your own browser (your saved passwords and passkeys already work there).",
        "hu": "Bejelentkezés a claude.ai-fiókodba a saját böngésződben (ott a jelszavaid és passkey-d már működnek).",
        "de": "Melde dich in deinem Browser bei claude.ai an (deine gespeicherten Passwörter und Passkeys funktionieren dort bereits).",
        "fr": "Connecte-toi à ton compte claude.ai dans ton navigateur (tes mots de passe et passkeys enregistrés y fonctionnent déjà).",
        "es": "Inicia sesión en tu cuenta de claude.ai en tu navegador (tus contraseñas y passkeys guardados ya funcionan ahí).",
        "it": "Accedi al tuo account claude.ai nel tuo browser (le password e le passkey salvate funzionano già lì).",
        "pt": "Entra na tua conta claude.ai no teu navegador (as tuas palavras-passe e passkeys guardadas já funcionam aí).",
        "pl": "Zaloguj się do konta claude.ai w swojej przeglądarce (zapisane hasła i passkeye już tam działają).",
        "nl": "Meld je aan bij je claude.ai-account in je eigen browser (je opgeslagen wachtwoorden en passkeys werken daar al).",
        "ru": "Войдите в свою учётную запись claude.ai в своём браузере (сохранённые пароли и passkey там уже работают).",
        "cs": "Přihlaste se ke svému účtu claude.ai ve svém prohlížeči (uložená hesla a passkeye tam už fungují).",
        "tr": "claude.ai hesabına kendi tarayıcında giriş yap (kayıtlı şifrelerin ve passkey'lerin orada zaten çalışır).",
    },
    "dlg.step1": {
        "en": "Step 1", "hu": "1. lépés", "de": "Schritt 1", "fr": "Étape 1", "es": "Paso 1",
        "it": "Passo 1", "pt": "Passo 1", "pl": "Krok 1", "nl": "Stap 1", "ru": "Шаг 1",
        "cs": "Krok 1", "tr": "1. adım",
    },
    "dlg.open_browser": {
        "en": "Open sign-in in your browser", "hu": "Bejelentkezés megnyitása a böngészőben",
        "de": "Anmeldung im Browser öffnen", "fr": "Ouvrir la connexion dans le navigateur",
        "es": "Abrir el inicio de sesión en el navegador", "it": "Apri l'accesso nel browser",
        "pt": "Abrir o início de sessão no navegador", "pl": "Otwórz logowanie w przeglądarce",
        "nl": "Aanmelden openen in browser", "ru": "Открыть вход в браузере",
        "cs": "Otevřít přihlášení v prohlížeči", "tr": "Girişi tarayıcıda aç",
    },
    "dlg.hint1": {
        "en": "Sign in on the page that opens and approve access. You'll get a code at the end.",
        "hu": "A megnyíló oldalon lépj be és engedélyezd a hozzáférést. A végén kapsz egy kódot.",
        "de": "Melde dich auf der geöffneten Seite an und erlaube den Zugriff. Am Ende erhältst du einen Code.",
        "fr": "Connecte-toi sur la page qui s'ouvre et autorise l'accès. Tu obtiens un code à la fin.",
        "es": "Inicia sesión en la página que se abre y aprueba el acceso. Al final obtendrás un código.",
        "it": "Accedi nella pagina che si apre e autorizza l'accesso. Alla fine ricevi un codice.",
        "pt": "Inicia sessão na página que abre e aprova o acesso. No fim recebes um código.",
        "pl": "Zaloguj się na otwartej stronie i zatwierdź dostęp. Na końcu otrzymasz kod.",
        "nl": "Meld je aan op de geopende pagina en keur toegang goed. Aan het eind krijg je een code.",
        "ru": "Войдите на открывшейся странице и разрешите доступ. В конце вы получите код.",
        "cs": "Přihlaste se na otevřené stránce a povolte přístup. Na konci dostanete kód.",
        "tr": "Açılan sayfada giriş yap ve erişimi onayla. Sonunda bir kod alırsın.",
    },
    "dlg.step2": {
        "en": "Step 2", "hu": "2. lépés", "de": "Schritt 2", "fr": "Étape 2", "es": "Paso 2",
        "it": "Passo 2", "pt": "Passo 2", "pl": "Krok 2", "nl": "Stap 2", "ru": "Шаг 2",
        "cs": "Krok 2", "tr": "2. adım",
    },
    "dlg.paste_label": {
        "en": "Paste the code you received here:", "hu": "Másold be ide a kapott kódot:",
        "de": "Füge den erhaltenen Code hier ein:", "fr": "Colle ici le code reçu :",
        "es": "Pega aquí el código recibido:", "it": "Incolla qui il codice ricevuto:",
        "pt": "Cola aqui o código recebido:", "pl": "Wklej tutaj otrzymany kod:",
        "nl": "Plak de ontvangen code hier:", "ru": "Вставьте полученный код сюда:",
        "cs": "Vložte sem obdržený kód:", "tr": "Aldığın kodu buraya yapıştır:",
    },
    "dlg.paste_placeholder": {
        "en": "paste code here", "hu": "kód beillesztése ide", "de": "Code hier einfügen",
        "fr": "coller le code ici", "es": "pega el código aquí", "it": "incolla il codice qui",
        "pt": "cola o código aqui", "pl": "wklej kod tutaj", "nl": "plak code hier",
        "ru": "вставьте код сюда", "cs": "vložte kód sem", "tr": "kodu buraya yapıştır",
    },
    "dlg.signin": {
        "en": "Sign in", "hu": "Bejelentkezés", "de": "Anmelden", "fr": "Se connecter",
        "es": "Iniciar sesión", "it": "Accedi", "pt": "Entrar", "pl": "Zaloguj",
        "nl": "Aanmelden", "ru": "Войти", "cs": "Přihlásit", "tr": "Giriş yap",
    },
    "dlg.cancel": {
        "en": "Cancel", "hu": "Mégse", "de": "Abbrechen", "fr": "Annuler", "es": "Cancelar",
        "it": "Annulla", "pt": "Cancelar", "pl": "Anuluj", "nl": "Annuleren", "ru": "Отмена",
        "cs": "Zrušit", "tr": "İptal",
    },
    "dlg.checking": {
        "en": "Checking…", "hu": "Ellenőrzés…", "de": "Prüfen…", "fr": "Vérification…",
        "es": "Comprobando…", "it": "Verifica…", "pt": "A verificar…", "pl": "Sprawdzanie…",
        "nl": "Controleren…", "ru": "Проверка…", "cs": "Ověřování…", "tr": "Kontrol ediliyor…",
    },
    "dlg.err_ratelimit": {
        "en": "Too many sign-in attempts in a short time.\n\nThe server is limiting you temporarily. Close this window, wait 10–15 minutes (don't try in the meantime), then start ONE new browser sign-in with a fresh code.",
        "hu": "Túl sok bejelentkezési próbálkozás rövid idő alatt.\n\nA szerver átmenetileg korlátoz. Zárd be ezt az ablakot, várj 10–15 percet (ne próbálkozz közben), majd indíts EGYETLEN új böngészős bejelentkezést friss kóddal.",
        "de": "Zu viele Anmeldeversuche in kurzer Zeit.\n\nDer Server begrenzt dich vorübergehend. Schließe dieses Fenster, warte 10–15 Minuten (versuche es zwischendurch nicht), und starte dann EINE neue Browser-Anmeldung mit einem frischen Code.",
        "fr": "Trop de tentatives de connexion en peu de temps.\n\nLe serveur te limite temporairement. Ferme cette fenêtre, attends 10–15 minutes (n'essaie pas entre-temps), puis lance UNE seule nouvelle connexion navigateur avec un code frais.",
        "es": "Demasiados intentos de inicio de sesión en poco tiempo.\n\nEl servidor te limita temporalmente. Cierra esta ventana, espera 10–15 minutos (no lo intentes mientras), y luego inicia UN solo nuevo inicio de sesión con un código nuevo.",
        "it": "Troppi tentativi di accesso in poco tempo.\n\nIl server ti limita temporaneamente. Chiudi questa finestra, attendi 10–15 minuti (non riprovare nel frattempo), poi avvia UN solo nuovo accesso dal browser con un codice nuovo.",
        "pt": "Demasiadas tentativas de início de sessão em pouco tempo.\n\nO servidor limita-te temporariamente. Fecha esta janela, espera 10–15 minutos (não tentes entretanto) e inicia UM único novo início de sessão no navegador com um código novo.",
        "pl": "Zbyt wiele prób logowania w krótkim czasie.\n\nSerwer tymczasowo Cię ogranicza. Zamknij to okno, odczekaj 10–15 minut (nie próbuj w tym czasie), a potem uruchom JEDNO nowe logowanie w przeglądarce ze świeżym kodem.",
        "nl": "Te veel aanmeldpogingen in korte tijd.\n\nDe server beperkt je tijdelijk. Sluit dit venster, wacht 10–15 minuten (probeer ondertussen niet), en start dan ÉÉN nieuwe browser-aanmelding met een verse code.",
        "ru": "Слишком много попыток входа за короткое время.\n\nСервер временно ограничивает вас. Закройте это окно, подождите 10–15 минут (не пытайтесь в это время), затем выполните ОДИН новый вход через браузер со свежим кодом.",
        "cs": "Příliš mnoho pokusů o přihlášení v krátké době.\n\nServer vás dočasně omezuje. Zavřete toto okno, počkejte 10–15 minut (mezitím to nezkoušejte) a pak spusťte JEDNO nové přihlášení v prohlížeči s čerstvým kódem.",
        "tr": "Kısa sürede çok fazla giriş denemesi.\n\nSunucu geçici olarak sınırlıyor. Bu pencereyi kapat, 10–15 dakika bekle (bu sırada deneme), sonra taze bir kodla TEK bir yeni tarayıcı girişi başlat.",
    },
    "dlg.err_badcode": {
        "en": "The code was not accepted.\n\n{}\n\nCheck that you pasted the whole code, or try the browser sign-in again (always a fresh code).",
        "hu": "A kód nem fogadható el.\n\n{}\n\nEllenőrizd, hogy a teljes kódot másoltad-e be, vagy próbáld újra a böngészős bejelentkezést (mindig friss kód kell).",
        "de": "Der Code wurde nicht akzeptiert.\n\n{}\n\nPrüfe, ob du den ganzen Code eingefügt hast, oder versuche die Browser-Anmeldung erneut (immer ein frischer Code).",
        "fr": "Le code n'a pas été accepté.\n\n{}\n\nVérifie que tu as collé le code entier, ou relance la connexion navigateur (toujours un code frais).",
        "es": "El código no fue aceptado.\n\n{}\n\nComprueba que pegaste el código completo, o vuelve a intentar el inicio de sesión (siempre un código nuevo).",
        "it": "Il codice non è stato accettato.\n\n{}\n\nVerifica di aver incollato tutto il codice, oppure riprova l'accesso dal browser (sempre un codice nuovo).",
        "pt": "O código não foi aceite.\n\n{}\n\nVerifica se colaste o código completo, ou tenta o início de sessão de novo (sempre um código novo).",
        "pl": "Kod nie został zaakceptowany.\n\n{}\n\nSprawdź, czy wkleiłeś cały kod, lub spróbuj logowania w przeglądarce ponownie (zawsze świeży kod).",
        "nl": "De code werd niet geaccepteerd.\n\n{}\n\nControleer of je de hele code hebt geplakt, of probeer de browser-aanmelding opnieuw (altijd een verse code).",
        "ru": "Код не принят.\n\n{}\n\nПроверьте, что вставили код целиком, или повторите вход через браузер (всегда свежий код).",
        "cs": "Kód nebyl přijat.\n\n{}\n\nZkontrolujte, zda jste vložili celý kód, nebo zkuste přihlášení v prohlížeči znovu (vždy čerstvý kód).",
        "tr": "Kod kabul edilmedi.\n\n{}\n\nKodun tamamını yapıştırdığından emin ol ya da tarayıcı girişini tekrar dene (her zaman taze kod).",
    },
    "dlg.unknown_err": {
        "en": "Unknown error.", "hu": "Ismeretlen hiba.", "de": "Unbekannter Fehler.",
        "fr": "Erreur inconnue.", "es": "Error desconocido.", "it": "Errore sconosciuto.",
        "pt": "Erro desconhecido.", "pl": "Nieznany błąd.", "nl": "Onbekende fout.",
        "ru": "Неизвестная ошибка.", "cs": "Neznámá chyba.", "tr": "Bilinmeyen hata.",
    },

    # ===================== settings window (settings_dialog) =====================
    "set.title": {
        "en": "settings", "hu": "beállítások", "de": "Einstellungen", "fr": "paramètres",
        "es": "ajustes", "it": "impostazioni", "pt": "configurações", "pl": "ustawienia",
        "nl": "instellingen", "ru": "настройки", "cs": "nastavení", "tr": "ayarlar",
    },
    "set.tab_appearance": {
        "en": "Appearance", "hu": "Megjelenés", "de": "Darstellung", "fr": "Apparence",
        "es": "Apariencia", "it": "Aspetto", "pt": "Aparência", "pl": "Wygląd",
        "nl": "Weergave", "ru": "Вид", "cs": "Vzhled", "tr": "Görünüm",
    },
    "set.tab_content": {
        "en": "Content", "hu": "Tartalom", "de": "Inhalt", "fr": "Contenu", "es": "Contenido",
        "it": "Contenuto", "pt": "Conteúdo", "pl": "Zawartość", "nl": "Inhoud", "ru": "Содержимое",
        "cs": "Obsah", "tr": "İçerik",
    },
    "set.tab_alerts": {
        "en": "Alerts", "hu": "Riasztások", "de": "Warnungen", "fr": "Alertes", "es": "Alertas",
        "it": "Avvisi", "pt": "Alertas", "pl": "Alerty", "nl": "Waarschuwingen", "ru": "Оповещения",
        "cs": "Upozornění", "tr": "Uyarılar",
    },
    "set.tab_data": {
        "en": "Data source", "hu": "Adatforrás", "de": "Datenquelle", "fr": "Source des données",
        "es": "Origen de datos", "it": "Origine dati", "pt": "Fonte de dados", "pl": "Źródło danych",
        "nl": "Gegevensbron", "ru": "Источник данных", "cs": "Zdroj dat", "tr": "Veri kaynağı",
    },
    "set.tab_system": {
        "en": "System", "hu": "Rendszer", "de": "System", "fr": "Système", "es": "Sistema",
        "it": "Sistema", "pt": "Sistema", "pl": "System", "nl": "Systeem", "ru": "Система",
        "cs": "Systém", "tr": "Sistem",
    },
    "set.close": {
        "en": "Close", "hu": "Bezárás", "de": "Schließen", "fr": "Fermer", "es": "Cerrar",
        "it": "Chiudi", "pt": "Fechar", "pl": "Zamknij", "nl": "Sluiten", "ru": "Закрыть",
        "cs": "Zavřít", "tr": "Kapat",
    },
    "set.theme": {
        "en": "Theme", "hu": "Téma", "de": "Design", "fr": "Thème", "es": "Tema", "it": "Tema",
        "pt": "Tema", "pl": "Motyw", "nl": "Thema", "ru": "Тема", "cs": "Motiv", "tr": "Tema",
    },
    "set.accent": {
        "en": "Accent color", "hu": "Kiemelőszín", "de": "Akzentfarbe", "fr": "Couleur d'accent",
        "es": "Color de acento", "it": "Colore d'accento", "pt": "Cor de destaque",
        "pl": "Kolor akcentu", "nl": "Accentkleur", "ru": "Акцентный цвет", "cs": "Barva akcentu",
        "tr": "Vurgu rengi",
    },
    "set.pick_color": {
        "en": "Choose color…", "hu": "Szín választása…", "de": "Farbe wählen…",
        "fr": "Choisir une couleur…", "es": "Elegir color…", "it": "Scegli colore…",
        "pt": "Escolher cor…", "pl": "Wybierz kolor…", "nl": "Kies kleur…",
        "ru": "Выбрать цвет…", "cs": "Vybrat barvu…", "tr": "Renk seç…",
    },
    "set.default": {
        "en": "Default", "hu": "Alap", "de": "Standard", "fr": "Défaut", "es": "Predet.",
        "it": "Predef.", "pt": "Padrão", "pl": "Domyślny", "nl": "Standaard", "ru": "Сброс",
        "cs": "Výchozí", "tr": "Varsayılan",
    },
    "set.theme_default": {
        "en": "Theme default", "hu": "Téma szerinti", "de": "Design-Standard",
        "fr": "Selon le thème", "es": "Según el tema", "it": "Come da tema",
        "pt": "Conforme o tema", "pl": "Wg motywu", "nl": "Themastandaard",
        "ru": "По теме", "cs": "Dle motivu", "tr": "Temaya göre",
    },
    "set.layout": {
        "en": "Layout", "hu": "Elrendezés", "de": "Layout", "fr": "Disposition", "es": "Diseño",
        "it": "Layout", "pt": "Layout", "pl": "Układ", "nl": "Indeling", "ru": "Вид",
        "cs": "Rozvržení", "tr": "Düzen",
    },
    "set.size": {
        "en": "Size", "hu": "Méret", "de": "Größe", "fr": "Taille", "es": "Tamaño",
        "it": "Dimensione", "pt": "Tamanho", "pl": "Rozmiar", "nl": "Grootte", "ru": "Размер",
        "cs": "Velikost", "tr": "Boyut",
    },
    "set.opacity": {
        "en": "Opacity", "hu": "Átlátszatlanság", "de": "Deckkraft", "fr": "Opacité",
        "es": "Opacidad", "it": "Opacità", "pt": "Opacidade", "pl": "Krycie",
        "nl": "Dekking", "ru": "Непрозрачность", "cs": "Krytí", "tr": "Saydamsızlık",
    },
    "set.visible": {
        "en": "Floating panel visible", "hu": "Lebegő panel látszik", "de": "Schwebendes Panel sichtbar",
        "fr": "Panneau flottant visible", "es": "Panel flotante visible", "it": "Pannello flottante visibile",
        "pt": "Painel flutuante visível", "pl": "Widoczny panel pływający", "nl": "Zwevend paneel zichtbaar",
        "ru": "Плавающая панель видна", "cs": "Plovoucí panel viditelný", "tr": "Yüzen panel görünür",
    },
    "set.always_top": {
        "en": "Above all other windows", "hu": "Mindig a többi ablak felett", "de": "Über allen anderen Fenstern",
        "fr": "Au-dessus des autres fenêtres", "es": "Sobre las demás ventanas", "it": "Sopra le altre finestre",
        "pt": "Acima das outras janelas", "pl": "Nad innymi oknami", "nl": "Boven alle andere vensters",
        "ru": "Поверх всех окон", "cs": "Nad všemi okny", "tr": "Diğer pencerelerin üstünde",
    },
    "set.lock": {
        "en": "Lock position (not draggable)", "hu": "Pozíció rögzítése (nem húzható)",
        "de": "Position sperren (nicht ziehbar)", "fr": "Verrouiller la position (non déplaçable)",
        "es": "Fijar posición (no arrastrable)", "it": "Blocca posizione (non trascinabile)",
        "pt": "Fixar posição (não arrastável)", "pl": "Zablokuj pozycję (bez przeciągania)",
        "nl": "Positie vergrendelen (niet sleepbaar)", "ru": "Зафиксировать (без перетаскивания)",
        "cs": "Zamknout pozici (nelze táhnout)", "tr": "Konumu kilitle (sürüklenemez)",
    },
    "set.snap": {
        "en": "Snap to screen edge", "hu": "Tapadás a képernyő széléhez", "de": "An Bildschirmrand einrasten",
        "fr": "Aligner sur le bord de l'écran", "es": "Ajustar al borde de la pantalla", "it": "Aggancia al bordo dello schermo",
        "pt": "Encaixar na borda do ecrã", "pl": "Przyciągaj do krawędzi ekranu", "nl": "Aan schermrand vastklikken",
        "ru": "Прилипать к краю экрана", "cs": "Přichytit k okraji obrazovky", "tr": "Ekran kenarına yapış",
    },
    "set.taskbar": {
        "en": "Show on the taskbar (as a window)", "hu": "Megjelenés a tálcán (ablakként)",
        "de": "In der Taskleiste anzeigen (als Fenster)", "fr": "Afficher dans la barre des tâches (comme fenêtre)",
        "es": "Mostrar en la barra de tareas (como ventana)", "it": "Mostra nella barra delle applicazioni (come finestra)",
        "pt": "Mostrar na barra de tarefas (como janela)", "pl": "Pokaż na pasku zadań (jako okno)",
        "nl": "Toon op de taakbalk (als venster)", "ru": "Показывать на панели задач (как окно)",
        "cs": "Zobrazit na hlavním panelu (jako okno)", "tr": "Görev çubuğunda göster (pencere olarak)",
    },
    "set.click_through": {
        "en": "Click-through (decoration only, ignores mouse)", "hu": "Kattintás-átengedés (csak dísz, nem fogad egeret)",
        "de": "Klick-durchlass (nur Deko, ignoriert Maus)", "fr": "Clic traversant (décoratif, ignore la souris)",
        "es": "Clic transparente (solo decorativo, ignora el ratón)", "it": "Clic passante (solo decorativo, ignora il mouse)",
        "pt": "Clique passante (só decorativo, ignora o rato)", "pl": "Przezroczysty klik (tylko ozdoba, ignoruje mysz)",
        "nl": "Klik doorlaten (alleen decoratie, negeert muis)", "ru": "Прозрачно для мыши (только вид, без ввода)",
        "cs": "Průchozí klik (jen dekorace, ignoruje myš)", "tr": "Tıklama geçişi (yalnızca süs, fareyi yok sayar)",
    },
    "set.tip": {
        "en": "Tip: drag the panel with the left button, Ctrl+scroll resizes,\nright-click = menu, double-click = history.",
        "hu": "Tipp: a panelt bal gombbal húzhatod, Ctrl+görgő méretez,\njobb gomb = menü, dupla kattintás = előzmények.",
        "de": "Tipp: Panel mit der linken Taste ziehen, Strg+Rad ändert die Größe,\nRechtsklick = Menü, Doppelklick = Verlauf.",
        "fr": "Astuce : déplace le panneau avec le bouton gauche, Ctrl+molette redimensionne,\nclic droit = menu, double-clic = historique.",
        "es": "Consejo: arrastra el panel con el botón izquierdo, Ctrl+rueda cambia el tamaño,\nclic derecho = menú, doble clic = historial.",
        "it": "Suggerimento: trascina il pannello col tasto sinistro, Ctrl+rotella ridimensiona,\nclic destro = menu, doppio clic = cronologia.",
        "pt": "Dica: arrasta o painel com o botão esquerdo, Ctrl+roda redimensiona,\nclique direito = menu, duplo clique = histórico.",
        "pl": "Wskazówka: przeciągaj panel lewym przyciskiem, Ctrl+kółko zmienia rozmiar,\nprawy przycisk = menu, dwuklik = historia.",
        "nl": "Tip: sleep het paneel met de linkerknop, Ctrl+scroll wijzigt de grootte,\nrechtsklik = menu, dubbelklik = geschiedenis.",
        "ru": "Совет: перетаскивайте панель левой кнопкой, Ctrl+колесо меняет размер,\nправый клик = меню, двойной клик = история.",
        "cs": "Tip: panel táhněte levým tlačítkem, Ctrl+kolečko mění velikost,\npravý klik = menu, dvojklik = historie.",
        "tr": "İpucu: paneli sol tuşla sürükle, Ctrl+tekerlek boyutlandırır,\nsağ tık = menü, çift tık = geçmiş.",
    },
    "set.show_five_hour": {
        "en": "Show 5-hour window", "hu": "5 órás ablak mutatása", "de": "5-Stunden-Fenster anzeigen",
        "fr": "Afficher la fenêtre 5 heures", "es": "Mostrar ventana de 5 horas", "it": "Mostra finestra 5 ore",
        "pt": "Mostrar janela de 5 horas", "pl": "Pokaż okno 5-godzinne", "nl": "5-uurs venster tonen",
        "ru": "Показывать окно 5 часов", "cs": "Zobrazit 5hodinové okno", "tr": "5 saatlik pencereyi göster",
    },
    "set.show_weekly": {
        "en": "Show weekly limit", "hu": "Heti keret mutatása", "de": "Wochenlimit anzeigen",
        "fr": "Afficher le quota hebdo", "es": "Mostrar límite semanal", "it": "Mostra limite settimanale",
        "pt": "Mostrar limite semanal", "pl": "Pokaż limit tygodniowy", "nl": "Weeklimiet tonen",
        "ru": "Показывать недельный лимит", "cs": "Zobrazit týdenní limit", "tr": "Haftalık kotayı göster",
    },
    "set.show_spark": {
        "en": "Trend curve (sparkline)", "hu": "Trendgörbe (sparkline)", "de": "Trendkurve (Sparkline)",
        "fr": "Courbe de tendance (sparkline)", "es": "Curva de tendencia (sparkline)", "it": "Curva di tendenza (sparkline)",
        "pt": "Curva de tendência (sparkline)", "pl": "Krzywa trendu (sparkline)", "nl": "Trendcurve (sparkline)",
        "ru": "Кривая тренда (спарклайн)", "cs": "Křivka trendu (sparkline)", "tr": "Eğilim eğrisi (sparkline)",
    },
    "set.show_burn": {
        "en": "Burn rate (%/hour, %/day)", "hu": "Fogyási ütem (%/óra, %/nap)", "de": "Verbrauchsrate (%/Std, %/Tag)",
        "fr": "Rythme de consommation (%/h, %/j)", "es": "Ritmo de consumo (%/h, %/día)", "it": "Ritmo di consumo (%/h, %/g)",
        "pt": "Ritmo de consumo (%/h, %/dia)", "pl": "Tempo zużycia (%/godz, %/dzień)", "nl": "Verbruikstempo (%/u, %/dag)",
        "ru": "Скорость расхода (%/ч, %/день)", "cs": "Tempo spotřeby (%/h, %/den)", "tr": "Tüketim hızı (%/sa, %/gün)",
    },
    "set.show_reset": {
        "en": "Countdown to reset", "hu": "Visszaszámlálás a resetig", "de": "Countdown bis Reset",
        "fr": "Compte à rebours avant reset", "es": "Cuenta atrás hasta el reinicio", "it": "Conto alla rovescia al reset",
        "pt": "Contagem decrescente até o reinício", "pl": "Odliczanie do resetu", "nl": "Aftellen tot reset",
        "ru": "Обратный отсчёт до сброса", "cs": "Odpočet do resetu", "tr": "Sıfırlamaya geri sayım",
    },
    "set.show_age": {
        "en": "Data freshness", "hu": "Adat frissessége", "de": "Datenaktualität",
        "fr": "Fraîcheur des données", "es": "Frescura de los datos", "it": "Freschezza dei dati",
        "pt": "Atualidade dos dados", "pl": "Świeżość danych", "nl": "Actualiteit van gegevens",
        "ru": "Свежесть данных", "cs": "Aktuálnost dat", "tr": "Veri tazeliği",
    },
    "set.tray_value": {
        "en": "Tray icon value", "hu": "Tálcaikon értéke", "de": "Tray-Symbol-Wert",
        "fr": "Valeur de l'icône", "es": "Valor del icono", "it": "Valore dell'icona",
        "pt": "Valor do ícone", "pl": "Wartość ikony", "nl": "Waarde van pictogram",
        "ru": "Значение значка", "cs": "Hodnota ikony", "tr": "Simge değeri",
    },
    "set.tray_five": {
        "en": "5-hour window", "hu": "5 órás ablak", "de": "5-Stunden-Fenster", "fr": "Fenêtre 5 heures",
        "es": "Ventana de 5 horas", "it": "Finestra 5 ore", "pt": "Janela de 5 horas", "pl": "Okno 5-godzinne",
        "nl": "5-uurs venster", "ru": "Окно 5 часов", "cs": "5hodinové okno", "tr": "5 saatlik pencere",
    },
    "set.tray_weekly": {
        "en": "Weekly limit", "hu": "Heti keret", "de": "Wochenlimit", "fr": "Quota hebdo",
        "es": "Límite semanal", "it": "Limite settimanale", "pt": "Limite semanal", "pl": "Limit tygodniowy",
        "nl": "Weeklimiet", "ru": "Недельный лимит", "cs": "Týdenní limit", "tr": "Haftalık kota",
    },
    "set.tray_max": {
        "en": "Whichever is higher", "hu": "Amelyik magasabb", "de": "Der höhere Wert",
        "fr": "Le plus élevé", "es": "El que sea mayor", "it": "Quello più alto",
        "pt": "O que for maior", "pl": "Ten wyższy", "nl": "De hoogste",
        "ru": "Который выше", "cs": "Ten vyšší", "tr": "Hangisi yüksekse",
    },
    "set.warn": {
        "en": "Warning", "hu": "Figyelmeztetés", "de": "Warnung", "fr": "Avertissement",
        "es": "Advertencia", "it": "Avviso", "pt": "Aviso", "pl": "Ostrzeżenie",
        "nl": "Waarschuwing", "ru": "Предупреждение", "cs": "Varování", "tr": "Uyarı",
    },
    "set.danger": {
        "en": "Critical", "hu": "Vészjelzés", "de": "Kritisch", "fr": "Critique", "es": "Crítico",
        "it": "Critico", "pt": "Crítico", "pl": "Krytyczny", "nl": "Kritiek", "ru": "Критично",
        "cs": "Kritické", "tr": "Kritik",
    },
    "set.notify_enabled": {
        "en": "Notify on threshold crossing", "hu": "Értesítés a küszöbök átlépésekor",
        "de": "Benachrichtigen beim Überschreiten von Schwellen", "fr": "Notifier au franchissement d'un seuil",
        "es": "Notificar al cruzar un umbral", "it": "Notifica al superamento di una soglia",
        "pt": "Notificar ao cruzar um limiar", "pl": "Powiadamiaj przy przekroczeniu progu",
        "nl": "Melden bij overschrijden van drempel", "ru": "Уведомлять при пересечении порога",
        "cs": "Upozornit při překročení prahu", "tr": "Eşik aşımında bildir",
    },
    "set.notify_reset": {
        "en": "Notify when a limit resets", "hu": "Értesítés, ha egy keret lenullázódott",
        "de": "Benachrichtigen, wenn ein Limit zurückgesetzt wird", "fr": "Notifier quand un quota est réinitialisé",
        "es": "Notificar cuando un límite se reinicia", "it": "Notifica quando un limite si azzera",
        "pt": "Notificar quando um limite reinicia", "pl": "Powiadamiaj, gdy limit się zeruje",
        "nl": "Melden wanneer een limiet reset", "ru": "Уведомлять при сбросе лимита",
        "cs": "Upozornit, když se limit vynuluje", "tr": "Bir kota sıfırlanınca bildir",
    },
    "set.notify_stale": {
        "en": "Notify when data goes stale", "hu": "Értesítés, ha elavul az adat",
        "de": "Benachrichtigen, wenn Daten veralten", "fr": "Notifier quand les données sont périmées",
        "es": "Notificar cuando los datos se vuelven obsoletos", "it": "Notifica quando i dati diventano obsoleti",
        "pt": "Notificar quando os dados ficam desatualizados", "pl": "Powiadamiaj, gdy dane się dezaktualizują",
        "nl": "Melden wanneer gegevens verouderen", "ru": "Уведомлять при устаревании данных",
        "cs": "Upozornit, když data zastarají", "tr": "Veri eskiyince bildir",
    },
    "set.color_hint": {
        "en": "Colors change with the thresholds: green → yellow → red.",
        "hu": "A színek a küszöbök szerint váltanak: zöld → sárga → piros.",
        "de": "Farben ändern sich mit den Schwellen: grün → gelb → rot.",
        "fr": "Les couleurs changent selon les seuils : vert → jaune → rouge.",
        "es": "Los colores cambian con los umbrales: verde → amarillo → rojo.",
        "it": "I colori cambiano con le soglie: verde → giallo → rosso.",
        "pt": "As cores mudam com os limiares: verde → amarelo → vermelho.",
        "pl": "Kolory zmieniają się z progami: zielony → żółty → czerwony.",
        "nl": "Kleuren veranderen met de drempels: groen → geel → rood.",
        "ru": "Цвета меняются по порогам: зелёный → жёлтый → красный.",
        "cs": "Barvy se mění podle prahů: zelená → žlutá → červená.",
        "tr": "Renkler eşiklerle değişir: yeşil → sarı → kırmızı.",
    },
    "set.source_label": {
        "en": "Measurement source", "hu": "Mérés forrása", "de": "Messquelle", "fr": "Source de mesure",
        "es": "Origen de medición", "it": "Origine misurazione", "pt": "Fonte de medição",
        "pl": "Źródło pomiaru", "nl": "Meetbron", "ru": "Источник измерения", "cs": "Zdroj měření",
        "tr": "Ölçüm kaynağı",
    },
    "set.source_local": {
        "en": "Local log – this PC only", "hu": "Helyi napló – csak ez a gép", "de": "Lokales Protokoll – nur dieser PC",
        "fr": "Journal local – ce PC uniquement", "es": "Registro local – solo este PC", "it": "Log locale – solo questo PC",
        "pt": "Registo local – só este PC", "pl": "Dziennik lokalny – tylko ten PC", "nl": "Lokaal logboek – alleen deze pc",
        "ru": "Локальный журнал – только этот ПК", "cs": "Místní protokol – jen tento PC", "tr": "Yerel günlük – yalnızca bu PC",
    },
    "set.source_api": {
        "en": "claude.ai – all devices (sign-in required)", "hu": "claude.ai – minden eszköz (bejelentkezés kell)",
        "de": "claude.ai – alle Geräte (Anmeldung nötig)", "fr": "claude.ai – tous appareils (connexion requise)",
        "es": "claude.ai – todos los dispositivos (requiere sesión)", "it": "claude.ai – tutti i dispositivi (accesso richiesto)",
        "pt": "claude.ai – todos os dispositivos (login necessário)", "pl": "claude.ai – wszystkie urządzenia (wymaga logowania)",
        "nl": "claude.ai – alle apparaten (aanmelden vereist)", "ru": "claude.ai – все устройства (нужен вход)",
        "cs": "claude.ai – všechna zařízení (nutné přihlášení)", "tr": "claude.ai – tüm cihazlar (giriş gerekir)",
    },
    "set.login_btn_in": {
        "en": "Sign out of claude.ai", "hu": "Kijelentkezés a claude.ai-ról", "de": "Von claude.ai abmelden",
        "fr": "Se déconnecter de claude.ai", "es": "Cerrar sesión de claude.ai", "it": "Esci da claude.ai",
        "pt": "Sair de claude.ai", "pl": "Wyloguj z claude.ai", "nl": "Afmelden bij claude.ai",
        "ru": "Выйти из claude.ai", "cs": "Odhlásit z claude.ai", "tr": "claude.ai'den çıkış yap",
    },
    "set.login_btn_out": {
        "en": "Sign in to claude.ai…", "hu": "Bejelentkezés a claude.ai-ra…", "de": "Bei claude.ai anmelden…",
        "fr": "Se connecter à claude.ai…", "es": "Iniciar sesión en claude.ai…", "it": "Accedi a claude.ai…",
        "pt": "Entrar em claude.ai…", "pl": "Zaloguj do claude.ai…", "nl": "Aanmelden bij claude.ai…",
        "ru": "Войти в claude.ai…", "cs": "Přihlásit ke claude.ai…", "tr": "claude.ai'ye giriş yap…",
    },
    "set.profile": {
        "en": "Profile / account", "hu": "Profil / fiók", "de": "Profil / Konto", "fr": "Profil / compte",
        "es": "Perfil / cuenta", "it": "Profilo / account", "pt": "Perfil / conta", "pl": "Profil / konto",
        "nl": "Profiel / account", "ru": "Профиль / аккаунт", "cs": "Profil / účet", "tr": "Profil / hesap",
    },
    "set.profile_auto": {
        "en": "Automatic (last used)", "hu": "Automatikus (legutóbb használt)", "de": "Automatisch (zuletzt verwendet)",
        "fr": "Automatique (dernier utilisé)", "es": "Automático (último usado)", "it": "Automatico (ultimo usato)",
        "pt": "Automático (último usado)", "pl": "Automatycznie (ostatnio używany)", "nl": "Automatisch (laatst gebruikt)",
        "ru": "Автоматически (последний)", "cs": "Automaticky (naposledy použitý)", "tr": "Otomatik (son kullanılan)",
    },
    "set.profile_n": {
        "en": "Profile {} – …{}", "hu": "Profil {} – …{}", "de": "Profil {} – …{}", "fr": "Profil {} – …{}",
        "es": "Perfil {} – …{}", "it": "Profilo {} – …{}", "pt": "Perfil {} – …{}", "pl": "Profil {} – …{}",
        "nl": "Profiel {} – …{}", "ru": "Профиль {} – …{}", "cs": "Profil {} – …{}", "tr": "Profil {} – …{}",
    },
    "set.refresh": {
        "en": "Refresh", "hu": "Frissítés", "de": "Aktualisierung", "fr": "Actualisation",
        "es": "Actualización", "it": "Aggiornamento", "pt": "Atualização", "pl": "Odświeżanie",
        "nl": "Vernieuwen", "ru": "Обновление", "cs": "Obnovení", "tr": "Yenileme",
    },
    "set.sec_suffix": {
        "en": " s", "hu": " mp", "de": " s", "fr": " s", "es": " s", "it": " s",
        "pt": " s", "pl": " s", "nl": " s", "ru": " с", "cs": " s", "tr": " sn",
    },
    "set.datafile": {
        "en": "Data file", "hu": "Adatfájl", "de": "Datendatei", "fr": "Fichier de données",
        "es": "Archivo de datos", "it": "File dati", "pt": "Ficheiro de dados", "pl": "Plik danych",
        "nl": "Gegevensbestand", "ru": "Файл данных", "cs": "Datový soubor", "tr": "Veri dosyası",
    },
    "set.data_hint": {
        "en": "Local log: Claude Desktop's plan-usage-history.json. No sign-in, but measures only this PC and refreshes about every 5 minutes.\n\nclaude.ai: after sign-in it queries the server. You see usage from all your devices, with exact reset times and more frequent refresh.",
        "hu": "Helyi napló: a Claude Desktop plan-usage-history.json fájlja. Nem kell bejelentkezés, de csak ezt a gépet méri, és kb. 5 percenként frissül.\n\nclaude.ai: a bejelentkezés után a szerverről kérdez le. Minden eszközöd használatát látod, pontos reset-időkkel, gyakoribb frissítéssel.",
        "de": "Lokales Protokoll: die plan-usage-history.json von Claude Desktop. Keine Anmeldung, misst aber nur diesen PC und aktualisiert etwa alle 5 Minuten.\n\nclaude.ai: nach der Anmeldung wird der Server abgefragt. Du siehst die Nutzung aller Geräte, mit exakten Reset-Zeiten und häufigerer Aktualisierung.",
        "fr": "Journal local : le plan-usage-history.json de Claude Desktop. Sans connexion, mais mesure seulement ce PC et se met à jour environ toutes les 5 minutes.\n\nclaude.ai : après connexion, interroge le serveur. Tu vois l'usage de tous tes appareils, avec des heures de reset exactes et une actualisation plus fréquente.",
        "es": "Registro local: el plan-usage-history.json de Claude Desktop. Sin inicio de sesión, pero mide solo este PC y se actualiza cada ~5 minutos.\n\nclaude.ai: tras iniciar sesión consulta el servidor. Ves el uso de todos tus dispositivos, con horas de reinicio exactas y actualización más frecuente.",
        "it": "Log locale: il plan-usage-history.json di Claude Desktop. Nessun accesso, ma misura solo questo PC e si aggiorna ogni ~5 minuti.\n\nclaude.ai: dopo l'accesso interroga il server. Vedi l'uso di tutti i dispositivi, con orari di reset esatti e aggiornamento più frequente.",
        "pt": "Registo local: o plan-usage-history.json do Claude Desktop. Sem login, mas mede só este PC e atualiza a cada ~5 minutos.\n\nclaude.ai: após o login consulta o servidor. Vês o uso de todos os teus dispositivos, com horas de reinício exatas e atualização mais frequente.",
        "pl": "Dziennik lokalny: plik plan-usage-history.json z Claude Desktop. Bez logowania, ale mierzy tylko ten PC i odświeża co ~5 minut.\n\nclaude.ai: po zalogowaniu odpytuje serwer. Widzisz użycie ze wszystkich urządzeń, z dokładnymi czasami resetu i częstszym odświeżaniem.",
        "nl": "Lokaal logboek: de plan-usage-history.json van Claude Desktop. Geen aanmelding, maar meet alleen deze pc en vernieuwt ongeveer elke 5 minuten.\n\nclaude.ai: na aanmelden bevraagt het de server. Je ziet het gebruik van al je apparaten, met exacte reset-tijden en vaker vernieuwen.",
        "ru": "Локальный журнал: файл plan-usage-history.json из Claude Desktop. Без входа, но измеряет только этот ПК и обновляется примерно раз в 5 минут.\n\nclaude.ai: после входа запрашивает сервер. Вы видите использование со всех устройств, с точным временем сброса и более частым обновлением.",
        "cs": "Místní protokol: soubor plan-usage-history.json z Claude Desktop. Bez přihlášení, ale měří jen tento PC a obnovuje se zhruba každých 5 minut.\n\nclaude.ai: po přihlášení se dotazuje serveru. Vidíte využití ze všech zařízení, s přesnými časy resetu a častější aktualizací.",
        "tr": "Yerel günlük: Claude Desktop'ın plan-usage-history.json dosyası. Giriş gerekmez ama yalnızca bu PC'yi ölçer ve ~5 dakikada bir yenilenir.\n\nclaude.ai: giriş sonrası sunucuyu sorgular. Tüm cihazlarının kullanımını, tam sıfırlama saatleriyle ve daha sık yenilemeyle görürsün.",
    },
    "set.pick_file_title": {
        "en": "Choose usage log", "hu": "Használati napló kiválasztása", "de": "Nutzungsprotokoll wählen",
        "fr": "Choisir le journal d'usage", "es": "Elegir el registro de uso", "it": "Scegli il log d'uso",
        "pt": "Escolher o registo de uso", "pl": "Wybierz dziennik użycia", "nl": "Kies gebruikslogboek",
        "ru": "Выбрать журнал использования", "cs": "Vybrat protokol využití", "tr": "Kullanım günlüğünü seç",
    },
    "set.file_filter": {
        "en": "JSON (*.json);;All files (*.*)", "hu": "JSON (*.json);;Minden fájl (*.*)",
        "de": "JSON (*.json);;Alle Dateien (*.*)", "fr": "JSON (*.json);;Tous les fichiers (*.*)",
        "es": "JSON (*.json);;Todos los archivos (*.*)", "it": "JSON (*.json);;Tutti i file (*.*)",
        "pt": "JSON (*.json);;Todos os ficheiros (*.*)", "pl": "JSON (*.json);;Wszystkie pliki (*.*)",
        "nl": "JSON (*.json);;Alle bestanden (*.*)", "ru": "JSON (*.json);;Все файлы (*.*)",
        "cs": "JSON (*.json);;Všechny soubory (*.*)", "tr": "JSON (*.json);;Tüm dosyalar (*.*)",
    },
    "set.open_config": {
        "en": "Open settings folder", "hu": "Beállítások mappa megnyitása", "de": "Einstellungsordner öffnen",
        "fr": "Ouvrir le dossier des paramètres", "es": "Abrir carpeta de ajustes", "it": "Apri cartella impostazioni",
        "pt": "Abrir pasta de configurações", "pl": "Otwórz folder ustawień", "nl": "Instellingenmap openen",
        "ru": "Открыть папку настроек", "cs": "Otevřít složku nastavení", "tr": "Ayarlar klasörünü aç",
    },
    "set.restore": {
        "en": "Restore defaults", "hu": "Alapértelmezések visszaállítása", "de": "Standard wiederherstellen",
        "fr": "Restaurer les valeurs par défaut", "es": "Restaurar predeterminados", "it": "Ripristina predefiniti",
        "pt": "Restaurar predefinições", "pl": "Przywróć domyślne", "nl": "Standaard herstellen",
        "ru": "Сбросить настройки", "cs": "Obnovit výchozí", "tr": "Varsayılanları geri yükle",
    },
    "set.about": {
        "en": "{}\nWorks from local data, sends nothing anywhere.",
        "hu": "{}\nHelyi adatokból dolgozik, semmit nem küld sehova.",
        "de": "{}\nArbeitet mit lokalen Daten, sendet nichts irgendwohin.",
        "fr": "{}\nFonctionne à partir de données locales, n'envoie rien nulle part.",
        "es": "{}\nFunciona con datos locales, no envía nada a ningún sitio.",
        "it": "{}\nLavora con dati locali, non invia nulla da nessuna parte.",
        "pt": "{}\nTrabalha com dados locais, não envia nada para lado nenhum.",
        "pl": "{}\nDziała na danych lokalnych, nic nigdzie nie wysyła.",
        "nl": "{}\nWerkt met lokale gegevens, verstuurt niets ergens heen.",
        "ru": "{}\nРаботает с локальными данными, ничего никуда не отправляет.",
        "cs": "{}\nPracuje z místních dat, nic nikam neposílá.",
        "tr": "{}\nYerel verilerle çalışır, hiçbir yere bir şey göndermez.",
    },
    "set.reset_confirm": {
        "en": "Are you sure you want to restore the default settings?",
        "hu": "Biztosan visszaállítod az alapértelmezett beállításokat?",
        "de": "Möchtest du die Standardeinstellungen wirklich wiederherstellen?",
        "fr": "Veux-tu vraiment restaurer les paramètres par défaut ?",
        "es": "¿Seguro que quieres restaurar los ajustes predeterminados?",
        "it": "Vuoi davvero ripristinare le impostazioni predefinite?",
        "pt": "Tens a certeza de que queres restaurar as predefinições?",
        "pl": "Na pewno przywrócić ustawienia domyślne?",
        "nl": "Weet je zeker dat je de standaardinstellingen wilt herstellen?",
        "ru": "Точно восстановить настройки по умолчанию?",
        "cs": "Opravdu obnovit výchozí nastavení?",
        "tr": "Varsayılan ayarları geri yüklemek istediğine emin misin?",
    },

    # ===================== history window (history) =====================
    "hist.title": {
        "en": "history", "hu": "előzmények", "de": "Verlauf", "fr": "historique", "es": "historial",
        "it": "cronologia", "pt": "histórico", "pl": "historia", "nl": "geschiedenis", "ru": "история",
        "cs": "historie", "tr": "geçmiş",
    },
    "hist.range_6h": {
        "en": "6 hours", "hu": "6 óra", "de": "6 Stunden", "fr": "6 heures", "es": "6 horas",
        "it": "6 ore", "pt": "6 horas", "pl": "6 godzin", "nl": "6 uur", "ru": "6 часов",
        "cs": "6 hodin", "tr": "6 saat",
    },
    "hist.range_24h": {
        "en": "24 hours", "hu": "24 óra", "de": "24 Stunden", "fr": "24 heures", "es": "24 horas",
        "it": "24 ore", "pt": "24 horas", "pl": "24 godziny", "nl": "24 uur", "ru": "24 часа",
        "cs": "24 hodin", "tr": "24 saat",
    },
    "hist.range_7d": {
        "en": "7 days", "hu": "7 nap", "de": "7 Tage", "fr": "7 jours", "es": "7 días",
        "it": "7 giorni", "pt": "7 dias", "pl": "7 dni", "nl": "7 dagen", "ru": "7 дней",
        "cs": "7 dní", "tr": "7 gün",
    },
    "hist.range_all": {
        "en": "All", "hu": "Teljes", "de": "Alle", "fr": "Tout", "es": "Todo", "it": "Tutto",
        "pt": "Tudo", "pl": "Wszystko", "nl": "Alles", "ru": "Всё", "cs": "Vše", "tr": "Tümü",
    },
    "hist.legend_5h": {
        "en": "5-hour window", "hu": "5 órás ablak", "de": "5-Stunden-Fenster", "fr": "fenêtre 5 h",
        "es": "ventana de 5 h", "it": "finestra 5 ore", "pt": "janela de 5 h", "pl": "okno 5-godz.",
        "nl": "5-uurs venster", "ru": "окно 5 часов", "cs": "5hodinové okno", "tr": "5 saatlik pencere",
    },
    "hist.legend_week": {
        "en": "weekly limit", "hu": "heti keret", "de": "Wochenlimit", "fr": "quota hebdo",
        "es": "límite semanal", "it": "limite settimanale", "pt": "limite semanal", "pl": "limit tygodniowy",
        "nl": "weeklimiet", "ru": "недельный лимит", "cs": "týdenní limit", "tr": "haftalık kota",
    },
    "hist.stat_now": {
        "en": "Current weekly", "hu": "Jelenlegi heti", "de": "Aktuell (Woche)", "fr": "Hebdo actuel",
        "es": "Semanal actual", "it": "Settimanale attuale", "pt": "Semanal atual", "pl": "Bieżący tygodniowy",
        "nl": "Huidig wekelijks", "ru": "Текущий недельный", "cs": "Aktuální týdenní", "tr": "Güncel haftalık",
    },
    "hist.stat_peak": {
        "en": "Weekly peak", "hu": "Heti csúcs", "de": "Wochen-Spitze", "fr": "Pic hebdo",
        "es": "Pico semanal", "it": "Picco settimanale", "pt": "Pico semanal", "pl": "Szczyt tygodniowy",
        "nl": "Weekpiek", "ru": "Недельный пик", "cs": "Týdenní vrchol", "tr": "Haftalık zirve",
    },
    "hist.stat_burn": {
        "en": "Avg daily burn", "hu": "Napi átlag fogyás", "de": "Ø täglicher Verbrauch",
        "fr": "Conso. moy./jour", "es": "Consumo medio diario", "it": "Consumo medio/giorno",
        "pt": "Consumo médio/dia", "pl": "Śr. dzienne zużycie", "nl": "Gem. dagverbruik",
        "ru": "Средн. расход/день", "cs": "Prům. denní spotřeba", "tr": "Ort. günlük tüketim",
    },
    "hist.stat_sessions": {
        "en": "5-hour windows", "hu": "5 órás ablakok", "de": "5-Stunden-Fenster", "fr": "Fenêtres de 5 h",
        "es": "Ventanas de 5 h", "it": "Finestre da 5 ore", "pt": "Janelas de 5 h", "pl": "Okna 5-godz.",
        "nl": "5-uurs vensters", "ru": "Окна по 5 часов", "cs": "5hodinová okna", "tr": "5 saatlik pencereler",
    },
    "hist.stat_forecast": {
        "en": "End-of-week projection", "hu": "Hét végére – előrejelzés", "de": "Prognose Wochenende",
        "fr": "Projection fin de semaine", "es": "Proyección fin de semana", "it": "Proiezione a fine settimana",
        "pt": "Projeção fim de semana", "pl": "Prognoza na koniec tygodnia", "nl": "Prognose weekeinde",
        "ru": "Прогноз на конец недели", "cs": "Odhad na konec týdne", "tr": "Hafta sonu tahmini",
    },
    "hist.no_data": {
        "en": "Not enough data for this period.", "hu": "Nincs elég adat ehhez az időszakhoz.",
        "de": "Nicht genug Daten für diesen Zeitraum.", "fr": "Pas assez de données pour cette période.",
        "es": "No hay datos suficientes para este período.", "it": "Dati insufficienti per questo periodo.",
        "pt": "Dados insuficientes para este período.", "pl": "Za mało danych dla tego okresu.",
        "nl": "Niet genoeg gegevens voor deze periode.", "ru": "Недостаточно данных за этот период.",
        "cs": "Pro toto období není dost dat.", "tr": "Bu dönem için yeterli veri yok.",
    },

    # ===================== állapot / hibaüzenetek (panel, dialógus) =====================
    "err.file_not_found": {
        "en": "Usage file not found.\nIs Claude Desktop running?",
        "hu": "A használati fájl nem található.\nFut a Claude Desktop?",
        "de": "Nutzungsdatei nicht gefunden.\nLäuft Claude Desktop?",
        "fr": "Fichier d'usage introuvable.\nClaude Desktop est-il lancé ?",
        "es": "Archivo de uso no encontrado.\n¿Claude Desktop está abierto?",
        "it": "File d'uso non trovato.\nClaude Desktop è in esecuzione?",
        "pt": "Ficheiro de uso não encontrado.\nO Claude Desktop está aberto?",
        "pl": "Nie znaleziono pliku użycia.\nCzy Claude Desktop działa?",
        "nl": "Gebruiksbestand niet gevonden.\nDraait Claude Desktop?",
        "ru": "Файл использования не найден.\nClaude Desktop запущен?",
        "cs": "Soubor s využitím nenalezen.\nBěží Claude Desktop?",
        "tr": "Kullanım dosyası bulunamadı.\nClaude Desktop çalışıyor mu?",
    },
    "err.file_unreadable": {
        "en": "The usage file is currently unreadable.", "hu": "A használati fájl jelenleg nem olvasható.",
        "de": "Die Nutzungsdatei ist derzeit nicht lesbar.", "fr": "Le fichier d'usage est illisible pour l'instant.",
        "es": "El archivo de uso no se puede leer ahora.", "it": "Il file d'uso non è leggibile al momento.",
        "pt": "O ficheiro de uso está ilegível de momento.", "pl": "Plik użycia jest teraz nieczytelny.",
        "nl": "Het gebruiksbestand is momenteel onleesbaar.", "ru": "Файл использования сейчас нечитаем.",
        "cs": "Soubor s využitím je momentálně nečitelný.", "tr": "Kullanım dosyası şu an okunamıyor.",
    },
    "err.file_empty": {
        "en": "The usage file is empty.", "hu": "A használati fájl üres.", "de": "Die Nutzungsdatei ist leer.",
        "fr": "Le fichier d'usage est vide.", "es": "El archivo de uso está vacío.", "it": "Il file d'uso è vuoto.",
        "pt": "O ficheiro de uso está vazio.", "pl": "Plik użycia jest pusty.", "nl": "Het gebruiksbestand is leeg.",
        "ru": "Файл использования пуст.", "cs": "Soubor s využitím je prázdný.", "tr": "Kullanım dosyası boş.",
    },
    "err.no_usage_data": {
        "en": "No usage data.", "hu": "Nincs használati adat.", "de": "Keine Nutzungsdaten.",
        "fr": "Aucune donnée d'usage.", "es": "Sin datos de uso.", "it": "Nessun dato d'uso.",
        "pt": "Sem dados de uso.", "pl": "Brak danych użycia.", "nl": "Geen gebruiksgegevens.",
        "ru": "Нет данных об использовании.", "cs": "Žádná data o využití.", "tr": "Kullanım verisi yok.",
    },
    "err.no_data_profile": {
        "en": "No data for this profile.", "hu": "Ehhez a profilhoz nincs adat.", "de": "Keine Daten für dieses Profil.",
        "fr": "Aucune donnée pour ce profil.", "es": "Sin datos para este perfil.", "it": "Nessun dato per questo profilo.",
        "pt": "Sem dados para este perfil.", "pl": "Brak danych dla tego profilu.", "nl": "Geen gegevens voor dit profiel.",
        "ru": "Нет данных для этого профиля.", "cs": "Pro tento profil nejsou data.", "tr": "Bu profil için veri yok.",
    },
    "err.session_expired": {
        "en": "The session has expired, sign in again.", "hu": "A munkamenet lejárt, jelentkezz be újra.",
        "de": "Die Sitzung ist abgelaufen, melde dich erneut an.", "fr": "La session a expiré, reconnecte-toi.",
        "es": "La sesión expiró, vuelve a iniciar sesión.", "it": "La sessione è scaduta, accedi di nuovo.",
        "pt": "A sessão expirou, entra novamente.", "pl": "Sesja wygasła, zaloguj się ponownie.",
        "nl": "De sessie is verlopen, meld je opnieuw aan.", "ru": "Сессия истекла, войдите снова.",
        "cs": "Relace vypršela, přihlaste se znovu.", "tr": "Oturum süresi doldu, tekrar giriş yap.",
    },
    "err.session_expired_nl": {
        "en": "The session has expired.\nSign in again.", "hu": "A munkamenet lejárt.\nJelentkezz be újra.",
        "de": "Die Sitzung ist abgelaufen.\nMelde dich erneut an.", "fr": "La session a expiré.\nReconnecte-toi.",
        "es": "La sesión expiró.\nVuelve a iniciar sesión.", "it": "La sessione è scaduta.\nAccedi di nuovo.",
        "pt": "A sessão expirou.\nEntra novamente.", "pl": "Sesja wygasła.\nZaloguj się ponownie.",
        "nl": "De sessie is verlopen.\nMeld je opnieuw aan.", "ru": "Сессия истекла.\nВойдите снова.",
        "cs": "Relace vypršela.\nPřihlaste se znovu.", "tr": "Oturum süresi doldu.\nTekrar giriş yap.",
    },
    "err.not_signed_in": {
        "en": "Not signed in.", "hu": "Nincs bejelentkezés.", "de": "Nicht angemeldet.",
        "fr": "Non connecté.", "es": "Sin sesión iniciada.", "it": "Non connesso.",
        "pt": "Sem sessão iniciada.", "pl": "Niezalogowano.", "nl": "Niet aangemeld.",
        "ru": "Вход не выполнен.", "cs": "Nepřihlášeno.", "tr": "Giriş yapılmadı.",
    },
    "err.query_http": {
        "en": "Query error (HTTP {}).", "hu": "Lekérdezési hiba (HTTP {}).", "de": "Abfragefehler (HTTP {}).",
        "fr": "Erreur de requête (HTTP {}).", "es": "Error de consulta (HTTP {}).", "it": "Errore di query (HTTP {}).",
        "pt": "Erro de consulta (HTTP {}).", "pl": "Błąd zapytania (HTTP {}).", "nl": "Query-fout (HTTP {}).",
        "ru": "Ошибка запроса (HTTP {}).", "cs": "Chyba dotazu (HTTP {}).", "tr": "Sorgu hatası (HTTP {}).",
    },
    "err.unexpected": {
        "en": "Unexpected error: {}", "hu": "Váratlan hiba: {}", "de": "Unerwarteter Fehler: {}",
        "fr": "Erreur inattendue : {}", "es": "Error inesperado: {}", "it": "Errore imprevisto: {}",
        "pt": "Erro inesperado: {}", "pl": "Nieoczekiwany błąd: {}", "nl": "Onverwachte fout: {}",
        "ru": "Непредвиденная ошибка: {}", "cs": "Neočekávaná chyba: {}", "tr": "Beklenmeyen hata: {}",
    },
    "err.loading": {
        "en": "Signing in / querying…", "hu": "Bejelentkezés / lekérdezés folyamatban…",
        "de": "Anmeldung / Abfrage läuft…", "fr": "Connexion / requête en cours…",
        "es": "Iniciando sesión / consultando…", "it": "Accesso / query in corso…",
        "pt": "A entrar / a consultar…", "pl": "Logowanie / zapytanie w toku…",
        "nl": "Aanmelden / opvragen…", "ru": "Вход / запрос…",
        "cs": "Přihlašování / dotaz…", "tr": "Giriş / sorgu sürüyor…",
    },
    "err.network": {
        "en": "network error: {}", "hu": "hálózati hiba: {}", "de": "Netzwerkfehler: {}",
        "fr": "erreur réseau : {}", "es": "error de red: {}", "it": "errore di rete: {}",
        "pt": "erro de rede: {}", "pl": "błąd sieci: {}", "nl": "netwerkfout: {}",
        "ru": "сетевая ошибка: {}", "cs": "chyba sítě: {}", "tr": "ağ hatası: {}",
    },
    "err.connection": {
        "en": "connection error: {}", "hu": "kapcsolati hiba: {}", "de": "Verbindungsfehler: {}",
        "fr": "erreur de connexion : {}", "es": "error de conexión: {}", "it": "errore di connessione: {}",
        "pt": "erro de ligação: {}", "pl": "błąd połączenia: {}", "nl": "verbindingsfout: {}",
        "ru": "ошибка соединения: {}", "cs": "chyba připojení: {}", "tr": "bağlantı hatası: {}",
    },
    "err.bad_token_resp": {
        "en": "invalid response from the token endpoint", "hu": "érvénytelen válasz a token-végponttól",
        "de": "ungültige Antwort vom Token-Endpunkt", "fr": "réponse invalide du point de terminaison du jeton",
        "es": "respuesta no válida del endpoint de token", "it": "risposta non valida dall'endpoint del token",
        "pt": "resposta inválida do endpoint de token", "pl": "nieprawidłowa odpowiedź z punktu tokena",
        "nl": "ongeldig antwoord van het token-eindpunt", "ru": "неверный ответ от token-эндпойнта",
        "cs": "neplatná odpověď z tokenového endpointu", "tr": "token uç noktasından geçersiz yanıt",
    },
    "err.bad_usage_resp": {
        "en": "invalid response from the usage endpoint", "hu": "érvénytelen válasz a usage-végponttól",
        "de": "ungültige Antwort vom Usage-Endpunkt", "fr": "réponse invalide du point de terminaison d'usage",
        "es": "respuesta no válida del endpoint de uso", "it": "risposta non valida dall'endpoint d'uso",
        "pt": "resposta inválida do endpoint de uso", "pl": "nieprawidłowa odpowiedź z punktu użycia",
        "nl": "ongeldig antwoord van het gebruik-eindpunt", "ru": "неверный ответ от usage-эндпойнта",
        "cs": "neplatná odpověď z usage endpointu", "tr": "kullanım uç noktasından geçersiz yanıt",
    },
    "err.no_code": {
        "en": "No code pasted.", "hu": "Nincs beillesztett kód.", "de": "Kein Code eingefügt.",
        "fr": "Aucun code collé.", "es": "No se pegó ningún código.", "it": "Nessun codice incollato.",
        "pt": "Nenhum código colado.", "pl": "Nie wklejono kodu.", "nl": "Geen code geplakt.",
        "ru": "Код не вставлен.", "cs": "Nevložen žádný kód.", "tr": "Kod yapıştırılmadı.",
    },
}
