# Microsoft Store – tanúsítási audit a 2.9.0.0 MSIX-csomaghoz

**Dátum:** 2026-10-13 · **Csomag:** `release\msix\ClaudeUsageMonitor_2.9.0.0_x64.msix` (48,9 MB, SHA-256 blokktérkép) ·
**Források:** Microsoft Store Policies 7.20 (2026-09-14), „App package requirements for MSIX app”, „App screenshots,
images, and trailers for MSIX app”, Windows App Certification Kit (WACK) tesztlista.

Jelmagyarázat: ✅ megfelel, bizonyítékkal · ⚠️ figyelni kell / részben a te döntésed · ❌ hiányzik, teendő · 🔍 csak
a te gépeden / a Partner Centerben ellenőrizhető.

## 1. Csomag és manifest (technikai követelmények)

| Követelmény | Állapot | Bizonyíték / teendő |
|---|---|---|
| Verzió négyrészes, a 4. rész 0 | ✅ | `Version="2.9.0.0"` – a `make_msix.ps1` a `__version__`-ból képzi, a 4. részt mindig 0-ra |
| Architektúra megadva | ✅ | `ProcessorArchitecture="x64"`; a PyInstaller-build x64 |
| `TargetDeviceFamily` Windows.Desktop, támogatott Min/MaxVersionTested | ✅ | Min 10.0.17763.0 (Windows 10 1809, a Qt 6 minimuma), MaxVersionTested 10.0.26100.0 |
| Az Identity (Name, Publisher) megegyezik a Partner Center „Product identity” értékeivel | ✅ | **2026-10-26 óta kitöltve** (2.9.3.0): `30km.huKft.UsageMonitorforClaudeAI` / `CN=B0B6BD6A-73A1-43D2-A270-B8D70B599DEA`; a lefoglalt név „Usage Monitor for Claude AI”. |
| `PublisherDisplayName` = a Partner Center kiadói neve | ✅ | „30km.hu Kft” |
| Blokktérkép SHA-256 | ✅ | `makeappx pack /h SHA256`, az `AppxBlockMap.xml` a kicsomagolt ellenőrzésben megvan |
| Csomagméret ≤ 25 GB | ✅ | 48,9 MB |
| Fájlnevek ANSI | ✅ | ellenőrizve: a 169 programfájl és a 28 kép neve mind ASCII |
| Manifest jól formázott, séma szerinti | ✅ | `[xml]` parse + `makeappx` elfogadta; névterek: uap, desktop, rescap |
| Képek a manifestben (Square44x44, Square150x150, Wide310x150, StoreLogo) léteznek, skála- és célméret-változatokkal | ✅ | 28 PNG, `resources.pri` a `makepri`-vel; az alapértelmezett (Visual Studio) helyőrző képek nincsenek – mind az app logója |
| Nyelvek a Store támogatott listájában | ✅ | a 34 `<Resource Language>` mind szerepel a listán (`es-MX`, `zh-CN`, `zh-TW`, `pt-BR`, `pt-PT`, `ga`, `mt` is) |
| Képességek: csak amit használ | ✅ | `internetClient` (Anthropic API, frissítés-ellenőrzés nincs a Store-módban), `runFullTrust` (klasszikus Win32) |
| Nincs privát kulcs / .pfx a csomagban (WACK „Private code signing”) | ✅ | a layoutban csak a program, a képek, a manifest és a `resources.pri` |
| Debug-build tiltása (WACK „Debug configuration”) | ✅ | PyInstaller release; a Python 3.12 és a Qt 6 DLL-ek release-ek |
| **Bináris elemzés** (WACK „Binary analyzer”: DEP/`NXCOMPAT`, ASLR/`DYNAMICBASE`, `HighEntropyVA`, x86-nál SafeSEH) | ✅ | **72 PE-fájl** (exe, dll, pyd) átnézve a PE-fejlécből: mind x64, mindben megvan a DYNAMICBASE, az NXCOMPAT és a HighEntropyVA. A főprogram jellemzői: `0xC160`. SafeSEH csak x86-ra követelmény. |
| Control Flow Guard | ⚠️ | 26 DLL CFG nélkül (Python-, Qt- és PySide-könyvtárak). A WACK ezt nem követeli; ha figyelmeztetést ad, az nem bukás. |
| Önfrissítő nem módosíthatja a csomagot (10.2.2, és a csomagmappa csak olvasható) | ✅ | Store-módban (`winutil.is_packaged()`) az önfrissítő, a frissítés-menüpont és -beállítás nincs; teszt: `tests\store_mode.py` |
| Nem ír a telepítési mappába | ✅ | a program az `%APPDATA%`-ba ír (a csomagban ez a csomag saját `LocalCache\Roaming` másolata – kezelve) |
| Indítás bejelentkezéskor csomagban | ✅ | `windows.startupTask`, `Enabled="false"` (a Store elvárása: ne kapcsoljon be magától); a felhasználó a Windows Indítás-oldalán kapcsolja, az app oda vezet |
| Egy példány fut egyszerre | ✅ | `QSharedMemory` zár – csomagban is működik (teljes bizalmú app) |
| Aláírás | ✅ | a Store beküldéshez **nem kell**: a Store a tanúsítás után saját tanúsítvánnyal írja alá (hivatalos dokumentáció). Helyi teszt-telepítéshez kellene (`make_msix.ps1 -Sign`). |
| **WACK lefuttatása a kész csomagon** | 🔍 | **Kötelező a beküldés előtt, és csak a te gépeden megy** (lásd 4. szakasz). Ebben a munkamenetben nem tudtam futtatni: a WACK a teljes Windows SDK része, és a csomag telepítését igényli, ahhoz pedig Fejlesztői mód vagy megbízhatónak jelölt aláírás kell – ezek rendszerbeállítások, amelyekhez nem nyúltam. |

