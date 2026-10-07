# -*- coding: utf-8 -*-
"""Svenska – UI strings of Claude Usage Monitor."""

CODE = "sv"
NAME = "Svenska"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{}d",
    "backup.age_h": "{}h",
    "backup.age_m": "{}min",
    "backup.and_more": "…och {} till",
    "backup.checked_at": "Kontrollerat: {}",
    "backup.checking": "Kontrollerar…",
    "backup.cloud_only": "Ögonblicksbilden är bara tillgänglig online i OneDrive. Innehållet listas inte, så att den inte behöver laddas ned.",
    "backup.comp.cowork": "Cowork-chattloggar (en ZIP-fil per session)",
    "backup.comp.vault": "Ögonblicksbild av Obsidian-valvet (ZIP)",
    "backup.disclaimer_short": "Programmet visar bara det som står i loggarna från säkerhetskopieringen. Vi ansvarar inte för säkerhetskopiorna – det är upp till dig att kontrollera att de är fullständiga och går att återställa.",
    "backup.done": "klar",
    "backup.dry_run": "(testkörning, inget laddades upp)",
    "backup.failed": "MISSLYCKADES",
    "backup.files_size": "{} filer, {}",
    "backup.folders": "Mappar",
    "backup.label_age": "Namn och ålder",
    "backup.label_name": "Bara namn",
    "backup.label_none": "Bara lampor",
    "backup.last_ok": "Senaste lyckade säkerhetskopia: {} (för {} sedan)",
    "backup.last_run": "Senaste körning: {} – {}",
    "backup.legend": "Grön: högst {} h gammal · Gul: upp till {} h · Röd: äldre eller ingen säkerhetskopia",
    "backup.level_green": "Aktuell",
    "backup.level_none": "Ingen säkerhetskopia hittades",
    "backup.level_red": "Inaktuell",
    "backup.level_yellow": "Börjar bli gammal",
    "backup.log_file": "Loggfil",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Mappen för säkerhetskopior hittades inte: {}",
    "backup.none_found": "Inga.",
    "backup.open": "öppna",
    "backup.rc_copied": "nya eller ändrade filer kopierades",
    "backup.rc_failed": "MISSLYCKADES (kod {})",
    "backup.rc_nochange": "aktuellt, inget att kopiera",
    "backup.recent_notes": "Senast redigerade anteckningar i ögonblicksbilden",
    "backup.refresh": "Kontrollera nu",
    "backup.sec_components": "Vad som säkerhetskopieras",
    "backup.sec_contents": "Innehåll",
    "backup.sec_log": "Logg (sista raderna)",
    "backup.sec_problems": "Fel och varningar",
    "backup.sec_tasks": "Schemalagda aktiviteter",
    "backup.skipped": "hoppades över (mappen hittades inte)",
    "backup.snap_kept": "{} ögonblicksbilder sparas, totalt {}",
    "backup.snapshot": "Senaste ögonblicksbild",
    "backup.source": "Källa",
    "backup.state_error": "slutfördes med fel",
    "backup.state_interrupted": "slutfördes inte",
    "backup.state_ok": "slutfördes utan fel",
    "backup.state_running": "körs nu",
    "backup.storage": "Fjärrlagring: {} av {} används, {} ledigt",
    "backup.target": "Mål",
    "backup.task_event": "vid händelse",
    "backup.task_row": "senaste körning {} · resultat {} · nästa {}",
    "backup.tip_click": "Klicka för att visa detaljer",
    "backup.title": "Säkerhetskopior",
    "backup.tray": "Säkerhetskopior: {}",
    "backup.uploaded": "Uppladdat i den här körningen: {} nya, {} ersatta, {} fel",
    "backup.uploaded_files": "Uppladdade filer",
    "backup.uploaded_groups": "Uppladdade filer per mapp",
    "backup.uploaded_no": "Uppladdat till Nextcloud: inte än",
    "backup.uploaded_yes": "Uppladdat till Nextcloud: ja ({})",
    "backup.vault": "Valv",
    "backup.vault_changed": "{} anteckningar har ändrats i valvet sedan den här ögonblicksbilden",
    "backup.zip_new": "{} nya/uppdaterade ZIP-filer",
    "backup.zip_summary": "{} filer ({} anteckningar), {} okomprimerat",

    # --- general ---------------------------------------------------------------------------
    "detail.extra": "Användningskrediter",
    "detail.local_header": "CLAUDE CODE · DEN HÄR DATORN · VECKANS FÖRDELNING",
    "detail.off": "av",
    "detail.on": "på",
    "detail.surface.oauth_apps": "Anslutna appar",
    "detail.unlimited": "ingen gräns",
    "dlg.cancel": "Avbryt",
    "dlg.checking": "Kontrollerar…",
    "dlg.err_badcode": "Koden godkändes inte.\n\n{}\n\nKontrollera att du klistrade in hela koden, eller logga in via webbläsaren igen (du får alltid en ny kod).",
    "dlg.err_ratelimit": "För många inloggningsförsök på kort tid.\n\nServern begränsar dig tillfälligt. Stäng det här fönstret, vänta 10–15 minuter (försök inte under tiden) och starta sedan EN ny inloggning i webbläsaren med en ny kod.",
    "dlg.hint1": "Logga in på sidan som öppnas och godkänn åtkomsten. Till sist får du en kod.",
    "dlg.intro": "Logga in på ditt claude.ai-konto i din egen webbläsare (där fungerar redan dina sparade lösenord och lösennycklar).",
    "dlg.login_title": "logga in",
    "dlg.open_browser": "Öppna inloggningen i webbläsaren",
    "dlg.paste_label": "Klistra in koden som du har fått:",
    "dlg.paste_placeholder": "klistra in koden här",
    "dlg.signin": "Logga in",
    "dlg.step1": "Steg 1",
    "dlg.step2": "Steg 2",
    "dlg.unknown_err": "Okänt fel.",

    # --- error messages --------------------------------------------------------------------
    "err.already_running": "Appen körs redan (titta i meddelandefältet).",
    "err.bad_token_resp": "ogiltigt svar från tokenslutpunkten",
    "err.bad_usage_resp": "ogiltigt svar från användningsslutpunkten",
    "err.connection": "anslutningsfel: {}",
    "err.file_empty": "Användningsfilen är tom.",
    "err.file_not_found": "Användningsfilen hittades inte.\nKörs Claude Desktop?",
    "err.file_unreadable": "Användningsfilen kan inte läsas just nu.",
    "err.loading": "Loggar in / hämtar data…",
    "err.network": "nätverksfel: {}",
    "err.no_code": "Ingen kod har klistrats in.",
    "err.no_data_profile": "Inga data för den här profilen.",
    "err.no_tray": "Meddelandefältet är inte tillgängligt, så ingen ikon visas där.",
    "err.no_usage_data": "Inga användningsdata.",
    "err.not_signed_in": "Inte inloggad.",
    "err.query_http": "Fel vid hämtning (HTTP {}).",
    "err.rate_limited": "Servern begränsar antalet förfrågningar (429) – försöker igen automatiskt.",
    "err.session_expired": "Sessionen har gått ut. Logga in igen.",
    "err.session_expired_nl": "Sessionen har gått ut.\nLogga in igen.",
    "err.signin_needed": "Inloggningen på claude.ai har gått ut.\nLogga in igen: högerklicka → Logga in på claude.ai",
    "err.unexpected": "Oväntat fel: {}",

    # --- 'Message to the developer' window -------------------------------------------------
    "fb.cancel": "Avbryt",
    "fb.close": "Stäng",
    "fb.consent": "Jag har läst och godkänner: {}.",
    "fb.email": "E-postadress",
    "fb.email_hint": "bara om du vill ha svar",
    "fb.err_consent": "Godkänn integritetspolicyn för att kunna skicka.",
    "fb.err_email": "E-postadressen ser inte riktigt rätt ut.",
    "fb.err_empty": "Skriv ett meddelande eller välj ett betyg först.",
    "fb.err_links": "För många länkar i meddelandet.",
    "fb.err_network": "Det gick inte att nå claudeusagemonitor.com. Kontrollera anslutningen och försök igen.",
    "fb.err_rate": "För många meddelanden på kort tid – försök igen senare.",
    "fb.err_server": "Servern kunde inte ta emot meddelandet just nu. Försök igen senare.",
    "fb.intro": "Har du en idé, har du hittat en bugg eller gillar du bara programmet? Berätta! Jag, Vidovics Gábor, som har utvecklat det, läser varje meddelande.",
    "fb.message": "Meddelande",
    "fb.message_ph": "Vad fungerar, vad fungerar inte, vad saknas?",
    "fb.meta": "Skickas med meddelandet: programversion {0}, operativsystem ({1}), gränssnittsspråk ({2}).",
    "fb.name": "Namn",
    "fb.optional": "(valfritt)",
    "fb.privacy_hide": "Dölj policyn",
    "fb.privacy_text": (
        "Personuppgiftsansvarig: Vidovics Gábor, privatperson (Ungern), utvecklare av Claude Usage Monitor. "
        "Den fullständiga integritetspolicyn finns på webbplatsen: https://claudeusagemonitor.com/#privacy\n\n"
        "Vad som skickas: det du skriver här – namn (valfritt), e-postadress (valfritt), meddelande, stjärnbetyg – "
        "och, för att jag ska förstå sammanhanget: programversionen, operativsystemets namn och version, "
        "gränssnittsspråket och tidpunkten då meddelandet skickades. Servern sparar ingen IP-adress; för att "
        "förhindra missbruk använder den bara ett hashvärde som byts ut varje dag och som inte kan räknas om "
        "till en adress.\n\n"
        "Varför: för att läsa och besvara ditt meddelande och för att förbättra programmet (berättigat intresse, "
        "artikel 6.1 f i dataskyddsförordningen (GDPR); själva svaret skickas på din begäran). Ditt betyg och ditt "
        "namn visas på webbplatsen bara om du kryssar i den separata rutan för det (samtycke, artikel 6.1 a), "
        "och först efter att utvecklaren har granskat dem; du kan när som helst återkalla samtycket.\n\n"
        "Hur länge: meddelanden i högst 2 år; ett publicerat betyg tills du återkallar ditt samtycke. Om "
        "utvecklaren har aktiverat vidarebefordran via e-post hamnar också en kopia i utvecklarens inkorg.\n\n"
        "Vem som ser uppgifterna: bara den personuppgiftsansvarige och – som personuppgiftsbiträde – "
        "webbhotellet (servern finns inom EU, i Tyskland). Ingenting säljs eller lämnas vidare; ingen profilering "
        "och inget automatiserat beslutsfattande förekommer.\n\n"
        "Dina rättigheter: tillgång, rättelse, radering, begränsning, invändning, återkallelse av samtycke samt "
        "klagomål till en tillsynsmyndighet (i Ungern: NAIH, naih.hu) eller till tillsynsmyndigheten i ditt eget "
        "land (i Sverige: IMY, imy.se). Kontakt: det här formuläret eller webbplatsen.\n\n"
        "Överföring: krypterad (HTTPS/TLS) till claudeusagemonitor.com. Version av den här informationen: 2026-10-06."
    ),
    "fb.privacy_title": "Integritetspolicy",
    "fb.publish": "Mitt betyg och mitt namn (om jag har angett det) får visas på claudeusagemonitor.com.",
    "fb.rating": "Helhetsbetyg",
    "fb.rating_clear": "rensa",
    "fb.rating_hint": "valfritt – klicka på en stjärna",
    "fb.rating_tip": "{} av 5",
    "fb.secure": "Krypterad anslutning (HTTPS) till claudeusagemonitor.com.",
    "fb.send": "Skicka",
    "fb.sending": "Skickar…",
    "fb.sent": "Tack – meddelandet har kommit fram!",
    "fb.sent_sub": "Jag läser varje meddelande. Om du har lämnat en e-postadress svarar jag dit.",
    "fb.title": "Meddelande till utvecklaren",

    # --- Help window -----------------------------------------------------------------------
    "help.disclaimer": "Ett oberoende, kostnadsfritt verktyg – inte gjort av eller knutet till Anthropic. ”Claude” är ett varumärke som tillhör Anthropic.",
    "help.feedback": "Frågor, idéer, felrapporter: meddelandeformuläret på webbplatsen.",
    "help.free": "Alltid gratis · MIT-licens · öppen källkod · ingen telemetri",
    "help.guide": (
        "\n"
        "<h2>Det här visar widgeten</h2>\n"
        "<ul>\n"
        "<li><b>5-timmarssession</b> – hur mycket av den aktuella sessionens gräns som har förbrukats. Den nollställs var femte timme; widgeten räknar ned till nollställningen.</li>\n"
        "<li><b>Veckogräns</b> – användningen för alla modeller tillsammans; den nollställs varje vecka vid en fast tidpunkt som hör till ditt konto.</li>\n"
        "<li><b>Veckogräns per modell</b> – en tredje mätare när servern rapporterar en sådan (t.ex. för en viss modell).</li>\n"
        "<li><b>Takt och förbrukningstakt</b> – hur snabbt du förbrukar gränsen och om den räcker till nollställningen; prognosen för veckans slut varnar i tid.</li>\n"
        "<li><b>Användningskrediter</b> och ditt abonnemangsmärke – när du aktiverar dem under <i>Abonnemangsmärke och extra gränser</i>.</li>\n"
        "</ul>\n"
        "<h2>Varifrån data kommer</h2>\n"
        "<ul>\n"
        "<li><b>claude.ai (alla enheter)</b> – frågar Anthropics server, så användning i mobilen, i webbläsaren och på andra datorer räknas med. Kräver en engångsinloggning i din egen webbläsare (menyn: <i>Logga in</i>). Uppdateras varannan minut, mer sällan om servern begär det.</li>\n"
        "<li><b>Lokal (bara den här datorn)</b> – läser Claude Desktops användningslogg på den här datorn. Ingen inloggning, men den känner bara till den här datorn.</li>\n"
        "</ul>\n"
        "<p>Byt mellan dem i menyn: <i>Datakälla</i>.</p>\n"
        "<h2>Använda widgeten</h2>\n"
        "<ul>\n"
        "<li><b>Högerklicka</b> på widgeten (eller ikonen i meddelandefältet) – hela menyn.</li>\n"
        "<li><b>Dubbelklicka</b> på en mätare – fönstret <b>Historik</b>: 6 timmar, 24 timmar, 7 dagar eller allt, med toppar, dagligt genomsnitt och prognos.</li>\n"
        "<li><b>Dra</b> för att flytta den; den fäster vid skärmkanterna. <b>Ctrl + skrollhjulet</b> – större eller mindre.</li>\n"
        "<li>Layouter: Post-it-kort, smal list, ringar; 6 teman. <i>Lås position</i> och <i>Släpp igenom klick</i> finns i Inställningar.</li>\n"
        "</ul>\n"
        "<h2>Varningar</h2>\n"
        "<p>Gul från 70 %, röd från 90 % (kan ändras). Valfria aviseringar när en gräns nollställs och när data börjar bli inaktuella.</p>\n"
        "<h2>Säkerhetskopior (valfritt)</h2>\n"
        "<p>De små lamporna visar om dina schemalagda säkerhetskopieringar har körts och slutförts. Klicka på en lampa för att se detaljerna. Programmet läser bara loggarna från säkerhetskopieringen – att göra och testa säkerhetskopiorna är ditt ansvar (se användarvillkoren).</p>\n"
        "<h2>Uppdateringar</h2>\n"
        "<p>Programmet söker själv efter nya versioner och uppdateras med ett klick. Varje paket kontrolleras med SHA-256 och kommer bara från <b>claudeusagemonitor.com</b>. Nya versioner och versionsinformation: {site}</p>\n"
        "<h2>Integritet</h2>\n"
        "<p>Ingen telemetri, ingen spårning. Inloggningen till claude.ai lagras krypterad och bara på den här datorn; ingenting skickas någon annanstans.</p>\n"
        "<h2>Om något inte fungerar</h2>\n"
        "<ul>\n"
        "<li><i>429 / för många förfrågningar</i> – servern bromsar förfrågningarna; programmet försöker igen av sig självt.</li>\n"
        "<li>Inga data – kontrollera <i>Datakälla</i>; använder du claude.ai, logga in igen.</li>\n"
        "<li>Historiken sparas i 7 dagar och finns kvar efter omstarter och uppdateringar.</li>\n"
        "<li>Loggar och inställningar: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Skapat av",
    "help.moved": "Ny adress sedan den 21 september 2026 – den tidigare sidan dinorr.hu/claude-usage-monitor omdirigerar hit.",
    "help.official": "OFFICIELL WEBBPLATS",
    "help.open_site": "Öppna claudeusagemonitor.com",
    "help.privacy": "Integritetspolicy",
    "help.site_what": "Nedladdningar, automatiska uppdateringar, nyheter, Claude Backup Kit, användarvillkor och integritet – allt på ett ställe.",
    "help.source_code": "Källkod (GitHub)",
    "help.tab_author": "Utvecklare",
    "help.tab_guide": "Så fungerar det",
    "help.terms": "Användarvillkor",
    "help.title": "Hjälp",
    "help.version": "Version",

    # --- History window --------------------------------------------------------------------
    "hist.legend_5h": "5-timmarssession",
    "hist.legend_week": "veckogräns",
    "hist.no_data": "Inte tillräckligt med data för den här perioden.",
    "hist.range_24h": "24 timmar",
    "hist.range_6h": "6 timmar",
    "hist.range_7d": "7 dagar",
    "hist.range_all": "Allt",
    "hist.stat_burn": "Snittförbrukning per dag",
    "hist.stat_forecast": "Prognos vid veckans slut",
    "hist.stat_now": "Veckan just nu",
    "hist.stat_peak": "Veckans topp",
    "hist.stat_sessions": "5-timmarssessioner",
    "hist.title": "historik",

    # --- layouts ---------------------------------------------------------------------------
    "layout.compact": "Smal list",
    "layout.postit": "Post-it-kort",
    "layout.ring": "Ringar",

    # --- context menu ----------------------------------------------------------------------
    "menu.always_top": "Alltid överst",
    "menu.autostart": "Starta med Windows",
    "menu.backup_bar": "Statusfält för säkerhetskopior",
    "menu.backups": "Säkerhetskopior…",
    "menu.check_update": "Sök efter programuppdateringar…",
    "menu.click_through": "Släpp igenom klick",
    "menu.details": "Abonnemangsmärke och extra gränser",
    "menu.feedback": "Meddelande till utvecklaren…",
    "menu.help": "Hjälp…",
    "menu.history": "Historik och statistik…",
    "menu.language": "Språk",
    "menu.layout": "Layout",
    "menu.locked": "Lås position",
    "menu.login": "Logga in (claude.ai, webbläsare)…",
    "menu.logout": "Logga ut",
    "menu.model_gauge": "{}-mätare",
    "menu.order": "Ordning",
    "menu.panel_visible": "Visa panelen",
    "menu.quit": "Avsluta",
    "menu.refresh": "Uppdatera användningsdata nu",
    "menu.settings": "Inställningar…",
    "menu.size": "Storlek",
    "menu.source": "Datakälla",
    "menu.start_menu": "Visa på Start-menyn",
    "menu.theme": "Tema",
    "menu.update_available": "Programuppdatering: installera version {}…",

    # --- desktop notifications -------------------------------------------------------------
    "notify.autostart_fail": "Det gick inte att ställa in automatisk start.",
    "notify.autostart_off": "Inaktiverat: appen startar inte med Windows.",
    "notify.autostart_on": "Aktiverat: appen startar med Windows.",
    "notify.first_run": "Panelen visas nu i det övre högra hörnet.\nHögerklicka på panelen eller ikonen i meddelandefältet för att öppna menyn.",
    "notify.login_ok": "Inloggad – data hämtas från servern.",
    "notify.logout": "Utloggad. Nu används den lokala datakällan.",
    "notify.reset_done": "{}: nollställd – en ny period har börjat.",
    "notify.signin_needed": "Inloggningen på claude.ai har gått ut. Högerklicka på panelen och logga in igen för att fortsätta se användningen från alla dina enheter.",
    "notify.stale_body": "Senaste mätningen är {} gammal. Körs Claude Desktop?",
    "notify.stale_title": "Inaktuella data",
    "notify.threshold": "{}: {} % förbrukat.",
    "notify.update": "Programversion {} finns tillgänglig. Högerklicka på panelen → Programuppdatering.",

    # --- panel (very tight space) ----------------------------------------------------------
    "panel.five_hour": "5-TIMMARSSESSION",
    "panel.five_hour_short": "5H",
    "panel.full_in": "full: {}",
    "panel.model": "{} VECKA",
    "panel.no_data": "Inga data",
    "panel.pace": "{} vs takt",
    "panel.per_day": "{}%/dag",
    "panel.per_hour": "{}%/h",
    "panel.refreshing": "hämtar data",
    "panel.reset": "nollst. {}",
    "panel.retry_in": "igen om {} s",
    "panel.updated": "hämtat: {}",
    "panel.week_short": "VECKA",
    "panel.weekly": "VECKOGRÄNS",

    # --- profile ---------------------------------------------------------------------------
    "profile.extra": "Användningskrediter: {}",
    "profile.plan": "Abonnemang: {}",
    "profile.since": "Medlem sedan: {}",
    "profile.tier": "Begränsningsnivå: {}",

    # --- Settings window -------------------------------------------------------------------
    "set.about": "{}\nIngen telemetri. Programmet frågar bara Anthropic om din egen användning och läser versionsnumret från uppdateringsservern.",
    "set.accent": "Accentfärg",
    "set.always_top": "Ovanför alla andra fönster",
    "set.auto": "automatiskt",
    "set.backup_config": "Skriptets konfigurationsfil",
    "set.backup_details": "Detaljfönstret visar",
    "set.backup_disclaimer": "Claude Usage Monitor läser och visar bara loggarna från din säkerhetskopiering – programmet skapar, kontrollerar eller garanterar inga säkerhetskopior. Claude Backup Kit är en kostnadsfri utgångspunkt som erbjuds som hjälp: vem som helst kan ändra skripten, så kvaliteten och fullständigheten hos en säkerhetskopia kan inte garanteras. Vi ansvarar inte för säkerhetskopior, förlorade data eller skador av något slag. Var och en ansvarar själv för att säkerhetskopiorna är fullständiga och går att återställa – testa en återställning då och då.",
    "set.backup_disclaimer_h": "Ansvarsfriskrivning",
    "set.backup_enabled": "Visa statusfältet för säkerhetskopior på panelen",
    "set.backup_found": "Hittades: {}",
    "set.backup_green": "Grön upp till",
    "set.backup_label": "Etikett bredvid lampan",
    "set.backup_lamps": "Lampor",
    "set.backup_root": "Mapp för säkerhetskopior",
    "set.backup_tasks": "Filter för schemalagda aktiviteter",
    "set.backup_unconfigured": "Ingen mapp för säkerhetskopior har angetts, så statusfältet förblir dolt. Välj mappen som ditt säkerhetskopieringsskript skriver till.",
    "set.backup_yellow": "Gul upp till",
    "set.browse": "Bläddra…",
    "set.click_through": "Släpp igenom klick (bara dekoration, ignorerar musen)",
    "set.close": "Stäng",
    "set.color_hint": "Färgerna ändras vid tröskelvärdena: grön → gul → röd.",
    "set.danger": "Kritisk",
    "set.data_hint": "Lokal logg: Claude Desktops plan-usage-history.json. Ingen inloggning, men mäter bara den här datorn och uppdateras ungefär var 5:e minut.\n\nclaude.ai: efter inloggningen hämtas data från servern. Du ser användningen från alla dina enheter, med exakta tider för nollställning och tätare uppdatering.",
    "set.datafile": "Datafil",
    "set.default": "Standard",
    "set.details_api_only": "De här uppgifterna kommer från datakällan claude.ai (kräver inloggning); den lokala loggen innehåller dem inte.",
    "set.file_filter": "JSON (*.json);;Alla filer (*.*)",
    "set.gauge_order": "Mätarnas ordning",
    "set.hours_suffix": " h",
    "set.layout": "Layout",
    "set.local_models_hint": "Servern har bara en separat räknare för vissa modeller (t.ex. Fable). För de övriga visar detta hur veckans Claude Code-arbete på den här datorn fördelas – en andel av din egen användning och utdatatokens, inte en andel av en gräns. Bara modellnamnet och antalet tokens läses, aldrig konversationen.",
    "set.local_models_none": "Ingen loggmapp för Claude Code hittades – den här gruppen förblir helt enkelt dold. Inget annat påverkas.",
    "set.local_models_path": "Loggmapp för Claude Code",
    "set.lock": "Lås position (kan inte dras)",
    "set.login_btn_in": "Logga ut från claude.ai",
    "set.login_btn_out": "Logga in på claude.ai…",
    "set.model_filter": "Modell att följa",
    "set.model_scale": "Storlek på modellmätaren",
    "set.not_set": "inte angivet",
    "set.notify_enabled": "Avisera när ett tröskelvärde passeras",
    "set.notify_reset": "Avisera när en gräns nollställs",
    "set.notify_stale": "Avisera när data blir inaktuella",
    "set.opacity": "Opacitet",
    "set.open_config": "Öppna inställningsmappen",
    "set.pick_color": "Välj färg…",
    "set.pick_file_title": "Välj användningslogg",
    "set.profile": "Profil / konto",
    "set.profile_auto": "Automatiskt (senast använd)",
    "set.profile_n": "Profil {} – …{}",
    "set.refresh": "Uppdateringsintervall",
    "set.reset_confirm": "Är du säker på att du vill återställa standardinställningarna?",
    "set.restore": "Återställ standardinställningar",
    "set.rows_available": "Det här kan visas just nu – avmarkera det du inte vill se:",
    "set.rows_none": "Servern skickar just nu inga fler gränser för ditt konto. De visas här automatiskt så fort den gör det.",
    "set.sec_suffix": " s",
    "set.show_age": "Dataålder",
    "set.show_burn": "Förbrukningstakt (%/timme, %/dag)",
    "set.show_extra_usage": "Användningskrediter (betala per användning)",
    "set.show_feedback_icon": "Meddelandeikon i panelens rubrikrad",
    "set.show_five_hour": "Visa 5-timmarssession",
    "set.show_local_models": "Fördelning mellan modellerna, från Claude Codes loggar på den här datorn",
    "set.show_model": "Visa modellens veckogräns (källa: claude.ai)",
    "set.show_model_list": "Veckogränser för övriga modeller",
    "set.show_plan_badge": "Abonnemangsmärke i rubrikraden (Pro / Max…)",
    "set.show_plan_name": "Visa mitt namn på märket",
    "set.show_reset": "Nedräkning till nollställning",
    "set.show_spark": "Trendkurva (sparkline)",
    "set.show_surfaces": "Gränser per yta (Claude Code, anslutna appar…)",
    "set.show_weekly": "Visa veckogräns",
    "set.size": "Storlek",
    "set.snap": "Fäst vid skärmkanten",
    "set.source_api": "claude.ai – alla enheter (inloggning krävs)",
    "set.source_label": "Mätkälla",
    "set.source_local": "Lokal logg – bara den här datorn",
    "set.tab_alerts": "Varningar",
    "set.tab_appearance": "Utseende",
    "set.tab_content": "Innehåll",
    "set.tab_data": "Datakälla",
    "set.tab_details": "Detaljer",
    "set.tab_system": "System",
    "set.taskbar": "Visa i aktivitetsfältet (som ett fönster)",
    "set.theme": "Tema",
    "set.theme_default": "Enligt temat",
    "set.tip": "Tips: dra panelen med vänster musknapp, Ctrl+skroll ändrar storlek,\nhögerklick = meny, dubbelklick = historik.",
    "set.title": "inställningar",
    "set.tray_five": "5-timmarssession",
    "set.tray_max": "Det som är högst",
    "set.tray_value": "Värde på ikonen i meddelandefältet",
    "set.tray_weekly": "Veckogräns",
    "set.update_check": "Sök efter programuppdateringar automatiskt",
    "set.version": "Version",
    "set.visible": "Visa den flytande panelen",
    "set.warn": "Varning",

    # --- sizes, sources, themes ------------------------------------------------------------
    "size.extra": "Extra stor",
    "size.large": "Stor",
    "size.normal": "Normal",
    "size.small": "Liten",
    "source.api": "claude.ai (alla enheter)",
    "source.local": "Lokal (bara den här datorn)",
    "theme.claude": "Claude (varmt mörkt)",
    "theme.graphite": "Grafit",
    "theme.midnight": "Midnattsglas",
    "theme.neon": "Neon",
    "theme.paper": "Ljust papper",
    "theme.postit": "Post-it-gul",

    # --- time units (panel) ----------------------------------------------------------------
    "time.day": "{} d",
    "time.dh": "{}d {}h",
    "time.hm": "{}h {}min",
    "time.hour": "{} h",
    "time.m": "{}min",
    "time.min": "{} min",
    "time.none": "inga data",
    "time.sec": "{} s",

    # --- tray ------------------------------------------------------------------------------
    "tray.head": "5h: {}%   ·   Vecka: {}%",
    "tray.line": "{}: {}%",

    # --- program update --------------------------------------------------------------------
    "update.available": "Version {} finns tillgänglig.",
    "update.check_failed": "Det gick inte att söka efter uppdateringar: {}",
    "update.check_now": "Sök nu",
    "update.checking": "Söker efter uppdateringar…",
    "update.downloading": "Laddar ned… {} av {}",
    "update.failed": "Uppdateringen misslyckades: {}",
    "update.install": "Installera nu",
    "update.installed": "Installerad version: {}",
    "update.later": "Senare",
    "update.manual": "Den här kopian kan inte uppdatera sig själv (den körs från källkod eller från en skrivskyddad mapp). Ladda ned det nya paketet i stället.",
    "update.open_page": "Öppna nedladdningssidan",
    "update.restarting": "Installerar – appen startas om strax.",
    "update.skip": "Hoppa över den här versionen",
    "update.title": "Programuppdatering",
    "update.uptodate": "Du har den senaste versionen.",
    "update.verifying": "Verifierar och packar upp…",
    "update.whats_new": "Nyheter",
}

# macOS wording (the four keys of source.json "mac"): login items and the menu bar (Apple Svenska)
STRINGS_MAC = {
    "menu.autostart": "Öppna vid inloggning",
    "notify.autostart_on": "Aktiverat: appen öppnas när du loggar in.",
    "notify.autostart_off": "Inaktiverat: appen öppnas inte vid inloggning.",
    "notify.first_run": "Panelen visas nu i det övre högra hörnet.\nHögerklicka på panelen eller symbolen i menyraden för att öppna menyn.",
}
