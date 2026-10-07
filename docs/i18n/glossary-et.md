# Glossary – Estonian (et) – Claude Usage Monitor

Estonian consumer-software register (Microsoft Windows / Office Estonian terminology for the Windows side,
natural Estonian for the four macOS texts – macOS itself has no Estonian UI, so there is no Apple
terminology to copy). One fixed translation per term; the module `claude_usage/langs/et.py` follows this list.

## Tone and form of address

- **"Sina" (sinatamine)** everywhere: "Logi sisse", "Kontrolli ühendust", "sinu konto", "sa näed".
  This is what Microsoft Windows 11, Google, Apple's Estonian site, Swedbank, Bolt and Telia use for consumers.
  Never "Teie". One form everywhere, also in the privacy notice (modern Estonian privacy notices of consumer
  services use "sina"; the legal register comes from the terminology, not from "Teie").
- Short, friendly, confident – like the English. The author speaks in the first person in the feedback window
  ("Kirjuta mulle", "loen läbi mina"). The program itself does not speak in the first person: progress texts
  are nominal, Microsoft-style ("Kontrollimine…", "Saatmine…", "Allalaadimine…", "värskendamine").
- Imperative on buttons and menu items ("Logi sisse", "Saada", "Sule", "Loobu", "Sirvi…", "Vali värv…").
- Panel labels in CAPITALS as the English (5 H SEANSS, NÄDALALIMIIT). Estonian long compounds are natural
  elsewhere, but the panel, time and *_short texts stay at or very near the English length.
- Quotation marks: „…“ (Estonian low-high). Dash: – (en dash with spaces). Percent: "{}%" without space inside
  a compact value, "70 %" with a space in running text (Estonian typography).
- Time units, the standard short forms: **s** (sekund), **min** (minut), **h** (tund – the SI symbol, used by
  Windows, Google and the Estonian press; "t" exists but is rarer and clashes with "t" for tonne), **p** (päev).
  Date: 06.10.2026 (dd.mm.yyyy, the Estonian standard).
- Product names stay as they are and are inflected with the Estonian suffix: Claude Desktopi, Claude Code'i
  (apostrophe, silent final e), Anthropicu, OneDrive'is, Nextcloudi, Obsidiani, Coworki, claude.ai-sse /
  claude.ai-st (hyphen after a domain). Fable, Opus, Sonnet, Haiku, PRO/MAX/TEAM/ENTERPRISE, rclone, PowerShell,
  HTTP(S), JSON, OAuth, SHA-256, DPAPI, GDPR, NAIH, GitHub, claudeusagemonitor.com, Vidovics Gábor,
  Claude Backup Kit, `*.json`, file and folder names – untouched.

## Microsoft (Windows) choices and why

| English | Estonian | Why |
|---|---|---|
| Settings | **Sätted** | Windows 10/11 Estonian ("Sätted"). Apple's site and Google/Android say "Seaded"; both are understood, but the app is a Windows tray tool and the brief asks for Microsoft wording. One form everywhere: menüü "Sätted…", aken "sätted", "Ava sätete kaust", "Taasta vaikesätted". |
| Help | **Spikker** | Windows / Office Estonian term for Help. "Abi" is the everyday word and the alternative if the maintainer prefers it (see REVIEW). |
| Sign in / Sign out | **Logi sisse / Logi välja**; noun: **sisselogimine** | Microsoft and every Estonian bank/e-service. |
| taskbar | **tegumiriba** | Windows Estonian. |
| notification area / system tray | **teavitusala**; tray icon = **teavitusala ikoon** | Windows Estonian ("teavitusala"). |
| Start menu | **menüü Start** | Windows Estonian keeps the name "Start" after "menüü". |
| notification | **teatis** (noun), **teavita** (verb) | Windows: "Teatised"; the verb form "Teavita, kui…" is the natural checkbox wording. |
| Cancel | **Loobu** | Microsoft Estonian (Google uses "Tühista"). |
| Quit / Exit | **Välju** | Microsoft Estonian. |
| Close | **Sule** | |
| Browse… | **Sirvi…** | |
| folder | **kaust** | |
| update (program) | **värskendus / värskenda** | Microsoft "update" = värskendus; also "Värskenda" for refresh. |
| download | **laadi alla / allalaadimine** | |
| upload | **laadi üles / üleslaadimine** | |
| server | **server** | |
| theme | **kujundus** | Windows "Kujundused". ("teema" is the Google word; not used.) |
| always on top | **alati pealmine** | Windows wording. |
| default | **vaikimisi**, default settings = **vaikesätted** | |
| widget | **vidin** | Windows Estonian for gadget/widget. |
| click / right-click / double-click | **klõps / paremklõps / topeltklõps** | Microsoft Estonian ("klõps", not "klikk"). |
| drag | **lohista** | |
| scheduled task | **ajastatud toiming** | Windows "Toiminguajur" (Task Scheduler), task = toiming. |
| endpoint | **lõpp-punkt** | Microsoft Estonian. |
| passkey | **pääsuvõti** | Google / Apple Estonian. |

