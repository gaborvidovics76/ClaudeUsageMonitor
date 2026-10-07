# Glossary – Slovak (sk)

Scope: the whole UI of Claude Usage Monitor (`claude_usage/langs/sk.py`, 358 keys + 4 macOS keys).
A fresh Slovak localisation made from the English source (Hungarian consulted for intent only);
the Czech module of the project was deliberately not read or used – no Czech vocabulary, no „bohemisms"
(priečinok not zložka, údaje not data, pomocník not nápoveda, lišta not řádek, kontrolka not světlo).

## Tone and form of address

- **Friendly singular „ty" (tykanie)**, written in lowercase („ty", „tvoj", „svoj"). The program speaks in the
  first person of its author („Napíš mi", „Každú správu čítam ja") and the English is short, warm and
  confident – that is the voice of modern Slovak consumer apps (banking apps, Duolingo, indie tools), not the
  distant „vykanie" of corporate suites. Microsoft/Apple **terminology** is still used for everything the OS
  names (see the table); only the address is informal. One form everywhere, including the privacy notice
  (consistent with the Hungarian original, which also uses the informal form there).
- Gender-neutral phrasing wherever Slovak past tense or participles would force a gender („je na tebe",
  „bez prihlásenia", „ak je v správe e-mailová adresa", „či je vložený celý kód"); where unavoidable the
  standard form „Prečítal/a som si" is used (consent checkbox).
- Slovak typography: quotation marks „…", en dash with spaces for a pause „ – ", a space before „%" in
  running text („70 %", „využitých {} %"); compact panel/tray formats keep „{}%" to save space. Dates in the
  Slovak form „6. 10. 2026". Rhythmic law respected („tohtotýždňová", „čítam", „kontrolujem").
