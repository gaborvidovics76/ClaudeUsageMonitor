# Mac App Store – megfelelés: mit követel az Apple, mit csináltunk, mi a kockázat

Kutatás dátuma: **2026. október 12.** A hivatkozott Apple-oldalak változhatnak; beadás előtt a
„Upcoming requirements” oldalt érdemes újra megnézni: <https://developer.apple.com/news/upcoming-requirements/>

Jelmagyarázat: ✅ megoldva a projektben · ⚠️ döntést/figyelmet igényel · ❌ nem teljesíthető/nyitott

---

## 1. ⚠️ A claude.ai-bejelentkezés és az Anthropic feltételei – A LEGNAGYOBB KOCKÁZAT

**Mit találtunk.** Az Anthropic jogi oldala (Claude Code „Legal and compliance”) kimondja: harmadik
fél fejlesztője *nem gyűjthet, tárolhat vagy közvetíthet Claude.ai belépési adatokat vagy
munkamenet-tokeneket*, és *nem kínálhat Claude.ai-bejelentkezést a saját alkalmazásában*, illetve
*nem irányíthat kéréseket Free/Pro/Max előfizetés hitelesítő adatain át*. A fogyasztói ÁSZF (2025.
október 8.) 3. pontja tiltja a szolgáltatás „automatizált vagy nem emberi” elérését és a fiók
belépési adatainak megosztását. 2026 februárjában az Anthropic már fel is lépett ilyen harmadik féltől
származó eszközök ellen (The Register, 2026-02-20).

Források: <https://code.claude.com/docs/en/legal-and-compliance> ·
<https://www.anthropic.com/legal/consumer-terms> ·
<https://www.theregister.com/2026/02/20/anthropic_clarifies_ban_third_party_claude_access/>

**Mit jelent ránk nézve.** Az app claude.ai-forrása pontosan ezt teszi: a Claude Code nyilvános OAuth
kliensével jelentkezik be, a tokent a Keychainben tárolja, és az `api.anthropic.com/api/oauth/usage`
végpontot kérdezi – ugyanúgy, mint a Windows-verzió. Az Apple ellenőre ezt az **5.2.1** (harmadik fél
szellemi tulajdona/feltételei) vagy az **5.1.1(v)** (harmadik fél tokenjeinek tárolása) alapján
kifogásolhatja, és az Anthropic is kérheti az eltávolítását.

**Mit csináltunk.** A teljes claude.ai-ág a `CLAUDE_SIGN_IN` fordítási feltétel mögött van
(`SWIFT_ACTIVE_COMPILATION_CONDITIONS`). Alapból **bekapcsolva** – ez Gábor döntése, mert a Windows-app
ugyanezt csinálja. A feltétel törlésével egy perc alatt készül a „store-biztos” változat (helyi napló
+ demó), kódmódosítás nélkül. Az app soha nem tölti fel a tokent sehová (5.1.1(v) ezt tiltja), csak a
Keychainben tartja és az Anthropic szerverével beszél vele.

**Ajánlás.** Beadás előtt Gábor döntse el: (a) beadás a bejelentkezéssel, vállalva az elutasítás
kockázatát; (b) első beadás a kapcsoló nélkül, és ha átmegy, később egy frissítésben próbálni;
(c) megkérdezni az Anthropicot (marketing@anthropic.com / a legal oldalon megadott cím).
A **helyi napló olvasása** (a Claude asztali app saját fájlja a felhasználó lemezén) **nem** esik
ezek alá.

Megjegyzés: a token-végponthoz az app a hivatalos parancssori kliens `User-Agent` fejlécét küldi
(a Windows-verzióval azonosan, mert a Cloudflare másként blokkol). Ez „a hivatalos kliensnek
kiadni magát” típusú kifogásra is alapot adhat; a kapcsoló ezt is kiveszi.

## 2. ⚠️ Védjegy: a „Claude” név és a logó (5.2.1)

- A **CLAUDE** az Anthropic bejegyzett védjegye (US Reg. 7645254). Az Anthropic védjegy-irányelve
  szerint a márkanevet csak előzetes jóváhagyással lehet használni; a Claude Code jogi oldal szerint
  plain textben mondható, hogy egy termék „Claude-dal működik”, de a név **nem lehet a saját termék
  nevének része**, és a logó/annak utánzata nem használható.
