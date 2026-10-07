# Gluais – Gaeilge (ga) – Claude Usage Monitor

Irish (Gaeilge), consumer-software register, **An Caighdeán Oifigiúil** (2017) spelling and grammar. Terminology
follows the Microsoft Irish Language Interface Pack / Microsoft Terminology and tearma.ie (An Coiste Téarmaíochta).
One fixed translation per term; `claude_usage/langs/ga.py` follows this list.

## Tone and form of address

- **Singular "tú"** throughout (imperative singular: "Sínigh isteach", "Seiceáil", "Greamaigh"; possessive "do"
  with lenition: "do chuntas", "do bhrabhsálaí", "d'úsáid"). This is the standard of Irish consumer software
  (Microsoft, Google, Mozilla Irish UIs) and of Irish-language public websites. Never the plural "sibh".
- Short, friendly, confident, like the English; the author speaks in the first person in the feedback window
  ("Inis dom", "Léim féin gach teachtaireacht").
- Progressive states use the verbal noun with "á" + object pronoun or "ag": "Á sheiceáil…", "Á sheoladh…",
  "Á íoslódáil…", "Ag lorg nuashonruithe…".
- **Initial mutations are written in full**, also after digits: "5 huaire", "6 huaire", "2 bhliain", "6 théama",
  "ar an bpainéal", "chuig an bhforbróir", "ón bhfreastalaí", "sa chúinne". In **UPPERCASE panel labels the
  prefixed letter stays lowercase** as the Caighdeán requires ("SEISIÚN 5 hUAIRE", "AN tSEACHTAIN").
- Where a number comes from a placeholder (`{}`) the mutation cannot be known in advance, so such texts are
  phrased as "label: {}" ("Comhaid: {}", "earráidí: {}") instead of "{} + noun".
- Panel labels in CAPITALS as the English (long vowels keep their síneadh fada: "SEISIÚN").
- Time units, short forms as used in Irish software: **s** (soicind), **nóim** (nóiméad), **u** (uair), **l** (lá).
  Percent without a space: "{}%", also in running text ("70%").
- Untranslated names: Claude, Claude Desktop, Claude Code, claude.ai, Anthropic, Fable, Opus, Sonnet, Haiku,
  PRO/MAX/TEAM/ENTERPRISE, OneDrive, Nextcloud, Obsidian, Cowork, rclone, PowerShell, HTTP(S), JSON, OAuth,
  SHA-256, DPAPI, NAIH, GitHub, claudeusagemonitor.com, Vidovics Gábor, Claude Backup Kit, Post-it, sparkline.
  They take no mutation ("ar claude.ai", "de chuid Anthropic", "le Windows").

## Name of the privacy document

**"Polasaí Príobháideachais"** (`fb.privacy_title`, `help.privacy`, and inside `fb.consent` / `fb.err_consent` /
`fb.privacy_hide`; with the article: "an Polasaí Príobháideachais", "leis an bPolasaí", gen. "an pholasaí seo").

Why: this is the name that Irish-language software and websites put on the link – TG4, RTÉ, Foras na Gaeilge,
Údarás na Gaeltachta, Conradh na Gaeilge, the Irish Microsoft and Mozilla UIs ("Polasaí príobháideachais") – and
it is the tearma.ie entry for *privacy policy*. The Irish supervisory authority, **An Coimisiún um Chosaint
Sonraí** (DPC), and gov.ie label their own notice "Ráiteas Príobháideachais" (privacy *statement*), and GDPR Irish texts
speak of "fógra príobháideachais" (privacy *notice*). Because the app shows one document under two English
names (notice on the form, policy in the Help window) and the user meets it as a link and a checkbox, the single
software-convention name "Polasaí Príobháideachais" is used everywhere, so that the consent line, the error line
and the Help link all name the same thing. The regulation is cited as **RGCS** (an Rialachán Ginearálta maidir le
Cosaint Sonraí) with the article numbers in the official form "Airteagal 6(1)(f)"; "GDPR" is not used in Irish.

## Fixed terms

