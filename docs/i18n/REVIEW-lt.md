# Review notes – Lithuanian (lt)

Checker: `check_i18n: OK` – 358 / 358 texts + 4 macOS texts. The only warning (`set.sec_suffix` = " s") is
correct: "s" is the standard Lithuanian abbreviation for seconds.

Form of address: polite plural **jūs** (lowercase), as in Microsoft / Apple Lithuanian. Settings = **Parametrai**
(Windows 10/11 name). Privacy document = **Privatumo politika**.

## The 10 texts I am least sure about

| # | Key | Lithuanian | Why unsure |
|---|---|---|---|
| 1 | `panel.five_hour_short` | `5 VAL.` | 6 characters vs English `5H` (2). Lithuanian has no one-letter hour abbreviation ("h" is not read by ordinary users); `5 VAL.` is the shortest natural form. Check that it fits the compact layout. |
| 2 | `time.dh`, `time.hm` | `{} d. {} val.`, `{} val. {} min` | Correct VLKK abbreviations, but about twice as long as `{}d {}h`. If the panel clips them, the fallback would be dropping spaces (`2d. 4val.`), which looks wrong to a Lithuanian reader – rather widen the field. |
| 3 | `panel.model` | `{} SAVAITĖ` | "FABLE SAVAITĖ" (= Fable · week) – the adjective "weekly" (savaitinis) sounds bureaucratic in a label, and the genitive `{} SAVAITĖS` would look unfinished. 1 char longer than the English. |
| 4 | `panel.full_in` | `pilna po {}` | "full in 2 val." – the noun (gauge/limit) is implied, like the English/Hungarian. A more idiomatic but longer alternative: `išseks po {}` ("runs out in"). |
| 5 | `panel.pace` | `tempas {}` | Reads "tempas +12%"; the literal "{} nuo tempo" was longer and clumsier. Meaning (deviation from the even pace) relies on the help text. |
| 6 | `panel.reset` | `liko {}` | "time left" instead of a literal "reset {}"; the value is always a countdown (also in the tray and threshold notification), so "liko 2 val. 10 min" is the natural phrasing. |
| 7 | `fb.privacy_text` | (… savo šalies institucijai (Lietuvoje – Valstybinei duomenų apsaugos inspekcijai) …) | I added the Lithuanian supervisory authority (VDAI) as the local example of "the authority of your own country" – brief rule 10 allows it; remove the parenthesis if the legal text must match the English word for word. GDPR rendered as BDAR, "6 str. 1 d. f p." / "6 str. 1 d. a p.". |
| 8 | `fb.consent` | `Perskaičiau ir sutinku su {}.` | Works only because the instrumental of "politika" equals the nominative ("su Privatumo politika"). If `fb.privacy_title` ever changes, re-check the case. |
| 9 | `err.bad_token_resp` | `netinkamas žetono galinio taško atsakymas` | Technical message; "žetonas" is the Microsoft term for an auth token but the same word is used for model tokens elsewhere (`set.local_models_hint`). Users rarely see it. |
| 10 | `set.show_spark` | `Tendencijos kreivė (mini diagrama)` | "sparkline" has no fixed everyday Lithuanian term (Excel uses "mažosios diagramos"); "mini diagrama" is the clearest for non-Excel users. |

Also worth a glance: `backup.cloud_only` ("pasiekiama tik internete" for OneDrive online-only files – the exact
OneDrive LT wording may differ slightly), and `menu.autostart` / `notify.autostart_*` which quote „Windows“ as
Microsoft Lithuanian does, while all other product names stay unquoted.

## en / hu differences noticed (English followed)

- `fb.privacy_text`: the English URL is `https://claudeusagemonitor.com/#privacy`, the Hungarian points to `/hu/#privacy`. Used the English one.
- `fb.privacy_title` "Privacy Notice" vs `help.privacy` "Privacy policy" – in Lithuanian both are "Privatumo politika" (one name everywhere).
- `set.show_extra_usage`: English explains "(pay-as-you-go)", Hungarian repeats "(usage credits)". Followed the English: "(mokama pagal naudojimą)".
- `detail.surface.oauth_apps`: English "Connected apps", Hungarian "Külső alkalmazások" (external apps). Followed the English: "Prijungtos programos".
- `menu.locked`: English imperative "Lock position", Hungarian a state ("Pozíció rögzítve"). Followed the English.
- `menu.help`: Hungarian adds "(HELP)"; not carried over.
- `set.notify_reset`: Hungarian adds "(reset)"; not carried over.
- The Hungarian uses the informal "te"; English is neutral; Lithuanian uses "jūs" (local norm).

