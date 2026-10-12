# Bemásolható prompt a Claude Code-hoz (macOS, Xcode-változat)

Nyisd meg a Terminált, lépj a projektmappába (`cd ClaudeUsageMonitor`), indítsd a Claude Code-ot
(`claude`), és másold be az alábbi promptot. A `---` vonalak közötti rész a prompt.

---

```text
Szia! Ebben a mappában a "Claude Usage Monitor" nyílt forrású program forrása van (MIT, GitHub:
gaborvidovics76/ClaudeUsageMonitor). Én vagyok a macOS-oldal: Macem és Xcode-om van, az én Apple
Developer fiókomból megy a Mac App Store-ba. A projekt gazdája (Gábor) Windowson fejleszt, Mac nélkül.

A natív macOS app Xcode-projektje a macos/Xcode/ mappában van. Mielőtt bármit csinálsz, olvasd el:
  - macos/Xcode/README.md                 (mi hol van, szabályok, a CLAUDE_SIGN_IN kapcsoló)
  - macos/Xcode/docs/APP-STORE-BEADAS.md  (a teljes beadási lépéssor)
  - macos/Xcode/docs/MEGFELELES.md        (Apple-követelmények, kockázatok)
  - CLAUDE.md                             (a projekt kontextusa)

Amit kérek, ebben a sorrendben:
1. Ellenőrizd az eszközöket: xcodebuild -version (Xcode 26+ kell), git.
2. Fordítsd le parancssorból, aláírás nélkül, hogy lássuk, lefordul-e ezen a gépen:
   xcodebuild -project macos/Xcode/ClaudeUsageMonitor.xcodeproj -scheme ClaudeUsageMonitor \
     -configuration Debug CODE_SIGNING_ALLOWED=NO build
   Ha hiba van, mutasd meg a hibát és javasolj javítást; a javítást macos/<téma> ágon készítsd.
3. Nyisd meg az Xcode-ban (open macos/Xcode/ClaudeUsageMonitor.xcodeproj), és mondd el, hol állítom
   be a Teamet (Signing & Capabilities). A DEVELOPMENT_TEAM-et NE írd be a repóba.
4. Indítsd el (⌘R) és menj végig velem az APP-STORE-BEADAS.md 4. pontjának tesztlistáján; amit nem
   tudsz te ellenőrizni, azt kérdezd meg tőlem.
5. Ha minden jó: vezess végig az App Store Connect rekord létrehozásán, a metaadatokon (az
   APP-STORE-BEADAS.md 5–7. pontja), az archiváláson és feltöltésen (8. pont). A review notes
   sablonját onnan másold.

Amit NE csinálj:
- ne változtasd a MARKETING_VERSION-t (a projekt gazdájáé); a build-számot (CURRENT_PROJECT_VERSION)
  csak feltöltés előtt növeld;
- ne tolj a main ágra (javítás: macos/<téma> ág + Pull Request);
- ne kapcsold ki a sandboxot, ne adj hozzá entitlementet, ne tegyél bele Sparkle-t vagy más frissítőt;
- a CLAUDE_SIGN_IN kapcsolót csak akkor vedd ki, ha Gábor kéri (MEGFELELES.md 1. pont).

Ha engedélyt kérsz valamihez, jóváhagyom. Kezdheted.
```

---

## English

```text
Hi! This folder holds the source of "Claude Usage Monitor" (MIT, GitHub: gaborvidovics76/ClaudeUsageMonitor).
I am the macOS side: I have the Mac, Xcode and the Apple Developer account for the Mac App Store. The
project owner (Gábor) develops on Windows without a Mac.

The native macOS app is the Xcode project in macos/Xcode/. Read first:
  - macos/Xcode/docs/START-HERE-XCODE.md
  - macos/Xcode/docs/APP-STORE-BEADAS.md (Hungarian; the step-by-step submission guide)
  - macos/Xcode/docs/MEGFELELES.md       (Hungarian; compliance research, English sources)
  - CLAUDE.md

Then: 1) check xcodebuild -version (Xcode 26+); 2) build unsigned from the command line
(xcodebuild -project macos/Xcode/ClaudeUsageMonitor.xcodeproj -scheme ClaudeUsageMonitor
 -configuration Debug CODE_SIGNING_ALLOWED=NO build) and fix errors on a macos/<topic> branch;
3) open the project in Xcode and tell me where to set the Team (never commit DEVELOPMENT_TEAM);
4) run it and walk me through the test list in APP-STORE-BEADAS.md §4; 5) guide me through the App
Store Connect record, metadata, archive and upload (§5–8).
Do not change MARKETING_VERSION, do not push to main, do not disable the sandbox or add entitlements,
do not add any updater, and do not remove the CLAUDE_SIGN_IN condition unless Gábor asks.
```