## 2. Szabályzati megfelelés (Microsoft Store Policies 7.20)

| Szabály | Állapot | Megjegyzés |
|---|---|---|
| **10.1.1 pontos bemutatás; a név egyedi, nincs benne marketingszöveg; nem állíthatja magáról, hogy más cégtől származik** | ⚠️ | A leírásban és a listázásban **kötelező** a „nem hivatalos, nem az Anthropic terméke; a Claude az Anthropic PBC védjegye” mondat (a weboldal láblécében már így van). **A név kockázata:** a „Claude Usage Monitor” tartalmazza az Anthropic védjegyét; a szabályzat szövege ezt nem tiltja kifejezetten, de a névfoglalásnál és a tanúsításnál elutasíthatják, mint más entitásra utaló nevet. Tartalék név a `display_name`-hez: **„Usage Monitor for Claude”** (a „… for X” alak az iparági gyakorlat), vagy semleges: „AI Usage Monitor”. Foglald le a nevet a Partner Centerben MIELŐTT bármit beküldesz: ott azonnal kiderül. |
| 10.1.1 „a termék értékajánlata az első indításkor világos legyen” / **10.1.2 teljesen működőképes a céleszközön** | ⚠️ | **A legnagyobb buktató.** A tesztelő gépén nincs Claude Desktop és nincs Claude-előfizetés, bejelentkezni csak Claude-fiókkal lehet. Teendők: (a) a beküldés „Notes for certification” mezőjébe pontos leírás (3. szakasz, kész szöveg); (b) **kész (2.9.1):** a panel üres állapota magyarázó szöveg lett mind a 34 nyelven – „Ezen a gépen nincs Claude Desktop használati napló. Indítsd el a Claude Desktopot, vagy jelentkezz be a claude.ai fiókoddal: jobb gomb a panelen › Bejelentkezés.” (helyi mód), illetve „Nincs bejelentkezés. Jobb gomb a panelen › Bejelentkezés (claude.ai, böngésző).” (claude.ai mód). **A Store-ba a 2.9.2.0 csomagot küldd be** (a 2.9.1 Claude Desktop nélkül, helyi módban indításkor leállt – épp a tesztelő gépén; javítva a 2.9.2-ben). |
| 10.1.3 keresőkifejezések: max 7, releváns, nincs ár, nincs más termék neve | ✅ | javasolt: `claude, usage, limits, monitor, anthropic, quota, tray` – a „claude”/„anthropic” mint kulcsszó releváns, de ha a név miatt kifogás jön, ezeket is cseréld |
| 10.1.4 értékes, minőségi, aktív termék | ✅ | 2.9.0, 34 nyelv, rendszeres kiadások, nyilvános forrás |
| 10.2 biztonság; 10.2.2 nincs dinamikus kódbetöltés | ✅ | Store-módban nincs önfrissítő, nem tölt le futtatható kódot; a hálózati forgalom: Anthropic API (saját belépéssel), claudeusagemonitor.com (csak az üzenetküldő űrlap, ha a felhasználó elküldi) |
| 10.2.3 nincs kártevő, nem telepít más szoftvert | ✅ | – |
| 10.2.4 külső szoftvertől függés | ✅ | a Claude Desktop/Claude Code **opcionális** (helyi napló-mód); a claude.ai-mód önálló. Ezt a leírásban mondd ki. |
| 10.2.9 MSIX vs. EXE/MSI | ✅ | MSIX – a Store írja alá, CDN-ről telepít |
| **10.5.1 adatvédelmi tájékoztató URL kötelező (Win32/Desktop Bridge terméknél mindig)** | ✅ | `https://claudeusagemonitor.com/legal/en.html` – önálló oldal, HTTP 200, „Privacy Policy” cím. (A `/#privacy` horgony JavaScripttel nyit ablakot – a Partner Centerbe az önálló URL-t írd.) Tartalmilag: milyen adat, hova megy, meddig, milyen jogok – ezt a tájékoztatónak tartalmaznia kell; nézd át, hogy a Store-verzió két végpontja (Anthropic API, claudeusagemonitor.com) szerepel-e benne. |
| 10.5.2 személyes adat továbbítása csak opt-in-nel | ✅ | az üzenetküldő űrlap csak kötelező hozzájárulással küld (2.7.0 óta) |
| 10.6 képességek a funkcióhoz kötve | ✅ | `runFullTrust` indoklás kész (3. szakasz) |
| 10.8 pénzügyi tranzakció | ✅ | nincs vásárlás, nincs adománykérés az appban |
| 10.13 játék-szabályok | – | nem játék; kategória: *Productivity* (vagy *Developer tools*) |
| 10.14 fióktípus | ✅ | a kiadó a **30km.hu Kft** (Company fiók). ⚠️ Az app adatkezelési tájékoztatója és a weboldal `legal` oldala jelenleg Vidovics Gábort nevezi meg adatkezelőként (magánszemély) – ezt a kiadóhoz kell igazítani, ha a Kft. az adatkezelő. |
| 11.x tartalom (PEGI 12 alatt, nem sértő, nem illegális) | ✅ | semleges, szakmai tartalom; IARC-kérdőívben minden „nem” |
| Listázás képei (11. és a képkövetelmények) | ✅ | lásd 5. szakasz |

