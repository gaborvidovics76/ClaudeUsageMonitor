# Claude Usage Monitor - changelog

<!-- newer-versions-here -->

## [2.6.0] - 2026-09-18

- New: the program now also runs on macOS. Everything system-specific has a macOS counterpart - sign-in token in the Keychain, start at login through a LaunchAgent, settings under ~/Library/Application Support, self-update of the .app bundle - while the Windows version behaves exactly as before.
- The macOS build has its own release manifest, so the Windows and the macOS releases are published independently and never overwrite each other. An Apple Silicon build is never offered to an Intel Mac.
- For developers: macos/build.sh builds the app with one command, macos/release.sh packages, uploads and verifies it, macos/doctor.sh collects diagnostics. The Windows release stays the base: a macOS release is only made for a version that is already out for Windows.
- A stale single-instance lock left behind by a crash no longer blocks the next start on macOS/Linux.

*Magyarul:*

- Új: a program mostantól macOS-en is fut. Minden rendszerfüggő résznek van macOS-es megfelelője - a belépési token a Kulcskarikában, indulás bejelentkezéskor LaunchAgenttel, beállítások a ~/Library/Application Support alatt, az .app csomag önfrissítése -, miközben a Windows-verzió pontosan úgy működik, mint eddig.
- A macOS-kiadásnak saját manifestje van, így a Windows- és a macOS-kiadás egymástól függetlenül jelenik meg, és sosem írják felül egymást. Apple Silicon-os csomagot a program Inteles Macnek nem ajánl fel.
- Fejlesztőknek: a macos/build.sh egy paranccsal lefordítja a programot, a macos/release.sh becsomagolja, feltölti és ellenőrzi, a macos/doctor.sh diagnosztikát gyűjt. A Windows-kiadás marad az alap: macOS-kiadás csak olyan verzióból készülhet, ami Windowsra már megjelent.
- Egy összeomlás után hátramaradt egypéldányos zár többé nem akadályozza a következő indulást macOS-en/Linuxon.


## [2.5.1] - 2026-09-18

- Fixed: an empty server placeholder ("Nimbus Quill", 0%, no reset time) showed up in the small list. Windows the server marks as not active, and code-name windows that are empty and never reset, are no longer shown. If such a window ever starts counting, it appears by itself.

*Magyarul:*

- Javítva: egy üres szerveroldali helyőrző („Nimbus Quill”, 0%, reset-időpont nélkül) megjelent a kis felsorolásban. Azok az ablakok, amelyeket a szerver nem aktívnak jelöl, illetve az üres, soha nem nullázódó kódnevű ablakok mostantól nem látszanak. Ha egy ilyen ablak egyszer számolni kezd, magától megjelenik.


## [2.5.0] - 2026-09-18

- New: usage of the OTHER models. The server keeps a separate counter only for some models (often just one), so for the rest the app now reads Claude Code's own logs on this PC and shows how this week's work is split between the models - e.g. Opus 4.8 49% · 932k output tokens. It sits under the gauges in its own group, clearly labelled, because it is a share of your own usage and not a share of a limit.
- Privacy: only the model name, the token counts and the timestamp are read from the logs - never the conversation. Nothing leaves your PC.
- Built to never get in the way: the log folder is found automatically (or pick it in Settings → Details), reading is incremental and runs in the background with a time and size budget, online-only files are skipped, broken lines and missing folders are ignored quietly. No logs - the group simply stays hidden.
- The small list now also shows server windows the app does not know by name, unless they only repeat a limit that is already on the panel.
- Each line of the split can be unticked one by one; the whole group has its own switch in the menu and in Settings → Details, and it also works with the local data source.

*Magyarul:*

