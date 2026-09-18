# Claude Usage Monitor – macOS fordítás és kiadás

Ez a leírás neked szól, aki Macen fordítod és adod ki a programot. Gábor Windowson fejleszti;
a program forrása közös, a macOS-es részek ebben a `macos/` mappában vannak.

> **English version:** [START-HERE.md](START-HERE.md)

---

## 1. Fordítás – egy parancs

Nyisd meg a **Terminált**, lépj be ebbe a mappába (a kicsomagolt csomag vagy a git-klón gyökerébe), és:

```bash
./macos/build.sh
```

Ennyi. A szkript mindent megcsinál: megkeresi a Pythont, létrehoz egy saját, elkülönített
környezetet (`.venv-macos`), letölti a függőségeket, elkészíti az ikont, lefordítja az alkalmazást,
aláírja (ad-hoc), és ki is próbálja, hogy elindul-e. Az első futás néhány perc, a továbbiak gyorsak.

Az eredmény: **`dist-macos/ClaudeUsageMonitor.app`**

```bash
open dist-macos/ClaudeUsageMonitor.app        # kipróbálás
```

### Ami kell hozzá

| Mi | Hogyan |
|---|---|
| macOS 12 vagy újabb | – |
| Python 3.10+ | <https://www.python.org/downloads/macos/> telepítő, vagy `brew install python@3.12` |
| Xcode parancssori eszközök (a `codesign`, `iconutil` miatt) | `xcode-select --install` |

Ha a szkript azt írja, hogy valami hiányzik, megmondja azt is, hogyan pótold.

### Ha valami nem megy

```bash
./macos/doctor.sh
```

Ez egy `macos-doctor-report.txt` fájlt készít (rendszer, verziók, fordítási napló, a program naplói –
jelszó és token **nincs** benne). **Ezt küldd el Gábornak**, ebből látszik, mi a baj.

---

## 2. Új verzió érkezett – hogyan frissíts

Minden fejlesztés Gábortól indul. Amikor szól, hogy kiadott egy új verziót:

**Ha gitből dolgozol (ajánlott):**

```bash
git pull
./macos/release.sh
```

**Ha csomagot (zipet) kaptál:** csomagold ki az újat a régi helyére (a `macos/release.local.env`
fájlodat előtte mentsd ki, utána másold vissza), majd `./macos/release.sh`.

Az első alkalommal gitből így indulj:

```bash
git clone https://github.com/gaborvidovics76/ClaudeUsageMonitor.git
cd ClaudeUsageMonitor
./macos/build.sh
```

---

## 3. Kiadás a szerverre

```bash
./macos/release.sh
```

Lefordítja, becsomagolja (`ClaudeUsageMonitor-macOS-<verzió>-<arm64|x86_64>.zip`), feltölti, és a végén
HTTPS-en ellenőrzi, hogy az élő oldalon tényleg az van-e kint, amit feltöltött. A macOS-re telepített
példányok innentől maguktól felajánlják az új verziót.

Csak kipróbálnád, feltöltés nélkül: `./macos/release.sh --no-upload`

### Egyszeri beállítás: a feltöltő fiók

Gábortól kapsz egy FTP-fiókot, ami **csak** a szerver `claude-usage-monitor/macos` mappájába lát be.

```bash
cp macos/release.local.env.example macos/release.local.env
chmod 600 macos/release.local.env
open -e macos/release.local.env        # töltsd ki a felhasználónevet és a jelszót
```

Ez a fájl git-ignorált: soha nem kerül fel a repóba. Ne küldd el senkinek, ne commitold.

---

## 4. A játékszabályok – hogy párhuzamosan tudjunk dolgozni

**Gábor Windows-kiadása a kiindulási alap.** Ebből következik néhány egyszerű szabály:

1. **A verziószámot sosem te állítod.** A `claude_usage/__init__.py`-ban lévő szám Gáboré. A
   `release.sh` csak olyan verziót enged kiadni, ami Windowsra már kint van (ha Gábor kifejezetten
   kéri, hogy előbb te adj ki: `./macos/release.sh --force`).
2. **Csak a szerver `macos/` mappájába töltesz fel.** A Windows-os `manifest.json`, `versions.json`
   és a letöltőoldal Gáboré – a fiókod nem is éri el őket. A két kiadás külön manifestet használ,
   így sosem írjuk felül egymást.
