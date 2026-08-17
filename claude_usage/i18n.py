"""Egyszerű, függőség nélküli lokalizáció.

A `tr(key, *args)` a jelenlegi nyelven adja vissza a szöveget (hiányzó fordításnál
angolra esik vissza). A nyelvet a beállítások tárolják; a `set_language` váltja.

Új nyelv hozzáadása: vedd fel a kódot a LANG_NAMES-be, és tölts a STRINGS minden
kulcsához egy `"<kód>": "..."` bejegyzést. Ami hiányzik, angolul jelenik meg.
"""

from __future__ import annotations

import locale
from typing import Dict, List

# A választható nyelvek – saját nevükön megjelenítve.
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
    """A Windows nyelvéből tippel egy támogatott kódot (különben angol)."""
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
# Fordítások.  Kulcs -> { nyelvkód: szöveg }.  Az "en" mindig kötelező (fallback).
# A {} helyőrzőkbe a tr() argumentumai kerülnek.
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

    # ---- idő (fmt_age / fmt_delta) ----
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
    # rövid összetett alakok: "{d}{d} {h}{h}" stb.
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

    # ---- menü ----
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

    # ---- tálca / értesítések ----
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
}