## macOS (STRINGS_MAC)

| English | Estonian |
|---|---|
| menu bar | **menüüriba** |
| Start at login (login items) | **Ava sisselogimisel** |

## Privacy document name

**Privaatsuspoliitika** (`fb.privacy_title`, `help.privacy`, and the word used in `fb.err_consent`).
This is what Estonian consumer software and websites call the notice on a link or a checkbox: Apple's
Estonian legal pages ("Apple'i privaatsuspoliitika"), Meta/Facebook, Bolt, Wise, Pipedrive, the Estonian
e-shops and banks. The Estonian supervisory authority (Andmekaitse Inspektsioon) itself uses
"andmekaitsetingimused" and "isikuandmete töötlemise teave" for the GDPR art. 13 information; those are the
precise legal names, but on a form the user looks for "Privaatsuspoliitika". Inside the legal text the regulation
is named once in full – "isikuandmete kaitse üldmäärus (GDPR)" – then "GDPR"; the articles follow the official
Estonian GDPR text: "artikli 6 lõike 1 punkt f / punkt a". Andmekaitse Inspektsioon (aki.ee) is added as the
Estonian example next to "oma riigi järelevalveasutus".

## Fixed terms

| English | Estonian | Note |
|---|---|---|
| 5-hour session | **5-tunni seanss** | panel: 5 H SEANSS; short: 5H; history: "5-tunni seansid" |
| weekly limit | **nädalalimiit** | panel: NÄDALALIMIIT; short: NÄDAL; tray: "Nädal" |
| per-model weekly limit | **mudelipõhine nädalalimiit** | |
| limit | **limiit** | "limiit" is the everyday Estonian word for a usage/credit limit; "piirang" only for rate limiting |
| rate limit / rate limited (429) | **päringupiirang** / "server piirab päringuid" | |
| rate-limit tier | **päringupiirangu tase** | |
| reset (noun / verb) | **lähtestus / lähtestub** | Microsoft "reset" = lähtesta; panel: "lähtestus {}" |
| countdown to reset | **pöördloendus lähtestuseni** | |
| pace | **tempo** | panel: "{} vs tempo" |
| burn rate | **kulumiskiirus** | "%/tund, %/päev" |
| avg daily burn | **keskmine päevakulu** | |
| usage | **kasutus**; usage data = **kasutusandmed**; usage file/log = **kasutusfail / kasutuslogi** | |
| usage credits (pay-as-you-go) | **kasutuskrediit (kasutuspõhine tasu)** | |
| plan | **pakett** | the Estonian word for a subscription plan (telcos, SaaS); "Pakett: Pro" |
| plan badge | **paketimärk** | "Paketimärk ja lisalimiidid" |
| gauge | **näidik** | "Näidik: Opus", "Näidikute järjestus" |
| panel | **paneel**; floating panel = **hõljuv paneel** | |
| layout | **paigutus** | märkmeleht (post-it), kitsas riba, rõngad |
| data source | **andmeallikas** | menu and tab |
| local log (this PC only) | **kohalik logi (ainult see arvuti)** | PC = "arvuti" |
| profile / account | **profiil / konto** | |
| history | **ajalugu** | "Ajalugu ja statistika…" |
| projection / forecast | **prognoos** | "Nädala lõpu prognoos" |
| weekly peak | **nädala tipp** | |
| threshold | **lävend** | "lävendi ületamisel" |
| alert (tab) / warning / critical | **hoiatused / hoiatus / kriitiline** | |
| stale data | **aegunud andmed**; "andmed vananevad" | |
| data freshness | **andmete värskus** | |
| backup (a copy) / backup (process) | **varukoopia / varundus** | "Varukoopiad…", "Varunduse olekuriba", "varunduslogid", "varundusskript" |
| snapshot | **hetktõmmis** | |
| vault (Obsidian) | **hoidla** | |
| lamp | **lamp** | the small status lights: "Ainult lambid", "Silt lambi kõrval" |
| disclaimer | **vastutuse välistamine** | |
| remote storage | **kaugsalvestusruum** | |
| message to the developer | **sõnum arendajale** | |
| rating / overall rating | **hinnang / üldhinnang** | star rating = tärnihinnang |
| consent | **nõusolek** | "Olen läbi lugenud ja nõustun: {}." |
| controller / processor (GDPR) | **vastutav töötleja / volitatud töötleja** | official Estonian GDPR terms |
| legitimate interest | **õigustatud huvi** | |
| profiling / automated decision-making | **profiilianalüüs / automatiseeritud otsuste tegemine** | |
| supervisory authority | **järelevalveasutus** | |
| encrypted | **krüptitud** | |
| telemetry | **telemeetria** | "telemeetriat pole" |
| open source | **avatud lähtekood** | source code = lähtekood |
| terms of use | **kasutustingimused** | |
| release notes / what's new | **väljalaskemärkmed / Mis on uut** | |
| version | **versioon** | |
| accent color | **rõhuvärv** | Windows "Värvid" page |
| opacity | **läbipaistmatus** | |
| click-through | **läbiklõpsatav** | "ainult kaunistus, hiirt eiratakse" |
| lock position | **lukusta asukoht** | |
| snap to screen edge | **haagi ekraani serva külge** | |
| trend curve | **trendikõver (sparkline)** | |
| connected apps | **ühendatud rakendused** | |
| per-surface limits | **limiidid keskkonna kaupa** | surface = keskkond (Claude Code, ühendatud rakendused) |
| app / program | **rakendus / programm** | as the English alternates |
| no data | **andmeid pole** | panel; time slot: "andmeid pole" |
| not set | **määramata** | |
| done / FAILED | **valmis / EBAÕNNESTUS** | |
| token (OAuth / output tokens) | **token** (tokeni, tokenid) | developer word, as in the Estonian dev press; "tõend" would be unclear here |
| snapshot / note (Obsidian) | **hetktõmmis / märge (märkmed)** | |
| Help | **Spikker** | menu "Spikker…", window title |

## Panel and tray short forms (tight space)

| English | Estonian | Note |
|---|---|---|
| updated: {} | **seisuga {}** | the idiomatic Estonian "as of 14:32"; shorter than "uuendatud" |
| fetching data | **andmepäring** | nominal, no first person |
| retry in {} s | **uus katse {} s** | |
| reset {} | **lähtestus {}** | consistent with the glossary term; 4 chars longer than English |
| full: {} | **täis: {}** | |
| {} WEEKLY / WEEK | **{} NÄDAL / NÄDAL** | |
| No data | **Andmeid pole** | |
| %/h, %/day | **%/h, %/p** | |
| time | **{} s, {} min, {} h, {} p; {}h {}min; {}p {}h** | "m" is the metre in Estonian, so minutes stay "min" |
| numbers + nouns | counted values are written as "Label: {}" where the noun would need number agreement ("Säilitatud hetktõmmiseid: {}", "uusi {}, asendatud {}, vigu {}") | avoids "1 faili"-type errors |