- Buttons and menu items use the infinitive as Microsoft SK does („Prihlásiť sa", „Zavrieť", „Obnoviť
  predvolené", „Nainštalovať teraz"); instructions use the 2nd-person imperative („Skontroluj", „Vyber",
  „Prilep sem kód").
- Plurals: Slovak has three forms (1 / 2–4 / 5+). Where a number is substituted, the sentence is built so
  that one form fits every count („Ponechané snímky: {}", „Súbory: {} ({})", „Nahrané v tomto behu – nové: {}…"),
  so no number ever needs a 1 / 2–4 / 5+ ending.

## Privacy document name

**Zásady ochrany osobných údajov** – the name every large platform uses in Slovak (Google, Microsoft, Apple,
Meta) and the wording Slovak websites put in their footers. „Oznámenie o ochrane osobných údajov" is a calque
seen on machine-translated sites; „Informácia o spracúvaní osobných údajov" is the formal Art. 13 GDPR name
used by authorities, but users recognise and expect „Zásady ochrany osobných údajov" on a link or a checkbox.
GDPR stays **GDPR** (the abbreviation is the everyday usage in Slovakia; the long name „všeobecné nariadenie
o ochrane údajov" is only used in statutes). Article citation in the Slovak style: **čl. 6 ods. 1 písm. f) GDPR**.
Supervisory authority: „dozorný orgán"; Slovak example added next to NAIH: **Úrad na ochranu osobných údajov
SR** (dataprotection.gov.sk) is added as the example for one's own country; „dozorný orgán vo vlastnej krajine"
is kept. The notice date is written the Slovak way („6. 10. 2026").

## Terms

| English | Slovak | Note |
|---|---|---|
| 5-hour session | 5-hodinová relácia | panel: 5-HODINOVÁ RELÁCIA; short: 5H; „relácia" = Microsoft SK for session |
| weekly limit | týždenný limit | panel: TÝŽDENNÝ LIMIT; short: TÝŽ. (standard abbreviation of „týždeň") |
| per-model weekly limit | týždenný limit modelu | „Týždenné limity ostatných modelov" |
| reset (of a limit) | reset / resetovať sa | established Slovak IT term; fits the tight panel („reset {}", „Odpočet do resetu") |
| pace | tempo | panel „tempo {}" („tempo +12%"); „k tempu" is a calque |
| burn rate | rýchlosť čerpania | „čerpanie" = drawing down a limit; „%/h, %/deň" |
| usage | využitie | „údaje o využití"; never the anglicism „usage" |
| usage credits | kredity na využitie | Anthropic's pay-as-you-go credits („platba podľa spotreby") |
| plan / plan badge | plán / odznak plánu | plan names (Pro, Max…) untouched |
| gauge | ukazovateľ | „Poradie ukazovateľov", „Ukazovateľ {}" |
| panel / widget | panel | one word for the floating window everywhere (also in the help) |
| history / stats | história / štatistiky | |
| projection / forecast | odhad | „Odhad na koniec týždňa" |
| peak | maximum | „Týždenné maximum" |
| data source | zdroj údajov | Microsoft SK „údaje", not the colloquial „dáta" |
| local log | lokálny záznam | „záznam" = log (Microsoft SK); „lokálny" for the this-PC source |
| log file | súbor záznamu | |
| this PC | tento počítač | |
| all devices | všetky zariadenia | |
| sign in / sign out | prihlásiť sa / odhlásiť sa | Microsoft SK; „prihlásenie na claude.ai" |
| session (sign-in) expired | platnosť relácie / prihlásenia vypršala | Microsoft SK wording |
| passkeys | prístupové kľúče | Apple/Google SK term |
| paste | prilepiť | Microsoft SK (Ctrl+V = Prilepiť) |
| tray / system tray | oblasť oznámení | Microsoft SK; „ikona v oblasti oznámení" = tray icon |
| taskbar | panel úloh | Microsoft SK |
| Start menu | ponuka Štart | Microsoft SK |
| menu | ponuka | context menu, Windows and macOS alike („… = ponuka", „v ponuke Štart") |
| menu bar (macOS) | lišta ponúk | Apple SK, binding per LANGUAGE-NOTES; „ikona v lište ponúk" |
| start at login (macOS) | Otvoriť pri prihlásení | Apple SK „Prihlasovacie položky" wording; notifications „sa otvorí / neotvorí pri prihlásení" |
| upload | nahrať / nahrané | Microsoft SK (OneDrive „Nahrať"); „Nahrané do Nextcloudu" |
| warning (in a list) | varovanie | „Chyby a varovania"; alert level „Varovanie" |
| endpoint | koncový bod | Microsoft SK |
| query / request | dopyt / požiadavka | „Chyba dopytu (HTTP {})", „obmedzuje počet požiadaviek" |
| Start with Windows | Spúšťať s Windowsom | short enough for the menu; notification: „spúšťa sa s Windowsom" |
| Settings | Nastavenia | Microsoft SK |
| notification (desktop) | oznámenie / oznámiť | Microsoft SK „Oznámenia"; checkbox verbs „Oznámiť, keď…" |
| alert (tab, colour levels) | upozornenie | tab „Upozornenia"; levels: Varovanie / Kritické |
| threshold | prah | „pri prekročení prahu" |
| stale data | zastarané údaje | |
| data freshness | aktuálnosť údajov | |
| refresh | obnoviť / obnovovanie | „Obnoviť údaje o využití teraz"; panel „obnovené: {}" |
| update (program) | aktualizácia / aktualizovať | „Aktualizácia programu", „Vyhľadať aktualizácie programu…" |
| download | stiahnuť / stiahnutie | „stránka na stiahnutie" |
| install | nainštalovať | |
| server | server | |
| backup / backups | záloha / zálohy | „priečinok záloh", „zálohovací skript" |
| backup status bar | stavový riadok záloh | |
| snapshot | snímka | |
| vault (Obsidian) | trezor | the usual Slovak Obsidian term; „Obsidian" stays |
| lamp (status light) | kontrolka | „Len kontrolky", „Kliknutím na kontrolku…" |
| scheduled task | naplánovaná úloha | Windows „Plánovač úloh" wording |
| folder | priečinok | Microsoft SK (never „zložka") |
| file | súbor | |
| profile / account | profil / účet | |
| theme | motív | Microsoft SK (Windows „Motívy") |
| layout | rozloženie | layouts: Lístok post-it, Úzky pásik, Kruhy |
| accent color | farba zvýraznenia | Windows SK |
| opacity | nepriehľadnosť | the slider sets opacity, not transparency |
| always on top | vždy navrchu | |
| click-through | prepúšťať kliknutia | „Prepúšťať kliknutia (len ozdoba, ignoruje myš)" |
| lock position | zamknúť polohu | |
| snap to screen edge | prichytávať k okraju obrazovky | |
| size | veľkosť | Malá / Normálna / Veľká / Extra |
| message to the developer | správa vývojárovi | dative, as Slovak says „napísať niekomu" |
| author | autor (programu) | |
| rating / overall rating | hodnotenie / celkové hodnotenie | „hodnotenie hviezdičkami" |
| optional | nepovinné | |
| privacy notice / policy | Zásady ochrany osobných údajov | see above |
| consent | súhlas | „odvolať súhlas" |
| controller / processor | prevádzkovateľ / sprostredkovateľ | Slovak GDPR terms (zákon č. 18/2018 Z. z.) |
| legitimate interest | oprávnený záujem | |
| supervisory authority | dozorný orgán | Slovak example: Úrad na ochranu osobných údajov SR |
| profiling / automated decision-making | profilovanie / automatizované rozhodovanie | |
| rights | prístup, oprava, vymazanie, obmedzenie spracúvania, namietanie | GDPR Art. 15–21 Slovak wording |
| hash | hash | established; „z ktorého sa adresa nedá spätne odvodiť" |
| encrypted connection | šifrované pripojenie | |
| terms of use | podmienky používania | |
| disclaimer | vylúčenie zodpovednosti | |
| help | Pomocník | Microsoft/Apple SK |
| quit | Ukončiť | |
| cancel / close | Zrušiť / Zavrieť | Microsoft SK |
| browse… | Prehľadávať… | Microsoft SK file-picker button |
| restore defaults / default | Obnoviť predvolené / Predvolené | |
| time units | s / min / h / d | „{} s", „{} min", „{} h", „{} d"; compact „{}h {}min", „{}d {}h"; never „m" for minute (= meter) |
| 5H / WEEK (tight panel) | 5H / TÝŽ. | same length as English; tray tooltip „5h: {}%   ·   Týž.: {}%" |
| per-model weekly label | {} TÝŽDEŇ | an adjective would need agreement with an unseen noun; the noun keeps the English length |