- Új: a TÖBBI modell használata. A szerver csak egyes modellekhez tart külön számlálót (gyakran csak egyhez), ezért a többinél a program mostantól a Claude Code saját naplóit olvassa ezen a gépen, és megmutatja, hogyan oszlik meg az e heti munka a modellek között - pl. Opus 4.8 49% · 932k kimeneti token. A mérők alatt külön, egyértelműen felcímkézett csoportban látszik, mert ez a saját használatod megoszlása, nem egy keret százaléka.
- Adatvédelem: a naplókból csak a modell neve, a tokenszámok és az időbélyeg kerül kiolvasásra - a beszélgetés soha. Semmi nem hagyja el a gépedet.
- Úgy készült, hogy sose akadjon meg miatta semmi: a naplómappát magától megtalálja (vagy megadhatod a Beállítások → Részletek lapon), az olvasás a háttérben, fokozatosan, idő- és méretkorláttal fut, a csak online fájlokat kihagyja, a sérült sorokat és a hiányzó mappát csendben átugorja. Ha nincs napló, a csoport egyszerűen rejtve marad.
- A kis felsorolás mostantól a név szerint nem ismert szerverablakokat is mutatja, kivéve ha csak egy már látható keretet ismételnek.
- A megoszlás sorai egyenként kipipálhatók; az egész csoportnak külön kapcsolója van a menüben és a Beállítások → Részletek lapon, és a helyi adatforrással is működik.


## [2.4.0] - 2026-09-18

- New: plan badge in the header - a little gradient pill with a sparkle: PRO, MAX 5×, MAX 20×, TEAM or ENTERPRISE. Hover it for your plan card (plan, rate-limit tier, extra usage, member since). Your name only appears on the badge if you switch that on.
- New: a small list under the gauges shows every other limit the server reports - the weekly windows of the other models (Opus, Sonnet…), per-surface windows (Claude Code, connected apps…) and limits the app does not know by name yet. Each line has a status dot, a thin bar, the percentage and the time to reset.
- New: extra usage (pay-as-you-go credit) - whether it is on, the monthly limit and what you have spent.
- Everything is selectable: five switches in Settings → Details and in the right-click menu, plus a tick box for every single line the server currently sends for your account.
- The list only takes room when there is something to show; the slim bar layout stays as it is.
- Privacy: the plan is read from Anthropic's profile endpoint with your existing sign-in. Your name and e-mail are never written to any log.

*Magyarul:*

- Új: csomagjelvény a fejlécben - kis színátmenetes, csillogó pirula: PRO, MAX 5×, MAX 20×, TEAM vagy ENTERPRISE. Ha fölé viszed az egeret, megjelenik a csomagkártyád (csomag, korlátozási szint, extra használat, mióta vagy tag). A neved csak akkor kerül a jelvényre, ha külön bekapcsolod.
- Új: a mérők alatt kis felsorolás mutat minden további keretet, amit a szerver küld - a többi modell heti keretét (Opus, Sonnet…), a felületenkénti kereteket (Claude Code, külső alkalmazások…), és azokat is, amelyeket a program név szerint még nem ismer. Minden sorban állapotpötty, vékony sáv, százalék és a resetig hátralévő idő.
- Új: extra használat (túlhasználati keret) - be van-e kapcsolva, mennyi a havi limit és mennyit költöttél el.
- Minden kiválasztható: öt kapcsoló a Beállítások → Részletek lapon és a jobb gombos menüben, plusz külön pipa minden egyes sorhoz, amit a szerver éppen a fiókodhoz küld.
- A lista csak akkor foglal helyet, ha van mit mutatnia; a vékony sáv elrendezés változatlan marad.
- Adatvédelem: a csomagot az Anthropic profil-végpontjáról olvassa ki, a meglévő belépéseddel. A neved és az e-mail-címed soha nem kerül semmilyen naplóba.


## [2.3.3] - 2026-09-18

- Clearer menu: "Refresh usage data now" (fetches your numbers) and "Check for program updates…" (looks for a new version) can no longer be mixed up - the program update now sits in its own section above Quit.
- The header shows "fetching data…" while a request runs, and the update window is titled "Program update".
- The installer also cleans up the leftovers of an interrupted self-update.
- Diagnostics: the log notes once per run which fields the server offers (names only, never values).

*Magyarul:*

- Egyértelmű menü: a „Használati adatok frissítése most” (a számaidat kéri le) és a „Programfrissítés keresése…” (új verziót keres) többé nem keverhető össze - a programfrissítés külön szakaszba került, a Kilépés fölé.
- A fejléc „adatlekérés…” feliratot mutat, amíg a kérés fut, a frissítés ablaka pedig a „Programfrissítés” címet kapta.
- A telepítő a félbemaradt önfrissítés maradványait is eltakarítja.
- Diagnosztika: a napló futásonként egyszer feljegyzi, milyen mezőket kínál a szerver (csak a neveket, értéket soha).


## [2.3.2] - 2026-09-18

