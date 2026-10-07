# -*- coding: utf-8 -*-
"""Eesti – UI strings of Claude Usage Monitor."""

CODE = "et"
NAME = "Eesti"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{}p",
    "backup.age_h": "{}h",
    "backup.age_m": "{}min",
    "backup.and_more": "…ja veel {}",
    "backup.checked_at": "Kontrollitud: {}",
    "backup.checking": "Kontrollimine…",
    "backup.cloud_only": "Hetktõmmis on OneDrive'is saadaval ainult võrgus; selle sisu ei loetleta, et seda ei peaks alla laadima.",
    "backup.comp.cowork": "Coworki vestluslogid (üks ZIP seansi kohta)",
    "backup.comp.vault": "Obsidiani hoidla hetktõmmis (ZIP)",
    "backup.disclaimer_short": "Monitor näitab ainult seda, mida varunduslogid ütlevad. Me ei vastuta varukoopiate eest – nende täielikkust ja taastatavust pead kontrollima ise.",
    "backup.done": "valmis",
    "backup.dry_run": "(proovikäivitus, midagi ei laaditud üles)",
    "backup.failed": "EBAÕNNESTUS",
    "backup.files_size": "{} faili, {}",
    "backup.folders": "Kaustad",
    "backup.label_age": "Nimi ja vanus",
    "backup.label_name": "Ainult nimi",
    "backup.label_none": "Ainult lambid",
    "backup.last_ok": "Viimane õnnestunud varundus: {} ({} tagasi)",
    "backup.last_run": "Viimane käivitus: {} – {}",
    "backup.legend": "Roheline: kuni {} h vana · Kollane: kuni {} h · Punane: vanem või varukoopiat pole",
    "backup.level_green": "Värske",
    "backup.level_none": "Varukoopiat ei leitud",
    "backup.level_red": "Aegunud",
    "backup.level_yellow": "Vananemas",
    "backup.log_file": "Logifail",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Varunduskausta ei leitud: {}",
    "backup.none_found": "Pole.",
    "backup.open": "ava",
    "backup.rc_copied": "uued või muudetud failid kopeeriti",
    "backup.rc_failed": "EBAÕNNESTUS (kood {})",
    "backup.rc_nochange": "ajakohane, polnud midagi kopeerida",
    "backup.recent_notes": "Hetktõmmise viimati muudetud märkmed",
    "backup.refresh": "Kontrolli kohe",
    "backup.sec_components": "Mida varundatakse",
    "backup.sec_contents": "Sisu",
    "backup.sec_log": "Logi (viimased read)",
    "backup.sec_problems": "Vead ja hoiatused",
    "backup.sec_tasks": "Ajastatud toimingud",
    "backup.skipped": "vahele jäetud (kausta ei leitud)",
    "backup.snap_kept": "Säilitatud hetktõmmiseid: {}, kokku {}",
    "backup.snapshot": "Viimane hetktõmmis",
    "backup.source": "Allikas",
    "backup.state_error": "lõppes vigadega",
    "backup.state_interrupted": "jäi pooleli",
    "backup.state_ok": "lõppes edukalt",
    "backup.state_running": "praegu käimas",
    "backup.storage": "Kaugsalvestusruum: kasutusel {} / {}, vaba {}",
    "backup.target": "Sihtkoht",
    "backup.task_event": "sündmuse korral",
    "backup.task_row": "viimane käivitus {} · tulemus {} · järgmine {}",
    "backup.tip_click": "Klõpsa üksikasjade vaatamiseks",
    "backup.title": "Varukoopiad",
    "backup.tray": "Varukoopiad: {}",
    "backup.uploaded": "Selles käivituses üles laaditud: uusi {}, asendatud {}, vigu {}",
    "backup.uploaded_files": "Üles laaditud failid",
    "backup.uploaded_groups": "Üles laaditud failid kausta kaupa",
    "backup.uploaded_no": "Nextcloudi üles laaditud: veel mitte",
    "backup.uploaded_yes": "Nextcloudi üles laaditud: jah ({})",
    "backup.vault": "Hoidla",
    "backup.vault_changed": "Pärast seda hetktõmmist on hoidlas muutunud märkmeid: {}",
    "backup.zip_new": "Uusi/värskendatud ZIP-e: {}",
    "backup.zip_summary": "{} faili ({} märget), lahtipakituna {}",

    # --- general ---------------------------------------------------------------------------
    "detail.extra": "Kasutuskrediit",
    "detail.local_header": "CLAUDE CODE · SEE ARVUTI · SELLE NÄDALA JAOTUS",
    "detail.off": "väljas",
    "detail.on": "sees",
    "detail.surface.oauth_apps": "Ühendatud rakendused",
    "detail.unlimited": "limiidita",
    "dlg.cancel": "Loobu",
    "dlg.checking": "Kontrollimine…",
    "dlg.err_badcode": "Koodi ei aktsepteeritud.\n\n{}\n\nKontrolli, kas kleepisid kogu koodi, või proovi brauseris uuesti sisse logida (iga kord on vaja uut koodi).",
    "dlg.err_ratelimit": "Liiga palju sisselogimiskatseid lühikese aja jooksul.\n\nServer piirab sind ajutiselt. Sule see aken, oota 10–15 minutit (vahepeal ära proovi) ja proovi siis brauseris värske koodiga ÜKS kord uuesti sisse logida.",
    "dlg.hint1": "Logi avanenud lehel sisse ja kinnita juurdepääs. Lõpus saad koodi.",
    "dlg.intro": "Logi oma brauseris claude.ai kontole sisse (sinu salvestatud paroolid ja pääsuvõtmed töötavad seal juba).",
    "dlg.login_title": "sisselogimine",
    "dlg.open_browser": "Ava sisselogimisleht brauseris",
    "dlg.paste_label": "Kleebi saadud kood siia:",
    "dlg.paste_placeholder": "kleebi kood siia",
    "dlg.signin": "Logi sisse",
    "dlg.step1": "1. samm",
    "dlg.step2": "2. samm",
    "dlg.unknown_err": "Tundmatu viga.",

    # --- error messages --------------------------------------------------------------------
    "err.already_running": "Rakendus juba töötab (vaata teavitusalast).",
    "err.bad_token_resp": "vigane vastus tokeni lõpp-punktist",
    "err.bad_usage_resp": "vigane vastus kasutusandmete lõpp-punktist",
    "err.connection": "ühendusviga: {}",
    "err.file_empty": "Kasutusfail on tühi.",
    "err.file_not_found": "Kasutusfaili ei leitud.\nKas Claude Desktop töötab?",
    "err.file_unreadable": "Kasutusfaili ei saa praegu lugeda.",
    "err.loading": "Sisselogimine / päring…",
    "err.network": "võrguviga: {}",
    "err.no_code": "Koodi pole kleebitud.",
    "err.no_data_profile": "Selle profiili kohta andmeid pole.",
    "err.no_tray": "Teavitusala pole saadaval; teavitusala ikooni ei kuvata.",
    "err.no_usage_data": "Kasutusandmeid pole.",
    "err.not_signed_in": "Pole sisse logitud.",
    "err.query_http": "Päringuviga (HTTP {}).",
    "err.rate_limited": "Server piirab päringuid (429) – proovitakse automaatselt uuesti.",
    "err.session_expired": "Seanss on aegunud, logi uuesti sisse.",
    "err.session_expired_nl": "Seanss on aegunud.\nLogi uuesti sisse.",
    "err.signin_needed": "claude.ai sisselogimine on aegunud.\nLogi uuesti sisse: paremklõps → Logi sisse claude.ai-sse",
    "err.unexpected": "Ootamatu viga: {}",

    # --- 'Message to the developer' window ---------------------------------------------------
    "fb.cancel": "Loobu",
    "fb.close": "Sule",
    "fb.consent": "Olen tutvunud dokumendiga {} ja nõustun sellega.",
    "fb.email": "E-post",
    "fb.email_hint": "ainult siis, kui soovid vastust",
    "fb.err_consent": "Saatmiseks nõustu privaatsuspoliitikaga.",
    "fb.err_email": "See e-posti aadress ei tundu õige.",
    "fb.err_empty": "Kirjuta esmalt sõnum või vali hinnang.",
    "fb.err_links": "Sõnumis on liiga palju linke.",
    "fb.err_network": "Saidiga claudeusagemonitor.com ei saanud ühendust. Kontrolli internetiühendust ja proovi uuesti.",
    "fb.err_rate": "Liiga palju sõnumeid lühikese aja jooksul – proovi hiljem uuesti.",
    "fb.err_server": "Server ei saanud sõnumit praegu vastu võtta. Proovi hiljem uuesti.",
    "fb.intro": "Sul on idee, leidsid vea või programm lihtsalt meeldib? Kirjuta mulle. Iga sõnumi loen läbi mina ise, Vidovics Gábor, programmi autor.",
    "fb.message": "Sõnum",
    "fb.message_ph": "Mis töötab, mis mitte, mis puudub?",
    "fb.meta": "Koos sõnumiga saadetakse: programmi versioon {0}, operatsioonisüsteem ({1}), kasutajaliidese keel ({2}).",
    "fb.name": "Nimi",
    "fb.optional": "(valikuline)",
    "fb.privacy_hide": "Peida privaatsuspoliitika",
    "fb.privacy_text": (
        "Vastutav töötleja: Vidovics Gábor, eraisik (Ungari), Claude Usage Monitori autor. Täielik "
        "privaatsuspoliitika on veebisaidil: https://claudeusagemonitor.com/#privacy\n\n"
        "Mida saadetakse: see, mille siia sisestad – nimi (valikuline), e-posti aadress (valikuline), sõnum, "
        "tärnihinnang –, ning et ma mõistaksin konteksti, ka programmi versioon, operatsioonisüsteemi nimi ja "
        "versioon, kasutajaliidese keel ja saatmise aeg. Server ei salvesta IP-aadressi; kuritarvitamise "
        "vältimiseks kasutab see ainult iga päev muutuvat räsi, millest aadressi tagasi tuletada ei saa.\n\n"
        "Miks: et sinu sõnumit lugeda ja sellele vastata ning programmi täiustada (õigustatud huvi, "
        "isikuandmete kaitse üldmääruse (GDPR) artikli 6 lõike 1 punkt f; vastus ise sinu taotlusel). Sinu "
        "hinnang ja nimi ilmuvad veebisaidil ainult siis, kui märgid selleks eraldi ruudu (nõusolek, "
        "artikli 6 lõike 1 punkt a), ja alles pärast seda, kui autor on need üle vaadanud; selle nõusoleku "
        "võid igal ajal tagasi võtta.\n\n"
        "Kui kaua: sõnumeid kuni 2 aastat; avaldatud hinnangut kuni nõusoleku tagasivõtmiseni. Kui autor on "
        "e-kirjade edastamise sisse lülitanud, jõuab koopia ka autori postkasti.\n\n"
        "Kes näeb: ainult vastutav töötleja ning volitatud töötlejana majutusteenuse pakkuja (server asub "
        "ELis, Saksamaal). Midagi ei müüda ega anta edasi; profiilianalüüsi ega automatiseeritud otsuste "
        "tegemist ei toimu.\n\n"
        "Sinu õigused: juurdepääs, parandamine, kustutamine, töötlemise piiramine, vastuväite esitamine, "
        "nõusoleku tagasivõtmine ning kaebuse esitamine järelevalveasutusele (Ungaris: NAIH, naih.hu) või "
        "oma riigi järelevalveasutusele (Eestis: Andmekaitse Inspektsioon, aki.ee). Kontakt: see vorm või "
        "veebisait.\n\n"
        "Edastamine: krüptitult (HTTPS/TLS) saidile claudeusagemonitor.com. Selle teabe versioon: 2026-10-06."
    ),
    "fb.privacy_title": "Privaatsuspoliitika",
    "fb.publish": "Minu hinnangut ja nime (kui see on antud) võib näidata saidil claudeusagemonitor.com.",
    "fb.rating": "Üldhinnang",
    "fb.rating_clear": "tühjenda",
    "fb.rating_hint": "valikuline – klõpsa tärnil",
    "fb.rating_tip": "{} / 5",
    "fb.secure": "Krüptitud ühendus (HTTPS) saidiga claudeusagemonitor.com.",
    "fb.send": "Saada",
    "fb.sending": "Saatmine…",
    "fb.sent": "Aitäh – sõnum jõudis kohale!",
    "fb.sent_sub": "Loen iga sõnumi läbi. Kui jätsid e-posti aadressi, vastan sinna.",
    "fb.title": "Sõnum arendajale",

    # --- Help window -------------------------------------------------------------------------
    "help.disclaimer": "Sõltumatu tasuta tööriist – Anthropic ei ole seda loonud ega sellega seotud. „Claude“ on Anthropicu kaubamärk.",
    "help.feedback": "Küsimused, ideed, veateated: veebisaidi sõnumivorm.",
    "help.free": "Igavesti tasuta · MIT-litsents · avatud lähtekood · telemeetriat pole",
    "help.guide": (
        "\n<h2>Mida vidin näitab</h2>\n<ul>\n"
        "<li><b>5-tunni seanss</b> – kui suur osa praeguse seansi limiidist on kasutatud. See lähtestub iga "
        "viie tunni järel; vidin näitab pöördloendust lähtestuseni.</li>\n"
        "<li><b>Nädalalimiit</b> – kõigi mudelite kasutus kokku; see lähtestub kord nädalas sinu kontole määratud ajal.</li>\n"
        "<li><b>Mudelipõhine nädalalimiit</b> – kolmas näidik, kui server sellest teatab (nt kindla mudeli "
        "kohta).</li>\n"
        "<li><b>Tempo ja kulumiskiirus</b> – kui kiiresti limiiti kulutad ja kas see peab lähtestuseni vastu; "
        "nädala lõpu prognoos hoiatab õigel ajal.</li>\n"
        "<li><b>Kasutuskrediit</b> ja paketimärk – kui lülitad need sisse menüüs <i>Paketimärk ja "
        "lisalimiidid</i>.</li>\n</ul>\n"
        "<h2>Kust andmed tulevad</h2>\n<ul>\n"
        "<li><b>claude.ai (kõik seadmed)</b> – küsib andmeid Anthropicu serverist, nii et arvesse läheb ka "
        "kasutus telefonis, brauseris ja teistes arvutites. Vajab ühekordset sisselogimist sinu enda brauseris "
        "(menüü: <i>Logi sisse</i>). Värskendub iga 2 minuti järel, harvemini, kui server seda palub.</li>\n"
        "<li><b>Kohalik (ainult see arvuti)</b> – loeb selles arvutis Claude Desktopi kasutuslogi. "
        "Sisselogimist pole vaja, kuid see näeb ainult selle arvuti kasutust.</li>\n</ul>\n"
        "<p>Nende vahel saad valida menüüs <i>Andmeallikas</i>.</p>\n"
        "<h2>Vidina kasutamine</h2>\n<ul>\n"
        "<li><b>Paremklõps</b> vidinal (või teavitusala ikoonil) – kogu menüü.</li>\n"
        "<li><b>Topeltklõps</b> näidikul – aken <b>Ajalugu</b>: 6 tundi, 24 tundi, 7 päeva või kõik, koos "
        "tippude, päevase keskmise ja prognoosiga.</li>\n"
        "<li><b>Lohista</b> vidinat, et seda liigutada; see haakub ekraani servade külge. "
        "<b>Ctrl + hiireratas</b> – suuremaks või väiksemaks.</li>\n"
        "<li>Paigutused: märkmeleht, kitsas riba, rõngad; 6 kujundust. <i>Lukusta asukoht</i> ja "
        "<i>Läbiklõpsatav</i> on sätetes.</li>\n</ul>\n"
        "<h2>Hoiatused</h2>\n"
        "<p>Kollane alates 70 %, punane alates 90 % (muudetav). Soovi korral teatised, kui limiit lähtestub "
        "ja kui andmed vananevad.</p>\n"
        "<h2>Varukoopiad (valikuline)</h2>\n"
        "<p>Väikesed lambid näitavad, kas sinu ajastatud varundused käivitusid ja lõppesid. Üksikasjade "
        "nägemiseks klõpsa lambil. Monitor loeb ainult varunduslogisid – varukoopiate tegemine ja testimine "
        "on sinu ülesanne (vt kasutustingimusi).</p>\n"
        "<h2>Värskendused</h2>\n"
        "<p>Programm otsib uusi versioone ise ja värskendub ühe klõpsuga. Iga paketti kontrollitakse "
        "SHA-256-ga ja see tuleb ainult saidilt <b>claudeusagemonitor.com</b>. Uued versioonid ja "
        "väljalaskemärkmed: {site}</p>\n"
        "<h2>Privaatsus</h2>\n"
        "<p>Telemeetriat ega jälgimist pole. claude.ai sisselogimisandmed salvestatakse krüptitult ainult "
        "selles arvutis; mujale ei saadeta midagi.</p>\n"
        "<h2>Kui midagi on valesti</h2>\n<ul>\n"
        "<li><i>429 / päringupiirang</i> – server aeglustab päringuid; programm proovib ise uuesti.</li>\n"
        "<li>Andmeid pole – kontrolli <i>andmeallikat</i>; claude.ai puhul logi uuesti sisse.</li>\n"
        "<li>Ajalugu säilitatakse 7 päeva ning see säilib ka pärast taaskäivitamist ja värskendamist.</li>\n"
        "<li>Logid ja sätted: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Loonud",
    "help.moved": "Uus aadress alates 21. septembrist 2026 – endine leht dinorr.hu/claude-usage-monitor suunab siia.",
    "help.official": "AMETLIK VEEBISAIT",
    "help.open_site": "Ava claudeusagemonitor.com",
    "help.privacy": "Privaatsuspoliitika",
    "help.site_what": "Allalaadimised, automaatsed värskendused, väljalaskemärkmed, Claude Backup Kit, kasutustingimused ja privaatsus – kõik ühes kohas.",
    "help.source_code": "Lähtekood (GitHub)",
    "help.tab_author": "Autor",
    "help.tab_guide": "Kuidas see töötab",
    "help.terms": "Kasutustingimused",
    "help.title": "Spikker",
    "help.version": "Versioon",

    # --- History window ----------------------------------------------------------------------
    "hist.legend_5h": "5-tunni seanss",
    "hist.legend_week": "nädalalimiit",
    "hist.no_data": "Selle perioodi kohta pole piisavalt andmeid.",
    "hist.range_24h": "24 tundi",
    "hist.range_6h": "6 tundi",
    "hist.range_7d": "7 päeva",
    "hist.range_all": "Kõik",
    "hist.stat_burn": "Keskmine päevakulu",
    "hist.stat_forecast": "Nädala lõpu prognoos",
    "hist.stat_now": "Praegune nädalakasutus",
    "hist.stat_peak": "Nädala tipp",
    "hist.stat_sessions": "5-tunni seansid",
    "hist.title": "ajalugu",

    # --- layout names ------------------------------------------------------------------------
    "layout.compact": "Kitsas riba",
    "layout.postit": "Märkmeleht",
    "layout.ring": "Rõngad",

    # --- context menu ------------------------------------------------------------------------
    "menu.always_top": "Alati pealmine",
    "menu.autostart": "Käivita koos Windowsiga",
    "menu.backup_bar": "Varunduse olekuriba",
    "menu.backups": "Varukoopiad…",
    "menu.check_update": "Otsi programmi värskendusi…",
    "menu.click_through": "Läbiklõpsatav",
    "menu.details": "Paketimärk ja lisalimiidid",
    "menu.feedback": "Sõnum arendajale…",
    "menu.help": "Spikker…",
    "menu.history": "Ajalugu ja statistika…",
    "menu.language": "Keel",
    "menu.layout": "Paigutus",
    "menu.locked": "Lukusta asukoht",
    "menu.login": "Logi sisse (claude.ai, brauser)…",
    "menu.logout": "Logi välja",
    "menu.model_gauge": "Näidik: {}",
    "menu.order": "Järjestus",
    "menu.panel_visible": "Kuva paneel",
    "menu.quit": "Välju",
    "menu.refresh": "Värskenda kasutusandmeid kohe",
    "menu.settings": "Sätted…",
    "menu.size": "Suurus",
    "menu.source": "Andmeallikas",
    "menu.start_menu": "Kuva menüüs Start",
    "menu.theme": "Kujundus",
    "menu.update_available": "Programmi värskendus: installi versioon {}…",

    # --- desktop notifications ---------------------------------------------------------------
    "notify.autostart_fail": "Automaatset käivitamist ei õnnestunud seadistada.",
    "notify.autostart_off": "Välja lülitatud: rakendus ei käivitu koos Windowsiga.",
    "notify.autostart_on": "Sisse lülitatud: rakendus käivitub koos Windowsiga.",
    "notify.first_run": "Paneel ilmus ekraani paremasse ülanurka.\nMenüü avamiseks paremklõpsa paneelil või teavitusala ikoonil.",
    "notify.login_ok": "Sisse logitud – serveri andmed on teel.",
    "notify.logout": "Välja logitud. Kasutusel on nüüd kohalik allikas.",
    "notify.reset_done": "{}: lähtestatud – algas uus periood.",
    "notify.signin_needed": "claude.ai sisselogimine on aegunud. Paremklõpsa paneelil ja logi uuesti sisse, et ka edaspidi näha kõigi oma seadmete kasutust.",
    "notify.stale_body": "Viimane näit on {} vana. Kas Claude Desktop töötab?",
    "notify.stale_title": "Aegunud andmed",
    "notify.threshold": "{}: {}% kasutatud.",
    "notify.update": "Saadaval on programmi versioon {}. Paremklõpsa paneelil → Programmi värskendus.",

    # --- panel labels (tight space) ----------------------------------------------------------
    "panel.five_hour": "5 H SEANSS",
    "panel.five_hour_short": "5H",
    "panel.full_in": "täis: {}",
    "panel.model": "{} NÄDAL",
    "panel.no_data": "Andmeid pole",
    "panel.pace": "{} vs tempo",
    "panel.per_day": "{}%/p",
    "panel.per_hour": "{}%/h",
    "panel.refreshing": "andmepäring",
    "panel.reset": "lähtestus {}",
    "panel.retry_in": "uus katse {} s",
    "panel.updated": "seisuga {}",
    "panel.week_short": "NÄDAL",
    "panel.weekly": "NÄDALALIMIIT",

    # --- profile -----------------------------------------------------------------------------
    "profile.extra": "Kasutuskrediit: {}",
    "profile.plan": "Pakett: {}",
    "profile.since": "Liige alates: {}",
    "profile.tier": "Päringupiirangu tase: {}",

    # --- Settings window ---------------------------------------------------------------------
    "set.about": "{}\nTelemeetriat pole. Rakendus küsib Anthropicult ainult sinu enda kasutust ja loeb värskendusserverist versiooninumbri.",
    "set.accent": "Rõhuvärv",
    "set.always_top": "Kõigi teiste akende peal",
    "set.auto": "automaatne",
    "set.backup_config": "Varundusskripti konfiguratsioon",
    "set.backup_details": "Üksikasjade aknas kuvatakse",
    "set.backup_disclaimer": "Claude Usage Monitor ainult loeb ja kuvab sinu varunduslogisid – see ei loo, ei kontrolli ega garanteeri ühtegi varukoopiat. Claude Backup Kit on abiks pakutav tasuta lähtepunkt: igaüks saab skripte muuta, seega ei saa varukoopia kvaliteeti ja täielikkust garanteerida. Me ei vastuta varukoopiate, kaotatud andmete ega mis tahes kahju eest. Varukoopiate täielikkuse ja taastatavuse tagamine on igaühe enda vastutus – testi aeg-ajalt taastamist.",
    "set.backup_disclaimer_h": "Vastutuse välistamine",
    "set.backup_enabled": "Kuva paneelil varunduse olekuriba",
    "set.backup_found": "Leitud: {}",
    "set.backup_green": "Roheline kuni",
    "set.backup_label": "Silt lambi kõrval",
    "set.backup_lamps": "Lambid",
    "set.backup_root": "Varunduskaust",
    "set.backup_tasks": "Ajastatud toimingute filter",
    "set.backup_unconfigured": "Varunduskausta pole määratud, seega jääb olekuriba peidetuks. Vali kaust, kuhu sinu varundusskript kirjutab.",
    "set.backup_yellow": "Kollane kuni",
    "set.browse": "Sirvi…",
    "set.click_through": "Läbiklõpsatav (ainult kaunistus, hiirt eiratakse)",
    "set.close": "Sule",
    "set.color_hint": "Värvid muutuvad lävendite järgi: roheline → kollane → punane.",
    "set.danger": "Kriitiline",
    "set.data_hint": "Kohalik logi: Claude Desktopi fail plan-usage-history.json. Sisselogimist pole vaja, kuid mõõdetakse ainult seda arvutit ja andmed värskenduvad umbes iga 5 minuti järel.\n\nclaude.ai: pärast sisselogimist küsitakse andmeid serverist. Näed kõigi oma seadmete kasutust ja täpseid lähtestusaegu ning andmed värskenduvad sagedamini.",
    "set.datafile": "Andmefail",
    "set.default": "Vaikimisi",
    "set.details_api_only": "Need tulevad andmeallikast claude.ai (vajab sisselogimist); kohalikus logis neid pole.",
    "set.file_filter": "JSON (*.json);;Kõik failid (*.*)",
    "set.gauge_order": "Näidikute järjestus",
    "set.hours_suffix": " h",
    "set.layout": "Paigutus",
    "set.local_models_hint": "Server peab eraldi loendurit ainult mõne mudeli kohta (nt Fable). Teiste puhul näitab see, kuidas jaguneb selle nädala Claude Code'i töö selles arvutis – osakaal sinu enda kasutusest ja väljundtokenitest, mitte limiidist. Loetakse ainult mudeli nime ja tokenite arvu, vestlusi mitte kunagi.",
    "set.local_models_none": "Claude Code'i logikausta ei leitud – see rühm jääb lihtsalt peidetuks. Muud see ei mõjuta.",
    "set.local_models_path": "Claude Code'i logikaust",
    "set.lock": "Lukusta asukoht (ei saa lohistada)",
    "set.login_btn_in": "Logi claude.ai-st välja",
    "set.login_btn_out": "Logi sisse claude.ai-sse…",
    "set.model_filter": "Jälgitav mudel",
    "set.model_scale": "Mudelinäidiku suurus",
    "set.not_set": "määramata",
    "set.notify_enabled": "Teavita lävendi ületamisel",
    "set.notify_reset": "Teavita, kui limiit lähtestub",
    "set.notify_stale": "Teavita, kui andmed vananevad",
    "set.opacity": "Läbipaistmatus",
    "set.open_config": "Ava sätete kaust",
    "set.pick_color": "Vali värv…",
    "set.pick_file_title": "Vali kasutuslogi",
    "set.profile": "Profiil / konto",
    "set.profile_auto": "Automaatne (viimati kasutatud)",
    "set.profile_n": "Profiil {} – …{}",
    "set.refresh": "Värskenda",
    "set.reset_confirm": "Kas soovid kindlasti vaikesätted taastada?",
    "set.restore": "Taasta vaikesätted",
    "set.rows_available": "Mida saab praegu kuvada – eemalda linnuke sellelt, mida sa näha ei soovi:",
    "set.rows_none": "Server ei saada praegu sinu konto kohta rohkem limiite. Niipea kui saadab, ilmuvad need siia automaatselt.",
    "set.sec_suffix": " s",
    "set.show_age": "Andmete värskus",
    "set.show_burn": "Kulumiskiirus (%/tund, %/päev)",
    "set.show_extra_usage": "Kasutuskrediit (kasutuspõhine tasu)",
    "set.show_feedback_icon": "Sõnumiikoon paneeli päises",
    "set.show_five_hour": "Kuva 5-tunni seanss",
    "set.show_local_models": "Mudelitevaheline jaotus selle arvuti Claude Code'i logide põhjal",
    "set.show_model": "Kuva mudeli nädalalimiit (allikas claude.ai)",
    "set.show_model_list": "Teiste mudelite nädalalimiidid",
    "set.show_plan_badge": "Paketimärk päises (Pro / Max…)",
    "set.show_plan_name": "Kuva märgil minu nimi",
    "set.show_reset": "Pöördloendus lähtestuseni",
    "set.show_spark": "Trendikõver (sparkline)",
    "set.show_surfaces": "Limiidid keskkonna kaupa (Claude Code, ühendatud rakendused…)",
    "set.show_weekly": "Kuva nädalalimiit",
    "set.size": "Suurus",
    "set.snap": "Haagi ekraani serva külge",
    "set.source_api": "claude.ai – kõik seadmed (vajab sisselogimist)",
    "set.source_label": "Mõõtmise allikas",
    "set.source_local": "Kohalik logi – ainult see arvuti",
    "set.tab_alerts": "Hoiatused",
    "set.tab_appearance": "Välimus",
    "set.tab_content": "Sisu",
    "set.tab_data": "Andmeallikas",
    "set.tab_details": "Üksikasjad",
    "set.tab_system": "Süsteem",
    "set.taskbar": "Kuva tegumiribal (aknana)",
    "set.theme": "Kujundus",
    "set.theme_default": "Kujunduse järgi",
    "set.tip": "Näpunäide: lohista paneeli hiire vasaku nupuga, Ctrl + kerimine muudab suurust,\nparemklõps = menüü, topeltklõps = ajalugu.",
    "set.title": "sätted",
    "set.tray_five": "5-tunni seanss",
    "set.tray_max": "Kumb on suurem",
    "set.tray_value": "Teavitusala ikooni väärtus",
    "set.tray_weekly": "Nädalalimiit",
    "set.update_check": "Otsi programmi värskendusi automaatselt",
    "set.version": "Versioon",
    "set.visible": "Hõljuv paneel nähtav",
    "set.warn": "Hoiatus",

    # --- size / source / theme options ---------------------------------------------------------
    "size.extra": "Väga suur",
    "size.large": "Suur",
    "size.normal": "Tavaline",
    "size.small": "Väike",
    "source.api": "claude.ai (kõik seadmed)",
    "source.local": "Kohalik (ainult see arvuti)",
    "theme.claude": "Claude (soe tume)",
    "theme.graphite": "Grafiit",
    "theme.midnight": "Kesköine klaas",
    "theme.neon": "Neoon",
    "theme.paper": "Hele paber",
    "theme.postit": "Märkmelehe kollane",

    # --- time units ----------------------------------------------------------------------------
    "time.day": "{} p",
    "time.dh": "{}p {}h",
    "time.hm": "{}h {}min",
    "time.hour": "{} h",
    "time.m": "{}min",
    "time.min": "{} min",
    "time.none": "andmeid pole",
    "time.sec": "{} s",

    # --- tray ----------------------------------------------------------------------------------
    "tray.head": "5h: {}%   ·   Nädal: {}%",
    "tray.line": "{}: {}%",

    # --- program update ------------------------------------------------------------------------
    "update.available": "Saadaval on versioon {}.",
    "update.check_failed": "Värskendusi ei õnnestunud otsida: {}",
    "update.check_now": "Otsi kohe",
    "update.checking": "Värskenduste otsimine…",
    "update.downloading": "Allalaadimine… {} / {}",
    "update.failed": "Värskendamine nurjus: {}",
    "update.install": "Installi kohe",
    "update.installed": "Installitud versioon: {}",
    "update.later": "Hiljem",
    "update.manual": "See koopia ei saa end ise värskendada (see töötab lähtekoodist või kirjutuskaitstud kaustast). Laadi selle asemel alla uus pakett.",
    "update.open_page": "Ava allalaadimisleht",
    "update.restarting": "Installimine – rakendus taaskäivitub kohe.",
    "update.skip": "Jäta see versioon vahele",
    "update.title": "Programmi värskendus",
    "update.uptodate": "Sul on uusim versioon.",
    "update.verifying": "Kontrollimine ja lahtipakkimine…",
    "update.whats_new": "Mis on uut",
}

# macOS wording (the four keys of source.json "mac"): "start at login" instead of "start with Windows", menu bar instead of tray
STRINGS_MAC = {
    "menu.autostart": "Ava sisselogimisel",
    "notify.autostart_on": "Sisse lülitatud: rakendus avaneb sisselogimisel.",
    "notify.autostart_off": "Välja lülitatud: rakendus ei avane sisselogimisel.",
    "notify.first_run": "Paneel ilmus ekraani paremasse ülanurka.\nMenüü avamiseks paremklõpsa paneelil või menüüriba ikoonil.",
}
