# Glossary – Maltese (mt)

Scope: the whole UI of Claude Usage Monitor (358 keys + 4 macOS keys), module `claude_usage/langs/mt.py`.

## Tone and form of address

- **Friendly singular "int"** – 2nd person singular imperatives and verbs everywhere ("Idħol", "Iċċekkja",
  "erġa' pprova", "tiegħek"). This is how Maltese consumer software and the Maltese Windows LIP address the
  user; the plural/formal "intom" is never used.
- Short, confident sentences; the author speaks in the first person in the feedback window ("Għidli",
  "Naqra kull messaġġ"). Program status texts use the 3rd person masculine ("Qed jiċċekkja…", "jaġġorna");
  "l-app" is feminine ("l-app tibda", "terġa' tibda").
- Standard Maltese orthography: ħ ġ ż ċ, għ, ie; capitals Ħ Ġ Ż Ċ in UPPERCASE labels ("LIMITU TAL-ĠIMGĦA").
  The apostrophe of "ta'", "erġa'", "mtella'" is the straight ASCII apostrophe, as in Microsoft and
  government Maltese software. Article assimilation and euphonic "i" are applied ("s-Sors", "l-iskrin",
  "fl-Issettjar", "naċċetta l-Politika").
- Numerals: 2–10 + plural ("6 sigħat", "7 ijiem"), 11–19 + "-il" + singular ("10–15-il minuta"), 20+ +
  singular ("24 siegħa"). Where a placeholder hides the number, the noun is put before it with a colon
  ("Fajls: {}", "Snapshots miżmuma: {}") so the agreement can never be wrong.
- Technical loanwords as Maltese software, gov.mt and EU Maltese translations use them: backup(s), browser,
  login, server, log(s), hash, widget, app(s), snapshot, token, taskbar, menu bar, badge.

## Privacy document name