- Az App Store 5.2.1: „don't use protected third-party material such as trademarks … without
  permission”. Az Apple tipikusan a jogtulajdonos panaszára cselekszik, de az ellenőr magától is
  kérhet engedély-igazolást.
- **Döntés (Gábor, 2026-10-12): egyelőre marad a „Claude Usage Monitor” név**, mert az App Store-ban
  több hasonló nevű app is él. A projektben a név egyetlen helyen van (`APP_DISPLAY_NAME` build
  setting a `project.pbxproj`-ban), tehát elutasítás esetén egy sor módosítás: pl.
  „Usage Monitor for Claude” vagy teljesen semleges név.
- ✅ Az **ikon** viszont már nem a narancs csillag (az a Claude-logó formája): semleges mérőóra-ikon
  (`tools/make_icon.py`). A panel fejlécében a „CLAUDE USAGE” felirat leíró szöveg, a Súgóban ott a
  „Claude is a trademark of Anthropic” nyilatkozat, az Info.plist copyrightjában is.
- Kulcsszavak az ASC-ben: **ne** szerepeljen „Claude”/„Anthropic” (más cég neve tiltott a
  keywords mezőben); a leírásban leíró módon igen.

Források: <https://www.anthropic.com/legal/trademark-guidelines> ·
<https://code.claude.com/docs/en/legal-and-compliance> ·
<https://developer.apple.com/app-store/review/guidelines/>

## 3. ✅ App Sandbox és fájlhozzáférés (2.4.5(i))

- A sandbox a Mac App Store-ban **kötelező**. Entitlements: `app-sandbox`, `network.client`,
  `network.server`, `files.user-selected.read-only`. Más nincs.
- `network.server` (2026-10, az első elutasítás után): az App Review a claude.ai-bejelentkezést csak
  `ASWebAuthenticationSession`-nel fogadja el (Guideline 4 – az alapértelmezett böngészőbe küldeni a
  felhasználót nem elfogadott). A rendszer bejelentkező lapja a kódot a `http://localhost:<port>/callback`
  címre küldi vissza (a Claude Code nyilvános kliense erre van regisztrálva, a CLI maga az 54545-ös
  portot használja); ezt az app saját, `Network.framework`-ös figyelője fogadja (`Data/LoopbackServer.swift`),
  amely csak a loopback-interfészre kötődik, csak a bejelentkező lap nyitva léte alatt él, és egyetlen
  kérést szolgál ki. A sandbox e jogosultság nélkül nem enged figyelő socketet nyitni. Ha a port nem
  nyitható, az app az Anthropic kódmutató oldalára esik vissza (kézi beillesztés, mint Windowson).
- A Claude Desktop naplója (`~/Library/Application Support/Claude/plan-usage-history.json`) és a
  Claude Code mappája (`~/.claude`) a sandboxon kívül van. Az Apple „temporary exception”
  entitlementjeit (home-relative-path) a bírálat **nem fogadja el** (Apple DTS: „very dim view”;
  más projekt tapasztalata: „never be approved”). Ezért: a felhasználó **egyszer kiválasztja** a
  fájlt/mappát az NSOpenPanelben, az app **security-scoped bookmark**-ként megjegyzi, és minden
  olvasás `startAccessingSecurityScopedResource` / `stop…` között történik (`Data/Bookmarks.swift`).
- Keychain: SecItem a data-protection keychainnel (`kSecUseDataProtectionKeychain`), saját
  hozzáférési csoport – külön entitlement nem kell (TN3137).
- Hardened Runtime: az App Store-hoz nem kötelező (csak a notarizáláshoz), de be van kapcsolva, nem
  zavar.

Források: <https://developer.apple.com/documentation/security/app-sandbox> ·
<https://developer.apple.com/documentation/security/accessing-files-from-the-macos-app-sandbox> ·
<https://developer.apple.com/documentation/technotes/tn3137-on-mac-keychains> ·
<https://developer.apple.com/forums/thread/663311>

## 4. ✅ Minimum funkcionalitás, demó mód (2.1(a), 4.2, 4.2.3)

- 4.2.3(i): az app **ne igényelje másik app telepítését**. A helyi napló Claude Desktopot kíván, a
  claude.ai fiókot – ezért van a **Demóadatok** forrás (`Data/DemoSource.swift`): fiók és másik app
  nélkül a teljes felület kipróbálható. Ez egyben a 2.1(a) „built-in demo mode in lieu of a demo
  account” megoldása, mert Claude-fiókot demóként átadni az Anthropic ÁSZF-be ütközne.
