# Glosar hr – Claude Usage Monitor

Standardni hrvatski jezik (ijekavica, hrvatsko računalno nazivlje po uzoru na hrvatska sučelja Microsofta i
Applea). Jedan fiksni prijevod po pojmu; modul `claude_usage/langs/hr.py` slijedi ovaj popis.
(Revidirano: prethodni nedovršeni pokušaj koristio je „ti” i „limit”; obvezne jezične bilješke traže
SESIJA OD 5 SATI / TJEDNO OGRANIČENJE, pa je nazivlje usklađeno s njima.)

## Ton i oblik obraćanja

- **Obraćanje: „vi”** (2. lice množine iz poštovanja), imperativ „Provjerite”, „Zalijepite”, „Prijavite se”,
  „Kliknite”. Razlozi: hrvatska sučelja velikih proizvođača (Microsoft Windows i Office, Apple iOS/macOS, Google)
  dosljedno se obraćaju korisniku s „vi”; to je oblik koji hrvatski korisnik očekuje u programu, a nužan je i u
  pravnom tekstu (`fb.privacy_text`). Prijateljski ton engleskog izvornika postiže se kratkim rečenicama i
  autorovim 1. licem („Javite mi”, „Svaku poruku čitam osobno”), ne zamjenicom.
- Zamjenica se piše **malim slovom** („vaš račun”, „vaša prava”) – prema hrvatskom pravopisu veliko „Vi/Vaš”
  pripada osobnim pismima, a tekstovi upućeni općoj publici (upute, sučelja) pišu se malim slovom. Gdje se može,
  zamjenica se izostavlja.
- Množina iz poštovanja ujedno izbjegava rod korisnika („Niste prijavljeni”, „Ako ste ostavili adresu”).
  Jedina rodna iznimka je `fb.consent` (1. lice korisnika): „Pročitao/la sam i prihvaćam …”, standardni
  hrvatski obrazac u obrascima.
- Ton: kratak, prijateljski, siguran. Bez kalkova; glagolske imenice za stanja u tijeku („Provjera…”,
  „Slanje…”, „Preuzimanje…”).
- Obvezno hrvatsko nazivlje: tjedan, sat, računalo, datoteka, mapa, poslužitelj, postavke, obavijest,
  korisnik, preuzimanje, ažuriranje, prijava/odjava, zaslon, miš, kotačić, poveznica, zapisnik, pogreška,
  trenutačno, uređaj, sučelje, preglednik, kôd. Ne: sedmica, fajl, folder, server, log (osim u nazivima
  datoteka), greška, link, ekran, download.
- „kôd” (programski / prijavni) s cirkumfleksom u nominativu/akuzativu, radi razlikovanja od prijedloga „kod”.
- Vlastita imena uglavnom se ne sklanjaju nego se uvode imenicom (Microsoftov obrazac): „programa Claude Code”,
  „tvrtke Anthropic”, „sa sustavom Windows”, „trezora programa Obsidian”. Uvriježeni izuzeci: „u OneDriveu”,
  „na Nextcloud”.
- Oznake panela VELIKIM SLOVIMA s dijakritikom (SESIJA OD 5 SATI, TJEDNO OGRANIČENJE, {} TJEDNO, TJED.).
  „TJ.” se ne koristi jer u hrvatskom znači „to jest”.
- Vremenske jedinice: **s / min / h / d** („2h 30min”, „3 min”, „1 d”, „12 h”). Postotak u dinamičkim
  nizovima bez razmaka („{}%”), u proznom tekstu pomoći po pravopisu s razmakom („70 %”).
- Navodnici „…”. Datum: „21. rujna 2026.”. Raspon brojeva crticom bez razmaka („10–15”).
- Brojevi uz imenice: zbog sklonidbe (1 datoteka / 2 datoteke / 5 datoteka) broj se piše iza dvotočke
  („datoteka: {}”, „novih: {}”).
- Ne prevodi se: Claude, Claude Desktop, Claude Code, claude.ai, Anthropic, Fable, Opus, Sonnet, Haiku,
  PRO/MAX/TEAM/ENTERPRISE, OneDrive, Nextcloud, Obsidian, Cowork, rclone, PowerShell, HTTP(S), JSON, OAuth,
  SHA-256, DPAPI, GDPR, NAIH, GitHub, claudeusagemonitor.com, Vidovics Gábor, Claude Backup Kit, Windows.

## Naziv dokumenta o privatnosti

**„Pravila privatnosti”** (`fb.privacy_title`, `help.privacy`). Od dviju mogućnosti iz jezičnih bilješki
odabrana je ona koja odgovara nazivu kod najvećih platformi na hrvatskom: Google i Meta/Facebook koriste
„Pravila o privatnosti”, a „Pravila privatnosti” isti je pojam u kraćem obliku kakav se vidi na mnogim
hrvatskim stranicama. „Politika privatnosti” česta je, ali je kalk engleskog *policy* (u hrvatskom „politika”
primarno znači državnu politiku). Riječ „pravila” je množina srednjeg roda, pa `fb.consent` glasi
„Pročitao/la sam i prihvaćam Pravila privatnosti.” bez gramatičkog sudara (akuzativ = nominativ).

