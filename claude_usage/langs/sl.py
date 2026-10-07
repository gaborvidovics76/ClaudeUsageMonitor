# -*- coding: utf-8 -*-
"""Slovenščina – UI strings of Claude Usage Monitor."""

CODE = "sl"
NAME = "Slovenščina"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{} d",
    "backup.age_h": "{} h",
    "backup.age_m": "{} min",
    "backup.and_more": "…in še {}",
    "backup.checked_at": "Preverjeno: {}",
    "backup.checking": "Preverjanje…",
    "backup.cloud_only": "Posnetek stanja je v storitvi OneDrive na voljo samo v spletu; vsebina ni izpisana, da ga ne bi bilo treba prenesti.",
    "backup.comp.cowork": "Dnevniki klepetov Cowork (ZIP za vsako sejo)",
    "backup.comp.vault": "Posnetek stanja trezorja Obsidian (ZIP)",
    "backup.disclaimer_short": "Monitor prikazuje samo to, kar piše v dnevnikih varnostnega kopiranja. Za varnostne kopije ne prevzemamo odgovornosti – ali so popolne in jih je mogoče obnoviti, morate preveriti sami.",
    "backup.done": "končano",
    "backup.dry_run": "(preizkusni zagon, nič ni bilo naloženo)",
    "backup.failed": "NI USPELO",
    "backup.files_size": "Št. datotek: {}, skupaj {}",
    "backup.folders": "Mape",
    "backup.label_age": "Ime in starost",
    "backup.label_name": "Samo ime",
    "backup.label_none": "Samo lučke",
    "backup.last_ok": "Zadnja uspešna varnostna kopija: {} (pred {})",
    "backup.last_run": "Zadnji zagon: {} – {}",
    "backup.legend": "Zelena: največ {} h · Rumena: do {} h · Rdeča: starejša ali brez varnostne kopije",
    "backup.level_green": "Sveže",
    "backup.level_none": "Ni varnostne kopije",
    "backup.level_red": "Zastarelo",
    "backup.level_yellow": "Zastareva",
    "backup.log_file": "Dnevniška datoteka",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Mape z varnostnimi kopijami ni mogoče najti: {}",
    "backup.none_found": "Ni jih.",
    "backup.open": "odpri",
    "backup.rc_copied": "nove ali spremenjene datoteke so kopirane",
    "backup.rc_failed": "NI USPELO (koda {})",
    "backup.rc_nochange": "brez sprememb, ničesar ni treba kopirati",
    "backup.recent_notes": "Nazadnje urejeni zapiski v posnetku stanja",
    "backup.refresh": "Preveri zdaj",
    "backup.sec_components": "Kaj se varnostno kopira",
    "backup.sec_contents": "Vsebina",
    "backup.sec_log": "Dnevnik (zadnje vrstice)",
    "backup.sec_problems": "Napake in opozorila",
    "backup.sec_tasks": "Načrtovana opravila",
    "backup.skipped": "preskočeno (mape ni mogoče najti)",
    "backup.snap_kept": "Shranjeni posnetki stanja: {}, skupaj {}",
    "backup.snapshot": "Najnovejši posnetek stanja",
    "backup.source": "Vir",
    "backup.state_error": "končano z napakami",
    "backup.state_interrupted": "ni bilo dokončano",
    "backup.state_ok": "uspešno dokončano",
    "backup.state_running": "trenutno se izvaja",
    "backup.storage": "Oddaljena shramba: porabljeno {} od {}, prosto {}",
    "backup.target": "Cilj",
    "backup.task_event": "ob dogodku",
    "backup.task_row": "zadnji zagon {} · rezultat {} · naslednji {}",
    "backup.tip_click": "Kliknite za podrobnosti",
    "backup.title": "Varnostne kopije",
    "backup.tray": "Varnostne kopije: {}",
    "backup.uploaded": "Naloženo v tem zagonu – nove: {}, zamenjane: {}, napake: {}",
    "backup.uploaded_files": "Naložene datoteke",
    "backup.uploaded_groups": "Naložene datoteke po mapah",
    "backup.uploaded_no": "Naloženo v Nextcloud: še ne",
    "backup.uploaded_yes": "Naloženo v Nextcloud: da ({})",
    "backup.vault": "Trezor",
    "backup.vault_changed": "Zapiski, spremenjeni v trezorju od tega posnetka stanja: {}",
    "backup.zip_new": "Nove ali posodobljene datoteke ZIP: {}",
    "backup.zip_summary": "Št. datotek: {} (od tega zapiskov: {}), nestisnjeno {}",

    # --- general ---------------------------------------------------------------------------
    "detail.extra": "Dobroimetje za porabo",
    "detail.local_header": "CLAUDE CODE · TA RAČUNALNIK · PORAZDELITEV TA TEDEN",
    "detail.off": "izklopljeno",
    "detail.on": "vklopljeno",
    "detail.surface.oauth_apps": "Povezane aplikacije",
    "detail.unlimited": "brez omejitve",
    "dlg.cancel": "Prekliči",
    "dlg.checking": "Preverjanje…",
    "dlg.err_badcode": "Koda ni bila sprejeta.\n\n{}\n\nPreverite, ali ste prilepili celotno kodo, ali pa se znova prijavite v brskalniku (vsakič z novo kodo).",
    "dlg.err_ratelimit": "Preveč poskusov prijave v kratkem času.\n\nStrežnik vas začasno omejuje. Zaprite to okno, počakajte 10–15 minut (vmes ne poskušajte), nato pa začnite ENO novo prijavo v brskalniku z novo kodo.",
    "dlg.hint1": "Na strani, ki se odpre, se prijavite in odobrite dostop. Na koncu boste prejeli kodo.",
    "dlg.intro": "Prijavite se v račun claude.ai v svojem brskalniku (tam že delujejo vaša shranjena gesla in ključi za dostop).",
    "dlg.login_title": "prijava",
    "dlg.open_browser": "Odpri prijavo v brskalniku",
    "dlg.paste_label": "Sem prilepite prejeto kodo:",
    "dlg.paste_placeholder": "sem prilepite kodo",
    "dlg.signin": "Prijava",
    "dlg.step1": "1. korak",
    "dlg.step2": "2. korak",
    "dlg.unknown_err": "Neznana napaka.",

    # --- error messages ----------------------------------------------------------------------
    "err.already_running": "Program se že izvaja (poglejte v območje za obvestila).",
    "err.bad_token_resp": "neveljaven odgovor končne točke za žetone",
    "err.bad_usage_resp": "neveljaven odgovor končne točke za porabo",
    "err.connection": "napaka povezave: {}",
    "err.file_empty": "Datoteka s podatki o porabi je prazna.",
    "err.file_not_found": "Datoteke s podatki o porabi ni mogoče najti.\nAli se Claude Desktop izvaja?",
    "err.file_unreadable": "Datoteke s podatki o porabi trenutno ni mogoče prebrati.",
    "err.loading": "Prijavljanje / poizvedovanje…",
    "err.network": "omrežna napaka: {}",
    "err.no_code": "Koda ni prilepljena.",
    "err.no_data_profile": "Za ta profil ni podatkov.",
    "err.no_tray": "Območje za obvestila ni na voljo, zato ikona ne bo prikazana.",
    "err.no_usage_data": "Ni podatkov o porabi.",
    "err.not_signed_in": "Niste prijavljeni.",
    "err.query_http": "Napaka poizvedbe (HTTP {}).",
    "err.rate_limited": "Strežnik omejuje število zahtev (429) – program bo samodejno poskusil znova.",
    "err.session_expired": "Seja je potekla, znova se prijavite.",
    "err.session_expired_nl": "Seja je potekla.\nZnova se prijavite.",
    "err.signin_needed": "Prijava v claude.ai je potekla.\nZnova se prijavite: desni klik → Prijava v claude.ai",
    "err.unexpected": "Nepričakovana napaka: {}",

    # --- 'Message to the developer' window -------------------------------------------------
    "fb.cancel": "Prekliči",
    "fb.close": "Zapri",
    "fb.consent": "Prebral/-a sem dokument {} in ga sprejemam.",
    "fb.email": "E-pošta",
    "fb.email_hint": "samo če želite odgovor",
    "fb.err_consent": "Če želite poslati sporočilo, sprejmite politiko zasebnosti.",
    "fb.err_email": "Ta e-poštni naslov ni videti pravilen.",
    "fb.err_empty": "Najprej napišite sporočilo ali izberite oceno.",
    "fb.err_links": "V sporočilu je preveč povezav.",
    "fb.err_network": "Spletnega mesta claudeusagemonitor.com ni mogoče doseči. Preverite povezavo in poskusite znova.",
    "fb.err_rate": "Preveč sporočil v kratkem času – poskusite znova pozneje.",
    "fb.err_server": "Strežnik trenutno ne more sprejeti sporočila. Poskusite znova pozneje.",
    "fb.intro": "Imate idejo, ste našli napako ali vam je program preprosto všeč? Povejte mi. Vsako sporočilo preberem sam – Vidovics Gábor, avtor programa.",
    "fb.message": "Sporočilo",
    "fb.message_ph": "Kaj deluje, kaj ne in kaj manjka?",
    "fb.meta": "S sporočilom se pošljejo tudi: različica programa {0}, operacijski sistem ({1}), jezik vmesnika ({2}).",
    "fb.name": "Ime",
    "fb.optional": "(neobvezno)",
    "fb.privacy_hide": "Skrij politiko zasebnosti",
    "fb.privacy_text": (
        "Upravljavec: Vidovics Gábor, fizična oseba (Madžarska), avtor programa Claude Usage Monitor. "
        "Celotna politika zasebnosti je objavljena na spletnem mestu: https://claudeusagemonitor.com/#privacy\n\n"
        "Kaj se pošlje: kar vnesete tukaj – ime (neobvezno), e-poštni naslov (neobvezno), sporočilo, ocena "
        "z zvezdicami – ter, da lahko razumem okoliščine: različica programa, ime in različica operacijskega "
        "sistema, jezik vmesnika in čas pošiljanja. Strežnik ne shranjuje naslovov IP; za preprečevanje zlorab "
        "uporablja samo zgoščeno vrednost, ki se spreminja vsak dan in je ni mogoče pretvoriti nazaj v naslov.\n\n"
        "Namen: da vaše sporočilo preberem in nanj odgovorim ter da izboljšam program (zakoniti interes, "
        "člen 6(1)(f) Splošne uredbe o varstvu podatkov (GDPR); odgovor sam pa na podlagi vaše zahteve). Vaša ocena in "
        "ime se na spletnem mestu prikažeta samo, če za to označite ločeno potrditveno polje (privolitev, člen 6(1)(a) "
        "GDPR), in šele potem, ko ju avtor pregleda; privolitev lahko kadar koli prekličete.\n\n"
        "Rok hrambe: sporočila največ 2 leti; objavljena ocena do preklica vaše privolitve. Če je avtor vklopil "
        "posredovanje po e-pošti, prispe kopija tudi v avtorjev poštni predal.\n\n"
        "Kdo ima dostop: samo upravljavec in – kot obdelovalec – ponudnik gostovanja (strežnik v EU, v Nemčiji). "
        "Podatki se ne prodajajo in ne posredujejo naprej; ni oblikovanja profilov in ni avtomatiziranega "
        "sprejemanja odločitev.\n\n"
        "Vaše pravice: dostop, popravek, izbris, omejitev obdelave, ugovor, preklic privolitve ter pritožba pri "
        "nadzornem organu (na Madžarskem: NAIH, naih.hu) ali pri organu v vaši državi (v Sloveniji: "
        "Informacijski pooblaščenec). Stik: ta obrazec ali spletno mesto.\n\n"
        "Prenos: šifrirano (HTTPS/TLS) do claudeusagemonitor.com. Različica tega obvestila: 6. 10. 2026."
    ),
    "fb.privacy_title": "Politika zasebnosti",
    "fb.publish": "Moja ocena in ime (če je navedeno) se lahko prikažeta na spletnem mestu claudeusagemonitor.com.",
    "fb.rating": "Skupna ocena",
    "fb.rating_clear": "počisti",
    "fb.rating_hint": "neobvezno – kliknite zvezdico",
    "fb.rating_tip": "{} od 5",
    "fb.secure": "Šifrirana povezava (HTTPS) do claudeusagemonitor.com.",
    "fb.send": "Pošlji",
    "fb.sending": "Pošiljanje…",
    "fb.sent": "Hvala – sporočilo je prispelo!",
    "fb.sent_sub": "Preberem vsako sporočilo. Če ste navedli e-poštni naslov, vam bom odgovoril tja.",
    "fb.title": "Sporočilo razvijalcu",

    # --- Help window ---------------------------------------------------------------------------
    "help.disclaimer": "Neodvisno, brezplačno orodje – ni izdelek družbe Anthropic in ni z njo povezano. „Claude“ je blagovna znamka družbe Anthropic.",
    "help.feedback": "Vprašanja, ideje, prijave napak: obrazec za sporočila na spletnem mestu.",
    "help.free": "Za vedno brezplačno · licenca MIT · odprta koda · brez telemetrije",
    "help.guide": (
        "\n<h2>Kaj prikazuje plošča</h2>\n<ul>\n"
        "<li><b>5-urna seja</b> – kolikšen del omejitve trenutne seje je porabljen. Ponastavi se vsakih pet ur; "
        "plošča odšteva čas do ponastavitve.</li>\n"
        "<li><b>Tedenska omejitev</b> – poraba vseh modelov skupaj; ponastavi se ob stalnem tedenskem terminu "
        "vašega računa.</li>\n"
        "<li><b>Tedenska omejitev modela</b> – tretji merilnik, kadar ga strežnik sporoči (npr. za določen model).</li>\n"
        "<li><b>Tempo in hitrost porabe</b> – kako hitro porabljate omejitev in ali bo zadoščala do ponastavitve; "
        "napoved za konec tedna vas pravočasno opozori.</li>\n"
        "<li><b>Dobroimetje za porabo</b> in značka paketa – ko ju vklopite v meniju "
        "<i>Značka paketa in dodatne omejitve</i>.</li>\n"
        "</ul>\n"
        "<h2>Od kod so podatki</h2>\n<ul>\n"
        "<li><b>claude.ai (vse naprave)</b> – podatke pridobi s strežnika družbe Anthropic, zato je upoštevana tudi "
        "poraba v telefonu, brskalniku in drugih računalnikih. Potrebna je enkratna prijava v vašem brskalniku "
        "(meni: <i>Prijava</i>). Osvežuje se vsaki 2 minuti, redkeje, če to zahteva strežnik.</li>\n"
        "<li><b>Lokalno (samo ta računalnik)</b> – bere dnevnik porabe aplikacije Claude Desktop v tem računalniku. "
        "Prijava ni potrebna, vendar pozna samo ta računalnik.</li>\n"
        "</ul>\n"
        "<p>Med njima preklopite v meniju: <i>Vir podatkov</i>.</p>\n"
        "<h2>Uporaba plošče</h2>\n<ul>\n"
        "<li><b>Desni klik</b> na ploščo (ali na ikono v območju za obvestila) – celoten meni.</li>\n"
        "<li><b>Dvoklik</b> na merilnik – okno <b>Zgodovina</b>: 6 ur, 24 ur, 7 dni ali vse, z vrhovi, dnevnim "
        "povprečjem in napovedjo.</li>\n"
        "<li><b>Povlecite</b> jo, da jo premaknete; pripne se na robove zaslona. <b>Ctrl + kolesce miške</b> – "
        "povečava ali pomanjšava.</li>\n"
        "<li>Postavitve: listek post-it, ozka vrstica, obroči; 6 tem. <i>Zakleni položaj</i> in "
        "<i>Prepuščanje klikov</i> najdete v nastavitvah.</li>\n"
        "</ul>\n"
        "<h2>Opozorila</h2>\n"
        "<p>Rumena od 70 %, rdeča od 90 % (nastavljivo). Po želji obvestila, ko se omejitev ponastavi in ko "
        "podatki zastarevajo.</p>\n"
        "<h2>Varnostne kopije (izbirno)</h2>\n"
        "<p>Majhne lučke kažejo, ali so se vaša načrtovana opravila varnostnega kopiranja zagnala in dokončala. Za "
        "podrobnosti kliknite lučko. Monitor samo bere dnevnike varnostnega kopiranja – izdelava in preizkušanje "
        "varnostnih kopij sta vaša naloga (glejte Pogoje uporabe).</p>\n"
        "<h2>Posodobitve</h2>\n"
        "<p>Program sam preverja, ali so na voljo nove različice, in se posodobi z enim klikom. Vsak paket je "
        "preverjen s SHA-256 in prihaja samo s spletnega mesta <b>claudeusagemonitor.com</b>. Nove različice in "
        "opombe ob izdaji: {site}</p>\n"
        "<h2>Zasebnost</h2>\n"
        "<p>Brez telemetrije, brez sledenja. Prijava v claude.ai je šifrirano shranjena samo v tem računalniku; "
        "nič se ne pošilja nikamor drugam.</p>\n"
        "<h2>Če kaj ne deluje</h2>\n<ul>\n"
        "<li><i>429 / omejitev zahtev</i> – strežnik upočasnjuje zahteve; program sam poskusi znova.</li>\n"
        "<li>Ni podatkov – preverite <i>Vir podatkov</i>; pri viru claude.ai se znova prijavite.</li>\n"
        "<li>Zgodovina se hrani 7 dni in ostane tudi po vnovičnem zagonu in posodobitvah.</li>\n"
        "<li>Dnevniki in nastavitve: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Avtor",
    "help.moved": "Nov naslov od 21. septembra 2026 – prejšnja stran dinorr.hu/claude-usage-monitor vas preusmeri sem.",
    "help.official": "URADNO SPLETNO MESTO",
    "help.open_site": "Odpri claudeusagemonitor.com",
    "help.privacy": "Politika zasebnosti",
    "help.site_what": "Prenosi, samodejne posodobitve, novosti, Claude Backup Kit, pogoji uporabe in zasebnost – vse na enem mestu.",
    "help.source_code": "Izvorna koda (GitHub)",
    "help.tab_author": "Avtor",
    "help.tab_guide": "Kako deluje",
    "help.terms": "Pogoji uporabe",
    "help.title": "Pomoč",
    "help.version": "Različica",

    # --- History window -------------------------------------------------------------------------
    "hist.legend_5h": "5-urna seja",
    "hist.legend_week": "tedenska omejitev",
    "hist.no_data": "Za to obdobje ni dovolj podatkov.",
    "hist.range_24h": "24 ur",
    "hist.range_6h": "6 ur",
    "hist.range_7d": "7 dni",
    "hist.range_all": "Vse",
    "hist.stat_burn": "Povpr. dnevna poraba",
    "hist.stat_forecast": "Napoved za konec tedna",
    "hist.stat_now": "Tedenska poraba zdaj",
    "hist.stat_peak": "Tedenski vrh",
    "hist.stat_sessions": "5-urne seje",
    "hist.title": "zgodovina",

    # --- layouts ---------------------------------------------------------------------------------
    "layout.compact": "Ozka vrstica",
    "layout.postit": "Listek post-it",
    "layout.ring": "Obroči",

    # --- context menu ---------------------------------------------------------------------------
    "menu.always_top": "Vedno na vrhu",
    "menu.autostart": "Zaženi s sistemom Windows",
    "menu.backup_bar": "Vrstica stanja varnostnih kopij",
    "menu.backups": "Varnostne kopije…",
    "menu.check_update": "Poišči posodobitve programa…",
    "menu.click_through": "Prepuščanje klikov",
    "menu.details": "Značka paketa in dodatne omejitve",
    "menu.feedback": "Sporočilo razvijalcu…",
    "menu.help": "Pomoč…",
    "menu.history": "Zgodovina in statistika…",
    "menu.language": "Jezik",
    "menu.layout": "Postavitev",
    "menu.locked": "Zakleni položaj",
    "menu.login": "Prijava (claude.ai, brskalnik)…",
    "menu.logout": "Odjava",
    "menu.model_gauge": "Merilnik {}",
    "menu.order": "Vrstni red",
    "menu.panel_visible": "Pokaži ploščo",
    "menu.quit": "Izhod",
    "menu.refresh": "Osveži podatke o porabi zdaj",
    "menu.settings": "Nastavitve…",
    "menu.size": "Velikost",
    "menu.source": "Vir podatkov",
    "menu.start_menu": "Pokaži v meniju Start",
    "menu.theme": "Tema",
    "menu.update_available": "Posodobitev programa: namesti različico {}…",

    # --- desktop notifications ------------------------------------------------------------------
    "notify.autostart_fail": "Samodejnega zagona ni bilo mogoče nastaviti.",
    "notify.autostart_off": "Izklopljeno: program se ne bo zagnal s sistemom Windows.",
    "notify.autostart_on": "Vklopljeno: program se zažene s sistemom Windows.",
    "notify.first_run": "Plošča se je prikazala v zgornjem desnem kotu.\nDesni klik na ploščo ali ikono v območju za obvestila = meni.",
    "notify.login_ok": "Prijava je uspela – podatki s strežnika so na poti.",
    "notify.logout": "Odjavljeni ste. Preklopljeno na lokalni vir.",
    "notify.reset_done": "{}: ponastavljeno – začelo se je novo obdobje.",
    "notify.signin_needed": "Prijava v claude.ai je potekla. Z desno tipko miške kliknite ploščo in se znova prijavite, da boste še naprej videli porabo v vseh svojih napravah.",
    "notify.stale_body": "Zadnja meritev je stara {}. Ali se Claude Desktop izvaja?",
    "notify.stale_title": "Zastareli podatki",
    "notify.threshold": "{}: porabljeno {} %.",
    "notify.update": "Na voljo je različica programa {}. Desni klik na ploščo → Posodobitev programa.",

    # --- floating panel labels (tight space, UPPERCASE) -------------------------------------
    "panel.five_hour": "5-URNA SEJA",
    "panel.five_hour_short": "5 H",
    "panel.full_in": "polno: {}",
    "panel.model": "{} TEDEN",
    "panel.no_data": "Ni podatkov",
    "panel.pace": "tempo {}",
    "panel.per_day": "{}%/dan",
    "panel.per_hour": "{}%/h",
    "panel.refreshing": "osveževanje",
    "panel.reset": "ponast. {}",
    "panel.retry_in": "znova čez {} s",
    "panel.updated": "osveženo: {}",
    "panel.week_short": "TEDEN",
    "panel.weekly": "TEDENSKA OMEJITEV",

    # --- profile ----------------------------------------------------------------------------------
    "profile.extra": "Dobroimetje za porabo: {}",
    "profile.plan": "Paket: {}",
    "profile.since": "Član od: {}",
    "profile.tier": "Raven omejitve hitrosti: {}",

    # --- Settings window ----------------------------------------------------------------------
    "set.about": "{}\nBrez telemetrije. Program pri družbi Anthropic poizveduje le o vaši porabi in s strežnika za posodobitve prebere številko različice.",
    "set.accent": "Poudarna barva",
    "set.always_top": "Nad vsemi drugimi okni",
    "set.auto": "samodejno",
    "set.backup_config": "Konfiguracija skripta za varnostno kopiranje",
    "set.backup_details": "Okno s podrobnostmi prikazuje",
    "set.backup_disclaimer": "Claude Usage Monitor samo bere in prikazuje dnevnike vašega varnostnega kopiranja – ne izdeluje, ne preverja in ne jamči za nobeno varnostno kopijo. Claude Backup Kit je brezplačno izhodišče, ponujeno kot pomoč: skripte lahko spremeni kdor koli, zato kakovosti in popolnosti varnostne kopije ni mogoče zagotoviti. Za varnostne kopije, izgubljene podatke ali kakršno koli škodo ne prevzemamo nobene odgovornosti. Za to, da so varnostne kopije popolne in jih je mogoče obnoviti, je odgovoren vsak sam – občasno preizkusite obnovitev.",
    "set.backup_disclaimer_h": "Omejitev odgovornosti",
    "set.backup_enabled": "Na plošči pokaži vrstico stanja varnostnih kopij",
    "set.backup_found": "Najdeno: {}",
    "set.backup_green": "Zelena do",
    "set.backup_label": "Napis ob lučki",
    "set.backup_lamps": "Lučke",
    "set.backup_root": "Mapa z varnostnimi kopijami",
    "set.backup_tasks": "Filter načrtovanih opravil",
    "set.backup_unconfigured": "Mapa z varnostnimi kopijami ni nastavljena, zato vrstica stanja ostane skrita. Izberite mapo, v katero piše vaš skript za varnostno kopiranje.",
    "set.backup_yellow": "Rumena do",
    "set.browse": "Prebrskaj…",
    "set.click_through": "Prepuščanje klikov (samo okras, miška se prezre)",
    "set.close": "Zapri",
    "set.color_hint": "Barve se spreminjajo glede na prage: zelena → rumena → rdeča.",
    "set.danger": "Kritično",
    "set.data_hint": "Lokalni dnevnik: datoteka plan-usage-history.json aplikacije Claude Desktop. Prijava ni potrebna, vendar upošteva samo ta računalnik in se osvežuje približno vsakih 5 minut.\n\nclaude.ai: po prijavi pridobiva podatke s strežnika. Vidite porabo v vseh svojih napravah, z natančnimi časi ponastavitve in pogostejšim osveževanjem.",
    "set.datafile": "Podatkovna datoteka",
    "set.default": "Privzeto",
    "set.details_api_only": "Ti podatki prihajajo iz vira claude.ai (potrebna je prijava); lokalni dnevnik jih ne vsebuje.",
    "set.file_filter": "JSON (*.json);;Vse datoteke (*.*)",
    "set.gauge_order": "Vrstni red merilnikov",
    "set.hours_suffix": " h",
    "set.layout": "Postavitev",
    "set.local_models_hint": "Strežnik vodi ločen števec samo za nekatere modele (npr. Fable). Za druge je tu prikazano, kako se ta teden porazdeli vaše delo s Claude Code v tem računalniku – delež vaše lastne porabe in izhodnih žetonov, ne delež omejitve. Prebereta se samo ime modela in število žetonov, pogovor nikoli.",
    "set.local_models_none": "Mape z dnevniki Claude Code ni bilo mogoče najti – ta skupina preprosto ostane skrita. Na nič drugega to ne vpliva.",
    "set.local_models_path": "Mapa z dnevniki Claude Code",
    "set.lock": "Zakleni položaj (ni mogoče vleči)",
    "set.login_btn_in": "Odjava iz claude.ai",
    "set.login_btn_out": "Prijava v claude.ai…",
    "set.model_filter": "Spremljani model",
    "set.model_scale": "Velikost merilnika modela",
    "set.not_set": "ni nastavljeno",
    "set.notify_enabled": "Obvesti ob prekoračitvi praga",
    "set.notify_reset": "Obvesti, ko se omejitev ponastavi",
    "set.notify_stale": "Obvesti, ko podatki zastarijo",
    "set.opacity": "Neprosojnost",
    "set.open_config": "Odpri mapo z nastavitvami",
    "set.pick_color": "Izberi barvo…",
    "set.pick_file_title": "Izberite dnevnik porabe",
    "set.profile": "Profil / račun",
    "set.profile_auto": "Samodejno (nazadnje uporabljen)",
    "set.profile_n": "Profil {} – …{}",
    "set.refresh": "Osveževanje",
    "set.reset_confirm": "Ali res želite obnoviti privzete nastavitve?",
    "set.restore": "Obnovi privzete nastavitve",
    "set.rows_available": "Kaj je mogoče prikazati zdaj – odstranite kljukico pri tistem, česar ne želite videti:",
    "set.rows_none": "Strežnik trenutno ne pošilja dodatnih omejitev za vaš račun. Ko jih bo začel pošiljati, se bodo tukaj prikazale samodejno.",
    "set.sec_suffix": " s",
    "set.show_age": "Svežost podatkov",
    "set.show_burn": "Hitrost porabe (%/h, %/dan)",
    "set.show_extra_usage": "Dobroimetje za porabo (plačilo po porabi)",
    "set.show_feedback_icon": "Ikona za sporočila v glavi plošče",
    "set.show_five_hour": "Pokaži 5-urno sejo",
    "set.show_local_models": "Porazdelitev med modeli iz dnevnikov Claude Code v tem računalniku",
    "set.show_model": "Pokaži tedensko omejitev modela (vir claude.ai)",
    "set.show_model_list": "Tedenske omejitve drugih modelov",
    "set.show_plan_badge": "Značka paketa v glavi (Pro / Max…)",
    "set.show_plan_name": "Na znački pokaži moje ime",
    "set.show_reset": "Odštevanje do ponastavitve",
    "set.show_spark": "Krivulja trenda (mini graf)",
    "set.show_surfaces": "Omejitve po storitvah (Claude Code, povezane aplikacije…)",
    "set.show_weekly": "Pokaži tedensko omejitev",
    "set.size": "Velikost",
    "set.snap": "Pripni na rob zaslona",
    "set.source_api": "claude.ai – vse naprave (potrebna je prijava)",
    "set.source_label": "Vir meritev",
    "set.source_local": "Lokalni dnevnik – samo ta računalnik",
    "set.tab_alerts": "Opozorila",
    "set.tab_appearance": "Videz",
    "set.tab_content": "Vsebina",
    "set.tab_data": "Vir podatkov",
    "set.tab_details": "Podrobnosti",
    "set.tab_system": "Sistem",
    "set.taskbar": "Pokaži v opravilni vrstici (kot okno)",
    "set.theme": "Tema",
    "set.theme_default": "Privzeto za temo",
    "set.tip": "Namig: ploščo vlecite z levo tipko, Ctrl+kolesce spremeni velikost,\ndesni klik = meni, dvoklik = zgodovina.",
    "set.title": "nastavitve",
    "set.tray_five": "5-urna seja",
    "set.tray_max": "Višja od obeh",
    "set.tray_value": "Vrednost ikone v območju za obvestila",
    "set.tray_weekly": "Tedenska omejitev",
    "set.update_check": "Samodejno preverjaj posodobitve programa",
    "set.version": "Različica",
    "set.visible": "Pokaži lebdečo ploščo",
    "set.warn": "Opozorilo",

    # --- menu options ---------------------------------------------------------------------------
    "size.extra": "Zelo velika",
    "size.large": "Velika",
    "size.normal": "Običajna",
    "size.small": "Majhna",
    "source.api": "claude.ai (vse naprave)",
    "source.local": "Lokalno (samo ta računalnik)",
    "theme.claude": "Claude (topla temna)",
    "theme.graphite": "Grafit",
    "theme.midnight": "Polnočno steklo",
    "theme.neon": "Neon",
    "theme.paper": "Svetel papir",
    "theme.postit": "Rumeni post-it",

    # --- time units -----------------------------------------------------------------------------
    "time.day": "{} d",
    "time.dh": "{} d {} h",
    "time.hm": "{} h {} min",
    "time.hour": "{} h",
    "time.m": "{} min",
    "time.min": "{} min",
    "time.none": "ni podatkov",
    "time.sec": "{} s",

    # --- tray -------------------------------------------------------------------------------------
    "tray.head": "5 h: {} %   ·   Teden: {} %",
    "tray.line": "{}: {} %",

    # --- program update ---------------------------------------------------------------------------
    "update.available": "Na voljo je različica {}.",
    "update.check_failed": "Posodobitev ni bilo mogoče preveriti: {}",
    "update.check_now": "Preveri zdaj",
    "update.checking": "Iskanje posodobitev…",
    "update.downloading": "Prenašanje… {} od {}",
    "update.failed": "Posodobitev ni uspela: {}",
    "update.install": "Namesti zdaj",
    "update.installed": "Nameščena različica: {}",
    "update.later": "Pozneje",
    "update.manual": "Ta kopija se ne more posodobiti sama (zagnana je iz izvorne kode ali iz mape, ki je samo za branje). Namesto tega prenesite novi paket.",
    "update.open_page": "Odpri stran za prenos",
    "update.restarting": "Nameščanje – aplikacija se bo takoj znova zagnala.",
    "update.skip": "Preskoči to različico",
    "update.title": "Posodobitev programa",
    "update.uptodate": "Imate najnovejšo različico.",
    "update.verifying": "Preverjanje in razpakiranje…",
    "update.whats_new": "Novosti",
}

# macOS wording: "Odpri ob prijavi" (Apple) instead of "start with Windows", menijska vrstica instead of the tray
STRINGS_MAC = {
    "menu.autostart": "Odpri ob prijavi",
    "notify.autostart_on": "Vklopljeno: program se zažene ob prijavi.",
    "notify.autostart_off": "Izklopljeno: program se ne bo zagnal ob prijavi.",
    "notify.first_run": "Plošča se je prikazala v zgornjem desnem kotu.\nDesni klik na ploščo ali ikono v menijski vrstici = meni.",
}
