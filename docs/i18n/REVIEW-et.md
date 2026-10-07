# REVIEW – Estonian (et)

Module: `claude_usage/langs/et.py` – 358/358 keys + 4 macOS keys. `check_i18n: OK` (6 warnings, all correct:
SI symbols `h` / `s` and `5H` are the same in Estonian).
Form of address: **sina**. Privacy document: **Privaatsuspoliitika** (see `glossary-et.md`).

## The 10 texts I am least sure about

| # | Key | Estonian | Why unsure |
|---|---|---|---|
| 1 | `panel.reset` | `lähtestus {}` | Correct Microsoft term, but 4 characters longer than "reset {}". If the panel clips it, a shorter option is `lähtest. {}`; colloquial "reset" was avoided on purpose. |
| 2 | `panel.no_data`, `time.none` | `Andmeid pole` | 12 characters vs 7. Estonian has no shorter natural form; check that it fits the smallest panel size. |
| 3 | `panel.retry_in` | `uus katse {} s` | One character longer than English; "uuesti {} s pärast" is more natural but too long for the panel. |
| 4 | `panel.pace` | `{} vs tempo` | "vs" is understood in Estonian but is a loan; one character longer than English. Alternative: `{} tempost` (shorter, but ambiguous). |
| 5 | `time.hm`, `time.m`, `backup.age_m` | `{}h {}min`, `{}min` | Minutes kept as "min" because "m" is the metre in Estonian; two characters longer than English. |
| 6 | `help.title`, `menu.help` | `Spikker` | Microsoft Office term; many younger users would expect "Abi". Swap to "Abi" / "Abi…" if the maintainer prefers the everyday word. |
| 7 | `fb.privacy_title`, `help.privacy` | `Privaatsuspoliitika` | Andmekaitse Inspektsioon itself says "isikuandmete töötlemise teave". The consumer-web name was chosen because the user looks for it on a form (see the glossary). |
| 8 | `err.bad_token_resp`, `set.local_models_hint` | `tokeni`, `väljundtokenid` | Developer loanword; the official term "tõend" is unclear in this context. |
| 9 | `menu.click_through` / `set.click_through` | `Läbiklõpsatav` | No established Windows term; the settings hint explains it ("ainult kaunistus, hiirt eiratakse"). |
| 10 | `fb.privacy_text` | Andmekaitse Inspektsioon added | English names only NAIH plus "the authority of your own country". I added "(Eestis: Andmekaitse Inspektsioon, aki.ee)" as the local example, as the language notes allow. Remove it if the notice must match the English word for word. |

## Differences between English and Hungarian

- `fb.privacy_text`: the Hungarian URL is `https://claudeusagemonitor.com/hu/#privacy`, the English one has no language
  path. Estonian follows the English (`https://claudeusagemonitor.com/#privacy`) because the site has no Estonian page.
- `menu.help`: Hungarian is "Súgó (HELP)…", English is "Help…". Estonian follows the English (`Spikker…`).
- `menu.locked`: Hungarian is a state ("Pozíció rögzítve"), English an action ("Lock position"). Estonian follows the
  English (`Lukusta asukoht`).
- `panel.five_hour_short`: Hungarian is "5 ÓRA", English "5H". Estonian follows the English (`5H`).
- `set.show_extra_usage`: Hungarian has "(usage credits)" in brackets; English has "(pay-as-you-go)". Estonian follows the
  English (`kasutuspõhine tasu`).
- `notify.logout`: Hungarian says the *panel* switched to the local source; English says "Switched to local source".
  Same meaning; Estonian: "Kasutusel on nüüd kohalik allikas."

## Lektor

Independent native review, 2026-10-07. The translation was already solid (correct sina, Microsoft terms Sätted /
tegumiriba / teavitusala / Spikker / Loobu / Välju, no Finnish-isms found). 20 edits in 17 keys, mostly word order and calques.
`check_i18n: OK` afterwards.

