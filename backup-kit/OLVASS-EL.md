# Claude mentő kezdőcsomag – ingyenes

Mindaz, amit a Claude-dal felépítettél – a skilljeid, a `CLAUDE.md` szabályaid, a projektmemória, az MCP-beállítások,
az agent-beszélgetések naplói és az Obsidian-jegyzeteid – általában **egyetlen lemezen** él. Egy tönkrement meghajtó,
egy ellopott laptop, egy rossz törlés, és oda az egész. Ez a csomag naponta **két, egymástól független helyre** ment,
a **Claude Usage Monitor pedig a panelen mutatja, hogy frissek-e a mentéseid.**

Ingyenes, nyílt forráskódú (MIT), Windows 10/11-re. Nincs regisztráció, semmilyen adat nem jön hozzánk.

## Mit ment

| | 1. lépés – OneDrive | 2. lépés – második felhő |
|---|---|---|
| Claude Code (`%USERPROFILE%\.claude`): skillek, beállítások, `CLAUDE.md`, projektmemória, pluginok | ✔ | ✔ |
| Claude Desktop (`%APPDATA%\Claude`): beállítások, MCP-szerverek | ✔ | ✔ |
| Agent (Cowork) beszélgetésnaplók – munkamenetenként egy ZIP | ✔ | ✔ |
| Obsidian vault – minden futáskor dátumozott ZIP-pillanatkép (opcionális) | ✔ | ✔ |
| Bármely további mappa, amit a `config.psd1`-ben felsorolsz | ✔ | ✔ |

**Soha nem kerül mentésbe:** a Claude Code bejelentkezési tokenje (`.credentials.json`), a Claude Desktop sütijei,
a gyorsítótárak és a nagy, újraletölthető VM-képek.

A **2. lépés** a teljes mentési mappát Nextcloudra másolja – vagy bármely más felhőbe, amit az rclone ismer
(Google Drive, Dropbox, S3, pCloud, SFTP …). OneDrive + egy második, független szolgáltató: ha az egyik elérhetetlen
vagy kizár, a másik megvan.

## Mit mutat a Claude Usage Monitor

A mentési állapotsor bekapcsolásával a panel alján három lámpa jelenik meg: **OneDrive · Nextcloud · Obsidian**,
mellettük az utolsó *sikeres* mentés kora.

- 🟢 zöld – legfeljebb 24 órás · 🟡 sárga – legfeljebb 48 órás · 🔴 piros – régebbi, vagy nincs mentés (az órák állíthatók)
- piros gyűrű a lámpa körül – a legutóbbi futás hibás volt vagy félbemaradt, akkor is, ha a lámpa még zöld
- lámpára kattintva a részletek: mi van elmentve (forrás, cél, fájlszám, méret), a vault-pillanatkép és a legutóbb
  szerkesztett jegyzetei, mi ment fel, a távoli tárhely, hibák, ütemezett feladatok, napló

Csak az a futás számít sikeresnek, amelynek naplója a szkript saját „… KESZ" sorával zárul – a hibás, félbemaradt
vagy próbafutás nem.

## Telepítés – 10 perc