- Az App Review Notes-ban ezt le kell írni (sablon az APP-STORE-BEADAS.md 6. pontjában).

## 5. ✅ Önfrissítés tilos (2.4.5(vii)), telepítő, kód-letöltés

- A Windows-app önfrissítője (manifest, SHA-256, csere) **kimaradt**: a frissítés az App Store-on át
  jön. A Súgó szövegéből a „Updates” és a „Backups” szakasz programból ki van vágva, helyette
  Mac-specifikus szöveg.
- Csak Xcode-dal csomagolt .pkg kerül feltöltésre (nincs harmadik fél telepítő) – ez az Organizer
  alapértelmezése.

## 6. ✅ Indítás bejelentkezéskor (2.4.5(iii))

- `SMAppService.mainApp` (macOS 13+), **alapból kikapcsolva**, csak a felhasználó kérésére
  regisztrál; ha a rendszer jóváhagyást kér, megnyitja a System Settings → Login Items panelt. Az app
  nem regisztrál újra magától (a felhasználó kikapcsolását tiszteletben tartja).
- `LSUIElement = true` (menüsor-app Dock-ikon nélkül) – bevett, nincs rá tiltás. Opcionálisan
  Dock-ikon kapcsolható (activation policy).

Forrás: <https://developer.apple.com/documentation/servicemanagement/smappservice>

## 7. ✅ Értesítések

`UNUserNotificationCenter`; az engedélyt **nem indításkor**, hanem az első esedékes értesítésnél
kéri (ez a jobb gyakorlat, és nem bosszantja az ellenőrt).

## 8. ✅ Privacy manifest, App Privacy címke (5.1.1)

- `Resources/PrivacyInfo.xcprivacy`: nincs tracking, nincs gyűjtött adat; „required reason” API-k:
  UserDefaults **CA92.1**, fájl-időbélyeg **C617.1 + 3B52.1** (saját konténer + felhasználó által
  kiválasztott fájl). Az Apple szövege szerint a required-reason követelmény az iOS-családra
  vonatkozik, macOS-re nem kötelező – a manifest így is benne van (ártalmatlan, jövőbiztos).
- App Privacy a Connectben: **Data Not Collected**. A „gyűjtés” az Apple definíciója szerint az
  eszközről kifelé továbbítás a fejlesztőhöz/harmadik félhez. A használati adatok csak megjelennek. Az
  „Üzenet a fejlesztőnek” űrlap önkéntes, ritka, nem elsődleges funkció, kifejezett hozzájárulással –
  ez az Apple „optional disclosure” kivétele.
- Adatvédelmi irányelv linkje **kötelező** az ASC-ben és az appban is: `https://claudeusagemonitor.com/#privacy`
  (Súgó → Szerző fül, és az üzenetküldő ablak). ✅

Források: <https://developer.apple.com/documentation/bundleresources/privacy-manifest-files> ·
<https://developer.apple.com/app-store/app-privacy-details/>

## 9. ✅ Export compliance (titkosítás)

`ITSAppUsesNonExemptEncryption = NO` az Info.plist-ben: csak az OS beépített HTTPS-ét (URLSession) és
a Keychaint használja → mentes, dokumentáció nem kell, francia nyilatkozat sem.
Forrás: <https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations>

## 10. ✅ Lokalizáció (2.4.5(ix))

- Mind a 34 nyelv **egy bundle-ben**, String Catalogból (`Localizable.xcstrings`) fordított
  `<nyelv>.lproj` mappákként. Az App Store „Languages” listája ezekből az lproj-mappákból áll össze
  (nem a CFBundleLocalizations-ból, nem az ASC-metaadatokból).
- A nyelvet futás közben is lehet váltani (a menüből), ezért a szövegeket az app a kiválasztott
  `.lproj` bundle-ből olvassa (`Core/Localization.swift`), a Windows-app visszaesési láncával
  (variáns → testvérváltozat → angol).
- ASC-metaadat (leírás, kulcsszavak) külön lokalizálható az ASC 50 nyelvén (magyar is van).

Forrás: <https://developer.apple.com/forums/thread/813504>

## 11. ✅ Xcode-verzió, SDK, architektúra