## 3. Kész szövegek a beküldéshez

**Notes for certification** (angol; a tesztelőnek szól):

```
Usage Monitor for Claude AI is a utility for subscribers of Anthropic's Claude (Pro/Max/Team). It shows the
subscription's usage limits in an always-on-top panel and a tray icon. (On the developer's website the same
open-source program is called "Claude Usage Monitor"; inside this package it uses the Store name everywhere.)

Testing without a Claude account: the app starts in "local log" mode and reads the usage history that the
Claude Desktop application writes on this PC. Without Claude Desktop installed the panel shows, by design,
"No Claude Desktop usage log on this computer. Start Claude Desktop, or sign in with your claude.ai account:
right-click the panel > Sign in."; all UI (settings, themes, layouts, 34 languages, help, history window) is
still available from the right-click menu of the panel or of the tray icon. The "claude.ai" data source needs the tester's own Claude
subscription (OAuth sign-in in the system browser, same flow as Anthropic's Claude Code tool); no test
credentials can be shared because they are personal accounts.

runFullTrust: classic Win32 desktop application (Python 3.12 + Qt 6, packaged with PyInstaller), converted
to MSIX. It needs full trust for: an always-on-top frameless panel and a tray icon, reading the user's own
Claude Code log files under the user profile, and calling Anthropic's usage API with the user's own sign-in.
No telemetry, no analytics, no third-party SDKs. The Store build has no self-updater.

WACK "Blocked executables" (optional test): the flagged strings are inside the bundled Python 3.12 and Qt 6
runtime DLLs. The app itself starts only two programs: "claude --version" (Anthropic's Claude Code, when it is
installed, to send its own version to the usage API) and, only when the user's own backup scripts are set up on the
PC (a backup_profile.json exists), a read-only PowerShell query of those scheduled tasks. Nothing is downloaded or executed from the network.

Unofficial community tool, not affiliated with Anthropic. "Claude" is a trademark of Anthropic, PBC.
Privacy policy: https://claudeusagemonitor.com/legal/en.html   Source code (MIT):
https://github.com/gaborvidovics76/ClaudeUsageMonitor
```

