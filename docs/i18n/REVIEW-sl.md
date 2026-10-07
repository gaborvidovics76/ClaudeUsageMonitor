# Review – Slovenian (sl)

Module: `claude_usage/langs/sl.py` – 358 / 358 keys + 4 macOS keys. `check_i18n.py sl` → OK (6 warnings, all
correct: SI unit symbols `h`, `s`, `d`, `%/h` and the theme name "Neon" are the same in Slovenian).
Form of address: **vikanje** (vi). Privacy document: **Politika zasebnosti**. See `glossary-sl.md`.

## The 10 texts I am least sure about

| # | Key | Slovenian | Why unsure |
|---|---|---|---|
| 1 | `fb.consent` | Prebral/-a sem dokument {} in ga sprejemam. | The link inserts the title in the nominative ("Politika zasebnosti"); "dokument {}" keeps the case correct, but the gendered past tense needs the "/-a" form. A native reviewer may prefer "Strinjam se z dokumentom {}" (neutral, but loses "read"). |
| 2 | `panel.pace` | tempo {} | Shorter and clearer than a calque of "vs" ("{} od tempa"). The code inserts a signed value ("tempo +12%"); check that it reads as a deviation, not as the pace itself. |
| 3 | `panel.reset` | ponast. {} | Abbreviation of "ponastavitev" to fit the panel; slightly bureaucratic. Alternative: "nova čez {}" (but ambiguous). |
| 4 | `panel.model` | {} TEDEN | "FABLE TEDEN" – the noun instead of a hanging adjective ("TEDENSKA" would need "omejitev"). |
| 5 | `panel.week_short`, `panel.five_hour_short` | TEDEN, 5 H | One character longer than the English (WEEK, 5H). "TED." / "5H" would fit but read worse. Please check on the slim-bar layout. |
| 6 | `time.dh`, `time.hm` | {} d {} h, {} h {} min | Slovenian typography (space between number and unit, "min" not "m") makes them 2–4 characters longer than the English `{}d {}h` / `{}h {}m`. |
| 7 | `detail.extra`, `profile.extra`, `set.show_extra_usage` | Dobroimetje za porabo | "Usage credits": "dobroimetje" is the established Slovenian word for prepaid credit (Skype, mobile operators); "krediti" would be an anglicism. Anthropic has no Slovenian UI to align with. |
| 8 | `set.show_surfaces` | Omejitve po storitvah (…) | "Per-surface" has no direct Slovenian equivalent; "po storitvah" (by service) describes Claude Code / connected apps best. |
| 9 | `fb.privacy_text` | …ali pri organu v vaši državi (v Sloveniji: Informacijski pooblaščenec). | I added the Slovenian authority as an example in parentheses (LANGUAGE-NOTES names it); the generic wording is kept. Remove the parenthesis if only the English facts may appear. Article citations in the form "člen 6(1)(f)". |
| 10 | `help.guide` (and the whole UI) | plošča | The English says both "widget" and "panel"; Slovenian uses "plošča" everywhere so the user meets one word ("pripomoček" means Windows 11 widgets). |

## en / hu differences noticed

- `fb.privacy_text`: the English link is `https://claudeusagemonitor.com/#privacy`, the Hungarian one `…/hu/#privacy`. The Slovenian text uses the English URL (no Slovenian page exists).
- `fb.privacy_text`: Hungarian says "I sell / pass on nothing" (1st person), English is passive. Slovenian follows the English ("Podatki se ne prodajajo in ne posredujejo naprej").
- `menu.locked`: English "Lock position" (an action), Hungarian "Pozíció rögzítve" (a state). Slovenian follows the English: "Zakleni položaj".
- `menu.panel_visible` / `set.visible`: Hungarian describes a state ("Panel látszik"); Slovenian uses the Windows-style checkbox command ("Pokaži ploščo", "Pokaži lebdečo ploščo"), in line with the English "Show panel".
- `set.show_extra_usage`: English adds "(pay-as-you-go)", Hungarian repeats "(usage credits)". Slovenian follows the English: "(plačilo po porabi)".
- `menu.help`: Hungarian "Súgó (HELP)…" contains the English word; Slovenian follows the English: "Pomoč…".

