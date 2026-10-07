# Review notes – Latvian (lv)

Checker: `check_i18n: OK` (358/358 keys, 4 mac keys). The 7 remaining warnings are unit symbols
(`5H`, `{}%/h`, ` h`, ` s`, `{} d`, `{}d {}h`, `{} h`) that are correct in Latvian.

Form of address: **jūs** (Microsoft/Apple/Google LV). Privacy document: **„Privātuma politika”**, GDPR → **VDAR**.

## Texts I am least sure about

1. **`panel.reset` – "atiest. {}"** – abbreviation of "atiestatīšana" to stay close to the English length
   ("reset {}"). Full alternatives ("atiestatīs pēc {}", "jauns pēc {}") are clearer but almost twice as long.
   A native reviewer should check whether "atiest." is understood at a glance on the panel.
2. **`panel.retry_in` – "vēlreiz pēc {} s"** (16 chars vs 13 in English). No natural shorter Latvian form
   found; check that it does not clip on the smallest panel size.
3. **`panel.updated` – "atjaunots: {}"** (+2 chars) and **`panel.full_in` – "pilns: {}"** (+1 char). Slightly
   longer than English; chosen for clarity.
4. **`panel.pace` – "temps {}"** – rendered as "temps +5%"; the English says "+5% vs pace". Shorter and
   idiomatic, but the word order differs from the English.
5. **`panel.model` – "{} NEDĒĻĀ"** (e.g. "FABLE NEDĒĻĀ") – "per week" construction instead of an adjective;
   Latvian has no short adjective for "weekly" that fits after a model name.
6. **`time.hm` / `time.m` – "{}h {}min" / "{}min"** – "m" is not a Latvian abbreviation for minutes, so "min" is
   used (per LANGUAGE-NOTES), two characters longer than the English.
7. **`backup.vault` / glossary – "glabātava"** for the Obsidian vault ("krātuve" is kept for remote storage).
   Obsidian has no Latvian UI, so there is no established term.
8. **Tokens – "tokeni" (`set.local_models_hint`)** for model output tokens; Microsoft LV uses "marķieris" for
   tokens (used here only for the OAuth token endpoint in `err.bad_token_resp`). In AI context Latvian
   tech media mostly say "tokeni".
9. **`fb.consent` – "Esmu izlasījis(-usi) un pieņemu dokumentu „{}”."** – gender-split form "(-usi)" is the
   usual Latvian form convention but slightly bureaucratic.
10. **`menu.click_through` / `set.click_through` – "Klikšķu caurlaidība"** – no standard Microsoft LV term;
    the parenthesis in the Settings text explains it.

## en / hu differences noticed

- `fb.privacy_text`: the English links to `https://claudeusagemonitor.com/#privacy`, the Hungarian to
  `/hu/#privacy`. Latvian follows the English (no `/lv/` page exists).
- `fb.privacy_text`: the version date is written in Latvian long form ("2026. gada 6. oktobris") instead of
  ISO 2026-10-06 – same fact, local format.
- `notify.logout`: English "Switched to local source." vs Hungarian "the panel switched…" – followed English.
- `menu.help`: Hungarian has "Súgó (HELP)…", English "Help…" – followed English ("Palīdzība…").
- `set.local_models_hint` / `set.local_models_none`: the English uses " - " as a dash; Latvian uses "–".

## Lektor

Native review (lv). Diacritics, "jūs" + -iet imperatives, Microsoft terms (Iestatījumi, uzdevumjosla,
paziņojumu apgabals, izvēlne Sākt) and VDAR were already correct throughout. Changes:

- panel.reset: "atiest. {}" → "atiestatīs pēc {}" – abbreviation not instantly understood; also reads right after notify.threshold
- panel.full_in: "pilns: {}" → "pilns pēc {}" – clearer countdown, matches panel.reset
- backup.cloud_only: "Momentuzņēmums OneDrive ir pieejams … lai to nevajadzētu lejupielādēt" → "Momentuzņēmums pakalpojumā OneDrive ir pieejams … lai tas nebūtu jālejupielādē" – ambiguous word order, smoother clause
- backup.uploaded_no / backup.uploaded_yes: "Augšupielādēts Nextcloud: …" → "Augšupielāde pakalpojumā Nextcloud: …" – uninflected name, odd participle
- dlg.intro: "savā claude.ai kontā savā pārlūkprogrammā (tur …" → "savā claude.ai kontā, izmantojot savu pārlūkprogrammu (tajā …" – doubled "savā" sounded clumsy
- fb.privacy_text: "publicētu vērtējumu – līdz …" → "publicēts vērtējums – līdz …" – case agreement with "ziņas"
- fb.privacy_text: "netiek veikta profilēšana un automatizēta lēmumu pieņemšana" → "netiek veikta ne profilēšana, ne automatizēta lēmumu pieņemšana" – correct negated coordination
- help.guide: "vai tas pietiks" → "vai ar to pietiks" – correct government of "pietikt"
- help.guide: "vaicā Anthropic serverim" → "dati tiek iegūti no Anthropic servera" – calque, wrong case
- help.free: "Bezmaksas uz visiem laikiem" → "Vienmēr bezmaksas" – natural Latvian phrasing
- help.moved: "novirza šeit" → "novirza uz šo vietni" – "šeit" is static location
- hist.stat_now: "Pašlaik nedēļā" → "Nedēļā līdz šim" – natural "current weekly" stat
- notify.logout: "Pārslēgts uz lokālo avotu." → "Tagad tiek izmantots lokālais avots." – subjectless participle sounded truncated
- notify.reset_done: "{}: atiestatīts — sācies …" → "{}: atiestatīšana – sācies …" – gender agreement with label; Latvian en dash
- notify.threshold: "{}: izlietoti {}%." → "{}: izlietoti {} %." – Latvian space before percent
- set.pick_file_title: "Izvēlieties lietojuma žurnālu" → "Izvēlēties lietojuma žurnālu" – dialog titles infinitive (glossary)
- set.show_burn: "(%/h, %/dienā)" → "(%/h, %/d)" – consistent units with panel
- STRINGS_MAC notify.autostart_off: "netiks atvērta, pierakstoties." → "netiks atvērta, kad pierakstīsieties." – comma rule; mirrors autostart_on
- glossary-lv.md: reset row (panel form now "atiestatīs pēc {}") and percent rule (space in notifications) updated.

Still in doubt:
- panel.reset "atiestatīs pēc {}" is about twice the English length; the panel fits text by shrinking the
  font, so it never clips, but check readability at the smallest size. Shorter fallback: "jauns pēc {}".
- fb.consent keeps the gendered "izlasījis(-usi)" – the standard Latvian form formula; no neutral wording that
  sounds natural.
- panel.updated "atjaunots: {}" kept (Latvian news sites use "Atjaunots" for updated timestamps), although the
  glossary term for program updates is "atjaunināt".