| English | Gaeilge | Note |
|---|---|---|
| 5-hour session | seisiún 5 huaire | panel: SEISIÚN 5 hUAIRE; short: 5U; plural "seisiúin 5 huaire" |
| weekly limit | teorainn seachtaine | (genitive-noun attribute, like "pas seachtaine"; shorter and more idiomatic than "teorainn sheachtainiúil"); pl. "teorainneacha seachtaine"; panel: AN tSEACHTAIN (tight space); short: SEACHT.; model label: "{} · SEACHTAIN" |
| per-model weekly limit | teorainn seachtaine na samhla | |
| model (AI) | samhail | gen. "na samhla", pl. "samhlacha" (tearma.ie: *model* = samhail) |
| gauge | tomhsaire | "Tomhsaire Opus", "ord na dtomhsairí" (tearma.ie) |
| reset (noun) | athshocrú | "comhaireamh síos go dtí an t-athshocrú" |
| reset (verb, a limit resets) | athshocraigh / athshocraítear | notification: "athshocraithe — tá tréimhse nua tosaithe" |
| reset (panel, tight) | athshocrú {} | |
| pace | luas | "{} vs luas" |
| burn rate | ráta caithimh | "(%/uair, %/lá)" |
| usage | úsáid | "sonraí úsáide", "comhad úsáide" |
| usage credits | creidmheasanna úsáide | |
| plan | plean | "Plean: {}"; Pro / Max unchanged |
| plan badge | suaitheantas an phlean | |
| rate-limit tier | leibhéal teorann ráta | |
| panel / floating panel | painéal / painéal ar snámh | "ar an bpainéal", "ceanntásc an phainéil" |
| widget | giuirléid | Microsoft Irish term; "ar an ngiuirléid" |
| tray / system tray | tráidire / tráidire an chórais | Microsoft Irish; icon: "deilbhín an tráidire" |
| notification area | limistéar na bhfógraí | mentioned only in the glossary; the UI says "tráidire" |
| menu bar (macOS) | barra roghchláir | only in STRINGS_MAC: "deilbhín an bharra roghchláir" |
| taskbar | tascbharra | |
| Start menu | an roghchlár Tosaigh | "Taispeáin sa roghchlár Tosaigh" |
| Settings | Socruithe | window and menu item |
| sign in / sign out | Sínigh isteach / Sínigh amach | "Sínigh isteach ar claude.ai…", "Sínigh amach as claude.ai" |
| sign-in (noun) | síniú isteach | "tá an síniú isteach imithe in éag", "síniú isteach de dhíth" |
| signed in / not signed in | sínithe isteach / Níl tú sínithe isteach | |
| log in (macOS login) | logáil isteach | "Oscail ar logáil isteach" (STRINGS_MAC only) |
| quit | Scoir | last menu item |
| notification / notify | fógra / fógra nuair a… | "Fógra nuair a shároítear tairseach" |
| alert | foláireamh | tab "Foláirimh" |
| threshold | tairseach | pl. "tairseacha", gen. pl. "na dtairseach" |
| warning / critical | Rabhadh / Criticiúil | threshold levels |
| backup | cúltaca | pl. "cúltacaí"; "fillteán cúltaca", "script cúltaca", "logchomhaid cúltaca" |
| snapshot | léargas | pl. "léargais"; "an léargas is déanaí" |
| vault (Obsidian) | taisceadán | "léargas ar thaisceadán Obsidian" |
| lamp | lampa | "Lampaí amháin", "lipéad in aice leis an lampa" |
| data source | foinse sonraí | "an fhoinse sonraí" |
| measurement source | foinse tomhais | |
| local log / log file | logchomhad áitiúil / logchomhad | log record: "logáil"; "fillteán logchomhad Claude Code" |
| profile / account | próifíl / cuntas | |
| theme | téama | "6 théama" |
| layout | leagan amach | pl. "leaganacha amach" |
| accent color | dath béime | |
| opacity | teimhneacht | |
| always on top | ar barr i gcónaí | |
| lock position | glasáil an suíomh | |
| click-through | cliceáil tríd | |
| snap to screen edge | greamaigh d'imeall an scáileáin | |
| update (program) | nuashonrú | "Nuashonrú an chláir", "lorg nuashonruithe" (Microsoft: *check for updates*) |
| download / upload | íoslódáil / uaslódáil | |
| install | suiteáil | |
| history | stair | window "Stair", "Stair agus staitisticí…" |
| projection / forecast | réamhaisnéis | "réamhaisnéis go deireadh na seachtaine" (avoids the disputed lenition of a definite genitive after a feminine noun) |
| peak | buaic | "Buaic na seachtaine" |
| avg daily burn | meánchaitheamh laethúil | |
| stale data / data freshness | sonraí as dáta / úire na sonraí | |
| message to the developer | teachtaireacht chuig an bhforbróir | |
| rating / overall rating | rátáil / rátáil fhoriomlán | "rátáil réaltaí", "cliceáil ar réalta" |
| privacy notice / policy | Polasaí Príobháideachais | see above |
| consent | toiliú | "Léigh mé an {} agus glacaim leis.", "do thoiliú a tharraingt siar" |
| controller / processor | rialaitheoir / próiseálaí | RGCS terms |
| supervisory authority | údarás maoirseachta | "údarás maoirseachta do thíre féin"; in Ireland: An Coimisiún um Chosaint Sonraí (not named in the notice – the generic wording is kept) |
| legitimate interest | leas dlisteanach | Airteagal 6(1)(f) RGCS |
| rights (access, rectification, erasure, restriction, objection) | rochtain, ceartú, léirscriosadh, srianadh, agóid | RGCS wording |
| profiling / automated decision-making | próifíliú / cinnteoireacht uathoibrithe | |
| terms of use | Téarmaí úsáide | |
| disclaimer | Séanadh | Microsoft Irish |
| connected apps | aipeanna ceangailte | app = aip (Microsoft Irish) |
| program / the app | an clár / an aip | "program update" = "nuashonrú an chláir" |
| scheduled task | tasc sceidealta | pl. "tascanna sceidealta" |
| folder / file | fillteán / comhad | |
| screen / mouse wheel | scáileán / roth na luiche | |
| right-click / double-click / drag | deaschliceáil / déchliceáil / tarraing | Microsoft Irish |
| e-mail / e-mail address | ríomhphost / seoladh ríomhphoist | label "Ríomhphost" |
| server / request / endpoint | freastalaí / iarratas / críochphointe | "ag cur teorann le hiarratais (429)" |
| token (API) | comhartha | "líon na gcomharthaí" (tearma.ie) |
| passkey | eochair rochtana | pl. "eochracha rochtana": "do phasfhocail agus d'eochracha rochtana" |
| this PC | an ríomhaire seo | Windows Irish "An Ríomhaire Seo"; panel header: AN RÍOMHAIRE SEO |
| snooze / later | ar ball | update dialog "Ar ball" |
| hash | hais | |
| replace / replaced | ionadaigh / ionadaithe | Microsoft Irish ("Aimsigh agus Ionadaigh") |
| top-right corner | an cúinne uachtarach ar dheis | "sa chúinne uachtarach ar dheis" |
| update server | freastalaí na nuashonruithe | not "freastalaí nuashonraithe" (= an updated server) |
| check / checking… | seiceáil / Á sheiceáil… | backups, codes; updates use "lorg" |
| refresh (data) | athnuaigh / athnuachan / athnuaite | "Athnuaigh sonraí úsáide anois", panel "athnuaite: {}" |
| done / completed successfully | críochnaithe / críochnaithe go rathúil | |
| failed | TEIPTHE / theip ar | |
| no data | gan sonraí | panel "Gan sonraí" |
| not set / default | gan socrú / réamhshocrú | "Athchóirigh na réamhshocruithe" |
| optional | roghnach | "(roghnach)" |
| enabled / disabled | Cumasaithe / Díchumasaithe | autostart notifications |
| on / off | air / as | details rows |
| details | mionsonraí | tab "Mionsonraí" (not "sonraí", which is *data*) |
| size: small / normal / large / extra | Beag / Gnáth / Mór / Breise | |
| step 1 / step 2 | Céim 1 / Céim 2 | |
| time formats (panel) | {}u {}nóim · {}l {}u · {} nóim · {} s · {} l · {} u | |
| fetching data (panel) | ag fáil sonraí | |
| retry in {} s (panel) | arís i gceann {} s | |
| full: {} (panel) | lán: {} | |
| What's new | Cad atá nua | Microsoft Irish |
| Help | Cabhair | Microsoft Irish |
