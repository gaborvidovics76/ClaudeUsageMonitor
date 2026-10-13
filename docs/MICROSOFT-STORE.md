# Microsoft Store (MSIX) – kiadás és beküldés

A Windows-program két úton jut el a felhasználókhoz:

| Út | Csomag | Frissítés | Készíti |
|---|---|---|---|
| Weboldal (marad, további utasításig) | `ClaudeUsageMonitor-Setup-X.Y.Z.zip` | a program saját frissítője | `release.ps1 -Version X.Y.Z [-Upload]` |
| Microsoft Store | `ClaudeUsageMonitor_X.Y.Z.0_x64.msix` | a Store | `release.ps1 -Version X.Y.Z -Msix` vagy `tools\make_msix.ps1` |

Mindkettő **ugyanabból a PyInstaller-buildből** készül. Az MSIX-et a weboldalra nem töltjük fel; a
`release\msix\` mappa és a `*.msix` git-ignorált.

## Mit csinál másképp a program a Store-csomagban

A program magától felismeri, hogy MSIX-csomagból fut (`winutil.is_packaged()`), és akkor:

- **nincs önfrissítő** – sem automatikus ellenőrzés, sem „Frissítések keresése” menüpont, sem a Beállítások
  frissítés-sora (a csomag mappája csak olvasható, és a Store szabályzata szerint a frissítést a Store adja);
  a verziószám mellett „Microsoft Store” áll;
- **az automatikus indítást a Windows kapcsolja**: a manifestben egy kikapcsolt `windows.startupTask` van; a
  menü „Indítás a Windows-zal…” pontja és a Beállítások gombja a Windows Indítás-oldalát nyitja
  (`ms-settings:startupapps`), mellette 34 nyelven a magyarázat (`set.autostart_store`);
- **nem nyúl** a ZIP-es telepítés ütemezett feladatához, Start menü parancsikonjához és „Telepített
  alkalmazások” bejegyzéséhez (ezeket a csomag adja);
- a beállítások mappája a csomag saját másolata (`%LOCALAPPDATA%\Packages\<család>\LocalCache\Roaming\
  ClaudeUsageMonitor`) – a „Beállítások mappa megnyitása” gomb ezt nyitja. A ZIP-es változatból átváltóknál a
  meglévő beállítások és a bejelentkezés első olvasáskor átjönnek.

Kipróbálás csomag nélkül: `CLAUDE_USAGE_MONITOR_PACKAGED=1` környezeti változóval a ZIP-es program is
„Store-módba” vált (`tests\store_mode.py` így teszteli).

## A csomag elkészítése

```powershell
.\tools\get_signtool.ps1          # egyszer: makeappx / makepri / signtool a Microsoft BuildTools NuGet-csomagjából
.\tools\make_msix.ps1 -Build      # build + MSIX  ->  release\msix\ClaudeUsageMonitor_<X.Y.Z.0>_x64.msix
```

A szkript: a programot változatlanul a csomagba másolja, az app logójából legyártja a 28 Store/Start-képet
(`tools\make_msix_assets.py`), kitölti a manifestet (`packaging\msix\AppxManifest.xml.in` +
`packaging\msix\identity.json`, verzió `X.Y.Z.0`), `resources.pri`-t készít a képváltozatokhoz, `makeappx`
csomagol SHA-256 blokktérképpel, majd kicsomagolva ellenőrzi.

## Teendők a Partner Centerben (egyszer)

1. **Fejlesztői fiók** (magánszemélyként egyszeri díj) a <https://storedeveloper.microsoft.com> oldalon.
2. **Alkalmazásnév foglalása.** Figyelem: a Store szabályzata szerint az alkalmazás neve nem tartalmazhat más
   védjegyét engedély nélkül, a „Claude” pedig az Anthropic védjegye. Számíts rá, hogy a „Claude Usage Monitor”
   név fennakadhat; ha igen, egy semleges név kell (a manifestben a `display_name`).
3. **Product identity** (Product management › Product identity): a három értéket másold a
   `packaging\msix\identity.json`-ba:
   - `Package/Identity/Name` → `name`
   - `Package/Identity/Publisher` (`CN=<GUID>`) → `publisher`
   - `Package/Properties/PublisherDisplayName` → `publisher_display_name`
   - a lefoglalt név → `display_name`
   Amíg ez nincs kitöltve, a szkript sárgán jelzi, hogy helyőrző-azonosítóval készült (a Store az ilyet elutasítja).
4. **Csomag feltöltése**: Submission › Packages – az **aláíratlan** `.msix` megfelelő, a Store maga írja alá.
5. **Korlátozott képesség indoklása** (`runFullTrust`), a beküldésnél kérik – javasolt szöveg:
   > This is a classic Win32 desktop application (Python/Qt, packaged with PyInstaller) converted to MSIX.
   > runFullTrust is required for a desktop app: it shows an always-on-top panel and a tray icon, reads the
   > user's own Claude Code log files in their profile folder, and calls the Anthropic usage API with the
   > user's own sign-in.
6. **Adatvédelmi tájékoztató URL** (internetelérés miatt kötelező): `https://claudeusagemonitor.com/#privacy`
7. **Korhatár-besorolás** (IARC kérdőív), kategória: *Productivity* vagy *Developer tools*, nyelvenkénti
   leírás és képernyőképek (a `build-shots\` mappa képei jól jönnek).

## Helyi kipróbálás (opcionális)

A gépen most nincs bekapcsolva a Windows Fejlesztői mód, ezért a csomagot helyben nem telepítettük. Ha ki
akarod próbálni: Beállítások › Rendszer › Fejlesztőknek › **Fejlesztői mód** be, majd

```powershell
Add-AppxPackage -Register .\build\msix\layout\AppxManifest.xml     # telepítés a kicsomagolt mappából
Get-AppxPackage *ClaudeUsageMonitor* | Remove-AppxPackage            # eltávolítás
```

Előtte a ZIP-es programból lépj ki (egyszerre csak egy példány futhat).
