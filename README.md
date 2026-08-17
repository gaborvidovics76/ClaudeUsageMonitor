# Claude Usage Monitor

Mindig felül lévő, designos használatfigyelő panel Windows 11-re. A Claude előfizetésed
**5 órás ablakának** és **heti keretének** kihasználtságát mutatja, folyamatosan frissítve.

## Honnan jönnek az adatok? – két forrás

A programnak két mérési forrása van, a menüben és a Beállítások → Adatforrás lapon
váltható:

### 1. Helyi napló (alapértelmezett, nem kell bejelentkezés)

A **Claude Desktop** saját használati naplójából olvas:

```
%APPDATA%\Claude\plan-usage-history.json
```

- Nem kell bejelentkezni, jelszó vagy kulcs; semmit nem küld sehova.
- **Csak ezt a gépet méri**, és csak amíg fut rajta a Claude Desktop.
- Kb. 5 percenként frissül (ennyente ír a Desktop); a becsült reset-idők közelítők.

### 2. claude.ai (OAuth bejelentkezés, minden eszköz)

Ugyanaz a folyamat, amit a **Claude Code** használ – a **rendszerböngésződben** lépsz be
(ahol a jelszavaid és passkey-d már működnek), nincs beágyazott böngésző:

1. A program megnyitja a bejelentkezést a böngésződben.
2. Belépsz és engedélyezed a hozzáférést; a végén kapsz egy kódot.
3. A kódot bemásolod a programba – kész.

- **Minden eszközöd** használatát mutatja (böngésző, másik gép, telefon).
- **Pontos reset-időbélyegek** a szerverről, nem becslés.
- Gyakrabban frissül.
- **Nincs szükség fejlesztői vagy rendszergazdai tudásra**, és nincs beágyazott böngésző
  (ezért a csomag ~90 MB, nem több száz).
- A kapott token (access + refresh) a Windows-fiókodhoz kötve, **DPAPI-val titkosítva**
  tárolódik; lejáratkor magától frissül. Kijelentkezni a menüből lehet.
- A lekérdezés a `https://api.anthropic.com/api/oauth/usage` végpont felé megy, csak a
  saját fiókod adataiért.

## Telepítés / indítás

Kész program (nem kell hozzá Python):

```
dist\ClaudeUsageMonitor\ClaudeUsageMonitor.exe
```

Az egész `dist\ClaudeUsageMonitor` mappát másold együtt (~90 MB). Szándékosan *nem*
egyfájlos (onefile) a csomag: az minden indításkor kicsomagolna a TEMP-be, ami
bejelentkezéskori kimaradásokat okozott. Így az indulás azonnali.

**Indulás a Windowsszal**: a jobb gombos menüben vagy a **Beállítások → Rendszer** lapon
kapcsolható. **Ütemezett feladatot** hoz létre `ClaudeUsageMonitor` néven (Feladatütemező),
bejelentkezési eseményre, 20 másodperc késleltetéssel, hibánál 3 újrapróbálkozással.
Ez megbízhatóbb, mint a `Run` registry kulcs (az utóbbi tartalékként marad, ha a feladat
létrehozása nem sikerül). Ha áthelyezed a mappát, a program a következő indításkor
magától frissíti a bejegyzést.

Parancssorból is állítható:

```
ClaudeUsageMonitor.exe --enable-autostart
ClaudeUsageMonitor.exe --disable-autostart
```

**Indítási napló** (ha valaha nem indulna): `%APPDATA%\ClaudeUsageMonitor\startup.log`

> A Windows 11 az új tálcaikonokat először a rejtett túlcsordulás-területre teszi
> (a `^` nyíl mögé). Ha állandóan látni akarod, húzd ki onnan a tálcára, vagy:
> Beállítások → Személyre szabás → Tálca → Egyéb tálcaikonok.

Forrásból:

```bash
pip install PySide6-Essentials PySide6-Addons
python main.py
```

(A `PySide6-Addons` a beépített claude.ai bejelentkezéshez kell – ez tartalmazza a
QtWebEngine böngészőt.)

Újrafordítás:

```bash
powershell -ExecutionPolicy Bypass -File build.ps1
```

## Kezelés

| Művelet | Hatás |
|---|---|
| Bal gomb + húzás | panel mozgatása (a képernyő széléhez tapad) |
| Jobb gomb | menü (elrendezés, téma, méret, beállítások, kilépés) |
| Dupla kattintás | előzmények és statisztika ablak |
| Ctrl + görgő | méretezés |
| Tálcaikon: 1 kattintás | panel elrejtése / megjelenítése |
| Tálcaikon: dupla kattintás | előzmények |
| Tálcaikon: jobb gomb | ugyanaz a menü (itt is kapcsolható az indulás a Windowsszal) |