**Leírás (Store listing, EN, ≤ 10 000 karakter – rövid változat):**

```
See how much of your Claude subscription you have used – always on top, at a glance.

• 5-hour and weekly limits, the per-model limit (e.g. Fable), reset countdown, burn rate and pace
• Every other limit the server reports: connected apps, routines, usage credits, saved limit resets
• This week's split by product (Claude Code, chats, Cowork) and, from Claude Code's local logs, by model
• History window: 6 hours, 24 hours or 7 days, with peak, average and an end-of-week projection
• Quiet notifications at thresholds you choose, and when a limit resets
• Six themes, three layouts, 34 languages

Two data sources: Claude Desktop's local log on this PC (no sign-in), or your claude.ai account for all
your devices (sign-in in your own browser, as Claude Code does). The program talks only to Anthropic's
servers and, for the optional "message to the developer" form, to claudeusagemonitor.com. No telemetry.

Unofficial community tool, not affiliated with Anthropic. "Claude" is a trademark of Anthropic, PBC.
Free and open source (MIT).
```

**Keresőkifejezések (max 7):** `claude`, `usage`, `limits`, `monitor`, `anthropic`, `quota`, `tray`

**Adatvédelmi URL:** `https://claudeusagemonitor.com/legal/en.html` · **Támogatás:** `https://claudeusagemonitor.com/#feedback`
· **Weboldal:** `https://claudeusagemonitor.com/`

## 4. Amit csak te tudsz megtenni (sorrendben)

1. **Partner Center fiók** (Individual), **névfoglalás** – itt dől el a „Claude” a névben. Ha elutasítják: `display_name`
   = „Usage Monitor for Claude” az `identity.json`-ban.
2. **Product identity** három értéke → `packaging\msix\identity.json` → `.\tools\make_msix.ps1 -Build`.
3. **WACK** a kész csomagon (kötelező; a Store ugyanezeket a teszteket futtatja):
   - Windows SDK telepítése (a „Windows App Certification Kit” összetevővel): `winget install Microsoft.WindowsSDK.10.0.26100`
   - Beállítások › Rendszer › Fejlesztőknek › **Fejlesztői mód** be (a csomag telepíthetőségéhez), vagy `make_msix.ps1 -Sign`
     + a tanúsítvány a „Megbízható személyek” tárba
   - ```powershell
     & "C:\Program Files (x86)\Windows Kits\10\App Certification Kit\appcert.exe" reset
     & "C:\Program Files (x86)\Windows Kits\10\App Certification Kit\appcert.exe" test -appxpackagepath .\release\msix\wack-test.msix -reportoutputpath .\release\msix\wack-report.xml
     ```
   - A jelentésben minden tesztnek PASS; a „Binary analyzer” CFG-figyelmeztetése elfogadható.