- `dlg.err_ratelimit`: "…ja alusta siis ÜHTE uut sisselogimist brauseris värske koodiga." → "…ja proovi siis brauseris värske koodiga ÜKS kord uuesti sisse logida." – stiff partitive object, unnatural
- `dlg.hint1`: "Lõpuks saad koodi." → "Lõpus saad koodi." – "lõpuks" means eventually
- `dlg.intro`: "Logi oma claude.ai kontole sisse oma brauseris (seal töötavad … juba)." → "Logi oma brauseris claude.ai kontole sisse (sinu salvestatud paroolid ja pääsuvõtmed töötavad seal juba)." – double "oma", word order
- `dlg.open_browser`: "Ava sisselogimine brauseris" → "Ava sisselogimisleht brauseris" – one opens a page
- `fb.consent`: "Olen läbi lugenud ja nõustun: {}." → "Olen tutvunud dokumendiga {} ja nõustun sellega." – colon construction read machine-made
- `fb.intro`: "Idee, viga või lihtsalt meeldib? … loen läbi mina, …" → "Sul on idee, leidsid vea või programm lihtsalt meeldib? … loen läbi mina ise, …" – fragment had no subject
- `fb.message_ph`: "…mis on puudu?" → "…mis puudub?" – more idiomatic, parallel
- `help.disclaimer`: "ei ole seda loonud ega ole sellega seotud" → "ei ole seda loonud ega sellega seotud" – redundant second "ole"
- `help.guide` (weekly limit): "lähtestub sinu konto kindlal nädalaajal" → "lähtestub kord nädalas sinu kontole määratud ajal" – "nädalaaeg" is not a word
- `help.guide` (pace): "kui kiiresti limiiti kasutad" → "kui kiiresti limiiti kulutad" – matches "kulumiskiirus"
- `help.guide` (claude.ai): "aeglasemalt, kui server seda palub" → "harvemini, kui server seda palub" – frequency, not speed
- `help.guide` (local): "see teab ainult seda arvutit" → "see näeb ainult selle arvuti kasutust" – calque of "knows this PC"
- `notify.signin_needed`: "et näha jätkuvalt kõigi…" → "et ka edaspidi näha kõigi…" – natural word order
- `set.backup_disclaimer`: "sinu varunduse logisid – see ei tee, ei kontrolli" → "sinu varunduslogisid – see ei loo, ei kontrolli" – glossary compound; "loo" for make
- `set.backup_disclaimer`: "proovi aeg-ajalt taastamist" → "testi aeg-ajalt taastamist" – "proovi" read as "try restoring"
- `set.data_hint`: "värskendus toimub umbes iga 5 minuti järel" / "…lähtestusaegu ja värskendus on sagedasem" → "andmed värskenduvad umbes iga 5 minuti järel" / "…ja täpseid lähtestusaegu ning andmed värskenduvad sagedamini" – broken parallel list, nominal style
- `set.local_models_hint`: "– osa sinu enda kasutusest ja väljundtokenid, mitte osa limiidist. … mitte kunagi vestlust." → "– osakaal sinu enda kasutusest ja väljundtokenitest, mitte limiidist. … vestlusi mitte kunagi." – mixed cases, meaning blurred
- `set.reset_confirm`: "Kas soovid kindlasti taastada vaikesätted?" → "Kas soovid kindlasti vaikesätted taastada?" – Estonian verb-final word order
- `set.rows_none`: "Kui saadab, ilmuvad need siia ise." → "Niipea kui saadab, ilmuvad need siia automaatselt." – "as soon as" kept; "ise" odd for limits
- `set.tip`: "lohista paneeli vasaku nupuga, Ctrl+kerimine" → "lohista paneeli hiire vasaku nupuga, Ctrl + kerimine" – which button; spacing as in help.guide

Kept on purpose / still in doubt:
- `panel.retry_in` "uus katse {} s" (14 vs 13) and `tray.head` "…Nädal: {}%" (24 vs 23) stay one character over the
  English: no natural shorter Estonian form ("uuesti {} s" is unclear, "Näd" is not a used abbreviation).
- `panel.reset` "lähtestus {}" (value is a duration, e.g. "lähtestus 2h 15min") is 4 characters longer; no natural
  shorter form – check it on the smallest panel size. `panel.no_data` "Andmeid pole" likewise.
- `panel.five_hour` "5 H SEANSS" kept (shorter than English); "5-TUNNI SEANSS" would be more natural and exactly the
  English length if the panel allows it.
- `backup.files_size` "{} faili" is wrong for exactly 1 ("1 faili"); needs plural support in code to fix.
- `help.title` "Spikker" is correct Microsoft Estonian; "Abi" would suit younger users – maintainer's choice.
- `fb.privacy_text`: back-translated, all facts, Art. 6(1)(f)/(a), 2 years, rights, NAIH and URL present; the
  added "(Eestis: Andmekaitse Inspektsioon, aki.ee)" is a local example of "your own country's authority".
