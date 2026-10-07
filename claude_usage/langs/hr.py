# -*- coding: utf-8 -*-
"""Hrvatski – UI strings of Claude Usage Monitor."""

CODE = "hr"
NAME = "Hrvatski"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{}d",
    "backup.age_h": "{}h",
    "backup.age_m": "{}min",
    "backup.and_more": "…i još {}",
    "backup.checked_at": "Provjereno: {}",
    "backup.checking": "Provjera…",
    "backup.cloud_only": "Snimka je u OneDriveu dostupna samo na mreži; njezin se sadržaj ne prikazuje kako se ne bi morala preuzimati.",
    "backup.comp.cowork": "Zapisnici razgovora iz Coworka (ZIP za svaku sesiju)",
    "backup.comp.vault": "Snimka trezora programa Obsidian (ZIP)",
    "backup.disclaimer_short": "Monitor prikazuje samo ono što piše u zapisnicima sigurnosnih kopija. Za sigurnosne kopije ne preuzimamo odgovornost – na vama je da provjerite jesu li potpune i mogu li se vratiti.",
    "backup.done": "gotovo",
    "backup.dry_run": "(probno pokretanje, ništa nije preneseno)",
    "backup.failed": "NEUSPJELO",
    "backup.files_size": "datoteka: {}, veličina {}",
    "backup.folders": "Mape",
    "backup.label_age": "Naziv i starost",
    "backup.label_name": "Samo naziv",
    "backup.label_none": "Samo lampice",
    "backup.last_ok": "Posljednja uspješna sigurnosna kopija: {} (prije {})",
    "backup.last_run": "Posljednje pokretanje: {} – {}",
    "backup.legend": "Zelena: ne starija od {} h · Žuta: do {} h · Crvena: starija ili nema kopije",
    "backup.level_green": "Svježa",
    "backup.level_none": "Sigurnosna kopija nije pronađena",
    "backup.level_red": "Zastarjela",
    "backup.level_yellow": "Postaje zastarjela",
    "backup.log_file": "Datoteka zapisnika",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Mapa sigurnosnih kopija nije pronađena: {}",
    "backup.none_found": "Nema.",
    "backup.open": "otvori",
    "backup.rc_copied": "kopirane su nove ili promijenjene datoteke",
    "backup.rc_failed": "NEUSPJELO (kôd {})",
    "backup.rc_nochange": "ažurno, nema se što kopirati",
    "backup.recent_notes": "Nedavno uređene bilješke u snimci",
    "backup.refresh": "Provjeri sada",
    "backup.sec_components": "Što se sigurnosno kopira",
    "backup.sec_contents": "Sadržaj",
    "backup.sec_log": "Zapisnik (posljednji retci)",
    "backup.sec_problems": "Pogreške i upozorenja",
    "backup.sec_tasks": "Zakazani zadaci",
    "backup.skipped": "preskočeno (mapa nije pronađena)",
    "backup.snap_kept": "Sačuvanih snimaka: {}, ukupno {}",
    "backup.snapshot": "Najnovija snimka",
    "backup.source": "Izvor",
    "backup.state_error": "završeno s pogreškama",
    "backup.state_interrupted": "nije dovršeno",
    "backup.state_ok": "uspješno dovršeno",
    "backup.state_running": "upravo se izvodi",
    "backup.storage": "Udaljena pohrana: iskorišteno {} od {}, slobodno {}",
    "backup.target": "Odredište",
    "backup.task_event": "pri događaju",
    "backup.task_row": "posljednje pokretanje {} · rezultat {} · sljedeće {}",
    "backup.tip_click": "Kliknite za pojedinosti",
    "backup.title": "Sigurnosne kopije",
    "backup.tray": "Sigurnosne kopije: {}",
    "backup.uploaded": "Preneseno u ovom pokretanju – novih: {}, zamijenjenih: {}, pogrešaka: {}",
    "backup.uploaded_files": "Prenesene datoteke",
    "backup.uploaded_groups": "Prenesene datoteke po mapama",
    "backup.uploaded_no": "Preneseno na Nextcloud: još ne",
    "backup.uploaded_yes": "Preneseno na Nextcloud: da ({})",
    "backup.vault": "Trezor",
    "backup.vault_changed": "Bilješki promijenjenih u trezoru od ove snimke: {}",
    "backup.zip_new": "Novih/ažuriranih ZIP-ova: {}",
    "backup.zip_summary": "datoteka: {} (bilješki: {}), nekomprimirano {}",

    # --- general -----------------------------------------------------------------------------
    "detail.extra": "Krediti za potrošnju",
    "detail.local_header": "CLAUDE CODE · OVO RAČUNALO · RASPODJELA OVOG TJEDNA",
    "detail.off": "isključeno",
    "detail.on": "uključeno",
    "detail.surface.oauth_apps": "Povezane aplikacije",
    "detail.unlimited": "bez ograničenja",
    "dlg.cancel": "Odustani",
    "dlg.checking": "Provjera…",
    "dlg.err_badcode": "Kôd nije prihvaćen.\n\n{}\n\nProvjerite jeste li zalijepili cijeli kôd ili se ponovno prijavite u pregledniku (svaki put je potreban novi kôd).",
    "dlg.err_ratelimit": "Previše pokušaja prijave u kratkom vremenu.\n\nPoslužitelj vam je privremeno ograničio pristup.Zatvorite ovaj prozor, pričekajte 10–15 minuta (u međuvremenu ne pokušavajte), a zatim pokrenite JEDNU novu prijavu u pregledniku s novim kôdom.",
    "dlg.hint1": "Prijavite se na stranici koja se otvori i odobrite pristup. Na kraju ćete dobiti kôd.",
    "dlg.intro": "Prijavite se na svoj račun claude.ai u vlastitom pregledniku (u njemu su vam već dostupne spremljene lozinke i pristupni ključevi).",
    "dlg.login_title": "prijava",
    "dlg.open_browser": "Otvori prijavu u pregledniku",
    "dlg.paste_label": "Ovdje zalijepite primljeni kôd:",
    "dlg.paste_placeholder": "zalijepite kôd ovdje",
    "dlg.signin": "Prijava",
    "dlg.step1": "1. korak",
    "dlg.step2": "2. korak",
    "dlg.unknown_err": "Nepoznata pogreška.",

    # --- error messages ----------------------------------------------------------------------
    "err.already_running": "Program je već pokrenut (pogledajte u području obavijesti).",
    "err.bad_token_resp": "nevažeći odgovor krajnje točke za tokene",
    "err.bad_usage_resp": "nevažeći odgovor krajnje točke za potrošnju",
    "err.connection": "pogreška veze: {}",
    "err.file_empty": "Datoteka potrošnje je prazna.",
    "err.file_not_found": "Datoteka potrošnje nije pronađena.\nJe li Claude Desktop pokrenut?",
    "err.file_unreadable": "Datoteku potrošnje trenutačno nije moguće pročitati.",
    "err.loading": "Prijava / dohvaćanje…",
    "err.network": "mrežna pogreška: {}",
    "err.no_code": "Kôd nije zalijepljen.",
    "err.no_data_profile": "Nema podataka za ovaj profil.",
    "err.no_tray": "Područje obavijesti nije dostupno; ikona se neće prikazati.",
    "err.no_usage_data": "Nema podataka o potrošnji.",
    "err.not_signed_in": "Niste prijavljeni.",
    "err.query_http": "Pogreška pri dohvaćanju (HTTP {}).",
    "err.rate_limited": "Poslužitelj ograničava broj zahtjeva (429) – automatski se pokušava ponovno.",
    "err.session_expired": "Sesija je istekla, ponovno se prijavite.",
    "err.session_expired_nl": "Sesija je istekla.\nPonovno se prijavite.",
    "err.signin_needed": "Prijava na claude.ai je istekla.\nPonovno se prijavite: desni klik → Prijava na claude.ai",
    "err.unexpected": "Neočekivana pogreška: {}",

    # --- 'Message to the developer' window ---------------------------------------------------
    "fb.cancel": "Odustani",
    "fb.close": "Zatvori",
    "fb.consent": "Pročitao/la sam i prihvaćam {}.",
    "fb.email": "E-pošta",
    "fb.email_hint": "samo ako želite odgovor",
    "fb.err_consent": "Za slanje prihvatite Pravila privatnosti.",
    "fb.err_email": "Ova adresa e-pošte ne izgleda ispravno.",
    "fb.err_empty": "Najprije napišite poruku ili odaberite ocjenu.",
    "fb.err_links": "U poruci je previše poveznica.",
    "fb.err_network": "Nije moguće pristupiti stranici claudeusagemonitor.com. Provjerite vezu i pokušajte ponovno.",
    "fb.err_rate": "Previše poruka u kratkom vremenu – pokušajte ponovno kasnije.",
    "fb.err_server": "Poslužitelj trenutačno ne može primiti poruku. Pokušajte ponovno kasnije.",
    "fb.intro": "Imate ideju, pronašli ste pogrešku ili vam se program jednostavno sviđa? Javite mi. Svaku poruku čitam osobno – Vidovics Gábor, autor programa.",
    "fb.message": "Poruka",
    "fb.message_ph": "Što radi, što ne radi, što nedostaje?",
    "fb.meta": "Uz poruku se šalju: verzija programa {0}, operacijski sustav ({1}) i jezik sučelja ({2}).",
    "fb.name": "Ime",
    "fb.optional": "(neobavezno)",
    "fb.privacy_hide": "Sakrij pravila privatnosti",
    "fb.privacy_text": (
        "Voditelj obrade: Vidovics Gábor, fizička osoba (Mađarska), autor programa Claude Usage Monitor. "
        "Potpuna pravila privatnosti dostupna su na web-stranici: https://claudeusagemonitor.com/#privacy\n\n"
        "Što se šalje: ono što ovdje upišete – ime (neobavezno), adresa e-pošte (neobavezno), poruka, ocjena "
        "zvjezdicama – te, kako bih razumio kontekst: verzija programa, naziv i verzija operacijskog sustava, "
        "jezik sučelja i vrijeme slanja. Poslužitelj ne pohranjuje IP adresu; radi sprječavanja zlouporabe "
        "koristi samo sažetak (hash) koji se mijenja svaki dan i iz kojeg se adresa ne može ponovno dobiti.\n\n"
        "Zašto: kako bih pročitao vašu poruku i odgovorio na nju te poboljšao program (legitimni interes, "
        "čl. 6. st. 1. t. (f) Opće uredbe o zaštiti podataka (GDPR); sam odgovor šalje se na vaš zahtjev). "
        "Vaša ocjena i ime prikazuju se na web-stranici samo ako za to označite zasebnu kućicu (privola, "
        "čl. 6. st. 1. t. (a) GDPR-a), i to tek nakon što ih autor pregleda; tu privolu možete povući u bilo "
        "kojem trenutku.\n\n"
        "Koliko dugo: poruke najdulje 2 godine; objavljena ocjena dok ne povučete privolu. Ako je autor uključio "
        "prosljeđivanje e-pošte, kopija stiže i u autorov poštanski sandučić.\n\n"
        "Tko vidi podatke: samo voditelj obrade te – kao izvršitelj obrade – pružatelj usluge hostinga "
        "(poslužitelj u EU-u, u Njemačkoj). Ništa se ne prodaje niti prosljeđuje drugima; nema izrade profila "
        "ni automatiziranog donošenja odluka.\n\n"
        "Vaša prava: pristup, ispravak, brisanje, ograničenje obrade, prigovor, povlačenje privole te pritužba "
        "nadzornom tijelu (u Mađarskoj: NAIH, naih.hu) ili nadzornom tijelu vlastite države (u Hrvatskoj: "
        "AZOP, azop.hr). Kontakt: ovaj obrazac ili web-stranica.\n\n"
        "Prijenos: šifrirano (HTTPS/TLS) do claudeusagemonitor.com. Verzija ove obavijesti: 6. listopada 2026."
    ),
    "fb.privacy_title": "Pravila privatnosti",
    "fb.publish": "Pristajem da se moja ocjena i ime (ako je upisano) prikažu na claudeusagemonitor.com.",
    "fb.rating": "Ukupna ocjena",
    "fb.rating_clear": "poništi",
    "fb.rating_hint": "neobavezno – kliknite zvjezdicu",
    "fb.rating_tip": "{} od 5",
    "fb.secure": "Šifrirana veza (HTTPS) do claudeusagemonitor.com.",
    "fb.send": "Pošalji",
    "fb.sending": "Slanje…",
    "fb.sent": "Hvala – poruka je stigla!",
    "fb.sent_sub": "Čitam svaku poruku. Ako ste ostavili adresu e-pošte, odgovorit ću na nju.",
    "fb.title": "Poruka programeru",

    # --- Help window -------------------------------------------------------------------------
    "help.disclaimer": "Neovisan, besplatan alat – nije proizvod tvrtke Anthropic niti je s njom povezan.„Claude” je zaštitni znak tvrtke Anthropic.",
    "help.feedback": "Pitanja, ideje, prijave pogrešaka: obrazac za poruke na web-stranici.",
    "help.free": "Zauvijek besplatno · licenca MIT · otvoreni kôd · bez telemetrije",
    "help.guide": (
        "\n<h2>Što widget prikazuje</h2>\n<ul>\n"
        "<li><b>Sesija od 5 sati</b> – koliko je ograničenja trenutačne sesije iskorišteno. Resetira se svakih pet "
        "sati; widget odbrojava do reseta.</li>\n"
        "<li><b>Tjedno ograničenje</b> – potrošnja svih modela zajedno; resetira se u fiksno tjedno vrijeme "
        "vezano uz vaš račun.</li>\n"
        "<li><b>Tjedno ograničenje po modelu</b> – treći mjerač, kad ga poslužitelj javlja (npr. za određeni "
        "model).</li>\n"
        "<li><b>Tempo i brzina potrošnje</b> – koliko brzo trošite ograničenje i hoće li vam dostajati do reseta; "
        "projekcija do kraja tjedna upozorava na vrijeme.</li>\n"
        "<li><b>Krediti za potrošnju</b> i oznaka paketa – kad ih uključite u izborniku <i>Oznaka paketa i "
        "dodatna ograničenja</i>.</li>\n</ul>\n"
        "<h2>Odakle dolaze podaci</h2>\n<ul>\n"
        "<li><b>claude.ai (svi uređaji)</b> – podatke traži od poslužitelja tvrtke Anthropic, pa je uključena i "
        "potrošnja na mobitelu, u pregledniku i na drugim računalima. Potrebna je jednokratna prijava u vlastitom "
        "pregledniku (izbornik: <i>Prijava</i>). Osvježava se svake 2 minute, rjeđe ako to poslužitelj "
        "zatraži.</li>\n"
        "<li><b>Lokalno (samo ovo računalo)</b> – čita zapisnik potrošnje programa Claude Desktop na ovom "
        "računalu. Prijava nije potrebna, ali obuhvaća samo ovo računalo.</li>\n</ul>\n"
        "<p>Izvor mijenjate u izborniku: <i>Izvor podataka</i>.</p>\n"
        "<h2>Korištenje widgeta</h2>\n<ul>\n"
        "<li><b>Desni klik</b> na widget (ili na ikonu u području obavijesti) – cijeli izbornik.</li>\n"
        "<li><b>Dvoklik</b> na mjerač – prozor <b>Povijest</b>: 6 sati, 24 sata, 7 dana ili sve, s maksimumima, "
        "dnevnim prosjekom i projekcijom.</li>\n"
        "<li><b>Povucite</b> ga da biste ga premjestili; prianja uz rubove zaslona. <b>Ctrl + kotačić miša</b> – "
        "veći ili manji.</li>\n"
        "<li>Rasporedi: post-it kartica, uska traka, prstenovi; 6 tema. <i>Zaključaj položaj</i> i "
        "<i>Propuštanje klikova</i> nalaze se u Postavkama.</li>\n</ul>\n"
        "<h2>Upozorenja</h2>\n"
        "<p>Žuto od 70 %, crveno od 90 % (podesivo). Neobavezne obavijesti kad se ograničenje resetira i kad "
        "podaci zastare.</p>\n"
        "<h2>Sigurnosne kopije (neobavezno)</h2>\n"
        "<p>Male lampice pokazuju jesu li se zakazane sigurnosne kopije pokrenule i dovršile. Kliknite lampicu za "
        "pojedinosti. Monitor samo čita zapisnike sigurnosnih kopija – za izradu i testiranje kopija odgovorni ste vi "
        "(pogledajte Uvjete korištenja).</p>\n"
        "<h2>Ažuriranja</h2>\n"
        "<p>Program sam provjerava ima li novih verzija i ažurira se jednim klikom. Svaki se paket provjerava "
        "algoritmom SHA-256 i preuzima isključivo s <b>claudeusagemonitor.com</b>. Nove verzije i napomene o "
        "izdanju: {site}</p>\n"
        "<h2>Privatnost</h2>\n"
        "<p>Bez telemetrije, bez praćenja. Prijava na claude.ai pohranjuje se šifrirano samo na ovom računalu; "
        "ništa se ne šalje nikamo drugamo.</p>\n"
        "<h2>Ako nešto ne radi</h2>\n<ul>\n"
        "<li><i>429 / ograničenje zahtjeva</i> – poslužitelj usporava zahtjeve; program sam pokušava "
        "ponovno.</li>\n"
        "<li>Nema podataka – provjerite <i>Izvor podataka</i>; ako koristite claude.ai, ponovno se prijavite.</li>\n"
        "<li>Povijest se čuva 7 dana i ostaje sačuvana nakon ponovnog pokretanja i ažuriranja.</li>\n"
        "<li>Zapisnici i postavke: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Izradio",
    "help.moved": "Nova adresa od 21. rujna 2026. – dosadašnja stranica dinorr.hu/claude-usage-monitor preusmjerava ovamo.",
    "help.official": "SLUŽBENA WEB-STRANICA",
    "help.open_site": "Otvori claudeusagemonitor.com",
    "help.privacy": "Pravila privatnosti",
    "help.site_what": "Preuzimanja, automatska ažuriranja, novosti, Claude Backup Kit, uvjeti korištenja i privatnost – sve na jednom mjestu.",
    "help.source_code": "Izvorni kôd (GitHub)",
    "help.tab_author": "Autor",
    "help.tab_guide": "Kako radi",
    "help.terms": "Uvjeti korištenja",
    "help.title": "Pomoć",
    "help.version": "Verzija",

    # --- History window ----------------------------------------------------------------------
    "hist.legend_5h": "sesija od 5 sati",
    "hist.legend_week": "tjedno ograničenje",
    "hist.no_data": "Za ovo razdoblje nema dovoljno podataka.",
    "hist.range_24h": "24 sata",
    "hist.range_6h": "6 sati",
    "hist.range_7d": "7 dana",
    "hist.range_all": "Sve",
    "hist.stat_burn": "Prosječna dnevna potrošnja",
    "hist.stat_forecast": "Projekcija do kraja tjedna",
    "hist.stat_now": "Ovaj tjedan",
    "hist.stat_peak": "Tjedni maksimum",
    "hist.stat_sessions": "Sesije od 5 sati",
    "hist.title": "povijest",

    # --- menu options / context menu ---------------------------------------------------------
    "layout.compact": "Uska traka",
    "layout.postit": "Post-it kartica",
    "layout.ring": "Prstenovi",
    "menu.always_top": "Uvijek na vrhu",
    "menu.autostart": "Pokreni sa sustavom Windows",
    "menu.backup_bar": "Traka stanja sigurnosnih kopija",
    "menu.backups": "Sigurnosne kopije…",
    "menu.check_update": "Provjeri ažuriranja programa…",
    "menu.click_through": "Propuštanje klikova",
    "menu.details": "Oznaka paketa i dodatna ograničenja",
    "menu.feedback": "Poruka programeru…",
    "menu.help": "Pomoć…",
    "menu.history": "Povijest i statistika…",
    "menu.language": "Jezik",
    "menu.layout": "Raspored",
    "menu.locked": "Zaključaj položaj",
    "menu.login": "Prijava (claude.ai, preglednik)…",
    "menu.logout": "Odjava",
    "menu.model_gauge": "Mjerač {}",
    "menu.order": "Redoslijed",
    "menu.panel_visible": "Prikaži panel",
    "menu.quit": "Izlaz",
    "menu.refresh": "Osvježi podatke o potrošnji",
    "menu.settings": "Postavke…",
    "menu.size": "Veličina",
    "menu.source": "Izvor podataka",
    "menu.start_menu": "Prikaži u izborniku Start",
    "menu.theme": "Tema",
    "menu.update_available": "Ažuriranje programa: instaliraj verziju {}…",

    # --- desktop notifications ---------------------------------------------------------------
    "notify.autostart_fail": "Automatsko pokretanje nije moguće postaviti.",
    "notify.autostart_off": "Isključeno: program se neće pokretati sa sustavom Windows.",
    "notify.autostart_on": "Uključeno: program se pokreće sa sustavom Windows.",
    "notify.first_run": "Panel se pojavio u gornjem desnom kutu.\nDesni klik na panel ili ikonu u području obavijesti = izbornik.",
    "notify.login_ok": "Prijava uspješna – stižu podaci s poslužitelja.",
    "notify.logout": "Odjavljeni ste. Sada se koristi lokalni izvor.",
    "notify.reset_done": "{}: resetirano – počelo je novo razdoblje.",
    "notify.signin_needed": "Prijava na claude.ai je istekla. Desnom tipkom kliknite panel i ponovno se prijavite kako biste i dalje vidjeli potrošnju sa svih svojih uređaja.",
    "notify.stale_body": "Posljednje očitanje staro je {}. Je li Claude Desktop pokrenut?",
    "notify.stale_title": "Zastarjeli podaci",
    "notify.threshold": "{}: iskorišteno {}%.",
    "notify.update": "Dostupna je verzija programa {}. Desni klik na panel → Ažuriranje programa.",

    # --- panel labels (tight space) ----------------------------------------------------------
    "panel.five_hour": "SESIJA OD 5 SATI",
    "panel.five_hour_short": "5H",
    "panel.full_in": "100% za {}",
    "panel.model": "{} TJEDNO",
    "panel.no_data": "Nema podataka",
    "panel.pace": "{} vs tempo",
    "panel.per_day": "{}%/dan",
    "panel.per_hour": "{}%/h",
    "panel.refreshing": "dohvaćanje",
    "panel.reset": "reset za {}",
    "panel.retry_in": "ponovno za {} s",
    "panel.updated": "ažurirano: {}",
    "panel.week_short": "TJED.",
    "panel.weekly": "TJEDNO OGRANIČENJE",

    # --- profile -----------------------------------------------------------------------------
    "profile.extra": "Krediti za potrošnju: {}",
    "profile.plan": "Paket: {}",
    "profile.since": "Član od: {}",
    "profile.tier": "Razina ograničenja zahtjeva: {}",

    # --- Settings window ---------------------------------------------------------------------
    "set.about": "{}\nBez telemetrije. Od tvrtke Anthropic traži samo podatke o vašoj potrošnji, a s poslužitelja za ažuriranja čita broj verzije.",
    "set.accent": "Boja naglaska",
    "set.always_top": "Iznad svih ostalih prozora",
    "set.auto": "automatski",
    "set.backup_config": "Konfiguracija skripte za sigurnosne kopije",
    "set.backup_details": "Prozor pojedinosti prikazuje",
    "set.backup_disclaimer": "Claude Usage Monitor samo čita i prikazuje zapisnike vaših sigurnosnih kopija – ne izrađuje, ne provjerava i ne jamči nijednu sigurnosnu kopiju. Claude Backup Kit besplatna je polazna točka ponuđena kao pomoć: skripte može promijeniti bilo tko, pa se kvaliteta i potpunost sigurnosne kopije ne mogu jamčiti. Ne preuzimamo nikakvu odgovornost za sigurnosne kopije, izgubljene podatke ni bilo kakvu štetu. Svatko je sam odgovoran za to da su njegove sigurnosne kopije potpune i da se mogu vratiti – povremeno isprobajte vraćanje.",
    "set.backup_disclaimer_h": "Odricanje od odgovornosti",
    "set.backup_enabled": "Prikaži traku stanja sigurnosnih kopija na panelu",
    "set.backup_found": "Pronađeno: {}",
    "set.backup_green": "Zelena do",
    "set.backup_label": "Oznaka uz lampicu",
    "set.backup_lamps": "Lampice",
    "set.backup_root": "Mapa sigurnosnih kopija",
    "set.backup_tasks": "Filtar zakazanih zadataka",
    "set.backup_unconfigured": "Mapa sigurnosnih kopija nije postavljena pa je traka stanja skrivena. Odaberite mapu u koju zapisuje vaša skripta za sigurnosne kopije.",
    "set.backup_yellow": "Žuta do",
    "set.browse": "Pregledaj…",
    "set.click_through": "Propuštanje klikova (samo ukras, zanemaruje miš)",
    "set.close": "Zatvori",
    "set.color_hint": "Boje se mijenjaju prema pragovima: zelena → žuta → crvena.",
    "set.danger": "Kritično",
    "set.data_hint": "Lokalni zapisnik: datoteka plan-usage-history.json programa Claude Desktop. Prijava nije potrebna, ali mjeri samo potrošnju na ovom računalu i osvježava se otprilike svakih 5 minuta.\n\nclaude.ai: nakon prijave podatke dohvaća s poslužitelja. Vidite potrošnju sa svih svojih uređaja, s točnim vremenima reseta i češćim osvježavanjem.",
    "set.datafile": "Datoteka s podacima",
    "set.default": "Zadano",
    "set.details_api_only": "Ovi podaci dolaze iz izvora podataka claude.ai (potrebna je prijava); lokalni zapisnik ih ne sadrži.",
    "set.file_filter": "JSON (*.json);;Sve datoteke (*.*)",
    "set.gauge_order": "Redoslijed mjerača",
    "set.hours_suffix": " h",
    "set.layout": "Raspored",
    "set.local_models_hint": "Poslužitelj vodi zaseban brojač samo za neke modele (npr. Fable). Za ostale ovo prikazuje kako je raspodijeljen ovotjedni rad u programu Claude Code na ovom računalu – udio u vašoj potrošnji i izlazni tokeni, a ne udio u ograničenju. Čitaju se samo naziv modela i broj tokena, nikada razgovor.",
    "set.local_models_none": "Mapa zapisnika programa Claude Code nije pronađena – ova grupa jednostavno ostaje skrivena. Na ništa drugo to ne utječe.",
    "set.local_models_path": "Mapa zapisnika programa Claude Code",
    "set.lock": "Zaključaj položaj (ne može se povlačiti)",
    "set.login_btn_in": "Odjava s claude.ai",
    "set.login_btn_out": "Prijava na claude.ai…",
    "set.model_filter": "Model koji se prati",
    "set.model_scale": "Veličina mjerača modela",
    "set.not_set": "nije postavljeno",
    "set.notify_enabled": "Obavijest pri prelasku praga",
    "set.notify_reset": "Obavijest kad se ograničenje resetira",
    "set.notify_stale": "Obavijest kad podaci zastare",
    "set.opacity": "Neprozirnost",
    "set.open_config": "Otvori mapu postavki",
    "set.pick_color": "Odaberi boju…",
    "set.pick_file_title": "Odabir zapisnika potrošnje",
    "set.profile": "Profil / račun",
    "set.profile_auto": "Automatski (posljednji korišteni)",
    "set.profile_n": "Profil {} – …{}",
    "set.refresh": "Osvježavanje",
    "set.reset_confirm": "Želite li zaista vratiti zadane postavke?",
    "set.restore": "Vrati zadano",
    "set.rows_available": "Što se trenutačno može prikazati – poništite odabir onoga što ne želite vidjeti:",
    "set.rows_none": "Poslužitelj trenutačno ne šalje dodatna ograničenja za vaš račun. Čim ih pošalje, automatski će se pojaviti ovdje.",
    "set.sec_suffix": " s",
    "set.show_age": "Svježina podataka",
    "set.show_burn": "Brzina potrošnje (%/h, %/dan)",
    "set.show_extra_usage": "Krediti za potrošnju (plaćanje po potrošnji)",
    "set.show_feedback_icon": "Ikona poruke u zaglavlju panela",
    "set.show_five_hour": "Prikaži sesiju od 5 sati",
    "set.show_local_models": "Raspodjela po modelima, iz zapisnika programa Claude Code na ovom računalu",
    "set.show_model": "Prikaži tjedno ograničenje modela (izvor claude.ai)",
    "set.show_model_list": "Tjedna ograničenja ostalih modela",
    "set.show_plan_badge": "Oznaka paketa u zaglavlju (Pro / Max…)",
    "set.show_plan_name": "Prikaži moje ime na oznaci",
    "set.show_reset": "Odbrojavanje do reseta",
    "set.show_spark": "Krivulja trenda (minigrafikon)",
    "set.show_surfaces": "Ograničenja po usluzi (Claude Code, povezane aplikacije…)",
    "set.show_weekly": "Prikaži tjedno ograničenje",
    "set.size": "Veličina",
    "set.snap": "Prianjanje uz rub zaslona",
    "set.source_api": "claude.ai – svi uređaji (potrebna je prijava)",
    "set.source_label": "Izvor mjerenja",
    "set.source_local": "Lokalni zapisnik – samo ovo računalo",
    "set.tab_alerts": "Upozorenja",
    "set.tab_appearance": "Izgled",
    "set.tab_content": "Sadržaj",
    "set.tab_data": "Izvor podataka",
    "set.tab_details": "Pojedinosti",
    "set.tab_system": "Sustav",
    "set.taskbar": "Prikaži na programskoj traci (kao prozor)",
    "set.theme": "Tema",
    "set.theme_default": "Zadano prema temi",
    "set.tip": "Savjet: panel povucite lijevom tipkom, Ctrl + kotačić mijenja veličinu,\ndesni klik = izbornik, dvoklik = povijest.",
    "set.title": "postavke",
    "set.tray_five": "Sesija od 5 sati",
    "set.tray_max": "Veća vrijednost",
    "set.tray_value": "Vrijednost na ikoni u području obavijesti",
    "set.tray_weekly": "Tjedno ograničenje",
    "set.update_check": "Automatski provjeravaj ažuriranja programa",
    "set.version": "Verzija",
    "set.visible": "Prikaži lebdeći panel",
    "set.warn": "Upozorenje",

    # --- size / source / theme options -------------------------------------------------------
    "size.extra": "Vrlo velika",
    "size.large": "Velika",
    "size.normal": "Normalna",
    "size.small": "Mala",
    "source.api": "claude.ai (svi uređaji)",
    "source.local": "Lokalno (samo ovo računalo)",
    "theme.claude": "Claude (topla tamna)",
    "theme.graphite": "Grafit",
    "theme.midnight": "Ponoćno staklo",
    "theme.neon": "Neonski sjaj",
    "theme.paper": "Svijetli papir",
    "theme.postit": "Post-it žuta",

    # --- time units (panel) ------------------------------------------------------------------
    "time.day": "{} d",
    "time.dh": "{}d {}h",
    "time.hm": "{}h {}min",
    "time.hour": "{} h",
    "time.m": "{}min",
    "time.min": "{} min",
    "time.none": "nema podataka",
    "time.sec": "{} s",

    # --- tray --------------------------------------------------------------------------------
    "tray.head": "5h: {}%   ·   Tjedno: {}%",
    "tray.line": "{}: {}%",

    # --- program update ----------------------------------------------------------------------
    "update.available": "Dostupna je verzija {}.",
    "update.check_failed": "Provjera ažuriranja nije uspjela: {}",
    "update.check_now": "Provjeri sada",
    "update.checking": "Provjera ažuriranja…",
    "update.downloading": "Preuzimanje… {} od {}",
    "update.failed": "Ažuriranje nije uspjelo: {}",
    "update.install": "Instaliraj sada",
    "update.installed": "Instalirana verzija: {}",
    "update.later": "Kasnije",
    "update.manual": "Ovaj se primjerak programa ne može sam ažurirati (pokreće se iz izvornog koda ili iz mape samo za čitanje). Umjesto toga preuzmite novi paket.",
    "update.open_page": "Otvori stranicu za preuzimanje",
    "update.restarting": "Instalacija u tijeku – program će se uskoro ponovno pokrenuti.",
    "update.skip": "Preskoči ovu verziju",
    "update.title": "Ažuriranje programa",
    "update.uptodate": "Imate najnoviju verziju.",
    "update.verifying": "Provjera i raspakiravanje…",
    "update.whats_new": "Novosti",
}

# macOS wording: "Otvori pri prijavi" (Apple) instead of "start with Windows", traka izbornika instead of tray
STRINGS_MAC = {
    "menu.autostart": "Otvori pri prijavi",
    "notify.autostart_on": "Uključeno: program se otvara pri prijavi.",
    "notify.autostart_off": "Isključeno: program se neće otvarati pri prijavi.",
    "notify.first_run": "Panel se pojavio u gornjem desnom kutu.\nDesni klik na panel ili ikonu na traci izbornika = izbornik.",
}
