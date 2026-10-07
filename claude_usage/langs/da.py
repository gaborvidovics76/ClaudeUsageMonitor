# -*- coding: utf-8 -*-
"""Dansk – UI strings of Claude Usage Monitor."""

CODE = "da"
NAME = "Dansk"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{}d",
    "backup.age_h": "{}t",
    "backup.age_m": "{}min",
    "backup.and_more": "…og {} mere",
    "backup.checked_at": "Tjekket: {}",
    "backup.checking": "Tjekker…",
    "backup.cloud_only": "Øjebliksbilledet findes kun online i OneDrive; indholdet vises ikke, så det ikke skal downloades.",
    "backup.comp.cowork": "Cowork-chatlogs (én ZIP pr. session)",
    "backup.comp.vault": "Øjebliksbillede af Obsidian-vault (ZIP)",
    "backup.disclaimer_short": "Monitoren viser kun, hvad sikkerhedskopieringens logs siger. Vi påtager os intet ansvar for sikkerhedskopier – det er op til dig at tjekke, at de er komplette og kan gendannes.",
    "backup.done": "færdig",
    "backup.dry_run": "(testkørsel, intet uploadet)",
    "backup.failed": "MISLYKKEDES",
    "backup.files_size": "{} filer, {}",
    "backup.folders": "Mapper",
    "backup.label_age": "Navn og alder",
    "backup.label_name": "Kun navn",
    "backup.label_none": "Kun lamper",
    "backup.last_ok": "Seneste vellykkede sikkerhedskopi: {} (for {} siden)",
    "backup.last_run": "Seneste kørsel: {} – {}",
    "backup.legend": "Grøn: højst {} t gammel · Gul: op til {} t · Rød: ældre eller ingen sikkerhedskopi",
    "backup.level_green": "Frisk",
    "backup.level_none": "Ingen sikkerhedskopi fundet",
    "backup.level_red": "Forældet",
    "backup.level_yellow": "Ved at blive gammel",
    "backup.log_file": "Logfil",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Sikkerhedskopimappen blev ikke fundet: {}",
    "backup.none_found": "Ingen.",
    "backup.open": "åbn",
    "backup.rc_copied": "nye eller ændrede filer kopieret",
    "backup.rc_failed": "MISLYKKEDES (kode {})",
    "backup.rc_nochange": "ajour, intet at kopiere",
    "backup.recent_notes": "Senest redigerede noter i øjebliksbilledet",
    "backup.refresh": "Tjek nu",
    "backup.sec_components": "Hvad der sikkerhedskopieres",
    "backup.sec_contents": "Indhold",
    "backup.sec_log": "Log (seneste linjer)",
    "backup.sec_problems": "Fejl og advarsler",
    "backup.sec_tasks": "Planlagte opgaver",
    "backup.skipped": "sprunget over (mappen blev ikke fundet)",
    "backup.snap_kept": "{} øjebliksbilleder beholdt, {} i alt",
    "backup.snapshot": "Seneste øjebliksbillede",
    "backup.source": "Kilde",
    "backup.state_error": "afsluttet med fejl",
    "backup.state_interrupted": "blev ikke færdig",
    "backup.state_ok": "gennemført uden fejl",
    "backup.state_running": "kører nu",
    "backup.storage": "Fjernlager: {} brugt af {}, {} ledig",
    "backup.target": "Destination",
    "backup.task_event": "ved hændelse",
    "backup.task_row": "seneste kørsel {} · resultat {} · næste {}",
    "backup.tip_click": "Klik for detaljer",
    "backup.title": "Sikkerhedskopier",
    "backup.tray": "Sikkerhedskopier: {}",
    "backup.uploaded": "Uploadet i denne kørsel: {} nye, {} erstattet, {} fejl",
    "backup.uploaded_files": "Uploadede filer",
    "backup.uploaded_groups": "Uploadede filer efter mappe",
    "backup.uploaded_no": "Uploadet til Nextcloud: ikke endnu",
    "backup.uploaded_yes": "Uploadet til Nextcloud: ja ({})",
    "backup.vault": "Vault",
    "backup.vault_changed": "{} noter er ændret i vaulten siden dette øjebliksbillede",
    "backup.zip_new": "{} ny/opdateret ZIP",
    "backup.zip_summary": "{} filer ({} noter), {} ukomprimeret",
    # --- details rows -----------------------------------------------------------------------
    "detail.extra": "Forbrugskreditter",
    "detail.local_header": "CLAUDE CODE · DENNE PC · FORDELING DENNE UGE",
    "detail.off": "fra",
    "detail.on": "til",
    "detail.surface.oauth_apps": "Tilsluttede apps",
    "detail.unlimited": "ingen grænse",
    # --- sign-in dialog ---------------------------------------------------------------------
    "dlg.cancel": "Annuller",
    "dlg.checking": "Tjekker…",
    "dlg.err_badcode": "Koden blev ikke accepteret.\n\n{}\n\nTjek, at du har indsat hele koden, eller prøv at logge på i browseren igen (altid med en ny kode).",
    "dlg.err_ratelimit": "For mange loginforsøg på kort tid.\n\nServeren begrænser dig midlertidigt. Luk dette vindue, vent 10–15 minutter (uden at prøve imens), og start derefter ÉT nyt login i browseren med en ny kode.",
    "dlg.hint1": "Log på den side, der åbnes, og godkend adgangen. Til sidst får du en kode.",
    "dlg.intro": "Log på din claude.ai-konto i din egen browser (dine gemte adgangskoder og adgangsnøgler virker allerede der).",
    "dlg.login_title": "log på",
    "dlg.open_browser": "Åbn login i browseren",
    "dlg.paste_label": "Indsæt den kode, du har fået, her:",
    "dlg.paste_placeholder": "indsæt koden her",
    "dlg.signin": "Log på",
    "dlg.step1": "Trin 1",
    "dlg.step2": "Trin 2",
    "dlg.unknown_err": "Ukendt fejl.",
    # --- error messages ---------------------------------------------------------------------
    "err.already_running": "Appen kører allerede (se i meddelelsesområdet).",
    "err.bad_token_resp": "ugyldigt svar fra tokenslutpunktet",
    "err.bad_usage_resp": "ugyldigt svar fra forbrugsslutpunktet",
    "err.connection": "forbindelsesfejl: {}",
    "err.file_empty": "Forbrugsfilen er tom.",
    "err.file_not_found": "Forbrugsfilen blev ikke fundet.\nKører Claude Desktop?",
    "err.file_unreadable": "Forbrugsfilen kan ikke læses lige nu.",
    "err.loading": "Logger på / henter data…",
    "err.network": "netværksfejl: {}",
    "err.no_code": "Der er ikke indsat nogen kode.",
    "err.no_data_profile": "Ingen data for denne profil.",
    "err.no_tray": "Meddelelsesområdet er ikke tilgængeligt; ikonet springes over.",
    "err.no_usage_data": "Ingen forbrugsdata.",
    "err.not_signed_in": "Ikke logget på.",
    "err.query_http": "Fejl ved forespørgsel (HTTP {}).",
    "err.rate_limited": "Serveren begrænser forespørgslerne (429) – prøver automatisk igen.",
    "err.session_expired": "Sessionen er udløbet. Log på igen.",
    "err.session_expired_nl": "Sessionen er udløbet.\nLog på igen.",
    "err.signin_needed": "Login til claude.ai er udløbet.\nLog på igen: højreklik → Log på claude.ai",
    "err.unexpected": "Uventet fejl: {}",
    # --- "Message to the developer" window --------------------------------------------------
    "fb.cancel": "Annuller",
    "fb.close": "Luk",
    "fb.consent": "Jeg har læst og accepterer udviklerens {}.",
    "fb.email": "E-mail",
    "fb.email_hint": "kun hvis du vil have svar",
    "fb.err_consent": "Du skal acceptere privatlivspolitikken for at sende.",
    "fb.err_email": "E-mailadressen ser ikke rigtig ud.",
    "fb.err_empty": "Skriv en besked, eller vælg en bedømmelse først.",
    "fb.err_links": "For mange links i beskeden.",
    "fb.err_network": "Kunne ikke nå claudeusagemonitor.com. Tjek din forbindelse, og prøv igen.",
    "fb.err_rate": "For mange beskeder på kort tid – prøv igen senere.",
    "fb.err_server": "Serveren kunne ikke tage imod beskeden lige nu. Prøv igen senere.",
    "fb.intro": "En idé, en fejl, eller kan du bare godt lide det? Skriv til mig. Hver eneste besked læses af mig, Vidovics Gábor, programmets udvikler.",
    "fb.message": "Besked",
    "fb.message_ph": "Hvad virker, hvad virker ikke, hvad mangler?",
    "fb.meta": "Sendes sammen med beskeden: programversion {0}, operativsystem ({1}), sprog i brugerfladen ({2}).",
    "fb.name": "Navn",
    "fb.optional": "(valgfrit)",
    "fb.privacy_hide": "Skjul teksten",
    "fb.privacy_text": (
        "Dataansvarlig: Vidovics Gábor, privatperson (Ungarn), udvikleren af Claude Usage Monitor. "
        "Den fulde privatlivspolitik findes på webstedet: https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "Hvad der sendes: det, du skriver her – navn (valgfrit), e-mailadresse (valgfrit), besked, "
        "stjernebedømmelse – samt, så jeg kan forstå sammenhængen, programversionen, operativsystemets navn "
        "og version, sproget i brugerfladen og tidspunktet for afsendelsen. Serveren gemmer ingen IP-adresse; "
        "for at forebygge misbrug bruger den kun en hashværdi, der skifter dagligt, og som ikke kan føres "
        "tilbage til en adresse."
        "\n\n"
        "Hvorfor: for at læse og besvare din besked og for at forbedre programmet (legitim interesse, jf. "
        "artikel 6, stk. 1, litra f, i databeskyttelsesforordningen, GDPR; selve svaret sendes på din "
        "anmodning). Din bedømmelse og dit navn vises kun på webstedet, hvis du sætter kryds i det særskilte "
        "felt for det (samtykke, jf. artikel 6, stk. 1, litra a), og først efter at udvikleren har gennemgået "
        "bedømmelsen; du kan til enhver tid trække dit samtykke tilbage."
        "\n\n"
        "Hvor længe: beskeder i højst 2 år; en offentliggjort bedømmelse, indtil du trækker dit samtykke "
        "tilbage. Hvis udvikleren har slået videresendelse pr. e-mail til, havner en kopi også i udviklerens "
        "indbakke."
        "\n\n"
        "Hvem ser det: kun den dataansvarlige og – som databehandler – hostingudbyderen (server i EU, "
        "Tyskland). Intet sælges eller videregives; der sker ingen profilering og ingen automatiske "
        "afgørelser."
        "\n\n"
        "Dine rettigheder: indsigt, berigtigelse, sletning, begrænsning af behandling, indsigelse, "
        "tilbagetrækning af samtykke samt klage til en tilsynsmyndighed (i Ungarn: NAIH, naih.hu; i Danmark: "
        "Datatilsynet) eller til tilsynsmyndigheden i dit eget land. Kontakt: denne formular eller webstedet."
        "\n\n"
        "Overførsel: krypteret (HTTPS/TLS) til claudeusagemonitor.com. Version af denne tekst: "
        "6. oktober 2026."
    ),
    "fb.privacy_title": "Privatlivspolitik",
    "fb.publish": "Min bedømmelse og mit navn (hvis angivet) må vises på claudeusagemonitor.com.",
    "fb.rating": "Samlet bedømmelse",
    "fb.rating_clear": "ryd",
    "fb.rating_hint": "valgfrit – klik på en stjerne",
    "fb.rating_tip": "{} af 5",
    "fb.secure": "Krypteret forbindelse (HTTPS) til claudeusagemonitor.com.",
    "fb.send": "Send",
    "fb.sending": "Sender…",
    "fb.sent": "Tak – beskeden er modtaget!",
    "fb.sent_sub": "Jeg læser hver eneste besked. Har du angivet en e-mailadresse, svarer jeg dér.",
    "fb.title": "Besked til udvikleren",
    # --- Help window ------------------------------------------------------------------------
    "help.disclaimer": "Et uafhængigt, gratis værktøj – hverken lavet af eller tilknyttet Anthropic. “Claude” er et varemærke tilhørende Anthropic.",
    "help.feedback": "Spørgsmål, idéer, fejlrapporter: beskedformularen på webstedet.",
    "help.free": "Gratis for altid · MIT-licens · open source · ingen telemetri",
    "help.guide": (
        "\n"
        "<h2>Hvad widgetten viser</h2>\n"
        "<ul>\n"
        "<li><b>5-timers session</b> – hvor meget af din aktuelle sessionsgrænse der er brugt. Den nulstilles hver femte time; widgetten tæller ned til nulstillingen.</li>\n"
        "<li><b>Ugegrænse</b> – forbruget på tværs af alle modeller; nulstilles på et fast ugentligt tidspunkt for din konto.</li>\n"
        "<li><b>Ugegrænse pr. model</b> – en tredje måler, når serveren rapporterer en (f.eks. for en bestemt model).</li>\n"
        "<li><b>Tempo og forbrugshastighed</b> – hvor hurtigt du bruger af grænsen, og om den holder til nulstillingen; prognosen for ugens udgang advarer i tide.</li>\n"
        "<li><b>Forbrugskreditter</b> og dit abonnementsbadge – når du slår dem til under <i>Abonnementsbadge og ekstra grænser</i>.</li>\n"
        "</ul>\n"
        "<h2>Hvor dataene kommer fra</h2>\n"
        "<ul>\n"
        "<li><b>claude.ai (alle enheder)</b> – spørger Anthropics server, så forbruget på din telefon, i browseren og på andre computere tælles med. Kræver, at du logger på én gang i din egen browser (menu: <i>Log på</i>). Opdateres hvert 2. minut, langsommere, hvis serveren beder om det.</li>\n"
        "<li><b>Lokal (kun denne pc)</b> – læser Claude Desktops forbrugslog på denne computer. Intet login, men den kender kun denne pc.</li>\n"
        "</ul>\n"
        "<p>Skift mellem dem i menuen: <i>Datakilde</i>.</p>\n"
        "<h2>Sådan bruger du widgetten</h2>\n"
        "<ul>\n"
        "<li><b>Højreklik</b> på widgetten (eller ikonet i meddelelsesområdet) – hele menuen.</li>\n"
        "<li><b>Dobbeltklik</b> på en måler – vinduet <b>Historik</b>: 6 timer, 24 timer, 7 dage eller alt, med toppe, dagligt gennemsnit og en prognose.</li>\n"
        "<li><b>Træk</b> for at flytte den; den fastgøres til skærmkanterne. <b>Ctrl + musehjul</b> – større eller mindre.</li>\n"
        "<li>Layouts: Post-it-kort, smal bjælke, ringe; 6 temaer. <i>Lås placering</i> og <i>Klik igennem</i> findes i Indstillinger.</li>\n"
        "</ul>\n"
        "<h2>Advarsler</h2>\n"
        "<p>Gul fra 70 %, rød fra 90 % (kan justeres). Valgfri meddelelser, når en grænse nulstilles, og når dataene er ved at blive gamle.</p>\n"
        "<h2>Sikkerhedskopier (valgfrit)</h2>\n"
        "<p>De små lamper viser, om dine planlagte sikkerhedskopieringer er kørt og blevet fuldført. Klik på en lampe for detaljer. Monitoren læser kun sikkerhedskopieringens logs – at lave og teste sikkerhedskopierne er dit ansvar (se Vilkår for brug).</p>\n"
        "<h2>Opdateringer</h2>\n"
        "<p>Programmet søger selv efter nye versioner og opdaterer med ét klik. Hver pakke kontrolleres med SHA-256 og kommer kun fra <b>claudeusagemonitor.com</b>. Nye versioner og udgivelsesnoter: {site}</p>\n"
        "<h2>Privatliv</h2>\n"
        "<p>Ingen telemetri, ingen sporing. Dit claude.ai-login gemmes krypteret og kun på denne computer; intet sendes andre steder hen.</p>\n"
        "<h2>Hvis noget ikke virker</h2>\n"
        "<ul>\n"
        "<li><i>429 / begrænset</i> – serveren sætter farten ned på forespørgslerne; programmet prøver selv igen.</li>\n"
        "<li>Ingen data – tjek <i>Datakilde</i>; med claude.ai skal du logge på igen.</li>\n"
        "<li>Historikken gemmes i 7 dage og bevares ved genstart og opdateringer.</li>\n"
        "<li>Logs og indstillinger: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Lavet af",
    "help.moved": "Ny adresse siden 21. september 2026 – den tidligere side dinorr.hu/claude-usage-monitor omdirigerer hertil.",
    "help.official": "OFFICIELT WEBSTED",
    "help.open_site": "Åbn claudeusagemonitor.com",
    "help.privacy": "Privatlivspolitik",
    "help.site_what": "Downloads, automatiske opdateringer, nyheder, Claude Backup Kit, vilkår for brug og privatliv – alt samlet ét sted.",
    "help.source_code": "Kildekode (GitHub)",
    "help.tab_author": "Udvikler",
    "help.tab_guide": "Sådan virker det",
    "help.terms": "Vilkår for brug",
    "help.title": "Hjælp",
    "help.version": "Version",
    # --- History window ---------------------------------------------------------------------
    "hist.legend_5h": "5-timers session",
    "hist.legend_week": "ugegrænse",
    "hist.no_data": "Ikke nok data for denne periode.",
    "hist.range_24h": "24 timer",
    "hist.range_6h": "6 timer",
    "hist.range_7d": "7 dage",
    "hist.range_all": "Alt",
    "hist.stat_burn": "Gns. dagligt forbrug",
    "hist.stat_forecast": "Prognose for ugens udgang",
    "hist.stat_now": "Aktuelt ugeforbrug",
    "hist.stat_peak": "Ugetop",
    "hist.stat_sessions": "5-timers sessioner",
    "hist.title": "historik",
    # --- layouts ----------------------------------------------------------------------------
    "layout.compact": "Smal bjælke",
    "layout.postit": "Post-it-kort",
    "layout.ring": "Ringe",
    # --- context menu -----------------------------------------------------------------------
    "menu.always_top": "Altid øverst",
    "menu.autostart": "Start sammen med Windows",
    "menu.backup_bar": "Statuslinje for sikkerhedskopier",
    "menu.backups": "Sikkerhedskopier…",
    "menu.check_update": "Søg efter programopdateringer…",
    "menu.click_through": "Klik igennem",
    "menu.details": "Abonnementsbadge og ekstra grænser",
    "menu.feedback": "Besked til udvikleren…",
    "menu.help": "Hjælp…",
    "menu.history": "Historik og statistik…",
    "menu.language": "Sprog",
    "menu.layout": "Layout",
    "menu.locked": "Lås placering",
    "menu.login": "Log på (claude.ai, browser)…",
    "menu.logout": "Log af",
    "menu.model_gauge": "{}-måler",
    "menu.order": "Rækkefølge",
    "menu.panel_visible": "Vis panel",
    "menu.quit": "Afslut",
    "menu.refresh": "Opdater forbrugsdata nu",
    "menu.settings": "Indstillinger…",
    "menu.size": "Størrelse",
    "menu.source": "Datakilde",
    "menu.start_menu": "Vis i menuen Start",
    "menu.theme": "Tema",
    "menu.update_available": "Programopdatering: installer version {}…",
    # --- desktop notifications --------------------------------------------------------------
    "notify.autostart_fail": "Automatisk start kunne ikke sættes op.",
    "notify.autostart_off": "Slået fra: appen starter ikke sammen med Windows.",
    "notify.autostart_on": "Slået til: appen starter sammen med Windows.",
    "notify.first_run": "Panelet er dukket op i øverste højre hjørne.\nHøjreklik på panelet eller ikonet i meddelelsesområdet = menu.",
    "notify.login_ok": "Logget på – serverdata er på vej.",
    "notify.logout": "Logget af. Skiftet til lokal kilde.",
    "notify.reset_done": "{}: nulstillet — en ny periode er begyndt.",
    "notify.signin_needed": "Login til claude.ai er udløbet. Højreklik på panelet, og log på igen for fortsat at se forbruget fra alle dine enheder.",
    "notify.stale_body": "Seneste aflæsning er {} gammel. Kører Claude Desktop?",
    "notify.stale_title": "Forældede data",
    "notify.threshold": "{}: {} % brugt.",
    "notify.update": "Programversion {} er tilgængelig. Højreklik på panelet → Programopdatering.",
    # --- floating panel labels (tight space, UPPERCASE) -------------------------------------
    "panel.five_hour": "5-TIMERS SESSION",
    "panel.five_hour_short": "5T",
    "panel.full_in": "fuld: {}",
    "panel.model": "{} UGE",
    "panel.no_data": "Ingen data",
    "panel.pace": "{} vs tempo",
    "panel.per_day": "{}%/dag",
    "panel.per_hour": "{}%/t",
    "panel.refreshing": "henter data",
    "panel.reset": "nulst. om {}",
    "panel.retry_in": "igen om {} s",
    "panel.updated": "opdateret: {}",
    "panel.week_short": "UGE",
    "panel.weekly": "UGEGRÆNSE",
    # --- profile ----------------------------------------------------------------------------
    "profile.extra": "Forbrugskreditter: {}",
    "profile.plan": "Abonnement: {}",
    "profile.since": "Medlem siden: {}",
    "profile.tier": "Grænseniveau: {}",
    # --- Settings window --------------------------------------------------------------------
    "set.about": "{}\nIngen telemetri. Programmet spørger kun Anthropic om dit eget forbrug og læser versionsnummeret fra opdateringsserveren.",
    "set.accent": "Accentfarve",
    "set.always_top": "Oven på alle andre vinduer",
    "set.auto": "automatisk",
    "set.backup_config": "Sikkerhedskopiscriptets konfigurationsfil",
    "set.backup_details": "Detaljevinduet viser",
    "set.backup_disclaimer": "Claude Usage Monitor læser og viser kun loggene fra din sikkerhedskopiering – den laver, tjekker eller garanterer ingen sikkerhedskopi. Claude Backup Kit er et gratis udgangspunkt, der tilbydes som en hjælp: alle kan ændre scriptene, og derfor kan kvaliteten og fuldstændigheden af en sikkerhedskopi ikke garanteres. Vi påtager os intet ansvar for sikkerhedskopier, tabte data eller nogen form for skade. At sikre, at dine sikkerhedskopier er komplette og kan gendannes, er hver enkelts eget ansvar – test en gendannelse en gang imellem.",
    "set.backup_disclaimer_h": "Ansvarsfraskrivelse",
    "set.backup_enabled": "Vis statuslinje for sikkerhedskopier på panelet",
    "set.backup_found": "Fundet: {}",
    "set.backup_green": "Grøn op til",
    "set.backup_label": "Etiket ved siden af lampen",
    "set.backup_lamps": "Lamper",
    "set.backup_root": "Sikkerhedskopimappe",
    "set.backup_tasks": "Filter for planlagte opgaver",
    "set.backup_unconfigured": "Der er ikke valgt nogen sikkerhedskopimappe, så statuslinjen forbliver skjult. Vælg den mappe, dit sikkerhedskopiscript skriver til.",
    "set.backup_yellow": "Gul op til",
    "set.browse": "Gennemse…",
    "set.click_through": "Klik igennem (kun pynt, ignorerer musen)",
    "set.close": "Luk",
    "set.color_hint": "Farverne skifter med tærsklerne: grøn → gul → rød.",
    "set.danger": "Kritisk",
    "set.data_hint": "Lokal log: Claude Desktops plan-usage-history.json. Intet login, men måler kun denne pc og opdateres ca. hvert 5. minut.\n\nclaude.ai: efter login spørger den serveren. Du ser forbruget fra alle dine enheder, med præcise nulstillingstidspunkter og hyppigere opdatering.",
    "set.datafile": "Datafil",
    "set.default": "Standard",
    "set.details_api_only": "Disse kommer fra datakilden claude.ai (kræver login); den lokale log indeholder dem ikke.",
    "set.file_filter": "JSON (*.json);;Alle filer (*.*)",
    "set.gauge_order": "Målernes rækkefølge",
    "set.hours_suffix": " t",
    "set.layout": "Layout",
    "set.local_models_hint": "Serveren fører kun en separat tæller for nogle modeller (f.eks. Fable). For de øvrige viser dette, hvordan denne uges Claude Code-arbejde på denne pc fordeler sig – en andel af dit eget forbrug og outputtokens, ikke en andel af en grænse. Kun modelnavnet og antallet af tokens læses, aldrig samtalen.",
    "set.local_models_none": "Der blev ikke fundet nogen Claude Code-logmappe – denne gruppe vises så bare ikke. Intet andet påvirkes.",
    "set.local_models_path": "Claude Code-logmappe",
    "set.lock": "Lås placering (kan ikke trækkes)",
    "set.login_btn_in": "Log af claude.ai",
    "set.login_btn_out": "Log på claude.ai…",
    "set.model_filter": "Model, der følges",
    "set.model_scale": "Størrelse på modelmåler",
    "set.not_set": "ikke angivet",
    "set.notify_enabled": "Giv besked, når en tærskel overskrides",
    "set.notify_reset": "Giv besked, når en grænse nulstilles",
    "set.notify_stale": "Giv besked, når dataene bliver forældede",
    "set.opacity": "Opacitet",
    "set.open_config": "Åbn indstillingsmappen",
    "set.pick_color": "Vælg farve…",
    "set.pick_file_title": "Vælg forbrugslog",
    "set.profile": "Profil / konto",
    "set.profile_auto": "Automatisk (senest brugt)",
    "set.profile_n": "Profil {} – …{}",
    "set.refresh": "Opdateringsinterval",
    "set.reset_confirm": "Er du sikker på, at du vil gendanne standardindstillingerne?",
    "set.restore": "Gendan standardindstillinger",
    "set.rows_available": "Hvad der kan vises lige nu – fjern fluebenet ved det, du ikke vil se:",
    "set.rows_none": "Serveren sender ingen yderligere grænser for din konto lige nu. De dukker op her af sig selv, så snart den gør.",
    "set.sec_suffix": " s",
    "set.show_age": "Dataalder",
    "set.show_burn": "Forbrugshastighed (%/time, %/dag)",
    "set.show_extra_usage": "Forbrugskreditter (betaling efter forbrug)",
    "set.show_feedback_icon": "Beskedikon i panelets titellinje",
    "set.show_five_hour": "Vis 5-timers session",
    "set.show_local_models": "Fordeling mellem modellerne, fra Claude Codes logs på denne pc",
    "set.show_model": "Vis modellens ugegrænse (kilde: claude.ai)",
    "set.show_model_list": "De øvrige modellers ugegrænser",
    "set.show_plan_badge": "Abonnementsbadge i titellinjen (Pro / Max…)",
    "set.show_plan_name": "Vis mit navn på badget",
    "set.show_reset": "Nedtælling til nulstilling",
    "set.show_spark": "Tendenskurve (sparkline)",
    "set.show_surfaces": "Grænser pr. platform (Claude Code, tilsluttede apps…)",
    "set.show_weekly": "Vis ugegrænse",
    "set.size": "Størrelse",
    "set.snap": "Fastgør til skærmkanten",
    "set.source_api": "claude.ai – alle enheder (kræver login)",
    "set.source_label": "Målekilde",
    "set.source_local": "Lokal log – kun denne pc",
    "set.tab_alerts": "Advarsler",
    "set.tab_appearance": "Udseende",
    "set.tab_content": "Indhold",
    "set.tab_data": "Datakilde",
    "set.tab_details": "Detaljer",
    "set.tab_system": "System",
    "set.taskbar": "Vis på proceslinjen (som vindue)",
    "set.theme": "Tema",
    "set.theme_default": "Temaets standard",
    "set.tip": "Tip: træk panelet med venstre museknap, Ctrl+musehjul ændrer størrelsen,\nhøjreklik = menu, dobbeltklik = historik.",
    "set.title": "indstillinger",
    "set.tray_five": "5-timers session",
    "set.tray_max": "Den højeste af de to",
    "set.tray_value": "Værdi for ikonet i meddelelsesområdet",
    "set.tray_weekly": "Ugegrænse",
    "set.update_check": "Søg automatisk efter programopdateringer",
    "set.version": "Version",
    "set.visible": "Svævende panel synligt",
    "set.warn": "Advarsel",
    # --- sizes, sources, themes -------------------------------------------------------------
    "size.extra": "Ekstra",
    "size.large": "Stor",
    "size.normal": "Normal",
    "size.small": "Lille",
    "source.api": "claude.ai (alle enheder)",
    "source.local": "Lokal (kun denne pc)",
    "theme.claude": "Claude (varmt mørkt)",
    "theme.graphite": "Grafit",
    "theme.midnight": "Midnatsglas",
    "theme.neon": "Neon",
    "theme.paper": "Lyst papir",
    "theme.postit": "Post-it-gul",
    # --- time formats (panel) ---------------------------------------------------------------
    "time.day": "{} d",
    "time.dh": "{}d {}t",
    "time.hm": "{}t {}min",
    "time.hour": "{} t",
    "time.m": "{}min",
    "time.min": "{} min",
    "time.none": "ingen data",
    "time.sec": "{} s",
    # --- tray -------------------------------------------------------------------------------
    "tray.head": "5t: {}%   ·   Uge: {}%",
    "tray.line": "{}: {}%",
    # --- program update ---------------------------------------------------------------------
    "update.available": "Version {} er tilgængelig.",
    "update.check_failed": "Kunne ikke søge efter opdateringer: {}",
    "update.check_now": "Søg nu",
    "update.checking": "Søger efter opdateringer…",
    "update.downloading": "Downloader… {} af {}",
    "update.failed": "Opdateringen mislykkedes: {}",
    "update.install": "Installer nu",
    "update.installed": "Installeret version: {}",
    "update.later": "Senere",
    "update.manual": "Denne kopi kan ikke opdatere sig selv (den kører fra kildekoden eller fra en skrivebeskyttet mappe). Download den nye pakke i stedet.",
    "update.open_page": "Åbn downloadsiden",
    "update.restarting": "Installerer – appen genstarter om et øjeblik.",
    "update.skip": "Spring denne version over",
    "update.title": "Programopdatering",
    "update.uptodate": "Du har den nyeste version.",
    "update.verifying": "Kontrollerer og pakker ud…",
    "update.whats_new": "Nyheder",
}

# macOS wording (Apple Dansk): "Åbn ved login" instead of "start sammen med Windows", menu bar instead of tray
STRINGS_MAC = {
    "menu.autostart": "Åbn ved login",
    "notify.autostart_on": "Slået til: appen åbnes, når du logger ind.",
    "notify.autostart_off": "Slået fra: appen åbnes ikke ved login.",
    "notify.first_run": "Panelet er dukket op i øverste højre hjørne.\nHøjreklik på panelet eller ikonet i menulinjen = menu.",
}
