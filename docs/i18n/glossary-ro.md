# Glosar ro – Claude Usage Monitor

Română, registru de software de consum (nivel Microsoft/Apple/Google România). O singură traducere fixă pentru
fiecare termen; modulul `claude_usage/langs/ro.py` urmează această listă.

## Ortografie

- **ș, ț, Ș, Ț numai cu virgulă dedesubt** (U+0219, U+021B, U+0218, U+021A). Niciodată ş/ţ cu sedilă –
  verificatorul le respinge.
- Ortografia DOOM în vigoare: **â** în interiorul cuvântului, **î** la început/sfârșit; „sunt”, nu „sînt”.
- Împrumuturi fără cratimă când terminația se citește românește: widgetul, tokenurile, linkuri, backupuri,
  leduri. Cu cratimă când nu se citește românește: mouse-ul, site-ul.
- Ghilimele românești „…” (U+201E / U+201D).
- Numerale: „24 de ore” (de la 20 în sus cu „de”), „7 zile”, „10–15 minute”. În textele cu un număr variabil
  (`{}`) folosim structura „etichetă: {}” („Fișiere: {}”, „ZIP noi/actualizate: {}”), ca să evităm „1 fișiere”
  și lipsa lui „de” la 20+.

## Ton și formă de adresare

- **Adresare: „tu”** – imperativ la persoana a II-a singular („Verifică”, „Lipește”, „Conectează-te din nou”,
  „Dă clic pe o stea”), posesive „tău / ta / tale”. Așa scriu Google, Apple, Meta, Revolut, eMAG și majoritatea
  aplicațiilor de consum în română. Windows folosește „dumneavoastră” sau formulări impersonale, dar tonul acestei
  aplicații este scurt, prietenos și personal (autorul îi scrie direct utilizatorului: „Spune-mi”, „îți răspund”),
  iar textele ar suna rigid la plural de politețe. **Niciodată „dumneavoastră” și niciun amestec.**
- Butoane la imperativ (stil Google/Apple): „Trimite”, „Anulează”, „Închide”, „Instalează acum”, „Răsfoiește…”.
  Elementele de meniu sunt substantive acolo unde e natural („Setări…”, „Deconectare”, „Istoric și statistici…”),
  iar acțiunile la imperativ („Afișează panoul”, „Blochează poziția”).
- Stări în curs cu reflexiv impersonal: „Se verifică…”, „Se trimite…”, „Se descarcă…”, „Se caută actualizări…”.
- Fraze scurte, fără calcuri: nu „a fost găsit cu succes”, nu „vă rugăm”, nu „te rog” inutil.
- Notificări: genul etichetei (`{}`) nu e cunoscut, deci folosim forme fără acord („{}: s-a utilizat {}%.”,
  „{}: s-a resetat — …”).
- Etichetele panoului în MAJUSCULE **cu diacritice** (SESIUNE DE 5 ORE, LIMITĂ SĂPTĂMÂNALĂ, SĂPT.).
- Unități de timp, consecvent: **s / min / h / z** („2h 30min”, „3 min”, „1 z”, „{}z {}h”); „min” și nu „m”
  (simbolul SI; „m” e metrul). Procent lipit de număr în valori („{}%”), cu spațiu în textul de ajutor („70 %”,
  ca în engleză).
- Nume proprii neschimbate: Claude, Claude Desktop, Claude Code, claude.ai, Anthropic, Fable, Opus, Sonnet,
  Haiku, PRO/MAX/TEAM/ENTERPRISE, OneDrive, Nextcloud, Obsidian, Cowork, rclone, PowerShell, HTTP(S), JSON,
  OAuth, SHA-256, DPAPI, NAIH, GitHub, claudeusagemonitor.com, Vidovics Gábor, Claude Backup Kit.

## Numele documentului de confidențialitate

**„Politica de confidențialitate”** (`fb.privacy_title`, `help.privacy`). Este denumirea folosită în România de
Google, Apple, Microsoft, Meta, eMAG și de bănci pentru informarea RGPD a unui serviciu; utilizatorul o
recunoaște imediat. „Notă de informare privind prelucrarea datelor” este formularea juridică din art. 13 RGPD,
dar în software de consum sună administrativ. Cu „P” mare doar la primul cuvânt, ca titlu de document, astfel
încât `fb.consent` să sune natural: „Am citit și accept Politica de confidențialitate.” Când textul se referă la
fragmentul afișat în fereastră („Ascunde nota”, „Versiunea acestei note”), folosim „nota”.

