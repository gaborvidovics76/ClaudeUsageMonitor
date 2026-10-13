# Fordítás és beadás a Mac App Store-ba – lépésről lépésre

Ez a leírás **neked szól, aki a Macen fordítod és beadod** a Claude Usage Monitort. Gábor Windowson
fejleszt, Macje és Xcode-ja nincs; minden, ami az Apple gépet és fiókot igényli, a te kezedben van.
Ahol **„KÉRDEZD GÁBORT”** áll, ott tőle kell egy adat vagy döntés.

Tartalom: 1. Előfeltételek · 2. Projekt megnyitása, aláírás · 3. Fordítás és kipróbálás · 4. Amit
Macen tesztelni kell · 5. App Store Connect – az app rekordja · 6. Metaadatok · 7. Képernyőképek ·
8. Archiválás és feltöltés · 9. TestFlight · 10. Beadás ellenőrzésre · 11. Ha elutasítják · 12. Új verzió

---

## 1. Előfeltételek (a te Macedre és fiókodra)

| Mi | Részlet |
|---|---|
| Mac | Apple Silicon vagy Intel, **macOS 15 Sequoia** (Xcode 26-hoz) – Xcode 27-hez macOS 26.6+ |
| Xcode | **Xcode 26 vagy újabb** a Mac App Store-ból (ingyenes, ~15 GB). Az Apple 2026 áprilisa óta Xcode 26-ot kér; macOS-appra nincs külön SDK-minimum, de a legfrissebb a biztos. |
| Apple Developer Program | **fizetős tagság** (99 USD/év) azon a fiókon, amelyik az appot kiadja. **KÉRDEZD GÁBORT:** a te fiókod vagy az övé? Ha az övé, ő vegyen fel téged a csapatába (App Store Connect → Users and Access → „App Manager” vagy „Developer” szerep), és az archiválás/feltöltés a te Xcode-odból megy a közös csapatnévvel. |
| Megállapodások | App Store Connect → Agreements, Tax, and Banking: a **Paid Apps** nem kell (ingyenes app), de a **Free Apps** / Developer Program License Agreement legyen elfogadva az Account Holder által. |
| Két-faktoros Apple ID | kötelező a fiókon. |
| git | `xcode-select --install` ha a Terminal kéri. |

## 2. A projekt megnyitása, aláírás beállítása

```bash
git clone https://github.com/gaborvidovics76/ClaudeUsageMonitor.git
cd ClaudeUsageMonitor
open macos/Xcode/ClaudeUsageMonitor.xcodeproj
```

1. Bal oldalt a projekt → **ClaudeUsageMonitor** target → **Signing & Capabilities**.
2. **Team:** válaszd ki a csapatot. **Automatically manage signing** maradjon bekapcsolva – az Xcode
   maga készíti a tanúsítványokat és a „Mac App Store Connect” típusú provisioning profilt.
3. A **Bundle Identifier** `hu.dinorr.claudeusagemonitor`. Az Xcode automatikusan regisztrálja a
   csapathoz (Certificates, Identifiers & Profiles → Identifiers). Ha a csapatban már foglalt lenne,
   **KÉRDEZD GÁBORT** – ne találj ki másikat egyedül, mert a Keychain-elem és a beállítások ehhez
   kötődnek.
4. Capabilities-ben ezeknek már ott kell lenniük (az entitlements-fájlból jönnek): **App Sandbox**
   (Outgoing Connections (Client) ✓, User Selected File: Read Only ✓), **Hardened Runtime**.
   Ne adj hozzá mást.
5. Ha az Xcode „Update to recommended settings” figyelmeztetést ad: elfogadhatod, nem árt.

## 3. Fordítás és kipróbálás

- Scheme: **ClaudeUsageMonitor**, cél: **My Mac**. ⌘B fordít, ⌘R indít.
- Az app **menüsor-ikonként** indul (nincs Dock-ikon), és a jobb felső sarokban megjelenik a panel.
  Első indításkor a **Beállítások** ablak nyílik meg a *Data source* fülön.
