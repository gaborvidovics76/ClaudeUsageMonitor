# Glossary – Svenska (sv)

Covers every key of `source.json` (358 + 4 macOS). Module: `claude_usage/langs/sv.py`.

## Form of address and tone

- **du** everywhere (du / din / dig). This is the standard of Swedish consumer software (Windows,
  macOS, Google, Spotify, BankID). *Ni* would sound stiff and dated. The privacy notice keeps *du* as
  well – that is how Swedish privacy policies are written today (IMY's own guidance uses *du*) – and
  carries its legal register through the GDPR vocabulary instead (personuppgiftsansvarig,
  personuppgiftsbiträde, berättigat intresse, rättelse, radering, begränsning, invändning).
- Short, friendly, confident. Error texts: what happened, then what to do ("Det gick inte att …",
  "Försök igen senare."). No anglicisms where a Swedish word is the established one
  (säkerhetskopia, inställningar, aviseringar, mapp, server).
- Swedish compounds are written as one word (programversion, veckogräns, loggfil, användningsdata,
  nedladdningssidan). Hyphen only after a proper name, a digit or an abbreviation (Cowork-chattloggar,
  Claude Code-arbete, Post-it-kort, 5-timmarssession, Obsidian-valvet, ZIP-fil, claude.ai-konto).
- Swedish typography: a space before % in running text ("70 %", "{} % förbrukat"); on the tight
  panel and tray the compact "{}%" is kept. En dash "–" with spaces for parenthetical dashes (also
  where the English has " - " or "—"), Swedish quotation marks ”…” (both U+201D), decimal comma, dates
  in the ISO form 2026-10-06 (normal Swedish form).
- "data" is treated as plural, as in Microsoft's and the authorities' Swedish: "inga data",
  "data blir inaktuella".
- Windows words follow Microsoft's Swedish; the four macOS texts follow Apple's Swedish.

## Platform terms (Microsoft Svenska / Apple Svenska)

| English | Svenska | Note |
|---|---|---|
| sign in / sign out | logga in / logga ut | Microsoft and Apple; noun: inloggning |
| Settings | Inställningar | |
| notification / notify | avisering / avisera | Microsoft term; "meddelande" is reserved for the message to the developer |
| taskbar | aktivitetsfältet | Microsoft |
| system tray / notification area | meddelandefältet | Microsoft's name for the tray; tray icon = "ikonen i meddelandefältet" |
| status bar | statusfält | Microsoft |
| Start menu | Start-menyn | Microsoft spelling |
| folder | mapp | |
| update (program) | uppdatering / uppdatera | |
| download | ladda ned / nedladdning | Microsoft wording ("Nedladdningar"); "hämta" is kept for *fetching data* from the server ("hämtar data") |
| upload | ladda upp / uppladdad | |
| server | server, servern | |
| scheduled task | schemalagd aktivitet | Schemaläggaren calls them "aktiviteter" |
| endpoint | slutpunkt | Microsoft |
| browse… | Bläddra… | Microsoft |
| menu bar (macOS) | menyraden | Apple; its icon = "symbolen i menyraden" |
| start at login (macOS) | Öppna vid inloggning | Apple's wording for login items |
| click / right-click / double-click | klicka / högerklicka / dubbelklicka | |
| mouse wheel | skrollhjulet | Microsoft ("Ctrl + skrollhjulet") |
| browser | webbläsare | |
| passkeys | lösennycklar | Apple's Swedish term; unambiguous next to "lösenord" (bare "nycklar" could mean any key) |
| app (this program) | appen / programmet | "appen" in short notifications, "programmet" in help and legal text |

## Product and domain terms

| English | Svenska | Note |
|---|---|---|
| 5-hour session | 5-timmarssession | panel label: 5-TIMMARSSESSION (binding per LANGUAGE-NOTES); short: 5H |
| weekly limit | veckogräns | panel: VECKOGRÄNS; short: VECKA |
| per-model weekly limit | veckogräns per modell | panel: "{} VECKA" |
| limit | gräns | never "limit" |
| reset (noun / verb) | nollställning / nollställs | a counter is zeroed; panel abbreviation "nollst. {}"; "återställa" is reserved for restoring settings and backups |
| pace | takt | "{} vs takt" |
| burn rate | förbrukningstakt | "förbrukning" for the average burn |
| usage | användning | användningsdata, användningsfil, användningslogg |
| usage credits | användningskrediter | |
| pay-as-you-go | betala per användning | |
| gauge | mätare | "{}-mätare", modellmätaren |
| panel (the floating widget) | panelen | "widget(en)" only in the help text, where the English says widget |
| plan / plan badge | abonnemang / abonnemangsmärke | Pro / Max badges stay |
| rate-limit tier | begränsningsnivå | |
| data source | datakälla | |
| local log | lokal logg | |
| profile | profil | |
| theme | tema (pl. teman) | |
| layout | layout | Microsoft keeps "layout" |
| appearance | utseende | |
| history | historik | |
| projection / forecast | prognos | |
| peak | topp | |
| threshold | tröskelvärde | |
| alert (tab) | varningar | the Alerts tab = Varningar; set.warn = Varning, set.danger = Kritisk |
| backup | säkerhetskopia (pl. säkerhetskopior) | Microsoft; the process = säkerhetskopiering |
| backup script | säkerhetskopieringsskript | |
| lamp | lampa | the small status lights |
| snapshot | ögonblicksbild | Microsoft / VSS term |
| vault (Obsidian) | valv | |
| note | anteckning | |
| log / log file | logg / loggfil | |
| remote storage | fjärrlagring | |
| stale data | inaktuella data | notification title "Inaktuella data" |
| updated: {} (panel) | hämtat: {} | pairs with "hämtar data"; shorter than "uppdaterat" |
| data freshness | dataålder | |
| click-through | släpp igenom klick | |
| lock position | lås position | |
| snap to screen edge | fäst vid skärmkanten | |
| always on top | alltid överst | |
| accent colour | accentfärg | Microsoft |
| opacity | opacitet | |
| trend curve (sparkline) | trendkurva (sparkline) | |
| connected apps | anslutna appar | |
| per-surface | per yta | |
| message to the developer | meddelande till utvecklaren | |
| rating / overall rating / star rating | betyg / helhetsbetyg / stjärnbetyg | |
| clear (the rating) | rensa | |
| optional | valfritt | |
| Send / Sending… | Skicka / Skickar… | |
| Cancel / Close | Avbryt / Stäng | |
| e-mail address | e-postadress | form label "E-postadress" |
| author (of the program) | utvecklaren | "upphovsman" sounds like copyright law |
| terms of use | användarvillkor | |
| disclaimer | ansvarsfriskrivning | |
| telemetry | telemetri | |
| open source / source code | öppen källkod / källkod | |
| what's new / release notes | nyheter / versionsinformation | |
| time units | s · min · h · d | SI abbreviations: "{}h {}min", "{}d {}h", "{} s" |

## Privacy document name

`fb.privacy_title` = **Integritetspolicy**. This is the term Swedish websites and apps use for the
notice shown to the data subject, and the one IMY (Integritetsskyddsmyndigheten) uses in its
guidance; Apple, Google and Spotify use it too. Microsoft's own translation ("sekretesspolicy") is
an outlier in Swedish usage and would feel foreign here. `help.privacy` uses the same word,
`fb.consent` = "Jag har läst och godkänner: {}." (the link text "Integritetspolicy" is inserted; the
colon lets the bare document title stand, since the definite "integritetspolicyn" cannot be linked),
`fb.err_consent` refers to "integritetspolicyn", `fb.privacy_hide` = "Dölj policyn".

GDPR stays **GDPR**, introduced once as "dataskyddsförordningen (GDPR)". Articles are cited the
Swedish way: "artikel 6.1 f" / "artikel 6.1 a". The supervisory authority: "tillsynsmyndighet",
NAIH for Hungary (as in the English), the generic "tillsynsmyndigheten i ditt eget land" kept, with
IMY given as the Swedish example in brackets (Swedish-speaking users in Finland have a different
authority, so the generic phrase stays the main one).