În `fb.privacy_text` regulamentul se numește **RGPD**, cu citare românească: „art. 6 alin. (1) lit. f) RGPD”.
Vocabular RGPD oficial: operator, persoană împuternicită de operator, interes legitim, consimțământ, autoritate de
supraveghere, acces, rectificare, ștergere, restricționarea prelucrării, opoziție, creare de profiluri, decizii
automatizate. NAIH rămâne; ANSPDCP (dataprotection.ro) este adăugată ca exemplu românesc, iar „autoritatea din
țara ta” se păstrează.

## Termeni ficși (60)

| Engleză | Română | Observație |
|---|---|---|
| 5-hour session | sesiune de 5 ore | panou: SESIUNE DE 5 ORE; scurt: 5H |
| weekly limit | limită săptămânală | panou: LIMITĂ SĂPTĂMÂNALĂ; scurt: SĂPT. |
| per-model weekly limit | limită săptămânală per model | panou: „{} SĂPTĂMÂNAL” |
| gauge | indicator | „Indicator Opus”, „ordinea indicatoarelor” |
| reset (noun) | resetare | „numărătoare inversă până la resetare”; panou: „resetare {}” |
| reset (verb) | a se reseta | „când o limită se resetează” |
| pace | ritm | panou: „{} vs ritm” |
| burn rate | rată de consum | „%/oră, %/zi” |
| usage | utilizare | „date de utilizare”, „fișier de utilizare” |
| usage credits | credite de utilizare | |
| pay-as-you-go | plată după consum | |
| plan / plan badge | plan / insigna planului | |
| rate-limit tier | nivel de limitare | |
| panel / floating panel | panou / panou flotant | |
| widget | widget | „widgetul” |
| tray, tray icon | zona de notificare, pictograma din zona de notificare | termen Microsoft |
| menu bar (macOS) | bara de meniu | numai în STRINGS_MAC |
| start at login (macOS) | Deschide la autentificare | termenul Apple pentru „Open at Login” |
| taskbar | bara de activități | |
| Start menu | meniul Start | |
| Settings | Setări | |
| sign in / sign out | Conectare / Deconectare | verb: „conectează-te”; „Conectare la claude.ai…” |
| sign-in (noun) | conectare | „conectarea a expirat” |
| passkeys | chei de acces | termenul Google/Apple/Microsoft |
| notification | notificare | |
| alert | alertă | fila „Alerte” |
| threshold | prag | „la depășirea unui prag” |
| warning / critical | Avertizare / Critic | pragurile galben / roșu |
| backup (noun) | backup, pl. backupuri | „Backupuri…”, „folder de backup” |
| backup status bar | bară de stare backup | |
| lamp | led, pl. leduri | luminile colorate de stare |
| snapshot | instantaneu, pl. instantanee | termen Microsoft |
| vault (Obsidian) | seif | |
| note (Obsidian) | notiță; în liste numărate „note” | |
| log / log file | jurnal / fișier jurnal | termen Microsoft |
| run (of a script) | rulare | „Ultima rulare” |
| scheduled tasks | activități planificate | Planificator activități (Windows) |
| data source | sursă de date | |
| data file | fișier de date | |
| profile / account | profil / cont | |
| theme | temă | |
| layout | dispunere | ca să nu se confunde cu „Aspect” |
| appearance (tab) | Aspect | |
| update (program) | actualizare | „Actualizare program” |
| download | descărcare | |
| refresh | reîmprospătare | „Reîmprospătează acum…” |
| history | istoric | „Istoric și statistici…” |
| projection / forecast | estimare | |
| peak | vârf | |
| stale | învechit | „Date învechite” |
| data freshness | vechimea datelor | |
| message to the developer | mesaj către dezvoltator | |
| rating | evaluare | „evaluare cu stele” |
| privacy notice | Politica de confidențialitate | vezi mai sus |
| consent | consimțământ | |
| controller / processor | operator / persoană împuternicită de operator | RGPD |
| terms of use / disclaimer | condiții de utilizare / declinarea răspunderii | |
| click-through | transparent la clic | |
| right-click / double-click | clic dreapta / dublu clic | „Dă clic” |
| endpoint | punct final | termen Microsoft |
