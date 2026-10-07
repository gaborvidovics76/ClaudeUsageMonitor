# Glossary – Lithuanian (lt)

Scope: the whole UI of Claude Usage Monitor (all 358 keys + the 4 macOS overrides). Target quality:
Microsoft / Apple Lietuvių UI. Diacritics (ą č ę ė į š ų ū ž) everywhere, also in UPPERCASE labels.

## Tone and form of address

- **Polite "jūs"**, lowercase, everywhere. This is what Microsoft, Apple, Google and every Lithuanian bank or
  e-shop use in their interfaces; the informal "tu" is practically unknown in Lithuanian consumer software and
  would read as unprofessional. Lowercase "jūs" (not the letter-style "Jūs") is the UI convention of Microsoft
  and Apple Lithuanian. The Hungarian source is informal ("te") – the English is neutral – so the register
  follows the English and the local norm.
- Instructions are plural imperatives ("Prisijunkite", "Patikrinkite", "Spustelėkite"); possessive is the
  reflexive "savo" wherever the subject is the user ("savo naršyklėje", "visuose savo įrenginiuose").
- The author speaks in the first person ("perskaitau aš", "Parašykite"). Short, friendly, confident.
- Product names stay as they are, uninflected and unquoted (Claude Desktop, claude.ai, OneDrive, Obsidian…).
  The single exception is the Microsoft convention „Windows“ in the two autostart texts, exactly as Windows
  itself writes "Paleisti kartu su „Windows“".
- Numbers: ranges with an en dash (10–15), dates in the ISO form the program uses (2026-10-06), "pvz." for e.g.
- Per cent: in prose with a space ("nuo 70 %"), as VLKK prescribes; in the tight panel/tray strings without a
  space ("{}%/val."), to match the "45%" the program itself draws next to them.

## Settings: "Parametrai" (Microsoft), not "Nustatymai" (Apple/Google)

The program is a Windows-first desktop app and the brief asks for Microsoft terminology for Windows things;
Windows 10/11 calls its Settings app **Parametrai**. "Nustatymai" is what Apple, Google and most web apps
use, so it would also be understood, but a Windows user sees "Parametrai" in the Start menu every day. One
word is used consistently: menu "Parametrai…", window title "parametrai", help text "rasite Parametruose".

## Privacy document name: "Privatumo politika"

**Privatumo politika** is the name every big platform uses in Lithuanian (Google, Microsoft, Apple, Meta),
the term the Lithuanian supervisory authority VDAI uses on its own site, and the term on Lithuanian e-shops.
"Privatumo pranešimas" (notice) exists in BDAR translations but is rare on links and checkboxes. The
consent line works grammatically because the instrumental of "politika" is identical to the nominative:
"Perskaičiau ir sutinku su Privatumo politika."

## Platform words

| English | Lithuanian | Source |
|---|---|---|
| sign in / sign out | prisijungti / atsijungti | Microsoft |
| signed in / not signed in | prisijungta / neprisijungta | Microsoft |
| Settings | Parametrai | Microsoft (Windows) |
| taskbar | užduočių juosta | Microsoft |
| notification area / tray | pranešimų sritis | Microsoft |
| tray icon | pranešimų srities piktograma | Microsoft |
| Start menu | meniu „Pradžia“ | Windows 11 |
| notification | pranešimas | Microsoft |
| folder / file | aplankas / failas | Microsoft |
| update (program) / to update | naujinimas / atnaujinti | Microsoft |
| server / download | serveris / atsisiųsti | Microsoft |
| this PC | šis kompiuteris | Microsoft ("Šis kompiuteris") |
| app / program | programa | one word for both |
| widget | valdiklis | Microsoft (Windows 11 "Valdikliai") |
| right-click | spustelėti dešiniuoju pelės mygtuku | Microsoft |
| double-click | dvikartis spustelėjimas | Microsoft |
| Help | Žinynas | Microsoft |
| Quit | Išeiti | Microsoft |
| Cancel / Close | Atšaukti / Uždaryti | Microsoft |
| Browse… | Naršyti… | Microsoft |
| Default / Restore defaults | Numatytasis / Atkurti numatytuosius | Microsoft |
| passkeys | prieigos raktai | Microsoft / Google |
| script | scenarijus | Microsoft |
| endpoint | galinis taškas | Microsoft |
| session (sign-in) | seansas | Microsoft |
| **macOS:** menu bar | meniu juosta | Apple |
| **macOS:** Open at Login | Atidaryti prisijungus | Apple |

## Product terms

