# Ordliste – Dansk (da), Claude Usage Monitor

Grundlag for `claude_usage/langs/da.py`. Én fast oversættelse pr. begreb; modulet følger listen.

## Tone og tiltaleform

- **Du-form** overalt („Log på igen", „Tjek din forbindelse"). Det er standarden i dansk
  forbrugersoftware (Microsoft, Apple, Google, MobilePay) – „De" findes ikke i moderne dansk UI.
- Kort, venligt, sikkert – som den engelske kilde. Ingen anglicismer, hvor der findes et dansk ord,
  der bruges i Windows/macOS.
- **Dansk sammenskrivning**: sammensatte ord i ét ord (ugegrænse, sikkerhedskopi, datakilde,
  forbrugsdata, logfil, proceslinjen). Bindestreg kun ved produktnavne og forkortelser
  (Post-it-kort, Claude Code-logmappe, e-mailadresse, IP-adresse).
- **Microsoft-terminologi** for Windows-begreber (Log på / Log af, Indstillinger, Meddelelser,
  proceslinjen, meddelelsesområdet, mappe, opdatering, server, download, menuen Start).
  **Apple-terminologi** for de fire macOS-tekster (menulinjen, „Åbn ved login").
- **Store bogstaver** på panelets etiketter som i den engelske kilde (5-TIMERS SESSION, UGEGRÆNSE).
- Tidsenheder: s / min / t / d. „pc" skrives med småt (denne pc).
- Ellipsen „…" beholdes som ét tegn. Tankestreg „–" som i kilden.

## Navnet på privatlivsdokumentet

`fb.privacy_title` = **Privatlivspolitik**. Det er det ord, de store platforme (Google, Microsoft,
Apple, Facebook, DR, TV 2, MobilePay) og danske webshops bruger om netop denne tekst, og det ord
brugeren kender fra samtykke-afkrydsningsfelter („Jeg har læst og accepterer privatlivspolitikken").
Datatilsynet skriver „oplysningspligt"/„privatlivspolitik" om samme dokument. „Persondatapolitik"
er også udbredt, men mere formelt; „fortrolighedserklæring" (ældre Microsoft-term) bruges stort
set ikke længere. `fb.consent` = „Jeg har læst og accepterer udviklerens {}." – pladsholderen
får dokumentets titel (linket) i ubestemt form; genitiven „udviklerens" gør sætningen grammatisk
korrekt uden bestemt form (koden kan ikke indsætte „privatlivspolitikken").

GDPR hedder på dansk **databeskyttelsesforordningen**; forkortelsen **GDPR** er almindelig og
forstås af alle, så første gang skrives „databeskyttelsesforordningen (GDPR)", derefter artikel-
henvisningerne i dansk juridisk form: **artikel 6, stk. 1, litra f**. Tilsynsmyndigheden i Danmark
hedder **Datatilsynet** – nævnes som eksempel ved siden af NAIH, og „tilsynsmyndigheden i dit eget
land" beholdes.

## Faste begreber

| Engelsk | Dansk | Bemærkning |
|---|---|---|
| 5-hour session | 5-timers session | panel: 5-TIMERS SESSION, kort: 5T |
| weekly limit | ugegrænse | panel: UGEGRÆNSE, kort: UGE |
| per-model weekly limit | ugegrænse pr. model | |
| limit | grænse | „limit" bruges ikke |
| reset (noun / verb) | nulstilling / nulstilles | panel: „nulst. om {}" (ikke bydeform) |
| countdown to reset | nedtælling til nulstilling | |
| pace | tempo | „{} vs tempo" |
| burn rate | forbrugshastighed | |
| usage | forbrug | forbrugsdata, forbrugsfil, forbrugslog |
| usage credits | forbrugskreditter | |
| plan | abonnement | „Abonnement: {}" |
| plan badge | abonnementsbadge | „badge" er gængs dansk |
| gauge | måler | „{} måler" |
| panel / widget | panel / widget | begge beholdes |
| floating panel | svævende panel | |
| tray / tray icon (Windows) | meddelelsesområdet / ikonet i meddelelsesområdet | Microsoft |
| menu bar icon (macOS) | ikonet i menulinjen | Apple |
| taskbar | proceslinjen | Microsoft |
| Start menu | menuen Start | Microsoft |
| sign in / sign out | Log på / Log af | Microsoft; „login" som navneord |
| sign-in (noun) | login | „Login til claude.ai er udløbet" |
| session (OAuth) | session | |
| notification | meddelelse | Microsoft; „Giv besked, når …" i afkrydsningsfelter |
| alert (tab) | advarsler | |
| warning / critical (levels) | advarsel / kritisk | |
| threshold | tærskel | |
| stale data | forældede data | |
| data freshness | dataalder | |
| backup | sikkerhedskopi | flertal: sikkerhedskopier |
| backup folder | sikkerhedskopimappe | |
| backup script | sikkerhedskopiscript | |
| backup run (process) | sikkerhedskopiering | „sikkerhedskopieringens logs" |
| surface (Claude Code, apps) | platform | „Grænser pr. platform"; ikke „flade" |
| refresh (interval, seconds) | opdateringsinterval | |
| backup status bar | statuslinje for sikkerhedskopier | |
| snapshot | øjebliksbillede | |
| vault (Obsidian) | vault | Obsidian-term, oversættes ikke |
| lamp | lampe | |
| scheduled task | planlagt opgave | Microsoft (Opgavestyring) |
| log / log file / local log | log / logfil / lokal log | |
| data source | datakilde | |
| data file | datafil | |
| profile / account | profil / konto | |
| theme | tema | |
| layout | layout | gængs dansk |
| settings | indstillinger | Microsoft |
| update / program update | opdatering / programopdatering | |
| check for updates | søg efter opdateringer | Microsoft |
| download (verb/noun) | download / downloade | Microsoft; „hent" bruges ikke |
| install | installer | |
| history | historik | |
| projection / forecast | prognose | |
| peak | top | „Ugetop" |
| avg daily burn | gns. dagligt forbrug | |
| message to the developer | besked til udvikleren | |
| author | udvikler | fane: „Udvikler", „Lavet af" |
| rating / overall rating | bedømmelse / samlet bedømmelse | |
| star rating | stjernebedømmelse | |
| privacy notice (title) | Privatlivspolitik | se ovenfor |
| the notice (hide link) | teksten | „Skjul teksten" – „meddelelse" er reserveret til notification |
| consent | samtykke | GDPR-term |
| controller / processor | dataansvarlig / databehandler | GDPR-termer |
| legitimate interest | legitim interesse | artikel 6, stk. 1, litra f |
| supervisory authority | tilsynsmyndighed | Datatilsynet |
| rights | indsigt, berigtigelse, sletning, begrænsning, indsigelse | artikel 15–21 |
| profiling / automated decision-making | profilering / automatiske afgørelser | |
| hosting provider | hostingudbyder | |
| encrypted | krypteret | |
| server | server | „serveren" |
| endpoint | slutpunkt | Microsoft |
| rate limited (429) | serveren begrænser forespørgslerne | |
| click-through | klik igennem | |
| lock position | lås placering | |
| always on top | altid øverst | |
| snap to screen edge | fastgør til skærmkanten | |
| accent color | accentfarve | Windows 11 |
| opacity | opacitet | |
| slim bar / post-it card / rings | smal bjælke / Post-it-kort / ringe | |
| this PC | denne pc | |
| all devices | alle enheder | |
| connected apps | tilsluttede apps | |
| terms of use | vilkår for brug | |
| disclaimer | ansvarsfraskrivelse | |
| what's new | nyheder | |
| quit / close / cancel | Afslut / Luk / Annuller | Microsoft |
| browse… | Gennemse… | Microsoft |
| default / restore defaults | standard / Gendan standardindstillinger | Microsoft |
| time units | s / min / t / d | „{}t {}m" på panelet |