**Politika tal-Privatezza** – for `fb.privacy_title` ("Privacy Notice") and `help.privacy` ("Privacy
policy"). This is the name used by Maltese government portals, the Maltese versions of the large platforms
and the Information and Data Protection Commissioner (IDPC) for the public privacy document. "Avviż ta'
privatezza" is the narrower GDPR-technical term, but on a link and a consent checkbox Maltese users expect
"Politika tal-Privatezza". Because "P" is not a sun letter, the article before it is "il-"/"l-"
("naċċetta l-Politika tal-Privatezza"), which makes `fb.consent` ("Qrajt u naċċetta l-{}.") grammatical.
GDPR keeps its name (Regolament Ġenerali dwar il-Protezzjoni tad-Data); articles are cited as
"Artikolu 6(1)(f) tal-GDPR", as in the Maltese text of Regulation (EU) 2016/679. Supervisory authority stays
generic ("l-awtorità tal-pajjiż tiegħek"); in Malta that is the IDPC.

## Settings

**Issettjar** ("Issettjar…", "fl-Issettjar", "il-folder tal-issettjar", window title "issettjar"). This is
the Microsoft Maltese terminology for "settings" (Windows Maltese LIP: "Issettjar tal-PC"). It is a
collective noun, so it is used in the singular with the article ("l-issettjar prestabbilit").
"Konfigurazzjoni" is kept for a configuration file of a script.

## Terms

| English | Maltese | Note |
|---|---|---|
| usage / usage data | użu / data tal-użu | "data" (not "dejta"), as on gov.mt and in the GDPR Maltese text; feminine ("id-data tqadem") |
| 5-hour session | sessjoni ta' 5 sigħat | panel label (tight): SESSJONI TA' 5H |
| mailbox (e-mail) | kaxxa tal-email | not "kaxxa postali" (= post-office box) |
| weekly limit | limitu tal-ġimgħa | panel label: LIMITU TAL-ĠIMGĦA |
| per-model weekly limit | limitu tal-ġimgħa għal kull mudell | |
| model | mudell | |
| reset (noun) / resets (verb) | reset / jerġa' jibda | "ir-reset", "għadd lura sar-reset" |
| pace | ritmu | panel: "{} vs ritmu"; "pass" is kept for "step" |
| step (dialog) | pass | "Pass 1", "Pass 2" |
| burn rate | rata ta' konsum | |
| gauge | indikatur | "Indikatur {}" |
| panel | pannell | |
| widget | widget | |
| tray / notification area | żona tan-notifiki | "l-ikona fiż-żona tan-notifiki" |
| taskbar | taskbar | Microsoft Maltese keeps it ("fit-taskbar") |
| Start menu | il-menu Start | |
| menu bar (macOS) | menu bar | STRINGS_MAC only |
| start at login (macOS) | Iftaħ mal-login | STRINGS_MAC only |
| start with Windows | Ibda ma' Windows | |
| sign in / sign out | Idħol / Oħroġ | "Idħol f'claude.ai", "Oħroġ minn claude.ai" |
| sign-in (noun) | login | "il-login ta' claude.ai skada" |
| browser | browser | |
| paste | waħħal | reserved for the clipboard; snapping uses "jeħel" |
| notification | notifika (pl. notifiki) | |
| alert (tab) | allert (pl. allerti) | |
| warning / critical (thresholds) | twissija / kritiku | |
| threshold | livell | "meta jinqabeż livell"; "limitu" is reserved for the usage limit |
| notify | avża | "Avża meta…" |
| backup (noun) | backup (pl. backups) | the everyday Maltese IT word |
| backup status bar | strixxa tal-istat tal-backups | |
| lamp | dawl (pl. dwal) | the small indicator lights |
| data source | sors tad-data | |
| local log | log lokali | |
| log file | fajl tal-log | |
| file / folder | fajl (pl. fajls) / folder (pl. folders) | Microsoft Maltese |
| snapshot | snapshot | masculine ("is-snapshot") |
| vault (Obsidian) | vault | product term |
| scheduled task | kompitu skedat (pl. kompiti skedati) | |
| profile / account | profil / kont | |
| theme | tema | |
| layout | tqassim | Microsoft Maltese; "split" between models = "qsim" |
| default | prestabbilit | "l-issettjar prestabbilit", "valuri prestabbiliti" |
| settings | Issettjar | see above |
| update (program) | aġġornament tal-programm | verb: aġġorna; "Installa issa" |
| check | iċċekkja | "Qed jiċċekkja…" |
| download | niżżel / tniżżil | "Qed jitniżżel…", "paġna tat-tniżżil" |
| refresh (data) | aġġorna | "Aġġorna d-data tal-użu issa" |
| history | storja | window title "storja", menu "Storja u statistika…" |
| projection / forecast | projezzjoni | "Projezzjoni sa tmiem il-ġimgħa" |
| peak | quċċata | |
| countdown | għadd lura | |
| plan badge | badge tal-pjan | |
| usage credits | krediti tal-użu | |
| connected apps | apps konnessi | |
| surface (Claude Code, apps…) | pjattaforma | |
| stale data | data qadima | |
| always on top | dejjem fuq quddiem | |
| lock position | sakkar il-pożizzjoni | |
| click-through | klikks jgħaddu minnu | |
| snap to edge | jeħel mat-tarf tal-iskrin | |
| drag / right-click / double-click | kaxkar / klikk bil-lemin / klikk doppju | |
| mouse wheel | rota tal-maws | |
| device(s) | apparat (pl. apparati) | "l-apparati kollha" |
| message to the developer | Messaġġ lill-iżviluppatur | |
| rating / overall rating | valutazzjoni / valutazzjoni ġenerali | |
| optional | mhux obbligatorju | |
| e-mail | email / indirizz tal-email | |
| consent | kunsens | "irtirar tal-kunsens" |
| privacy notice / policy | Politika tal-Privatezza | see above |
| controller / processor | kontrollur / proċessur | GDPR Maltese text |
| legitimate interest | interess leġittimu | Artikolu 6(1)(f) |
| supervisory authority | awtorità superviżorja | |
| profiling / automated decision-making | tfassil ta' profili / teħid ta' deċiżjonijiet awtomatizzat | GDPR Maltese text |
| access, rectification, erasure, restriction, objection | aċċess, rettifika, tħassir, restrizzjoni, oġġezzjoni | GDPR Art. 15–21 |
| encrypted | kriptat | "konnessjoni kriptata" |
| disclaimer | ċaħda ta' responsabbiltà | |
| terms of use | termini tal-użu | |
| cancel / close / quit | Ikkanċella / Agħlaq / Agħlaq il-programm | "Oħroġ" is reserved for sign-out |
| send / sending… | Ibgħat / Qed jintbagħat… | |
| time units | s / min / h / j | "j" = jum; "{}j {}h", "{}h {}min" |