- Három adatforrás van:
  1. **Local log** – a Claude Desktop naplója. A sandbox miatt egyszer **engedélyezni** kell:
     *Grant access…* → a Megnyitás panel a `~/Library/Application Support/Claude/` mappában nyílik →
     válaszd a `plan-usage-history.json` fájlt. (Ehhez a Claude asztali app legyen telepítve és
     fusson, különben nincs fájl.)
  2. **claude.ai (all devices)** – bejelentkezés a saját böngésződben, kód beillesztése (mint
     Windowson). Csak akkor látszik, ha a `CLAUDE_SIGN_IN` fordítási feltétel be van kapcsolva
     (alapból be van).
  3. **Demo data** – generált mintaadatok, fiók és Claude app nélkül. **Ezt látja az Apple
     ellenőre** (lásd 6. pont, App Review notes).
- Naplók: `~/Library/Containers/hu.dinorr.claudeusagemonitor/Data/Library/Application Support/ClaudeUsageMonitor/`
  (`startup.log`, `api.log`) – vagy Beállítások → System → *Open settings folder*.

Ha a fordítás hibával áll meg: a GitHub Actions „Xcode build” futása (Actions fül a repón) ugyanezt a
projektet fordítja a GitHub Macjén – ha ott zöld, a különbség a te géped (Xcode-verzió, Team).
A hibát küldd el Gábornak (a teljes szöveget, az Xcode Report navigatorból: ⌘9).

## 4. Amit valódi Macen tesztelni kell (Gábor Mac nélkül írta)

Menj végig ezen, és ami nem jó, azt írd meg (képernyőképpel):

- [ ] a panel megjelenik, **mindig felül** marad más appok fölött is; teljes képernyős app mellett is látszik
- [ ] húzható egérrel, a képernyő széléhez pattan; a pozíciót újraindítás után is tudja
- [ ] jobb gomb a panelen és a menüsor-ikonon → menü; bal kattintás az ikonon → panel el/elő
- [ ] dupla kattintás → Előzmények ablak, a grafikon rajzolódik
- [ ] Beállítások minden füle megnyílik, a kapcsolók azonnal hatnak a panelre
- [ ] *Grant access…* → a kiválasztás után a panel adatot mutat, és **újraindítás után is** (könyvjelző)
- [ ] Demóadatok: panel, részletlista, plan-jelvény, előzmények mind látszanak
- [ ] claude.ai bejelentkezés: a böngésző megnyílik, a kód beillesztése után a panel szerveradatot mutat; újraindítás után is be van jelentkezve (Keychain – első alkalommal a rendszer rákérdezhet)
- [ ] értesítés: Beállítások → Alerts küszöb állítása lefelé (pl. 1 %) után jön banner; az első alkalommal a rendszer engedélyt kér
- [ ] *Start at login* bekapcsolása → System Settings → General → Login Items-ben megjelenik; ki/be-jelentkezés után tényleg elindul
- [ ] nyelvváltás a menüből (pl. Magyar, 日本語): panel, menü, ablakok átváltanak; CJK betűk rendben
- [ ] *Click-through* bekapcsolva a panel átengedi a kattintást; visszakapcsolni a menüsor-ikon menüjéből lehet
- [ ] Retina kijelzőn éles minden; sötét és világos rendszertéma mellett is olvasható a menü
- [ ] Üzenet a fejlesztőnek: elküldés működik (megérkezik Gáborhoz)

## 5. App Store Connect – az app rekordjának létrehozása

<https://appstoreconnect.apple.com> → **My Apps** → **+** → **New App**

| Mező | Érték |
|---|---|
| Platforms | macOS |
| Name | **Claude Usage Monitor** (Gábor döntése: egyelőre ez; lásd MEGFELELES.md 2. pont a kockázatról) |
| Primary Language | English (U.S.) |
| Bundle ID | `hu.dinorr.claudeusagemonitor` (a listából) |
| SKU | `claudeusagemonitor-mac` (bármi egyedi, nem látszik) |
| User Access | Full Access |

Ha a név foglalt, az ASC szól. Alternatíva: „Claude Usage Monitor – Panel”, vagy **KÉRDEZD GÁBORT**.

## 6. Metaadatok (App Information, az 1.0-s verzió oldala)

