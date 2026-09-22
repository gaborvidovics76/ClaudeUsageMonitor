# Új domain, új kiadási rend – macOS

**Neked szól, aki Macen fordítod és adod ki a programot.** Ez a lap azt írja le, mi változott a
domainköltözéssel, miért akadt meg a Claude Code, és mit kell tenned.

Kapcsolódó: [KEZDD-ITT.md](KEZDD-ITT.md) (teljes macOS-kézikönyv) · [KOLLEGA-PROMPT.md](KOLLEGA-PROMPT.md)
(bemásolható prompt) · [START-HERE.md](START-HERE.md) (English)

---

## 1. Mi változott

| | Régi | Új |
|---|---|---|
| Az app honlapja, letöltés | `https://dinorr.hu/claude-usage-monitor/` | **`https://claudeusagemonitor.com/`** |
| macOS-manifest (innen frissül az app) | `…/claude-usage-monitor/macos/manifest.json` | **`https://claudeusagemonitor.com/macos/manifest.json`** |
| Feltöltés | egy FTP-fiók a dinorr.hu-ra | **két fiók**: elsődleges (új domain) + átmeneti (régi domain) |

**A jövő: csak a `claudeusagemonitor.com` számít.** A régi cím egyetlen dolog miatt él még: a
költözés ELŐTT telepített példányok a régi manifestet kérdezik, és csak onnan találnak rá az új
verzióra. Amint ezek átálltak, a régi csatorna kikapcsolható – egy szerkesztés a beállításfájlodban,
lásd 4. pont.

A Windows-verzió már ezen a rendben megy (Gábor `release.ps1`-e mindkét helyre publikál); a macOS
mostantól ugyanígy működik.

---

## 2. Miért akadt meg a Claude Code – és mi az igazság

Fontos, hogy pontosan tudd, mi történt, mert ez nem valami „engedélyezési trükkel” oldódik meg:

**A Claude Code-ban nincs domain-hírnév-vizsgálat és nincs „hitelesített domain” fogalom.** Nem
létezik olyan mechanizmus, amivel egy DNS TXT rekorddal igazolni lehetne egy domaint a Claude felé.
Gábor felajánlotta, hogy tesz ki ilyen rekordot – erre **nincs szükség**, mert nem is nézi semmi.
(Nem is javítana semmit: bármelyik támadó ki tud tenni TXT rekordot a saját domainjére.)

Ami valójában történik:

1. **Engedélykérés.** A Claude Code minden új domainhez és sok parancshoz rákérdez. Ha egyszer
   „nem”-et kap, a munkamenetben onnantól tiltott marad.
2. **A modell saját mérlegelése.** Ha azt kérik tőle, hogy egy frissen regisztrált, számára ismeretlen
   domainre töltsön fel fájlokat – ráadásul a **DCB-Native** token-alapú, rejtőzködő hídfőn keresztül,
   ami képes bárhová fájlt írni a webgyökérben –, akkor jogosan húzza a száját. Kívülről nézve ez
   tényleg úgy fest, mint egy webshell-művelet egy idegen oldalon.

**A megoldás tehát az, hogy a művelet valóban legyen ártalmatlan, és a kontextus legyen egyértelmű:**

| Mi | Hogyan |
|---|---|
| A kiadáshoz **nem kell** a DCB-Native | a `release.sh` sima **FTPS**-sel (`curl --ssl-reqd`) tölt fel négy fájlt egy olyan fiókkal, ami **csak a `macos/` mappát látja**. Semmi máshoz nincs joga. |
| A projekt megmondja, kié a domain | `CLAUDE.md` a repó gyökerében: leírja, hogy a `claudeusagemonitor.com` ennek a programnak a saját oldala, és hogy a kiadás a projekt normál működése |
| Az engedélyek előre megvannak | `.claude/settings.json` a repóban: a projekt saját domainjei és a build/kiadás parancsai előre engedélyezve |
| Ellenőrizhető tulajdonlás | a hivatkozás **oda-vissza** megvan: a repó (README, az app frissítője) az oldalra mutat, az oldal pedig a GitHub-repóra. Ez bárki által ellenőrizhető, és ez ér valamit – nem egy TXT rekord. |

Ha a Claude Code mégis rákérdez valamire, az normális: válaszd a **„Yes, and don't ask again”**
lehetőséget. Ilyenkor a saját gépeden a `.claude/settings.local.json` fájlba menti (ez git-ignorált,
nem kerül vissza a repóba).