4. **Beküldés**: csomag feltöltése (aláíratlan jó), a 3. szakasz szövegei, a képek (5. szakasz), IARC-kérdőív,
   kategória, árazás (ingyenes, minden piac), adatvédelmi URL, támogatási URL.
5. **Tanúsítás után**: a Store-oldal linkje a weboldalra; a README és a `docs\MICROSOFT-STORE.md` frissítése.

## 5. Képek a beküldéshez (mind elkészült: `docs\store\`)

A Store szabályai: képernyőkép PNG, legalább 1366×768 (4K-ig), max 50 MB, asztali listázáshoz legfeljebb 10 db; a
fontos tartalom a felső kétharmadban; nincs rárajzolt logó, ikon vagy marketingszöveg. Minden kép 1920×1080, kizárólag
a program felülete, sima sötét háttéren, mintaadatokkal (bejelentkezés és saját adat nélkül). Nyelvenként külön kell
feltölteni (a Store listázás nyelvenként van): **en**, **hu**, **de** kész; más nyelv: `python tools\make_store_shots.py ja ko`.

| Fájl | Mit mutat | Felirat (captions-<nyelv>.txt) |
|---|---|---|
| `screenshots/<nyelv>/01-panel.png` | a panel (post-it elrendezés, midnight téma): három mérő, részletsorok, termék- és modellbontás, trendvonal | igen |
| `02-rings.png` | gyűrűs elrendezés, Claude-téma | igen |
| `03-compact.png` | vékony sáv | igen |
| `04-history.png` | előzmény-ablak 24 órás nézetben, statisztikákkal | igen |
| `05-settings.png` | Beállítások › Részletek fül | igen |
| `06-themes.png` | paper és neon téma egymás mellett | igen |
| `AppTileIcon-300x300.png` | 1:1 app-ikon (erősen ajánlott; ha nincs, a csomag logóját használják) | – |
| `SuperHero-1920x1080.png` | 16:9 „super hero” kép: logó, szöveg és UI nélkül, ahogy a szabály kéri | – |

Nem kell: 2:3 poszter és 1:1 dobozkép (csak játékokhoz), Xbox-képek, előzetes videó.

## 6. Buktatók összefoglalva

1. **Helyőrző azonosító a manifestben** → biztos elutasítás, amíg az `identity.json` nincs kitöltve.
2. **A név „Claude” része** → névfoglalásnál vagy tanúsításnál kifogás jöhet; tartalék név készen.
3. **Tesztelő Claude-fiók nélkül** → a 2.9.1 óta a panel maga mondja el, mi a teendő (Claude Desktop indítása vagy
   bejelentkezés a jobb gombos menüből); a „Notes for certification” szöveg ugyanezt írja le.
4. **WACK kihagyása** → a Store ugyanazt futtatja; a bináris ellenőrzést itt előre elvégeztem (tiszta), de a telepítési
   és indítási teszt csak a te gépeden megy.
5. **Adatvédelmi URL** → az önálló `legal/en.html` oldalt add meg, ne a `#privacy` horgonyt.
6. **Nyelvenkénti listázás** → ha 34 nyelvre nyitsz listázást, mindegyikhez képek és leírás kell; kezdd angollal (és
   magyarral), a többit később.
7. **Verziószám** → minden újrabeküldéshez magasabb verzió kell (a `__version__` léptetése után a csomag 4. része marad 0).
8. **Fiók-típus** → ha a kiadó neve cégnév, Company fiók és cégazonosítás kell (10.14).
