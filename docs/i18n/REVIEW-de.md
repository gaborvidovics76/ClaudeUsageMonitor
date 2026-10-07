# REVIEW – Deutsch (de), Fenster „Nachricht an den Entwickler"

Texte, bei denen eine zweite Meinung sinnvoll ist (max. 5).

1. **`fb.privacy_title` – „Datenschutzerklärung"** statt „Datenschutzhinweis". Gewählt, weil es der
   gebräuchliche Name in deutscher Software und auf Websites ist und zum Checkbox-Satz passt
   („Ich habe die Datenschutzerklärung gelesen und akzeptiere sie."). Wer den In-App-Text strikt als
   Kurzfassung der Website-Erklärung sehen will, könnte „Datenschutzhinweise" (Plural) bevorzugen –
   `fb.consent` funktioniert dann unverändert („… gelesen und akzeptiere sie."), `fb.err_consent`
   müsste angepasst werden.

2. **`fb.privacy_text` – URL.** Beibehalten wie im Englischen (`https://claudeusagemonitor.com/#privacy`).
   Das Ungarische verweist auf `/hu/#privacy`; gibt es eine deutsche Seite (`/de/#privacy`), bitte
   die URL im Modul anpassen.

3. **`fb.privacy_text` – Datum.** „Stand dieser Erklärung: 06.10.2026" – deutsches Datumsformat und
   das übliche Wort „Stand". Wenn das Datum maschinell verglichen wird, auf ISO (2026-10-06) zurückstellen.

4. **`fb.privacy_hide` – „Hinweis ausblenden".** Bewusst nicht „Datenschutzerklärung ausblenden"
   (zu lang für den Link, EN hat 15 Zeichen). „Hinweis" bezieht sich hier auf den eingeblendeten
   Textkasten, nicht auf den Dokumenttitel.

5. **`fb.rating_clear` – „löschen".** Kleiner Link neben den Sternen; „zurücksetzen" wäre genauer,
   aber mehr als doppelt so lang wie „clear". Falls Platz ist: „zurücksetzen".

Unterschiede EN/HU: keine inhaltlichen. HU nutzt „nem kötelező" (nicht verpflichtend) für
„optional"; im Deutschen ist „(optional)" die Formularkonvention. Die Warnungen des Checkers für
„Name", „E-Mail" und „(optional)" sind beabsichtigt (die deutschen Wörter sind identisch).

## Lektor

Geprüft: alle 34 Texte, du-Form (wie `dlg.*`, `err.*` inline), DSGVO-Zitierweise, alle Fakten/Fristen/URL
in `fb.privacy_text` (vollständig, nichts hinzugefügt). Name des Dokuments „Datenschutzerklärung" bestätigt
(so auch auf claudeusagemonitor.com/de/). 6 Änderungen:

- fb.err_empty: „…oder wähle eine Bewertung." → „…oder vergib eine Bewertung." – idiomatische Kollokation
- fb.err_network: „claudeusagemonitor.com ist nicht erreichbar. Prüfe deine Verbindung…" → „Keine Verbindung zu claudeusagemonitor.com. Prüfe deine Internetverbindung…" – kein Satzanfang mit Kleinbuchstaben
- fb.intro: „Eine Idee, ein Fehler, oder es gefällt dir einfach? … Jede Nachricht lese ich persönlich – …" → „Eine Idee, ein Fehler – oder gefällt dir das Programm einfach? … Ich lese jede Nachricht selbst – …" – Komma vor „oder" falsch, Wortstellung
- fb.privacy_text: „geht eine Kopie auch in das Postfach" → „landet eine Kopie auch im Postfach" – natürlicher
- fb.privacy_text: „Wer sie sieht: … (Server in der EU, Deutschland). Nichts wird verkauft oder weitergegeben" → „Wer Zugriff hat: … (Server in der EU, in Deutschland). Daten werden weder verkauft noch weitergegeben" – Bezug von „sie" unklar
- fb.sent_sub: „antworte ich dir dort." → „antworte ich dir per E-Mail." – „dort" klang holprig

Offen: „Stand dieser Erklärung: 06.10.2026" bleibt im deutschen Datumsformat (der Code vergleicht nur
`CONSENT_VERSION` in feedback.py, nicht den Text). Die vollständige Erklärung auf der Website ist für
nicht-ungarische Sprachen derzeit englisch (legal/en.html) – der Hinweis verspricht das nicht anders, ist also korrekt.