**App Information**
- Subtitle (30 karakter): `Session & weekly limits, live` (vagy **KÉRDEZD GÁBORT**)
- Category: Primary **Developer Tools**, Secondary **Utilities**
- Content Rights: *does not contain, show, or access third-party content* → **No** (nem tartalmaz
  harmadik fél tartalmát) – az app csak a felhasználó saját számait mutatja.
- Age Rating: töltsd ki a (2026-os, új) kérdőívet – mindenre „None/No” → **4+**.
- License Agreement: Apple Standard EULA (hagyd).

**Version Information (1.0 / 2.9.0)**
- Promotional Text (opcionális): egy mondat, amit review nélkül cserélhetsz.
- Description: a weboldal angol szövegéből (<https://claudeusagemonitor.com/>) – **KÉRDEZD GÁBORT**,
  ő adja a végleges szöveget. Írd bele: *independent tool, not affiliated with Anthropic*.
- Keywords (100 byte): `usage,monitor,limit,quota,session,weekly,menu bar,panel,tokens,rate limit`
  **Ne** írd bele, hogy `Claude` vagy `Anthropic` – más cég/app nevét az ASC szabály tiltja a kulcsszavakban.
- Support URL: `https://claudeusagemonitor.com/` (az oldalon van kapcsolati űrlap – az Apple elvárja, hogy tényleges elérhetőség legyen rajta)
- Marketing URL: `https://claudeusagemonitor.com/`
- Privacy Policy URL (**App Privacy** szekcióban): `https://claudeusagemonitor.com/#privacy`
- Copyright: `2026 Vidovics Gábor`
- Version: `2.9.0` (= MARKETING_VERSION), Build: a feltöltött build.
- **App Review Information:**
  - Contact: a te neved, telefonod nemzetközi formátumban (+36…), e-mail címed.
  - Sign-in required: **No** (nincs kötelező bejelentkezés – a demó és a helyi napló fiók nélkül megy).
  - **Notes** – másold be (angolul, kiegészítve ha kell):

    ```
    Claude Usage Monitor is an independent, open-source utility (MIT, source on GitHub) that shows the
    user's OWN usage of their Claude subscription as an always-on-top panel and menu bar item. It is not
    made by or affiliated with Anthropic.

    HOW TO TEST WITHOUT AN ACCOUNT: the app has a built-in DEMO MODE (Guideline 2.1(a)). On first launch
    the Settings window opens on the "Data source" tab: choose "Demo data – no account needed". Every
    part of the UI (panel, three layouts, six themes, details list, history window, alerts, 34 languages)
    works with the demo data. Nothing is fetched or sent in demo mode.

    The other two sources are optional: (1) reading the local usage log of the Claude desktop app, which
    the user selects once in an Open panel (sandbox, security-scoped bookmark); (2) the user's own
    claude.ai sign-in in their browser. No demo account can be provided for a Claude subscription, as it
    is a third-party service tied to a personal account; the demo mode is provided instead.

    Launch at login is OFF by default and only registered (SMAppService) when the user turns it on.
    Notifications are requested only when the first alert is due. No analytics, no tracking, no ads,
    no in-app purchases. The optional "Message to the developer" form sends only what the user types,
    to the developer's own website, after explicit consent.
    ```

**App Privacy** (Data Collection)
- Válasz: **Data Not Collected** → az app semmit nem gyűjt (a használati adatok csak megjelennek, nem
  mennek sehova; az üzenetküldő űrlap önkéntes, ritka, külön hozzájárulással – ez az Apple „optional
  disclosure” kivétele). Ha az Apple rákérdez, írd le ugyanezt.

**Pricing and Availability**
- Price: **Free**. Availability: minden ország. (Ingyenes, nincs IAP.)

**EU Digital Services Act (Business → Trader status)** – az **Account Holder** nyilatkozik:
- Ingyenes hobbi app, nincs bevétel → „**I am not a trader**” választható; ekkor az EU-s boltokban egy
  megjegyzés jelenik meg, hogy fogyasztóvédelmi jogok nem érvényesülnek. Ha „trader”-nek nyilatkozik,
  a cím/telefon/e-mail nyilvánosan megjelenik az összes EU-s áruházban. **KÉRDEZD GÁBORT.**

**Accessibility Nutrition Labels** (még önkéntes, de töltsd ki, ha látod): Dark Interface ✓,
Sufficient Contrast ✓ (a témák nagy kontrasztúak), a többi –.

## 7. Képernyőképek (kötelező)

- macOS-hez **16:10**, az engedélyezett méretek egyike: **2880 × 1800** (Retina), 2560 × 1600,
  1440 × 900 vagy 1280 × 800. PNG vagy JPEG, **alfa nélkül**. 1–10 kép.
- Készítsd a demóadatokkal, különböző elrendezés/téma: post-it (midnight), rings (claude), slim bar,
  Előzmények ablak, Beállítások.
- ⇧⌘5 → terület → a kész PNG-t a Preview-ban (Tools → Adjust Size) hozd a pontos méretre, vagy
  készíts a teljes képernyőről (Retina 13"/14" MacBook: 2560×1600 / 3024×1964 → méretezd 2880×1800-ra).
- Alfa-csatorna eltávolítása: Preview → File → Export → „Alpha” pipa ki.

## 8. Archiválás és feltöltés

1. Xcode: Product → **Archive** (a scheme Release konfigurációban archivál).
2. Organizer (Window → Organizer) → az archív → **Distribute App** → **App Store Connect** → **Upload**.
   Hagyd bekapcsolva: *Upload your app's symbols*, *Manage Version and Build Number* (ez növeli a
   build-számot, ha ütközik).