| English | Lithuanian | Note |
|---|---|---|
| usage | naudojimas | "naudojimo duomenys", "naudojimo failas" |
| usage credits | naudojimo kreditai | |
| 5-hour session | 5 val. sesija | panel: 5 VAL. SESIJA; short: 5 VAL. |
| weekly limit | savaitės limitas | panel: SAVAITĖS LIMITAS; short: SAV. |
| per-model weekly limit | modelio savaitės limitas | |
| limit | limitas | not "riba" – that is the threshold |
| reset (a limit resets) | atsinaujina / atsinaujinimas | "limitas atsinaujina"; on the panel the countdown reads "liko {}" (time left) |
| countdown to reset | atgalinis skaičiavimas iki atsinaujinimo | |
| pace | tempas | panel: "tempas {}" → "tempas +12%" (deviation from pace; shortest unambiguous form) |
| burn rate | naudojimo sparta | "%/val., %/d." |
| full in (session) | pilna po {} | {} is a duration ("pilna po 2 val.") |
| automatic (path placeholder) | automatiškai | adverb: the folder is found automatically |
| Critical / Warning (threshold labels) | Pavojus / Įspėjimas | |
| message window term "notice" | privatumo politika | one name for the document everywhere, also in "Slėpti privatumo politiką" |
| projection / forecast | prognozė | |
| gauge | matuoklis | "Matuoklių tvarka", "{} matuoklis" |
| panel | skydelis | "Rodyti skydelį"; floating panel = slankusis skydelis |
| lamp (backup indicator) | lemputė | |
| threshold | riba | "peržengus ribą"; yellow/red labels: Įspėjimas / Pavojus |
| alerts (tab) | Įspėjimai | |
| notify / notification | pranešti / pranešimas | |
| stale data | pasenę duomenys | |
| data source | duomenų šaltinis | |
| local log | vietinis žurnalas | log = žurnalas, log file = žurnalo failas |
| backup | atsarginė kopija | Microsoft; "Atsarginės kopijos" (window, menu) |
| backup status bar | atsarginių kopijų būsenos juosta | |
| snapshot | momentinė kopija | Microsoft |
| vault (Obsidian) | saugykla | |
| note (Obsidian) | užrašas | |
| scheduled tasks | suplanuotos užduotys | Microsoft (Užduočių planuoklė) |
| profile | profilis | "Profilis / paskyra" |
| theme | tema | |
| layout | išdėstymas | layouts: Lipnus lapelis, Siaura juosta, Žiedai |
| size | dydis | Mažas / Įprastas / Didelis / Ypač didelis |
| accent color | akcento spalva | |
| opacity | nepermatomumas | Microsoft |
| always on top | visada viršuje | |
| lock position | užrakinti padėtį | |
| click-through | praleisti spustelėjimus | |
| snap to screen edge | pritraukti prie ekrano krašto | |
| plan badge | plano ženklelis | |
| connected apps | prijungtos programos | |
| per-surface limits | limitai pagal aplinką | |
| history | istorija | "Istorija ir statistika…" |
| what's new | kas naujo | |
| message to the developer | žinutė kūrėjui | message = žinutė (not "pranešimas", that is a notification) |
| rating / overall rating | įvertinimas / bendras įvertinimas | star = žvaigždutė |
| optional | neprivaloma | |
| privacy policy | Privatumo politika | see above |
| consent | sutikimas | "atšaukti sutikimą" |
| terms of use | naudojimo sąlygos | |
| disclaimer | atsakomybės apribojimas | |
| source code / open source | pirminis kodas / atvirasis kodas | VLKK |
| tokens (model) | žetonai | |
| encrypted | šifruotas | |

## Legal terms (BDAR)

| English | Lithuanian |
|---|---|
| GDPR | BDAR (Bendrasis duomenų apsaugos reglamentas) |
| Art. 6(1)(f) / Art. 6(1)(a) | 6 str. 1 d. f p. / 6 str. 1 d. a p. |
| controller | duomenų valdytojas |
| processor | duomenų tvarkytojas |
| hosting provider | prieglobos paslaugų teikėjas |
| legitimate interest | teisėtas interesas |
| supervisory authority | priežiūros institucija (Lietuvoje: VDAI) |
| access, rectification, erasure, restriction, objection | susipažinti su duomenimis, juos ištaisyti, ištrinti, apriboti jų tvarkymą, nesutikti su tvarkymu |
| profiling / automated decision-making | profiliavimas / automatizuotas sprendimų priėmimas |
| hash | maišos reikšmė |

## Time units (VLKK abbreviations)

s · min · val. · d. – e.g. "2 val. 15 min", "3 d. 4 val.", "{} s". These are the only abbreviations a
Lithuanian user reads instantly; "h"/"m" are not used in Lithuanian.
