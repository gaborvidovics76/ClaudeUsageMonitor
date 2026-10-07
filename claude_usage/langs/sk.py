# -*- coding: utf-8 -*-
"""Slovenčina – UI strings of Claude Usage Monitor."""

CODE = "sk"
NAME = "Slovenčina"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{}d",
    "backup.age_h": "{}h",
    "backup.age_m": "{}min",
    "backup.and_more": "…a ešte {}",
    "backup.checked_at": "Skontrolované: {}",
    "backup.checking": "Kontroluje sa…",
    "backup.cloud_only": "Snímka je v OneDrive dostupná len online; jej obsah sa nevypisuje, aby sa nemusela sťahovať.",
    "backup.comp.cowork": "Záznamy konverzácií Cowork (ZIP pre každú reláciu)",
    "backup.comp.vault": "Snímka trezora Obsidian (ZIP)",
    "backup.disclaimer_short": "Monitor zobrazuje len to, čo uvádzajú záznamy záloh. Za zálohy nepreberáme žiadnu zodpovednosť – skontrolovať, či sú úplné a dajú sa obnoviť, je na tebe.",
    "backup.done": "hotovo",
    "backup.dry_run": "(skúšobný beh, nič sa nenahralo)",
    "backup.failed": "ZLYHALO",
    "backup.files_size": "Súbory: {} ({})",
    "backup.folders": "Priečinky",
    "backup.label_age": "Názov a uplynutý čas",
    "backup.label_name": "Len názov",
    "backup.label_none": "Len kontrolky",
    "backup.last_ok": "Posledná úspešná záloha: {} (pred {})",
    "backup.last_run": "Posledné spustenie: {} – {}",
    "backup.legend": "Zelená: nie staršia ako {} h · Žltá: do {} h · Červená: staršia alebo žiadna záloha",
    "backup.level_green": "Aktuálna",
    "backup.level_none": "Nenašla sa žiadna záloha",
    "backup.level_red": "Zastaraná",
    "backup.level_yellow": "Začína zastarávať",
    "backup.log_file": "Súbor záznamu",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Priečinok záloh sa nenašiel: {}",
    "backup.none_found": "Žiadne.",
    "backup.open": "otvoriť",
    "backup.rc_copied": "nové alebo zmenené súbory sa skopírovali",
    "backup.rc_failed": "ZLYHALO (kód {})",
    "backup.rc_nochange": "aktuálne, nebolo čo kopírovať",
    "backup.recent_notes": "Naposledy upravené poznámky v snímke",
    "backup.refresh": "Skontrolovať teraz",
    "backup.sec_components": "Čo sa zálohuje",
    "backup.sec_contents": "Obsah",
    "backup.sec_log": "Záznam (posledné riadky)",
    "backup.sec_problems": "Chyby a varovania",
    "backup.sec_tasks": "Naplánované úlohy",
    "backup.skipped": "preskočené (priečinok sa nenašiel)",
    "backup.snap_kept": "Ponechané snímky: {}, spolu {}",
    "backup.snapshot": "Najnovšia snímka",
    "backup.source": "Zdroj",
    "backup.state_error": "skončilo s chybami",
    "backup.state_interrupted": "nedokončilo sa",
    "backup.state_ok": "úspešne dokončené",
    "backup.state_running": "práve prebieha",
    "backup.storage": "Vzdialené úložisko: využité {} z {}, voľné {}",
    "backup.target": "Cieľ",
    "backup.task_event": "pri udalosti",
    "backup.task_row": "posledné spustenie {} · výsledok {} · ďalšie {}",
    "backup.tip_click": "Kliknutím zobrazíš podrobnosti",
    "backup.title": "Zálohy",
    "backup.tray": "Zálohy: {}",
    "backup.uploaded": "Nahrané v tomto behu – nové: {}, nahradené: {}, chyby: {}",
    "backup.uploaded_files": "Nahrané súbory",
    "backup.uploaded_groups": "Nahrané súbory podľa priečinkov",
    "backup.uploaded_no": "Nahrané do Nextcloudu: zatiaľ nie",
    "backup.uploaded_yes": "Nahrané do Nextcloudu: áno ({})",
    "backup.vault": "Trezor",
    "backup.vault_changed": "Poznámky zmenené v trezore od tejto snímky: {}",
    "backup.zip_new": "Nové/aktualizované ZIP: {}",
    "backup.zip_summary": "Súbory: {} (poznámky: {}), po rozbalení {}",

    # --- general ------------------------------------------------------------------------------
    "detail.extra": "Kredity na využitie",
    "detail.local_header": "CLAUDE CODE · TENTO POČÍTAČ · ROZDELENIE TOHTO TÝŽDŇA",
    "detail.off": "vypnuté",
    "detail.on": "zapnuté",
    "detail.surface.oauth_apps": "Pripojené aplikácie",
    "detail.unlimited": "bez limitu",
    "dlg.cancel": "Zrušiť",
    "dlg.checking": "Kontroluje sa…",
    "dlg.err_badcode": "Kód nebol prijatý.\n\n{}\n\nSkontroluj, či je vložený celý kód, alebo sa skús znova prihlásiť v prehliadači (vždy s novým kódom).",
    "dlg.err_ratelimit": "Príliš veľa pokusov o prihlásenie v krátkom čase.\n\nServer ťa dočasne obmedzuje. Zavri toto okno, počkaj 10–15 minút (medzitým to neskúšaj) a potom spusti JEDNO nové prihlásenie v prehliadači s novým kódom.",
    "dlg.hint1": "Na stránke, ktorá sa otvorí, sa prihlás a schváľ prístup. Na konci dostaneš kód.",
    "dlg.intro": "Prihlás sa do svojho účtu claude.ai vo vlastnom prehliadači (uložené heslá a prístupové kľúče tam už fungujú).",
    "dlg.login_title": "prihlásenie",
    "dlg.open_browser": "Otvoriť prihlásenie v prehliadači",
    "dlg.paste_label": "Sem prilep získaný kód:",
    "dlg.paste_placeholder": "sem prilep kód",
    "dlg.signin": "Prihlásiť sa",
    "dlg.step1": "Krok 1",
    "dlg.step2": "Krok 2",
    "dlg.unknown_err": "Neznáma chyba.",

    # --- error messages ---------------------------------------------------------------------
    "err.already_running": "Aplikácia je už spustená (pozri oblasť oznámení).",
    "err.bad_token_resp": "neplatná odpoveď z koncového bodu tokenu",
    "err.bad_usage_resp": "neplatná odpoveď z koncového bodu využitia",
    "err.connection": "chyba pripojenia: {}",
    "err.file_empty": "Súbor s údajmi o využití je prázdny.",
    "err.file_not_found": "Súbor s údajmi o využití sa nenašiel.\nJe Claude Desktop spustený?",
    "err.file_unreadable": "Súbor s údajmi o využití sa momentálne nedá prečítať.",
    "err.loading": "Prihlasovanie / načítavanie…",
    "err.network": "chyba siete: {}",
    "err.no_code": "Nebol vložený žiadny kód.",
    "err.no_data_profile": "Pre tento profil nie sú žiadne údaje.",
    "err.no_tray": "Oblasť oznámení nie je k dispozícii; ikona sa nezobrazí.",
    "err.no_usage_data": "Žiadne údaje o využití.",
    "err.not_signed_in": "Bez prihlásenia.",
    "err.query_http": "Chyba dopytu (HTTP {}).",
    "err.rate_limited": "Server obmedzuje počet požiadaviek (429) – automaticky to skúsim znova.",
    "err.session_expired": "Platnosť relácie vypršala, prihlás sa znova.",
    "err.session_expired_nl": "Platnosť relácie vypršala.\nPrihlás sa znova.",
    "err.signin_needed": "Platnosť prihlásenia na claude.ai vypršala.\nPrihlás sa znova: pravé tlačidlo → Prihlásiť sa na claude.ai",
    "err.unexpected": "Neočakávaná chyba: {}",

    # --- 'Message to the developer' window ------------------------------------------------
    "fb.cancel": "Zrušiť",
    "fb.close": "Zavrieť",
    "fb.consent": "Prečítal/a som si {} a súhlasím s nimi.",
    "fb.email": "E-mail",
    "fb.email_hint": "len ak chceš odpoveď",
    "fb.err_consent": "Na odoslanie musíš prijať Zásady ochrany osobných údajov.",
    "fb.err_email": "Táto e-mailová adresa nevyzerá správne.",
    "fb.err_empty": "Najprv napíš správu alebo vyber hodnotenie.",
    "fb.err_links": "V správe je príliš veľa odkazov.",
    "fb.err_network": "Nepodarilo sa spojiť s claudeusagemonitor.com. Skontroluj pripojenie a skús to znova.",
    "fb.err_rate": "Príliš veľa správ v krátkom čase – skús to neskôr.",
    "fb.err_server": "Server momentálne nemôže správu prijať. Skús to neskôr.",
    "fb.intro": "Nápad, chyba alebo sa ti to jednoducho páči? Napíš mi. Každú správu čítam ja, Vidovics Gábor, autor programu.",
    "fb.message": "Správa",
    "fb.message_ph": "Čo funguje, čo nie a čo chýba?",
    "fb.meta": "So správou sa odošle aj: verzia programu {0}, operačný systém ({1}), jazyk rozhrania ({2}).",
    "fb.name": "Meno",
    "fb.optional": "(nepovinné)",
    "fb.privacy_hide": "Skryť zásady",
    "fb.privacy_text": (
        "Prevádzkovateľ: Vidovics Gábor, fyzická osoba (Maďarsko), autor programu Claude Usage Monitor. "
        "Úplné zásady ochrany osobných údajov nájdeš na webovej stránke: https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "Čo sa odosiela: to, čo sem napíšeš – meno (nepovinné), e-mailová adresa (nepovinná), správa, "
        "hodnotenie hviezdičkami – a aby som rozumel súvislostiam: verzia programu, názov a verzia operačného "
        "systému, jazyk rozhrania a čas odoslania. Server neukladá IP adresu; na ochranu pred zneužitím používa "
        "len denne sa meniaci hash, z ktorého sa adresa nedá spätne odvodiť."
        "\n\n"
        "Prečo: aby som si mohol tvoju správu prečítať a odpovedať na ňu a aby som mohol program zlepšovať "
        "(oprávnený záujem, čl. 6 ods. 1 písm. f) GDPR; samotná odpoveď na tvoju žiadosť). Tvoje hodnotenie "
        "a meno sa na webovej stránke zobrazia, len ak na to zaškrtneš samostatné políčko (súhlas, čl. 6 ods. 1 "
        "písm. a) GDPR), a až potom, ako ich autor skontroluje; tento súhlas môžeš kedykoľvek odvolať."
        "\n\n"
        "Ako dlho: správy najviac 2 roky; zverejnené hodnotenie, kým neodvoláš súhlas. Ak autor zapol "
        "preposielanie e-mailov, kópia príde aj do jeho poštovej schránky."
        "\n\n"
        "Kto má prístup k údajom:len prevádzkovateľ a – ako sprostredkovateľ – poskytovateľ hostingu (server "
        "v EÚ, v Nemecku). Nič sa nepredáva ani neposkytuje ďalej; nedochádza k profilovaniu ani "
        "k automatizovanému rozhodovaniu."
        "\n\n"
        "Tvoje práva: prístup, oprava, vymazanie, obmedzenie spracúvania, namietanie, odvolanie súhlasu "
        "a podanie sťažnosti dozornému orgánu (v Maďarsku: NAIH, naih.hu) alebo dozornému orgánu vo vlastnej "
        "krajine (na Slovensku: Úrad na ochranu osobných údajov SR). Kontakt: tento formulár alebo webová stránka."
        "\n\n"
        "Prenos: šifrovane (HTTPS/TLS) na claudeusagemonitor.com. Verzia týchto zásad: 6. 10. 2026."
    ),
    "fb.privacy_title": "Zásady ochrany osobných údajov",
    "fb.publish": "Moje hodnotenie a meno (ak je uvedené) sa môžu zobraziť na claudeusagemonitor.com.",
    "fb.rating": "Celkové hodnotenie",
    "fb.rating_clear": "vymazať",
    "fb.rating_hint": "nepovinné – klikni na hviezdičku",
    "fb.rating_tip": "{} z 5",
    "fb.secure": "Šifrované pripojenie (HTTPS) na claudeusagemonitor.com.",
    "fb.send": "Odoslať",
    "fb.sending": "Odosiela sa…",
    "fb.sent": "Ďakujem – správa dorazila!",
    "fb.sent_sub": "Čítam každú správu. Ak je v nej e-mailová adresa, odpoviem na ňu.",
    "fb.title": "Správa vývojárovi",

    # --- Help window --------------------------------------------------------------------------
    "help.disclaimer": "Nezávislý bezplatný nástroj – nevytvorila ho spoločnosť Anthropic a nie je s ňou nijako prepojený. „Claude“ je ochranná známka spoločnosti Anthropic.",
    "help.feedback": "Otázky, nápady, hlásenia chýb: formulár na odoslanie správy na webovej stránke.",
    "help.free": "Navždy zadarmo · licencia MIT · otvorený zdrojový kód · bez telemetrie",
    "help.guide": (
        "\n<h2>Čo panel zobrazuje</h2>"
        "\n<ul>"
        "\n<li><b>5-hodinová relácia</b> – aká časť limitu aktuálnej relácie je už využitá. Resetuje sa každých päť hodín; panel odpočítava čas do resetu.</li>"
        "\n<li><b>Týždenný limit</b> – využitie všetkých modelov spolu; resetuje sa raz týždenne v čase pevne stanovenom pre tvoj účet.</li>"
        "\n<li><b>Týždenný limit modelu</b> – tretí ukazovateľ, ak ho server hlási (napr. pre konkrétny model).</li>"
        "\n<li><b>Tempo a rýchlosť čerpania</b> – ako rýchlo limit míňaš a či vydrží do resetu; odhad na koniec týždňa ťa včas upozorní.</li>"
        "\n<li><b>Kredity na využitie</b> a odznak plánu – ak ich zapneš v ponuke <i>Odznak plánu a ďalšie limity</i>.</li>"
        "\n</ul>"
        "\n<h2>Odkiaľ pochádzajú údaje</h2>"
        "\n<ul>"
        "\n<li><b>claude.ai (všetky zariadenia)</b> – dopytuje sa servera spoločnosti Anthropic, takže započíta aj využitie v telefóne, v prehliadači a na iných počítačoch. Vyžaduje jednorazové prihlásenie vo vlastnom prehliadači (ponuka: <i>Prihlásiť sa</i>). Obnovuje sa každé 2 minúty, zriedkavejšie, ak o to server požiada.</li>"
        "\n<li><b>Lokálne (len tento počítač)</b> – číta záznam o využití aplikácie Claude Desktop na tomto počítači. Nevyžaduje prihlásenie, ale pozná len tento počítač.</li>"
        "\n</ul>"
        "\n<p>Prepínať medzi nimi môžeš v ponuke <i>Zdroj údajov</i>.</p>"
        "\n<h2>Ovládanie panela</h2>"
        "\n<ul>"
        "\n<li><b>Kliknutie pravým tlačidlom</b> na panel (alebo na ikonu v oblasti oznámení) – celá ponuka.</li>"
        "\n<li><b>Dvojité kliknutie</b> na ukazovateľ – okno <b>História</b>: 6 hodín, 24 hodín, 7 dní alebo všetko, s maximami, denným priemerom a odhadom.</li>"
        "\n<li><b>Ťahaním</b> panel presunieš; prichytáva sa k okrajom obrazovky. <b>Ctrl + koliesko myši</b> – zväčšenie alebo zmenšenie.</li>"
        "\n<li>Rozloženia: lístok post-it, úzky pásik, kruhy; 6 motívov. <i>Zamknúť polohu</i> a <i>Prepúšťať kliknutia</i> nájdeš v Nastaveniach.</li>"
        "\n</ul>"
        "\n<h2>Upozornenia</h2>"
        "\n<p>Žltá od 70 %, červená od 90 % (nastaviteľné). Môžeš si zapnúť aj oznámenia pri resete limitu a pri zastarávaní údajov.</p>"
        "\n<h2>Zálohy (nepovinné)</h2>"
        "\n<p>Malé kontrolky ukazujú, či sa tvoje naplánované zálohy spustili a dokončili. Kliknutím na kontrolku zobrazíš podrobnosti. Monitor iba číta záznamy záloh – vytvárať a testovať zálohy je tvoja úloha (pozri Podmienky používania).</p>"
        "\n<h2>Aktualizácie</h2>"
        "\n<p>Program sám vyhľadáva nové verzie a aktualizuje sa jedným kliknutím. Každý balík sa overuje pomocou SHA-256 a pochádza výhradne z <b>claudeusagemonitor.com</b>. Nové verzie a poznámky k vydaniu: {site}</p>"
        "\n<h2>Ochrana súkromia</h2>"
        "\n<p>Žiadna telemetria, žiadne sledovanie. Prihlásenie na claude.ai sa ukladá šifrovane len na tomto počítači; nikam inam sa nič neodosiela.</p>"
        "\n<h2>Keď niečo nefunguje</h2>"
        "\n<ul>"
        "\n<li><i>429 / obmedzenie požiadaviek</i> – server spomaľuje požiadavky; program to sám skúsi znova.</li>"
        "\n<li>Žiadne údaje – skontroluj <i>Zdroj údajov</i>; pri claude.ai sa prihlás znova.</li>"
        "\n<li>História sa uchováva 7 dní a zostane zachovaná aj po reštarte a aktualizácii.</li>"
        "\n<li>Záznamy a nastavenia: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>"
        "\n</ul>"
        "\n"
    ),
    "help.made_by": "Autor",
    "help.moved": "Nová adresa od 21. septembra 2026 – pôvodná stránka dinorr.hu/claude-usage-monitor presmerúva sem.",
    "help.official": "OFICIÁLNA WEBOVÁ STRÁNKA",
    "help.open_site": "Otvoriť claudeusagemonitor.com",
    "help.privacy": "Zásady ochrany osobných údajov",
    "help.site_what": "Stiahnutie, automatické aktualizácie, novinky, Claude Backup Kit, podmienky používania a ochrana súkromia – všetko na jednom mieste.",
    "help.source_code": "Zdrojový kód (GitHub)",
    "help.tab_author": "Autor",
    "help.tab_guide": "Ako to funguje",
    "help.terms": "Podmienky používania",
    "help.title": "Pomocník",
    "help.version": "Verzia",

    # --- History window -----------------------------------------------------------------------
    "hist.legend_5h": "5-hodinová relácia",
    "hist.legend_week": "týždenný limit",
    "hist.no_data": "Na toto obdobie nie je dosť údajov.",
    "hist.range_24h": "24 hodín",
    "hist.range_6h": "6 hodín",
    "hist.range_7d": "7 dní",
    "hist.range_all": "Všetko",
    "hist.stat_burn": "Priem. denné čerpanie",
    "hist.stat_forecast": "Odhad na koniec týždňa",
    "hist.stat_now": "Aktuálne za týždeň",
    "hist.stat_peak": "Týždenné maximum",
    "hist.stat_sessions": "5-hodinové relácie",
    "hist.title": "história",

    # --- layouts / menu -----------------------------------------------------------------------
    "layout.compact": "Úzky pásik",
    "layout.postit": "Lístok post-it",
    "layout.ring": "Kruhy",
    "menu.always_top": "Vždy navrchu",
    "menu.autostart": "Spúšťať s Windowsom",
    "menu.backup_bar": "Stavový riadok záloh",
    "menu.backups": "Zálohy…",
    "menu.check_update": "Vyhľadať aktualizácie programu…",
    "menu.click_through": "Prepúšťať kliknutia",
    "menu.details": "Odznak plánu a ďalšie limity",
    "menu.feedback": "Správa vývojárovi…",
    "menu.help": "Pomocník…",
    "menu.history": "História a štatistiky…",
    "menu.language": "Jazyk",
    "menu.layout": "Rozloženie",
    "menu.locked": "Zamknúť polohu",
    "menu.login": "Prihlásiť sa (claude.ai, prehliadač)…",
    "menu.logout": "Odhlásiť sa",
    "menu.model_gauge": "Ukazovateľ {}",
    "menu.order": "Poradie",
    "menu.panel_visible": "Zobraziť panel",
    "menu.quit": "Ukončiť",
    "menu.refresh": "Obnoviť údaje o využití teraz",
    "menu.settings": "Nastavenia…",
    "menu.size": "Veľkosť",
    "menu.source": "Zdroj údajov",
    "menu.start_menu": "Zobraziť v ponuke Štart",
    "menu.theme": "Motív",
    "menu.update_available": "Aktualizácia programu: nainštalovať verziu {}…",

    # --- desktop notifications ----------------------------------------------------------------
    "notify.autostart_fail": "Automatické spúšťanie sa nepodarilo nastaviť.",
    "notify.autostart_off": "Vypnuté: aplikácia sa nebude spúšťať s Windowsom.",
    "notify.autostart_on": "Zapnuté: aplikácia sa spúšťa s Windowsom.",
    "notify.first_run": "Panel sa zobrazil v pravom hornom rohu.\nKliknutie pravým tlačidlom na panel alebo ikonu v oblasti oznámení = ponuka.",
    "notify.login_ok": "Prihlásenie úspešné – prichádzajú údaje zo servera.",
    "notify.logout": "Odhlásené. Prepnuté na lokálny zdroj.",
    "notify.reset_done": "{}: reset – začalo sa nové obdobie.",
    "notify.signin_needed": "Platnosť prihlásenia na claude.ai vypršala. Klikni pravým tlačidlom na panel a znova sa prihlás, aby sa naďalej zobrazovalo využitie zo všetkých tvojich zariadení.",
    "notify.stale_body": "Posledné meranie bolo pred {}. Je Claude Desktop spustený?",
    "notify.stale_title": "Zastarané údaje",
    "notify.threshold": "{}: využitie {} %.",
    "notify.update": "K dispozícii je verzia programu {}. Pravé tlačidlo na paneli → Aktualizácia programu.",

    # --- panel labels -------------------------------------------------------------------------
    "panel.five_hour": "5-HODINOVÁ RELÁCIA",
    "panel.five_hour_short": "5H",
    "panel.full_in": "plný: {}",
    "panel.model": "{} TÝŽDEŇ",
    "panel.no_data": "Bez údajov",
    "panel.pace": "tempo {}",
    "panel.per_day": "{}%/deň",
    "panel.per_hour": "{}%/h",
    "panel.refreshing": "načítava sa",
    "panel.reset": "reset: {}",
    "panel.retry_in": "znova o {} s",
    "panel.updated": "obnovené: {}",
    "panel.week_short": "TÝŽ.",
    "panel.weekly": "TÝŽDENNÝ LIMIT",

    # --- profile ------------------------------------------------------------------------------
    "profile.extra": "Kredity na využitie: {}",
    "profile.plan": "Plán: {}",
    "profile.since": "Členstvo od: {}",
    "profile.tier": "Úroveň limitov: {}",

    # --- Settings window ----------------------------------------------------------------------
    "set.about": "{}\nBez telemetrie. Od spoločnosti Anthropic si vyžiada len údaje o tvojom vlastnom využití a zo servera aktualizácií načíta číslo verzie.",
    "set.accent": "Farba zvýraznenia",
    "set.always_top": "Nad všetkými ostatnými oknami",
    "set.auto": "automaticky",
    "set.backup_config": "Konfigurácia zálohovacieho skriptu",
    "set.backup_details": "Okno podrobností zobrazuje",
    "set.backup_disclaimer": "Claude Usage Monitor iba načítava a zobrazuje záznamy tvojej zálohy – žiadnu zálohu nevytvára, nekontroluje ani negarantuje. Claude Backup Kit je bezplatný východiskový bod ponúkaný ako pomoc: skripty môže ktokoľvek zmeniť, preto kvalitu a úplnosť zálohy nemožno zaručiť. Za zálohy, stratu údajov ani akúkoľvek škodu nepreberáme žiadnu zodpovednosť. Zabezpečiť, aby boli zálohy úplné a dali sa obnoviť, je zodpovednosťou každého – z času na čas si vyskúšaj obnovenie.",
    "set.backup_disclaimer_h": "Vylúčenie zodpovednosti",
    "set.backup_enabled": "Zobraziť na paneli stavový riadok záloh",
    "set.backup_found": "Nájdené: {}",
    "set.backup_green": "Zelená do",
    "set.backup_label": "Popis vedľa kontrolky",
    "set.backup_lamps": "Kontrolky",
    "set.backup_root": "Priečinok záloh",
    "set.backup_tasks": "Filter naplánovaných úloh",
    "set.backup_unconfigured": "Nie je nastavený priečinok záloh, preto stavový riadok zostáva skrytý. Vyber priečinok, do ktorého zapisuje tvoj zálohovací skript.",
    "set.backup_yellow": "Žltá do",
    "set.browse": "Prehľadávať…",
    "set.click_through": "Prepúšťať kliknutia (len ozdoba, ignoruje myš)",
    "set.close": "Zavrieť",
    "set.color_hint": "Farby sa menia podľa prahov: zelená → žltá → červená.",
    "set.danger": "Kritické",
    "set.data_hint": "Lokálny záznam: súbor plan-usage-history.json aplikácie Claude Desktop. Nevyžaduje prihlásenie, ale meria len tento počítač a obnovuje sa približne každých 5 minút.\n\nclaude.ai: po prihlásení sa dopytuje servera. Vidíš využitie zo všetkých svojich zariadení s presnými časmi resetu a častejším obnovovaním.",
    "set.datafile": "Súbor s údajmi",
    "set.default": "Predvolené",
    "set.details_api_only": "Tieto údaje pochádzajú zo zdroja claude.ai (vyžaduje prihlásenie); lokálny záznam ich neobsahuje.",
    "set.file_filter": "JSON (*.json);;Všetky súbory (*.*)",
    "set.gauge_order": "Poradie ukazovateľov",
    "set.hours_suffix": " h",
    "set.layout": "Rozloženie",
    "set.local_models_hint": "Server vedie samostatné počítadlo len pre niektoré modely (napr. Fable). Pri ostatných sa tu zobrazuje, ako sa tento týždeň rozdeľuje tvoja práca v Claude Code na tomto počítači – podiel na tvojom vlastnom využití a výstupné tokeny, nie podiel z limitu. Načítavajú sa len názvy modelov a počty tokenov, nikdy nie obsah konverzácie.",
    "set.local_models_none": "Nenašiel sa žiadny priečinok so záznamami Claude Code – táto skupina jednoducho zostane skrytá. Nič iné to neovplyvní.",
    "set.local_models_path": "Priečinok záznamov Claude Code",
    "set.lock": "Zamknúť polohu (nedá sa presúvať)",
    "set.login_btn_in": "Odhlásiť sa z claude.ai",
    "set.login_btn_out": "Prihlásiť sa na claude.ai…",
    "set.model_filter": "Sledovaný model",
    "set.model_scale": "Veľkosť ukazovateľa modelu",
    "set.not_set": "nenastavené",
    "set.notify_enabled": "Oznámiť prekročenie prahu",
    "set.notify_reset": "Oznámiť reset limitu",
    "set.notify_stale": "Oznámiť, keď údaje zastarajú",
    "set.opacity": "Nepriehľadnosť",
    "set.open_config": "Otvoriť priečinok nastavení",
    "set.pick_color": "Vybrať farbu…",
    "set.pick_file_title": "Výber záznamu o využití",
    "set.profile": "Profil / účet",
    "set.profile_auto": "Automaticky (naposledy použitý)",
    "set.profile_n": "Profil {} – …{}",
    "set.refresh": "Obnoviť",
    "set.reset_confirm": "Naozaj chceš obnoviť predvolené nastavenia?",
    "set.restore": "Obnoviť predvolené",
    "set.rows_available": "Čo sa dá práve zobraziť – zruš začiarknutie pri tom, čo nechceš vidieť:",
    "set.rows_none": "Server momentálne neposiela pre tvoj účet žiadne ďalšie limity. Hneď ako ich začne posielať, zobrazia sa tu automaticky.",
    "set.sec_suffix": " s",
    "set.show_age": "Aktuálnosť údajov",
    "set.show_burn": "Rýchlosť čerpania (%/h, %/deň)",
    "set.show_extra_usage": "Kredity na využitie (platba podľa spotreby)",
    "set.show_feedback_icon": "Ikona správy v hlavičke panela",
    "set.show_five_hour": "Zobraziť 5-hodinovú reláciu",
    "set.show_local_models": "Rozdelenie medzi modely zo záznamov Claude Code na tomto počítači",
    "set.show_model": "Zobraziť týždenný limit modelu (zdroj claude.ai)",
    "set.show_model_list": "Týždenné limity ostatných modelov",
    "set.show_plan_badge": "Odznak plánu v hlavičke (Pro / Max…)",
    "set.show_plan_name": "Zobraziť moje meno na odznaku",
    "set.show_reset": "Odpočet do resetu",
    "set.show_spark": "Krivka trendu (sparkline)",
    "set.show_surfaces": "Limity podľa prostredia (Claude Code, pripojené aplikácie…)",
    "set.show_weekly": "Zobraziť týždenný limit",
    "set.size": "Veľkosť",
    "set.snap": "Prichytávať k okraju obrazovky",
    "set.source_api": "claude.ai – všetky zariadenia (vyžaduje prihlásenie)",
    "set.source_label": "Zdroj merania",
    "set.source_local": "Lokálny záznam – len tento počítač",
    "set.tab_alerts": "Upozornenia",
    "set.tab_appearance": "Vzhľad",
    "set.tab_content": "Obsah",
    "set.tab_data": "Zdroj údajov",
    "set.tab_details": "Podrobnosti",
    "set.tab_system": "Systém",
    "set.taskbar": "Zobraziť na paneli úloh (ako okno)",
    "set.theme": "Motív",
    "set.theme_default": "Podľa motívu",
    "set.tip": "Tip: panel presúvaš ľavým tlačidlom, Ctrl + koliesko mení veľkosť,\npravé tlačidlo = ponuka, dvojité kliknutie = história.",
    "set.title": "nastavenia",
    "set.tray_five": "5-hodinová relácia",
    "set.tray_max": "Vyššia z oboch",
    "set.tray_value": "Hodnota ikony v oblasti oznámení",
    "set.tray_weekly": "Týždenný limit",
    "set.update_check": "Automaticky vyhľadávať aktualizácie programu",
    "set.version": "Verzia",
    "set.visible": "Zobraziť plávajúci panel",
    "set.warn": "Varovanie",

    # --- sizes / sources / themes ---------------------------------------------------------------
    "size.extra": "Extra",
    "size.large": "Veľká",
    "size.normal": "Normálna",
    "size.small": "Malá",
    "source.api": "claude.ai (všetky zariadenia)",
    "source.local": "Lokálne (len tento počítač)",
    "theme.claude": "Claude (teplý tmavý)",
    "theme.graphite": "Grafit",
    "theme.midnight": "Polnočné sklo",
    "theme.neon": "Neón",
    "theme.paper": "Svetlý papier",
    "theme.postit": "Žltý post-it",

    # --- time units ---------------------------------------------------------------------------
    "time.day": "{} d",
    "time.dh": "{}d {}h",
    "time.hm": "{}h {}min",
    "time.hour": "{} h",
    "time.m": "{}min",
    "time.min": "{} min",
    "time.none": "bez údajov",
    "time.sec": "{} s",

    # --- tray ---------------------------------------------------------------------------------
    "tray.head": "5h: {}%   ·   Týž.: {}%",
    "tray.line": "{}: {}%",

    # --- program update -----------------------------------------------------------------------
    "update.available": "K dispozícii je verzia {}.",
    "update.check_failed": "Aktualizácie sa nepodarilo vyhľadať: {}",
    "update.check_now": "Vyhľadať teraz",
    "update.checking": "Vyhľadávajú sa aktualizácie…",
    "update.downloading": "Sťahuje sa… {} z {}",
    "update.failed": "Aktualizácia zlyhala: {}",
    "update.install": "Nainštalovať teraz",
    "update.installed": "Nainštalovaná verzia: {}",
    "update.later": "Neskôr",
    "update.manual": "Táto kópia sa nedokáže aktualizovať sama (beží zo zdrojového kódu alebo z priečinka určeného iba na čítanie). Stiahni si radšej nový balík.",
    "update.open_page": "Otvoriť stránku na stiahnutie",
    "update.restarting": "Inštaluje sa – aplikácia sa o chvíľu reštartuje.",
    "update.skip": "Preskočiť túto verziu",
    "update.title": "Aktualizácia programu",
    "update.uptodate": "Máš najnovšiu verziu.",
    "update.verifying": "Overuje sa a rozbaľuje…",
    "update.whats_new": "Čo je nové",
}

# macOS wording (the four keys of source.json "mac"): "start at login" instead of "start with Windows", menu bar instead of tray
STRINGS_MAC = {
    "menu.autostart": "Otvoriť pri prihlásení",
    "notify.autostart_on": "Zapnuté: aplikácia sa otvorí pri prihlásení.",
    "notify.autostart_off": "Vypnuté: aplikácia sa pri prihlásení neotvorí.",
    "notify.first_run": "Panel sa zobrazil v pravom hornom rohu.\nKliknutie pravým tlačidlom na panel alebo ikonu v lište ponúk = ponuka.",
}
