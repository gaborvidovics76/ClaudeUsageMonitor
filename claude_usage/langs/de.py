# -*- coding: utf-8 -*-
"""Deutsch – UI strings of Claude Usage Monitor.

Only the keys that are NOT already inline in claude_usage/i18n*.py: the
"Nachricht an den Entwickler" window (fb.*), its menu item and its Settings checkbox.
Du-form, Microsoft terminology – consistent with the inline German texts.
"""

CODE = "de"
NAME = "Deutsch"

STRINGS = {
    # --- "Message to the developer" window -------------------------------------------------
    "fb.cancel": "Abbrechen",
    "fb.close": "Schließen",
    "fb.consent": "Ich habe die {} gelesen und akzeptiere sie.",
    "fb.email": "E-Mail",
    "fb.email_hint": "nur, wenn du eine Antwort möchtest",
    "fb.err_consent": "Zum Senden musst du die Datenschutzerklärung akzeptieren.",
    "fb.err_email": "Diese E-Mail-Adresse scheint ungültig zu sein.",
    "fb.err_empty": "Schreib zuerst eine Nachricht oder vergib eine Bewertung.",
    "fb.err_links": "Zu viele Links in der Nachricht.",
    "fb.err_network": "Keine Verbindung zu claudeusagemonitor.com. Prüfe deine Internetverbindung und versuche es erneut.",
    "fb.err_rate": "Zu viele Nachrichten in kurzer Zeit – bitte versuche es später noch einmal.",
    "fb.err_server": "Der Server konnte die Nachricht gerade nicht annehmen. Bitte versuche es später noch einmal.",
    "fb.intro": "Eine Idee, ein Fehler – oder gefällt dir das Programm einfach? Schreib mir. Ich lese jede Nachricht selbst – Vidovics Gábor, der Autor des Programms.",
    "fb.message": "Nachricht",
    "fb.message_ph": "Was funktioniert, was nicht, was fehlt?",
    "fb.meta": "Mit der Nachricht werden gesendet: Programmversion {0}, Betriebssystem ({1}), Sprache der Oberfläche ({2}).",
    "fb.name": "Name",
    "fb.optional": "(optional)",
    "fb.privacy_hide": "Hinweis ausblenden",
    "fb.privacy_text": (
        "Verantwortlicher: Vidovics Gábor, Privatperson (Ungarn), Autor von Claude Usage Monitor. "
        "Die vollständige Datenschutzerklärung findest du auf der Website: https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "Was übermittelt wird: was du hier eingibst – Name (optional), E-Mail-Adresse (optional), Nachricht, "
        "Sternebewertung – sowie, damit ich den Zusammenhang verstehe: die Programmversion, Name und Version des "
        "Betriebssystems, die Sprache der Oberfläche und der Zeitpunkt des Absendens. Der Server speichert keine "
        "IP-Adresse; zum Schutz vor Missbrauch verwendet er lediglich einen täglich wechselnden Hashwert, der sich "
        "nicht in eine Adresse zurückrechnen lässt."
        "\n\n"
        "Zweck: deine Nachricht zu lesen und zu beantworten sowie das Programm zu verbessern (berechtigtes "
        "Interesse, Art. 6 Abs. 1 lit. f DSGVO; die Antwort selbst erfolgt auf deine Anfrage). Deine Bewertung und "
        "dein Name erscheinen nur dann auf der Website, wenn du das gesonderte Kästchen dafür ankreuzt "
        "(Einwilligung, Art. 6 Abs. 1 lit. a DSGVO), und erst, nachdem der Autor sie geprüft hat; diese "
        "Einwilligung kannst du jederzeit widerrufen."
        "\n\n"
        "Speicherdauer: Nachrichten höchstens 2 Jahre; eine veröffentlichte Bewertung bis zum Widerruf deiner "
        "Einwilligung. Hat der Autor die E-Mail-Weiterleitung eingeschaltet, landet eine Kopie auch im Postfach "
        "des Autors."
        "\n\n"
        "Wer Zugriff hat: nur der Verantwortliche und – als Auftragsverarbeiter – der Hosting-Anbieter (Server in "
        "der EU, in Deutschland). Daten werden weder verkauft noch weitergegeben; es findet kein Profiling und keine "
        "automatisierte Entscheidungsfindung statt."
        "\n\n"
        "Deine Rechte: Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Widerspruch, Widerruf der "
        "Einwilligung sowie Beschwerde bei einer Aufsichtsbehörde (in Ungarn: NAIH, naih.hu) oder bei der "
        "Aufsichtsbehörde deines Landes. Kontakt: dieses Formular oder die Website."
        "\n\n"
        "Übertragung: verschlüsselt (HTTPS/TLS) an claudeusagemonitor.com. Stand dieser Erklärung: 06.10.2026."
    ),
    "fb.privacy_title": "Datenschutzerklärung",
    "fb.publish": "Meine Bewertung und mein Name (falls angegeben) dürfen auf claudeusagemonitor.com angezeigt werden.",
    "fb.rating": "Gesamtbewertung",
    "fb.rating_clear": "löschen",
    "fb.rating_hint": "optional – klicke auf einen Stern",
    "fb.rating_tip": "{} von 5",
    "fb.secure": "Verschlüsselte Verbindung (HTTPS) zu claudeusagemonitor.com.",
    "fb.send": "Senden",
    "fb.sending": "Wird gesendet…",
    "fb.sent": "Danke – deine Nachricht ist angekommen!",
    "fb.sent_sub": "Ich lese jede Nachricht. Wenn du eine E-Mail-Adresse angegeben hast, antworte ich dir per E-Mail.",
    "fb.title": "Nachricht an den Entwickler",
    # --- menu + Settings -------------------------------------------------------------------
    "menu.feedback": "Nachricht an den Entwickler…",
    "set.show_feedback_icon": "Nachrichtensymbol in der Kopfzeile des Panels",
}

# The four macOS-only texts already exist inline in i18n_mac.py for German.
STRINGS_MAC = {}
