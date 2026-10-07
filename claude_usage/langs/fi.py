# -*- coding: utf-8 -*-
"""Suomi – UI strings of Claude Usage Monitor."""

CODE = "fi"
NAME = "Suomi"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{}pv",
    "backup.age_h": "{}h",
    "backup.age_m": "{}min",
    "backup.and_more": "…ja {} muuta",
    "backup.checked_at": "Tarkistettu: {}",
    "backup.checking": "Tarkistetaan…",
    "backup.cloud_only": "Tilannevedos on OneDrivessa saatavilla vain verkossa; sen sisältöä ei luetella, jotta sitä ei tarvitse ladata.",
    "backup.comp.cowork": "Cowork-keskustelulokit (oma ZIP jokaisesta istunnosta)",
    "backup.comp.vault": "Obsidian-holvin tilannevedos (ZIP)",
    "backup.disclaimer_short": "Ohjelma näyttää vain sen, mitä varmuuskopioinnin lokit kertovat. Emme vastaa varmuuskopioista – sinun on itse tarkistettava, että ne ovat täydellisiä ja palautettavissa.",
    "backup.done": "valmis",
    "backup.dry_run": "(testiajo, mitään ei siirretty)",
    "backup.failed": "EPÄONNISTUI",
    "backup.files_size": "{} tiedostoa, {}",
    "backup.folders": "Kansiot",
    "backup.label_age": "Nimi ja ikä",
    "backup.label_name": "Vain nimi",
    "backup.label_none": "Vain merkkivalot",
    "backup.last_ok": "Viimeisin onnistunut varmuuskopio: {} ({} sitten)",
    "backup.last_run": "Viimeisin ajo: {} – {}",
    "backup.legend": "Vihreä: enintään {} h vanha · Keltainen: enintään {} h · Punainen: vanhempi tai ei varmuuskopiota",
    "backup.level_green": "Tuore",
    "backup.level_none": "Varmuuskopiota ei löytynyt",
    "backup.level_red": "Vanhentunut",
    "backup.level_yellow": "Vanhenemassa",
    "backup.log_file": "Lokitiedosto",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Varmuuskopiokansiota ei löytynyt: {}",
    "backup.none_found": "Ei mitään.",
    "backup.open": "avaa",
    "backup.rc_copied": "uudet tai muuttuneet tiedostot kopioitu",
    "backup.rc_failed": "EPÄONNISTUI (koodi {})",
    "backup.rc_nochange": "ajan tasalla, ei kopioitavaa",
    "backup.recent_notes": "Tilannevedoksen viimeksi muokatut muistiinpanot",
    "backup.refresh": "Tarkista nyt",
    "backup.sec_components": "Mitä varmuuskopioidaan",
    "backup.sec_contents": "Sisältö",
    "backup.sec_log": "Loki (viimeiset rivit)",
    "backup.sec_problems": "Virheet ja varoitukset",
    "backup.sec_tasks": "Ajoitetut tehtävät",
    "backup.skipped": "ohitettu (kansiota ei löytynyt)",
    "backup.snap_kept": "Säilytettyjä tilannevedoksia: {}, yhteensä {}",
    "backup.snapshot": "Uusin tilannevedos",
    "backup.source": "Lähde",
    "backup.state_error": "päättyi virheisiin",
    "backup.state_interrupted": "jäi kesken",
    "backup.state_ok": "valmistui onnistuneesti",
    "backup.state_running": "käynnissä nyt",
    "backup.storage": "Etätallennustila: käytössä {} / {}, vapaana {}",
    "backup.target": "Kohde",
    "backup.task_event": "tapahtuman yhteydessä",
    "backup.task_row": "viimeisin ajo {} · tulos {} · seuraava {}",
    "backup.tip_click": "Näytä tiedot napsauttamalla",
    "backup.title": "Varmuuskopiot",
    "backup.tray": "Varmuuskopiot: {}",
    "backup.uploaded": "Tässä ajossa siirretty: {} uutta, {} korvattua, {} virhettä",
    "backup.uploaded_files": "Siirretyt tiedostot",
    "backup.uploaded_groups": "Siirretyt tiedostot kansioittain",
    "backup.uploaded_no": "Siirretty Nextcloudiin: ei vielä",
    "backup.uploaded_yes": "Siirretty Nextcloudiin: kyllä ({})",
    "backup.vault": "Holvi",
    "backup.vault_changed": "Muuttuneita muistiinpanoja holvissa tämän tilannevedoksen jälkeen: {}",
    "backup.zip_new": "Uusia tai päivitettyjä ZIP-tiedostoja: {}",
    "backup.zip_summary": "{} tiedostoa ({} muistiinpanoa), pakkaamattomana {}",

    # --- general -----------------------------------------------------------------------------
    "detail.extra": "Käyttökrediitit",
    "detail.local_header": "CLAUDE CODE · TÄMÄ KONE · TÄMÄN VIIKON JAKAUMA",
    "detail.off": "ei käytössä",
    "detail.on": "käytössä",
    "detail.surface.oauth_apps": "Yhdistetyt sovellukset",
    "detail.unlimited": "ei rajaa",
    "dlg.cancel": "Peruuta",
    "dlg.checking": "Tarkistetaan…",
    "dlg.err_badcode": "Koodia ei hyväksytty.\n\n{}\n\nVarmista, että liitit koko koodin, tai kirjaudu uudelleen selaimessa (tarvitset aina uuden koodin).",
    "dlg.err_ratelimit": "Liian monta kirjautumisyritystä lyhyessä ajassa.\n\nPalvelin rajoittaa yrityksiäsi tilapäisesti. Sulje tämä ikkuna, odota 10–15 minuuttia (älä yritä sillä välin) ja aloita sitten YKSI uusi kirjautuminen selaimessa uudella koodilla.",
    "dlg.hint1": "Kirjaudu sisään avautuvalla sivulla ja hyväksy käyttöoikeus. Lopuksi saat koodin.",
    "dlg.intro": "Kirjaudu claude.ai-tiliisi omassa selaimessasi (tallennetut salasanasi ja pääsyavaimesi toimivat siellä jo).",
    "dlg.login_title": "kirjautuminen",
    "dlg.open_browser": "Avaa kirjautuminen selaimessa",
    "dlg.paste_label": "Liitä saamasi koodi tähän:",
    "dlg.paste_placeholder": "liitä koodi tähän",
    "dlg.signin": "Kirjaudu sisään",
    "dlg.step1": "Vaihe 1",
    "dlg.step2": "Vaihe 2",
    "dlg.unknown_err": "Tuntematon virhe.",

    # --- error messages ----------------------------------------------------------------------
    "err.already_running": "Sovellus on jo käynnissä (katso ilmoitusalueelta).",
    "err.bad_token_resp": "virheellinen vastaus tunnuksen päätepisteestä",
    "err.bad_usage_resp": "virheellinen vastaus käyttötietojen päätepisteestä",
    "err.connection": "yhteysvirhe: {}",
    "err.file_empty": "Käyttötiedosto on tyhjä.",
    "err.file_not_found": "Käyttötiedostoa ei löytynyt.\nOnko Claude Desktop käynnissä?",
    "err.file_unreadable": "Käyttötiedostoa ei voi juuri nyt lukea.",
    "err.loading": "Kirjaudutaan / haetaan tietoja…",
    "err.network": "verkkovirhe: {}",
    "err.no_code": "Koodia ei liitetty.",
    "err.no_data_profile": "Tälle profiilille ei ole tietoja.",
    "err.no_tray": "Ilmoitusalue ei ole käytettävissä, joten kuvaketta ei näytetä.",
    "err.no_usage_data": "Ei käyttötietoja.",
    "err.not_signed_in": "Et ole kirjautunut sisään.",
    "err.query_http": "Kyselyvirhe (HTTP {}).",
    "err.rate_limited": "Palvelin rajoittaa pyyntöjä (429) – yritetään automaattisesti uudelleen.",
    "err.session_expired": "Istunto on vanhentunut, kirjaudu sisään uudelleen.",
    "err.session_expired_nl": "Istunto on vanhentunut.\nKirjaudu sisään uudelleen.",
    "err.signin_needed": "claude.ai-kirjautuminen on vanhentunut.\nKirjaudu uudelleen: kakkospainike → Kirjaudu sisään (claude.ai, selain)",
    "err.unexpected": "Odottamaton virhe: {}",

    # --- 'Message to the developer' window ---------------------------------------------------
    "fb.cancel": "Peruuta",
    "fb.close": "Sulje",
    "fb.consent": "Olen lukenut ja hyväksyn: {}.",
    "fb.email": "Sähköposti",
    "fb.email_hint": "vain jos haluat vastauksen",
    "fb.err_consent": "Hyväksy tietosuojaseloste, jotta voit lähettää viestin.",
    "fb.err_email": "Tämä sähköpostiosoite ei näytä oikealta.",
    "fb.err_empty": "Kirjoita ensin viesti tai valitse arvio.",
    "fb.err_links": "Viestissä on liikaa linkkejä.",
    "fb.err_network": "Sivustoon claudeusagemonitor.com ei saatu yhteyttä. Tarkista verkkoyhteys ja yritä uudelleen.",
    "fb.err_rate": "Liian monta viestiä lyhyessä ajassa – yritä myöhemmin uudelleen.",
    "fb.err_server": "Palvelin ei juuri nyt voinut vastaanottaa viestiä. Yritä myöhemmin uudelleen.",
    "fb.intro": "Idea, virhe vai pidätkö vain ohjelmasta? Kerro minulle. Luen jokaisen viestin itse – Vidovics Gábor, ohjelman tekijä.",
    "fb.message": "Viesti",
    "fb.message_ph": "Mikä toimii, mikä ei, mitä puuttuu?",
    "fb.meta": "Viestin mukana lähetetään: ohjelman versio {0}, käyttöjärjestelmä ({1}) ja käyttöliittymän kieli ({2}).",
    "fb.name": "Nimi",
    "fb.optional": "(valinnainen)",
    "fb.privacy_hide": "Piilota seloste",
    "fb.privacy_text": (
        "Rekisterinpitäjä: Vidovics Gábor, yksityishenkilö (Unkari), Claude Usage Monitorin tekijä. "
        "Koko tietosuojaseloste on verkkosivustolla: https://claudeusagemonitor.com/#privacy\n\n"
        "Mitä lähetetään: tähän kirjoittamasi tiedot – nimi (valinnainen), sähköpostiosoite (valinnainen), "
        "viesti ja tähtiarvio – sekä asiayhteyden ymmärtämiseksi ohjelman versio, käyttöjärjestelmän nimi ja "
        "versio, käyttöliittymän kieli ja lähetysaika. Palvelin ei tallenna IP-osoitetta; väärinkäytösten "
        "estämiseksi se käyttää vain päivittäin vaihtuvaa tiivistettä, josta osoitetta ei voi palauttaa.\n\n"
        "Miksi: jotta voin lukea viestisi ja vastata siihen sekä kehittää ohjelmaa – käsittelyperusteena "
        "oikeutettu etu, tietosuoja-asetuksen (GDPR) 6 artiklan 1 kohdan f alakohta; itse vastaus annetaan "
        "pyynnöstäsi. Arviosi ja nimesi näytetään verkkosivustolla vain, jos valitset sitä varten erillisen "
        "valintaruudun (suostumus, 6 artiklan 1 kohdan a alakohta), ja vasta kun tekijä on tarkistanut ne; "
        "voit peruuttaa suostumuksesi milloin tahansa.\n\n"
        "Kuinka kauan: viestejä säilytetään enintään 2 vuotta ja julkaistua arviota siihen asti, kunnes "
        "peruutat suostumuksesi. Jos tekijä on ottanut sähköpostin edelleenlähetyksen käyttöön, kopio menee "
        "myös tekijän sähköpostilaatikkoon.\n\n"
        "Kuka tiedot näkee: vain rekisterinpitäjä sekä henkilötietojen käsittelijänä toimiva palvelintilan "
        "tarjoaja (palvelin EU:ssa, Saksassa). Mitään ei myydä eikä luovuteta eteenpäin; profilointia tai "
        "automaattista päätöksentekoa ei ole.\n\n"
        "Oikeutesi: oikeus saada pääsy tietoihin, oikeus tietojen oikaisemiseen ja poistamiseen, oikeus "
        "käsittelyn rajoittamiseen, oikeus vastustaa käsittelyä, oikeus peruuttaa suostumus sekä oikeus "
        "tehdä valitus valvontaviranomaiselle (Unkarissa NAIH, naih.hu) tai oman maasi "
        "valvontaviranomaiselle (Suomessa tietosuojavaltuutettu). Yhteydenotot: tämä lomake tai verkkosivusto.\n\n"
        "Siirto: salattuna (HTTPS/TLS) sivustoon claudeusagemonitor.com. Tämän selosteen versio: 6.10.2026."
    ),
    "fb.privacy_title": "Tietosuojaseloste",
    "fb.publish": "Arvioni ja nimeni (jos annoin sen) saa näyttää sivustolla claudeusagemonitor.com.",
    "fb.rating": "Yleisarvio",
    "fb.rating_clear": "tyhjennä",
    "fb.rating_hint": "valinnainen – napsauta tähteä",
    "fb.rating_tip": "{}/5",
    "fb.secure": "Salattu yhteys (HTTPS) sivustoon claudeusagemonitor.com.",
    "fb.send": "Lähetä",
    "fb.sending": "Lähetetään…",
    "fb.sent": "Kiitos – viesti on perillä!",
    "fb.sent_sub": "Luen jokaisen viestin. Jos annoit sähköpostiosoitteen, vastaan siihen.",
    "fb.title": "Viesti kehittäjälle",

    # --- Help window -------------------------------------------------------------------------
    "help.disclaimer": "Itsenäinen, ilmainen työkalu – Anthropic ei ole tehnyt sitä, eikä se ole sidoksissa Anthropiciin. ”Claude” on Anthropicin tavaramerkki.",
    "help.feedback": "Kysymykset, ideat ja virheilmoitukset: viestilomake verkkosivustolla.",
    "help.free": "Ikuisesti ilmainen · MIT-lisenssi · avoin lähdekoodi · ei telemetriaa",
    "help.guide": (
        "\n<h2>Mitä paneeli näyttää</h2>\n"
        "<ul>\n"
        "<li><b>5 tunnin istunto</b> – kuinka suuri osa nykyisen istunnon rajasta on käytetty. Raja nollautuu "
        "viiden tunnin välein; paneeli laskee aikaa nollaukseen.</li>\n"
        "<li><b>Viikkoraja</b> – kaikkien mallien käyttö yhteensä; se nollautuu tilisi kiinteänä viikoittaisena "
        "ajankohtana.</li>\n"
        "<li><b>Mallikohtainen viikkoraja</b> – kolmas mittari, kun palvelin ilmoittaa sellaisen (esim. "
        "tietylle mallille).</li>\n"
        "<li><b>Tahti ja kulutusnopeus</b> – kuinka nopeasti käytät rajaa ja riittääkö se nollaukseen asti; "
        "viikon lopun ennuste varoittaa ajoissa.</li>\n"
        "<li><b>Käyttökrediitit</b> ja tilausmerkki – kun otat ne käyttöön kohdassa <i>Tilausmerkki ja "
        "lisärajat</i>.</li>\n"
        "</ul>\n"
        "<h2>Mistä tiedot tulevat</h2>\n"
        "<ul>\n"
        "<li><b>claude.ai (kaikki laitteet)</b> – kysyy tiedot Anthropicin palvelimelta, joten mukana on myös "
        "puhelimella, selaimessa ja muilla tietokoneilla kertynyt käyttö. Vaatii kertaluonteisen kirjautumisen "
        "omassa selaimessasi (valikko: <i>Kirjaudu sisään</i>). Päivittyy 2 minuutin välein, harvemmin, jos "
        "palvelin niin pyytää.</li>\n"
        "<li><b>Paikallinen (vain tämä tietokone)</b> – lukee tämän tietokoneen Claude Desktopin käyttölokia. "
        "Kirjautumista ei tarvita, mutta se tuntee vain tämän tietokoneen.</li>\n"
        "</ul>\n"
        "<p>Voit vaihtaa niiden välillä valikossa: <i>Tietolähde</i>.</p>\n"
        "<h2>Paneelin käyttö</h2>\n"
        "<ul>\n"
        "<li><b>Napsauta hiiren kakkospainikkeella</b> paneelia (tai ilmoitusalueen kuvaketta) – koko "
        "valikko avautuu.</li>\n"
        "<li><b>Kaksoisnapsauta</b> mittaria – avautuu <b>Historia</b>-ikkuna: 6 tuntia, 24 tuntia, 7 päivää tai "
        "kaikki, huippuineen, päivittäisine keskiarvoineen ja ennusteineen.</li>\n"
        "<li><b>Vedä</b> paneeli haluamaasi kohtaan; se kiinnittyy näytön reunoihin. <b>Ctrl + hiiren "
        "rulla</b> – suurenna tai pienennä.</li>\n"
        "<li>Asettelut: post-it-lappu, kapea palkki, renkaat; 6 teemaa. <i>Lukitse sijainti</i> ja "
        "<i>Läpinapsautus</i> löytyvät asetuksista.</li>\n"
        "</ul>\n"
        "<h2>Hälytykset</h2>\n"
        "<p>Keltainen 70 %:sta, punainen 90 %:sta (säädettävissä). Halutessasi saat ilmoituksen, kun raja "
        "nollautuu ja kun tiedot alkavat vanhentua.</p>\n"
        "<h2>Varmuuskopiot (valinnainen)</h2>\n"
        "<p>Pienet merkkivalot näyttävät, ovatko ajoitetut varmuuskopiosi käynnistyneet ja valmistuneet. "
        "Napsauta merkkivaloa, niin näet tiedot. Ohjelma vain lukee varmuuskopioinnin lokeja – varmuuskopioiden "
        "tekeminen ja testaaminen on sinun tehtäväsi (katso käyttöehdot).</p>\n"
        "<h2>Päivitykset</h2>\n"
        "<p>Ohjelma tarkistaa uudet versiot itse ja päivittyy yhdellä napsautuksella. Jokainen paketti "
        "tarkistetaan SHA-256:lla, ja paketit tulevat ainoastaan osoitteesta <b>claudeusagemonitor.com</b>. "
        "Uudet versiot ja julkaisutiedot: {site}</p>\n"
        "<h2>Tietosuoja</h2>\n"
        "<p>Ei telemetriaa, ei seurantaa. claude.ai-kirjautuminen tallennetaan salattuna vain tälle "
        "tietokoneelle; mitään ei lähetetä muualle.</p>\n"
        "<h2>Jos jokin ei toimi</h2>\n"
        "<ul>\n"
        "<li><i>429 / pyyntöjä rajoitettu</i> – palvelin hidastaa pyyntöjä; ohjelma yrittää itse "
        "uudelleen.</li>\n"
        "<li>Ei tietoja – tarkista <i>Tietolähde</i>; jos käytät claude.ai:ta, kirjaudu uudelleen.</li>\n"
        "<li>Historia säilyy 7 päivää, myös uudelleenkäynnistysten ja päivitysten yli.</li>\n"
        "<li>Lokit ja asetukset: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Ohjelman tekijä",
    "help.moved": "Uusi osoite 21.9.2026 alkaen – entinen dinorr.hu/claude-usage-monitor-sivu ohjaa tänne.",
    "help.official": "VIRALLINEN VERKKOSIVUSTO",
    "help.open_site": "Avaa claudeusagemonitor.com",
    "help.privacy": "Tietosuojaseloste",
    "help.site_what": "Lataukset, automaattiset päivitykset, uutuudet, Claude Backup Kit, käyttöehdot ja tietosuoja – kaikki yhdessä paikassa.",
    "help.source_code": "Lähdekoodi (GitHub)",
    "help.tab_author": "Tekijä",
    "help.tab_guide": "Näin se toimii",
    "help.terms": "Käyttöehdot",
    "help.title": "Ohje",
    "help.version": "Versio",

    # --- History window ----------------------------------------------------------------------
    "hist.legend_5h": "5 tunnin istunto",
    "hist.legend_week": "viikkoraja",
    "hist.no_data": "Tältä ajanjaksolta ei ole tarpeeksi tietoja.",
    "hist.range_24h": "24 tuntia",
    "hist.range_6h": "6 tuntia",
    "hist.range_7d": "7 päivää",
    "hist.range_all": "Kaikki",
    "hist.stat_burn": "Keskikulutus päivässä",
    "hist.stat_forecast": "Ennuste viikon loppuun",
    "hist.stat_now": "Viikkokäyttö nyt",
    "hist.stat_peak": "Viikon huippu",
    "hist.stat_sessions": "5 tunnin istunnot",
    "hist.title": "historia",

    # --- layout names ------------------------------------------------------------------------
    "layout.compact": "Kapea palkki",
    "layout.postit": "Post-it-lappu",
    "layout.ring": "Renkaat",

    # --- context menu ------------------------------------------------------------------------
    "menu.always_top": "Aina päällimmäisenä",
    "menu.autostart": "Käynnistä Windowsin mukana",
    "menu.backup_bar": "Varmuuskopioiden tilarivi",
    "menu.backups": "Varmuuskopiot…",
    "menu.check_update": "Tarkista ohjelmapäivitykset…",
    "menu.click_through": "Läpinapsautus",
    "menu.details": "Tilausmerkki ja lisärajat",
    "menu.feedback": "Viesti kehittäjälle…",
    "menu.help": "Ohje…",
    "menu.history": "Historia ja tilastot…",
    "menu.language": "Kieli",
    "menu.layout": "Asettelu",
    "menu.locked": "Lukitse sijainti",
    "menu.login": "Kirjaudu sisään (claude.ai, selain)…",
    "menu.logout": "Kirjaudu ulos",
    "menu.model_gauge": "{}-mittari",
    "menu.order": "Järjestys",
    "menu.panel_visible": "Näytä paneeli",
    "menu.quit": "Lopeta",
    "menu.refresh": "Päivitä käyttötiedot nyt",
    "menu.settings": "Asetukset…",
    "menu.size": "Koko",
    "menu.source": "Tietolähde",
    "menu.start_menu": "Näytä Käynnistä-valikossa",
    "menu.theme": "Teema",
    "menu.update_available": "Ohjelmapäivitys: asenna versio {}…",

    # --- desktop notifications ---------------------------------------------------------------
    "notify.autostart_fail": "Automaattista käynnistystä ei voitu ottaa käyttöön.",
    "notify.autostart_off": "Ei käytössä: sovellus ei käynnisty Windowsin mukana.",
    "notify.autostart_on": "Käytössä: sovellus käynnistyy Windowsin mukana.",
    "notify.first_run": "Paneeli ilmestyi näytön oikeaan yläkulmaan.\nValikko: napsauta paneelia tai ilmoitusalueen kuvaketta hiiren kakkospainikkeella.",
    "notify.login_ok": "Kirjauduit sisään – tiedot haetaan palvelimelta.",
    "notify.logout": "Kirjauduit ulos. Tietolähteeksi vaihdettiin paikallinen loki.",
    "notify.reset_done": "{}: nollautui — uusi jakso alkoi.",
    "notify.signin_needed": "claude.ai-kirjautuminen on vanhentunut. Napsauta paneelia hiiren kakkospainikkeella ja kirjaudu uudelleen, niin näet edelleen kaikkien laitteidesi käytön.",
    "notify.stale_body": "Viimeisin lukema on {} vanha. Onko Claude Desktop käynnissä?",
    "notify.stale_title": "Vanhentuneet tiedot",
    "notify.threshold": "{}: {} % käytetty.",
    "notify.update": "Ohjelman versio {} on saatavilla. Napsauta paneelia hiiren kakkospainikkeella → Ohjelmapäivitys.",

    # --- panel labels (tight) ----------------------------------------------------------------
    "panel.five_hour": "5 TUNNIN ISTUNTO",
    "panel.five_hour_short": "5H",
    "panel.full_in": "täynnä {}",
    "panel.model": "{} VIIKKO",
    "panel.no_data": "Ei dataa",
    "panel.pace": "tahti {}",
    "panel.per_day": "{} %/pv",
    "panel.per_hour": "{} %/h",
    "panel.refreshing": "haetaan dataa",
    "panel.reset": "nollaus {}",
    "panel.retry_in": "uudelleen {} s",
    "panel.updated": "haettu: {}",
    "panel.week_short": "VKO",
    "panel.weekly": "VIIKKORAJA",

    # --- profile -----------------------------------------------------------------------------
    "profile.extra": "Käyttökrediitit: {}",
    "profile.plan": "Tilaus: {}",
    "profile.since": "Liittynyt: {}",
    "profile.tier": "Rajoitustaso: {}",

    # --- Settings window ---------------------------------------------------------------------
    "set.about": "{}\nEi telemetriaa. Ohjelma kysyy Anthropicilta vain oman käyttösi ja lukee versionumeron päivityspalvelimelta.",
    "set.accent": "Korostusväri",
    "set.always_top": "Kaikkien muiden ikkunoiden päällä",
    "set.auto": "automaattinen",
    "set.backup_config": "Varmuuskopioskriptin asetustiedosto",
    "set.backup_details": "Tietoikkunassa näytetään",
    "set.backup_disclaimer": "Claude Usage Monitor vain lukee ja näyttää varmuuskopiointisi lokit – se ei tee, tarkista eikä takaa mitään varmuuskopiota. Claude Backup Kit on avuksi tarjottu ilmainen lähtökohta: kuka tahansa voi muuttaa skriptejä, joten varmuuskopioiden laatua ja täydellisyyttä ei voida taata. Emme vastaa varmuuskopioista, kadonneista tiedoista emmekä mistään vahingoista. Jokainen vastaa itse siitä, että varmuuskopiot ovat täydellisiä ja palautettavissa – kokeile palautusta aina välillä.",
    "set.backup_disclaimer_h": "Vastuuvapauslauseke",
    "set.backup_enabled": "Näytä varmuuskopioiden tilarivi paneelissa",
    "set.backup_found": "Löytyi: {}",
    "set.backup_green": "Vihreä enintään",
    "set.backup_label": "Teksti merkkivalon vieressä",
    "set.backup_lamps": "Merkkivalot",
    "set.backup_root": "Varmuuskopiokansio",
    "set.backup_tasks": "Ajoitettujen tehtävien suodatin",
    "set.backup_unconfigured": "Varmuuskopiokansiota ei ole määritetty, joten tilarivi pysyy piilossa. Valitse kansio, johon varmuuskopioskriptisi kirjoittaa.",
    "set.backup_yellow": "Keltainen enintään",
    "set.browse": "Selaa…",
    "set.click_through": "Läpinapsautus (vain koriste, ei reagoi hiireen)",
    "set.close": "Sulje",
    "set.color_hint": "Värit vaihtuvat kynnysarvojen mukaan: vihreä → keltainen → punainen.",
    "set.danger": "Kriittinen",
    "set.data_hint": "Paikallinen loki: Claude Desktopin plan-usage-history.json. Kirjautumista ei tarvita, mutta se mittaa vain tätä tietokonetta ja päivittyy noin 5 minuutin välein.\n\nclaude.ai: kirjautumisen jälkeen tiedot kysytään palvelimelta. Näet kaikkien laitteidesi käytön tarkkoine nollausaikoineen, ja tiedot päivittyvät useammin.",
    "set.datafile": "Käyttötiedosto",
    "set.default": "Oletus",
    "set.details_api_only": "Nämä tulevat claude.ai-tietolähteestä (vaatii kirjautumisen); paikallisessa lokissa niitä ei ole.",
    "set.file_filter": "JSON (*.json);;Kaikki tiedostot (*.*)",
    "set.gauge_order": "Mittarien järjestys",
    "set.hours_suffix": " h",
    "set.layout": "Asettelu",
    "set.local_models_hint": "Palvelin pitää erillistä laskuria vain joillekin malleille (esim. Fable). Muiden osalta tämä näyttää, miten tämän viikon Claude Code -työsi jakautuu tällä tietokoneella – osuuden omasta käytöstäsi ja tulostetokenit, ei osuutta rajasta. Ohjelma lukee vain mallin nimen ja tokenimäärät, ei koskaan keskustelua.",
    "set.local_models_none": "Claude Code -lokikansiota ei löytynyt – tämä ryhmä jää vain piiloon. Muuhun tämä ei vaikuta.",
    "set.local_models_path": "Claude Code -lokikansio",
    "set.lock": "Lukitse sijainti (ei voi vetää)",
    "set.login_btn_in": "Kirjaudu ulos claude.ai-palvelusta",
    "set.login_btn_out": "Kirjaudu claude.ai-palveluun…",
    "set.model_filter": "Seurattava malli",
    "set.model_scale": "Mallimittarin koko",
    "set.not_set": "ei määritetty",
    "set.notify_enabled": "Ilmoita, kun kynnysarvo ylittyy",
    "set.notify_reset": "Ilmoita, kun raja nollautuu",
    "set.notify_stale": "Ilmoita, kun tiedot vanhentuvat",
    "set.opacity": "Peittävyys",
    "set.open_config": "Avaa asetuskansio",
    "set.pick_color": "Valitse väri…",
    "set.pick_file_title": "Valitse käyttöloki",
    "set.profile": "Profiili / tili",
    "set.profile_auto": "Automaattinen (viimeksi käytetty)",
    "set.profile_n": "Profiili {} – …{}",
    "set.refresh": "Päivitä",
    "set.reset_confirm": "Haluatko varmasti palauttaa oletusasetukset?",
    "set.restore": "Palauta oletukset",
    "set.rows_available": "Nämä voidaan näyttää juuri nyt – poista valinta niistä, joita et halua nähdä:",
    "set.rows_none": "Palvelin ei tällä hetkellä lähetä tilillesi muita rajoja. Ne tulevat tähän näkyviin itsestään heti, kun palvelin lähettää niitä.",
    "set.sec_suffix": " s",
    "set.show_age": "Tietojen tuoreus",
    "set.show_burn": "Kulutusnopeus (%/tunti, %/päivä)",
    "set.show_extra_usage": "Käyttökrediitit (käytön mukaan laskutettavat)",
    "set.show_feedback_icon": "Viestikuvake paneelin otsikossa",
    "set.show_five_hour": "Näytä 5 tunnin istunto",
    "set.show_local_models": "Jakauma mallien kesken tämän tietokoneen Claude Code -lokeista",
    "set.show_model": "Näytä mallin viikkoraja (claude.ai-lähde)",
    "set.show_model_list": "Muiden mallien viikkorajat",
    "set.show_plan_badge": "Tilausmerkki otsikossa (Pro / Max…)",
    "set.show_plan_name": "Näytä nimeni merkissä",
    "set.show_reset": "Aika nollaukseen",
    "set.show_spark": "Trendikäyrä (sparkline)",
    "set.show_surfaces": "Käyttöympäristökohtaiset rajat (Claude Code, yhdistetyt sovellukset…)",
    "set.show_weekly": "Näytä viikkoraja",
    "set.size": "Koko",
    "set.snap": "Kiinnitä näytön reunaan",
    "set.source_api": "claude.ai – kaikki laitteet (vaatii kirjautumisen)",
    "set.source_label": "Mittauksen lähde",
    "set.source_local": "Paikallinen loki – vain tämä tietokone",
    "set.tab_alerts": "Hälytykset",
    "set.tab_appearance": "Ulkoasu",
    "set.tab_content": "Sisältö",
    "set.tab_data": "Tietolähde",
    "set.tab_details": "Lisätiedot",
    "set.tab_system": "Järjestelmä",
    "set.taskbar": "Näytä tehtäväpalkissa (ikkunana)",
    "set.theme": "Teema",
    "set.theme_default": "Teeman oletus",
    "set.tip": "Vinkki: vedä paneelia hiiren vasemmalla painikkeella, Ctrl+rulla muuttaa kokoa,\nkakkospainike = valikko, kaksoisnapsautus = historia.",
    "set.title": "asetukset",
    "set.tray_five": "5 tunnin istunto",
    "set.tray_max": "Suurempi kahdesta",
    "set.tray_value": "Ilmoitusalueen kuvakkeen arvo",
    "set.tray_weekly": "Viikkoraja",
    "set.update_check": "Tarkista ohjelmapäivitykset automaattisesti",
    "set.version": "Versio",
    "set.visible": "Kelluva paneeli näkyvissä",
    "set.warn": "Varoitus",

    # --- menu options --------------------------------------------------------------------------
    "size.extra": "Erittäin suuri",
    "size.large": "Suuri",
    "size.normal": "Normaali",
    "size.small": "Pieni",
    "source.api": "claude.ai (kaikki laitteet)",
    "source.local": "Paikallinen (vain tämä tietokone)",
    "theme.claude": "Claude (lämmin tumma)",
    "theme.graphite": "Grafiitti",
    "theme.midnight": "Keskiyön lasi",
    "theme.neon": "Neon",
    "theme.paper": "Vaalea paperi",
    "theme.postit": "Post-it-keltainen",

    # --- time units (panel) ------------------------------------------------------------------
    "time.day": "{} pv",
    "time.dh": "{}pv {}h",
    "time.hm": "{}h {}min",
    "time.hour": "{} h",
    "time.m": "{}min",
    "time.min": "{} min",
    "time.none": "ei dataa",
    "time.sec": "{} s",

    # --- tray --------------------------------------------------------------------------------
    "tray.head": "5 h: {} %  ·  Vko: {} %",
    "tray.line": "{}: {} %",

    # --- program update ----------------------------------------------------------------------
    "update.available": "Versio {} on saatavilla.",
    "update.check_failed": "Päivitysten tarkistus epäonnistui: {}",
    "update.check_now": "Tarkista nyt",
    "update.checking": "Tarkistetaan päivityksiä…",
    "update.downloading": "Ladataan… {} / {}",
    "update.failed": "Päivitys epäonnistui: {}",
    "update.install": "Asenna nyt",
    "update.installed": "Asennettu versio: {}",
    "update.later": "Myöhemmin",
    "update.manual": "Tämä kopio ei voi päivittää itseään (se suoritetaan lähdekoodista tai kirjoitussuojatusta kansiosta). Lataa sen sijaan uusi paketti.",
    "update.open_page": "Avaa lataussivu",
    "update.restarting": "Asennetaan – sovellus käynnistyy hetken kuluttua uudelleen.",
    "update.skip": "Ohita tämä versio",
    "update.title": "Ohjelmapäivitys",
    "update.uptodate": "Sinulla on uusin versio.",
    "update.verifying": "Tarkistetaan ja puretaan…",
    "update.whats_new": "Mitä uutta",
}

# macOS wording (the four keys of source.json "mac"): "start at login" instead of "start with Windows", menu bar instead of tray
STRINGS_MAC = {
    "menu.autostart": "Avaa kirjautuessa",
    "notify.autostart_on": "Käytössä: sovellus avautuu, kun kirjaudut sisään.",
    "notify.autostart_off": "Ei käytössä: sovellus ei avaudu kirjautuessa.",
    "notify.first_run": "Paneeli ilmestyi näytön oikeaan yläkulmaan.\nValikko: osoita toissijaisesti paneelia tai valikkorivin kuvaketta.",
}