U pravnom tekstu (`fb.privacy_text`) uredba se prvi put navodi punim hrvatskim imenom **„Opća uredba o zaštiti
podataka (GDPR)”**, dalje skraćeno; članci po hrvatskom uzusu: „čl. 6. st. 1. t. (f)”. Nazivlje iz službenog
hrvatskog prijevoda uredbe: voditelj obrade, izvršitelj obrade, privola, legitimni interes, nadzorno tijelo,
izrada profila, automatizirano donošenje odluka, ispravak, brisanje, ograničenje obrade, prigovor. Mađarski
NAIH ostaje; uz „nadzorno tijelo vlastite države” dodan je hrvatski primjer **AZOP (azop.hr)** – Agencija za
zaštitu osobnih podataka.

## Fiksni pojmovi

| Engleski | Hrvatski | Napomena |
|---|---|---|
| 5-hour session | sesija od 5 sati | panel: SESIJA OD 5 SATI (obvezno po bilješkama); kratko: 5H |
| weekly limit | tjedno ograničenje | panel: TJEDNO OGRANIČENJE; kratko: TJED. |
| per-model weekly limit | tjedno ograničenje po modelu | panel: „{} TJEDNO” |
| limit | ograničenje | dosljedno, i u „bez ograničenja”, „dodatna ograničenja” |
| gauge | mjerač | „Mjerač Fable”, „redoslijed mjerača” |
| reset (noun) | reset | „odbrojavanje do reseta”; panel: „reset za {}” |
| reset (verb) | resetirati se | „kad se ograničenje resetira”; obavijest: „resetirano” |
| pace | tempo | panel: „{} vs tempo” |
| burn rate | brzina potrošnje | „%/h, %/dan” |
| full in (panel) | 100% za {} | kad će ograničenje biti potpuno iskorišteno |
| usage | potrošnja | „podaci o potrošnji”, „datoteka potrošnje” |
| usage credits | krediti za potrošnju | |
| plan | paket | Pro / Max ostaju |
| plan badge | oznaka paketa | |
| rate-limit tier | razina ograničenja zahtjeva | |
| panel / floating panel | panel / lebdeći panel | |
| widget | widget | uobičajeno u hrvatskom |
| tray (Windows) | područje obavijesti | Microsoft; „ikona u području obavijesti” |
| taskbar | programska traka | Microsoft |
| menu bar (macOS) | traka izbornika | samo u STRINGS_MAC |
| start at login (macOS) | Otvori pri prijavi | Apple |
| Start menu | izbornik Start | Microsoft |
| menu | izbornik | |
| Settings | Postavke | |
| sign in / sign out | Prijava / Odjava | glagol: „Prijavite se ponovno” |
| quit | Izlaz | |
| notification | obavijest | |
| alert | upozorenje | kartica „Upozorenja” |
| threshold | prag | razine: Upozorenje / Kritično |
| backup | sigurnosna kopija | Microsoft; „Sigurnosne kopije” |
| backup script | skripta za sigurnosne kopije | |
| snapshot | snimka | |
| vault (Obsidian) | trezor | |
| lamp | lampica | „Samo lampice”, „oznaka uz lampicu” |
| data source | izvor podataka | |
| measurement source | izvor mjerenja | |
| local log | lokalni zapisnik | |
| log / log file | zapisnik / datoteka zapisnika | |
| upload | prijenos / prenijeti | Microsoft (OneDrive: „Prenesi”) |
| online-only (OneDrive) | samo na mreži | Microsoftov naziv u OneDriveu |
| restore | vraćanje / vratiti | |
| profile / account | profil / račun | |
| theme | tema | |
| layout | raspored | |
| accent color | boja naglaska | |
| opacity | neprozirnost | |
| always on top | uvijek na vrhu | |
| lock position | zaključaj položaj | |
| click-through | propuštanje klikova | |
| snap to screen edge | prianjanje uz rub zaslona | |
| details | pojedinosti | Microsoft |
| update (program) | ažuriranje | „Ažuriranje programa” |
| download | preuzimanje / preuzmi | |
| install | instaliraj | |
| history | povijest | |
| projection / forecast | projekcija | |
| peak | maksimum | |
| stale data | zastarjeli podaci | |
| data freshness | svježina podataka | |
| message to the developer | poruka programeru | |
| rating | ocjena | „Ukupna ocjena” |
| privacy notice / policy | Pravila privatnosti | vidi gore |
| consent | privola | GDPR |
| controller / processor | voditelj obrade / izvršitelj obrade | |
| supervisory authority | nadzorno tijelo | |
| terms of use | Uvjeti korištenja | |
| disclaimer | odricanje od odgovornosti | |
| website | web-stranica | |
| connected apps | povezane aplikacije | |
| scheduled task | zakazani zadatak | Microsoft (Planer zadataka) |
| e-mail | e-pošta / adresa e-pošte | |
| server | poslužitelj | |
| request | zahtjev | |
| endpoint | krajnja točka | |
| browser | preglednik | |
| passkey | pristupni ključ | Google/Apple |
| default | zadano | „Vrati zadano” |
| optional | neobavezno | |
| cancel / close | Odustani / Zatvori | Microsoft |
| size | Mala / Normalna / Velika / Vrlo velika | uz „veličina” |
