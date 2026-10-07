# -*- coding: utf-8 -*-
"""Latviešu – UI strings of Claude Usage Monitor."""

CODE = "lv"
NAME = "Latviešu"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{} d",
    "backup.age_h": "{} h",
    "backup.age_m": "{} min",
    "backup.and_more": "…un vēl {}",
    "backup.checked_at": "Pārbaudīts: {}",
    "backup.checking": "Pārbauda…",
    "backup.cloud_only": "Momentuzņēmums pakalpojumā OneDrive ir pieejams tikai tiešsaistē; tā saturs netiek parādīts, lai tas nebūtu jālejupielādē.",
    "backup.comp.cowork": "Cowork tērzēšanas žurnāli (ZIP katrai sesijai)",
    "backup.comp.vault": "Obsidian glabātavas momentuzņēmums (ZIP)",
    "backup.disclaimer_short": "Monitors rāda tikai to, kas rakstīts dublēšanas žurnālos. Mēs neuzņemamies atbildību par dublējumiem – vai tie ir pilnīgi un atjaunojami, jāpārbauda jums pašiem.",
    "backup.done": "pabeigts",
    "backup.dry_run": "(izmēģinājuma palaišana, nekas netika augšupielādēts)",
    "backup.failed": "KĻŪDA",
    "backup.files_size": "Faili: {}, {}",
    "backup.folders": "Mapes",
    "backup.label_age": "Nosaukums un vecums",
    "backup.label_name": "Tikai nosaukums",
    "backup.label_none": "Tikai indikatori",
    "backup.last_ok": "Pēdējais veiksmīgais dublējums: {} (pirms {})",
    "backup.last_run": "Pēdējā palaišana: {} – {}",
    "backup.legend": "Zaļš: ne vecāks par {} h · Dzeltens: līdz {} h · Sarkans: vecāks vai dublējuma nav",
    "backup.level_green": "Svaigs",
    "backup.level_none": "Dublējums nav atrasts",
    "backup.level_red": "Novecojis",
    "backup.level_yellow": "Sāk novecot",
    "backup.log_file": "Žurnālfails",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Dublējumu mape nav atrasta: {}",
    "backup.none_found": "Nav.",
    "backup.open": "atvērt",
    "backup.rc_copied": "jaunie vai mainītie faili nokopēti",
    "backup.rc_failed": "KĻŪDA (kods {})",
    "backup.rc_nochange": "aktuāls, nav ko kopēt",
    "backup.recent_notes": "Pēdējās rediģētās piezīmes momentuzņēmumā",
    "backup.refresh": "Pārbaudīt tūlīt",
    "backup.sec_components": "Kas tiek dublēts",
    "backup.sec_contents": "Saturs",
    "backup.sec_log": "Žurnāls (pēdējās rindas)",
    "backup.sec_problems": "Kļūdas un brīdinājumi",
    "backup.sec_tasks": "Plānotie uzdevumi",
    "backup.skipped": "izlaists (mape nav atrasta)",
    "backup.snap_kept": "Saglabātie momentuzņēmumi: {}, kopā {}",
    "backup.snapshot": "Jaunākais momentuzņēmums",
    "backup.source": "Avots",
    "backup.state_error": "pabeigts ar kļūdām",
    "backup.state_interrupted": "netika pabeigts",
    "backup.state_ok": "veiksmīgi pabeigts",
    "backup.state_running": "pašlaik darbojas",
    "backup.storage": "Attālā krātuve: izmantoti {} no {}, brīvi {}",
    "backup.target": "Galamērķis",
    "backup.task_event": "pēc notikuma",
    "backup.task_row": "pēdējā palaišana {} · rezultāts {} · nākamā {}",
    "backup.tip_click": "Noklikšķiniet, lai skatītu detaļas",
    "backup.title": "Dublējumi",
    "backup.tray": "Dublējumi: {}",
    "backup.uploaded": "Augšupielādēts šajā palaišanā: jauni {}, aizstāti {}, kļūdas {}",
    "backup.uploaded_files": "Augšupielādētie faili",
    "backup.uploaded_groups": "Augšupielādētie faili pa mapēm",
    "backup.uploaded_no": "Augšupielāde pakalpojumā Nextcloud: vēl nav",
    "backup.uploaded_yes": "Augšupielāde pakalpojumā Nextcloud: jā ({})",
    "backup.vault": "Glabātava",
    "backup.vault_changed": "Kopš šī momentuzņēmuma glabātavā mainītas piezīmes: {}",
    "backup.zip_new": "Jauni/atjaunināti ZIP: {}",
    "backup.zip_summary": "Faili: {} (piezīmes: {}), nesaspiesti {}",
    # --- general ------------------------------------------------------------------------------
    "detail.extra": "Lietojuma kredīti",
    "detail.local_header": "CLAUDE CODE · ŠIS DATORS · ŠĪS NEDĒĻAS SADALĪJUMS",
    "detail.off": "izslēgts",
    "detail.on": "ieslēgts",
    "detail.surface.oauth_apps": "Pievienotās lietotnes",
    "detail.unlimited": "bez limita",
    "dlg.cancel": "Atcelt",
    "dlg.checking": "Pārbauda…",
    "dlg.err_badcode": "Kods netika pieņemts.\n\n{}\n\nPārbaudiet, vai ielīmējāt visu kodu, vai arī vēlreiz pierakstieties pārlūkprogrammā (katru reizi ir vajadzīgs jauns kods).",
    "dlg.err_ratelimit": "Pārāk daudz pierakstīšanās mēģinājumu īsā laikā.\n\nServeris uz laiku ierobežo jūsu piekļuvi. Aizveriet šo logu, pagaidiet 10–15 minūtes (pa to laiku nemēģiniet) un pēc tam sāciet VIENU jaunu pierakstīšanos pārlūkprogrammā ar jaunu kodu.",
    "dlg.hint1": "Atvērtajā lapā pierakstieties un atļaujiet piekļuvi. Beigās saņemsiet kodu.",
    "dlg.intro": "Pierakstieties savā claude.ai kontā, izmantojot savu pārlūkprogrammu (tajā jau darbojas jūsu saglabātās paroles un piekļuves atslēgas).",
    "dlg.login_title": "pierakstīšanās",
    "dlg.open_browser": "Atvērt pierakstīšanos pārlūkprogrammā",
    "dlg.paste_label": "Ielīmējiet šeit saņemto kodu:",
    "dlg.paste_placeholder": "ielīmējiet kodu šeit",
    "dlg.signin": "Pierakstīties",
    "dlg.step1": "1. solis",
    "dlg.step2": "2. solis",
    "dlg.unknown_err": "Nezināma kļūda.",
    # --- error messages -----------------------------------------------------------------------
    "err.already_running": "Programma jau darbojas (skatiet paziņojumu apgabalu).",
    "err.bad_token_resp": "nederīga atbilde no marķiera galapunkta",
    "err.bad_usage_resp": "nederīga atbilde no lietojuma galapunkta",
    "err.connection": "savienojuma kļūda: {}",
    "err.file_empty": "Lietojuma fails ir tukšs.",
    "err.file_not_found": "Lietojuma fails nav atrasts.\nVai Claude Desktop darbojas?",
    "err.file_unreadable": "Lietojuma failu pašlaik nevar nolasīt.",
    "err.loading": "Notiek pierakstīšanās / datu iegūšana…",
    "err.network": "tīkla kļūda: {}",
    "err.no_code": "Kods nav ielīmēts.",
    "err.no_data_profile": "Šim profilam nav datu.",
    "err.no_tray": "Paziņojumu apgabals nav pieejams; ikona netiks rādīta.",
    "err.no_usage_data": "Nav lietojuma datu.",
    "err.not_signed_in": "Nav veikta pierakstīšanās.",
    "err.query_http": "Vaicājuma kļūda (HTTP {}).",
    "err.rate_limited": "Serveris ierobežo pieprasījumu skaitu (429) – mēģinājums tiks atkārtots automātiski.",
    "err.session_expired": "Sesijas derīgums ir beidzies, pierakstieties vēlreiz.",
    "err.session_expired_nl": "Sesijas derīgums ir beidzies.\nPierakstieties vēlreiz.",
    "err.signin_needed": "Jūsu claude.ai pierakstīšanās derīgums ir beidzies.\nPierakstieties vēlreiz: labā poga → Pierakstīties vietnē claude.ai",
    "err.unexpected": "Neparedzēta kļūda: {}",
    # --- 'Message to the developer' window ------------------------------------------------------
    "fb.cancel": "Atcelt",
    "fb.close": "Aizvērt",
    "fb.consent": "Esmu izlasījis(-usi) un pieņemu dokumentu „{}”.",
    "fb.email": "E-pasts",
    "fb.email_hint": "tikai tad, ja vēlaties saņemt atbildi",
    "fb.err_consent": "Lai nosūtītu ziņu, lūdzu, pieņemiet privātuma politiku.",
    "fb.err_email": "Šī e-pasta adrese neizskatās pareiza.",
    "fb.err_empty": "Vispirms uzrakstiet ziņu vai izvēlieties vērtējumu.",
    "fb.err_links": "Ziņā ir pārāk daudz saišu.",
    "fb.err_network": "Nevarēja sazināties ar claudeusagemonitor.com. Pārbaudiet interneta savienojumu un mēģiniet vēlreiz.",
    "fb.err_rate": "Pārāk daudz ziņu īsā laikā – lūdzu, mēģiniet vēlāk.",
    "fb.err_server": "Serveris pašlaik nevarēja pieņemt ziņu. Lūdzu, mēģiniet vēlāk.",
    "fb.intro": "Ideja, kļūda vai vienkārši patīk? Uzrakstiet man. Katru ziņu izlasu es pats – Vidovics Gábor, programmas autors.",
    "fb.message": "Ziņa",
    "fb.message_ph": "Kas darbojas, kas nedarbojas, kā trūkst?",
    "fb.meta": "Kopā ar ziņu tiek nosūtīta programmas versija {0}, operētājsistēma ({1}) un saskarnes valoda ({2}).",
    "fb.name": "Vārds",
    "fb.optional": "(nav obligāti)",
    "fb.privacy_hide": "Paslēpt privātuma politiku",
    "fb.privacy_text": (
        "Pārzinis: Vidovics Gábor, privātpersona (Ungārija), Claude Usage Monitor autors. "
        "Pilna privātuma politika ir pieejama tīmekļa vietnē: https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "Kas tiek nosūtīts: tas, ko jūs šeit ievadāt, – vārds (nav obligāti), e-pasta adrese (nav obligāti), "
        "ziņa, vērtējums zvaigznēs –, kā arī, lai es saprastu kontekstu, programmas versija, operētājsistēmas "
        "nosaukums un versija, saskarnes valoda un nosūtīšanas laiks. Serveris neglabā IP adresi; lai novērstu "
        "ļaunprātīgu izmantošanu, tas izmanto tikai katru dienu mainīgu jaucējvērtību, no kuras adresi atjaunot "
        "nav iespējams."
        "\n\n"
        "Kāpēc: lai izlasītu jūsu ziņu un atbildētu uz to, kā arī lai uzlabotu programmu (leģitīmās intereses, "
        "VDAR 6. panta 1. punkta f) apakšpunkts; pati atbilde – pēc jūsu pieprasījuma). Jūsu vērtējums un vārds "
        "tīmekļa vietnē tiek parādīts tikai tad, ja atzīmējat tam paredzēto atsevišķo izvēles rūtiņu "
        "(piekrišana, 6. panta 1. punkta a) apakšpunkts), un tikai pēc tam, kad autors to ir pārskatījis; šo "
        "piekrišanu jūs varat jebkurā laikā atsaukt."
        "\n\n"
        "Cik ilgi: ziņas – ne ilgāk kā 2 gadus; publicēts vērtējums – līdz piekrišanas atsaukšanai. Ja autors "
        "ir ieslēdzis pārsūtīšanu uz e-pastu, kopija nonāk arī autora pastkastītē."
        "\n\n"
        "Kas to redz: tikai pārzinis un – kā apstrādātājs – mitināšanas pakalpojumu sniedzējs (serveris atrodas "
        "ES, Vācijā). Nekas netiek pārdots vai nodots tālāk; netiek veikta ne profilēšana, ne automatizēta "
        "lēmumu pieņemšana."
        "\n\n"
        "Jūsu tiesības: piekļūt saviem datiem, labot tos, dzēst, ierobežot apstrādi, iebilst pret apstrādi, "
        "atsaukt piekrišanu, kā arī iesniegt sūdzību uzraudzības iestādei (Ungārijā: NAIH, naih.hu) vai savas "
        "valsts uzraudzības iestādei. Saziņa: šī veidlapa vai tīmekļa vietne."
        "\n\n"
        "Datu pārsūtīšana: šifrēta (HTTPS/TLS) uz claudeusagemonitor.com. Šīs privātuma politikas versija: "
        "2026. gada 6. oktobris."
    ),
    "fb.privacy_title": "Privātuma politika",
    "fb.publish": "Manu vērtējumu un vārdu (ja norādīts) drīkst parādīt vietnē claudeusagemonitor.com.",
    "fb.rating": "Kopējais vērtējums",
    "fb.rating_clear": "notīrīt",
    "fb.rating_hint": "nav obligāti – noklikšķiniet uz zvaigznes",
    "fb.rating_tip": "{} no 5",
    "fb.secure": "Šifrēts savienojums (HTTPS) ar claudeusagemonitor.com.",
    "fb.send": "Sūtīt",
    "fb.sending": "Sūta…",
    "fb.sent": "Paldies – ziņa saņemta!",
    "fb.sent_sub": "Es izlasu katru ziņu. Ja norādījāt e-pasta adresi, atbildēšu uz to.",
    "fb.title": "Ziņa izstrādātājam",
    # --- Help window ------------------------------------------------------------------------
    "help.disclaimer": "Neatkarīgs, bezmaksas rīks – to nav izstrādājis Anthropic, un tas nav saistīts ar Anthropic. „Claude” ir Anthropic preču zīme.",
    "help.feedback": "Jautājumi, idejas, ziņojumi par kļūdām: ziņas veidlapa tīmekļa vietnē.",
    "help.free": "Vienmēr bezmaksas · MIT licence · atvērtais pirmkods · bez telemetrijas",
    "help.guide": (
        "\n"
        "<h2>Ko rāda logrīks</h2>\n"
        "<ul>\n"
        "<li><b>5 stundu sesija</b> – cik liela daļa no pašreizējās sesijas limita ir izlietota. Limits tiek atiestatīts ik pēc piecām stundām; logrīks rāda atpakaļskaitīšanu līdz atiestatīšanai.</li>\n"
        "<li><b>Nedēļas limits</b> – visu modeļu kopējais lietojums; tas tiek atiestatīts reizi nedēļā jūsu kontam noteiktā laikā.</li>\n"
        "<li><b>Modeļa nedēļas limits</b> – trešais mērītājs, ja serveris tādu norāda (piemēram, konkrētam modelim).</li>\n"
        "<li><b>Temps un patēriņa ātrums</b> – cik ātri jūs izlietojat limitu un vai ar to pietiks līdz atiestatīšanai; prognoze nedēļas beigām brīdina laikus.</li>\n"
        "<li><b>Lietojuma kredīti</b> un jūsu plāna emblēma – ja tos ieslēdzat sadaļā <i>Plāna emblēma un papildu limiti</i>.</li>\n"
        "</ul>\n"
        "<h2>No kurienes nāk dati</h2>\n"
        "<ul>\n"
        "<li><b>claude.ai (visas ierīces)</b> – dati tiek iegūti no Anthropic servera, tāpēc tiek ieskaitīts arī lietojums tālrunī, pārlūkprogrammā un citos datoros. Vienreiz jāpierakstās savā pārlūkprogrammā (izvēlne: <i>Pierakstīties</i>). Dati tiek atsvaidzināti ik pēc 2 minūtēm vai retāk, ja serveris to pieprasa.</li>\n"
        "<li><b>Lokālais (tikai šis dators)</b> – nolasa Claude Desktop lietojuma žurnālu šajā datorā. Nav jāpierakstās, taču tas zina tikai par šo datoru.</li>\n"
        "</ul>\n"
        "<p>Pārslēgties var izvēlnē: <i>Datu avots</i>.</p>\n"
        "<h2>Logrīka lietošana</h2>\n"
        "<ul>\n"
        "<li><b>Labā poga</b> uz logrīka (vai paziņojumu apgabala ikonas) – pilnā izvēlne.</li>\n"
        "<li><b>Dubultklikšķis</b> uz mērītāja – logs <b>Vēsture</b>: 6 stundas, 24 stundas, 7 dienas vai viss, ar maksimumiem, vidējo patēriņu dienā un prognozi.</li>\n"
        "<li><b>Velciet</b>, lai pārvietotu; logrīks piesaistās ekrāna malām. <b>Ctrl + peles ritenītis</b> – lielāks vai mazāks.</li>\n"
        "<li>Izkārtojumi: līmlapiņa, šaura josla, gredzeni; 6 dizaini. <i>Fiksēt pozīciju</i> un <i>Klikšķu caurlaidība</i> ir atrodami iestatījumos.</li>\n"
        "</ul>\n"
        "<h2>Brīdinājumi</h2>\n"
        "<p>Dzeltens no 70 %, sarkans no 90 % (var pielāgot). Pēc izvēles – paziņojumi, kad limits tiek atiestatīts un kad dati noveco.</p>\n"
        "<h2>Dublējumi (nav obligāti)</h2>\n"
        "<p>Mazie indikatori rāda, vai jūsu plānotie dublējumi tika palaisti un pabeigti. Noklikšķiniet uz indikatora, lai skatītu detaļas. Monitors tikai nolasa dublēšanas žurnālus – dublējumu izveide un pārbaude ir jūsu ziņā (skatiet lietošanas noteikumus).</p>\n"
        "<h2>Atjauninājumi</h2>\n"
        "<p>Programma pati meklē jaunas versijas un atjauninās ar vienu klikšķi. Katra pakotne tiek pārbaudīta ar SHA-256 un tiek lejupielādēta tikai no <b>claudeusagemonitor.com</b>. Jaunās versijas un jaunumi: {site}</p>\n"
        "<h2>Privātums</h2>\n"
        "<p>Bez telemetrijas, bez izsekošanas. Jūsu claude.ai pierakstīšanās tiek glabāta šifrētā veidā tikai šajā datorā; nekas netiek sūtīts citur.</p>\n"
        "<h2>Ja kaut kas nedarbojas</h2>\n"
        "<ul>\n"
        "<li><i>429 / ierobežojums</i> – serveris palēnina pieprasījumus; programma pati mēģina vēlreiz.</li>\n"
        "<li>Nav datu – pārbaudiet <i>Datu avotu</i>; ja izmantojat claude.ai, pierakstieties vēlreiz.</li>\n"
        "<li>Vēsture tiek glabāta 7 dienas un saglabājas arī pēc restartēšanas un atjaunināšanas.</li>\n"
        "<li>Žurnāli un iestatījumi: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Izstrādāja",
    "help.moved": "Jaunā adrese kopš 2026. gada 21. septembra – iepriekšējā lapa dinorr.hu/claude-usage-monitor novirza uz šo vietni.",
    "help.official": "OFICIĀLĀ TĪMEKĻA VIETNE",
    "help.open_site": "Atvērt claudeusagemonitor.com",
    "help.privacy": "Privātuma politika",
    "help.site_what": "Lejupielādes, automātiskie atjauninājumi, jaunumi, Claude Backup Kit, lietošanas noteikumi un privātums – viss vienuviet.",
    "help.source_code": "Pirmkods (GitHub)",
    "help.tab_author": "Autors",
    "help.tab_guide": "Kā tas darbojas",
    "help.terms": "Lietošanas noteikumi",
    "help.title": "Palīdzība",
    "help.version": "Versija",
    # --- History window ---------------------------------------------------------------------
    "hist.legend_5h": "5 stundu sesija",
    "hist.legend_week": "nedēļas limits",
    "hist.no_data": "Šim periodam nepietiek datu.",
    "hist.range_24h": "24 stundas",
    "hist.range_6h": "6 stundas",
    "hist.range_7d": "7 dienas",
    "hist.range_all": "Viss",
    "hist.stat_burn": "Vid. patēriņš dienā",
    "hist.stat_forecast": "Prognoze nedēļas beigām",
    "hist.stat_now": "Nedēļā līdz šim",
    "hist.stat_peak": "Nedēļas maksimums",
    "hist.stat_sessions": "5 stundu sesijas",
    "hist.title": "vēsture",
    # --- menu options -------------------------------------------------------------------------
    "layout.compact": "Šaura josla",
    "layout.postit": "Līmlapiņa",
    "layout.ring": "Gredzeni",
    "menu.always_top": "Vienmēr virspusē",
    "menu.autostart": "Palaist kopā ar Windows",
    "menu.backup_bar": "Dublējumu statusa josla",
    "menu.backups": "Dublējumi…",
    "menu.check_update": "Meklēt programmas atjauninājumus…",
    "menu.click_through": "Klikšķu caurlaidība",
    "menu.details": "Plāna emblēma un papildu limiti",
    "menu.feedback": "Ziņa izstrādātājam…",
    "menu.help": "Palīdzība…",
    "menu.history": "Vēsture un statistika…",
    "menu.language": "Valoda",
    "menu.layout": "Izkārtojums",
    "menu.locked": "Fiksēt pozīciju",
    "menu.login": "Pierakstīties (claude.ai, pārlūkprogramma)…",
    "menu.logout": "Izrakstīties",
    "menu.model_gauge": "{} mērītājs",
    "menu.order": "Secība",
    "menu.panel_visible": "Rādīt paneli",
    "menu.quit": "Iziet",
    "menu.refresh": "Atsvaidzināt lietojuma datus tūlīt",
    "menu.settings": "Iestatījumi…",
    "menu.size": "Izmērs",
    "menu.source": "Datu avots",
    "menu.start_menu": "Rādīt izvēlnē Sākt",
    "menu.theme": "Dizains",
    "menu.update_available": "Programmas atjauninājums: instalēt versiju {}…",
    # --- desktop notifications ----------------------------------------------------------------
    "notify.autostart_fail": "Neizdevās iestatīt automātisko palaišanu.",
    "notify.autostart_off": "Izslēgts: programma netiks palaista kopā ar Windows.",
    "notify.autostart_on": "Ieslēgts: programma tiks palaista kopā ar Windows.",
    "notify.first_run": "Panelis parādījās ekrāna augšējā labajā stūrī.\nLabā poga uz paneļa vai paziņojumu apgabala ikonas = izvēlne.",
    "notify.login_ok": "Pierakstīšanās izdevās – tiek saņemti servera dati.",
    "notify.logout": "Jūs izrakstījāties. Tagad tiek izmantots lokālais avots.",
    "notify.reset_done": "{}: atiestatīšana – sācies jauns periods.",
    "notify.signin_needed": "Jūsu claude.ai pierakstīšanās derīgums ir beidzies. Noklikšķiniet ar peles labo pogu uz paneļa un pierakstieties vēlreiz, lai joprojām redzētu lietojumu no visām savām ierīcēm.",
    "notify.stale_body": "Pēdējais mērījums veikts pirms {}. Vai Claude Desktop darbojas?",
    "notify.stale_title": "Novecojuši dati",
    "notify.threshold": "{}: izlietoti {} %.",
    "notify.update": "Pieejama programmas versija {}. Labā poga uz paneļa → Programmas atjauninājums.",
    # --- floating panel -----------------------------------------------------------------------
    "panel.five_hour": "5 STUNDU SESIJA",
    "panel.five_hour_short": "5H",
    "panel.full_in": "pilns pēc {}",
    "panel.model": "{} NEDĒĻĀ",
    "panel.no_data": "Nav datu",
    "panel.pace": "temps {}",
    "panel.per_day": "{}%/d",
    "panel.per_hour": "{}%/h",
    "panel.refreshing": "ielādē datus",
    "panel.reset": "atiestatīs pēc {}",
    "panel.retry_in": "vēlreiz pēc {} s",
    "panel.updated": "atjaunots: {}",
    "panel.week_short": "NED.",
    "panel.weekly": "NEDĒĻAS LIMITS",
    # --- profile ------------------------------------------------------------------------------
    "profile.extra": "Lietojuma kredīti: {}",
    "profile.plan": "Plāns: {}",
    "profile.since": "Dalībnieks kopš: {}",
    "profile.tier": "Ierobežojumu līmenis: {}",
    # --- Settings window ----------------------------------------------------------------------
    "set.about": "{}\nBez telemetrijas. Programma tikai pieprasa Anthropic datus par jūsu lietojumu un nolasa versijas numuru no atjauninājumu servera.",
    "set.accent": "Akcenta krāsa",
    "set.always_top": "Virs visiem pārējiem logiem",
    "set.auto": "automātiski",
    "set.backup_config": "Dublēšanas skripta konfigurācija",
    "set.backup_details": "Detaļu logā rādīt",
    "set.backup_disclaimer": "Claude Usage Monitor tikai nolasa un parāda jūsu dublēšanas žurnālus – tas neveido, nepārbauda un negarantē nekādus dublējumus. Claude Backup Kit ir bezmaksas sākumpunkts, kas piedāvāts kā palīdzība: skriptus var mainīt ikviens, tāpēc dublējuma kvalitāti un pilnīgumu nevar garantēt. Mēs neuzņemamies atbildību par dublējumiem, datu zudumu vai jebkādiem zaudējumiem. Katrs pats atbild par to, lai viņa dublējumi būtu pilnīgi un atjaunojami, – laiku pa laikam izmēģiniet atjaunošanu.",
    "set.backup_disclaimer_h": "Atruna",
    "set.backup_enabled": "Rādīt dublējumu statusa joslu panelī",
    "set.backup_found": "Atrasts: {}",
    "set.backup_green": "Zaļš līdz",
    "set.backup_label": "Uzraksts blakus indikatoram",
    "set.backup_lamps": "Indikatori",
    "set.backup_root": "Dublējumu mape",
    "set.backup_tasks": "Plānoto uzdevumu filtrs",
    "set.backup_unconfigured": "Dublējumu mape nav iestatīta, tāpēc statusa josla ir paslēpta. Izvēlieties mapi, kurā raksta jūsu dublēšanas skripts.",
    "set.backup_yellow": "Dzeltens līdz",
    "set.browse": "Pārlūkot…",
    "set.click_through": "Klikšķu caurlaidība (tikai dekorācija, nereaģē uz peli)",
    "set.close": "Aizvērt",
    "set.color_hint": "Krāsas mainās atkarībā no sliekšņiem: zaļa → dzeltena → sarkana.",
    "set.danger": "Kritisks",
    "set.data_hint": "Lokālais žurnāls: Claude Desktop fails plan-usage-history.json. Nav jāpierakstās, taču tiek mērīts tikai šis dators, un dati tiek atsvaidzināti aptuveni ik pēc 5 minūtēm.\n\nclaude.ai: pēc pierakstīšanās dati tiek iegūti no servera. Jūs redzat lietojumu no visām savām ierīcēm ar precīziem atiestatīšanas laikiem un biežāku atsvaidzināšanu.",
    "set.datafile": "Datu fails",
    "set.default": "Noklusējums",
    "set.details_api_only": "Šie dati nāk no claude.ai datu avota (nepieciešama pierakstīšanās); lokālajā žurnālā to nav.",
    "set.file_filter": "JSON (*.json);;Visi faili (*.*)",
    "set.gauge_order": "Mērītāju secība",
    "set.hours_suffix": " h",
    "set.layout": "Izkārtojums",
    "set.local_models_hint": "Serveris atsevišķu skaitītāju uztur tikai dažiem modeļiem (piem., Fable). Pārējiem šeit redzams, kā sadalās šīs nedēļas Claude Code darbs šajā datorā – jūsu lietojuma daļa un izvades tokeni, nevis limita daļa. Tiek nolasīts tikai modeļa nosaukums un tokenu skaits, nekad – saruna.",
    "set.local_models_none": "Claude Code žurnālu mape netika atrasta – šī grupa vienkārši paliek paslēpta. Nekas cits netiek ietekmēts.",
    "set.local_models_path": "Claude Code žurnālu mape",
    "set.lock": "Fiksēt pozīciju (nevar pārvilkt)",
    "set.login_btn_in": "Izrakstīties no claude.ai",
    "set.login_btn_out": "Pierakstīties vietnē claude.ai…",
    "set.model_filter": "Uzraugāmais modelis",
    "set.model_scale": "Modeļa mērītāja izmērs",
    "set.not_set": "nav iestatīts",
    "set.notify_enabled": "Paziņot, kad tiek pārsniegts slieksnis",
    "set.notify_reset": "Paziņot, kad limits tiek atiestatīts",
    "set.notify_stale": "Paziņot, kad dati noveco",
    "set.opacity": "Necaurredzamība",
    "set.open_config": "Atvērt iestatījumu mapi",
    "set.pick_color": "Izvēlēties krāsu…",
    "set.pick_file_title": "Izvēlēties lietojuma žurnālu",
    "set.profile": "Profils / konts",
    "set.profile_auto": "Automātiski (pēdējais lietotais)",
    "set.profile_n": "Profils {} – …{}",
    "set.refresh": "Atsvaidzināšanas intervāls",
    "set.reset_confirm": "Vai tiešām vēlaties atjaunot noklusējuma iestatījumus?",
    "set.restore": "Atjaunot noklusējumus",
    "set.rows_available": "Ko pašlaik var parādīt – noņemiet atzīmi no tā, ko nevēlaties redzēt:",
    "set.rows_none": "Serveris pašlaik nesūta citus limitus jūsu kontam. Tiklīdz tas notiks, tie automātiski parādīsies šeit.",
    "set.sec_suffix": " s",
    "set.show_age": "Datu aktualitāte",
    "set.show_burn": "Patēriņa ātrums (%/h, %/d)",
    "set.show_extra_usage": "Lietojuma kredīti (maksa par faktisko lietojumu)",
    "set.show_feedback_icon": "Ziņas ikona paneļa galvenē",
    "set.show_five_hour": "Rādīt 5 stundu sesiju",
    "set.show_local_models": "Sadalījums starp modeļiem no Claude Code žurnāliem šajā datorā",
    "set.show_model": "Rādīt modeļa nedēļas limitu (claude.ai avots)",
    "set.show_model_list": "Citu modeļu nedēļas limiti",
    "set.show_plan_badge": "Plāna emblēma galvenē (Pro / Max…)",
    "set.show_plan_name": "Rādīt manu vārdu uz emblēmas",
    "set.show_reset": "Atpakaļskaitīšana līdz atiestatīšanai",
    "set.show_spark": "Tendences līkne (mazdiagramma)",
    "set.show_surfaces": "Limiti pa saskarnēm (Claude Code, pievienotās lietotnes…)",
    "set.show_weekly": "Rādīt nedēļas limitu",
    "set.size": "Izmērs",
    "set.snap": "Piesaistīt ekrāna malai",
    "set.source_api": "claude.ai – visas ierīces (nepieciešama pierakstīšanās)",
    "set.source_label": "Mērījumu avots",
    "set.source_local": "Lokālais žurnāls – tikai šis dators",
    "set.tab_alerts": "Brīdinājumi",
    "set.tab_appearance": "Izskats",
    "set.tab_content": "Saturs",
    "set.tab_data": "Datu avots",
    "set.tab_details": "Detaļas",
    "set.tab_system": "Sistēma",
    "set.taskbar": "Rādīt uzdevumjoslā (kā logu)",
    "set.theme": "Dizains",
    "set.theme_default": "Dizaina noklusējums",
    "set.tip": "Padoms: velciet paneli ar kreiso pogu, Ctrl+ritināšana maina izmēru,\nlabā poga = izvēlne, dubultklikšķis = vēsture.",
    "set.title": "iestatījumi",
    "set.tray_five": "5 stundu sesija",
    "set.tray_max": "Lielākā vērtība",
    "set.tray_value": "Paziņojumu apgabala ikonas vērtība",
    "set.tray_weekly": "Nedēļas limits",
    "set.update_check": "Automātiski meklēt programmas atjauninājumus",
    "set.version": "Versija",
    "set.visible": "Peldošais panelis redzams",
    "set.warn": "Brīdinājums",
    # --- menu options (size, data source, theme) ------------------------------------------------
    "size.extra": "Īpaši liels",
    "size.large": "Liels",
    "size.normal": "Normāls",
    "size.small": "Mazs",
    "source.api": "claude.ai (visas ierīces)",
    "source.local": "Lokālais (tikai šis dators)",
    "theme.claude": "Claude (silti tumšs)",
    "theme.graphite": "Grafīts",
    "theme.midnight": "Pusnakts stikls",
    "theme.neon": "Neons",
    "theme.paper": "Gaišs papīrs",
    "theme.postit": "Līmlapiņu dzeltens",
    # --- time units ---------------------------------------------------------------------------
    "time.day": "{} d",
    "time.dh": "{}d {}h",
    "time.hm": "{}h {}min",
    "time.hour": "{} h",
    "time.m": "{}min",
    "time.min": "{} min",
    "time.none": "nav datu",
    "time.sec": "{} s",
    # --- tray ---------------------------------------------------------------------------------
    "tray.head": "5h: {}%   ·   Ned.: {}%",
    "tray.line": "{}: {}%",
    # --- program update -----------------------------------------------------------------------
    "update.available": "Pieejama versija {}.",
    "update.check_failed": "Neizdevās pārbaudīt atjauninājumus: {}",
    "update.check_now": "Pārbaudīt tūlīt",
    "update.checking": "Meklē atjauninājumus…",
    "update.downloading": "Lejupielādē… {} no {}",
    "update.failed": "Atjaunināšana neizdevās: {}",
    "update.install": "Instalēt tūlīt",
    "update.installed": "Instalētā versija: {}",
    "update.later": "Vēlāk",
    "update.manual": "Šī kopija nevar pati sevi atjaunināt (tā darbojas no pirmkoda vai no mapes, kurā nav rakstīšanas atļaujas). Lejupielādējiet jauno pakotni.",
    "update.open_page": "Atvērt lejupielādes lapu",
    "update.restarting": "Notiek instalēšana – programma pēc brīža restartēsies.",
    "update.skip": "Izlaist šo versiju",
    "update.title": "Programmas atjauninājums",
    "update.uptodate": "Jums ir jaunākā versija.",
    "update.verifying": "Pārbauda un izpako…",
    "update.whats_new": "Jaunumi",
}

# macOS wording (Apple LV): "Atvērt pierakstoties" instead of "Palaist kopā ar Windows", menu bar instead of tray
STRINGS_MAC = {
    "menu.autostart": "Atvērt pierakstoties",
    "notify.autostart_on": "Ieslēgts: programma tiks atvērta, kad pierakstīsieties.",
    "notify.autostart_off": "Izslēgts: programma netiks atvērta, kad pierakstīsieties.",
    "notify.first_run": "Panelis parādījās ekrāna augšējā labajā stūrī.\nLabā poga uz paneļa vai izvēļņu joslas ikonas = izvēlne.",
}