## Lektor

Native review (standard Slovenian, vikanje, Microsoft terminology). The translation was already solid: dual,
form of address and platform terms were correct throughout. 18 changes in 16 keys:

- `backup.cloud_only`: „…njegova vsebina ni prikazana, da ga ni treba prenesti.“ → „…vsebina ni izpisana, da ga ne bi bilo treba prenesti.“ – natural purpose clause, “listed”
- `backup.level_yellow`: Se stara → Zastareva – clitic cannot open label
- `backup.rc_nochange`: posodobljeno, ni česa kopirati → brez sprememb, ničesar ni treba kopirati – “posodobljeno” suggests updated
- `backup.storage`: Oddaljeni prostor za shranjevanje: … → Oddaljena shramba: … – Microsoft/OneDrive term, shorter
- `backup.zip_new`: Novi ali posodobljeni ZIP-i: {} → Nove ali posodobljene datoteke ZIP: {} – colloquial plural, Microsoft style
- `dlg.intro`: Prijavite se v svoj račun claude.ai v svojem brskalniku → Prijavite se v račun claude.ai v svojem brskalniku – double “svoj” removed
- `fb.err_consent`: Za pošiljanje morate sprejeti politiko zasebnosti. → Če želite poslati sporočilo, sprejmite politiko zasebnosti. – polite request, not command
- `fb.privacy_text`: „sam odgovor na vašo zahtevo“ → „odgovor sam pa na podlagi vaše zahteve“ – legal basis clearer
- `fb.privacy_text`: „označite posebno polje“ → „označite ločeno potrditveno polje“ – Microsoft term for checkbox
- `help.guide`: Preklopite ju v meniju → Med njima preklopite v meniju – switch between, not toggle
- `help.guide`: ali so se vaša načrtovana varnostna kopiranja zagnala → ali so se vaša načrtovana opravila varnostnega kopiranja zagnala – awkward plural of activity
- `hist.stat_now`: Trenutna tedenska → Tedenska poraba zdaj – hanging adjective sounded incomplete
- `menu.refresh`: Zdaj osveži podatke o porabi → Osveži podatke o porabi zdaj – command starts with verb
- `set.data_hint`: „meri samo ta računalnik in se osveži“ → „upošteva samo ta računalnik in se osvežuje“ – meaning and aspect fixed
- `set.rows_available`: počistite kljukico → odstranite kljukico – natural collocation
- `set.rows_none`: Ko jih bo, se bodo … → Ko jih bo začel pošiljati, se bodo … – elliptical clause was ungrammatical
- `theme.claude`: Claude (toplo temna) → Claude (topla temna) – adjective agreement
- `update.downloading`: Prenos… {} od {} → Prenašanje… {} od {} – Microsoft progress wording, consistent

Glossary updated: “getting old” = zastareva; added prenašanje…, shramba, datoteka ZIP.

### Still in doubt
- `panel.reset` „ponast. {}“ – the abbreviation reads bureaucratically, but no full word fits the panel; kept.
- `tray.head` „5 h: {} %   ·   Teden: {} %“ is 4 characters longer than the English because of the Slovenian
  space before % and in „5 h“; it is a tooltip, so kept for typographic correctness.
- `fb.consent` keeps the gendered „Prebral/-a sem…“; no fully neutral wording keeps “read and accept”.
- `fb.privacy_text` names the Slovenian authority in parentheses („v Sloveniji: Informacijski pooblaščenec“) –
  factually correct and allowed by the brief; remove if strictly only source facts may appear.
- GDPR article citations follow LANGUAGE-NOTES („člen 6(1)(f)“); Slovenian legal texts would normally write
  „točka (f) prvega odstavka 6. člena“ – acceptable in a UI, but noted.
