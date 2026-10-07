# -*- coding: utf-8 -*-
"""Malti – UI strings of Claude Usage Monitor."""

CODE = "mt"
NAME = "Malti"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{}j",
    "backup.age_h": "{}h",
    "backup.age_m": "{}min",
    "backup.and_more": "…u {} oħra",
    "backup.checked_at": "Iċċekkjat: {}",
    "backup.checking": "Qed jiċċekkja…",
    "backup.cloud_only": "Is-snapshot jinsab online biss f'OneDrive; il-kontenut tiegħu mhuwiex elenkat biex ma jkollux għalfejn jitniżżel.",
    "backup.comp.cowork": "Logs taċ-chat ta' Cowork (ZIP għal kull sessjoni)",
    "backup.comp.vault": "Snapshot tal-vault ta' Obsidian (ZIP)",
    "backup.disclaimer_short": "Il-monitor juri biss dak li jgħidu l-logs tal-backup. Ma naċċettaw l-ebda responsabbiltà għall-backups – hija r-responsabbiltà tiegħek li tiċċekkja li huma kompluti u li jistgħu jiġu rrestawrati.",
    "backup.done": "lest",
    "backup.dry_run": "(test, ma ttella' xejn)",
    "backup.failed": "FALLA",
    "backup.files_size": "Fajls: {}, {}",
    "backup.folders": "Folders",
    "backup.label_age": "Isem u kemm ilu",
    "backup.label_name": "Isem biss",
    "backup.label_none": "Dwal biss",
    "backup.last_ok": "L-aħħar backup b'suċċess: {} ({} ilu)",
    "backup.last_run": "L-aħħar tħaddim: {} – {}",
    "backup.legend": "Aħdar: mhux eqdem minn {} h · Isfar: sa {} h · Aħmar: eqdem, jew l-ebda backup",
    "backup.level_green": "Riċenti",
    "backup.level_none": "Ma nstab l-ebda backup",
    "backup.level_red": "Qadim",
    "backup.level_yellow": "Qed isir qadim",
    "backup.log_file": "Fajl tal-log",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Il-folder tal-backups ma nstabx: {}",
    "backup.none_found": "Xejn.",
    "backup.open": "iftaħ",
    "backup.rc_copied": "ġew ikkupjati fajls ġodda jew mibdula",
    "backup.rc_failed": "FALLA (kodiċi {})",
    "backup.rc_nochange": "aġġornat, xejn x'jiġi kkupjat",
    "backup.recent_notes": "L-aħħar noti editjati fis-snapshot",
    "backup.refresh": "Iċċekkja issa",
    "backup.sec_components": "X'jidħol fil-backup",
    "backup.sec_contents": "Kontenut",
    "backup.sec_log": "Log (l-aħħar linji)",
    "backup.sec_problems": "Żbalji u twissijiet",
    "backup.sec_tasks": "Kompiti skedati",
    "backup.skipped": "maqbuż (il-folder ma nstabx)",
    "backup.snap_kept": "Snapshots miżmuma: {}, {} b'kollox",
    "backup.snapshot": "L-aħħar snapshot",
    "backup.source": "Sors",
    "backup.state_error": "spiċċa bi żbalji",
    "backup.state_interrupted": "ma spiċċax",
    "backup.state_ok": "intemm b'suċċess",
    "backup.state_running": "għaddej issa",
    "backup.storage": "Ħażna remota: {} użati minn {}, {} liberi",
    "backup.target": "Destinazzjoni",
    "backup.task_event": "fuq avveniment",
    "backup.task_row": "l-aħħar tħaddim {} · riżultat {} · li jmiss {}",
    "backup.tip_click": "Ikklikkja għad-dettalji",
    "backup.title": "Backups",
    "backup.tray": "Backups: {}",
    "backup.uploaded": "Mtella' f'dan it-tħaddim: {} ġodda, {} sostitwiti, {} żbalji",
    "backup.uploaded_files": "Fajls mtellgħin",
    "backup.uploaded_groups": "Fajls mtellgħin skont il-folder",
    "backup.uploaded_no": "Mtella' f'Nextcloud: għadu le",
    "backup.uploaded_yes": "Mtella' f'Nextcloud: iva ({})",
    "backup.vault": "Vault",
    "backup.vault_changed": "Noti mibdula fil-vault minn dan is-snapshot 'l hawn: {}",
    "backup.zip_new": "ZIP ġodda/aġġornati: {}",
    "backup.zip_summary": "Fajls: {0} (noti: {1}), daqs mhux kompressat: {2}",

    # --- general -------------------------------------------------------------------------------
    "detail.extra": "Krediti tal-użu",
    "detail.local_header": "CLAUDE CODE · DAN IL-PC · QSIM TA' DIN IL-ĠIMGĦA",
    "detail.off": "mitfi",
    "detail.on": "mixgħul",
    "detail.surface.oauth_apps": "Apps konnessi",
    "detail.unlimited": "l-ebda limitu",
    "dlg.cancel": "Ikkanċella",
    "dlg.checking": "Qed jiċċekkja…",
    "dlg.err_badcode": "Il-kodiċi ma ġiex aċċettat.\n\n{}\n\nIċċekkja li waħħalt il-kodiċi kollu, jew erġa' pprova l-login mill-browser (dejjem b'kodiċi ġdid).",
    "dlg.err_ratelimit": "Wisq tentattivi ta' login fi ftit ħin.\n\nIs-server qed jillimitak b'mod temporanju. Agħlaq din it-tieqa, stenna 10–15-il minuta (tippruvax sadanittant), imbagħad ibda login ġdid WIEĦED biss mill-browser b'kodiċi ġdid.",
    "dlg.hint1": "Idħol fil-paġna li tinfetaħ u approva l-aċċess. Fl-aħħar tirċievi kodiċi.",
    "dlg.intro": "Idħol fil-kont tiegħek ta' claude.ai fil-browser tiegħek stess (il-passwords u l-passkeys salvati tiegħek diġà jaħdmu hemm).",
    "dlg.login_title": "idħol",
    "dlg.open_browser": "Iftaħ il-login fil-browser",
    "dlg.paste_label": "Waħħal hawn il-kodiċi li rċevejt:",
    "dlg.paste_placeholder": "waħħal il-kodiċi hawn",
    "dlg.signin": "Idħol",
    "dlg.step1": "Pass 1",
    "dlg.step2": "Pass 2",
    "dlg.unknown_err": "Żball mhux magħruf.",

    # --- error messages ------------------------------------------------------------------------
    "err.already_running": "Il-programm diġà għaddej (ara ż-żona tan-notifiki).",
    "err.bad_token_resp": "tweġiba invalida mill-endpoint tat-token",
    "err.bad_usage_resp": "tweġiba invalida mill-endpoint tal-użu",
    "err.connection": "żball fil-konnessjoni: {}",
    "err.file_empty": "Il-fajl tal-użu huwa vojt.",
    "err.file_not_found": "Il-fajl tal-użu ma nstabx.\nClaude Desktop għaddej?",
    "err.file_unreadable": "Bħalissa l-fajl tal-użu ma jistax jinqara.",
    "err.loading": "Qed jidħol / qed jiġbor id-data…",
    "err.network": "żball fin-netwerk: {}",
    "err.no_code": "Ma twaħħal l-ebda kodiċi.",
    "err.no_data_profile": "L-ebda data għal dan il-profil.",
    "err.no_tray": "Iż-żona tan-notifiki mhix disponibbli; l-ikona mhux se tintwera.",
    "err.no_usage_data": "L-ebda data tal-użu.",
    "err.not_signed_in": "Ma sar l-ebda login.",
    "err.query_http": "Żball fit-talba (HTTP {}).",
    "err.rate_limited": "Is-server qed jillimita t-talbiet (429) – se jerġa' jipprova awtomatikament.",
    "err.session_expired": "Is-sessjoni skadiet, erġa' idħol.",
    "err.session_expired_nl": "Is-sessjoni skadiet.\nErġa' idħol.",
    "err.signin_needed": "Il-login ta' claude.ai skada.\nErġa' idħol: klikk bil-lemin → Idħol f'claude.ai",
    "err.unexpected": "Żball mhux mistenni: {}",

    # --- 'Message to the developer' window -----------------------------------------------------
    "fb.cancel": "Ikkanċella",
    "fb.close": "Agħlaq",
    "fb.consent": "Qrajt u naċċetta l-{}.",
    "fb.email": "Email",
    "fb.email_hint": "biss jekk tixtieq tweġiba",
    "fb.err_consent": "Biex tibgħat, jekk jogħġbok aċċetta l-Politika tal-Privatezza.",
    "fb.err_email": "Dan l-indirizz tal-email ma jidhirx korrett.",
    "fb.err_empty": "L-ewwel ikteb messaġġ jew agħżel valutazzjoni.",
    "fb.err_links": "Hemm wisq links fil-messaġġ.",
    "fb.err_network": "Ma setax jintlaħaq claudeusagemonitor.com. Iċċekkja l-konnessjoni tiegħek u erġa' pprova.",
    "fb.err_rate": "Wisq messaġġi fi ftit ħin – jekk jogħġbok erġa' pprova aktar tard.",
    "fb.err_server": "Is-server ma setax jilqa' l-messaġġ bħalissa. Jekk jogħġbok erġa' pprova aktar tard.",
    "fb.intro": "Għandek idea, sibt bug, jew sempliċement jogħġbok? Għidli. Kull messaġġ naqrah jien, Vidovics Gábor, l-awtur.",
    "fb.message": "Messaġġ",
    "fb.message_ph": "X'jaħdem, x'ma jaħdimx, x'inhu nieqes?",
    "fb.meta": "Flimkien mal-messaġġ jintbagħtu: il-verżjoni tal-programm {0}, is-sistema operattiva ({1}), il-lingwa tal-interfaċċja ({2}).",
    "fb.name": "Isem",
    "fb.optional": "(mhux obbligatorju)",
    "fb.privacy_hide": "Aħbi l-Politika",
    "fb.privacy_text": (
        "Kontrollur: Vidovics Gábor, persuna privata (l-Ungerija), l-awtur ta' Claude Usage Monitor. "
        "Il-Politika tal-Privatezza sħiħa tinsab fuq is-sit web: https://claudeusagemonitor.com/#privacy\n\n"
        "X'jintbagħat: dak li tikteb hawn – isem (mhux obbligatorju), indirizz tal-email (mhux obbligatorju), "
        "messaġġ, valutazzjoni bl-istilel – u, biex nifhem il-kuntest: il-verżjoni tal-programm, l-isem u "
        "l-verżjoni tas-sistema operattiva, il-lingwa tal-interfaċċja u l-ħin tal-bgħit. Is-server ma jaħżen "
        "l-ebda indirizz IP; biex jipprevjeni l-abbuż, juża biss hash li jinbidel kuljum u li ma jistax "
        "jerġa' jinqaleb f'indirizz.\n\n"
        "Għaliex: biex naqra u nwieġeb il-messaġġ tiegħek u biex intejjeb il-programm (interess leġittimu, "
        "Artikolu 6(1)(f) tal-GDPR; it-tweġiba nfisha ssir fuq talba tiegħek). Il-valutazzjoni u l-isem "
        "tiegħek jidhru fuq is-sit web biss jekk timmarka l-kaxxa separata għal dan (kunsens, "
        "Artikolu 6(1)(a)), u biss wara li l-awtur ikun eżaminahom; tista' tirtira dak il-kunsens fi "
        "kwalunkwe ħin.\n\n"
        "Għal kemm żmien: il-messaġġi jinżammu għal mhux aktar minn sentejn; valutazzjoni ppubblikata "
        "tinżamm sakemm tirtira l-kunsens tiegħek. Jekk l-awtur ikun attiva l-forwarding tal-emails, kopja "
        "tasal ukoll fil-kaxxa tal-email tal-awtur.\n\n"
        "Min jarah: il-kontrollur biss, u – bħala proċessur – il-fornitur tal-hosting (server fl-UE, "
        "fil-Ġermanja). Xejn ma jinbiegħ jew jingħadda lil ħaddieħor; m'hemm l-ebda tfassil ta' profili u "
        "l-ebda teħid ta' deċiżjonijiet awtomatizzat.\n\n"
        "Id-drittijiet tiegħek: aċċess, rettifika, tħassir, restrizzjoni, oġġezzjoni, irtirar tal-kunsens, "
        "u lment quddiem awtorità superviżorja (fl-Ungerija: NAIH, naih.hu) jew quddiem l-awtorità "
        "tal-pajjiż tiegħek. Kuntatt: din il-formola jew is-sit web.\n\n"
        "Trażmissjoni: kriptata (HTTPS/TLS) lejn claudeusagemonitor.com. Verżjoni ta' din il-Politika: "
        "2026-10-06."
    ),
    "fb.privacy_title": "Politika tal-Privatezza",
    "fb.publish": "Il-valutazzjoni tiegħi u ismi (jekk ingħata) jistgħu jintwerew fuq claudeusagemonitor.com.",
    "fb.rating": "Valutazzjoni ġenerali",
    "fb.rating_clear": "ħassar",
    "fb.rating_hint": "mhux obbligatorju – ikklikkja fuq stilla",
    "fb.rating_tip": "{} minn 5",
    "fb.secure": "Konnessjoni kriptata (HTTPS) lejn claudeusagemonitor.com.",
    "fb.send": "Ibgħat",
    "fb.sending": "Qed jintbagħat…",
    "fb.sent": "Grazzi – wasal!",
    "fb.sent_sub": "Naqra kull messaġġ. Jekk ħallejt indirizz tal-email, inwieġbek hemmhekk.",
    "fb.title": "Messaġġ lill-iżviluppatur",

    # --- Help window ---------------------------------------------------------------------------
    "help.disclaimer": "Għodda indipendenti u b'xejn – mhix magħmula minn Anthropic u m'għandha l-ebda rabta magħha. “Claude” hija marka kummerċjali ta' Anthropic.",
    "help.feedback": "Mistoqsijiet, ideat, rapporti ta' bugs: il-formola tal-messaġġi fuq is-sit web.",
    "help.free": "B'xejn għal dejjem · liċenzja MIT · sors miftuħ · l-ebda telemetrija",
    "help.guide": (
        "\n<h2>X'juri l-widget</h2>\n<ul>\n"
        "<li><b>Sessjoni ta' 5 sigħat</b> – kemm intuża mil-limitu tas-sessjoni attwali. Jerġa' jibda kull "
        "ħames sigħat; il-widget jagħmel għadd lura sar-reset.</li>\n"
        "<li><b>Limitu tal-ġimgħa</b> – l-użu tal-mudelli kollha flimkien; jerġa' jibda f'ħin fiss kull "
        "ġimgħa, skont il-kont tiegħek.</li>\n"
        "<li><b>Limitu tal-ġimgħa għal kull mudell</b> – it-tielet indikatur, meta s-server jirrapporta "
        "wieħed (eż. għal mudell speċifiku).</li>\n"
        "<li><b>Ritmu u rata ta' konsum</b> – kemm qed tuża l-limitu malajr u jekk hux se jkun biżżejjed sar-reset; "
        "il-projezzjoni sa tmiem il-ġimgħa twissik fil-ħin.</li>\n"
        "<li><b>Krediti tal-użu</b> u l-badge tal-pjan tiegħek – meta tixgħelhom taħt "
        "<i>Badge tal-pjan u limiti oħra</i>.</li>\n</ul>\n"
        "<h2>Minn fejn tiġi d-data</h2>\n<ul>\n"
        "<li><b>claude.ai (l-apparati kollha)</b> – jistaqsi lis-server ta' Anthropic, għalhekk jinkludi "
        "l-użu fuq il-mowbajl, fil-browser u fuq kompjuters oħra. Jeħtieġ login darba biss fil-browser "
        "tiegħek stess (menu: <i>Idħol</i>). Jaġġorna kull 2 minuti, aktar bil-mod jekk is-server jitlob "
        "hekk.</li>\n"
        "<li><b>Lokali (dan il-PC biss)</b> – jaqra l-log tal-użu ta' Claude Desktop fuq dan il-kompjuter. "
        "Mingħajr login, iżda jaf biss b'dan il-PC.</li>\n</ul>\n"
        "<p>Aqleb bejniethom mill-menu: <i>Sors tad-data</i>.</p>\n"
        "<h2>Kif tużah</h2>\n<ul>\n"
        "<li><b>Klikk bil-lemin</b> fuq il-widget (jew fuq l-ikona fiż-żona tan-notifiki) – il-menu "
        "sħiħ.</li>\n"
        "<li><b>Klikk doppju</b> fuq indikatur – it-tieqa <b>Storja</b>: 6 sigħat, 24 siegħa, 7 ijiem jew "
        "kollox, bil-quċċati, il-medja ta' kuljum u projezzjoni.</li>\n"
        "<li><b>Kaxkru</b> biex iċċaqilqu; jeħel mat-truf tal-iskrin. <b>Ctrl + rota tal-maws</b> – akbar "
        "jew iżgħar.</li>\n"
        "<li>Tqassim: kard post-it, strixxa rqiqa, ċrieki; 6 temi. <i>Sakkar il-pożizzjoni</i> u "
        "<i>Klikks jgħaddu minnu</i> jinsabu fl-Issettjar.</li>\n</ul>\n"
        "<h2>Allerti</h2>\n"
        "<p>Isfar minn 70 %, aħmar minn 90 % (tista' tibdilhom). Notifiki mhux obbligatorji meta limitu "
        "jerġa' jibda u meta d-data tkun qed tqadem.</p>\n"
        "<h2>Backups (mhux obbligatorju)</h2>\n"
        "<p>Id-dwal iż-żgħar juru jekk il-backups skedati tiegħek ħadmux u spiċċawx. Ikklikkja fuq dawl "
        "għad-dettalji. Il-monitor jaqra biss il-logs tal-backups – li tagħmel u tittestja l-backups hija "
        "r-responsabbiltà tiegħek (ara t-Termini tal-użu).</p>\n"
        "<h2>Aġġornamenti</h2>\n"
        "<p>Il-programm ifittex verżjonijiet ġodda waħdu u jaġġorna ruħu bi klikk wieħed. Kull pakkett "
        "jiġi ċċekkjat bis-SHA-256 u jiġi biss minn <b>claudeusagemonitor.com</b>. Verżjonijiet ġodda u "
        "x'hemm ġdid: {site}</p>\n"
        "<h2>Privatezza</h2>\n"
        "<p>L-ebda telemetrija, l-ebda traċċar. Il-login ta' claude.ai jinħażen kriptat fuq dan il-kompjuter "
        "biss; xejn ma jintbagħat x'imkien ieħor.</p>\n"
        "<h2>Jekk xi ħaġa ma tkunx sew</h2>\n<ul>\n"
        "<li><i>429 / limitazzjoni tar-rata</i> – is-server qed inaqqas ir-ritmu tat-talbiet; il-programm "
        "jerġa' jipprova waħdu.</li>\n"
        "<li>L-ebda data – iċċekkja s-<i>Sors tad-data</i>; bi claude.ai, erġa' idħol.</li>\n"
        "<li>L-istorja tinżamm għal 7 ijiem u tibqa' anki wara restart u aġġornamenti.</li>\n"
        "<li>Il-logs u l-issettjar: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Magħmul minn",
    "help.moved": "Indirizz ġdid mill-21 ta' Settembru 2026 – il-paġna ta' qabel dinorr.hu/claude-usage-monitor tidderieġik hawn.",
    "help.official": "SIT WEB UFFIĊJALI",
    "help.open_site": "Iftaħ claudeusagemonitor.com",
    "help.privacy": "Politika tal-Privatezza",
    "help.site_what": "Tniżżil, aġġornamenti awtomatiċi, x'hemm ġdid, il-Claude Backup Kit, it-termini tal-użu u l-privatezza – kollox f'post wieħed.",
    "help.source_code": "Kodiċi tas-sors (GitHub)",
    "help.tab_author": "Awtur",
    "help.tab_guide": "Kif jaħdem",
    "help.terms": "Termini tal-użu",
    "help.title": "Għajnuna",
    "help.version": "Verżjoni",

    # --- History window ------------------------------------------------------------------------
    "hist.legend_5h": "sessjoni ta' 5 sigħat",
    "hist.legend_week": "limitu tal-ġimgħa",
    "hist.no_data": "M'hemmx biżżejjed data għal dan il-perjodu.",
    "hist.range_24h": "24 siegħa",
    "hist.range_6h": "6 sigħat",
    "hist.range_7d": "7 ijiem",
    "hist.range_all": "Kollox",
    "hist.stat_burn": "Konsum medju kuljum",
    "hist.stat_forecast": "Projezzjoni sa tmiem il-ġimgħa",
    "hist.stat_now": "Użu tal-ġimgħa issa",
    "hist.stat_peak": "Quċċata tal-ġimgħa",
    "hist.stat_sessions": "Sessjonijiet ta' 5 sigħat",
    "hist.title": "storja",

    # --- layouts -------------------------------------------------------------------------------
    "layout.compact": "Strixxa rqiqa",
    "layout.postit": "Kard post-it",
    "layout.ring": "Ċrieki",

    # --- context menu --------------------------------------------------------------------------
    "menu.always_top": "Dejjem fuq quddiem",
    "menu.autostart": "Ibda ma' Windows",
    "menu.backup_bar": "Strixxa tal-istat tal-backups",
    "menu.backups": "Backups…",
    "menu.check_update": "Fittex aġġornamenti tal-programm…",
    "menu.click_through": "Klikks jgħaddu minnu",
    "menu.details": "Badge tal-pjan u limiti oħra",
    "menu.feedback": "Messaġġ lill-iżviluppatur…",
    "menu.help": "Għajnuna…",
    "menu.history": "Storja u statistika…",
    "menu.language": "Lingwa",
    "menu.layout": "Tqassim",
    "menu.locked": "Sakkar il-pożizzjoni",
    "menu.login": "Idħol (claude.ai, browser)…",
    "menu.logout": "Oħroġ",
    "menu.model_gauge": "Indikatur {}",
    "menu.order": "Ordni",
    "menu.panel_visible": "Uri l-pannell",
    "menu.quit": "Agħlaq il-programm",
    "menu.refresh": "Aġġorna d-data tal-użu issa",
    "menu.settings": "Issettjar…",
    "menu.size": "Daqs",
    "menu.source": "Sors tad-data",
    "menu.start_menu": "Uri fil-menu Start",
    "menu.theme": "Tema",
    "menu.update_available": "Aġġornament tal-programm: installa l-verżjoni {}…",

    # --- desktop notifications -----------------------------------------------------------------
    "notify.autostart_fail": "Il-bidu awtomatiku ma setax jiġi ssettjat.",
    "notify.autostart_off": "Mitfi: l-app mhix se tibda ma' Windows.",
    "notify.autostart_on": "Mixgħul: l-app tibda ma' Windows.",
    "notify.first_run": "Il-pannell deher fir-rokna ta' fuq tal-lemin.\nKlikk bil-lemin fuq il-pannell jew fuq l-ikona fiż-żona tan-notifiki = menu.",
    "notify.login_ok": "Dħalt – id-data mis-server qed tasal.",
    "notify.logout": "Ħriġt. Il-pannell qaleb għas-sors lokali.",
    "notify.reset_done": "{}: reset — beda perjodu ġdid.",
    "notify.signin_needed": "Il-login ta' claude.ai skada. Ikklikkja bil-lemin fuq il-pannell u erġa' idħol biex tkompli tara l-użu mill-apparati kollha tiegħek.",
    "notify.stale_body": "L-aħħar qari kien {} ilu. Claude Desktop għaddej?",
    "notify.stale_title": "Data qadima",
    "notify.threshold": "{}: intuża {}%.",
    "notify.update": "Il-verżjoni {} tal-programm hija disponibbli. Klikk bil-lemin fuq il-pannell → Aġġornament tal-programm.",

    # --- floating panel ------------------------------------------------------------------------
    "panel.five_hour": "SESSJONI TA' 5H",
    "panel.five_hour_short": "5H",
    "panel.full_in": "mimli: {}",
    "panel.model": "{} ĠIMGĦA",
    "panel.no_data": "Ebda data",
    "panel.pace": "{} vs ritmu",
    "panel.per_day": "{}%/jum",
    "panel.per_hour": "{}%/h",
    "panel.refreshing": "qed jaġġorna",
    "panel.reset": "reset {}",
    "panel.retry_in": "jerġa' f'{} s",
    "panel.updated": "aġġornat: {}",
    "panel.week_short": "ĠIMGĦA",
    "panel.weekly": "LIMITU TAL-ĠIMGĦA",

    # --- profile -------------------------------------------------------------------------------
    "profile.extra": "Krediti tal-użu: {}",
    "profile.plan": "Pjan: {}",
    "profile.since": "Membru minn: {}",
    "profile.tier": "Kategorija tal-limitu tar-rata: {}",

    # --- Settings window -----------------------------------------------------------------------
    "set.about": "{}\nL-ebda telemetrija. Jistaqsi lil Anthropic biss għall-użu tiegħek u jaqra n-numru tal-verżjoni mis-server tal-aġġornamenti.",
    "set.accent": "Kulur tal-aċċent",
    "set.always_top": "Fuq it-twieqi l-oħra kollha",
    "set.auto": "awtomatiku",
    "set.backup_config": "Konfigurazzjoni tal-iskript tal-backup",
    "set.backup_details": "It-tieqa tad-dettalji turi",
    "set.backup_disclaimer": "Claude Usage Monitor jaqra u juri biss il-logs tal-backup tiegħek – ma jagħmel, ma jiċċekkja u ma jiggarantixxi l-ebda backup. Il-Claude Backup Kit huwa punt tat-tluq b'xejn, offrut bħala għajnuna: kulħadd jista' jibdel l-iskripts, għalhekk il-kwalità u l-kompletezza ta' backup ma jistgħux jiġu garantiti. Ma naċċettaw l-ebda responsabbiltà għall-backups, għal data mitlufa jew għal kwalunkwe dannu. Kull persuna hija responsabbli biex tiżgura li l-backups tagħha jkunu kompluti u jistgħu jiġu rrestawrati – minn żmien għal żmien ipprova rrestawra backup biex tittestjah.",
    "set.backup_disclaimer_h": "Ċaħda ta' responsabbiltà",
    "set.backup_enabled": "Uri l-istrixxa tal-istat tal-backups fuq il-pannell",
    "set.backup_found": "Instab: {}",
    "set.backup_green": "Aħdar sa",
    "set.backup_label": "Tikketta ħdejn id-dawl",
    "set.backup_lamps": "Dwal",
    "set.backup_root": "Folder tal-backups",
    "set.backup_tasks": "Filtru tal-kompiti skedati",
    "set.backup_unconfigured": "Ma ġie ssettjat l-ebda folder tal-backups, għalhekk l-istrixxa tal-istat tibqa' moħbija. Agħżel il-folder fejn jikteb l-iskript tal-backup tiegħek.",
    "set.backup_yellow": "Isfar sa",
    "set.browse": "Fittex…",
    "set.click_through": "Klikks jgħaddu minnu (dekorazzjoni biss, jinjora l-maws)",
    "set.close": "Agħlaq",
    "set.color_hint": "Il-kuluri jinbidlu skont il-livelli: aħdar → isfar → aħmar.",
    "set.danger": "Kritiku",
    "set.data_hint": "Log lokali: il-plan-usage-history.json ta' Claude Desktop. Mingħajr login, iżda jkejjel dan il-PC biss u jaġġorna bejn wieħed u ieħor kull 5 minuti.\n\nclaude.ai: wara l-login jistaqsi lis-server. Tara l-użu mill-apparati kollha tiegħek, bil-ħinijiet eżatti tar-reset u aġġornament aktar spiss.",
    "set.datafile": "Fajl tad-data",
    "set.default": "Prestabbilit",
    "set.details_api_only": "Dawn jiġu mis-sors tad-data claude.ai (jeħtieġ login); il-log lokali ma fihomx.",
    "set.file_filter": "JSON (*.json);;Il-fajls kollha (*.*)",
    "set.gauge_order": "Ordni tal-indikaturi",
    "set.hours_suffix": " h",
    "set.layout": "Tqassim",
    "set.local_models_hint": "Is-server iżomm kontatur separat għal xi mudelli biss (eż. Fable). Għall-oħrajn, dan juri kif jinqasam ix-xogħol ta' din il-ġimgħa ma' Claude Code fuq dan il-PC - sehem mill-użu tiegħek stess u t-tokens tal-output, mhux sehem minn limitu. Jinqraw biss l-isem tal-mudell u l-għadd ta' tokens, qatt il-konversazzjoni.",
    "set.local_models_none": "Ma nstab l-ebda folder tal-logs ta' Claude Code - dan il-grupp sempliċement jibqa' moħbi. Xejn ieħor ma jintlaqat.",
    "set.local_models_path": "Folder tal-logs ta' Claude Code",
    "set.lock": "Sakkar il-pożizzjoni (ma jistax jitkaxkar)",
    "set.login_btn_in": "Oħroġ minn claude.ai",
    "set.login_btn_out": "Idħol f'claude.ai…",
    "set.model_filter": "Mudell li jiġi segwit",
    "set.model_scale": "Daqs tal-indikatur tal-mudell",
    "set.not_set": "mhux issettjat",
    "set.notify_enabled": "Avża meta jinqabeż livell",
    "set.notify_reset": "Avża meta limitu jerġa' jibda",
    "set.notify_stale": "Avża meta d-data tqadem",
    "set.opacity": "Opaċità",
    "set.open_config": "Iftaħ il-folder tal-issettjar",
    "set.pick_color": "Agħżel kulur…",
    "set.pick_file_title": "Agħżel il-log tal-użu",
    "set.profile": "Profil / kont",
    "set.profile_auto": "Awtomatiku (l-aħħar wieħed użat)",
    "set.profile_n": "Profil {} – …{}",
    "set.refresh": "Aġġornament",
    "set.reset_confirm": "Żgur li trid tirrestawra l-issettjar prestabbilit?",
    "set.restore": "Irrestawra l-valuri prestabbiliti",
    "set.rows_available": "X'jista' jintwera issa – neħħi l-marka minn dak li ma tridx tara:",
    "set.rows_none": "Bħalissa s-server ma jibgħat l-ebda limitu ieħor għall-kont tiegħek. Jidhru hawn waħedhom hekk kif jibgħathom.",
    "set.sec_suffix": " s",
    "set.show_age": "Kemm hi aġġornata d-data",
    "set.show_burn": "Rata ta' konsum (%/siegħa, %/jum)",
    "set.show_extra_usage": "Krediti tal-użu (ħlas skont l-użu)",
    "set.show_feedback_icon": "Ikona tal-messaġġi fl-intestatura tal-pannell",
    "set.show_five_hour": "Uri s-sessjoni ta' 5 sigħat",
    "set.show_local_models": "Qsim bejn il-mudelli, mil-logs ta' Claude Code fuq dan il-PC",
    "set.show_model": "Uri l-limitu tal-ġimgħa tal-mudell (sors claude.ai)",
    "set.show_model_list": "Limiti tal-ġimgħa tal-mudelli l-oħra",
    "set.show_plan_badge": "Badge tal-pjan fl-intestatura (Pro / Max…)",
    "set.show_plan_name": "Uri ismi fuq il-badge",
    "set.show_reset": "Għadd lura sar-reset",
    "set.show_spark": "Kurva tax-xejra (sparkline)",
    "set.show_surfaces": "Limiti għal kull pjattaforma (Claude Code, apps konnessi…)",
    "set.show_weekly": "Uri l-limitu tal-ġimgħa",
    "set.size": "Daqs",
    "set.snap": "Jeħel mat-tarf tal-iskrin",
    "set.source_api": "claude.ai – l-apparati kollha (jeħtieġ login)",
    "set.source_label": "Sors tal-kejl",
    "set.source_local": "Log lokali – dan il-PC biss",
    "set.tab_alerts": "Allerti",
    "set.tab_appearance": "Dehra",
    "set.tab_content": "Kontenut",
    "set.tab_data": "Sors tad-data",
    "set.tab_details": "Dettalji",
    "set.tab_system": "Sistema",
    "set.taskbar": "Uri fit-taskbar (bħala tieqa)",
    "set.theme": "Tema",
    "set.theme_default": "Skont it-tema",
    "set.tip": "Ħjiel: kaxkar il-pannell bil-buttuna tax-xellug, Ctrl+rota tibdel id-daqs,\nklikk bil-lemin = menu, klikk doppju = storja.",
    "set.title": "issettjar",
    "set.tray_five": "Sessjoni ta' 5 sigħat",
    "set.tray_max": "Liema jkun l-ogħla",
    "set.tray_value": "Valur tal-ikona fiż-żona tan-notifiki",
    "set.tray_weekly": "Limitu tal-ġimgħa",
    "set.update_check": "Fittex aġġornamenti tal-programm awtomatikament",
    "set.version": "Verżjoni",
    "set.visible": "Il-pannell jidher fuq l-iskrin",
    "set.warn": "Twissija",

    # --- sizes, sources, themes ----------------------------------------------------------------
    "size.extra": "Ekstra",
    "size.large": "Kbir",
    "size.normal": "Normali",
    "size.small": "Żgħir",
    "source.api": "claude.ai (l-apparati kollha)",
    "source.local": "Lokali (dan il-PC biss)",
    "theme.claude": "Claude (skur sħun)",
    "theme.graphite": "Grafit",
    "theme.midnight": "Ħġieġ ta' nofsillejl",
    "theme.neon": "Neon",
    "theme.paper": "Karta ċara",
    "theme.postit": "Post-it isfar",

    # --- time units ----------------------------------------------------------------------------
    "time.day": "{} j",
    "time.dh": "{}j {}h",
    "time.hm": "{}h {}min",
    "time.hour": "{} h",
    "time.m": "{}min",
    "time.min": "{} min",
    "time.none": "ebda data",
    "time.sec": "{} s",

    # --- tray ----------------------------------------------------------------------------------
    "tray.head": "5h: {}%   ·   Ġimgħa: {}%",
    "tray.line": "{}: {}%",

    # --- program update ------------------------------------------------------------------------
    "update.available": "Il-verżjoni {} hija disponibbli.",
    "update.check_failed": "It-tfittxija għal aġġornamenti ma rnexxietx: {}",
    "update.check_now": "Iċċekkja issa",
    "update.checking": "Qed ifittex aġġornamenti…",
    "update.downloading": "Qed jitniżżel… {} minn {}",
    "update.failed": "L-aġġornament falla: {}",
    "update.install": "Installa issa",
    "update.installed": "Verżjoni installata: {}",
    "update.later": "Aktar tard",
    "update.manual": "Din il-kopja ma tistax taġġorna lilha nfisha (taħdem mis-sors jew minn folder li jinqara biss). Niżżel il-pakkett il-ġdid minflok.",
    "update.open_page": "Iftaħ il-paġna tat-tniżżil",
    "update.restarting": "Qed jinstalla – l-app terġa' tibda fi ftit mumenti.",
    "update.skip": "Aqbeż din il-verżjoni",
    "update.title": "Aġġornament tal-programm",
    "update.uptodate": "Għandek l-aħħar verżjoni.",
    "update.verifying": "Qed jivverifika u jestratta…",
    "update.whats_new": "X'hemm ġdid",
}

# macOS wording: "start at login" instead of "start with Windows", menu bar instead of tray
STRINGS_MAC = {
    "menu.autostart": "Iftaħ mal-login",
    "notify.autostart_on": "Mixgħul: l-app tibda meta tidħol.",
    "notify.autostart_off": "Mitfi: l-app mhix se tibda mal-login.",
    "notify.first_run": "Il-pannell deher fir-rokna ta' fuq tal-lemin.\nKlikk bil-lemin fuq il-pannell jew fuq l-ikona fil-menu bar = menu.",
}
