# Review – Nederlands (nl): texts I am least sure about

1. **`fb.privacy_text` – form of address.** Dutch privacy statements are usually written with *u*, but
   the whole app (and this window) uses *je*. I kept *je* for one consistent voice and used the formal
   legal vocabulary of the AVG instead to carry the register. If the owner prefers *u* for the notice
   only, replace *je/jouw* with *u/uw* in that one text.

2. **`fb.privacy_text` – supervisory authority.** I named both NAIH (as in the English) and, in
   addition, the Autoriteit Persoonsgegevens for the Netherlands, and kept "de toezichthouder in je
   eigen land". Belgian (Flemish) users would turn to the Gegevensbeschermingsautoriteit; it is covered
   by the generic phrase, not named.

3. **`fb.privacy_title` = "Privacyverklaring" vs. existing `help.privacy` = "Privacybeleid".** Both are
   correct: the notice shown to the user is a *privacyverklaring*; the policy document on the website
   is a *privacybeleid*. `fb.err_consent` and `fb.privacy_hide` follow "privacyverklaring"/"verklaring".

4. **`fb.intro`** – "Een idee, een fout, of bevalt het je gewoon? Laat het me weten." is a free
   rendering of "An idea, a bug, or you simply like it? Tell me." The Hungarian adds "a program
   készítője" (the author of the program); I followed that ("de maker van het programma") since
   "de auteur" alone sounds odd in Dutch for software.

5. **`fb.meta`** – en/hu differ slightly: the English puts the version without brackets
   ("program version {0}") while Hungarian brackets all three. I followed the English.

## Lektor

Checked all 34 texts: *je* form (as in the inline `notify.*`, `set.*`, `dlg.*`), AVG vocabulary and citation,
every fact / article / period / URL in `fb.privacy_text` kept. "Privacyverklaring" confirmed (it is also the
footer link on claudeusagemonitor.com/nl/). 10 changes:

- fb.err_server: "De server kon het bericht nu niet aannemen." → "De server kan het bericht op dit moment niet ontvangen." – "aannemen" sounds like a parcel
- fb.intro: "Een idee, een fout, of bevalt het je gewoon? … Elk bericht wordt gelezen door mij, Vidovics Gábor, …" → "Een idee, een bug, of vind je het programma gewoon fijn? … Ik lees elk bericht zelf – Vidovics Gábor, …" – passive calque, missing subject
- fb.meta: "Wordt met het bericht meegestuurd:" → "Met je bericht worden meegestuurd:" – plural subject, word order
- fb.sent: "Bedankt – het is aangekomen!" → "Bedankt – je bericht is aangekomen!" – "het" had no referent
- fb.sent_sub: "Als je een e-mailadres hebt achtergelaten, antwoord ik daar." → "Als je een e-mailadres hebt opgegeven, antwoord ik je per e-mail." – "daar" unnatural
- fb.privacy_text: "Wat wordt verzonden" → "Wat er wordt verzonden" – Dutch needs "er"
- fb.privacy_text: "niet naar een adres is terug te herleiden" → "niet tot een adres te herleiden is" – pleonasm, wrong preposition
- fb.privacy_text: "het antwoord zelf op jouw verzoek" → "het antwoord zelf volgt op jouw verzoek"; "nadat de maker ze heeft beoordeeld" → "…gecontroleerd" – elliptical; clash with "beoordeling"
- fb.privacy_text: "Wie het ziet" → "Wie het kan zien"; "beperking, …, intrekking van toestemming, en" → "beperking van de verwerking, …, intrekking van toestemming en" – AVG term, no comma before "en"
- fb.privacy_text: "+ autoriteitpersoonsgegevens.nl"; "Transport:" → "Verzending:"; "2026-10-06" → "6 oktober 2026" – parallel to naih.hu; calque; Dutch date

Still in doubt: Belgian users are covered only by "de toezichthouder in je eigen land" (the
Gegevensbeschermingsautoriteit is not named) – acceptable. The full policy at the URL is English for Dutch visitors
(the site loads legal/en.html for all languages except Hungarian).
