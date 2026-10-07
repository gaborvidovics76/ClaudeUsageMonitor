# -*- coding: utf-8 -*-
"""Čeština – UI strings of Claude Usage Monitor (only the keys missing from the inline i18n tables)."""

CODE = "cs"
NAME = "Čeština"

STRINGS = {
    # 'Message to the developer' window
    "fb.cancel": "Zrušit",
    "fb.close": "Zavřít",
    "fb.consent": "Přečetl(a) jsem si {} a souhlasím s nimi.",
    "fb.email": "E-mail",
    "fb.email_hint": "jen pokud chcete odpověď",
    "fb.err_consent": "Před odesláním prosím přijměte zásady ochrany osobních údajů.",
    "fb.err_email": "Tato e-mailová adresa nevypadá správně.",
    "fb.err_empty": "Nejprve napište zprávu nebo zvolte hodnocení.",
    "fb.err_links": "Ve zprávě je příliš mnoho odkazů.",
    "fb.err_network": "Nepodařilo se spojit se serverem claudeusagemonitor.com. Zkontrolujte připojení a zkuste to znovu.",
    "fb.err_rate": "Příliš mnoho zpráv v krátké době – zkuste to prosím později.",
    "fb.err_server": "Server teď nemůže zprávu přijmout. Zkuste to prosím později.",
    "fb.intro": "Nápad, chyba, nebo se vám program prostě líbí? Napište mi. Každou zprávu čtu osobně – Vidovics Gábor, autor programu.",
    "fb.message": "Zpráva",
    "fb.message_ph": "Co funguje, co ne, co chybí?",
    "fb.meta": "Spolu se zprávou se odešle: verze programu {0}, operační systém ({1}), jazyk rozhraní ({2}).",
    "fb.name": "Jméno",
    "fb.optional": "(nepovinné)",
    "fb.privacy_hide": "Skrýt zásady",
    "fb.privacy_text": (
        "Správce osobních údajů: Vidovics Gábor, fyzická osoba (Maďarsko), autor programu Claude Usage Monitor. "
        "Úplné zásady ochrany osobních údajů najdete na webu: https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "Co se odesílá: to, co sem napíšete – jméno (nepovinné), e-mailová adresa (nepovinná), zpráva a "
        "hodnocení hvězdičkami – a dále, abych rozuměl souvislostem: verze programu, název a verze operačního "
        "systému, jazyk rozhraní a čas odeslání. Server neukládá IP adresu; proti zneužití používá pouze "
        "denně se měnící hash, který nelze převést zpět na adresu."
        "\n\n"
        "Účel: přečíst vaši zprávu, odpovědět na ni a zlepšovat program (oprávněný zájem, čl. 6 odst. 1 "
        "písm. f) GDPR; samotnou odpověď posílám na vaši žádost). Vaše hodnocení a jméno se na webu zobrazí "
        "jen tehdy, pokud to povolíte zaškrtnutím samostatného políčka (souhlas, čl. 6 odst. 1 písm. a) GDPR), "
        "a teprve poté, co je autor zkontroluje; tento souhlas můžete kdykoli odvolat."
        "\n\n"
        "Doba uchování: zprávy nejvýše 2 roky; zveřejněné hodnocení do odvolání souhlasu. Pokud má autor "
        "zapnuté přeposílání e-mailem, kopie dorazí i do jeho e-mailové schránky."
        "\n\n"
        "Kdo má přístup: pouze správce a – jako zpracovatel – poskytovatel hostingu (server v EU, "
        "v Německu). Nic se neprodává ani nepředává dál; neprobíhá profilování ani automatizované "
        "rozhodování."
        "\n\n"
        "Vaše práva: přístup, oprava, výmaz, omezení zpracování, námitka, odvolání souhlasu a stížnost "
        "u dozorového úřadu (v Maďarsku: NAIH, naih.hu) nebo u dozorového úřadu ve vaší zemi (v ČR: ÚOOÚ, "
        "uoou.gov.cz). Kontakt: tento formulář nebo web."
        "\n\n"
        "Přenos: šifrovaný (HTTPS/TLS) na claudeusagemonitor.com. Verze těchto zásad: 6. 10. 2026."
    ),
    "fb.privacy_title": "Zásady ochrany osobních údajů",
    "fb.publish": "Moje hodnocení a jméno (je-li uvedeno) se mohou zobrazit na webu claudeusagemonitor.com.",
    "fb.rating": "Celkové hodnocení",
    "fb.rating_clear": "vymazat",
    "fb.rating_hint": "nepovinné – klikněte na hvězdičku",
    "fb.rating_tip": "{} z 5",
    "fb.secure": "Šifrované připojení (HTTPS) k claudeusagemonitor.com.",
    "fb.send": "Odeslat",
    "fb.sending": "Odesílání…",
    "fb.sent": "Děkuji – zpráva dorazila!",
    "fb.sent_sub": "Každou zprávu si přečtu. Je-li vyplněna e-mailová adresa, odpovím na ni.",
    "fb.title": "Zpráva pro vývojáře",
    # context menu + Settings
    "menu.feedback": "Zpráva pro vývojáře…",
    "set.show_feedback_icon": "Ikona zprávy v záhlaví panelu",
}

# macOS wording: none of the new keys differ on macOS
STRINGS_MAC = {}
