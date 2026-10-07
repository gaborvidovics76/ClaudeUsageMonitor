# Glossary – Slovenian (sl)

Scope: the whole UI of Claude Usage Monitor (all 358 keys of `source.json` + the 4 macOS keys).
Standard Slovenian (knjižna slovenščina), Microsoft Windows / Office Slovenian terminology for the
platform words, Apple-style wording for the four macOS texts.

## Form of address and tone

- **Vikanje (vi / vaš / prijavite se / kliknite)** in every sentence addressed to the user. This is what
  Microsoft (Windows, Office), Google, banks, the public administration and the big Slovenian web shops use;
  "ti" is reserved for games and some start-ups. Vikanje also sidesteps the gendered past participle in most
  places ("Odjavljeni ste", "ste prilepili").
- **Commands (buttons, menu items, checkbox labels) are short singular imperatives**, exactly as Windows does
  it in Slovenian: *Zapri, Prekliči, Pošlji, Prebrskaj…, Pokaži ploščo, Zakleni položaj, Namesti zdaj*.
  Group labels and window titles are nouns (*Nastavitve, Zgodovina, Varnostne kopije*).
- The author speaks in the 1st person singular where the English does ("Vsako sporočilo preberem jaz").
- Where a gendered form is unavoidable (a first-person past tense in a checkbox), the usual Slovenian form
  "Prebral/-a sem" is used; elsewhere the sentence is rephrased to stay neutral ("ime (če je navedeno)").
- Tone: short, friendly, confident. No calques; a sentence must read as if written in Slovenian first.
- Typography: Slovenian quotation marks „…“; a space before `%` in sentences (70 %), before units
  (5 h, 10 min); en dash with spaces for an aside (also where the English uses " - " or " — ");
  dates as 6. 10. 2026. Exception: on the tight floating panel (`panel.per_day`, `panel.per_hour`)
  `%` stays attached ("{}%/dan"), because the code itself builds the pace value without a space ("+12%").
- Time formats on the panel: "{} d {} h", "{} h {} min", "{} min", "{} s" – SI symbols with a space,
  which the Slovenian reader expects; one or two characters longer than the English at most.
- **Dual.** Wherever a runtime number precedes a noun, the text is phrased so the dual cannot go wrong:
  the noun comes first followed by a colon ("Št. datotek: {}", "nove: {}, zamenjane: {}, napake: {}"),
  or an abbreviated unit is used ("{} min", "{} h", "{} d"). Fixed numbers are inflected normally
  ("vsaki 2 minuti", "največ 2 leti").

## Sign in / sign out – why "Prijava / Odjava"

Microsoft's own Windows/Microsoft-account strings use **Vpis / Izpis** ("Vpišite se v Microsoftov račun");
for the OS logon it uses **Prijava** ("Odpri ob prijavi", "Prijavite se v Windows"). Everything else the
Slovenian user meets – Google, Meta, Apple's Slovenian pages, banks, e-uprava, every Slovenian web shop –
says **Prijava / Odjava**. The sign-in here happens on a website in the user's browser, and the macOS text is
"Odpri ob prijavi" (Apple), so "Prijava" is the term users expect and it keeps the four macOS texts
consistent with the rest. Verb forms: *prijavite se / odjavite se*; noun forms on buttons and menu items:
*Prijava / Odjava*; "Prijava v claude.ai" / "Odjava iz claude.ai".

## Privacy document name

**Politika zasebnosti** – confirmed. It is by far the most common name on Slovenian websites and in Slovenian
apps, and the term the Slovenian supervisory authority (Informacijski pooblaščenec, ip-rs.si) uses in its
guidance for the public. The alternatives are brand-specific: Microsoft says "Izjava o zasebnosti", Google and
Meta "Pravilnik o zasebnosti"; the strictly legal "Informacije o obdelavi osebnih podatkov" belongs to
contracts and forms, not to an app window. Used for `fb.privacy_title` and `help.privacy`; lower-case inside
a sentence ("sprejeti politiko zasebnosti"). GDPR: written out once as "Splošna uredba o varstvu podatkov
(GDPR)", then "GDPR"; article citations in the form "člen 6(1)(f)".

## Fixed terms

