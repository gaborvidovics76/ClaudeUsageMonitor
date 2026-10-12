# Claude Usage Monitor – natív macOS app (Xcode, Mac App Store)

Ez a mappa a program **natív Swift/AppKit/SwiftUI változata**, Xcode-projektként, a **Mac App Store-ba
szánva**. A Windows-verzió (Python + PySide6) forrásából készült, ugyanazzal a működéssel, ugyanazokkal a
fordításokkal (34 nyelv), de az Apple elvárásai szerint: App Sandbox, Keychain, SMAppService,
UserNotifications, String Catalog, privacy manifest, nincs önfrissítés.

> **English:** [docs/START-HERE-XCODE.md](docs/START-HERE-XCODE.md)
> **A kollégának, aki fordít és beadja:** [docs/APP-STORE-BEADAS.md](docs/APP-STORE-BEADAS.md) (lépésről lépésre)
> **Mit követel az Apple és mi a kockázat:** [docs/MEGFELELES.md](docs/MEGFELELES.md)
> **Bemásolható Claude Code prompt Macre:** [docs/KOLLEGA-PROMPT-XCODE.md](docs/KOLLEGA-PROMPT-XCODE.md)

A régi, PyInstalleres macOS-csomag (`macos/build.sh`, `macos/release.sh`) továbbra is itt van a `macos/`
mappában – az a weboldalról letölthető, **nem** App Store-os változat. A kettő egymástól független.

---

## Mi hol van

| Útvonal | Mi ez |
|---|---|
| `ClaudeUsageMonitor.xcodeproj` | az Xcode-projekt (Xcode 16+; szinkronizált mappa, nem kell fájlokat kézzel hozzáadni) |
| `ClaudeUsageMonitor/App/` | belépési pont (`AppDelegate`), vezérlő (`MonitorController`: időzítők, menü, értesítések, ablakok) |
| `ClaudeUsageMonitor/Core/` | fordítás (`Localization`), beállítások (`Settings` – UserDefaults), adatmodell, témák, napló |
| `ClaudeUsageMonitor/Data/` | adatforrások: Claude Desktop napló (`LocalLogReader`), claude.ai (`OAuth`, `ApiSource`), Claude Code naplók (`LocalModelUsage`), demó (`DemoSource`), Keychain, sandbox-könyvjelzők, üzenetküldés |
| `ClaudeUsageMonitor/UI/` | a lebegő panel (`PanelView`, `PanelWindow`), menüsor-ikon, Beállítások / Előzmények / Bejelentkezés / Súgó / Üzenet ablakok |
| `ClaudeUsageMonitor/Resources/Localizable.xcstrings` | **generált** – a 34 nyelv (lásd lent) |
| `ClaudeUsageMonitor/Resources/Assets.xcassets` | app-ikon (generált), accent szín |
| `ClaudeUsageMonitor/Resources/PrivacyInfo.xcprivacy` | privacy manifest |
| `ClaudeUsageMonitor/Info.plist`, `ClaudeUsageMonitor.entitlements` | bundle-adatok, sandbox-jogosultságok |
| `tools/gen_xcstrings.py` | a Windows-fordításokból String Catalogot készít |
| `tools/extra_strings.json` | csak a Mac/App Store változatban létező szövegek |
| `tools/make_icon.py` | az ikonkészlet (PNG-k) rajzolása |
| `../../.github/workflows/xcode-build.yml` | GitHub Actions: fordítás a GitHub Macjén (Mac nélkül ellenőrizhető, hogy lefordul-e) |

## Fordítás Macen (röviden)

1. Xcode 26 (vagy újabb) a Mac App Store-ból; `xcode-select --install` nem kell külön.
2. `git clone https://github.com/gaborvidovics76/ClaudeUsageMonitor.git`
3. Nyisd meg: `macos/Xcode/ClaudeUsageMonitor.xcodeproj`
4. **Signing & Capabilities** → Team: válaszd ki a saját Apple Developer csapatod (ez az egyetlen kötelező
   kézi beállítás; a `DEVELOPMENT_TEAM` szándékosan üres a repóban).
5. ⌘R – fut. Első indításkor a Beállítások ablak nyílik meg: ott kell **engedélyezni** a Claude Desktop
   naplójának olvasását (sandbox), vagy **Demóadatok** forrást választani, vagy bejelentkezni a claude.ai-ba.

Részletesen, az App Store Connect beadással együtt: [docs/APP-STORE-BEADAS.md](docs/APP-STORE-BEADAS.md).

## Verziószám

- `MARKETING_VERSION` (= `CFBundleShortVersionString`) a Windows-verzióval **azonos** legyen
  (`claude_usage/__init__.py`). Jelenleg 2.7.1. Ezt Gábor állítja.
- `CURRENT_PROJECT_VERSION` (= `CFBundleVersion`, build-szám) **minden App Store-feltöltésnél nő**
  (1, 2, 3…). Ezt a kolléga állítja az Xcode-ban (General → Build) vagy a `project.pbxproj`-ban.

## A claude.ai-bejelentkezés kapcsolója (fontos)

A claude.ai-forrás (OAuth a Claude Code nyilvános kliensével) **fordítási feltétel** mögött van:
`CLAUDE_SIGN_IN` – Build Settings → *Active Compilation Conditions*. Alapból **be van kapcsolva**.
Ha az Apple vagy az Anthropic kifogásolja (lásd [docs/MEGFELELES.md](docs/MEGFELELES.md) 1. pont), a
feltétel törlésével egy „store-biztos” változat készül, amely csak a helyi naplót és a demóadatokat
kínálja – a kód többi része változatlan.

## Fordítások frissítése

A szövegek forrása a Windows-app `claude_usage/i18n*.py` + `claude_usage/langs/*.py`. Ha ott változik
valami, vagy új kulcs kerül a Swift-forrásba:

```bash
python macos/Xcode/tools/gen_xcstrings.py
```

A csak Macen létező kulcsok (`set.dock`, `err.no_access_mac`, …) a `tools/extra_strings.json`-ban
vannak; amelyik nyelvre ott nincs fordítás, az angolra esik vissza (a script kiírja, melyek). A
generált `Localizable.xcstrings` commitolva van, hogy a Macen semmit ne kelljen futtatni.

## Ikon

```bash
python macos/Xcode/tools/make_icon.py
```

Szándékosan **nem** a Windows-app narancs csillagikonja: az Anthropic Claude-logójának formája, amit
az App Store szabályzat (5.2.1) és az Anthropic védjegy-irányelvei tiltanak harmadik fél appjában.
Az új ikon egy semleges mérőóra (sötét négyzet, háromnegyed gyűrű, %-jel).

## Mi NINCS benne a Windows-verzióhoz képest (szándékosan)

- **Önfrissítés** – az App Store nem engedi; frissítés az App Store-on át.
- **Mentési állapotsor** (OneDrive/Nextcloud/Obsidian) – Windows-os mentőszkriptekre épül.
- **Start menü / tálca** – helyette menüsor-ikon és (opcionálisan) Dock-ikon.
- **Kézi fájlútvonal** – a sandbox miatt a fájlt a rendszer Megnyitás panelével kell egyszer kiválasztani.

## Szabályok (ugyanazok, mint eddig)

1. A verziószám Gáboré. 2. `main`-re nem a macOS-oldal tol: javítás `macos/<téma>` ágon, Pull Request.
3. A `macos/Xcode/` mappa teljes egészében a macOS-oldalé – itt bátran lehet javítani.
