# Review notes – Italian (it) – feedback window keys

Texts I am least sure about (the rest follows the glossary and the existing inline Italian).

1. **fb.consent** – `Ho letto e accetto l'{}.` The article is elided onto the placeholder because the
   title starts with a vowel (*l'Informativa sulla privacy*). If the privacy title is ever changed to a word
   starting with a consonant, the article must become `la {}` / `il {}`. The link text itself stays
   "Informativa sulla privacy" (without the article) – check that the apostrophe sits visually right
   before the underlined link.
2. **fb.intro** – "bug" kept as a loanword (`Un'idea, un bug o semplicemente ti piace?`). It is the normal
   word in Italian software; *errore* would also cover user mistakes. "Every message is read by me" was
   turned active (`Ogni messaggio lo leggo io personalmente`) – more natural, same meaning.
3. **fb.privacy_text** – the supervisory authority sentence names both the Hungarian NAIH (as in the English)
   and, as the local example, the Italian *Garante per la protezione dei dati personali*; "the authority of
   your own country" is kept as `all'autorità del tuo Paese`. The GDPR citation uses the Italian style
   `art. 6, par. 1, lett. f) GDPR`. The URL is the English one (`/#privacy`, not `/hu/#privacy`).
4. **fb.err_rate** – the English en dash was replaced by a colon (`Troppi messaggi in poco tempo: riprova
   più tardi.`), consistent with the colon style of the existing Italian texts (e.g. the backup disclaimer).
5. **fb.secure / privacy "Transport"** – *crittografata* (Microsoft term) rather than *cifrata* (the word the
   Italian GDPR text uses, "cifratura"). Both are correct; one was chosen for consistency.

No en/hu differences affecting the Italian were found, other than the HU-specific privacy URL (`/hu/#privacy`),
which the Italian does not use.

## Lektor

Checked all 34 texts against EN/HU: *tu* form (as in the inline `notify.*`, `set.*`, `dlg.*`), Italian GDPR
vocabulary, every fact / article / period / URL in `fb.privacy_text` kept. Document name "Informativa sulla
privacy" confirmed (same as `help.privacy` and claudeusagemonitor.com/it/). 10 changes:

- set.show_feedback_icon: "Icona messaggio nell'…" → "Icona dei messaggi nell'…" – no telegraphic noun pair
- fb.intro: "Un'idea, un bug o semplicemente ti piace? … Ogni messaggio lo leggo io personalmente, Vidovics Gábor, l'autore." → "Un'idea, un bug o semplicemente il programma ti piace? … Leggo personalmente ogni messaggio: sono Vidovics Gábor, l'autore." – missing subject, smoother apposition
- fb.sent: "Grazie – è arrivato!" → "Grazie, il tuo messaggio è arrivato!" – subject was unclear
- fb.sent_sub: "ti risponderò lì." → "ti risponderò via e-mail." – "lì" sounded unnatural
- fb.err_consent: "Per inviare, accetta…" → "Per inviare il messaggio, accetta…" – "inviare" needs an object
- fb.privacy_text: "l'ora dell'invio" → "la data e l'ora dell'invio" – "time of sending" = timestamp
- fb.privacy_text: "un hash … che non può essere ricondotto a un indirizzo" → "un'impronta (hash) … da cui non è possibile risalire all'indirizzo" – correct idiom, legal register
- fb.privacy_text: "art. 6, par. 1, lett. f) GDPR; la risposta stessa su tua richiesta" → "art. 6, par. 1, lett. f), del GDPR; la risposta in sé è fornita su tua richiesta" (same for lett. a) – Italian citation style; elliptical clause completed
- fb.privacy_text: "Chi li vede" → "Chi può vederli"; "fino alla revoca del consenso" → "…del tuo consenso" – closer to source
- fb.privacy_text: Garante + "garanteprivacy.it" added; "Versione …: 2026-10-06" → "6 ottobre 2026" – parallel to naih.hu; Italian date format

Still in doubt: none of substance. The full policy linked by the URL is currently English for Italian visitors (the
site loads legal/en.html for every language except Hungarian); the notice does not claim otherwise.