| English | Slovenian | Note |
|---|---|---|
| 5-hour session | 5-urna seja | panel: 5-URNA SEJA; short: 5 H |
| weekly limit | tedenska omejitev | panel: TEDENSKA OMEJITEV; short: TEDEN |
| per-model weekly limit | tedenska omejitev modela | |
| limit | omejitev | Microsoft term; never "limit" |
| reset (noun / verb) | ponastavitev / ponastaviti | panel abbreviation: ponast. |
| pace | tempo | panel: "tempo {}" (the code inserts a signed value, e.g. "tempo +12%") |
| burn rate | hitrost porabe | |
| usage | poraba | Microsoft: "poraba podatkov" |
| usage credits | dobroimetje za porabo | Microsoft: Skype "dobroimetje"; pay-as-you-go = plačilo po porabi |
| gauge | merilnik | |
| widget | plošča | the app's own widget is always called "plošča" (also in the help text), so the user meets one word; "pripomoček" is reserved for Windows 11 widgets |
| panel (the floating widget) | plošča | "lebdeča plošča" |
| gauge (menu) | merilnik {} | "Merilnik FABLE"; panel label for a model: "{} TEDEN" |
| tray / tray icon | območje za obvestila / ikona v območju za obvestila | Microsoft term for the notification area |
| taskbar | opravilna vrstica | |
| Start menu | meni Start | |
| menu bar (macOS) | menijska vrstica | |
| start at login (macOS) | Odpri ob prijavi | Apple: Login Items = "Elementi prijave" |
| start with Windows | Zaženi s sistemom Windows | Microsoft never declines "Windows" |
| sign in / sign out | prijava / odjava; prijavite se / odjavite se | see above |
| browser | brskalnik | |
| passkeys | ključi za dostop | Microsoft / Google term |
| notification | obvestilo | |
| alert / alerts tab | opozorilo / Opozorila | |
| warning / critical (levels) | Opozorilo / Kritično | |
| threshold | prag | "ob prekoračitvi praga" |
| backup (noun) | varnostna kopija | plural: varnostne kopije; the activity: varnostno kopiranje |
| backup status bar | vrstica stanja varnostnih kopij | |
| lamp (status light) | lučka | |
| snapshot | posnetek stanja | Microsoft term |
| vault (Obsidian) | trezor | |
| note (Obsidian) | zapisek | |
| scheduled task | načrtovano opravilo | Windows: Načrtovalnik opravil |
| upload / download | naložiti (naloženo) / prenesti (prenos) | kept apart deliberately |
| data source | vir podatkov | |
| local log | lokalni dnevnik | log = dnevnik, log file = dnevniška datoteka |
| this PC | ta računalnik | Windows Explorer: "Ta računalnik" |
| all devices | vse naprave | |
| profile / account | profil / račun | |
| plan / plan badge | paket / značka paketa | PRO, MAX… stay |
| theme | tema | |
| layout | postavitev | Microsoft term |
| settings | nastavitve | |
| update (program) | posodobitev | "Posodobitev programa" |
| version | različica | Microsoft term, not "verzija" |
| history | zgodovina | |
| projection / forecast | napoved | |
| peak | vrh | |
| message to the developer | Sporočilo razvijalcu | |
| rating / overall rating | ocena / skupna ocena | star rating = ocena z zvezdicami |
| clear (the rating) | počisti | not "izbriši" |
| privacy notice (document) | Politika zasebnosti | see above |
| consent | privolitev | GDPR Slovenian term; withdraw = preklicati |
| controller / processor | upravljavec / obdelovalec | GDPR terms |
| legitimate interest | zakoniti interes | |
| supervisory authority | nadzorni organ | SI: Informacijski pooblaščenec |
| hosting provider | ponudnik gostovanja | |
| hash | zgoščena vrednost | Microsoft term |
| profiling / automated decision-making | oblikovanje profilov / avtomatizirano sprejemanje odločitev | |
| rights | dostop, popravek, izbris, omejitev obdelave, ugovor | |
| encrypted connection | šifrirana povezava | |
| server | strežnik | |
| endpoint / token | končna točka / žeton | Microsoft terms |
| folder | mapa | |
| e-mail / e-mail address | e-pošta / e-poštni naslov | Microsoft term |
| opacity | neprosojnost | unambiguous for a 0–100 % slider |
| accent color | poudarna barva | Windows 11 term |
| snap to edge | pripni na rob | Windows: "pripenjanje" |
| click-through | prepuščanje klikov | |
| always on top | vedno na vrhu | |
| lock position | zakleni položaj | |
| header (of the panel) | glava | |
| disclaimer | omejitev odgovornosti | |
| terms of use | pogoji uporabe | |
| stale data | zastareli podatki | |
| fresh / getting old / outdated | sveže / zastareva / zastarelo | backup lamp levels (a label may not start with the clitic "se") |
| downloading… / checking… | prenašanje… / preverjanje… | Microsoft progress wording (verbal noun) |
| storage (remote) | shramba | Microsoft / OneDrive term |
| ZIP file | datoteka ZIP | not "ZIP-i" |
| time units | s · min · h · d | SI abbreviations, dual-proof |
| Quit / Cancel / Close | Izhod / Prekliči / Zapri | Windows wording |