## Áttérés a claude.ai (minden eszköz) mérésre

1. Jobb gomb a panelen → **Adatforrás → claude.ai (minden eszköz)**, vagy
   **Bejelentkezés a claude.ai-ra…**
2. A megnyíló ablakban lépj be a szokásos módon (e-mail vagy Google).
3. A program automatikusan átvált, és onnantól a szerverről kérdez le. A bejelentkezés
   megmarad újraindítás után is; kijelentkezni a menüből lehet.

## Mit mutat?

**Panel**

- **5 órás ablak**: aktuális %, visszaszámlálás a resetig, fogyási ütem (%/óra) és
  becslés, mikor telne be az adott tempóval.
- **Heti keret**: aktuális %, hátralévő idő a heti resetig, napi ütem, és a **tempó**:
  mennyivel vagy előrébb/hátrébb az egyenletes heti fogyasztáshoz képest
  (`+12% a tempóhoz` = túl gyorsan égeted a keretet).
- Trendgörbe az utóbbi időszakról.
- A színek a küszöbök szerint váltanak: zöld → sárga → piros.

**Előzmények ablak** (dupla kattintás)

- 6 óra / 24 óra / 7 nap / teljes idővonal mindkét kerettel, küszöbvonalakkal.
  A mérési szünetek (amikor a Claude Desktop nem futott) megszakadt vonalként látszanak.
- Statisztikák: jelenlegi heti, heti csúcs, napi átlagfogyás, 5 órás ablakok száma,
  és a **hét végére vetített előrejelzés** – ha ez 100% fölé menne, pirosan világít.

**Tálcaikon**: a választott mutató %-a körgyűrűvel, az egérrel fölé állva minden részlet.

## Beállítások

- **Megjelenés**: 6 téma (Éjkék üveg, Claude meleg sötét, Grafit, Neon, Világos papír,
  Post-it sárga), egyedi kiemelőszín, 3 elrendezés (Post-it kártya / Vékony sáv /
  Körgyűrűk), méret, átlátszatlanság, mindig felül, pozíció rögzítése, széphez tapadás,
  tálcán ablakként, kattintás-átengedés (csak dísz üzemmód).
- **Tartalom**: melyik keret, trendgörbe, ütem, visszaszámlálás, frissesség; a tálcaikon
  melyik értéket mutassa.
- **Riasztások**: figyelmeztető és vészküszöb (alap 70% / 90%), értesítés küszöbátlépéskor,
  keret-resetkor és elavult adat esetén.
- **Adatforrás**: profil (ha több fiókod van), frissítési gyakoriság, egyedi adatfájl.
- **Rendszer**: automatikus indítás, beállítások mappa, alapértelmezések visszaállítása.

A beállítások helye: `%APPDATA%\ClaudeUsageMonitor\settings.json` (kézzel is szerkeszthető).

## Ha nem jelenik meg adat

1. Fut a Claude Desktop? Indítsd el, és várj egy mérési ciklust (max. 5 perc).
2. Létezik a `%APPDATA%\Claude\plan-usage-history.json`? Ha máshol van, add meg a
   Beállítások → Adatforrás lapon.
3. Több fiókod van? Válaszd ki a megfelelő profilt ugyanott.

## Nyelvek

A felület **12 nyelven** elérhető (a panel, a menü, a tálca és az értesítések):
angol, magyar, német, francia, spanyol, olasz, portugál, lengyel, holland, orosz,
cseh, török. Induláskor a **rendszer nyelvét** veszi fel (ha támogatott), különben
angol. Kézzel a **jobb gomb → Nyelv** menüből váltható; a választás megmarad.

Új nyelv hozzáadása egyszerű: a [claude_usage/i18n.py](claude_usage/i18n.py) `LANG_NAMES`
listájához vedd fel a kódot, és tölts a `STRINGS` kulcsaihoz egy fordítást. Ami hiányzik,
angolul jelenik meg.

## Fejlesztés / forrás

```bash
pip install -r requirements.txt
python main.py
```

Exe készítése (a `dist\ClaudeUsageMonitor` mappa lesz a kimenet):

```bash
powershell -ExecutionPolicy Bypass -File build.ps1
```

A build leállítja a futó példányokat, kizárja a felesleges Qt-modulokat, és a végén
ellenőrzi a csomag épségét. A `dist/` és `build/` a `.gitignore`-ban van — a repo csak
a forrást tartalmazza.
