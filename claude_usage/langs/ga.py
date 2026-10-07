# -*- coding: utf-8 -*-
"""Gaeilge – UI strings of Claude Usage Monitor."""

CODE = "ga"
NAME = "Gaeilge"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{}l",
    "backup.age_h": "{}u",
    "backup.age_m": "{}nóim",
    "backup.and_more": "…agus {} eile",
    "backup.checked_at": "Seiceáilte: {}",
    "backup.checking": "Á sheiceáil…",
    "backup.cloud_only": "Níl an léargas ar fáil ach ar líne in OneDrive; ní liostaítear a ábhar, ionas nach gá é a íoslódáil.",
    "backup.comp.cowork": "Logchomhaid comhrá Cowork (ZIP in aghaidh an tseisiúin)",
    "backup.comp.vault": "Léargas ar thaisceadán Obsidian (ZIP)",
    "backup.disclaimer_short": "Ní thaispeánann an monatóir ach a bhfuil sna logchomhaid cúltaca. Ní ghlacaimid aon dliteanas as cúltacaí – is fútsa atá sé a sheiceáil go bhfuil siad iomlán agus gur féidir iad a athchóiriú.",
    "backup.done": "críochnaithe",
    "backup.dry_run": "(rith tástála, níor uaslódáladh aon rud)",
    "backup.failed": "TEIPTHE",
    "backup.files_size": "Comhaid: {} ({})",
    "backup.folders": "Fillteáin",
    "backup.label_age": "Ainm agus aois",
    "backup.label_name": "Ainm amháin",
    "backup.label_none": "Lampaí amháin",
    "backup.last_ok": "An cúltaca rathúil is déanaí: {} ({} ó shin)",
    "backup.last_run": "An rith is déanaí: {} – {}",
    "backup.legend": "Glas: {} u ar a mhéad · Buí: suas le {} u · Dearg: níos sine, nó gan chúltaca",
    "backup.level_green": "Úr",
    "backup.level_none": "Níor aimsíodh cúltaca",
    "backup.level_red": "As dáta",
    "backup.level_yellow": "Ag dul in aois",
    "backup.log_file": "Logchomhad",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Níor aimsíodh an fillteán cúltaca: {}",
    "backup.none_found": "Níl aon cheann.",
    "backup.open": "oscail",
    "backup.rc_copied": "cóipeáladh comhaid nua nó athraithe",
    "backup.rc_failed": "TEIPTHE (cód {})",
    "backup.rc_nochange": "cothrom le dáta, níl aon rud le cóipeáil",
    "backup.recent_notes": "Na nótaí is déanaí a cuireadh in eagar sa léargas",
    "backup.refresh": "Seiceáil anois",
    "backup.sec_components": "Cad atá sa chúltaca",
    "backup.sec_contents": "Ábhar",
    "backup.sec_log": "Logchomhad (na línte deiridh)",
    "backup.sec_problems": "Earráidí agus rabhaidh",
    "backup.sec_tasks": "Tascanna sceidealta",
    "backup.skipped": "scipeáilte (níor aimsíodh an fillteán)",
    "backup.snap_kept": "Léargais coinnithe: {}, {} san iomlán",
    "backup.snapshot": "An léargas is déanaí",
    "backup.source": "Foinse",
    "backup.state_error": "críochnaithe le hearráidí",
    "backup.state_interrupted": "níor chríochnaigh sé",
    "backup.state_ok": "críochnaithe go rathúil",
    "backup.state_running": "ag rith anois",
    "backup.storage": "Stóras cianda: {} in úsáid as {}, {} saor",
    "backup.target": "Ceann scríbe",
    "backup.task_event": "ar theagmhas",
    "backup.task_row": "rith deireanach {} · toradh {} · an chéad rith eile {}",
    "backup.tip_click": "Cliceáil le haghaidh mionsonraí",
    "backup.title": "Cúltacaí",
    "backup.tray": "Cúltacaí: {}",
    "backup.uploaded": "Uaslódáilte sa rith seo: {} nua, {} ionadaithe, earráidí: {}",
    "backup.uploaded_files": "Comhaid uaslódáilte",
    "backup.uploaded_groups": "Comhaid uaslódáilte de réir fillteáin",
    "backup.uploaded_no": "Uaslódáilte chuig Nextcloud: níl fós",
    "backup.uploaded_yes": "Uaslódáilte chuig Nextcloud: tá ({})",
    "backup.vault": "Taisceadán",
    "backup.vault_changed": "Nótaí athraithe sa taisceadán ón léargas seo i leith: {}",
    "backup.zip_new": "ZIP nua/nuashonraithe: {}",
    "backup.zip_summary": "Comhaid: {} (nótaí: {}), {} gan chomhbhrú",

    # --- general -----------------------------------------------------------------------------
    "detail.extra": "Creidmheasanna úsáide",
    "detail.local_header": "CLAUDE CODE · AN RÍOMHAIRE SEO · ROINNT NA SEACHTAINE SEO",
    "detail.off": "as",
    "detail.on": "air",
    "detail.surface.oauth_apps": "Aipeanna ceangailte",
    "detail.unlimited": "gan teorainn",
    "dlg.cancel": "Cealaigh",
    "dlg.checking": "Á sheiceáil…",
    "dlg.err_badcode": "Níor glacadh leis an gcód.\n\n{}\n\nDeimhnigh gur ghreamaigh tú an cód ar fad, nó bain triail eile as an síniú isteach sa bhrabhsálaí (cód úr gach uair).",
    "dlg.err_ratelimit": "An iomarca iarrachtaí síniú isteach in achar gearr.\n\nTá an freastalaí ag cur sriain ort go sealadach. Dún an fhuinneog seo, fan 10–15 nóiméad (ná bain triail as idir an dá linn), ansin tosaigh AON síniú isteach nua amháin sa bhrabhsálaí le cód úr.",
    "dlg.hint1": "Sínigh isteach ar an leathanach a osclóidh, agus ceadaigh rochtain. Gheobhaidh tú cód ag an deireadh.",
    "dlg.intro": "Sínigh isteach i do chuntas claude.ai i do bhrabhsálaí féin (oibríonn do phasfhocail agus d'eochracha rochtana sábháilte ansin cheana féin).",
    "dlg.login_title": "síniú isteach",
    "dlg.open_browser": "Oscail an síniú isteach i do bhrabhsálaí",
    "dlg.paste_label": "Greamaigh anseo an cód a fuair tú:",
    "dlg.paste_placeholder": "greamaigh an cód anseo",
    "dlg.signin": "Sínigh isteach",
    "dlg.step1": "Céim 1",
    "dlg.step2": "Céim 2",
    "dlg.unknown_err": "Earráid anaithnid.",

    # --- error messages ----------------------------------------------------------------------
    "err.already_running": "Tá an aip ag rith cheana féin (féach sa tráidire).",
    "err.bad_token_resp": "freagra neamhbhailí ó chríochphointe na gcomharthaí",
    "err.bad_usage_resp": "freagra neamhbhailí ó chríochphointe na húsáide",
    "err.connection": "earráid cheangail: {}",
    "err.file_empty": "Tá an comhad úsáide folamh.",
    "err.file_not_found": "Níor aimsíodh an comhad úsáide.\nAn bhfuil Claude Desktop ag rith?",
    "err.file_unreadable": "Ní féidir an comhad úsáide a léamh faoi láthair.",
    "err.loading": "Ag síniú isteach / ag fiosrú…",
    "err.network": "earráid líonra: {}",
    "err.no_code": "Níor greamaíodh aon chód.",
    "err.no_data_profile": "Níl aon sonraí don phróifíl seo.",
    "err.no_tray": "Níl tráidire an chórais ar fáil; ní thaispeánfar deilbhín an tráidire.",
    "err.no_usage_data": "Níl aon sonraí úsáide ann.",
    "err.not_signed_in": "Níl tú sínithe isteach.",
    "err.query_http": "Earráid iarratais (HTTP {}).",
    "err.rate_limited": "Tá an freastalaí ag cur teorann le hiarratais (429) – bainfear triail eile as go huathoibríoch.",
    "err.session_expired": "Tá an seisiún imithe in éag, sínigh isteach arís.",
    "err.session_expired_nl": "Tá an seisiún imithe in éag.\nSínigh isteach arís.",
    "err.signin_needed": "Tá an síniú isteach ar claude.ai imithe in éag.\nSínigh isteach arís: deaschliceáil → Sínigh isteach ar claude.ai",
    "err.unexpected": "Earráid gan choinne: {}",

    # --- 'Message to the developer' window ----------------------------------------------------
    "fb.cancel": "Cealaigh",
    "fb.close": "Dún",
    "fb.consent": "Léigh mé an {} agus glacaim leis.",
    "fb.email": "Ríomhphost",
    "fb.email_hint": "más mian leat freagra a fháil",
    "fb.err_consent": "Chun í a sheoladh, glac leis an bPolasaí Príobháideachais.",
    "fb.err_email": "Ní cosúil go bhfuil an seoladh ríomhphoist seo ceart.",
    "fb.err_empty": "Scríobh teachtaireacht nó roghnaigh rátáil ar dtús.",
    "fb.err_links": "An iomarca naisc sa teachtaireacht.",
    "fb.err_network": "Níorbh fhéidir claudeusagemonitor.com a bhaint amach. Seiceáil do cheangal agus bain triail eile as.",
    "fb.err_rate": "An iomarca teachtaireachtaí in achar gearr – bain triail eile as ar ball.",
    "fb.err_server": "Níorbh fhéidir leis an bhfreastalaí an teachtaireacht a ghlacadh faoi láthair. Bain triail eile as ar ball.",
    "fb.intro": "An bhfuil smaoineamh agat, ar aimsigh tú fabht, nó an maith leat an clár, sin an méid? Inis dom. Léim féin gach teachtaireacht – mise Vidovics Gábor, údar an chláir.",
    "fb.message": "Teachtaireacht",
    "fb.message_ph": "Cad a oibríonn, cad nach n-oibríonn, cad atá in easnamh?",
    "fb.meta": "Seoltar leis an teachtaireacht: leagan an chláir {0}, an córas oibriúcháin ({1}), teanga an chomhéadain ({2}).",
    "fb.name": "Ainm",
    "fb.optional": "(roghnach)",
    "fb.privacy_hide": "Folaigh an polasaí",
    "fb.privacy_text": (
        "Rialaitheoir: Vidovics Gábor, duine aonair príobháideach (an Ungáir), údar Claude Usage Monitor. "
        "Tá an Polasaí Príobháideachais iomlán ar an suíomh gréasáin: https://claudeusagemonitor.com/#privacy\n\n"
        "Cad a sheoltar: a gclóscríobhann tú anseo – ainm (roghnach), seoladh ríomhphoist (roghnach), teachtaireacht, "
        "rátáil réaltaí – agus, ionas go dtuigfidh mé an comhthéacs: leagan an chláir, ainm agus leagan an chórais "
        "oibriúcháin, teanga an chomhéadain agus am an tseolta. Ní stórálann an freastalaí aon seoladh IP; chun "
        "mí-úsáid a chosc, ní úsáideann sé ach hais a athraíonn gach lá agus nach féidir a iompú ar ais ina sheoladh.\n\n"
        "Cén fáth: chun do theachtaireacht a léamh agus a fhreagairt agus chun an clár a fheabhsú (leas dlisteanach, "
        "Airteagal 6(1)(f) RGCS; an freagra féin, ar d'iarratas). Ní thaispeántar do rátáil ná d'ainm ar an suíomh "
        "gréasáin ach amháin má chuireann tú tic sa bhosca ar leith chuige sin (toiliú, Airteagal 6(1)(a)), agus "
        "ach amháin tar éis don údar iad a athbhreithniú; is féidir leat an toiliú sin a tharraingt siar am ar bith.\n\n"
        "Cá fhad: teachtaireachtaí ar feadh 2 bhliain ar a mhéad; rátáil fhoilsithe go dtí go dtarraingeoidh tú do "
        "thoiliú siar. Má tá cur ar aghaidh ríomhphoist casta air ag an údar, rachaidh cóip chuig bosca poist an "
        "údair freisin.\n\n"
        "Cé a fheiceann iad: an rialaitheoir amháin, agus – mar phróiseálaí – an soláthraí óstála (freastalaí san AE, "
        "sa Ghearmáin). Ní dhíoltar aon rud agus ní thugtar aon rud ar aghaidh; níl aon phróifíliú ná cinnteoireacht "
        "uathoibrithe ann.\n\n"
        "Do chearta: rochtain, ceartú, léirscriosadh, srianadh, agóid, an toiliú a tharraingt siar, agus gearán a "
        "dhéanamh le húdarás maoirseachta (san Ungáir: NAIH, naih.hu) nó le húdarás do thíre féin. Teagmháil: an "
        "fhoirm seo nó an suíomh gréasáin.\n\n"
        "Iompar: criptithe (HTTPS/TLS) chuig claudeusagemonitor.com. Leagan an pholasaí seo: 2026-10-06."
    ),
    "fb.privacy_title": "Polasaí Príobháideachais",
    "fb.publish": "Féadfar mo rátáil agus m'ainm (má thug mé é) a thaispeáint ar claudeusagemonitor.com.",
    "fb.rating": "Rátáil fhoriomlán",
    "fb.rating_clear": "glan",
    "fb.rating_hint": "roghnach – cliceáil ar réalta",
    "fb.rating_tip": "{} as 5",
    "fb.secure": "Ceangal criptithe (HTTPS) chuig claudeusagemonitor.com.",
    "fb.send": "Seol",
    "fb.sending": "Á sheoladh…",
    "fb.sent": "Go raibh maith agat – tá sí faighte agam!",
    "fb.sent_sub": "Léim gach teachtaireacht. Má d'fhág tú seoladh ríomhphoist, freagróidh mé thú ar an seoladh sin.",
    "fb.title": "Teachtaireacht chuig an bhforbróir",

    # --- Help window -------------------------------------------------------------------------
    "help.disclaimer": "Uirlis neamhspleách saor in aisce – ní de chuid Anthropic í agus níl baint ar bith aici le Anthropic. Is trádmharc de chuid Anthropic é “Claude”.",
    "help.feedback": "Ceisteanna, smaointe, tuairiscí fabhtanna: an fhoirm teachtaireachta ar an suíomh gréasáin.",
    "help.free": "Saor in aisce go deo · ceadúnas MIT · foinse oscailte · gan teileiméadracht",
    "help.guide": (
        "\n<h2>Cad a thaispeánann an ghiuirléid</h2>\n"
        "<ul>\n"
        "<li><b>Seisiún 5 huaire</b> – an méid de theorainn do sheisiúin reatha atá úsáidte. Athshocraítear í gach cúig huaire; déanann an ghiuirléid comhaireamh síos go dtí an t-athshocrú.</li>\n"
        "<li><b>Teorainn seachtaine</b> – úsáid na samhlacha go léir le chéile; athshocraítear í ag am seasta gach seachtain, de réir do chuntais.</li>\n"
        "<li><b>Teorainn seachtaine na samhla</b> – tríú tomhsaire nuair a thuairiscíonn an freastalaí ceann (m.sh. do shamhail ar leith).</li>\n"
        "<li><b>Luas agus ráta caithimh</b> – cé chomh tapa is atá tú ag ídiú na teorann agus an mairfidh sí go dtí an t-athshocrú; tugann an réamhaisnéis go deireadh na seachtaine rabhadh duit in am.</li>\n"
        "<li><b>Creidmheasanna úsáide</b> agus suaitheantas do phlean – nuair a chasann tú air iad faoi <i>Suaitheantas an phlean agus teorainneacha breise</i>.</li>\n"
        "</ul>\n"
        "<h2>Cá as a dtagann na sonraí</h2>\n"
        "<ul>\n"
        "<li><b>claude.ai (gach gléas)</b> – cuireann sé ceist ar fhreastalaí Anthropic, mar sin áirítear an úsáid ar do ghuthán, sa bhrabhsálaí agus ar ríomhairí eile. Teastaíonn síniú isteach aon uaire i do bhrabhsálaí féin (roghchlár: <i>Sínigh isteach</i>). Athnuaitear na sonraí gach 2 nóiméad, nó níos moille má iarrann an freastalaí é.</li>\n"
        "<li><b>Áitiúil (an ríomhaire seo amháin)</b> – léann sé logchomhad úsáide Claude Desktop ar an ríomhaire seo. Níl síniú isteach de dhíth, ach ní heol dó ach an ríomhaire seo.</li>\n"
        "</ul>\n"
        "<p>Athraigh eatarthu sa roghchlár: <i>Foinse sonraí</i>.</p>\n"
        "<h2>An ghiuirléid a úsáid</h2>\n"
        "<ul>\n"
        "<li><b>Deaschliceáil</b> ar an ngiuirléid (nó ar dheilbhín an tráidire) – an roghchlár iomlán.</li>\n"
        "<li><b>Déchliceáil</b> ar thomhsaire – an fhuinneog <b>Stair</b>: 6 huaire, 24 huaire, 7 lá nó gach rud, le buaicphointí, meán laethúil agus réamhaisnéis.</li>\n"
        "<li><b>Tarraing</b> í chun í a bhogadh; greamaíonn sí d'imill an scáileáin. <b>Ctrl + roth na luiche</b> – níos mó nó níos lú.</li>\n"
        "<li>Leaganacha amach: cárta Post-it, barra caol, fáinní; 6 théama. Tá <i>Glasáil an suíomh</i> agus <i>Cliceáil tríd</i> sna Socruithe.</li>\n"
        "</ul>\n"
        "<h2>Foláirimh</h2>\n"
        "<p>Buí ó 70%, dearg ó 90% (is féidir iad a athrú). Fógraí roghnacha nuair a athshocraítear teorainn agus nuair atá na sonraí ag dul as dáta.</p>\n"
        "<h2>Cúltacaí (roghnach)</h2>\n"
        "<p>Taispeánann na lampaí beaga ar ritheadh do chúltacaí sceidealta agus ar chríochnaigh siad. Cliceáil ar lampa le haghaidh mionsonraí. Ní léann an monatóir ach na logchomhaid cúltaca – is ortsa atá sé na cúltacaí a dhéanamh agus a thástáil (féach na Téarmaí úsáide).</p>\n"
        "<h2>Nuashonruithe</h2>\n"
        "<p>Lorgaíonn an clár leaganacha nua as a stuaim féin agus nuashonraíonn sé le cliceáil amháin. Seiceáiltear gach pacáiste le SHA-256 agus ní thagann aon phacáiste ach ó <b>claudeusagemonitor.com</b>. Leaganacha nua agus nótaí eisiúna: {site}</p>\n"
        "<h2>Príobháideachas</h2>\n"
        "<p>Gan teileiméadracht, gan rianú. Stóráiltear an síniú isteach ar claude.ai i bhfoirm chriptithe ar an ríomhaire seo amháin; ní sheoltar aon rud áit ar bith eile.</p>\n"
        "<h2>Má tá rud éigin mícheart</h2>\n"
        "<ul>\n"
        "<li><i>429 / teorainn ráta</i> – tá an freastalaí ag moilliú na n-iarratas; baineann an clár triail eile as leis féin.</li>\n"
        "<li>Gan sonraí – seiceáil an socrú <i>Foinse sonraí</i>; le claude.ai, sínigh isteach arís.</li>\n"
        "<li>Coinnítear an stair ar feadh 7 lá, fiú tar éis atosuithe agus nuashonruithe.</li>\n"
        "<li>Logchomhaid agus socruithe: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Déanta ag",
    "help.moved": "Seoladh nua ón 21 Meán Fómhair 2026 i leith – atreoraíonn an seanleathanach dinorr.hu/claude-usage-monitor anseo.",
    "help.official": "SUÍOMH GRÉASÁIN OIFIGIÚIL",
    "help.open_site": "Oscail claudeusagemonitor.com",
    "help.privacy": "Polasaí Príobháideachais",
    "help.site_what": "Íoslódálacha, nuashonruithe uathoibríocha, cad atá nua, Claude Backup Kit, téarmaí úsáide agus príobháideachas – iad uile in aon áit amháin.",
    "help.source_code": "Cód foinseach (GitHub)",
    "help.tab_author": "Údar",
    "help.tab_guide": "Conas a oibríonn sé",
    "help.terms": "Téarmaí úsáide",
    "help.title": "Cabhair",
    "help.version": "Leagan",

    # --- History window ----------------------------------------------------------------------
    "hist.legend_5h": "seisiún 5 huaire",
    "hist.legend_week": "teorainn seachtaine",
    "hist.no_data": "Níl go leor sonraí ann don tréimhse seo.",
    "hist.range_24h": "24 huaire",
    "hist.range_6h": "6 huaire",
    "hist.range_7d": "7 lá",
    "hist.range_all": "Gach rud",
    "hist.stat_burn": "Meánchaitheamh laethúil",
    "hist.stat_forecast": "Réamhaisnéis go deireadh na seachtaine",
    "hist.stat_now": "Seachtain reatha",
    "hist.stat_peak": "Buaic na seachtaine",
    "hist.stat_sessions": "Seisiúin 5 huaire",
    "hist.title": "stair",

    # --- layouts -----------------------------------------------------------------------------
    "layout.compact": "Barra caol",
    "layout.postit": "Cárta Post-it",
    "layout.ring": "Fáinní",

    # --- context menu ------------------------------------------------------------------------
    "menu.always_top": "Ar barr i gcónaí",
    "menu.autostart": "Tosaigh le Windows",
    "menu.backup_bar": "Barra stádais na gcúltacaí",
    "menu.backups": "Cúltacaí…",
    "menu.check_update": "Lorg nuashonruithe ar an gclár…",
    "menu.click_through": "Cliceáil tríd",
    "menu.details": "Suaitheantas an phlean agus teorainneacha breise",
    "menu.feedback": "Teachtaireacht chuig an bhforbróir…",
    "menu.help": "Cabhair…",
    "menu.history": "Stair agus staitisticí…",
    "menu.language": "Teanga",
    "menu.layout": "Leagan amach",
    "menu.locked": "Glasáil an suíomh",
    "menu.login": "Sínigh isteach (claude.ai, brabhsálaí)…",
    "menu.logout": "Sínigh amach",
    "menu.model_gauge": "Tomhsaire {}",
    "menu.order": "Ord",
    "menu.panel_visible": "Taispeáin an painéal",
    "menu.quit": "Scoir",
    "menu.refresh": "Athnuaigh sonraí úsáide anois",
    "menu.settings": "Socruithe…",
    "menu.size": "Méid",
    "menu.source": "Foinse sonraí",
    "menu.start_menu": "Taispeáin sa roghchlár Tosaigh",
    "menu.theme": "Téama",
    "menu.update_available": "Nuashonrú an chláir: suiteáil leagan {}…",

    # --- desktop notifications ---------------------------------------------------------------
    "notify.autostart_fail": "Níorbh fhéidir an tosú uathoibríoch a shocrú.",
    "notify.autostart_off": "Díchumasaithe: ní thosóidh an aip le Windows.",
    "notify.autostart_on": "Cumasaithe: tosóidh an aip le Windows.",
    "notify.first_run": "Tá an painéal sa chúinne uachtarach ar dheis.\nDeaschliceáil ar an bpainéal nó ar dheilbhín an tráidire = roghchlár.",
    "notify.login_ok": "Sínithe isteach – tá sonraí an fhreastalaí ag teacht.",
    "notify.logout": "Sínithe amach. Aistríodh go dtí an fhoinse áitiúil.",
    "notify.reset_done": "{}: athshocraithe — tá tréimhse nua tosaithe.",
    "notify.signin_needed": "Tá an síniú isteach ar claude.ai imithe in éag. Deaschliceáil ar an bpainéal agus sínigh isteach arís chun úsáid do ghléasanna go léir a fheiceáil i gcónaí.",
    "notify.stale_body": "Tá an léamh is déanaí {} d'aois. An bhfuil Claude Desktop ag rith?",
    "notify.stale_title": "Sonraí as dáta",
    "notify.threshold": "{}: {}% úsáidte.",
    "notify.update": "Tá leagan {} den chlár ar fáil. Deaschliceáil ar an bpainéal → Nuashonrú an chláir.",

    # --- panel labels (tight space) ----------------------------------------------------------
    "panel.five_hour": "SEISIÚN 5 hUAIRE",
    "panel.five_hour_short": "5U",
    "panel.full_in": "lán: {}",
    "panel.model": "{} · SEACHTAIN",
    "panel.no_data": "Gan sonraí",
    "panel.pace": "{} vs luas",
    "panel.per_day": "{}%/lá",
    "panel.per_hour": "{}%/u",
    "panel.refreshing": "ag fáil sonraí",
    "panel.reset": "athshocrú {}",
    "panel.retry_in": "arís i gceann {} s",
    "panel.updated": "athnuaite: {}",
    "panel.week_short": "SEACHT.",
    "panel.weekly": "AN tSEACHTAIN",

    # --- profile -----------------------------------------------------------------------------
    "profile.extra": "Creidmheasanna úsáide: {}",
    "profile.plan": "Plean: {}",
    "profile.since": "Ball ó: {}",
    "profile.tier": "Leibhéal teorann ráta: {}",

    # --- Settings window ---------------------------------------------------------------------
    "set.about": "{}\nGan teileiméadracht. Ní iarrann sé ar Anthropic ach d'úsáid féin, agus léann sé uimhir an leagain ó fhreastalaí na nuashonruithe.",
    "set.accent": "Dath béime",
    "set.always_top": "Os cionn gach fuinneoige eile",
    "set.auto": "uathoibríoch",
    "set.backup_config": "Cumraíocht na scripte cúltaca",
    "set.backup_details": "Taispeánann fuinneog na mionsonraí",
    "set.backup_disclaimer": "Ní dhéanann Claude Usage Monitor ach logchomhaid do chúltaca a léamh agus a thaispeáint – ní dhéanann sé, ní sheiceálann sé agus ní ráthaíonn sé aon chúltaca. Is pointe tosaigh saor in aisce é Claude Backup Kit, a thairgtear mar chabhair: is féidir le duine ar bith na scripteanna a athrú, mar sin ní féidir cáilíocht ná iomláine cúltaca a ráthú. Ní ghlacaimid aon dliteanas as cúltacaí, as sonraí caillte ná as aon damáiste. Is ar gach duine féin atá an fhreagracht a chinntiú go bhfuil a chúltacaí féin iomlán agus gur féidir iad a athchóiriú – déan tástáil ar athchóiriú ó am go chéile.",
    "set.backup_disclaimer_h": "Séanadh",
    "set.backup_enabled": "Taispeáin barra stádais na gcúltacaí ar an bpainéal",
    "set.backup_found": "Aimsithe: {}",
    "set.backup_green": "Glas suas le",
    "set.backup_label": "Lipéad in aice leis an lampa",
    "set.backup_lamps": "Lampaí",
    "set.backup_root": "Fillteán cúltaca",
    "set.backup_tasks": "Scagaire tascanna sceidealta",
    "set.backup_unconfigured": "Níl aon fhillteán cúltaca socraithe, mar sin fanann an barra stádais i bhfolach. Roghnaigh an fillteán ina scríobhann do script cúltaca.",
    "set.backup_yellow": "Buí suas le",
    "set.browse": "Brabhsáil…",
    "set.click_through": "Cliceáil tríd (maisiúchán amháin, déanann sé neamhaird den luch)",
    "set.close": "Dún",
    "set.color_hint": "Athraíonn na dathanna de réir na dtairseach: glas → buí → dearg.",
    "set.danger": "Criticiúil",
    "set.data_hint": "Logchomhad áitiúil: plan-usage-history.json de chuid Claude Desktop. Níl síniú isteach de dhíth, ach ní thomhaiseann sé ach an ríomhaire seo agus athnuaitear é thart ar gach 5 nóiméad.\n\nclaude.ai: tar éis duit síniú isteach, cuireann sé ceist ar an bhfreastalaí. Feiceann tú úsáid do ghléasanna go léir, le hamanna cruinne athshocraithe agus athnuachan níos minice.",
    "set.datafile": "Comhad sonraí",
    "set.default": "Réamhshocrú",
    "set.details_api_only": "Tagann siad seo ón bhfoinse sonraí claude.ai (síniú isteach de dhíth); níl siad sa logchomhad áitiúil.",
    "set.file_filter": "JSON (*.json);;Gach comhad (*.*)",
    "set.gauge_order": "Ord na dtomhsairí",
    "set.hours_suffix": " u",
    "set.layout": "Leagan amach",
    "set.local_models_hint": "Ní choinníonn an freastalaí áiritheoir ar leith ach do shamhlacha áirithe (m.sh. Fable). Do na cinn eile, taispeánann sé seo conas atá obair Claude Code na seachtaine seo ar an ríomhaire seo roinnte - sciar de d'úsáid féin agus na comharthaí aschuir, ní sciar de theorainn. Ní léitear ach ainm na samhla agus líon na gcomharthaí - ní léitear an comhrá choíche.",
    "set.local_models_none": "Níor aimsíodh fillteán logchomhad Claude Code - fanann an grúpa seo i bhfolach, sin an méid. Ní dhéanann sé difear d'aon rud eile.",
    "set.local_models_path": "Fillteán logchomhad Claude Code",
    "set.lock": "Glasáil an suíomh (ní féidir é a tharraingt)",
    "set.login_btn_in": "Sínigh amach as claude.ai",
    "set.login_btn_out": "Sínigh isteach ar claude.ai…",
    "set.model_filter": "Samhail le rianú",
    "set.model_scale": "Méid tomhsaire na samhla",
    "set.not_set": "gan socrú",
    "set.notify_enabled": "Fógra nuair a shároítear tairseach",
    "set.notify_reset": "Fógra nuair a athshocraítear teorainn",
    "set.notify_stale": "Fógra nuair a théann na sonraí as dáta",
    "set.opacity": "Teimhneacht",
    "set.open_config": "Oscail fillteán na socruithe",
    "set.pick_color": "Roghnaigh dath…",
    "set.pick_file_title": "Roghnaigh logchomhad úsáide",
    "set.profile": "Próifíl / cuntas",
    "set.profile_auto": "Uathoibríoch (an ceann is déanaí a úsáideadh)",
    "set.profile_n": "Próifíl {} – …{}",
    "set.refresh": "Athnuachan",
    "set.reset_confirm": "An bhfuil tú cinnte gur mian leat na réamhshocruithe a athchóiriú?",
    "set.restore": "Athchóirigh na réamhshocruithe",
    "set.rows_available": "Cad is féidir a thaispeáint anois – bain an tic de na rudaí nach dteastaíonn uait a fheiceáil:",
    "set.rows_none": "Ní sheolann an freastalaí aon teorainneacha eile do do chuntas faoi láthair. Taispeánfar anseo iad leo féin a luaithe a sheolann sé iad.",
    "set.sec_suffix": " s",
    "set.show_age": "Úire na sonraí",
    "set.show_burn": "Ráta caithimh (%/uair, %/lá)",
    "set.show_extra_usage": "Creidmheasanna úsáide (íoc de réir úsáide)",
    "set.show_feedback_icon": "Deilbhín teachtaireachta i gceanntásc an phainéil",
    "set.show_five_hour": "Taispeáin an seisiún 5 huaire",
    "set.show_local_models": "Roinnt idir na samhlacha, ó logchomhaid Claude Code ar an ríomhaire seo",
    "set.show_model": "Taispeáin teorainn seachtaine na samhla (foinse claude.ai)",
    "set.show_model_list": "Teorainneacha seachtaine na samhlacha eile",
    "set.show_plan_badge": "Suaitheantas an phlean sa cheanntásc (Pro / Max…)",
    "set.show_plan_name": "Taispeáin m'ainm ar an suaitheantas",
    "set.show_reset": "Comhaireamh síos go dtí an t-athshocrú",
    "set.show_spark": "Cuar treochta (sparkline)",
    "set.show_surfaces": "Teorainneacha de réir dromchla (Claude Code, aipeanna ceangailte…)",
    "set.show_weekly": "Taispeáin an teorainn seachtaine",
    "set.size": "Méid",
    "set.snap": "Greamaigh d'imeall an scáileáin",
    "set.source_api": "claude.ai – gach gléas (síniú isteach de dhíth)",
    "set.source_label": "Foinse tomhais",
    "set.source_local": "Logchomhad áitiúil – an ríomhaire seo amháin",
    "set.tab_alerts": "Foláirimh",
    "set.tab_appearance": "Cuma",
    "set.tab_content": "Ábhar",
    "set.tab_data": "Foinse sonraí",
    "set.tab_details": "Mionsonraí",
    "set.tab_system": "Córas",
    "set.taskbar": "Taispeáin ar an tascbharra (mar fhuinneog)",
    "set.theme": "Téama",
    "set.theme_default": "Réamhshocrú an téama",
    "set.tip": "Leid: tarraing an painéal leis an gcnaipe clé, athraíonn Ctrl+scrollú an méid,\ndeaschliceáil = roghchlár, déchliceáil = stair.",
    "set.title": "socruithe",
    "set.tray_five": "Seisiún 5 huaire",
    "set.tray_max": "Cibé ceann is airde",
    "set.tray_value": "Luach deilbhín an tráidire",
    "set.tray_weekly": "Teorainn seachtaine",
    "set.update_check": "Lorg nuashonruithe ar an gclár go huathoibríoch",
    "set.version": "Leagan",
    "set.visible": "Painéal ar snámh le feiceáil",
    "set.warn": "Rabhadh",

    # --- sizes, sources, themes --------------------------------------------------------------
    "size.extra": "Breise",
    "size.large": "Mór",
    "size.normal": "Gnáth",
    "size.small": "Beag",
    "source.api": "claude.ai (gach gléas)",
    "source.local": "Áitiúil (an ríomhaire seo amháin)",
    "theme.claude": "Claude (dorcha te)",
    "theme.graphite": "Graifít",
    "theme.midnight": "Gloine mheán oíche",
    "theme.neon": "Neon",
    "theme.paper": "Páipéar geal",
    "theme.postit": "Buí Post-it",

    # --- time units (panel) ------------------------------------------------------------------
    "time.day": "{} l",
    "time.dh": "{}l {}u",
    "time.hm": "{}u {}nóim",
    "time.hour": "{} u",
    "time.m": "{}nóim",
    "time.min": "{} nóim",
    "time.none": "gan sonraí",
    "time.sec": "{} s",

    # --- tray --------------------------------------------------------------------------------
    "tray.head": "5u: {}%   ·   Seacht.: {}%",
    "tray.line": "{}: {}%",

    # --- program update ----------------------------------------------------------------------
    "update.available": "Tá leagan {} ar fáil.",
    "update.check_failed": "Níorbh fhéidir nuashonruithe a lorg: {}",
    "update.check_now": "Lorg anois",
    "update.checking": "Ag lorg nuashonruithe…",
    "update.downloading": "Á íoslódáil… {} as {}",
    "update.failed": "Theip ar an nuashonrú: {}",
    "update.install": "Suiteáil anois",
    "update.installed": "Leagan suiteáilte: {}",
    "update.later": "Ar ball",
    "update.manual": "Ní féidir leis an gcóip seo í féin a nuashonrú (ritheann sí ón gcód foinseach nó ó fhillteán inléite amháin). Íoslódáil an pacáiste nua ina áit sin.",
    "update.open_page": "Oscail an leathanach íoslódála",
    "update.restarting": "Á shuiteáil – atosóidh an aip i gceann nóiméid.",
    "update.skip": "Scipeáil an leagan seo",
    "update.title": "Nuashonrú an chláir",
    "update.uptodate": "Tá an leagan is déanaí agat.",
    "update.verifying": "Á fhíorú agus á dhíphacáil…",
    "update.whats_new": "Cad atá nua",
}

# macOS wording (the four keys of source.json "mac"): "start at login" instead of "start with Windows", menu bar instead of tray
STRINGS_MAC = {
    "menu.autostart": "Oscail ar logáil isteach",
    "notify.autostart_on": "Cumasaithe: tosóidh an aip nuair a logálann tú isteach.",
    "notify.autostart_off": "Díchumasaithe: ní thosóidh an aip ar logáil isteach.",
    "notify.first_run": "Tá an painéal sa chúinne uachtarach ar dheis.\nDeaschliceáil ar an bpainéal nó ar dheilbhín an bharra roghchláir = roghchlár.",
}