## Lektor

Overall: a solid translation – diacritics, "jūs", Microsoft terms (Parametrai, pranešimų sritis, užduočių juosta,
meniu „Pradžia“, prisijungti/atsijungti) and the BDAR notice were already correct. Back-translation of
`help.guide`, `err.*`, `notify.*`, `fb.privacy_text`, `fb.intro`, `set.backup_disclaimer`,
`backup.disclaimer_short`: no omission or shift of meaning; all facts, article numbers, 2-year retention, rights
and the URL are present. 16 changes:

- `backup.cloud_only`: „…nerodomas – kad jos…“ → „…nerodomas, kad jos…“ – „kad“ clause needs comma
- `backup.rc_nochange`: „viskas atnaujinta“ → „viskas naujausia“ – up to date, not updated
- `dlg.err_ratelimit`: „Serveris laikinai jus riboja.“ → „Serveris laikinai apribojo prisijungimą.“ – natural, less accusatory phrasing
- `dlg.intro`: „Prisijunkite prie savo claude.ai paskyros savo naršyklėje“ → „Prisijunkite prie claude.ai paskyros savo naršyklėje“ – removed double „savo“
- `fb.privacy_text`: „kopija pristatoma ir į…“ → „kopija patenka ir į…“ – idiomatic verb for mailbox
- `help.guide` (Įspėjimai): „Pasirinktinai – pranešimai, kai…“ → „Galima įjungti ir pranešimus, kai…“ – telegraphic calque made natural
- `help.guide` (Naujinimai): „tikrinamas SHA-256“ → „tikrinamas pagal SHA-256“ – missing preposition
- `help.guide` (Privatumas): „Prisijungimas … saugomas užšifruotas“ → „Prisijungimo … duomenys saugomi užšifruoti“ – a sign-in is not stored
- `hist.stat_now`: „Dabar per savaitę“ → „Dabartinė savaitė“ – stat caption, calque removed
- `notify.reset_done`: em dash „—“ → en dash „–“ – Lithuanian dash typography
- `notify.update`: „Galima programos versija {}.“ → „Galima įdiegti programos versiją {}.“ – „galima versija“ is calque
- `update.available`: „Galima versija {}.“ → „Galima įdiegti versiją {}.“ – same, consistent with notify
- `set.about`: „Programa tik užklausia Anthropic … duomenų ir nuskaito…“ → „Programa iš Anthropic gauna tik jūsų pačių naudojimo duomenis ir iš naujinimų serverio nuskaito versijos numerį.“ – awkward „užklausti“ government
- `set.backup_label`: „Užrašas šalia lemputės“ → „Tekstas šalia lemputės“ – „užrašas“ = Obsidian note (clash)
- `set.click_through`: „(…, pelė nepaisoma)“ → „(…, į pelę nereaguoja)“ – natural Lithuanian phrasing
- `update.restarting`: „programa netrukus pasileis iš naujo“ → „netrukus programa bus paleista iš naujo“ – „pasileis“ colloquial

Still in doubt:
- `panel.full_in` „pilna po {}“ – fine for the 5-hour gauge (sesija is feminine), but „išseks po {}“ would be more
  idiomatic if one more character fits.
- `panel.model` „{} SAVAITĖ“ – understandable next to „SAVAITĖS LIMITAS“, but not a perfect equivalent of „WEEKLY“.
- `panel.five_hour_short` „5 VAL.“ and `time.dh` / `time.hm` are longer than English – verify they are not clipped.
- `fb.privacy_text` names VDAI as the local authority (an addition allowed by the brief; correct name). Remove the
  parenthesis if the notice must match the English word for word.
- `err.bad_token_resp` „žetonas“: Microsoft LT sometimes uses „atpažinimo ženklas“ for security tokens; kept
  „žetonas“ for consistency with model tokens – rarely seen by users.
- `backup.cloud_only` „pasiekiama tik internete“ – exact OneDrive LT status wording not verified.