- Fixed: the self-update downloaded and verified the new version but never swapped it in (the helper process did not start). Found and fixed by updating a real installation end to end.
- If you have 2.3.0 or 2.3.1: install this version once with INSTALL.bat - from here on updates install themselves.
- The app now confirms that the update helper really started, and reports it if not.
- New: --manifest-url=<https url> for the command-line update switches.

*Magyarul:*

- Javítva: az önfrissítés letöltötte és ellenőrizte az új verziót, de a cserét már nem végezte el (a segédfolyamat nem indult el). Valódi telepítésen, végigvitt frissítéssel találtam meg és javítottam.
- Ha 2.3.0 vagy 2.3.1 van nálad: ezt a verziót még egyszer a TELEPITES.bat fájllal tedd fel - innentől a frissítések maguktól települnek.
- A program mostantól ellenőrzi, hogy a frissítő segédfolyamat tényleg elindult-e, és jelzi, ha nem.
- Új: --manifest-url=<https cím> kapcsoló a parancssori frissítéshez.


## [2.3.1] - 2026-09-18

- New: hover the status text in the panel header to see when the data was last updated and, if a request failed, why - plus the countdown to the automatic retry.
- Improved: updating from the command line (--update-now) now also works while the panel is running.
- First release delivered through the built-in online updater.

*Magyarul:*

- Új: ha a panel fejlécében az állapotszöveg fölé viszed az egeret, látod, mikor frissült utoljára az adat, és ha egy kérés nem sikerült, azt is, hogy miért - az automatikus újrapróbálásig hátralévő idővel együtt.
- Javítva: a parancssori frissítés (--update-now) mostantól akkor is működik, ha a panel közben fut.
- Az első kiadás, amely már a beépített netes frissítőn keresztül érkezik.


## [2.3.0] - 2026-09-18

- New: installer - unzip, double-click INSTALL.bat, done. No admin rights; appears under Installed apps with a proper uninstaller.
- New: online updates - the app checks for a newer version, downloads it, verifies the SHA-256, replaces itself and restarts. Your settings stay.
- Fixed: "Refresh now" sometimes seemed to do nothing. The server rate-limits the usage endpoint (HTTP 429); a manual refresh now retries until it gets an answer.
- Fixed: the data no longer goes stale every other minute - polling adapts to what the server allows and backs off when it pushes back.
- New: visible activity - a spinning ring and "refreshing..." while a request runs, a countdown to the automatic retry, and a warning colour when the last request failed.
- New: size and order of the per-model (Fable) gauge are adjustable; the gauge can be switched off on its own.
- New (optional): backup status bar with traffic-light lamps for OneDrive / Nextcloud / Obsidian backups; click a lamp to see what was backed up. Configured per user, hidden unless set up.
- Privacy: nothing about your machine is built into the program - backup locations come only from your own local profile.

*Magyarul:*

- Új: telepítő - kicsomagolod, duplán kattintasz a TELEPITES.bat fájlra, kész. Rendszergazdai jog nem kell; megjelenik a Telepített alkalmazások között, rendes eltávolítóval.
- Új: netes frissítés - a program figyeli az új verziót, letölti, SHA-256-tal ellenőrzi, lecseréli magát és újraindul. A beállításaid megmaradnak.
- Javítva: a „Frissítés most” néha látszólag nem csinált semmit. A szerver korlátozza a lekérdezést (HTTP 429); a kézi frissítés mostantól addig próbálkozik, amíg választ nem kap.
- Javítva: az adat már nem avul el minden második percben - a lekérdezés üteme ahhoz igazodik, amit a szerver enged, és visszavesz, ha a szerver korlátoz.
- Új: látható működés - forgó gyűrű és „frissítés...” felirat, amíg a kérés fut, visszaszámlálás az automatikus újrapróbálásig, és figyelmeztető szín, ha az utolsó kérés nem sikerült.
- Új: a modellenkénti (Fable) mérő mérete és a mérők sorrendje állítható; a mérő önállóan kikapcsolható.
- Új (opcionális): mentési állapotsor színes lámpákkal a OneDrive / Nextcloud / Obsidian mentésekhez; egy lámpára kattintva látszik, mi lett elmentve. Felhasználónként állítható, beállítás nélkül rejtve marad.
- Adatvédelem: a programba semmi nincs beleégetve a gépedről - a mentések helye kizárólag a saját, helyi profilodból jön.

