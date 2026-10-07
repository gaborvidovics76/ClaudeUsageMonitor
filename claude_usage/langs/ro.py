# -*- coding: utf-8 -*-
"""Română – UI strings of Claude Usage Monitor."""

CODE = "ro"
NAME = "Română"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{}z",
    "backup.age_h": "{}h",
    "backup.age_m": "{}min",
    "backup.and_more": "…și încă {}",
    "backup.checked_at": "Verificat: {}",
    "backup.checking": "Se verifică…",
    "backup.cloud_only": "Instantaneul este disponibil doar online în OneDrive; conținutul lui nu este listat, ca să nu fie nevoie de descărcare.",
    "backup.comp.cowork": "Jurnalele conversațiilor Cowork (câte un ZIP pe sesiune)",
    "backup.comp.vault": "Instantaneu al seifului Obsidian (ZIP)",
    "backup.disclaimer_short": "Monitorul afișează doar ce scrie în jurnalele de backup. Nu ne asumăm nicio răspundere pentru backupuri – e responsabilitatea ta să verifici dacă sunt complete și pot fi restaurate.",
    "backup.done": "finalizat",
    "backup.dry_run": "(rulare de test, nu s-a încărcat nimic)",
    "backup.failed": "EȘUAT",
    "backup.files_size": "fișiere: {}, {}",
    "backup.folders": "Foldere",
    "backup.label_age": "Nume și vechime",
    "backup.label_name": "Doar numele",
    "backup.label_none": "Doar ledurile",
    "backup.last_ok": "Ultimul backup reușit: {} (acum {})",
    "backup.last_run": "Ultima rulare: {} – {}",
    "backup.legend": "Verde: cel mult {} h · Galben: până la {} h · Roșu: mai vechi sau fără backup",
    "backup.level_green": "Recent",
    "backup.level_none": "Niciun backup găsit",
    "backup.level_red": "Învechit",
    "backup.level_yellow": "Se învechește",
    "backup.log_file": "Fișier jurnal",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Folderul de backup nu a fost găsit: {}",
    "backup.none_found": "Niciunul.",
    "backup.open": "deschide",
    "backup.rc_copied": "fișierele noi sau modificate au fost copiate",
    "backup.rc_failed": "EȘUAT (cod {})",
    "backup.rc_nochange": "la zi, nimic de copiat",
    "backup.recent_notes": "Notițele editate cel mai recent din instantaneu",
    "backup.refresh": "Verifică acum",
    "backup.sec_components": "Ce se salvează",
    "backup.sec_contents": "Conținut",
    "backup.sec_log": "Jurnal (ultimele rânduri)",
    "backup.sec_problems": "Erori și avertismente",
    "backup.sec_tasks": "Activități planificate",
    "backup.skipped": "omis (folderul nu a fost găsit)",
    "backup.snap_kept": "Instantanee păstrate: {}, în total {}",
    "backup.snapshot": "Cel mai recent instantaneu",
    "backup.source": "Sursă",
    "backup.state_error": "s-a încheiat cu erori",
    "backup.state_interrupted": "nu s-a încheiat",
    "backup.state_ok": "s-a încheiat cu succes",
    "backup.state_running": "rulează acum",
    "backup.storage": "Spațiu de stocare la distanță: utilizat {} din {}, liber {}",
    "backup.target": "Destinație",
    "backup.task_event": "la eveniment",
    "backup.task_row": "ultima rulare {} · rezultat {} · următoarea {}",
    "backup.tip_click": "Dă clic pentru detalii",
    "backup.title": "Backupuri",
    "backup.tray": "Backupuri: {}",
    "backup.uploaded": "Încărcate în această rulare: noi {}, înlocuite {}, erori {}",
    "backup.uploaded_files": "Fișiere încărcate",
    "backup.uploaded_groups": "Fișiere încărcate, pe foldere",
    "backup.uploaded_no": "Încărcat în Nextcloud: încă nu",
    "backup.uploaded_yes": "Încărcat în Nextcloud: da ({})",
    "backup.vault": "Seif",
    "backup.vault_changed": "Note modificate în seif de la acest instantaneu: {}",
    "backup.zip_new": "ZIP noi/actualizate: {}",
    "backup.zip_summary": "Fișiere: {} (note: {}), dimensiune necomprimată: {}",

    # --- general -----------------------------------------------------------------------------
    "detail.extra": "Credite de utilizare",
    "detail.local_header": "CLAUDE CODE · ACEST PC · REPARTIZAREA DIN SĂPTĂMÂNA ACEASTA",
    "detail.off": "dezactivat",
    "detail.on": "activat",
    "detail.surface.oauth_apps": "Aplicații conectate",
    "detail.unlimited": "fără limită",
    "dlg.cancel": "Anulează",
    "dlg.checking": "Se verifică…",
    "dlg.err_badcode": "Codul nu a fost acceptat.\n\n{}\n\nVerifică dacă ai lipit codul complet sau încearcă din nou conectarea din browser (de fiecare dată cu un cod nou).",
    "dlg.err_ratelimit": "Prea multe încercări de conectare într-un timp scurt.\n\nServerul te limitează temporar. Închide această fereastră, așteaptă 10–15 minute (nu încerca între timp), apoi pornește O SINGURĂ conectare nouă din browser, cu un cod nou.",
    "dlg.hint1": "Conectează-te pe pagina care se deschide și aprobă accesul. La final vei primi un cod.",
    "dlg.intro": "Conectează-te la contul tău claude.ai în browserul tău (parolele și cheile de acces salvate funcționează deja acolo).",
    "dlg.login_title": "conectare",
    "dlg.open_browser": "Deschide conectarea în browser",
    "dlg.paste_label": "Lipește aici codul primit:",
    "dlg.paste_placeholder": "lipește codul aici",
    "dlg.signin": "Conectare",
    "dlg.step1": "Pasul 1",
    "dlg.step2": "Pasul 2",
    "dlg.unknown_err": "Eroare necunoscută.",

    # --- error messages ----------------------------------------------------------------------
    "err.already_running": "Aplicația rulează deja (verifică zona de notificare).",
    "err.bad_token_resp": "răspuns nevalid de la punctul final pentru token",
    "err.bad_usage_resp": "răspuns nevalid de la punctul final pentru utilizare",
    "err.connection": "eroare de conexiune: {}",
    "err.file_empty": "Fișierul de utilizare este gol.",
    "err.file_not_found": "Fișierul de utilizare nu a fost găsit.\nEste pornit Claude Desktop?",
    "err.file_unreadable": "Fișierul de utilizare nu poate fi citit momentan.",
    "err.loading": "Conectare / interogare în curs…",
    "err.network": "eroare de rețea: {}",
    "err.no_code": "Nu ai lipit niciun cod.",
    "err.no_data_profile": "Nu există date pentru acest profil.",
    "err.no_tray": "Zona de notificare nu este disponibilă; pictograma nu va fi afișată.",
    "err.no_usage_data": "Nu există date de utilizare.",
    "err.not_signed_in": "Nu ești conectat.",
    "err.query_http": "Eroare la interogare (HTTP {}).",
    "err.rate_limited": "Serverul limitează solicitările (429) – se reîncearcă automat.",
    "err.session_expired": "Sesiunea a expirat, conectează-te din nou.",
    "err.session_expired_nl": "Sesiunea a expirat.\nConectează-te din nou.",
    "err.signin_needed": "Conectarea la claude.ai a expirat.\nConectează-te din nou: clic dreapta → Conectare la claude.ai",
    "err.unexpected": "Eroare neașteptată: {}",

    # --- 'Message to the developer' window ---------------------------------------------------
    "fb.cancel": "Anulează",
    "fb.close": "Închide",
    "fb.consent": "Am citit și accept {}.",
    "fb.email": "Adresă de e-mail",
    "fb.email_hint": "doar dacă vrei un răspuns",
    "fb.err_consent": "Pentru a trimite mesajul, acceptă Politica de confidențialitate.",
    "fb.err_email": "Adresa de e-mail nu pare corectă.",
    "fb.err_empty": "Scrie mai întâi un mesaj sau alege o evaluare.",
    "fb.err_links": "Mesajul conține prea multe linkuri.",
    "fb.err_network": "Nu s-a putut accesa claudeusagemonitor.com. Verifică-ți conexiunea și încearcă din nou.",
    "fb.err_rate": "Prea multe mesaje într-un timp scurt – încearcă din nou mai târziu.",
    "fb.err_server": "Serverul nu a putut primi mesajul acum. Încearcă din nou mai târziu.",
    "fb.intro": "Ai o idee, ai găsit o eroare sau pur și simplu îți place programul? Spune-mi. Citesc personal fiecare mesaj – sunt Vidovics Gábor, autorul.",
    "fb.message": "Mesaj",
    "fb.message_ph": "Ce funcționează, ce nu, ce lipsește?",
    "fb.meta": "Împreună cu mesajul se trimit: versiunea programului {0}, sistemul de operare ({1}), limba interfeței ({2}).",
    "fb.name": "Nume",
    "fb.optional": "(opțional)",
    "fb.privacy_hide": "Ascunde nota",
    "fb.privacy_text": (
        "Operator: Vidovics Gábor, persoană fizică (Ungaria), autorul aplicației Claude Usage Monitor. Politica de "
        "confidențialitate completă se află pe site: https://claudeusagemonitor.com/#privacy\n\n"
        "Ce se transmite: ceea ce scrii aici – numele (opțional), adresa de e-mail (opțional), mesajul, evaluarea "
        "cu stele – și, pentru a înțelege contextul: versiunea programului, numele și versiunea sistemului de "
        "operare, limba interfeței și momentul trimiterii. Serverul nu stochează adrese IP; pentru prevenirea "
        "abuzurilor folosește doar un hash care se schimbă zilnic și din care adresa nu poate fi reconstituită.\n\n"
        "De ce: pentru a citi mesajul tău și a-ți răspunde, precum și pentru a îmbunătăți programul (interes "
        "legitim, art. 6 alin. (1) lit. f) RGPD; răspunsul propriu-zis, la cererea ta). Evaluarea și numele tău "
        "apar pe site doar dacă bifezi caseta separată prevăzută pentru aceasta (consimțământ, art. 6 alin. (1) "
        "lit. a) RGPD) și numai după ce autorul le-a verificat; îți poți retrage oricând consimțământul.\n\n"
        "Cât timp: mesajele, cel mult 2 ani; o evaluare publicată, până la retragerea consimțământului. Dacă "
        "autorul a activat redirecționarea prin e-mail, o copie ajunge și în căsuța de e-mail a autorului.\n\n"
        "Cine are acces: doar operatorul și – în calitate de persoană împuternicită de operator – furnizorul de "
        "găzduire (server în UE, în Germania). Nimic nu este vândut sau transmis mai departe; nu se creează "
        "profiluri și nu se iau decizii automatizate.\n\n"
        "Drepturile tale: dreptul de acces, la rectificare, la ștergere, la restricționarea prelucrării, la "
        "opoziție, dreptul de a-ți retrage consimțământul și dreptul de a depune o plângere la o autoritate de "
        "supraveghere (în Ungaria: NAIH, naih.hu; în România: ANSPDCP, dataprotection.ro) sau la autoritatea din "
        "țara ta. Contact: acest formular sau site-ul.\n\n"
        "Transmitere: criptată (HTTPS/TLS) către claudeusagemonitor.com. Versiunea acestei note: 2026-10-06."
    ),
    "fb.privacy_title": "Politica de confidențialitate",
    "fb.publish": "Evaluarea și numele meu (dacă l-am completat) pot fi afișate pe claudeusagemonitor.com.",
    "fb.rating": "Evaluare generală",
    "fb.rating_clear": "șterge",
    "fb.rating_hint": "opțional – dă clic pe o stea",
    "fb.rating_tip": "{} din 5",
    "fb.secure": "Conexiune criptată (HTTPS) cu claudeusagemonitor.com.",
    "fb.send": "Trimite",
    "fb.sending": "Se trimite…",
    "fb.sent": "Mulțumesc – mesajul a ajuns!",
    "fb.sent_sub": "Citesc fiecare mesaj. Dacă ai lăsat o adresă de e-mail, îți răspund acolo.",
    "fb.title": "Mesaj către dezvoltator",

    # --- Help window -------------------------------------------------------------------------
    "help.disclaimer": "Un instrument independent și gratuit – nu este realizat de Anthropic și nici afiliat cu aceasta. „Claude” este o marcă comercială a Anthropic.",
    "help.feedback": "Întrebări, idei, raportări de erori: formularul de mesaje de pe site.",
    "help.free": "Gratuit pentru totdeauna · licență MIT · sursă deschisă · fără telemetrie",
    "help.guide": (
        "\n<h2>Ce afișează widgetul</h2>\n<ul>\n"
        "<li><b>Sesiune de 5 ore</b> – cât s-a consumat din limita sesiunii curente. Se resetează la fiecare cinci "
        "ore; widgetul face numărătoarea inversă până la resetare.</li>\n"
        "<li><b>Limită săptămânală</b> – utilizarea tuturor modelelor la un loc; se resetează săptămânal, la o oră "
        "fixă stabilită pentru contul tău.</li>\n"
        "<li><b>Limită săptămânală per model</b> – un al treilea indicator, când serverul raportează o astfel de "
        "limită (de ex. pentru un anumit model).</li>\n"
        "<li><b>Ritm și rată de consum</b> – cât de repede consumi limita și dacă îți ajunge până la resetare; "
        "estimarea pentru sfârșitul săptămânii te avertizează din timp.</li>\n"
        "<li><b>Credite de utilizare</b> și insigna planului – dacă le activezi în <i>Insigna planului și limite "
        "suplimentare</i>.</li>\n</ul>\n"
        "<h2>De unde provin datele</h2>\n<ul>\n"
        "<li><b>claude.ai (toate dispozitivele)</b> – interoghează serverul Anthropic, deci include și utilizarea "
        "de pe telefon, din browser și de pe alte computere. Necesită o singură conectare, în browserul tău "
        "(meniu: <i>Conectare</i>). Se reîmprospătează la fiecare 2 minute, mai rar dacă serverul cere asta.</li>\n"
        "<li><b>Local (doar acest PC)</b> – citește jurnalul de utilizare al aplicației Claude Desktop de pe acest computer. "
        "Nu necesită conectare, dar cunoaște doar acest PC.</li>\n</ul>\n"
        "<p>Comuți între ele din meniu: <i>Sursă de date</i>.</p>\n"
        "<h2>Utilizarea widgetului</h2>\n<ul>\n"
        "<li><b>Clic dreapta</b> pe widget (sau pe pictograma din zona de notificare) – meniul complet.</li>\n"
        "<li><b>Dublu clic</b> pe un indicator – fereastra <b>Istoric</b>: 6 ore, 24 de ore, 7 zile sau tot, cu "
        "vârfuri, medie zilnică și estimare.</li>\n"
        "<li><b>Trage</b> widgetul ca să-l muți; se fixează la marginile ecranului. <b>Ctrl + rotița "
        "mouse-ului</b> – mai mare sau mai mic.</li>\n"
        "<li>Dispuneri: card post-it, bară subțire, inele; 6 teme. <i>Blochează poziția</i> și <i>Transparent la "
        "clic</i> se găsesc în Setări.</li>\n</ul>\n"
        "<h2>Alerte</h2>\n"
        "<p>Galben de la 70 %, roșu de la 90 % (reglabil). Notificări opționale când o limită se resetează și când "
        "datele se învechesc.</p>\n"
        "<h2>Backupuri (opțional)</h2>\n"
        "<p>Ledurile mici arată dacă backupurile tale planificate au rulat și s-au încheiat. Dă clic pe un led "
        "pentru detalii. Monitorul doar citește jurnalele de backup – crearea și testarea backupurilor sunt "
        "responsabilitatea ta (vezi Condițiile de utilizare).</p>\n"
        "<h2>Actualizări</h2>\n"
        "<p>Programul caută singur versiuni noi și se actualizează cu un singur clic. Fiecare pachet este verificat "
        "cu SHA-256 și provine exclusiv de pe <b>claudeusagemonitor.com</b>. Versiuni noi și note de lansare: "
        "{site}</p>\n"
        "<h2>Confidențialitate</h2>\n"
        "<p>Fără telemetrie, fără urmărire. Conectarea la claude.ai este stocată criptat, doar pe acest computer; "
        "nimic nu este trimis în altă parte.</p>\n"
        "<h2>Dacă ceva nu merge</h2>\n<ul>\n"
        "<li><i>429 / limitare</i> – serverul încetinește solicitările; programul reîncearcă singur.</li>\n"
        "<li>Nu există date – verifică <i>Sursă de date</i>; pentru claude.ai, conectează-te din nou.</li>\n"
        "<li>Istoricul se păstrează 7 zile și rămâne și după reporniri și actualizări.</li>\n"
        "<li>Jurnale și setări: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Realizat de",
    "help.moved": "Adresă nouă din 21 septembrie 2026 – fosta pagină dinorr.hu/claude-usage-monitor redirecționează aici.",
    "help.official": "SITE OFICIAL",
    "help.open_site": "Deschide claudeusagemonitor.com",
    "help.privacy": "Politica de confidențialitate",
    "help.site_what": "Descărcări, actualizări automate, noutăți, Claude Backup Kit, condițiile de utilizare și confidențialitatea – totul într-un singur loc.",
    "help.source_code": "Cod sursă (GitHub)",
    "help.tab_author": "Autor",
    "help.tab_guide": "Cum funcționează",
    "help.terms": "Condiții de utilizare",
    "help.title": "Ajutor",
    "help.version": "Versiune",

    # --- History window ----------------------------------------------------------------------
    "hist.legend_5h": "sesiune de 5 ore",
    "hist.legend_week": "limită săptămânală",
    "hist.no_data": "Nu sunt destule date pentru această perioadă.",
    "hist.range_24h": "24 de ore",
    "hist.range_6h": "6 ore",
    "hist.range_7d": "7 zile",
    "hist.range_all": "Tot",
    "hist.stat_burn": "Consum mediu zilnic",
    "hist.stat_forecast": "Estimare pentru sfârșitul săptămânii",
    "hist.stat_now": "Utilizare săptămânală actuală",
    "hist.stat_peak": "Vârf săptămânal",
    "hist.stat_sessions": "Sesiuni de 5 ore",
    "hist.title": "istoric",

    # --- layouts -----------------------------------------------------------------------------
    "layout.compact": "Bară subțire",
    "layout.postit": "Card post-it",
    "layout.ring": "Inele",

    # --- context menu ------------------------------------------------------------------------
    "menu.always_top": "Întotdeauna deasupra",
    "menu.autostart": "Pornește odată cu Windows",
    "menu.backup_bar": "Bară de stare backup",
    "menu.backups": "Backupuri…",
    "menu.check_update": "Caută actualizări ale programului…",
    "menu.click_through": "Transparent la clic",
    "menu.details": "Insigna planului și limite suplimentare",
    "menu.feedback": "Mesaj către dezvoltator…",
    "menu.help": "Ajutor…",
    "menu.history": "Istoric și statistici…",
    "menu.language": "Limbă",
    "menu.layout": "Dispunere",
    "menu.locked": "Blochează poziția",
    "menu.login": "Conectare (claude.ai, browser)…",
    "menu.logout": "Deconectare",
    "menu.model_gauge": "Indicator {}",
    "menu.order": "Ordine",
    "menu.panel_visible": "Afișează panoul",
    "menu.quit": "Ieșire",
    "menu.refresh": "Reîmprospătează acum datele de utilizare",
    "menu.settings": "Setări…",
    "menu.size": "Dimensiune",
    "menu.source": "Sursă de date",
    "menu.start_menu": "Afișează în meniul Start",
    "menu.theme": "Temă",
    "menu.update_available": "Actualizare program: instalează versiunea {}…",

    # --- desktop notifications ---------------------------------------------------------------
    "notify.autostart_fail": "Pornirea automată nu a putut fi configurată.",
    "notify.autostart_off": "Dezactivat: aplicația nu va mai porni odată cu Windows.",
    "notify.autostart_on": "Activat: aplicația pornește odată cu Windows.",
    "notify.first_run": "Panoul a apărut în colțul din dreapta sus.\nClic dreapta pe panou sau pe pictograma din zona de notificare = meniu.",
    "notify.login_ok": "Te-ai conectat – sosesc datele de la server.",
    "notify.logout": "Te-ai deconectat. S-a trecut la sursa locală.",
    "notify.reset_done": "{}: s-a resetat — a început o perioadă nouă.",
    "notify.signin_needed": "Conectarea la claude.ai a expirat. Dă clic dreapta pe panou și conectează-te din nou ca să vezi în continuare utilizarea de pe toate dispozitivele tale.",
    "notify.stale_body": "Ultima citire este de acum {}. Este pornit Claude Desktop?",
    "notify.stale_title": "Date învechite",
    "notify.threshold": "{}: s-a utilizat {}%.",
    "notify.update": "Versiunea {} a programului este disponibilă. Clic dreapta pe panou → Actualizare program.",

    # --- floating panel (tight space) --------------------------------------------------------
    "panel.five_hour": "SESIUNE DE 5 ORE",
    "panel.five_hour_short": "5H",
    "panel.full_in": "plin: {}",
    "panel.model": "{} SĂPTĂMÂNAL",
    "panel.no_data": "Fără date",
    "panel.pace": "{} vs ritm",
    "panel.per_day": "{}%/zi",
    "panel.per_hour": "{}%/h",
    "panel.refreshing": "preluare date",
    "panel.reset": "resetare {}",
    "panel.retry_in": "din nou în {} s",
    "panel.updated": "actualizat: {}",
    "panel.week_short": "SĂPT.",
    "panel.weekly": "LIMITĂ SĂPTĂMÂNALĂ",

    # --- profile -----------------------------------------------------------------------------
    "profile.extra": "Credite de utilizare: {}",
    "profile.plan": "Planul tău: {}",
    "profile.since": "Membru din: {}",
    "profile.tier": "Nivel de limitare: {}",

    # --- Settings window ---------------------------------------------------------------------
    "set.about": "{}\nFără telemetrie. Cere de la Anthropic doar datele despre propria ta utilizare și citește numărul versiunii de pe serverul de actualizări.",
    "set.accent": "Culoare de accent",
    "set.always_top": "Deasupra tuturor celorlalte ferestre",
    "set.auto": "automat",
    "set.backup_config": "Configurația scriptului de backup",
    "set.backup_details": "Fereastra de detalii afișează",
    "set.backup_disclaimer": "Claude Usage Monitor doar citește și afișează jurnalele backupului tău – nu creează, nu verifică și nu garantează niciun backup. Claude Backup Kit este un punct de plecare gratuit, oferit ca ajutor: oricine poate modifica scripturile, așa că nu se pot garanta calitatea și completitudinea unui backup. Nu ne asumăm nicio răspundere pentru backupuri, pentru pierderea de date sau pentru orice fel de daune. Fiecare este responsabil să se asigure că backupurile sale sunt complete și pot fi restaurate – testează din când în când o restaurare.",
    "set.backup_disclaimer_h": "Declinarea răspunderii",
    "set.backup_enabled": "Afișează bara de stare backup pe panou",
    "set.backup_found": "Găsit: {}",
    "set.backup_green": "Verde până la",
    "set.backup_label": "Etichetă lângă led",
    "set.backup_lamps": "Leduri",
    "set.backup_root": "Folder de backup",
    "set.backup_tasks": "Filtru pentru activitățile planificate",
    "set.backup_unconfigured": "Nu este setat niciun folder de backup, așa că bara de stare rămâne ascunsă. Alege folderul în care scrie scriptul tău de backup.",
    "set.backup_yellow": "Galben până la",
    "set.browse": "Răsfoiește…",
    "set.click_through": "Transparent la clic (doar decorativ, ignoră mouse-ul)",
    "set.close": "Închide",
    "set.color_hint": "Culorile se schimbă în funcție de praguri: verde → galben → roșu.",
    "set.danger": "Critic",
    "set.data_hint": "Jurnal local: fișierul plan-usage-history.json al aplicației Claude Desktop. Nu necesită conectare, dar măsoară doar acest PC și se reîmprospătează cam la fiecare 5 minute.\n\nclaude.ai: după conectare, interoghează serverul. Vezi utilizarea de pe toate dispozitivele tale, cu orele exacte de resetare și cu reîmprospătare mai frecventă.",
    "set.datafile": "Fișier de date",
    "set.default": "Implicit",
    "set.details_api_only": "Acestea provin din sursa de date claude.ai (necesită conectare); jurnalul local nu le conține.",
    "set.file_filter": "JSON (*.json);;Toate fișierele (*.*)",
    "set.gauge_order": "Ordinea indicatoarelor",
    "set.hours_suffix": " h",
    "set.layout": "Dispunere",
    "set.local_models_hint": "Serverul păstrează un contor separat doar pentru unele modele (de ex. Fable). Pentru celelalte, aici vezi cum se împarte munca din Claude Code de săptămâna aceasta pe acest PC – o parte din propria ta utilizare și tokenurile de ieșire, nu o parte dintr-o limită. Se citesc doar numele modelului și numărul de tokenuri, niciodată conversația.",
    "set.local_models_none": "Nu a fost găsit niciun folder de jurnale Claude Code – acest grup rămâne pur și simplu ascuns. Restul nu este afectat.",
    "set.local_models_path": "Folderul de jurnale Claude Code",
    "set.lock": "Blochează poziția (panoul nu poate fi tras)",
    "set.login_btn_in": "Deconectare de la claude.ai",
    "set.login_btn_out": "Conectare la claude.ai…",
    "set.model_filter": "Model urmărit",
    "set.model_scale": "Dimensiunea indicatorului de model",
    "set.not_set": "nesetat",
    "set.notify_enabled": "Notifică la depășirea unui prag",
    "set.notify_reset": "Notifică atunci când o limită se resetează",
    "set.notify_stale": "Notifică atunci când datele se învechesc",
    "set.opacity": "Opacitate",
    "set.open_config": "Deschide folderul de setări",
    "set.pick_color": "Alege culoarea…",
    "set.pick_file_title": "Alege jurnalul de utilizare",
    "set.profile": "Profil / cont",
    "set.profile_auto": "Automat (ultimul utilizat)",
    "set.profile_n": "Profilul {} – …{}",
    "set.refresh": "Reîmprospătare",
    "set.reset_confirm": "Sigur vrei să restaurezi setările implicite?",
    "set.restore": "Restaurează setările implicite",
    "set.rows_available": "Ce se poate afișa acum – debifează ce nu vrei să vezi:",
    "set.rows_none": "Momentan serverul nu trimite alte limite pentru contul tău. Vor apărea aici automat de îndată ce o va face.",
    "set.sec_suffix": " s",
    "set.show_age": "Vechimea datelor",
    "set.show_burn": "Rată de consum (%/oră, %/zi)",
    "set.show_extra_usage": "Credite de utilizare (plată după consum)",
    "set.show_feedback_icon": "Pictograma de mesaj în antetul panoului",
    "set.show_five_hour": "Afișează sesiunea de 5 ore",
    "set.show_local_models": "Repartizarea pe modele, din jurnalele Claude Code de pe acest PC",
    "set.show_model": "Afișează limita săptămânală a modelului (sursa claude.ai)",
    "set.show_model_list": "Limitele săptămânale ale celorlalte modele",
    "set.show_plan_badge": "Insigna planului în antet (Pro / Max…)",
    "set.show_plan_name": "Afișează numele meu pe insignă",
    "set.show_reset": "Numărătoare inversă până la resetare",
    "set.show_spark": "Curbă de tendință (sparkline)",
    "set.show_surfaces": "Limite pe produs (Claude Code, aplicații conectate…)",
    "set.show_weekly": "Afișează limita săptămânală",
    "set.size": "Dimensiune",
    "set.snap": "Fixare la marginea ecranului",
    "set.source_api": "claude.ai – toate dispozitivele (necesită conectare)",
    "set.source_label": "Sursa măsurătorii",
    "set.source_local": "Jurnal local – doar acest PC",
    "set.tab_alerts": "Alerte",
    "set.tab_appearance": "Aspect",
    "set.tab_content": "Conținut",
    "set.tab_data": "Sursă de date",
    "set.tab_details": "Detalii",
    "set.tab_system": "Sistem",
    "set.taskbar": "Afișează în bara de activități (ca fereastră)",
    "set.theme": "Temă",
    "set.theme_default": "Din temă",
    "set.tip": "Sfat: trage panoul cu butonul stâng, Ctrl+rotiță redimensionează,\nclic dreapta = meniu, dublu clic = istoric.",
    "set.title": "setări",
    "set.tray_five": "Sesiune de 5 ore",
    "set.tray_max": "Valoarea mai mare",
    "set.tray_value": "Valoare în zona de notificare",
    "set.tray_weekly": "Limită săptămânală",
    "set.update_check": "Caută automat actualizări ale programului",
    "set.version": "Versiune",
    "set.visible": "Panou flotant vizibil",
    "set.warn": "Avertizare",

    # --- sizes, sources, themes --------------------------------------------------------------
    "size.extra": "Foarte mare",
    "size.large": "Mare",
    "size.normal": "Normală",
    "size.small": "Mică",
    "source.api": "claude.ai (toate dispozitivele)",
    "source.local": "Local (doar acest PC)",
    "theme.claude": "Claude (cald, întunecat)",
    "theme.graphite": "Grafit",
    "theme.midnight": "Sticlă de noapte",
    "theme.neon": "Neon",
    "theme.paper": "Hârtie deschisă",
    "theme.postit": "Galben post-it",

    # --- time units (panel) ------------------------------------------------------------------
    "time.day": "{} z",
    "time.dh": "{}z {}h",
    "time.hm": "{}h {}min",
    "time.hour": "{} h",
    "time.m": "{}min",
    "time.min": "{} min",
    "time.none": "fără date",
    "time.sec": "{} s",

    # --- tray --------------------------------------------------------------------------------
    "tray.head": "5h: {}%   ·   Săpt.: {}%",
    "tray.line": "{}: {}%",

    # --- program update ----------------------------------------------------------------------
    "update.available": "Versiunea {} este disponibilă.",
    "update.check_failed": "Căutarea actualizărilor nu a reușit: {}",
    "update.check_now": "Caută acum",
    "update.checking": "Se caută actualizări…",
    "update.downloading": "Se descarcă… {} din {}",
    "update.failed": "Actualizarea nu a reușit: {}",
    "update.install": "Instalează acum",
    "update.installed": "Versiune instalată: {}",
    "update.later": "Mai târziu",
    "update.manual": "Această copie nu se poate actualiza singură (rulează din codul sursă sau dintr-un folder doar în citire). Descarcă în schimb pachetul nou.",
    "update.open_page": "Deschide pagina de descărcare",
    "update.restarting": "Se instalează – aplicația repornește imediat.",
    "update.skip": "Omite această versiune",
    "update.title": "Actualizare program",
    "update.uptodate": "Ai cea mai recentă versiune.",
    "update.verifying": "Se verifică și se dezarhivează…",
    "update.whats_new": "Noutăți",
}

# macOS wording (the four keys of source.json "mac"): "start at login" instead of "start with Windows", menu bar instead of tray
STRINGS_MAC = {
    "menu.autostart": "Deschide la autentificare",
    "notify.autostart_on": "Activat: aplicația se deschide când te autentifici.",
    "notify.autostart_off": "Dezactivat: aplicația nu se va mai deschide la autentificare.",
    "notify.first_run": "Panoul a apărut în colțul din dreapta sus.\nClic dreapta pe panou sau pe pictograma din bara de meniu = meniu.",
}