- 2026. április 28. óta az ASC **Xcode 26**-ot kér (az iOS-családra kimondva; macOS-re nincs külön
  szabály). Jelenleg Xcode 26.x és 27.x is elfogadott; az Xcode 27 macOS 26.6+-t igényel.
- Deployment target: **macOS 13 Ventura** (SMAppService és a használt SwiftUI API-k miatt);
  univerzális (Apple Silicon + Intel) build.
- Feltöltés előtt a bundle-ben ne legyen `com.apple.quarantine` attribútum (az Xcode saját archívuma
  rendben van; idegen gépről másolt .app nem).

Források: <https://developer.apple.com/news/upcoming-requirements/> ·
<https://developer.apple.com/help/app-store-connect/release-notes/>

## 12. ✅ App Store Connect metaadatok, képernyőképek, korhatár

Részletesen az APP-STORE-BEADAS.md 5–7. pontjában. Röviden: képernyőkép 16:10 (2880×1800 stb.,
alfa nélkül); ikon 1024×1024 (asset catalogban, kész); Support URL valódi elérhetőséggel; az új
korhatár-kérdőív (2026. január 31. óta kötelező) → 4+; kulcsszavakban más cég neve tilos.

## 13. ⚠️ EU DSA „trader” nyilatkozat

2025. február 17. óta az EU-ban csak az az app elérhető, amelynek fejlesztője nyilatkozott.
Ingyenes, bevétel nélküli hobbi app → **„nem kereskedő”** választható (az EU-s boltokban megjegyzés
jelenik meg); ha „kereskedő”, a cím/telefon/e-mail nyilvános. Az **Account Holder** nyilatkozik.
Forrás: <https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements>

## 14. ℹ️ Egyéb 2025–26-os változások

- Accessibility Nutrition Labels: egyelőre önkéntes, később kötelező lesz – az app sötét felületet
  és nagy kontrasztot ad; VoiceOver-feliratok a panelen nincsenek (rajzolt nézet), ez később teendő.
- Apple Intelligence-nyilatkozat: nem találtunk ilyen követelményt; az app nem használ ilyet.
- macOS 27 csak Apple Silicon; 2026. június óta elhagyható az Intel, de a projekt univerzális marad.

## 15. ❌ / ⚠️ Nyitott pontok Gábornak

1. **claude.ai-bejelentkezés:** benne maradjon-e az App Store-os buildben (1. pont). Ez a döntő kérdés.
2. **Név:** marad „Claude Usage Monitor” (döntés megvan), de ha 5.2.1-es elutasítás jön, a B-terv a
   semleges név.
3. **Fejlesztői fiók:** kié (Gáboré vagy a kollégáé)? Ettől függ a Team, a tanúsítvány és a DSA-nyilatkozat.
4. **App Store ID:** amint az ASC-ben létrejön az app, a numerikus ID-t az `AppInfo.appStoreID`-be
   (`Core/Settings.swift`) beírva megjelenik az „Értékelés az App Store-ban” menüpont.
5. **Weboldal:** a `claudeusagemonitor.com/macos/` oldalon jelenleg „coming soon”; az App Store-link
   (és esetleg az App Store badge) kerül oda a megjelenés után.

## Várható elutasítási okok és a válasz

| Guideline | Mit ír az Apple | Mit tegyünk |
|---|---|---|
| 2.1 – nem tudták tesztelni | „We were unable to sign in / the app shows no data” | Resolution Centerben: a demó mód leírása (Settings → Data source → Demo data), képernyőképpel. |
| 2.4.5 – sandbox/entitlement | „uses entitlement X” | Nincs kivétel-entitlement; a user-selected read-only + bookmark a szabályos út – leírni. |
| 4.2 – minimális funkcionalitás | „limited functionality” | A három forrás, az előzmények, riasztások, 34 nyelv – leírás + a demó. |
| 5.1.1 – adatvédelem | privacy policy link / adatgyűjtés | A link az appban és az ASC-ben; Data Not Collected indoklása. |
| 5.2.1 – védjegy | „uses the name/logo of Claude without authorization” | B-terv: `APP_DISPLAY_NAME` semleges név, a leírásban csak „works with Claude”; ikon már semleges. Ha az Anthropic adott engedélyt, azt feltölteni. |
| 5.2.x / 5.1.1(v) – harmadik fél tokenje | „stores third-party credentials / violates third-party terms” | `CLAUDE_SIGN_IN` feltétel törlése, újra beadás (helyi napló + demó). |
