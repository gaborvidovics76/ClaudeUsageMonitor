# Review – Svenska (sv)

Module: `claude_usage/langs/sv.py` · 358/358 keys + 4 macOS keys · `check_i18n.py sv` → OK
(17 warnings, all deliberate: unit symbols h/d/s, "5H", and the words Version, Layout, System,
Normal, Neon, "full", which are the correct Swedish words too).

## The ten texts I am least sure about

| # | Key | Swedish | Why it needs a look |
|---|---|---|---|
| 1 | `panel.five_hour` | 5-TIMMARSSESSION | 16 characters against the English 14. Prescribed by LANGUAGE-NOTES (binding), and there is no shorter natural Swedish form ("5 TIM. SESSION" looks broken). Check that it fits the narrowest panel layout. |
| 2 | `panel.reset` | nollst. {} | 10 vs 8 characters. "nollställs om 2h 10min" would be the natural phrase but is far too long; "reset" itself is an anglicism. Alternative if space allows: "nollställs {}". Some Swedish apps also use "återställs" – I kept that word for restoring settings. |
| 3 | `panel.week_short` / `tray.head` | VECKA / "Vecka: {}%" | One character longer than WEEK / Week. "V." is the Swedish week-number abbreviation but is too cryptic as a gauge label. |
| 4 | `time.m`, `time.hm` | {}min, {}h {}min | Two characters longer than the English. LANGUAGE-NOTES prescribe min; a bare "m" reads as metre in Swedish. If the compact layout overflows, "{}h {}m" is the fallback. |
| 5 | `panel.no_data` / `time.none` | Inga data | 9 vs 7 characters; the shortest natural Swedish ("Ingen data" is colloquial and longer). |
| 6 | `panel.updated` | hämtat: {} | Chosen instead of "uppdaterat: {}" to stay within the English length; pairs with `panel.refreshing` "hämtar data". With the local log source the data is read from a file, but "hämtat" still reads naturally. |
| 7 | `panel.full_in` | full: {} | Identical to the English (checker warning); it is the right Swedish word (the gauge is "full"). "full om {}" would be more idiomatic but longer. |
| 8 | `fb.privacy_text` | … (i Sverige: IMY, imy.se) | I kept the generic "tillsynsmyndigheten i ditt eget land" and added IMY as the Swedish example in brackets (Swedish-speaking users in Finland have Dataombudsmannens byrå, hence the generic phrase stays first). Legal basis written the Swedish way: "artikel 6.1 f i dataskyddsförordningen (GDPR)". "the reply itself at your request" → "själva svaret skickas på din begäran" – please confirm this reading. |
| 9 | `fb.consent` | Jag har läst och godkänner {}. | The inserted link text is "Integritetspolicy" (capitalised, as a document title). In running Swedish one would write "integritetspolicyn"; the link mechanism does not allow the definite form. |
| 10 | `set.backup_config` | Skriptets konfigurationsfil | The English "Backup script config" is cut short; I assumed it is a file path (it sits next to "Found: {}"). The literal "Konfiguration för säkerhetskopieringsskript" is very long. |

## en / hu differences noticed (English followed everywhere)

- `fb.privacy_text`: the Hungarian links to `/hu/#privacy`, the English to `/#privacy`. There is no
  Swedish page, so the Swedish text uses the English URL.
- `menu.locked`: hu "Pozíció rögzítve" (a state), en "Lock position" (an action) → "Lås position".
- `menu.help`: hu adds "(HELP)" → Swedish just "Hjälp…".
- `set.show_extra_usage`: en "(pay-as-you-go)", hu "(usage credits)" → "(betala per användning)".
- `detail.surface.oauth_apps`: hu "Külső alkalmazások" (external apps), en "Connected apps" → "Anslutna appar".
- `notify.logout`: hu "the panel switched to the local source", en "Switched to local source" →
  "Bytte till lokal datakälla."
- `set.notify_reset`: hu adds "(reset)" → not repeated in Swedish.
- `notify.reset_done`: the English uses an em dash "—"; Swedish typography uses a spaced en dash "–".

## Lektor

Independent native review. The translation was already good (correct Microsoft/Apple terms, consistent
"du", Swedish compounds and typography); the changes below remove calques and a few awkward phrasings.

- `notify.logout`: Utloggad. Bytte till lokal datakälla. → Utloggad. Nu används den lokala datakällan. – subjectless "Bytte" is a calque
- `notify.first_run`: …ikonen i meddelandefältet för menyn. → …ikonen i meddelandefältet för att öppna menyn. – "för menyn" unidiomatic
- `STRINGS_MAC notify.first_run`: …symbolen i menyraden för menyn. → …symbolen i menyraden för att öppna menyn. – same, macOS variant
- `dlg.paste_label`: Klistra in koden du fick här: → Klistra in koden som du har fått: – "här" attached to "fick" (ambiguous)
- `dlg.intro`: …sparade lösenord och nycklar → …sparade lösenord och lösennycklar – Apple term, unambiguous passkeys
- `set.theme_default`: Temats standard → Enligt temat – natural label on colour button
- `theme.claude`: Claude (varm mörk) → Claude (varmt mörkt) – agreement, like Windows "Mörkt"
- `set.refresh`: Uppdatering → Uppdateringsintervall – label of a seconds spinbox; avoids confusion with program update
- `fb.consent`: Jag har läst och godkänner {}. → Jag har läst och godkänner: {}. – bare linked title needs colon
- `set.backup_disclaimer`: …förlorade data eller någon annan skada. → …förlorade data eller skador av något slag. – "any damage", no added "other"
- `backup.legend`: Röd: äldre, eller ingen säkerhetskopia → Röd: äldre eller ingen säkerhetskopia – no comma before "eller"
- `help.guide`: den nollställs vid en fast tidpunkt varje vecka som hör till ditt konto → den nollställs varje vecka vid en fast tidpunkt som hör till ditt konto – relative clause attached to wrong noun
- `help.guide`: <i>429 / begränsad</i> → <i>429 / för många förfrågningar</i> – "begränsad" alone meaningless
- `help.guide`: Inga data – kontrollera Datakälla; med claude.ai, logga in igen. → …; använder du claude.ai, logga in igen. – calque of "with claude.ai"

Glossary updated: passkeys = lösennycklar; note on the `fb.consent` colon.

Back-translation of `help.guide`, `err.*`, `notify.*`, `fb.privacy_text`, `fb.intro`, `set.backup_disclaimer` and
`backup.disclaimer_short`: no shift of meaning or omission; every fact, article number (6.1 f, 6.1 a), retention
period, right and the URL of the privacy notice are present. Checker: `check_i18n: OK` (17 warnings, all
legitimate identical words/units).

### Still in doubt

- `panel.five_hour` 5-TIMMARSSESSION (16 vs 14 chars): kept because LANGUAGE-NOTES prescribe it and it matches
  `hist.legend_5h` / `set.tray_five`. The only shorter natural word, "5-TIMMARSPASS" (13), would need the whole
  file changed to "pass" and reads less clearly for a usage window – decide only if the label is clipped.
- `panel.reset` nollst. {} (10 vs 8), `panel.no_data` Inga data (9 vs 7), `time.m` / `time.hm` "min": no
  shorter natural Swedish form exists; check on the narrowest layout.
- `fb.privacy_text`: the bracket "(i Sverige: IMY, imy.se)" is an addition to the source; it is correct and
  harmless, but the maintainer may prefer to drop it for a strictly literal notice.
- `fb.consent`: if the colon form feels too formal, the alternative is "Jag har läst och godkänner {}." with the
  title as a proper name (common on Swedish sites, but grammatically weaker).