**Kell hozzá:** Windows 10/11, bejelentkezett OneDrive, telepített [Claude Usage Monitor](https://dinorr.hu/claude-usage-monitor/hu/).
A 2. lépéshez: Nextcloud-fiók (vagy más, rclone által ismert felhő).

1. **Nextcloud alkalmazásjelszó** (csak a 2. lépéshez). Böngészőben: Nextcloud → profilkép → *Személyes beállítások*
   → *Biztonság* → *Eszközök és munkamenetek* → alkalmazás neve: `rclone-backup` → *Új alkalmazásjelszó létrehozása*.
   Másold ki – csak egyszer látod. Ez **nem** a fiókjelszavad, és bármikor visszavonható.
2. **Csomagold ki** a csomagot egy végleges mappába, pl. `C:\Tools\ClaudeBackup`.
3. **Szerkeszd a `config.psd1`-et** Jegyzettömbbel: mit mentsen (`VaultPath` az Obsidianhoz, `ExtraFolders`), a második felhő
   (`NextcloudRemote`, `NextcloudBasePath` – ha a `NextcloudRemote` üres, a 2. lépés kimarad) és az időpont (`DailyTime`).
4. **Futtasd a telepítőt rendszergazdaként.** Win+X → *Terminál (rendszergazda)*:
   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
   cd C:\Tools\ClaudeBackup
   Unblock-File *.ps1
   .\Install-BackupKit.ps1
   ```
   Szükség esetén telepíti az rclone-t, bekéri a Nextcloud címét, a felhasználónevet és az alkalmazásjelszót
   (rejtve gépeled), regisztrálja a két ütemezett feladatot, megírja a monitor profilját, és elvégez egy első futást.
5. **Első éles feltöltés:** `.\Backup-Step2-Cloud.ps1` (a telepítő 2. lépése csak próbafutás volt).
6. **Ellenőrzés:** `.\Test-BackupKit.ps1` – minden sor legyen `[OK]`. A panelen 5 percen belül megjelenik a három lámpa
   (vagy: jobb gomb a panelen → *Mentések…* → *Ellenőrzés most*).

## Beállítások a Claude Usage Monitorban (Beállítások → Mentések)

| Beállítás | Mit csinál |
|---|---|
| Mentési állapotsor a panelen | be- vagy kikapcsolja a három lámpát |
| Lámpák | melyik látszódjon: OneDrive / Nextcloud / Obsidian (nincs Obsidianod? vedd ki a pipát) |
| Felirat a lámpa mellett | név és eltelt idő · csak név · csak lámpák |
| Zöld eddig / Sárga eddig | a korhatárok órában (alap: 24 / 48) |
| Mentési mappa | ahová az 1. lépés ír – üresen a telepítő által írt profilból jön |
| Mentőszkript konfigja | a csomag `config.psd1`-je – innen olvassa a monitor a vault helyét és a felhőcélt |
| Ütemezett feladatok szűrője | pl. `ClaudeBackup*` – mely ütemezett feladatokat mutassa a részletező ablak |
| A részletező ablak mutassa | mi van elmentve · tartalom · hibák és figyelmeztetések · ütemezett feladatok · napló |

A telepítő által írt profil: `%APPDATA%\ClaudeUsageMonitor\backup_profile.json` – csak útvonalak, se jelszó, se token.
A beállítások lapján megadott érték elsőbbséget élvez a profilfájllal szemben (a fájl nem változik).

## Van már saját mentőszkripted?

A monitornak nem ez a csomag kell, hanem a naplók. A szkripted írjon

- futásonként egy naplófájlt a `<mentési mappa>\logs` mappába, `onedrive_ÉÉÉÉ-HH-NN_ÓÓPPMM.log` (1. lépés) és
  `nextcloud_ÉÉÉÉ-HH-NN_ÓÓPPMM.log` (2. lépés) néven,
- minden sort `yyyy-MM-dd HH:mm:ss [SZINT] üzenet` alakban,
- sikeres futásnál egy `KESZ`-t, hibásnál egy `HIBAVAL ZARULT`-at tartalmazó utolsó sort (a többi szót, amit a monitor
  megért, a `Common.ps1` eleje sorolja fel).

Más nevek vagy mappák? Add meg őket a `%APPDATA%\ClaudeUsageMonitor\backup_profile.json` fájlban (minden kulcs elhagyható):

```json
{
  "root": "%OneDrive%\\MyBackup",
  "log_dir": "logs",
  "snapshot_dir": "vault-snapshots",
  "snapshot_glob": "Vault_*.zip",
  "onedrive_log_prefix": "onedrive",
  "nextcloud_log_prefix": "nextcloud",
  "vault": "%USERPROFILE%\\Documents\\Obsidian Vault",
  "remote": "nextcloud:Backups/MyPC",
  "task_filter": "MyBackup*"
}
```

Ebbe a fájlba se jelszó, se token nem való – a monitornak soha nincs rá szüksége.

## Biztonság – hogyan épül fel

- **Sehol nincs jelszó a csomagban.** Az alkalmazásjelszót rejtve gépeled be, és csak az rclone saját konfigjában
  (`%APPDATA%\rclone\rclone.conf`) tárolódik, obfuszkálva. A Nextcloudban bármikor visszavonhatod.
- **A Claude Code bejelentkezési tokenje sosem kerül mentésbe**, ahogy a Claude Desktop sütijei sem.
- **Nincs tükrözés.** Az 1. lépés `robocopy /E /XO`, a 2. `rclone copy` – amit a gépen törölsz, az mindkét mentésben
  megmarad. (A tükrözés hűségesen lemásolná a tévedést is.)
- **A vault dátumozott ZIP-ekbe kerül**, így egy későbbi hibás másolat nem írhat felül egy régebbi állapotot (30 napig őrzi).
- **Figyelem:** a `claude_desktop_config.json` és a `.claude\settings.json` tartalmazhat MCP-szerverek API-kulcsait vagy
  környezeti változókat. Ezek mentésbe kerülnek (a visszaállításhoz kellenek), a saját OneDrive-odba és a saját felhődbe –
  ezeket a fiókokat védd kétlépcsős bejelentkezéssel.
- A két lépés láncban fut: a 2. akkor indul, amikor az 1. befejeződött, sosem közben. Ehhez a telepítő bekapcsolja
  a Windows Feladatütemező előzményeit.

## Visszaállítás

| Mi veszett el | Honnan |
|---|---|
| Egy jegyzet régebbi változata | onedrive.com → jobb klikk a fájlon → *Verzióelőzmények* |
| Egy törölt fájl | onedrive.com → *Lomtár* (30 nap), vagy Nextcloud → *Törölt fájlok* |
| Az egész vault egy adott napról | `ClaudeBackup\vault-snapshots\Vault_ÉÉÉÉ-HH-NN_ÓÓPP.zip` – **üres** mappába bontsd ki, és nyisd meg Obsidianban: *Open folder as vault* |
| Claude Code skillek / beállítások | a `ClaudeBackup\files\claude-code\*` vissza a `%USERPROFILE%\.claude\` mappába, majd jelentkezz be újra a Claude Code-ba |
| Claude Desktop beállítások | zárd be a Claude Desktopot, és másold vissza a `ClaudeBackup\files\claude-desktop\*` tartalmát a `%APPDATA%\Claude\` mappába |

## Fájlok

| Fájl | Szerep |
|---|---|
| `config.psd1` | minden beállítás |
| `Install-BackupKit.ps1` | egyszeri telepítő (rendszergazdaként) |
| `Backup-Step1-OneDrive.ps1` | 1. lépés – naponta futtatja a *ClaudeBackup 1 - OneDrive* feladat |
| `Backup-Step2-Cloud.ps1` | 2. lépés – közvetlenül utána a *ClaudeBackup 2 - Nextcloud* (`-DryRun` = próba) |
| `Set-CloudRemote.ps1` | a Nextcloud-kapcsolat (újra)beállítása |
| `Test-BackupKit.ps1` | állapotellenőrzés |
| `Common.ps1` | közös függvények és a monitor által olvasott naplóformátum – a naplószavakat ne írd át |

Naplók: `<OneDrive>\ClaudeBackup\logs\onedrive_*.log` és `nextcloud_*.log` (90 napig).

Eltávolítás: `Unregister-ScheduledTask 'ClaudeBackup*'`, és töröld ezt a mappát. A mentéseid megmaradnak.

---
Készítette: Vidovics Gábor · a Claude Usage Monitor része · MIT-licenc · jótállás nélkül – ellenőrizd a mentéseidet
(pontosan erre valók a lámpák).
