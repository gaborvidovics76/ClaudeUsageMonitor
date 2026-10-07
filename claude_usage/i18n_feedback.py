"""'Message to the developer' window: form, consent, privacy notice (merged into i18n.STRINGS).

English and Hungarian live here; every other language is in claude_usage/langs/<code>.py.
"""

STRINGS_FEEDBACK = {
    "menu.feedback": {
        "en": "Message to the developer…", "hu": "Üzenet a fejlesztőnek…",
    },
    "set.show_feedback_icon": {
        "en": "Message icon in the panel header", "hu": "Üzenet-ikon a panel fejlécében",
    },
    "fb.title": {
        "en": "Message to the developer", "hu": "Üzenet a fejlesztőnek",
    },
    "fb.intro": {
        "en": "An idea, a bug, or you simply like it? Tell me. Every message is read by me, Vidovics Gábor, the author.",
        "hu": "Ötlet, hiba, vagy egyszerűen tetszik? Írd meg. Minden üzenetet én olvasok el, Vidovics Gábor, a program készítője.",
    },
    "fb.rating": {
        "en": "Overall rating", "hu": "Általános értékelés",
    },
    "fb.rating_hint": {
        "en": "optional – click a star", "hu": "nem kötelező – kattints egy csillagra",
    },
    "fb.rating_tip": {
        "en": "{} of 5", "hu": "{} / 5",
    },
    "fb.rating_clear": {
        "en": "clear", "hu": "törlés",
    },
    "fb.name": {
        "en": "Name", "hu": "Név",
    },
    "fb.optional": {
        "en": "(optional)", "hu": "(nem kötelező)",
    },
    "fb.email": {
        "en": "E-mail", "hu": "E-mail-cím",
    },
    "fb.email_hint": {
        "en": "only if you'd like a reply", "hu": "csak ha választ szeretnél",
    },
    "fb.message": {
        "en": "Message", "hu": "Üzenet",
    },
    "fb.message_ph": {
        "en": "What works, what doesn't, what's missing?",
        "hu": "Mi működik, mi nem, mi hiányzik?",
    },
    "fb.consent": {
        # {} = the title of the privacy notice (fb.privacy_title), shown as a link
        "en": "I have read and accept the {}.", "hu": "Elolvastam és elfogadom: {}.",
    },
    "fb.privacy_title": {
        "en": "Privacy Notice", "hu": "Adatkezelési tájékoztató",
    },
    "fb.privacy_hide": {
        "en": "Hide the notice", "hu": "Tájékoztató elrejtése",
    },
    "fb.publish": {
        "en": "My rating and my name (if given) may be shown on claudeusagemonitor.com.",
        "hu": "Az értékelésem és a nevem (ha megadtam) megjelenhet a claudeusagemonitor.com oldalon.",
    },
    "fb.meta": {
        # {0} = app version, {1} = operating system, {2} = interface language
        "en": "Sent along with the message: program version {0}, operating system ({1}), interface language ({2}).",
        "hu": "Az üzenettel együtt elmegy: a program verziója ({0}), az operációs rendszer ({1}), a felület nyelve ({2}).",
    },
    "fb.secure": {
        "en": "Encrypted connection (HTTPS) to claudeusagemonitor.com.",
        "hu": "Titkosított kapcsolat (HTTPS) a claudeusagemonitor.com felé.",
    },
    "fb.send": {
        "en": "Send", "hu": "Küldés",
    },
    "fb.cancel": {
        "en": "Cancel", "hu": "Mégse",
    },
    "fb.close": {
        "en": "Close", "hu": "Bezárás",
    },
    "fb.sending": {
        "en": "Sending…", "hu": "Küldés…",
    },
    "fb.sent": {
        "en": "Thank you – it has arrived!", "hu": "Köszönöm – megérkezett!",
    },
    "fb.sent_sub": {
        "en": "I read every message. If you left an e-mail address, I'll reply there.",
        "hu": "Minden üzenetet elolvasok. Ha megadtál e-mail-címet, oda válaszolok.",
    },
    "fb.err_empty": {
        "en": "Write a message or pick a rating first.",
        "hu": "Előbb írj üzenetet, vagy válassz értékelést.",
    },
    "fb.err_email": {
        "en": "This e-mail address doesn't look right.",
        "hu": "Ez az e-mail-cím nem tűnik érvényesnek.",
    },
    "fb.err_consent": {
        "en": "To send, please accept the privacy notice.",
        "hu": "A küldéshez el kell fogadnod az adatkezelési tájékoztatót.",
    },
    "fb.err_links": {
        "en": "Too many links in the message.",
        "hu": "Túl sok link van az üzenetben.",
    },
    "fb.err_rate": {
        "en": "Too many messages in a short time – please try again later.",
        "hu": "Túl sok üzenet rövid idő alatt – próbáld meg később.",
    },
    "fb.err_network": {
        "en": "Could not reach claudeusagemonitor.com. Check your connection and try again.",
        "hu": "Nem érhető el a claudeusagemonitor.com. Ellenőrizd a kapcsolatot, és próbáld újra.",
    },
    "fb.err_server": {
        "en": "The server could not take the message right now. Please try again later.",
        "hu": "A szerver most nem tudta fogadni az üzenetet. Próbáld meg később.",
    },
    "fb.privacy_text": {
        "en": (
            "Controller: Vidovics Gábor, private individual (Hungary), the author of Claude Usage Monitor. "
            "The full privacy policy is on the website: https://claudeusagemonitor.com/#privacy\n\n"
            "What is sent: what you type here – name (optional), e-mail address (optional), message, star rating – "
            "and, so that I can understand the context: the program version, the operating system name and version, "
            "the interface language and the time of sending. The server stores no IP address; to prevent abuse it "
            "only uses a daily-changing hash that cannot be turned back into an address.\n\n"
            "Why: to read and answer your message and to improve the program (legitimate interest, GDPR Art. 6(1)(f); "
            "the reply itself at your request). Your rating and your name appear on the website only if you tick the "
            "separate box for it (consent, Art. 6(1)(a)), and only after the author has reviewed it; you can withdraw "
            "that consent at any time.\n\n"
            "How long: messages for at most 2 years; a published rating until you withdraw your consent. If the author "
            "has switched on e-mail forwarding, a copy also reaches the author's mailbox.\n\n"
            "Who sees it: only the controller, and – as processor – the hosting provider (server in the EU, Germany). "
            "Nothing is sold or passed on; there is no profiling and no automated decision-making.\n\n"
            "Your rights: access, rectification, erasure, restriction, objection, withdrawal of consent, and a complaint "
            "to a supervisory authority (in Hungary: NAIH, naih.hu) or to the authority of your own country. "
            "Contact: this form or the website.\n\n"
            "Transport: encrypted (HTTPS/TLS) to claudeusagemonitor.com. Version of this notice: 2026-10-06."
        ),
        "hu": (
            "Adatkezelő: Vidovics Gábor, magánszemély (Magyarország), a Claude Usage Monitor készítője. "
            "A teljes adatkezelési tájékoztató a weboldalon olvasható: https://claudeusagemonitor.com/hu/#privacy\n\n"
            "Mi megy el: amit ide beírsz – név (nem kötelező), e-mail-cím (nem kötelező), üzenet, csillagos értékelés –, "
            "és hogy értsem az összefüggést: a program verziója, az operációs rendszer neve és verziója, a felület "
            "nyelve és a küldés időpontja. A szerver IP-címet nem tárol; a visszaélések ellen csak egy naponta változó, "
            "címmé vissza nem fejthető lenyomatot használ.\n\n"
            "Miért: hogy elolvassam és megválaszoljam az üzenetet, és hogy javítsam a programot (jogos érdek, GDPR "
            "6. cikk (1) f); maga a válasz a te kérésedre). Az értékelésed és a neved csak akkor jelenik meg a "
            "weboldalon, ha ezt külön bejelölöd (hozzájárulás, 6. cikk (1) a), és csak miután a készítő átnézte; a "
            "hozzájárulást bármikor visszavonhatod.\n\n"
            "Meddig: az üzeneteket legfeljebb 2 évig; a közzétett értékelést a hozzájárulás visszavonásáig. Ha a "
            "készítő bekapcsolta az e-mailes továbbítást, egy másolat a készítő postafiókjába is megérkezik.\n\n"
            "Ki látja: csak az adatkezelő, és adatfeldolgozóként a tárhelyszolgáltató (a szerver az EU-ban, "
            "Németországban van). Semmit nem adok el és nem adok tovább; profilalkotás és automatizált döntéshozatal nincs.\n\n"
            "Jogaid: hozzáférés, helyesbítés, törlés, korlátozás, tiltakozás, a hozzájárulás visszavonása, valamint "
            "panasz a felügyeleti hatóságnál (Magyarországon: NAIH, naih.hu) vagy a saját országod hatóságánál. "
            "Kapcsolat: ez az űrlap vagy a weboldal.\n\n"
            "Átvitel: titkosítva (HTTPS/TLS) a claudeusagemonitor.com felé. A tájékoztató verziója: 2026-10-06."
        ),
    },
}