3. **Az újdonságok szövege közös:** a `release/notes/<verzió>.json` fájlt Gábor írja, a macOS-kiadás
   ugyanazt használja.
4. **A `main` ágra nem te tolsz.** Ha javítanál valamit (jellemzően macOS-specifikus hibát):

   ```bash
   git checkout -b macos/rovid-leiras
   # ... javítás, próba: ./macos/build.sh ...
   git commit -am "macOS: mit javítottam és miért"
   ```

   aztán vagy **Pull Requestet** nyitsz a GitHubon, vagy elküldöd Gábornak a javítást fájlként:

   ```bash
   git format-patch main --stdout > macos-javitas.patch
   ```

   Gábor nézi át és olvasztja be, és a következő kiadásában már benne lesz. Így a forrás egy
   helyen marad, és nem ágazik el két irányba.
5. **Közös kódhoz (ami Windowson is fut) csak egyeztetve nyúlj.** A macOS-specifikus részek:
   `macos/` mappa, `claude_usage/macutil.py`, `secretstore_mac.py`, `updater_mac.py`, `i18n_mac.py`.
   Ezek Windowson be sem töltődnek, úgyhogy itt bátran javíthatsz.

---

## 5. Amit a macOS-verzióról tudni érdemes

- **Nincs Apple-aláírás (notarizáció).** Más gépén az első indításnál: jobb gomb → *Megnyitás*. Ha a
  macOS „sérültnek” mondja: `xattr -dr com.apple.quarantine /Applications/ClaudeUsageMonitor.app`.
  Ez benne van a csomag `OLVASS-EL.txt` fájljában is. (Apple Developer ID-val:
  `CODESIGN_IDENTITY="Developer ID Application: Név (TEAMID)" ./macos/build.sh`)
- **Architektúra:** a fordítás annak a Macnek szól, amin készül (`arm64` = Apple Silicon, `x86_64` =
  Intel). Az Inteles csomag fut Apple Siliconon is (Rosetta), fordítva nem – a program ezt tudja, és
  Inteles gépnek nem ajánl fel arm64-es frissítést.
- **A belépési token a Kulcskarikában (Keychain) van**, fájlba sosem kerül. Új fordítás vagy frissítés
  után a macOS egyszer újra megkérdezheti a hozzáférést (az ad-hoc aláírás minden fordításnál más).
- **Önfrissítés csak az Alkalmazások mappából működik.** A Letöltésekből futtatott programot a macOS
  egy véletlen, írásvédett helyről indítja („App Translocation”) – ilyenkor a program a letöltőoldalt
  ajánlja fel.
- **A Dockban nincs ikon** (szándékosan: panel + menüsor-ikon). Kilépés: jobb gomb a panelen → Kilépés.
- **A mentési állapotsor** (OneDrive/Nextcloud/Obsidian lámpák) Gábor Windows-os mentőszkriptjeire
  épül; Macen beállítás nélkül rejtve marad.
- Naplók, ha hibát keresel: `~/Library/Application Support/ClaudeUsageMonitor/`
  (`startup.log`, `api.log`, `update.log`).

---

## 6. Őszintén: mi nincs még kipróbálva

A macOS-es részeket Gábor Windowson, **Mac nélkül** írta meg. Szimulált környezetben tesztelve van
(mappák, automatikus indulás, Kulcskarika-réteg, frissítő logika), de **valódi Macen te futtatod
először.** Ezekre figyelj külön, és ha bármelyik nem jó, küldd a `doctor` jelentést:

- [ ] a panel megjelenik, mindig felül marad, és akkor is látszik, ha másik alkalmazás aktív
- [ ] egérrel áthúzható; jobb gombra menü jön
- [ ] a menüsorban megjelenik az ikon a százalékkal
- [ ] claude.ai-belépés után a token megmarad újraindítás után is (Kulcskarika)
- [ ] „Induljon bejelentkezéskor” → kijelentkezés/bejelentkezés után tényleg elindul
- [ ] értesítések megjelennek
- [ ] önfrissítés: `update.log` végén `staged → helper started → folder swapped → done`
- [ ] Retina kijelzőn éles a rajz, a betűk a rendszer betűtípusával jelennek meg

Az önfrissítést nyilvános verzió elhasználása nélkül is ki tudod próbálni – kérdezd Gábort a
`--manifest-url` kapcsolóról.
