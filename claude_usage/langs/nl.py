# -*- coding: utf-8 -*-
"""Nederlands – UI strings of Claude Usage Monitor (only the keys that are not inline in i18n*.py)."""

CODE = "nl"
NAME = "Nederlands"

STRINGS = {
    # 'Message to the developer' window
    "fb.cancel": "Annuleren",
    "fb.close": "Sluiten",
    "fb.consent": "Ik heb de {} gelezen en ga ermee akkoord.",
    "fb.email": "E-mailadres",
    "fb.email_hint": "alleen als je antwoord wilt",
    "fb.err_consent": "Om te verzenden moet je eerst de privacyverklaring accepteren.",
    "fb.err_email": "Dit e-mailadres lijkt niet te kloppen.",
    "fb.err_empty": "Schrijf eerst een bericht of kies een beoordeling.",
    "fb.err_links": "Te veel links in het bericht.",
    "fb.err_network": "Kan claudeusagemonitor.com niet bereiken. Controleer je verbinding en probeer het opnieuw.",
    "fb.err_rate": "Te veel berichten in korte tijd – probeer het later opnieuw.",
    "fb.err_server": "De server kan het bericht op dit moment niet ontvangen. Probeer het later opnieuw.",
    "fb.intro": "Een idee, een bug, of vind je het programma gewoon fijn? Laat het me weten. Ik lees elk bericht zelf – Vidovics Gábor, de maker van het programma.",
    "fb.message": "Bericht",
    "fb.message_ph": "Wat werkt, wat niet, wat ontbreekt?",
    "fb.meta": "Met je bericht worden meegestuurd: programmaversie {0}, besturingssysteem ({1}), taal van de interface ({2}).",
    "fb.name": "Naam",
    "fb.optional": "(optioneel)",
    "fb.privacy_hide": "Verklaring verbergen",
    "fb.privacy_text": (
        "Verwerkingsverantwoordelijke: Vidovics Gábor, particulier (Hongarije), de maker van Claude Usage Monitor. "
        "De volledige privacyverklaring staat op de website: https://claudeusagemonitor.com/#privacy\n\n"
        "Wat er wordt verzonden: wat je hier invult – naam (optioneel), e-mailadres (optioneel), bericht, "
        "sterrenbeoordeling – en, zodat ik de context kan begrijpen: de programmaversie, de naam en versie van het "
        "besturingssysteem, de taal van de interface en het tijdstip van verzending. De server slaat geen IP-adres op; "
        "om misbruik te voorkomen gebruikt hij alleen een dagelijks wisselende hash die niet tot een adres te "
        "herleiden is.\n\n"
        "Waarom: om je bericht te lezen en te beantwoorden en om het programma te verbeteren (gerechtvaardigd belang, "
        "art. 6 lid 1 onder f AVG; het antwoord zelf volgt op jouw verzoek). Je beoordeling en je naam verschijnen alleen "
        "op de website als je daarvoor het aparte vakje aanvinkt (toestemming, art. 6 lid 1 onder a AVG), en pas nadat "
        "de maker ze heeft gecontroleerd; je kunt die toestemming op elk moment intrekken.\n\n"
        "Hoe lang: berichten maximaal 2 jaar; een gepubliceerde beoordeling totdat je je toestemming intrekt. Als de "
        "maker het doorsturen per e-mail heeft ingeschakeld, komt een kopie ook in de mailbox van de maker terecht.\n\n"
        "Wie het kan zien: alleen de verwerkingsverantwoordelijke en – als verwerker – de hostingprovider (server in de EU, "
        "Duitsland). Er wordt niets verkocht of doorgegeven; er vindt geen profilering en geen geautomatiseerde "
        "besluitvorming plaats.\n\n"
        "Je rechten: inzage, rectificatie, wissing, beperking van de verwerking, bezwaar, intrekking van toestemming en "
        "het indienen van een klacht bij een toezichthoudende autoriteit (in Hongarije: NAIH, naih.hu; in Nederland: "
        "Autoriteit Persoonsgegevens, autoriteitpersoonsgegevens.nl) of bij de toezichthouder in je eigen land. "
        "Contact: dit formulier of de website.\n\n"
        "Verzending: versleuteld (HTTPS/TLS) naar claudeusagemonitor.com. Versie van deze verklaring: 6 oktober 2026."
    ),
    "fb.privacy_title": "Privacyverklaring",
    "fb.publish": "Mijn beoordeling en mijn naam (indien opgegeven) mogen op claudeusagemonitor.com worden getoond.",
    "fb.rating": "Algemene beoordeling",
    "fb.rating_clear": "wissen",
    "fb.rating_hint": "optioneel – klik op een ster",
    "fb.rating_tip": "{} van 5",
    "fb.secure": "Versleutelde verbinding (HTTPS) met claudeusagemonitor.com.",
    "fb.send": "Verzenden",
    "fb.sending": "Verzenden…",
    "fb.sent": "Bedankt – je bericht is aangekomen!",
    "fb.sent_sub": "Ik lees elk bericht. Als je een e-mailadres hebt opgegeven, antwoord ik je per e-mail.",
    "fb.title": "Bericht aan de ontwikkelaar",
    # context menu + Settings
    "menu.feedback": "Bericht aan de ontwikkelaar…",
    "set.show_feedback_icon": "Berichtpictogram in de kop van het paneel",
}

# macOS wording: nothing of the new keys differs on macOS; the four mac keys are inline in i18n_mac.py
STRINGS_MAC = {}