3. Az Xcode aláír („Apple Distribution” tanúsítvány + „Mac App Store Connect” profil) és feltölt.
   Ha hiányzik tanúsítvány, az automatikus aláírás létrehozza (ehhez a csapatban Admin/Account Holder
   kell – ha nem te vagy, **KÉRDEZD GÁBORT**, vagy ő hozza létre a tanúsítványt a Certificates oldalon).
4. 5–30 perc múlva az ASC-ben a build „Processing” → kész. E-mailben jöhet figyelmeztetés
   (pl. hiányzó usage description) – küldd el Gábornak.

Ismert buktatók:
- **ITMS-90xxx „Invalid bundle”/quarantine**: ne másold a kész .app-ot Finderrel más gépről – mindig a
  saját Xcode-od archiválja.
- **Hiányzó export compliance kérdés**: az `ITSAppUsesNonExemptEncryption = NO` benne van az
  Info.plist-ben, így nem kérdez.

## 9. TestFlight (ajánlott, nem kötelező)

ASC → TestFlight fül → a build mellé **Internal Testing** csoport (te + Gábor Apple ID-ja, max. 100 fő)
→ a TestFlight for Mac appból telepíthető, 90 napig. Így Gábor is látja, mielőtt beadod.

## 10. Beadás ellenőrzésre

A verzió oldalán: válaszd ki a buildet → **Add for Review** → **Submit to App Review**.
Jellemzően 1–3 nap. Az eredmény e-mailben és az ASC-ben jön.

## 11. Ha elutasítják (Resolution Center)

Küldd el Gábornak **szó szerint** az elutasítás szövegét (guideline-szám + indoklás). A várható esetek
és a válaszok a [MEGFELELES.md](MEGFELELES.md) végén vannak (pl. 5.2.1 védjegy → név/ikon;
2.1 → a demó mód leírása; 2.4.5 → sandbox/entitlement kérdés). Válaszolni a Resolution Centerben
lehet, új build nélkül is, ha csak szöveg/metaadat a kifogás.

## 12. Új verzió kiadása

1. Gábor kiad Windowsra, frissíti a `MARKETING_VERSION`-t a `project.pbxproj`-ban és a fordításokat
   (`Localizable.xcstrings`), és szól.
2. `git pull` → Xcode: General → **Build** szám +1 → Archive → Upload.
3. ASC: **+ Version** → a „What's New” szöveg (Gábor adja, a `release/notes/<verzió>.json` angol
   részéből) → build kiválasztása → Submit.

A release notes szövege a Windows-éval közös; más nyelvekre az ASC-ben a lokalizált
„What's New”-t ugyanabból a JSON-ból lehet bemásolni (hu, de, fr, …).
