# REVIEW – Gaeilge (ga)

Module: `claude_usage/langs/ga.py` (358 + 4 mac keys, `check_i18n: OK`; the only warnings are `set.sec_suffix` " s"
and `theme.neon` "Neon", which are correct in Irish). Glossary: `docs/i18n/glossary-ga.md`.

## The 10 texts I am least sure about

| # | Key | Irish | Why |
|---|---|---|---|
| 1 | `panel.weekly` | AN tSEACHTAIN | "Teorainn seachtaine" (the term used everywhere else) is 19 characters against 12; the panel gets "THE WEEK" with the Caighdeán caps rule (lowercase t-prefix). If the panel has room, "TEORAINN SEACHTAINE" is the exact form. |
| 2 | `panel.five_hour` | SEISIÚN 5 hUAIRE | 16 characters vs 14 in English (hu is 17). Grammatically right (h-prefix after 5, kept lowercase in capitals). Shorter fallback: "SEISIÚN 5U". |
| 3 | `panel.week_short` / `tray.head` | SEACHT. / "Seacht.: {}%" | No established 4-letter abbreviation of *seachtain*; "SEACHT" without the dot would read as the number seven, so the dot is needed. |
| 4 | `panel.model` | "{} · SEACHTAIN" | "OPUS WEEKLY" has no natural adjective-after-name equivalent ("OPUS SEACHTAINE" is odd); the separator form reads as a label. |
| 5 | `backup.*` "snapshot" | léargas | Used for the Obsidian vault snapshot ZIP. Microsoft Irish uses *léargas* for snapshot, but a reviewer may prefer "cóip phointe ama". |
| 6 | `dlg.intro` "passkeys" | eochracha rochtana | Microsoft/Google Irish rendering of *passkey* is not fully settled; "eochair rochtana" follows the access-key model of other Microsoft languages. |
| 7 | `time.*`, `backup.age_*` | u / nóim / l / s | Units as set by LANGUAGE-NOTES; "{}u {}nóim" is longer than "{}h {}m" – on a very tight panel "nóim" may be the widest token. |
| 8 | `fb.privacy_title`, `help.privacy` | Polasaí Príobháideachais | Chosen over "Ráiteas Príobháideachais" (used by the DPC and gov.ie) because it is the name Irish-language software and websites put on the link; one name everywhere (title, Help link, consent, error). Reasoning in the glossary. |
| 9 | `fb.privacy_text` | full notice | Legal register checked (rialaitheoir, próiseálaí, leas dlisteanach, léirscriosadh, srianadh, údarás maoirseachta, RGCS, "Airteagal 6(1)(f)"); authority kept generic ("údarás do thíre féin"). A legal reviewer should confirm "duine aonair príobháideach" for *private individual* and "hais" for *hash*. |
| 10 | `backup.uploaded`, `backup.files_size`, `backup.zip_summary`, `backup.snap_kept`, `backup.vault_changed`, `backup.zip_new` | "label: {}" phrasing | Irish nouns after numbers mutate by number (3 chomhad / 7 gcomhad / 20 comhad), which a `{}` cannot know; these texts are reworded as "Comhaid: {}" etc. Slightly less fluent than English but never wrong. |

## en / hu differences noticed

- `menu.help`: en "Help…", hu "Súgó (HELP)…" – followed the English ("Cabhair…").
- `menu.locked`: en "Lock position" (action), hu "Pozíció rögzítve" (state) – followed the English ("Glasáil an suíomh").
- `menu.panel_visible`: en "Show panel", hu "Panel látszik" (state) – followed the English.
- `set.show_extra_usage`: en "(pay-as-you-go)", hu "(usage credits)" – followed the English ("íoc de réir úsáide").
- `fb.privacy_text`: en links `https://claudeusagemonitor.com/#privacy`, hu `/hu/#privacy` – the English URL is kept (no Irish page exists).
- `fb.privacy_title`: en "Privacy Notice", `help.privacy` en "Privacy policy" – one Irish name for both (see #8).
- `notify.logout`: en "Switched to local source." (impersonal), hu "the panel switched…" – Irish uses the impersonal "Aistríodh go dtí an fhoinse áitiúil."

## Lektor

Independent native review (An Caighdeán Oifigiúil 2017, Microsoft Irish / tearma.ie). Mutations after articles,
prepositions, possessives and numbers checked throughout (incl. "5 hUAIRE", "AN tSEACHTAIN", "6 théama",
"24 huaire", "leis an bPolasaí", "am an tseolta", "an pholasaí"); "tú" consistent; privacy notice back-translated –
every fact, article number (6(1)(f), 6(1)(a)), the 2-year retention, rights, NAIH and the URL are present.

- `set.about`: "…ón bhfreastalaí nuashonraithe" → "…ó fhreastalaí na nuashonruithe" – meant "updated server", not "update server"
- `set.backup_details`: "Taispeánann an fhuinneog mionsonraí" → "Taispeánann fuinneog na mionsonraí" – "the details window", not "window shows details"
- `notify.first_run` (+ STRINGS_MAC): "sa chúinne ag barr ar dheis" → "sa chúinne uachtarach ar dheis" – standard Microsoft "top right"
- `backup.uploaded`: "{} athsholáthraithe" → "{} ionadaithe" – Microsoft term for replace
- `dlg.err_ratelimit`: "ag cur srian ort" → "ag cur sriain ort" – genitive object of verbal noun (as "ag cur teorann" in `err.rate_limited`)
- `hist.stat_forecast`: "Réamhaisnéis dheireadh na seachtaine" → "Réamhaisnéis go deireadh na seachtaine" – avoids disputed definite-genitive lenition
- `help.guide`: "tugann réamhaisnéis dheireadh na seachtaine" → "tugann an réamhaisnéis go deireadh na seachtaine" – same, consistent with stat label
- `help.guide`: "gach pacáiste … ní thagann siad ach ó" → "… ní thagann aon phacáiste ach ó" – number agreement with "gach"
- `fb.sent_sub`: "freagróidh mé ansin thú" → "freagróidh mé thú ar an seoladh sin" – "ansin" read as "then"
- `fb.intro`: "nó an maith leat an clár, díreach?" → "…, sin an méid?" – "díreach" tag sounded calqued
- `backup.cloud_only`: "ionas nach mbeidh ort é a íoslódáil" → "ionas nach gá é a íoslódáil" – impersonal, as English
- glossary: forecast example updated; added replace, top-right corner, update server.

Still in doubt:
- `panel.five_hour` "SEISIÚN 5 hUAIRE" is 2 characters longer than the English; kept (correct and clear), fallback "SEISIÚN 5U".
- `panel.pace` "{} vs luas": Irish has no settled abbreviation ("v." in sport); kept "vs" for the tight panel.
- `menu.check_update` / `update.checking` use Mozilla's "Lorg nuashonruithe"; the Windows Irish LIP says "Seiceáil le haghaidh nuashonruithe" – both are understood, kept the shorter one.
- `detail.local_header` "ROINNT NA SEACHTAINE SEO": acceptable for "split", but "MIONDEALÚ" (breakdown) would be less ambiguous if space allows.
- `backup.*` "léargas" for snapshot (see translator's #5) – kept.
