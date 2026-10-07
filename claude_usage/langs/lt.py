# -*- coding: utf-8 -*-
"""Lietuvių – UI strings of Claude Usage Monitor."""

CODE = "lt"
NAME = "Lietuvių"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{} d.",
    "backup.age_h": "{} val.",
    "backup.age_m": "{} min",
    "backup.and_more": "…ir dar {}",
    "backup.checked_at": "Patikrinta: {}",
    "backup.checking": "Tikrinama…",
    "backup.cloud_only": "Momentinė kopija OneDrive pasiekiama tik internete, todėl jos turinys nerodomas, kad jos nereikėtų atsisiųsti.",
    "backup.comp.cowork": "Cowork pokalbių žurnalai (po vieną ZIP kiekvienai sesijai)",
    "backup.comp.vault": "Obsidian saugyklos momentinė kopija (ZIP)",
    "backup.disclaimer_short": "Monitorius rodo tik tai, kas įrašyta atsarginių kopijų žurnaluose. Už atsargines kopijas neatsakome – ar jos išsamios ir ar jas galima atkurti, turite patikrinti patys.",
    "backup.done": "atlikta",
    "backup.dry_run": "(bandomasis paleidimas, nieko neįkelta)",
    "backup.failed": "NEPAVYKO",
    "backup.files_size": "Failų: {}, {}",
    "backup.folders": "Aplankai",
    "backup.label_age": "Pavadinimas ir senumas",
    "backup.label_name": "Tik pavadinimas",
    "backup.label_none": "Tik lemputės",
    "backup.last_ok": "Paskutinė sėkminga atsarginė kopija: {} (prieš {})",
    "backup.last_run": "Paskutinis paleidimas: {} – {}",
    "backup.legend": "Žalia: ne senesnė nei {} val. · Geltona: iki {} val. · Raudona: senesnė arba kopijos nėra",
    "backup.level_green": "Aktuali",
    "backup.level_none": "Atsarginės kopijos nerasta",
    "backup.level_red": "Pasenusi",
    "backup.level_yellow": "Sensta",
    "backup.log_file": "Žurnalo failas",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Atsarginių kopijų aplankas nerastas: {}",
    "backup.none_found": "Nėra.",
    "backup.open": "atidaryti",
    "backup.rc_copied": "nukopijuoti nauji arba pakeisti failai",
    "backup.rc_failed": "NEPAVYKO (kodas {})",
    "backup.rc_nochange": "viskas naujausia, nėra ką kopijuoti",
    "backup.recent_notes": "Paskiausiai redaguoti momentinės kopijos užrašai",
    "backup.refresh": "Tikrinti dabar",
    "backup.sec_components": "Kas kopijuojama",
    "backup.sec_contents": "Turinys",
    "backup.sec_log": "Žurnalas (paskutinės eilutės)",
    "backup.sec_problems": "Klaidos ir įspėjimai",
    "backup.sec_tasks": "Suplanuotos užduotys",
    "backup.skipped": "praleista (aplankas nerastas)",
    "backup.snap_kept": "Saugomų momentinių kopijų: {}, iš viso {}",
    "backup.snapshot": "Naujausia momentinė kopija",
    "backup.source": "Šaltinis",
    "backup.state_error": "baigta su klaidomis",
    "backup.state_interrupted": "nebaigta",
    "backup.state_ok": "sėkmingai baigta",
    "backup.state_running": "vykdoma dabar",
    "backup.storage": "Nuotolinė saugojimo vieta: užimta {} iš {}, laisva {}",
    "backup.target": "Paskirtis",
    "backup.task_event": "pagal įvykį",
    "backup.task_row": "paskutinis paleidimas {} · rezultatas {} · kitas {}",
    "backup.tip_click": "Spustelėkite, kad pamatytumėte daugiau",
    "backup.title": "Atsarginės kopijos",
    "backup.tray": "Atsarginės kopijos: {}",
    "backup.uploaded": "Įkelta šiuo paleidimu: naujų {}, pakeistų {}, klaidų {}",
    "backup.uploaded_files": "Įkelti failai",
    "backup.uploaded_groups": "Įkelti failai pagal aplankus",
    "backup.uploaded_no": "Įkelta į Nextcloud: dar ne",
    "backup.uploaded_yes": "Įkelta į Nextcloud: taip ({})",
    "backup.vault": "Saugykla",
    "backup.vault_changed": "Nuo šios momentinės kopijos saugykloje pakeista užrašų: {}",
    "backup.zip_new": "Naujų / atnaujintų ZIP: {}",
    "backup.zip_summary": "Failų: {} (užrašų: {}), išskleidus {}",

    # --- general ---------------------------------------------------------------------------
    "detail.extra": "Naudojimo kreditai",
    "detail.local_header": "CLAUDE CODE · ŠIS KOMPIUTERIS · ŠIOS SAVAITĖS PASISKIRSTYMAS",
    "detail.off": "išjungta",
    "detail.on": "įjungta",
    "detail.surface.oauth_apps": "Prijungtos programos",
    "detail.unlimited": "be limito",
    "dlg.cancel": "Atšaukti",
    "dlg.checking": "Tikrinama…",
    "dlg.err_badcode": "Kodas nepriimtas.\n\n{}\n\nPatikrinkite, ar įklijavote visą kodą, arba dar kartą prisijunkite per naršyklę (kodas kaskart naujas).",
    "dlg.err_ratelimit": "Per trumpą laiką per daug bandymų prisijungti.\n\nServeris laikinai apribojo prisijungimą. Uždarykite šį langą, palaukite 10–15 minučių (tuo metu nebandykite), tada pradėkite VIENĄ naują prisijungimą per naršyklę su nauju kodu.",
    "dlg.hint1": "Atsidariusiame puslapyje prisijunkite ir suteikite prieigą. Pabaigoje gausite kodą.",
    "dlg.intro": "Prisijunkite prie claude.ai paskyros savo naršyklėje (ten jau veikia jūsų išsaugoti slaptažodžiai ir prieigos raktai).",
    "dlg.login_title": "prisijungimas",
    "dlg.open_browser": "Prisijungti per naršyklę",
    "dlg.paste_label": "Čia įklijuokite gautą kodą:",
    "dlg.paste_placeholder": "įklijuokite kodą čia",
    "dlg.signin": "Prisijungti",
    "dlg.step1": "1 veiksmas",
    "dlg.step2": "2 veiksmas",
    "dlg.unknown_err": "Nežinoma klaida.",

    # --- error messages ---------------------------------------------------------------------
    "err.already_running": "Programa jau veikia (patikrinkite pranešimų sritį).",
    "err.bad_token_resp": "netinkamas žetono galinio taško atsakymas",
    "err.bad_usage_resp": "netinkamas naudojimo duomenų galinio taško atsakymas",
    "err.connection": "ryšio klaida: {}",
    "err.file_empty": "Naudojimo failas tuščias.",
    "err.file_not_found": "Naudojimo failas nerastas.\nAr veikia Claude Desktop?",
    "err.file_unreadable": "Naudojimo failo šiuo metu nepavyksta perskaityti.",
    "err.loading": "Prisijungiama / gaunami duomenys…",
    "err.network": "tinklo klaida: {}",
    "err.no_code": "Kodas neįklijuotas.",
    "err.no_data_profile": "Šiam profiliui duomenų nėra.",
    "err.no_tray": "Pranešimų sritis nepasiekiama, todėl piktograma nerodoma.",
    "err.no_usage_data": "Naudojimo duomenų nėra.",
    "err.not_signed_in": "Neprisijungta.",
    "err.query_http": "Užklausos klaida (HTTP {}).",
    "err.rate_limited": "Serveris riboja užklausas (429) – automatiškai bandoma dar kartą.",
    "err.session_expired": "Seansas baigėsi, prisijunkite iš naujo.",
    "err.session_expired_nl": "Seansas baigėsi.\nPrisijunkite iš naujo.",
    "err.signin_needed": "Prisijungimas prie claude.ai nebegalioja.\nPrisijunkite iš naujo: dešinysis spustelėjimas → Prisijungti prie claude.ai",
    "err.unexpected": "Netikėta klaida: {}",

    # --- 'Message to the developer' window ---------------------------------------------------
    "fb.cancel": "Atšaukti",
    "fb.close": "Uždaryti",
    "fb.consent": "Perskaičiau ir sutinku su {}.",
    "fb.email": "El. paštas",
    "fb.email_hint": "tik jei norite atsakymo",
    "fb.err_consent": "Kad galėtumėte išsiųsti, sutikite su privatumo politika.",
    "fb.err_email": "Šis el. pašto adresas atrodo netinkamas.",
    "fb.err_empty": "Pirmiausia parašykite žinutę arba pasirinkite įvertinimą.",
    "fb.err_links": "Žinutėje per daug nuorodų.",
    "fb.err_network": "Nepavyko pasiekti claudeusagemonitor.com. Patikrinkite ryšį ir bandykite dar kartą.",
    "fb.err_rate": "Per trumpą laiką per daug žinučių – bandykite vėliau.",
    "fb.err_server": "Serveris šiuo metu negali priimti žinutės. Bandykite vėliau.",
    "fb.intro": "Turite idėją, radote klaidą ar programa tiesiog patinka? Parašykite. Kiekvieną žinutę skaitau aš pats – Vidovics Gábor, programos autorius.",
    "fb.message": "Žinutė",
    "fb.message_ph": "Kas veikia, kas ne, ko trūksta?",
    "fb.meta": "Kartu su žinute siunčiama: programos versija {0}, operacinė sistema ({1}), sąsajos kalba ({2}).",
    "fb.name": "Vardas",
    "fb.optional": "(neprivaloma)",
    "fb.privacy_hide": "Slėpti privatumo politiką",
    "fb.privacy_text": (
        "Duomenų valdytojas: Vidovics Gábor, fizinis asmuo (Vengrija), Claude Usage Monitor autorius. "
        "Visa privatumo politika pateikta svetainėje: https://claudeusagemonitor.com/#privacy\n\n"
        "Kas siunčiama: tai, ką čia įvedate, – vardas (neprivaloma), el. pašto adresas (neprivaloma), žinutė, "
        "įvertinimas žvaigždutėmis, – ir, kad suprasčiau kontekstą, programos versija, operacinės sistemos "
        "pavadinimas ir versija, sąsajos kalba bei išsiuntimo laikas. Serveris IP adresų nesaugo; piktnaudžiavimui "
        "išvengti jis naudoja tik kasdien kintančią maišos reikšmę, iš kurios adreso atkurti neįmanoma.\n\n"
        "Kodėl: kad galėčiau perskaityti jūsų žinutę, į ją atsakyti ir tobulinti programą (teisėtas interesas, "
        "BDAR 6 str. 1 d. f p.; pats atsakymas – jūsų prašymu). Jūsų įvertinimas ir vardas svetainėje rodomi tik "
        "tuo atveju, jei tam pažymite atskirą langelį (sutikimas, 6 str. 1 d. a p.), ir tik autoriui juos "
        "peržiūrėjus; šį sutikimą galite bet kada atšaukti.\n\n"
        "Kiek laiko: žinutės saugomos ne ilgiau kaip 2 metus; paskelbtas įvertinimas – kol atšauksite sutikimą. "
        "Jei autorius yra įjungęs el. laiškų persiuntimą, kopija patenka ir į autoriaus pašto dėžutę.\n\n"
        "Kas mato: tik duomenų valdytojas ir, kaip duomenų tvarkytojas, prieglobos paslaugų teikėjas (serveris "
        "ES, Vokietijoje). Duomenys neparduodami ir niekam neperduodami; profiliavimas ir automatizuotas "
        "sprendimų priėmimas netaikomi.\n\n"
        "Jūsų teisės: susipažinti su duomenimis, juos ištaisyti, ištrinti, apriboti jų tvarkymą, nesutikti su "
        "tvarkymu, atšaukti sutikimą ir pateikti skundą priežiūros institucijai (Vengrijoje – NAIH, naih.hu) arba "
        "savo šalies institucijai (Lietuvoje – Valstybinei duomenų apsaugos inspekcijai). Kontaktai: ši forma "
        "arba svetainė.\n\n"
        "Perdavimas: šifruotu ryšiu (HTTPS/TLS) į claudeusagemonitor.com. Šios informacijos versija: 2026-10-06."
    ),
    "fb.privacy_title": "Privatumo politika",
    "fb.publish": "Mano įvertinimas ir vardas (jei nurodytas) gali būti rodomi claudeusagemonitor.com svetainėje.",
    "fb.rating": "Bendras įvertinimas",
    "fb.rating_clear": "išvalyti",
    "fb.rating_hint": "neprivaloma – spustelėkite žvaigždutę",
    "fb.rating_tip": "{} iš 5",
    "fb.secure": "Šifruotas ryšys (HTTPS) su claudeusagemonitor.com.",
    "fb.send": "Siųsti",
    "fb.sending": "Siunčiama…",
    "fb.sent": "Ačiū – gauta!",
    "fb.sent_sub": "Skaitau kiekvieną žinutę. Jei nurodėte el. pašto adresą, atsakysiu ten.",
    "fb.title": "Žinutė kūrėjui",

    # --- Help window -------------------------------------------------------------------------
    "help.disclaimer": "Nepriklausomas nemokamas įrankis – jo nesukūrė Anthropic ir jis nėra su Anthropic susijęs. „Claude“ yra Anthropic prekių ženklas.",
    "help.feedback": "Klausimai, idėjos, pranešimai apie klaidas: žinučių forma svetainėje.",
    "help.free": "Visada nemokama · MIT licencija · atvirasis kodas · jokios telemetrijos",
    "help.guide": (
        "\n"
        "<h2>Ką rodo valdiklis</h2>\n"
        "<ul>\n"
        "<li><b>5 val. sesija</b> – kiek išnaudota dabartinės sesijos limito. Jis atsinaujina kas penkias valandas; valdiklis rodo, kiek laiko liko iki atsinaujinimo.</li>\n"
        "<li><b>Savaitės limitas</b> – visų modelių naudojimas kartu; jis atsinaujina kiekvieną savaitę jūsų paskyrai nustatytu laiku.</li>\n"
        "<li><b>Modelio savaitės limitas</b> – trečias matuoklis, jei serveris tokį limitą pateikia (pvz., konkrečiam modeliui).</li>\n"
        "<li><b>Tempas ir naudojimo sparta</b> – kaip greitai naudojate limitą ir ar jo užteks iki atsinaujinimo; savaitės pabaigos prognozė įspėja laiku.</li>\n"
        "<li><b>Naudojimo kreditai</b> ir jūsų plano ženklelis – jei juos įjungiate meniu <i>Plano ženklelis ir papildomi limitai</i>.</li>\n"
        "</ul>\n"
        "<h2>Iš kur gaunami duomenys</h2>\n"
        "<ul>\n"
        "<li><b>claude.ai (visi įrenginiai)</b> – užklausiamas Anthropic serveris, todėl įskaičiuojamas ir naudojimas telefone, naršyklėje bei kituose kompiuteriuose. Reikia vieną kartą prisijungti savo naršyklėje (meniu: <i>Prisijungti</i>). Duomenys atnaujinami kas 2 minutes, rečiau – jei to prašo serveris.</li>\n"
        "<li><b>Vietinis (tik šis kompiuteris)</b> – nuskaitomas šiame kompiuteryje esantis Claude Desktop naudojimo žurnalas. Prisijungti nereikia, bet matomas tik šis kompiuteris.</li>\n"
        "</ul>\n"
        "<p>Šaltinį galima perjungti meniu: <i>Duomenų šaltinis</i>.</p>\n"
        "<h2>Kaip naudotis valdikliu</h2>\n"
        "<ul>\n"
        "<li><b>Spustelėkite dešiniuoju pelės mygtuku</b> valdiklį (arba pranešimų srities piktogramą) – atsivers visas meniu.</li>\n"
        "<li><b>Dukart spustelėkite</b> matuoklį – atsivers <b>Istorijos</b> langas: 6 valandos, 24 valandos, 7 dienos arba viskas, su maksimumais, dienos vidurkiu ir prognoze.</li>\n"
        "<li><b>Vilkite</b>, kad perkeltumėte; valdiklis prisitraukia prie ekrano kraštų. <b>Ctrl + pelės ratukas</b> – didinti arba mažinti.</li>\n"
        "<li>Išdėstymai: lipnus lapelis, siaura juosta, žiedai; 6 temos. <i>Užrakinti padėtį</i> ir <i>Praleisti spustelėjimus</i> rasite Parametruose.</li>\n"
        "</ul>\n"
        "<h2>Įspėjimai</h2>\n"
        "<p>Geltona nuo 70 %, raudona nuo 90 % (galima keisti). Galima įjungti ir pranešimus, kai limitas atsinaujina ir kai duomenys pasensta.</p>\n"
        "<h2>Atsarginės kopijos (neprivaloma)</h2>\n"
        "<p>Mažos lemputės rodo, ar suplanuotas atsarginis kopijavimas buvo paleistas ir baigtas. Spustelėkite lemputę, kad pamatytumėte išsamią informaciją. Monitorius tik skaito atsarginių kopijų žurnalus – sukurti ir išbandyti kopijas turite patys (žr. Naudojimo sąlygas).</p>\n"
        "<h2>Naujinimai</h2>\n"
        "<p>Programa pati ieško naujų versijų ir atsinaujina vienu spustelėjimu. Kiekvienas paketas tikrinamas pagal SHA-256 ir atsisiunčiamas tik iš <b>claudeusagemonitor.com</b>. Naujos versijos ir jų aprašai: {site}</p>\n"
        "<h2>Privatumas</h2>\n"
        "<p>Jokios telemetrijos, jokio sekimo. Prisijungimo prie claude.ai duomenys saugomi užšifruoti tik šiame kompiuteryje; niekur kitur nieko nesiunčiama.</p>\n"
        "<h2>Jei kas nors negerai</h2>\n"
        "<ul>\n"
        "<li><i>429 / užklausos ribojamos</i> – serveris lėtina užklausas; programa pati bandys dar kartą.</li>\n"
        "<li>Nėra duomenų – patikrinkite <i>Duomenų šaltinį</i>; jei naudojate claude.ai, prisijunkite iš naujo.</li>\n"
        "<li>Istorija saugoma 7 dienas ir išlieka paleidus programą iš naujo bei ją atnaujinus.</li>\n"
        "<li>Žurnalai ir parametrai: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Sukūrė",
    "help.moved": "Naujas adresas nuo 2026 m. rugsėjo 21 d. – ankstesnis dinorr.hu/claude-usage-monitor puslapis nukreipia čia.",
    "help.official": "OFICIALI SVETAINĖ",
    "help.open_site": "Atidaryti claudeusagemonitor.com",
    "help.privacy": "Privatumo politika",
    "help.site_what": "Atsisiuntimai, automatiniai naujinimai, naujienos, Claude Backup Kit, naudojimo sąlygos ir privatumas – viskas vienoje vietoje.",
    "help.source_code": "Pirminis kodas (GitHub)",
    "help.tab_author": "Autorius",
    "help.tab_guide": "Kaip tai veikia",
    "help.terms": "Naudojimo sąlygos",
    "help.title": "Žinynas",
    "help.version": "Versija",

    # --- History window ----------------------------------------------------------------------
    "hist.legend_5h": "5 val. sesija",
    "hist.legend_week": "savaitės limitas",
    "hist.no_data": "Šiam laikotarpiui nepakanka duomenų.",
    "hist.range_24h": "24 valandos",
    "hist.range_6h": "6 valandos",
    "hist.range_7d": "7 dienos",
    "hist.range_all": "Viskas",
    "hist.stat_burn": "Vidutiniškai per dieną",
    "hist.stat_forecast": "Savaitės pabaigos prognozė",
    "hist.stat_now": "Dabartinė savaitė",
    "hist.stat_peak": "Savaitės maksimumas",
    "hist.stat_sessions": "5 val. sesijos",
    "hist.title": "istorija",

    # --- layout names ------------------------------------------------------------------------
    "layout.compact": "Siaura juosta",
    "layout.postit": "Lipnus lapelis",
    "layout.ring": "Žiedai",

    # --- context menu ------------------------------------------------------------------------
    "menu.always_top": "Visada viršuje",
    "menu.autostart": "Paleisti kartu su „Windows“",
    "menu.backup_bar": "Atsarginių kopijų būsenos juosta",
    "menu.backups": "Atsarginės kopijos…",
    "menu.check_update": "Ieškoti programos naujinimų…",
    "menu.click_through": "Praleisti spustelėjimus",
    "menu.details": "Plano ženklelis ir papildomi limitai",
    "menu.feedback": "Žinutė kūrėjui…",
    "menu.help": "Žinynas…",
    "menu.history": "Istorija ir statistika…",
    "menu.language": "Kalba",
    "menu.layout": "Išdėstymas",
    "menu.locked": "Užrakinti padėtį",
    "menu.login": "Prisijungti (claude.ai, naršyklė)…",
    "menu.logout": "Atsijungti",
    "menu.model_gauge": "{} matuoklis",
    "menu.order": "Tvarka",
    "menu.panel_visible": "Rodyti skydelį",
    "menu.quit": "Išeiti",
    "menu.refresh": "Atnaujinti naudojimo duomenis dabar",
    "menu.settings": "Parametrai…",
    "menu.size": "Dydis",
    "menu.source": "Duomenų šaltinis",
    "menu.start_menu": "Rodyti meniu „Pradžia“",
    "menu.theme": "Tema",
    "menu.update_available": "Programos naujinimas: įdiegti versiją {}…",

    # --- desktop notifications ---------------------------------------------------------------
    "notify.autostart_fail": "Nepavyko nustatyti automatinio paleidimo.",
    "notify.autostart_off": "Išjungta: programa nebus paleidžiama kartu su „Windows“.",
    "notify.autostart_on": "Įjungta: programa bus paleidžiama kartu su „Windows“.",
    "notify.first_run": "Skydelis atsirado viršutiniame dešiniajame kampe.\nSpustelėkite skydelį ar pranešimų srities piktogramą dešiniuoju pelės mygtuku – atsivers meniu.",
    "notify.login_ok": "Prisijungta – gaunami serverio duomenys.",
    "notify.logout": "Atsijungta. Perjungta į vietinį šaltinį.",
    "notify.reset_done": "{}: limitas atsinaujino – prasidėjo naujas laikotarpis.",
    "notify.signin_needed": "Prisijungimas prie claude.ai nebegalioja. Spustelėkite skydelį dešiniuoju pelės mygtuku ir prisijunkite iš naujo, kad toliau matytumėte naudojimą visuose savo įrenginiuose.",
    "notify.stale_body": "Paskutinis matavimas atliktas prieš {}. Ar veikia Claude Desktop?",
    "notify.stale_title": "Pasenę duomenys",
    "notify.threshold": "{}: išnaudota {} %.",
    "notify.update": "Galima įdiegti programos versiją {}. Dešinysis spustelėjimas skydelyje → Programos naujinimas.",

    # --- floating panel labels (tight space, UPPERCASE) -------------------------------------
    "panel.five_hour": "5 VAL. SESIJA",
    "panel.five_hour_short": "5 VAL.",
    "panel.full_in": "pilna po {}",
    "panel.model": "{} SAVAITĖ",
    "panel.no_data": "Nėra duomenų",
    "panel.pace": "tempas {}",
    "panel.per_day": "{}%/d.",
    "panel.per_hour": "{}%/val.",
    "panel.refreshing": "atnaujinama",
    "panel.reset": "liko {}",
    "panel.retry_in": "vėl po {} s",
    "panel.updated": "atnaujinta: {}",
    "panel.week_short": "SAV.",
    "panel.weekly": "SAVAITĖS LIMITAS",

    # --- profile -----------------------------------------------------------------------------
    "profile.extra": "Naudojimo kreditai: {}",
    "profile.plan": "Planas: {}",
    "profile.since": "Narys nuo: {}",
    "profile.tier": "Ribojimo lygis: {}",

    # --- Settings window ---------------------------------------------------------------------
    "set.about": "{}\nJokios telemetrijos. Programa iš Anthropic gauna tik jūsų pačių naudojimo duomenis ir iš naujinimų serverio nuskaito versijos numerį.",
    "set.accent": "Akcento spalva",
    "set.always_top": "Virš visų kitų langų",
    "set.auto": "automatiškai",
    "set.backup_config": "Kopijavimo scenarijaus konfigūracija",
    "set.backup_details": "Išsamios informacijos lange rodoma",
    "set.backup_disclaimer": "Claude Usage Monitor tik nuskaito ir rodo jūsų atsarginio kopijavimo žurnalus – jis nekuria, netikrina ir negarantuoja jokių atsarginių kopijų. Claude Backup Kit – nemokamas pradinis rinkinys, siūlomas kaip pagalba: scenarijus gali pakeisti bet kas, todėl atsarginės kopijos kokybės ir išsamumo garantuoti neįmanoma. Neprisiimame jokios atsakomybės už atsargines kopijas, prarastus duomenis ar bet kokią žalą. Kiekvienas pats atsako už tai, kad jo atsarginės kopijos būtų išsamios ir jas būtų galima atkurti, – retkarčiais išbandykite atkūrimą.",
    "set.backup_disclaimer_h": "Atsakomybės apribojimas",
    "set.backup_enabled": "Rodyti atsarginių kopijų būsenos juostą skydelyje",
    "set.backup_found": "Rasta: {}",
    "set.backup_green": "Žalia iki",
    "set.backup_label": "Tekstas šalia lemputės",
    "set.backup_lamps": "Lemputės",
    "set.backup_root": "Atsarginių kopijų aplankas",
    "set.backup_tasks": "Suplanuotų užduočių filtras",
    "set.backup_unconfigured": "Atsarginių kopijų aplankas nenurodytas, todėl būsenos juosta nerodoma. Pasirinkite aplanką, į kurį rašo jūsų kopijavimo scenarijus.",
    "set.backup_yellow": "Geltona iki",
    "set.browse": "Naršyti…",
    "set.click_through": "Praleisti spustelėjimus (tik dekoracija, į pelę nereaguoja)",
    "set.close": "Uždaryti",
    "set.color_hint": "Spalvos keičiasi pagal ribas: žalia → geltona → raudona.",
    "set.danger": "Pavojus",
    "set.data_hint": "Vietinis žurnalas: Claude Desktop failas plan-usage-history.json. Prisijungti nereikia, bet matuojamas tik šis kompiuteris, o duomenys atnaujinami maždaug kas 5 minutes.\n\nclaude.ai: prisijungus užklausiamas serveris. Matote naudojimą visuose savo įrenginiuose, tikslų atsinaujinimo laiką, o duomenys atnaujinami dažniau.",
    "set.datafile": "Duomenų failas",
    "set.default": "Numatytoji",
    "set.details_api_only": "Šie duomenys gaunami iš claude.ai duomenų šaltinio (reikia prisijungti); vietiniame žurnale jų nėra.",
    "set.file_filter": "JSON (*.json);;Visi failai (*.*)",
    "set.gauge_order": "Matuoklių tvarka",
    "set.hours_suffix": " val.",
    "set.layout": "Išdėstymas",
    "set.local_models_hint": "Serveris atskirą skaitiklį turi tik kai kuriems modeliams (pvz., Fable). Kitiems čia rodoma, kaip šią savaitę šiame kompiuteryje pasiskirstė jūsų darbas su Claude Code – jūsų pačių naudojimo dalis ir išvesties žetonai, o ne limito dalis. Nuskaitomi tik modelio pavadinimas ir žetonų skaičiai, pokalbiai – niekada.",
    "set.local_models_none": "Claude Code žurnalų aplankas nerastas – ši grupė tiesiog nerodoma. Visa kita veikia įprastai.",
    "set.local_models_path": "Claude Code žurnalų aplankas",
    "set.lock": "Užrakinti padėtį (negalima vilkti)",
    "set.login_btn_in": "Atsijungti nuo claude.ai",
    "set.login_btn_out": "Prisijungti prie claude.ai…",
    "set.model_filter": "Stebimas modelis",
    "set.model_scale": "Modelio matuoklio dydis",
    "set.not_set": "nenurodyta",
    "set.notify_enabled": "Pranešti peržengus ribą",
    "set.notify_reset": "Pranešti, kai limitas atsinaujina",
    "set.notify_stale": "Pranešti, kai duomenys pasensta",
    "set.opacity": "Nepermatomumas",
    "set.open_config": "Atidaryti parametrų aplanką",
    "set.pick_color": "Pasirinkti spalvą…",
    "set.pick_file_title": "Pasirinkite naudojimo žurnalą",
    "set.profile": "Profilis / paskyra",
    "set.profile_auto": "Automatinis (paskutinis naudotas)",
    "set.profile_n": "Profilis {} – …{}",
    "set.refresh": "Atnaujinti",
    "set.reset_confirm": "Ar tikrai norite atkurti numatytuosius parametrus?",
    "set.restore": "Atkurti numatytuosius",
    "set.rows_available": "Ką galima rodyti dabar – nuimkite žymę nuo to, ko nenorite matyti:",
    "set.rows_none": "Šiuo metu serveris jūsų paskyrai daugiau limitų nesiunčia. Kai tik atsiųs, jie čia atsiras patys.",
    "set.sec_suffix": " s",
    "set.show_age": "Duomenų naujumas",
    "set.show_burn": "Naudojimo sparta (%/val., %/d.)",
    "set.show_extra_usage": "Naudojimo kreditai (mokama pagal naudojimą)",
    "set.show_feedback_icon": "Žinutės piktograma skydelio antraštėje",
    "set.show_five_hour": "Rodyti 5 val. sesiją",
    "set.show_local_models": "Pasiskirstymas tarp modelių pagal Claude Code žurnalus šiame kompiuteryje",
    "set.show_model": "Rodyti modelio savaitės limitą (claude.ai šaltinis)",
    "set.show_model_list": "Kitų modelių savaitės limitai",
    "set.show_plan_badge": "Plano ženklelis antraštėje (Pro / Max…)",
    "set.show_plan_name": "Rodyti mano vardą ženklelyje",
    "set.show_reset": "Atgalinis skaičiavimas iki atsinaujinimo",
    "set.show_spark": "Tendencijos kreivė (mini diagrama)",
    "set.show_surfaces": "Limitai pagal aplinką (Claude Code, prijungtos programos…)",
    "set.show_weekly": "Rodyti savaitės limitą",
    "set.size": "Dydis",
    "set.snap": "Pritraukti prie ekrano krašto",
    "set.source_api": "claude.ai – visi įrenginiai (reikia prisijungti)",
    "set.source_label": "Matavimo šaltinis",
    "set.source_local": "Vietinis žurnalas – tik šis kompiuteris",
    "set.tab_alerts": "Įspėjimai",
    "set.tab_appearance": "Išvaizda",
    "set.tab_content": "Turinys",
    "set.tab_data": "Duomenų šaltinis",
    "set.tab_details": "Išsami informacija",
    "set.tab_system": "Sistema",
    "set.taskbar": "Rodyti užduočių juostoje (kaip langą)",
    "set.theme": "Tema",
    "set.theme_default": "Pagal temą",
    "set.tip": "Patarimas: skydelį vilkite kairiuoju pelės mygtuku, Ctrl + ratukas keičia dydį,\ndešinysis spustelėjimas – meniu, dvikartis spustelėjimas – istorija.",
    "set.title": "parametrai",
    "set.tray_five": "5 val. sesija",
    "set.tray_max": "Kuris didesnis",
    "set.tray_value": "Pranešimų srities piktogramos reikšmė",
    "set.tray_weekly": "Savaitės limitas",
    "set.update_check": "Automatiškai ieškoti programos naujinimų",
    "set.version": "Versija",
    "set.visible": "Rodyti slankųjį skydelį",
    "set.warn": "Įspėjimas",

    # --- menu options ------------------------------------------------------------------------
    "size.extra": "Ypač didelis",
    "size.large": "Didelis",
    "size.normal": "Įprastas",
    "size.small": "Mažas",
    "source.api": "claude.ai (visi įrenginiai)",
    "source.local": "Vietinis (tik šis kompiuteris)",
    "theme.claude": "Claude (šilta tamsi)",
    "theme.graphite": "Grafitas",
    "theme.midnight": "Vidurnakčio stiklas",
    "theme.neon": "Neonas",
    "theme.paper": "Šviesus popierius",
    "theme.postit": "Lipnaus lapelio geltona",

    # --- time units (VLKK abbreviations) -----------------------------------------------------
    "time.day": "{} d.",
    "time.dh": "{} d. {} val.",
    "time.hm": "{} val. {} min",
    "time.hour": "{} val.",
    "time.m": "{} min",
    "time.min": "{} min",
    "time.none": "nėra duomenų",
    "time.sec": "{} s",

    # --- tray --------------------------------------------------------------------------------
    "tray.head": "5 val.: {}%   ·   Sav.: {}%",
    "tray.line": "{}: {}%",

    # --- program update ----------------------------------------------------------------------
    "update.available": "Galima įdiegti versiją {}.",
    "update.check_failed": "Nepavyko patikrinti naujinimų: {}",
    "update.check_now": "Tikrinti dabar",
    "update.checking": "Ieškoma naujinimų…",
    "update.downloading": "Atsisiunčiama… {} iš {}",
    "update.failed": "Naujinimas nepavyko: {}",
    "update.install": "Įdiegti dabar",
    "update.installed": "Įdiegta versija: {}",
    "update.later": "Vėliau",
    "update.manual": "Ši kopija negali atsinaujinti pati (ji paleista iš pirminio kodo arba iš aplanko, į kurį negalima rašyti). Atsisiųskite naują paketą.",
    "update.open_page": "Atidaryti atsisiuntimo puslapį",
    "update.restarting": "Diegiama – netrukus programa bus paleista iš naujo.",
    "update.skip": "Praleisti šią versiją",
    "update.title": "Programos naujinimas",
    "update.uptodate": "Naudojate naujausią versiją.",
    "update.verifying": "Tikrinama ir išpakuojama…",
    "update.whats_new": "Kas naujo",
}

# macOS wording: "Atidaryti prisijungus" (Apple login items) and the menu bar instead of the notification area
STRINGS_MAC = {
    "menu.autostart": "Atidaryti prisijungus",
    "notify.autostart_on": "Įjungta: programa bus atidaroma jums prisijungus.",
    "notify.autostart_off": "Išjungta: programa nebus atidaroma prisijungus.",
    "notify.first_run": "Skydelis atsirado viršutiniame dešiniajame kampe.\nSpustelėkite skydelį ar meniu juostos piktogramą dešiniuoju pelės mygtuku – atsivers meniu.",
}
