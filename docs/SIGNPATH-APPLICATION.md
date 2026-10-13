# SignPath Foundation – kérelem (ingyenes kódaláírás nyílt forráskódú projektnek)

Ezt a kérelmet csak a projekt tulajdonosa adhatja be, a saját fiókjával: <https://signpath.org/apply>
(a SignPath oldalán „Apply”). Az űrlap angol; alább a kész szövegek, csak be kell másolni.

## Előfeltételek – mind kész (2026-10-13)

| Feltétel | Hol |
|---|---|
| OSI-licenc, kereskedelmi kettős licenc nélkül | MIT – `LICENSE` a repó gyökerében |
| Nyilvános, aktívan karbantartott, már kiadott projekt | <https://github.com/gaborvidovics76/ClaudeUsageMonitor>, 2.9.0 (2026-10-13) |
| Dokumentált működés a letöltő oldalon | <https://claudeusagemonitor.com/> (34 nyelv), `README.md` |
| Nyilvános CI-build a forrásból | `.github/workflows/windows-build.yml` (GitHub Actions, windows-latest, build.ps1) |
| „Code signing policy” a honlapon ÉS a letöltő oldalon, ezzel a kifejezéssel | <https://claudeusagemonitor.com/#code-signing-policy> (a letöltés szekcióban és a láblécben), `CODE_SIGNING_POLICY.md` |
| Csapatszerepek és adatvédelmi nyilatkozat a policy-ben | ugyanott (Author / Reviewer / Approver: Vidovics Gábor) |
| Magatartási kódex | `CODE_OF_CONDUCT.md` |
| Kétlépcsős belépés (MFA) a GitHub-fiókon | **neked kell bekapcsolnod**: GitHub › Settings › Password and authentication |

## Az űrlap mezői – kész szövegek

**Project / repository URL**
```
https://github.com/gaborvidovics76/ClaudeUsageMonitor
```

**License**
```
MIT (LICENSE file in the repository root; no dual licensing, no proprietary components)
```

**Download / release URL**
```
https://claudeusagemonitor.com/  (free download; versions/ClaudeUsageMonitor-Setup-<version>.zip, SHA-256 in manifest.json)
```

**Project description**
```
Claude Usage Monitor is a free, open-source (MIT) always-on-top desktop panel for Windows and macOS that shows
how much of the user's own Claude subscription (Anthropic) is used: the 5-hour and weekly limits, per-model
limits, reset times, pace and burn rate, with notifications. Python 3 + PySide6, packaged with PyInstaller
(onedir). It talks only to Anthropic's own API with the user's own sign-in and to our website for update checks;
no telemetry. First released 2026-08, now at version 2.9.0, 34 UI languages, ~160 downloads from the website
plus the Mac App Store version in preparation.

Artifacts to sign: the Windows program ClaudeUsageMonitor.exe (PyInstaller bootloader) and the installer
scripts Install.ps1 / Uninstall.ps1 inside the release zip. They are built by the public GitHub Actions workflow
.github/workflows/windows-build.yml on windows-latest from the repository source (build.ps1), uploaded as a
workflow artifact; the release zip on the website is the same package.

Code signing policy: https://claudeusagemonitor.com/#code-signing-policy and CODE_SIGNING_POLICY.md.
Team: Vidovics Gábor (author, reviewer, approver); every signing request is approved manually.
```

**Contact e-mail** – egy cím, amit rendszeresen nézel (ide jön a válasz és a beállítási útmutató).

## Beadás után

1. A SignPath e-mailben kérdezhet vissza; a válaszokat is angolul.
2. Elfogadáskor kapsz egy SignPath-szervezetet, projekt-slugot és aláírási házirendet. Ezeket a workflow `sign`
   jobjába kell írni (`project-slug`, `signing-policy-slug`), a tokent és a szervezet-azonosítót a repó
   Secrets-ébe (`SIGNPATH_API_TOKEN`, `SIGNPATH_ORGANIZATION_ID`), és a `SIGNPATH_ENABLED` repository
   variable-t `true`-ra. Ettől kezdve egy `v2.x.y` tag pusholása elindítja a buildet és az aláírást; minden
   kérést a SignPath felületén kézzel hagysz jóvá.
3. A honlapon a policy „Status” sorát átírjuk véglegesre (a `cs.status` i18n-kulcs).

## Hogyan viszonyul a Certum-kártyához

A kettő megfér egymás mellett: a Certum a saját nevedre szóló aláírás a helyi `release.ps1` folyamatban, a
SignPath a GitHub Actions-ben épült csomagot írja alá a SignPath Foundation nevében. Ha mindkettő megvan,
a honlapra kerülő csomagnál te döntesz, melyiket használod.