> **Amit ne csinálj:** ne indítsd a Claude Code-ot `--dangerously-skip-permissions` kapcsolóval.
> Nincs rá szükség, és pont azt a védelmet kapcsolná ki, amitől ez az egész biztonságos.

---

## 3. Amit egyszer be kell állítanod

```bash
cp macos/release.local.env.example macos/release.local.env
chmod 600 macos/release.local.env
open -e macos/release.local.env
```

Két blokk van benne:

- **PRIMARY (kötelező)** – `claudeusagemonitor.com`. Ide kell a Gábortól kapott új FTP-fiók
  (felhasználó + jelszó). Ez a fiók kizárólag a `macos/` mappát látja.
- **LEGACY (átmeneti, elhagyható)** – a régi domain. Ha megkapod hozzá a régi fiókot, töltsd ki;
  ha nem, hagyd üresen, és a szkript egyszerűen kihagyja.

A fájl **git-ignorált**: sosem kerül be a repóba. Ne küldd el senkinek, ne commitold.

---

## 4. A kiadás – egy parancs

```bash
./macos/release.sh
```

Amit csinál, sorban:

1. **`git pull`** – lehúzza a legfrissebb forrást (ha van helyi módosításod, kihagyja és szól).
2. **Fordítás** – `build.sh`: Python-környezet, ikon, PyInstaller, ad-hoc aláírás, indulás-teszt.
3. **Csomagolás** – `ditto`-val (a szimlinkek és futtatási jogok miatt), `ClaudeUsageMonitor-macOS-<verzió>-<arch>.zip`.
4. **Manifestek** – az elsődleges csatornához, és ha be van állítva, a régihez is (annak a letöltési
   címe szándékosan a régi hostra mutat, mert a régi telepítések azt kérik).
5. **Feltöltés** – FTPS-sel, előbb a csomag, utána a JSON-ok, **a manifest a legutolsó**, hogy sose
   mutasson olyan csomagra, ami még nincs fent.
6. **Ellenőrzés** – HTTPS-en visszaolvassa mindkét csatornát: egyezik-e a verzió, a SHA-256 és a
   csomag mérete. Ha nem, hibával megáll.

Hasznos kapcsolók: `--no-upload` (csak fordítás+csomagolás), `--skip-build`, `--no-pull`,
`--force` (csak ha Gábor kifejezetten kéri).

**A régi csatorna kikapcsolása** (amikor Gábor szól, hogy már nem kell): a
`macos/release.local.env`-ben töröld ki vagy ürítsd ki az `UM_LEGACY_…` sorokat. Ettől kezdve a
szkript csak az új domainre publikál – ez lesz a végállapot.

---

## 5. A szabályok, amik nem változtak

1. **A verziószámot nem te lépteted** – a forrásból jön (`claude_usage/__init__.py`).
2. **macOS-kiadás csak olyan verzióból**, ami Windowsra már megjelent – a szkript ellenőrzi az élő
   Windows-verziólistát, és mást visszautasít.
3. **Csak a `macos/` mappába töltesz fel.**
4. **A `main` ágra nem tolsz** – javítás: `macos/<téma>` ág + Pull Request, vagy
   `git format-patch main --stdout > javitas.patch` Gábornak.
5. **Közös kódhoz csak egyeztetve nyúlj.** Szabadon a tiéd: `macos/`, `claude_usage/macutil.py`,
   `secretstore_mac.py`, `updater_mac.py`, `i18n_mac.py`.

---

## 6. Ha valami nem megy

```bash
./macos/doctor.sh
```

Készít egy `macos-doctor-report.txt` fájlt (rendszer, verziók, fordítási napló, az app naplói).
**Jelszó és token nincs benne.** Ezt küldd el Gábornak.

Gyakori esetek:

| Tünet | Mi a teendő |
|---|---|
| `permission denied` a szkriptre | `chmod +x macos/*.sh` |
| a macOS nem engedi futtatni a letöltött fájlokat | `xattr -dr com.apple.quarantine .` a projektmappában |
| `UM_FTP_HOST: unbound variable` | nincs kitöltve a `macos/release.local.env` (3. pont) |
| `upload … failed` | rossz fiókadat, vagy a szerver nem enged FTPS-t – szólj Gábornak |
| `version … is not published for Windows yet` | Gábor még nem adta ki Windowsra; várd meg, vagy kérd tőle a `--force`-ot |
| a Claude Code rákérdez egy parancsra | válaszd: *Yes, and don't ask again* |
