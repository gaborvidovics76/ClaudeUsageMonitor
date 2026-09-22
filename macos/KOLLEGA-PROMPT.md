# Bemásolható prompt a Claude Code-hoz (macOS)

Nyisd meg a Terminált, lépj be a projektmappába, indítsd a Claude Code-ot, és másold be az alábbi
promptot. A `---` vonalak közötti rész a prompt; a vonalakat ne másold.

> Ha a Claude Code megkérdezi, hogy megbízol-e a mappa fájljaiban („Do you trust the files in this
> folder?”), válaszd az igent: ez a projekt saját forrása, a beállításai a repóban vannak.

---

## 1. Prompt – magyarul

```text
Szia! Ebben a projektmappában a "Claude Usage Monitor" nevű nyílt forrású program forrása van
(MIT licenc, GitHub: gaborvidovics76/ClaudeUsageMonitor). Én vagyok a macOS-változat karbantartója;
a projekt gazdája Windowson fejleszti, én Macen fordítom és publikálom ugyanabból a forrásból.

A feladatom most: kiadni a macOS-változat legfrissebb verzióját.

Mielőtt bármit csinálsz, olvasd el ezeket a fájlokat, mert minden lényeges bennük van:
  - CLAUDE.md                      (a projekt kontextusa, ki mit birtokol, mik a szabályok)
  - macos/UJ-DOMAIN-KOLLEGA.md     (a mostani kiadási rend, a domainköltözés után)
  - macos/KEZDD-ITT.md             (a teljes macOS-kézikönyv)

Fontos tudnivalók, hogy ne lepődj meg:
- A claudeusagemonitor.com ENNEK a programnak a saját weboldala, a projekt gazdájáé. A hivatkozás
  oda-vissza megvan: a repó az oldalra mutat, az oldal a repóra. A kiadás publikálása oda a projekt
  normál, szándékolt működése, ugyanaz, amit a Windows-oldali release.ps1 csinál.
- A feltöltés sima FTPS (curl --ssl-reqd) egy olyan fiókkal, ami KIZÁRÓLAG a macos/ mappát látja.
  A DCB-Native hídfőre NINCS szükség, és ne is használd ehhez.
- A hitelesítő adatok a macos/release.local.env fájlban vannak, ami git-ignorált. NE nyisd meg,
  ne írd ki a tartalmát, ne másold sehova - a szkript magától beolvassa.

Amit kérek tőled, ebben a sorrendben:

1. Ellenőrizd, hogy minden eszköz megvan-e a fordításhoz (Python 3.10+, Xcode command line tools).
   Ha valami hiányzik, mondd meg, mit telepítsek.
2. Futtasd: ./macos/release.sh
   Ez lehúzza a legfrissebb forrást a gitről, lefordítja az appot, becsomagolja, feltölti az
   elsődleges oldalra (claudeusagemonitor.com) és - ha a beállításfájlban szerepel - a régi
   címre is, végül HTTPS-en ellenőrzi mindkettőt.
3. Ha a szkript hibával áll meg, olvasd el a hibaüzenetet, és mondd meg, mi a teendő. Ha nem
   egyértelmű, futtasd a ./macos/doctor.sh parancsot, és foglald össze, mit találtál.
4. A végén foglald össze röviden: melyik verzió ment ki, milyen architektúrára, mekkora a csomag,
   egyezik-e a SHA-256 az élő oldalon, és hogy a régi csatornára ment-e fel valami.

Amit NE csinálj:
- ne változtasd meg a verziószámot (a claude_usage/__init__.py-ból jön, a projekt gazdájáé);
- ne tolj a main ágra (ha javítanál valamit: macos/<téma> ág + Pull Request, vagy patch-fájl);
- ne írj a macos/ mappán kívülre a szervereken;
- ne indítsd magad engedélyek megkerülésével.

Ha bármihez engedélyt kérsz, én jóváhagyom. Kezdheted.
```

---

## 2. Prompt – English

```text
Hi! This folder holds the source of an open-source program called "Claude Usage Monitor"
(MIT licence, GitHub: gaborvidovics76/ClaudeUsageMonitor). I maintain the macOS build: the project
owner develops on Windows, I build and publish the macOS version from the same source.

My task now: publish the latest macOS release.

Before doing anything, read these files - everything important is in them:
  - CLAUDE.md                      (project context, who owns what, the rules)
  - macos/UJ-DOMAIN-KOLLEGA.md     (the current release setup after the domain move; Hungarian)
  - macos/START-HERE.md            (the macOS handbook in English)

Context so nothing surprises you:
- claudeusagemonitor.com is THIS program's own website, owned by the project owner. The link goes
  both ways and can be checked: the repository points at the site, the site points back at the
  repository. Publishing a release there is this project's normal, intended operation - the same
  thing the Windows release.ps1 does.
- Uploading is plain FTPS (curl --ssl-reqd) with an account confined to the macos/ folder only.
  The DCB-Native bridge is NOT needed and must NOT be used for this.
- Credentials live in macos/release.local.env, which is git-ignored. Do NOT open it, print it or
  copy it anywhere - the script reads it by itself.

What I would like you to do, in this order:

1. Check that the build tools are in place (Python 3.10+, Xcode command line tools). Tell me what
   to install if something is missing.
2. Run: ./macos/release.sh
   It pulls the latest source, builds the app, packages it, uploads to the primary site
   (claudeusagemonitor.com) and - if configured - to the legacy address as well, then verifies
   both over HTTPS.
3. If the script stops with an error, read it and tell me what to do. If it is not obvious, run
   ./macos/doctor.sh and summarise what you found.
4. At the end give me a short summary: which version went out, for which architecture, the package
   size, whether the SHA-256 matches on the live site, and whether anything went to the legacy
   channel.

What NOT to do:
- do not change the version number (it comes from claude_usage/__init__.py and belongs to the owner);
- do not push to main (fixes go on a macos/<topic> branch as a Pull Request, or as a patch file);
- do not write anywhere outside the macos/ folder on the servers;
- do not run yourself with permission checks disabled.

I will approve anything you ask permission for. Go ahead.
```

---

## 3. Rövid prompt későbbre (ha már egyszer lefutott)

```text
Add ki a legfrissebb macOS-verziót: ./macos/release.sh
A részletek a CLAUDE.md és a macos/UJ-DOMAIN-KOLLEGA.md fájlban vannak.
A végén mondd meg, milyen verzió ment ki és egyezik-e a SHA-256 az élő oldalon.
```

---

## 4. Ha a Claude Code mégis akadékoskodik

1. **Engedélykérésnél** válaszd: *Yes, and don't ask again*. A saját gépeden a
   `.claude/settings.local.json` fájlba menti, a repót nem érinti.
2. **Ha elutasított valamit** és utána makacs: indíts új munkamenetet (a tiltás munkamenetenként él).
3. **Nézd meg az engedélyeket:** a `/permissions` paranccsal látod és szerkesztheted a szabályokat.
4. **Ne kapcsold ki az engedélyeket** (`--dangerously-skip-permissions`): nincs rá szükség, és pont
   azt a védelmet venné le, amitől ez biztonságos.
5. A projekt `.claude/settings.json` fájlja már előre engedélyezi ennek a projektnek a saját
   domainjeit és a build/kiadás parancsait – ha ez valamiért nem érvényesül, nézd meg, hogy tényleg
   a projekt gyökeréből indítottad-e a Claude Code-ot.
