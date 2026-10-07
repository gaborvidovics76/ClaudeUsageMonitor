# REVIEW – suomi (fi)

`claude_usage/langs/fi.py`: 358/358 keys + 4 `STRINGS_MAC`, `check_i18n.py fi` → OK.
Remaining warnings are correct as they are: `{}h`, `{} h`, ` h`, ` s` (SI units), `5H`, `Neon`.

Form of address: **sinä** (imperatives, "Sinulla on uusin versio"). Privacy document: **Tietosuojaseloste**.

## Least-certain texts (≤ 10)

| # | Key | Finnish | Why unsure |
|---|---|---|---|
| 1 | `panel.five_hour` | `5 H:N ISTUNTO` | Correct Finnish (abbreviation + genitive colon), but the natural `5 TUNNIN ISTUNTO` is 2 characters longer than the English and breaks the panel length rule. A reviewer may prefer `ISTUNTO 5 H`. |
| 2 | `panel.updated` | `haettu: {}` | `{}` is the data *age* ("5 min"), not a clock time; `päivitetty: {}` is 3 chars longer and `{} sitten` breaks with `time.none` ("ei dataa"). "haettu" = fetched. |
| 3 | `panel.pace` | `tahti {}` | Word order flipped ("tahti +12%") – `{} vs tahti` is understandable but un-Finnish and longer. |
| 4 | `panel.full_in`, `panel.retry_in`, `panel.reset`, `panel.no_data`, `panel.per_hour`, `time.hm`, `time.m` | `täynnä {}`, `uudelleen {} s`, `nollaus {}`, `Ei dataa`, `{} %/h`, `{}h {}min`, `{}min` | 1–2 characters longer than English (Finnish words are long; `%` needs a space; minute must be `min`, `m` = metre). Please check on the real panel at the smallest size. |
| 5 | `fb.consent` | `Olen lukenut ja hyväksyn: {}.` | The placeholder receives "Tietosuojaseloste" in the nominative; "Olen lukenut tietosuojaselosteen" would need the genitive, so a colon construction is used (same solution as the Hungarian). |
| 6 | `menu.click_through` / `set.click_through` | `Läpinapsautus` | No established Microsoft Finnish term; the settings text explains it in parentheses. |
| 7 | `backup.task_event` | `tapahtuman yhteydessä` | Shown in the "next run" column for event-triggered tasks; Task Scheduler wording varies. |
| 8 | `profile.tier` | `Rajoitustaso: {}` | "Rate-limit tier" – no standard Finnish term; kept short and neutral. |
| 9 | `err.bad_token_resp` | `virheellinen vastaus tunnuksen päätepisteestä` | "token" rendered as "tunnus"; some developers would write "token-päätepisteestä". |
| 10 | `fb.privacy_text` | (whole notice) | Added "(Suomessa tietosuojavaltuutettu)" after "oman maasi valvontaviranomaiselle" (the brief allows naming the local authority when certain); version date localised to `6.10.2026`; hosting provider = "palvelintilan tarjoaja"; Art. references in Finnish statutory form ("6 artiklan 1 kohdan f alakohta"). Legal review recommended. |

## en / hu differences noticed (English followed)

- `fb.privacy_text`: hu links to `https://claudeusagemonitor.com/hu/#privacy`, en to `/#privacy` → kept the English URL (no Finnish page).
- `set.show_extra_usage`: en "(pay-as-you-go)", hu "(usage credits)" → followed English ("käytön mukaan laskutettava").
- `menu.help`: hu "Súgó (HELP)…" has an extra "(HELP)" → "Ohje…".
- `menu.locked`, `menu.panel_visible`: en are actions ("Lock position", "Show panel"), hu are states ("Pozíció rögzítve", "Panel látszik") → actions used.
- `set.notify_reset`: hu adds "(reset)" → not added.
- `notify.logout`: en "Switched to local source", hu "the panel switched…" → impersonal Finnish passive.
- `panel.five_hour_short`: en "5H", hu "5 ÓRA" → kept "5H" for length.
- `notify.reset_done` uses an em dash "—" in en, while other texts use "–" → kept the em dash as in English.

## Lektor

Independent native review (fi). Overall a solid translation: consistent sinä forms, passive in neutral status
messages, Microsoft terms (tehtäväpalkki, ilmoitusalue, Käynnistä-valikko, kakkospainike) and Apple terms
(valikkorivi, osoita toissijaisesti) correct, case endings after names correct (Anthropicin, OneDrivessa,
Nextcloudiin, Claude Coden, SHA-256:lla, claude.ai:ta). Privacy notice back-translated: every fact, article,
retention period, right and the URL kept. `check_i18n.py fi` → OK (only the expected unit/name warnings).

Changes:
- `help.disclaimer`: "ei Anthropicin tekemä eikä sen kanssa yhteistyössä" → "Anthropic ei ole tehnyt sitä, eikä se ole sidoksissa Anthropiciin" – "affiliated" = sidoksissa, not yhteistyö.
- `help.guide`: "– koko valikko." → "– koko valikko avautuu." – verbless fragment read unnatural.
- `help.guide`: "mittaria – Historia-ikkuna:" → "mittaria – avautuu Historia-ikkuna:" – same, parallel structure.
- `help.guide`: "Ctrl + hiiren rulla – suuremmaksi tai pienemmäksi." → "– suurenna tai pienennä." – dangling translative, now imperative.
- `notify.login_ok`: "palvelimen tiedot ovat tulossa" → "tiedot haetaan palvelimelta" – calque; neutral passive status.
- `profile.since`: "Jäsen alkaen: {}" → "Liittynyt: {}" – idiomatic "member since".
- `set.local_models_none`: "tämä ryhmä vain pysyy piilossa" → "tämä ryhmä jää vain piiloon" – unnatural word order.
- `set.local_models_path`: "Claude Coden lokikansio" → "Claude Code -lokikansio" – consistent with other Claude Code compounds.
- `set.show_extra_usage`: "(käytön mukaan laskutettava)" → "(käytön mukaan laskutettavat)" – number agreement with krediitit.
- `set.tray_max`: "Kumpi on suurempi" → "Suurempi kahdesta" – natural dropdown option wording.
- `set.backup_config`: "Varmuuskopioskriptin asetukset" → "Varmuuskopioskriptin asetustiedosto" – label of a file picker.
- `update.whats_new`: "Uutta" → "Mitä uutta" – Microsoft/app-store standard; glossary updated.

Still in doubt:
- `panel.five_hour` "5 H:N ISTUNTO": correct but slightly stiff in capitals; "5 TUNNIN ISTUNTO" would be ideal if the panel has 2 more characters. Check on the smallest panel size.
- `panel.model` "{} VIIKKO" ("FABLE VIIKKO") is terse; "{}-VIIKKORAJA" is clearer but too long for the panel.
- `panel.retry_in` "uudelleen {} s": understandable in context; "uusi yritys {} s" is clearer but 2 characters longer.
- `backup.cloud_only` "saatavilla vain verkossa": Microsoft Finnish OneDrive status wording for "online-only" not verified.
- `STRINGS_MAC` "Avaa kirjautuessa": kept per LANGUAGE-NOTES; Apple's own Finnish may read "Avaa sisäänkirjautuessa" – verify on a Finnish macOS.
- `menu.click_through` "Läpinapsautus": no established Microsoft term; explained in the settings text.
