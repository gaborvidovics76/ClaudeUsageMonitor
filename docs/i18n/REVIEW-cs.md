# REVIEW – Czech (cs), "Message to the developer" keys

Texts I am least sure about, and one consistency note.

1. **`fb.consent` – "Přečetl(a) jsem si {} a souhlasím s nimi."**
   Czech past tense is gendered; the bracketed "(a)" is the usual neutral form in Czech software
   ("Přečetl/a jsem"). "s nimi" (plural) is correct because the placeholder is "Zásady ochrany osobních údajů"
   (plural noun). If the placeholder ever becomes a singular title, this must change to "s ním/s ní".

2. **`fb.privacy_text` – supervisory authority.** I added the Czech authority as "v ČR: ÚOOÚ, uoou.gov.cz".
   The ÚOOÚ moved to the gov.cz domain in 2024 (uoou.cz redirects there). If the maintainer prefers no URL,
   drop ", uoou.gov.cz" – everything else stays valid. The URL of the full policy was kept as in the
   English (`/#privacy`), not the Hungarian (`/hu/#privacy`).

3. **`fb.privacy_hide` – "Skrýt zásady"** for "Hide the notice". Short, matches the document name; an
   alternative would be "Skrýt tento text".

4. **`fb.rating_clear` – "vymazat"** (lower-case, as the English "clear"). "Zrušit" would read as Cancel,
   "smazat" sounds like deleting a file; "vymazat" is the usual word for clearing a selection.

5. **Form of address – vykání.** The existing Czech UI is overwhelmingly "vy" (notify.*, set.*, help.guide),
   so the new texts use "vy" too. Two inline strings (`set.backup_disclaimer`, `backup.disclaimer_short`)
   use "ty" ("tvé zálohy", "vyzkoušej") – they are inconsistent with the rest of the Czech UI and could be
   switched to "vy" in a later pass (not touched here, outside the task's scope).

en/hu difference noticed: hu `fb.email` is "E-mail-cím" (address), en is "E-mail"; the Czech label follows
the English ("E-mail"), the error text spells it out ("e-mailová adresa").

## Lektor

Form of address checked against the inline Czech (`Přihlaste se`, `Vyberte složku`, `váš účet`): vykání is
correct and kept. Back-translation of `fb.privacy_text`: all facts, articles, the 2-year period, the rights,
NAIH and the URL are present.

- fb.err_network: "Server claudeusagemonitor.com je nedostupný." → "Nepodařilo se spojit se serverem claudeusagemonitor.com." – cause may be local
- fb.err_server: "Server teď nemohl zprávu přijmout." → "Server teď nemůže zprávu přijmout." – tense with "teď"
- fb.intro: "Každou zprávu čtu já, Vidovics Gábor, autor programu." → "Každou zprávu čtu osobně – Vidovics Gábor, autor programu." – smoother, less calqued
- fb.privacy_text: "Správce:" → "Správce osobních údajů:" – full GDPR term first
- fb.privacy_text: "… hodnocení hvězdičkami –, a pro pochopení souvislostí:" → "… zpráva a hodnocení hvězdičkami – a dále, abych rozuměl souvislostem:" – wrong "–," punctuation, nominal style
- fb.privacy_text: "přečíst a zodpovědět vaši zprávu a zlepšovat … samotná odpověď na vaši žádost" → "přečíst vaši zprávu, odpovědět na ni a zlepšovat … samotnou odpověď posílám na vaši žádost" – verbless clause, double "a"
- fb.privacy_text: "pokud to zaškrtnete v samostatném políčku (souhlas, čl. 6 odst. 1 písm. a))" → "pokud to povolíte zaškrtnutím samostatného políčka (souhlas, čl. 6 odst. 1 písm. a) GDPR)" – "a))" unreadable, regulation named
- fb.privacy_text: "Doba uložení" → "Doba uchování" – GDPR Czech term (čl. 13)
- fb.privacy_text: "do autorovy e-mailové schránky" → "do jeho e-mailové schránky" – avoid repetition
- fb.privacy_text: "(v Maďarsku: NAIH, naih.hu; v ČR: ÚOOÚ, uoou.gov.cz) nebo u dozorového úřadu ve vaší zemi" → "(v Maďarsku: NAIH, naih.hu) nebo u dozorového úřadu ve vaší zemi (v ČR: ÚOOÚ, uoou.gov.cz)" – ÚOOÚ belongs to "your country"
- fb.privacy_text: "Přenos: šifrovaně …" → "Přenos: šifrovaný …" – adjective after heading noun
- fb.privacy_text: "Verze těchto zásad: 2026-10-06." → "Verze těchto zásad: 6. 10. 2026." – Czech date format (ČSN 01 6910)
- fb.publish: "(pokud je uvedu) se mohou zobrazit na claudeusagemonitor.com" → "(je-li uvedeno) se mohou zobrazit na webu claudeusagemonitor.com" – future tense was wrong
- fb.sent_sub: "Pokud jste uvedli e-mailovou adresu, odpovím vám na ni." → "Je-li vyplněna e-mailová adresa, odpovím na ni." – "jste uvedli" is colloquial vykání

Still in doubt:
- uoou.gov.cz – the ÚOOÚ domain since 2024 (uoou.cz redirects); verify before release if unsure.
- fb.consent "Přečetl(a) jsem si {} a souhlasím s nimi." – correct only while the title stays the plural
  "Zásady ochrany osobních údajů".
