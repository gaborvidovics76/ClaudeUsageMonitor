"""Translations of the Help window (merged into i18n.STRINGS).

help.guide is HTML for a QTextBrowser. Placeholders filled in by help_dialog.py (str.replace, not format):
{site} = the website in the current language, {cfg} = the settings folder of this computer.
Terminology follows Anthropic's own words: 5-hour session, weekly limit, reset, usage credits.
"""

STRINGS_HELP = {
    "menu.help": {
        "en": "Help…", "hu": "Súgó (HELP)…", "de": "Hilfe…", "fr": "Aide…", "es": "Ayuda…", "it": "Guida…",
        "pt": "Ajuda…", "pl": "Pomoc…", "nl": "Help…", "ru": "Справка…", "cs": "Nápověda…", "tr": "Yardım…",
    },
    "help.title": {
        "en": "Help", "hu": "Súgó", "de": "Hilfe", "fr": "Aide", "es": "Ayuda", "it": "Guida",
        "pt": "Ajuda", "pl": "Pomoc", "nl": "Help", "ru": "Справка", "cs": "Nápověda", "tr": "Yardım",
    },
    "help.tab_guide": {
        "en": "How it works", "hu": "Használat", "de": "So funktioniert’s", "fr": "Mode d’emploi",
        "es": "Cómo funciona", "it": "Come funziona", "pt": "Como funciona", "pl": "Jak to działa",
        "nl": "Zo werkt het", "ru": "Как пользоваться", "cs": "Jak to funguje", "tr": "Nasıl çalışır",
    },
    "help.tab_author": {
        "en": "Author", "hu": "Készítő", "de": "Entwickler", "fr": "Auteur", "es": "Autor", "it": "Autore",
        "pt": "Autor", "pl": "Autor", "nl": "Maker", "ru": "Автор", "cs": "Autor", "tr": "Geliştirici",
    },
    "help.official": {
        "en": "OFFICIAL WEBSITE", "hu": "HIVATALOS WEBOLDAL", "de": "OFFIZIELLE WEBSITE", "fr": "SITE OFFICIEL",
        "es": "SITIO OFICIAL", "it": "SITO UFFICIALE", "pt": "SITE OFICIAL", "pl": "OFICJALNA STRONA",
        "nl": "OFFICIËLE WEBSITE", "ru": "ОФИЦИАЛЬНЫЙ САЙТ", "cs": "OFICIÁLNÍ WEB", "tr": "RESMİ WEB SİTESİ",
    },
    "help.site_what": {
        "en": "Downloads, automatic updates, what’s new, the Claude Backup Kit, terms of use and privacy – all in one place.",
        "hu": "Letöltés, automatikus frissítések, újdonságok, a Claude Backup Kit, felhasználási feltételek és adatvédelem – egy helyen.",
        "de": "Downloads, automatische Updates, Neuigkeiten, das Claude Backup Kit, Nutzungsbedingungen und Datenschutz – alles an einem Ort.",
        "fr": "Téléchargements, mises à jour automatiques, nouveautés, le Claude Backup Kit, conditions d’utilisation et confidentialité – au même endroit.",
        "es": "Descargas, actualizaciones automáticas, novedades, el Claude Backup Kit, condiciones de uso y privacidad, todo en un solo lugar.",
        "it": "Download, aggiornamenti automatici, novità, il Claude Backup Kit, condizioni d’uso e privacy – tutto in un unico posto.",
        "pt": "Downloads, atualizações automáticas, novidades, o Claude Backup Kit, termos de uso e privacidade – tudo em um só lugar.",
        "pl": "Pobieranie, automatyczne aktualizacje, nowości, Claude Backup Kit, warunki korzystania i prywatność – wszystko w jednym miejscu.",
        "nl": "Downloads, automatische updates, nieuws, de Claude Backup Kit, gebruiksvoorwaarden en privacy – alles op één plek.",
        "ru": "Загрузки, автоматические обновления, новости, Claude Backup Kit, условия использования и конфиденциальность — всё в одном месте.",
        "cs": "Stahování, automatické aktualizace, novinky, Claude Backup Kit, podmínky používání a ochrana soukromí – vše na jednom místě.",
        "tr": "İndirmeler, otomatik güncellemeler, yenilikler, Claude Backup Kit, kullanım koşulları ve gizlilik – hepsi tek yerde.",
    },
    "help.moved": {
        "en": "New address since 21 September 2026 – the former dinorr.hu/claude-usage-monitor page redirects here.",
        "hu": "Új cím 2026. szeptember 21. óta – a korábbi dinorr.hu/claude-usage-monitor oldal ide irányít át.",
        "de": "Neue Adresse seit 21. September 2026 – die frühere Seite dinorr.hu/claude-usage-monitor leitet hierher weiter.",
        "fr": "Nouvelle adresse depuis le 21 septembre 2026 – l’ancienne page dinorr.hu/claude-usage-monitor redirige ici.",
        "es": "Nueva dirección desde el 21 de septiembre de 2026: la antigua página dinorr.hu/claude-usage-monitor redirige aquí.",
        "it": "Nuovo indirizzo dal 21 settembre 2026 – la vecchia pagina dinorr.hu/claude-usage-monitor reindirizza qui.",
        "pt": "Novo endereço desde 21 de setembro de 2026 – a antiga página dinorr.hu/claude-usage-monitor redireciona para cá.",
        "pl": "Nowy adres od 21 września 2026 – dawna strona dinorr.hu/claude-usage-monitor przekierowuje tutaj.",
        "nl": "Nieuw adres sinds 21 september 2026 – de oude pagina dinorr.hu/claude-usage-monitor verwijst hierheen.",
        "ru": "Новый адрес с 21 сентября 2026 г. — прежняя страница dinorr.hu/claude-usage-monitor перенаправляет сюда.",
        "cs": "Nová adresa od 21. září 2026 – dřívější stránka dinorr.hu/claude-usage-monitor sem přesměrovává.",
        "tr": "21 Eylül 2026’dan beri yeni adres – eski dinorr.hu/claude-usage-monitor sayfası buraya yönlendirir.",
    },
    "help.open_site": {
        "en": "Open claudeusagemonitor.com", "hu": "claudeusagemonitor.com megnyitása",
        "de": "claudeusagemonitor.com öffnen", "fr": "Ouvrir claudeusagemonitor.com", "es": "Abrir claudeusagemonitor.com",
        "it": "Apri claudeusagemonitor.com", "pt": "Abrir claudeusagemonitor.com", "pl": "Otwórz claudeusagemonitor.com",
        "nl": "claudeusagemonitor.com openen", "ru": "Открыть claudeusagemonitor.com", "cs": "Otevřít claudeusagemonitor.com",
        "tr": "claudeusagemonitor.com’u aç",
    },
    "help.made_by": {
        "en": "Made by", "hu": "Készítette", "de": "Entwickelt von", "fr": "Créé par", "es": "Creado por", "it": "Creato da",
        "pt": "Criado por", "pl": "Autor", "nl": "Gemaakt door", "ru": "Автор", "cs": "Vytvořil", "tr": "Geliştiren",
    },
    "help.version": {
        "en": "Version", "hu": "Verzió", "de": "Version", "fr": "Version", "es": "Versión", "it": "Versione",
        "pt": "Versão", "pl": "Wersja", "nl": "Versie", "ru": "Версия", "cs": "Verze", "tr": "Sürüm",
    },
    "help.free": {
        "en": "Free forever · MIT licence · open source · no telemetry",
        "hu": "Örökre ingyenes · MIT-licenc · nyílt forrás · nincs telemetria",
        "de": "Für immer kostenlos · MIT-Lizenz · Open Source · keine Telemetrie",
        "fr": "Gratuit pour toujours · licence MIT · open source · aucune télémétrie",
        "es": "Gratis para siempre · licencia MIT · código abierto · sin telemetría",
        "it": "Gratis per sempre · licenza MIT · open source · nessuna telemetria",
        "pt": "Grátis para sempre · licença MIT · código aberto · sem telemetria",
        "pl": "Na zawsze za darmo · licencja MIT · open source · bez telemetrii",
        "nl": "Voor altijd gratis · MIT-licentie · open source · geen telemetrie",
        "ru": "Бесплатно навсегда · лицензия MIT · открытый код · без телеметрии",
        "cs": "Navždy zdarma · licence MIT · open source · bez telemetrie",
        "tr": "Sonsuza dek ücretsiz · MIT lisansı · açık kaynak · telemetri yok",
    },
    "help.source_code": {
        "en": "Source code (GitHub)", "hu": "Forráskód (GitHub)", "de": "Quellcode (GitHub)", "fr": "Code source (GitHub)",
        "es": "Código fuente (GitHub)", "it": "Codice sorgente (GitHub)", "pt": "Código-fonte (GitHub)",
        "pl": "Kod źródłowy (GitHub)", "nl": "Broncode (GitHub)", "ru": "Исходный код (GitHub)",
        "cs": "Zdrojový kód (GitHub)", "tr": "Kaynak kodu (GitHub)",
    },
    "help.terms": {
        "en": "Terms of use", "hu": "Felhasználási feltételek", "de": "Nutzungsbedingungen", "fr": "Conditions d’utilisation",
        "es": "Condiciones de uso", "it": "Condizioni d’uso", "pt": "Termos de uso", "pl": "Warunki korzystania",
        "nl": "Gebruiksvoorwaarden", "ru": "Условия использования", "cs": "Podmínky používání", "tr": "Kullanım koşulları",
    },
    "help.privacy": {
        "en": "Privacy policy", "hu": "Adatkezelési tájékoztató", "de": "Datenschutzerklärung", "fr": "Politique de confidentialité",
        "es": "Política de privacidad", "it": "Informativa sulla privacy", "pt": "Política de privacidade",
        "pl": "Polityka prywatności", "nl": "Privacybeleid", "ru": "Политика конфиденциальности",
        "cs": "Zásady ochrany osobních údajů", "tr": "Gizlilik politikası",
    },
    "help.feedback": {
        "en": "Questions, ideas, bug reports: the message form on the website.",
        "hu": "Kérdés, ötlet, hibajelzés: az üzenetküldő űrlap a weboldalon.",
        "de": "Fragen, Ideen, Fehlermeldungen: das Nachrichtenformular auf der Website.",
        "fr": "Questions, idées, signalements de bugs : le formulaire de contact du site.",
        "es": "Preguntas, ideas, errores: el formulario de mensajes del sitio web.",
        "it": "Domande, idee, segnalazioni: il modulo di contatto sul sito.",
        "pt": "Dúvidas, ideias, relatos de erro: o formulário de mensagem no site.",
        "pl": "Pytania, pomysły, zgłoszenia błędów: formularz kontaktowy na stronie.",
        "nl": "Vragen, ideeën, foutmeldingen: het berichtformulier op de website.",
        "ru": "Вопросы, идеи, сообщения об ошибках — форма обратной связи на сайте.",
        "cs": "Dotazy, nápady, hlášení chyb: formulář pro zprávy na webu.",
        "tr": "Sorular, fikirler, hata bildirimleri: web sitesindeki mesaj formu.",
    },
    "help.disclaimer": {
        "en": "An independent, free tool – not made by or affiliated with Anthropic. “Claude” is a trademark of Anthropic.",
        "hu": "Független, ingyenes eszköz – nem az Anthropic készítette, és nem áll kapcsolatban vele. A „Claude” az Anthropic védjegye.",
        "de": "Ein unabhängiges, kostenloses Werkzeug – nicht von Anthropic und nicht mit Anthropic verbunden. „Claude“ ist eine Marke von Anthropic.",
        "fr": "Un outil indépendant et gratuit – ni créé par Anthropic ni affilié à Anthropic. « Claude » est une marque d’Anthropic.",
        "es": "Una herramienta independiente y gratuita: no está creada por Anthropic ni afiliada a ella. «Claude» es una marca de Anthropic.",
        "it": "Uno strumento indipendente e gratuito – non realizzato da Anthropic né affiliato. «Claude» è un marchio di Anthropic.",
        "pt": "Uma ferramenta independente e gratuita – não é feita pela Anthropic nem afiliada a ela. “Claude” é uma marca da Anthropic.",
        "pl": "Niezależne, darmowe narzędzie – nie jest tworzone przez Anthropic ani z nim powiązane. „Claude” jest znakiem towarowym Anthropic.",
        "nl": "Een onafhankelijk, gratis hulpmiddel – niet gemaakt door of verbonden aan Anthropic. ‘Claude’ is een handelsmerk van Anthropic.",
        "ru": "Независимый бесплатный инструмент — не создан Anthropic и не связан с ней. «Claude» — товарный знак Anthropic.",
        "cs": "Nezávislý bezplatný nástroj – nevytvořila ho společnost Anthropic ani s ní není spojen. „Claude“ je ochranná známka Anthropic.",
        "tr": "Bağımsız, ücretsiz bir araç – Anthropic tarafından yapılmamıştır ve Anthropic ile bağlantılı değildir. “Claude”, Anthropic’in ticari markasıdır.",
    },
    # ------------------------------------------------------------------ the guide (HTML)
    "help.guide": {
        "en": """
<h2>What the widget shows</h2>
<ul>
<li><b>5-hour session</b> – how much of your current session limit is used. It resets every five hours; the widget counts down to the reset.</li>
<li><b>Weekly limit</b> – usage across all models; it resets at a fixed weekly time of your account.</li>
<li><b>Per-model weekly limit</b> – a third gauge when the server reports one (e.g. for a specific model).</li>
<li><b>Pace and burn rate</b> – how fast you are using the limit and whether it will last until the reset; the end-of-week forecast warns in time.</li>
<li><b>Usage credits</b> and your plan badge – when you switch them on under <i>Plan badge and extra limits</i>.</li>
</ul>
<h2>Where the data comes from</h2>
<ul>
<li><b>claude.ai (all devices)</b> – asks Anthropic’s server, so usage on your phone, in the browser and on other computers is included. Needs a one-time sign-in in your own browser (menu: <i>Sign in</i>). Refreshes every 2 minutes, slower if the server asks for it.</li>
<li><b>Local (this PC only)</b> – reads the usage log of Claude Desktop on this computer. No sign-in, but it only knows this PC.</li>
</ul>
<p>Switch between them in the menu: <i>Data source</i>.</p>
<h2>Using the widget</h2>
<ul>
<li><b>Right-click</b> the widget (or the tray icon) – the full menu.</li>
<li><b>Double-click</b> a gauge – the <b>History</b> window: 6 hours, 24 hours, 7 days or everything, with peaks, daily average and a forecast.</li>
<li><b>Drag</b> to move it; it snaps to the screen edges. <b>Ctrl + mouse wheel</b> – bigger or smaller.</li>
<li>Layouts: post-it card, slim bar, rings; 6 themes. <i>Lock position</i> and <i>Click-through</i> are in the Settings.</li>
</ul>
<h2>Alerts</h2>
<p>Yellow from 70 %, red from 90 % (adjustable). Optional notifications when a limit resets and when the data is getting old.</p>
<h2>Backups (optional)</h2>
<p>The small lamps show whether your scheduled backups ran and finished. Click a lamp for the details. The monitor only reads the backup logs – making and testing the backups is your job (see the Terms of use).</p>
<h2>Updates</h2>
<p>The program checks for new versions by itself and updates in one click. Every package is checked with SHA-256 and comes only from <b>claudeusagemonitor.com</b>. New versions and release notes: {site}</p>
<h2>Privacy</h2>
<p>No telemetry, no tracking. The claude.ai sign-in is stored encrypted on this computer only; nothing is sent anywhere else.</p>
<h2>If something is wrong</h2>
<ul>
<li><i>429 / rate limited</i> – the server is slowing requests down; the program retries by itself.</li>
<li>No data – check the <i>Data source</i>; with claude.ai, sign in again.</li>
<li>History is kept for 7 days and survives restarts and updates.</li>
<li>Logs and settings: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>
</ul>
""",
        "hu": """
<h2>Mit mutat a widget</h2>
<ul>
<li><b>5 órás munkamenet</b> – az aktuális munkamenet limitjének mekkora része fogyott el. Ötóránként visszaáll; a widget visszaszámol a resetig.</li>
<li><b>Heti limit</b> – minden modell együtt; a fiókodhoz rögzített heti időpontban áll vissza.</li>
<li><b>Modellenkénti heti limit</b> – harmadik mérő, ha a szerver jelent ilyet (egy adott modellre).</li>
<li><b>Tempó és fogyási ütem</b> – milyen gyorsan fogy a limit, és kitart-e a resetig; a hét végi előrejelzés időben szól.</li>
<li><b>Használati kredit</b> és a csomagjelvény – ha bekapcsolod a <i>Csomagjelvény és további limitek</i> menüben.</li>
</ul>
<h2>Honnan jön az adat</h2>
<ul>
<li><b>claude.ai (minden eszköz)</b> – az Anthropic szerverétől kérdez, így a telefonon, böngészőben, másik gépen elhasznált rész is látszik. Egyszeri belépés kell a saját böngésződben (menü: <i>Bejelentkezés</i>). 2 percenként frissül, lassabban, ha a szerver ezt kéri.</li>
<li><b>Helyi (csak ez a gép)</b> – a Claude Desktop naplóját olvassa ezen a gépen. Nem kell belépni, de csak ezt a gépet ismeri.</li>
</ul>
<p>Váltás a menüben: <i>Adatforrás</i>.</p>
<h2>Kezelés</h2>
<ul>
<li><b>Jobb kattintás</b> a widgeten (vagy a tálcaikonon) – a teljes menü.</li>
<li><b>Dupla kattintás</b> egy mérőn – az <b>Előzmények</b> ablak: 6 óra, 24 óra, 7 nap vagy teljes, csúccsal, napi átlaggal és előrejelzéssel.</li>
<li><b>Húzással</b> mozgatható, a képernyő széléhez tapad. <b>Ctrl + egérgörgő</b> – nagyítás, kicsinyítés.</li>
<li>Elrendezések: post-it kártya, vékony sáv, körgyűrűk; 6 téma. <i>Pozíció rögzítése</i> és <i>Kattintás-átengedés</i> a Beállításokban.</li>
</ul>
<h2>Riasztások</h2>
<p>70 %-tól sárga, 90 %-tól piros (állítható). Kérhető értesítés, amikor egy limit visszaáll, és amikor az adat elavul.</p>
<h2>Mentések (nem kötelező)</h2>
<p>A kis lámpák mutatják, hogy az ütemezett mentéseid lefutottak-e és befejeződtek-e. Kattints egy lámpára a részletekért. A program csak a mentési naplókat olvassa – a mentés elkészítése és kipróbálása a te feladatod (lásd a Felhasználási feltételeket).</p>
<h2>Frissítések</h2>
<p>A program magától keres új verziót, és egy kattintással frissül. Minden csomagot SHA-256-tal ellenőriz, és kizárólag a <b>claudeusagemonitor.com</b>-ról tölt le. Új verziók és újdonságok: {site}</p>
<h2>Adatvédelem</h2>
<p>Nincs telemetria, nincs követés. A claude.ai-belépés titkosítva, csak ezen a gépen tárolódik; semmi nem megy máshová.</p>
<h2>Ha valami nem stimmel</h2>
<ul>
<li><i>429 / korlátozás</i> – a szerver lassítja a lekérdezéseket; a program magától újrapróbálja.</li>
<li>Nincs adat – nézd meg az <i>Adatforrás</i>t; claude.ai esetén jelentkezz be újra.</li>
<li>Az előzmények 7 napig megmaradnak, újraindítás és frissítés után is.</li>
<li>Naplók és beállítások: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>
</ul>
""",
        "de": """
<h2>Was das Widget zeigt</h2>
<ul>
<li><b>5-Stunden-Sitzung</b> – wie viel des Limits der aktuellen Sitzung verbraucht ist. Es wird alle fünf Stunden zurückgesetzt; das Widget zählt bis dahin herunter.</li>
<li><b>Wöchentliches Limit</b> – alle Modelle zusammen; wird zu einem festen wöchentlichen Zeitpunkt deines Kontos zurückgesetzt.</li>
<li><b>Wöchentliches Limit pro Modell</b> – eine dritte Anzeige, wenn der Server eines meldet.</li>
<li><b>Tempo und Verbrauchsrate</b> – wie schnell das Limit sinkt und ob es bis zum Zurücksetzen reicht; die Prognose zum Wochenende warnt rechtzeitig.</li>
<li><b>Nutzungsguthaben</b> und Tarif-Abzeichen – wenn du sie unter <i>Tarif-Abzeichen und weitere Limits</i> einschaltest.</li>
</ul>
<h2>Woher die Daten kommen</h2>
<ul>
<li><b>claude.ai (alle Geräte)</b> – fragt den Server von Anthropic, daher zählt auch die Nutzung auf dem Handy, im Browser und auf anderen Rechnern. Einmalige Anmeldung im eigenen Browser nötig (Menü: <i>Anmelden</i>). Aktualisiert alle 2 Minuten, langsamer, wenn der Server es verlangt.</li>
<li><b>Lokal (nur dieser PC)</b> – liest das Nutzungsprotokoll von Claude Desktop auf diesem Rechner. Ohne Anmeldung, kennt aber nur diesen PC.</li>
</ul>
<p>Umschalten im Menü: <i>Datenquelle</i>.</p>
<h2>Bedienung</h2>
<ul>
<li><b>Rechtsklick</b> auf das Widget (oder das Tray-Symbol) – das ganze Menü.</li>
<li><b>Doppelklick</b> auf eine Anzeige – das Fenster <b>Verlauf</b>: 6 Stunden, 24 Stunden, 7 Tage oder alles, mit Spitzen, Tagesdurchschnitt und Prognose.</li>
<li><b>Ziehen</b> zum Verschieben; rastet an den Bildschirmrändern ein. <b>Strg + Mausrad</b> – größer oder kleiner.</li>
<li>Layouts: Post-it-Karte, schmale Leiste, Ringe; 6 Designs. <i>Position fixieren</i> und <i>Klick-Durchlass</i> in den Einstellungen.</li>
</ul>
<h2>Warnungen</h2>
<p>Ab 70 % gelb, ab 90 % rot (einstellbar). Optionale Benachrichtigungen, wenn ein Limit zurückgesetzt wird und wenn die Daten veralten.</p>
<h2>Sicherungen (optional)</h2>
<p>Die kleinen Lämpchen zeigen, ob deine geplanten Sicherungen gelaufen und fertig sind. Klick auf ein Lämpchen für Details. Das Programm liest nur die Sicherungsprotokolle – Sicherungen anzulegen und zu testen ist deine Aufgabe (siehe Nutzungsbedingungen).</p>
<h2>Updates</h2>
<p>Das Programm sucht selbst nach neuen Versionen und aktualisiert mit einem Klick. Jedes Paket wird per SHA-256 geprüft und kommt nur von <b>claudeusagemonitor.com</b>. Neue Versionen und Neuigkeiten: {site}</p>
<h2>Datenschutz</h2>
<p>Keine Telemetrie, kein Tracking. Die claude.ai-Anmeldung wird verschlüsselt nur auf diesem Rechner gespeichert; nichts geht anderswohin.</p>
<h2>Wenn etwas nicht stimmt</h2>
<ul>
<li><i>429 / Begrenzung</i> – der Server bremst die Anfragen; das Programm versucht es selbst erneut.</li>
<li>Keine Daten – prüfe die <i>Datenquelle</i>; bei claude.ai erneut anmelden.</li>
<li>Der Verlauf bleibt 7 Tage erhalten, auch nach Neustart und Update.</li>
<li>Protokolle und Einstellungen: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>
</ul>
""",
        "fr": """
<h2>Ce qu’affiche le widget</h2>
<ul>
<li><b>Session de 5 heures</b> – la part utilisée de la limite de la session actuelle. Réinitialisation toutes les cinq heures ; le widget affiche le compte à rebours.</li>
<li><b>Limite hebdomadaire</b> – tous les modèles confondus ; réinitialisée à une heure hebdomadaire fixe propre à votre compte.</li>
<li><b>Limite hebdomadaire par modèle</b> – une troisième jauge quand le serveur en indique une.</li>
<li><b>Rythme et vitesse de consommation</b> – à quelle vitesse la limite baisse et si elle tiendra jusqu’à la réinitialisation ; la prévision de fin de semaine prévient à temps.</li>
<li><b>Crédits d’utilisation</b> et badge d’abonnement – si vous les activez dans <i>Badge d’abonnement et limites supplémentaires</i>.</li>
</ul>
<h2>D’où viennent les données</h2>
<ul>
<li><b>claude.ai (tous appareils)</b> – interroge le serveur d’Anthropic : l’usage sur téléphone, navigateur et autres ordinateurs est inclus. Une connexion unique dans votre propre navigateur est nécessaire (menu : <i>Se connecter</i>). Mise à jour toutes les 2 minutes, plus lentement si le serveur le demande.</li>
<li><b>Local (ce PC uniquement)</b> – lit le journal d’utilisation de Claude Desktop sur cet ordinateur. Sans connexion, mais ne connaît que ce PC.</li>
</ul>
<p>Changer dans le menu : <i>Source des données</i>.</p>
<h2>Utilisation</h2>
<ul>
<li><b>Clic droit</b> sur le widget (ou l’icône de la barre des tâches) – le menu complet.</li>
<li><b>Double-clic</b> sur une jauge – la fenêtre <b>Historique</b> : 6 heures, 24 heures, 7 jours ou tout, avec pics, moyenne journalière et prévision.</li>
<li><b>Glisser</b> pour déplacer ; il s’aimante aux bords de l’écran. <b>Ctrl + molette</b> – agrandir ou réduire.</li>
<li>Dispositions : carte post-it, barre fine, anneaux ; 6 thèmes. <i>Verrouiller la position</i> et <i>Clic traversant</i> dans les Réglages.</li>
</ul>
<h2>Alertes</h2>
<p>Jaune dès 70 %, rouge dès 90 % (réglable). Notifications facultatives à la réinitialisation d’une limite et quand les données deviennent anciennes.</p>
<h2>Sauvegardes (facultatif)</h2>
<p>Les petits voyants indiquent si vos sauvegardes planifiées ont tourné et se sont terminées. Cliquez sur un voyant pour les détails. Le programme lit seulement les journaux – réaliser et tester les sauvegardes reste votre responsabilité (voir les Conditions d’utilisation).</p>
<h2>Mises à jour</h2>
<p>Le programme cherche seul les nouvelles versions et se met à jour en un clic. Chaque paquet est vérifié par SHA-256 et provient uniquement de <b>claudeusagemonitor.com</b>. Nouvelles versions et nouveautés : {site}</p>
<h2>Confidentialité</h2>
<p>Aucune télémétrie, aucun pistage. La connexion claude.ai est stockée chiffrée sur cet ordinateur uniquement ; rien n’est envoyé ailleurs.</p>
<h2>En cas de problème</h2>
<ul>
<li><i>429 / limité</i> – le serveur ralentit les requêtes ; le programme réessaie tout seul.</li>
<li>Pas de données – vérifiez la <i>Source des données</i> ; avec claude.ai, reconnectez-vous.</li>
<li>L’historique est conservé 7 jours, même après redémarrage et mise à jour.</li>
<li>Journaux et réglages : <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>
</ul>
""",
        "es": """
<h2>Qué muestra el widget</h2>
<ul>
<li><b>Sesión de 5 horas</b> – cuánto se ha usado del límite de la sesión actual. Se reinicia cada cinco horas; el widget cuenta atrás hasta el reinicio.</li>
<li><b>Límite semanal</b> – todos los modelos juntos; se reinicia a una hora semanal fija de tu cuenta.</li>
<li><b>Límite semanal por modelo</b> – un tercer indicador cuando el servidor informa de uno.</li>
<li><b>Ritmo y velocidad de consumo</b> – lo rápido que baja el límite y si llegará hasta el reinicio; la previsión de fin de semana avisa a tiempo.</li>
<li><b>Créditos de uso</b> e insignia del plan – si los activas en <i>Insignia del plan y límites adicionales</i>.</li>
</ul>
<h2>De dónde vienen los datos</h2>
<ul>
<li><b>claude.ai (todos los dispositivos)</b> – consulta el servidor de Anthropic, así que incluye el uso en el móvil, el navegador y otros equipos. Requiere iniciar sesión una vez en tu propio navegador (menú: <i>Iniciar sesión</i>). Se actualiza cada 2 minutos, más despacio si el servidor lo pide.</li>
<li><b>Local (solo este PC)</b> – lee el registro de uso de Claude Desktop en este equipo. Sin inicio de sesión, pero solo conoce este PC.</li>
</ul>
<p>Cambia en el menú: <i>Origen de datos</i>.</p>
<h2>Uso</h2>
<ul>
<li><b>Clic derecho</b> en el widget (o en el icono de la bandeja) – el menú completo.</li>
<li><b>Doble clic</b> en un indicador – la ventana <b>Historial</b>: 6 horas, 24 horas, 7 días o todo, con picos, media diaria y previsión.</li>
<li><b>Arrastra</b> para moverlo; se ajusta a los bordes de la pantalla. <b>Ctrl + rueda</b> – más grande o más pequeño.</li>
<li>Diseños: nota adhesiva, barra fina, anillos; 6 temas. <i>Bloquear posición</i> y <i>Clic a través</i> están en Ajustes.</li>
</ul>
<h2>Alertas</h2>
<p>Amarillo desde el 70 %, rojo desde el 90 % (ajustable). Avisos opcionales cuando un límite se reinicia y cuando los datos se quedan antiguos.</p>
<h2>Copias de seguridad (opcional)</h2>
<p>Las pequeñas luces muestran si tus copias programadas se ejecutaron y terminaron. Haz clic en una luz para ver los detalles. El programa solo lee los registros: hacer y probar las copias es responsabilidad tuya (consulta las Condiciones de uso).</p>
<h2>Actualizaciones</h2>
<p>El programa busca nuevas versiones por sí mismo y se actualiza con un clic. Cada paquete se comprueba con SHA-256 y procede solo de <b>claudeusagemonitor.com</b>. Nuevas versiones y novedades: {site}</p>
<h2>Privacidad</h2>
<p>Sin telemetría ni seguimiento. El inicio de sesión de claude.ai se guarda cifrado solo en este equipo; no se envía nada a ningún otro sitio.</p>
<h2>Si algo falla</h2>
<ul>
<li><i>429 / limitado</i> – el servidor frena las solicitudes; el programa reintenta solo.</li>
<li>Sin datos – revisa el <i>Origen de datos</i>; con claude.ai, vuelve a iniciar sesión.</li>
<li>El historial se conserva 7 días, también tras reinicios y actualizaciones.</li>
<li>Registros y ajustes: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>
</ul>
""",
        "it": """
<h2>Cosa mostra il widget</h2>
<ul>
<li><b>Sessione di 5 ore</b> – quanto del limite della sessione attuale è stato usato. Si ripristina ogni cinque ore; il widget mostra il conto alla rovescia.</li>
<li><b>Limite settimanale</b> – tutti i modelli insieme; si ripristina a un orario settimanale fisso del tuo account.</li>
<li><b>Limite settimanale per modello</b> – un terzo indicatore quando il server ne segnala uno.</li>
<li><b>Ritmo e velocità di consumo</b> – quanto in fretta scende il limite e se basterà fino al ripristino; la previsione di fine settimana avvisa in tempo.</li>
<li><b>Crediti di utilizzo</b> e badge del piano – se li attivi in <i>Badge del piano e limiti aggiuntivi</i>.</li>
</ul>
<h2>Da dove arrivano i dati</h2>
<ul>
<li><b>claude.ai (tutti i dispositivi)</b> – interroga il server di Anthropic, quindi include l’uso su telefono, browser e altri computer. Serve un accesso una tantum nel tuo browser (menu: <i>Accedi</i>). Aggiorna ogni 2 minuti, più lentamente se il server lo richiede.</li>
<li><b>Locale (solo questo PC)</b> – legge il registro di utilizzo di Claude Desktop su questo computer. Nessun accesso, ma conosce solo questo PC.</li>
</ul>
<p>Si cambia dal menu: <i>Origine dati</i>.</p>
<h2>Uso</h2>
<ul>
<li><b>Clic destro</b> sul widget (o sull’icona nell’area di notifica) – il menu completo.</li>
<li><b>Doppio clic</b> su un indicatore – la finestra <b>Cronologia</b>: 6 ore, 24 ore, 7 giorni o tutto, con picchi, media giornaliera e previsione.</li>
<li><b>Trascina</b> per spostarlo; si aggancia ai bordi dello schermo. <b>Ctrl + rotellina</b> – più grande o più piccolo.</li>
<li>Layout: post-it, barra sottile, anelli; 6 temi. <i>Blocca posizione</i> e <i>Clic passante</i> nelle Impostazioni.</li>
</ul>
<h2>Avvisi</h2>
<p>Giallo dal 70 %, rosso dal 90 % (regolabile). Notifiche facoltative quando un limite si ripristina e quando i dati diventano vecchi.</p>
<h2>Backup (facoltativo)</h2>
<p>Le piccole spie mostrano se i backup pianificati sono stati eseguiti e completati. Clicca su una spia per i dettagli. Il programma legge solo i registri: creare e verificare i backup è compito tuo (vedi le Condizioni d’uso).</p>
<h2>Aggiornamenti</h2>
<p>Il programma cerca da solo le nuove versioni e si aggiorna con un clic. Ogni pacchetto è verificato con SHA-256 e proviene solo da <b>claudeusagemonitor.com</b>. Nuove versioni e novità: {site}</p>
<h2>Privacy</h2>
<p>Nessuna telemetria, nessun tracciamento. L’accesso a claude.ai è salvato cifrato solo su questo computer; nulla viene inviato altrove.</p>
<h2>Se qualcosa non va</h2>
<ul>
<li><i>429 / limitato</i> – il server rallenta le richieste; il programma riprova da solo.</li>
<li>Nessun dato – controlla l’<i>Origine dati</i>; con claude.ai, accedi di nuovo.</li>
<li>La cronologia resta per 7 giorni, anche dopo riavvii e aggiornamenti.</li>
<li>Registri e impostazioni: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>
</ul>
""",
        "pt": """
<h2>O que o widget mostra</h2>
<ul>
<li><b>Sessão de 5 horas</b> – quanto do limite da sessão atual já foi usado. É redefinido a cada cinco horas; o widget faz a contagem regressiva.</li>
<li><b>Limite semanal</b> – todos os modelos juntos; é redefinido num horário semanal fixo da sua conta.</li>
<li><b>Limite semanal por modelo</b> – um terceiro medidor quando o servidor informa um.</li>
<li><b>Ritmo e taxa de consumo</b> – quão rápido o limite cai e se durará até a redefinição; a previsão de fim de semana avisa a tempo.</li>
<li><b>Créditos de uso</b> e selo do plano – se você os ativar em <i>Selo do plano e limites extras</i>.</li>
</ul>
<h2>De onde vêm os dados</h2>
<ul>
<li><b>claude.ai (todos os dispositivos)</b> – consulta o servidor da Anthropic, então inclui o uso no celular, no navegador e em outros computadores. Exige um login único no seu próprio navegador (menu: <i>Entrar</i>). Atualiza a cada 2 minutos, mais devagar se o servidor pedir.</li>
<li><b>Local (só este PC)</b> – lê o registro de uso do Claude Desktop neste computador. Sem login, mas só conhece este PC.</li>
</ul>
<p>Troque no menu: <i>Origem dos dados</i>.</p>
<h2>Uso</h2>
<ul>
<li><b>Clique direito</b> no widget (ou no ícone da bandeja) – o menu completo.</li>
<li><b>Clique duplo</b> num medidor – a janela <b>Histórico</b>: 6 horas, 24 horas, 7 dias ou tudo, com picos, média diária e previsão.</li>
<li><b>Arraste</b> para mover; ele se encaixa nas bordas da tela. <b>Ctrl + roda do mouse</b> – maior ou menor.</li>
<li>Layouts: post-it, barra fina, anéis; 6 temas. <i>Travar posição</i> e <i>Clique através</i> ficam nas Configurações.</li>
</ul>
<h2>Alertas</h2>
<p>Amarelo a partir de 70 %, vermelho a partir de 90 % (ajustável). Notificações opcionais quando um limite é redefinido e quando os dados ficam antigos.</p>
<h2>Backups (opcional)</h2>
<p>As pequenas luzes mostram se seus backups agendados rodaram e terminaram. Clique numa luz para ver os detalhes. O programa só lê os registros – fazer e testar os backups é tarefa sua (veja os Termos de uso).</p>
<h2>Atualizações</h2>
<p>O programa procura novas versões sozinho e atualiza com um clique. Cada pacote é verificado com SHA-256 e vem somente de <b>claudeusagemonitor.com</b>. Novas versões e novidades: {site}</p>
<h2>Privacidade</h2>
<p>Sem telemetria, sem rastreamento. O login do claude.ai fica guardado criptografado só neste computador; nada é enviado para outro lugar.</p>
<h2>Se algo der errado</h2>
<ul>
<li><i>429 / limitado</i> – o servidor está freando as requisições; o programa tenta de novo sozinho.</li>
<li>Sem dados – confira a <i>Origem dos dados</i>; com o claude.ai, entre novamente.</li>
<li>O histórico é mantido por 7 dias, mesmo após reinícios e atualizações.</li>
<li>Registros e configurações: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>
</ul>
""",
        "pl": """
<h2>Co pokazuje widżet</h2>
<ul>
<li><b>Sesja 5-godzinna</b> – ile limitu bieżącej sesji zużyto. Resetuje się co pięć godzin; widżet odlicza czas do resetu.</li>
<li><b>Limit tygodniowy</b> – wszystkie modele razem; resetuje się o stałej porze tygodnia przypisanej do konta.</li>
<li><b>Tygodniowy limit modelu</b> – trzeci wskaźnik, gdy serwer go podaje.</li>
<li><b>Tempo i szybkość zużycia</b> – jak szybko ubywa limitu i czy wystarczy do resetu; prognoza na koniec tygodnia ostrzega na czas.</li>
<li><b>Kredyty użycia</b> i odznaka planu – po włączeniu w <i>Odznaka planu i dodatkowe limity</i>.</li>
</ul>
<h2>Skąd pochodzą dane</h2>
<ul>
<li><b>claude.ai (wszystkie urządzenia)</b> – pyta serwer Anthropic, więc liczy też użycie na telefonie, w przeglądarce i na innych komputerach. Wymaga jednorazowego logowania we własnej przeglądarce (menu: <i>Zaloguj</i>). Odświeża co 2 minuty, wolniej, gdy serwer o to prosi.</li>
<li><b>Lokalnie (tylko ten PC)</b> – czyta dziennik użycia Claude Desktop na tym komputerze. Bez logowania, ale zna tylko ten PC.</li>
</ul>
<p>Przełączanie w menu: <i>Źródło danych</i>.</p>
<h2>Obsługa</h2>
<ul>
<li><b>Prawy przycisk</b> na widżecie (lub ikonie w zasobniku) – pełne menu.</li>
<li><b>Dwuklik</b> na wskaźniku – okno <b>Historia</b>: 6 godzin, 24 godziny, 7 dni lub całość, ze szczytami, średnią dzienną i prognozą.</li>
<li><b>Przeciągnij</b>, aby przesunąć; przykleja się do krawędzi ekranu. <b>Ctrl + kółko myszy</b> – większy lub mniejszy.</li>
<li>Układy: karteczka, cienki pasek, pierścienie; 6 motywów. <i>Zablokuj pozycję</i> i <i>Przepuszczanie kliknięć</i> w Ustawieniach.</li>
</ul>
<h2>Alerty</h2>
<p>Żółty od 70 %, czerwony od 90 % (do ustawienia). Opcjonalne powiadomienia o resecie limitu i o starzejących się danych.</p>
<h2>Kopie zapasowe (opcjonalnie)</h2>
<p>Małe lampki pokazują, czy zaplanowane kopie się wykonały i zakończyły. Kliknij lampkę, aby zobaczyć szczegóły. Program tylko czyta dzienniki – wykonanie i testowanie kopii to twoje zadanie (zob. Warunki korzystania).</p>
<h2>Aktualizacje</h2>
<p>Program sam szuka nowych wersji i aktualizuje się jednym kliknięciem. Każdy pakiet jest sprawdzany SHA-256 i pochodzi wyłącznie z <b>claudeusagemonitor.com</b>. Nowe wersje i nowości: {site}</p>
<h2>Prywatność</h2>
<p>Bez telemetrii i śledzenia. Logowanie do claude.ai jest przechowywane w postaci zaszyfrowanej tylko na tym komputerze; nic nie jest wysyłane nigdzie indziej.</p>
<h2>Gdy coś nie działa</h2>
<ul>
<li><i>429 / ograniczenie</i> – serwer spowalnia zapytania; program sam ponawia próbę.</li>
<li>Brak danych – sprawdź <i>Źródło danych</i>; przy claude.ai zaloguj się ponownie.</li>
<li>Historia jest przechowywana 7 dni, także po restarcie i aktualizacji.</li>
<li>Dzienniki i ustawienia: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>
</ul>
""",
        "nl": """
<h2>Wat de widget laat zien</h2>
<ul>
<li><b>5-uurssessie</b> – hoeveel van de limiet van de huidige sessie is gebruikt. Wordt elke vijf uur gereset; de widget telt af tot de reset.</li>
<li><b>Weeklimiet</b> – alle modellen samen; wordt gereset op een vast wekelijks tijdstip van je account.</li>
<li><b>Weeklimiet per model</b> – een derde meter als de server er een meldt.</li>
<li><b>Tempo en verbruikssnelheid</b> – hoe snel de limiet daalt en of die tot de reset volstaat; de prognose voor het weekeinde waarschuwt op tijd.</li>
<li><b>Gebruikstegoed</b> en abonnementsbadge – als je ze inschakelt onder <i>Abonnementsbadge en extra limieten</i>.</li>
</ul>
<h2>Waar de gegevens vandaan komen</h2>
<ul>
<li><b>claude.ai (alle apparaten)</b> – vraagt de server van Anthropic, dus gebruik op je telefoon, in de browser en op andere computers telt mee. Eenmalig inloggen in je eigen browser (menu: <i>Inloggen</i>). Ververst elke 2 minuten, trager als de server daarom vraagt.</li>
<li><b>Lokaal (alleen deze pc)</b> – leest het gebruikslogboek van Claude Desktop op deze computer. Zonder inloggen, maar kent alleen deze pc.</li>
</ul>
<p>Wisselen via het menu: <i>Gegevensbron</i>.</p>
<h2>Bediening</h2>
<ul>
<li><b>Rechtsklik</b> op de widget (of het systeemvakpictogram) – het volledige menu.</li>
<li><b>Dubbelklik</b> op een meter – het venster <b>Geschiedenis</b>: 6 uur, 24 uur, 7 dagen of alles, met pieken, daggemiddelde en prognose.</li>
<li><b>Sleep</b> om te verplaatsen; klikt vast aan de schermranden. <b>Ctrl + muiswiel</b> – groter of kleiner.</li>
<li>Indelingen: post-it, smalle balk, ringen; 6 thema’s. <i>Positie vergrendelen</i> en <i>Doorklikken</i> staan in de Instellingen.</li>
</ul>
<h2>Waarschuwingen</h2>
<p>Geel vanaf 70 %, rood vanaf 90 % (instelbaar). Optionele meldingen wanneer een limiet wordt gereset en wanneer de gegevens verouderen.</p>
<h2>Back-ups (optioneel)</h2>
<p>De kleine lampjes tonen of je geplande back-ups zijn gedraaid en voltooid. Klik op een lampje voor details. Het programma leest alleen de logboeken – back-ups maken en testen is jouw taak (zie de Gebruiksvoorwaarden).</p>
<h2>Updates</h2>
<p>Het programma zoekt zelf naar nieuwe versies en werkt bij met één klik. Elk pakket wordt met SHA-256 gecontroleerd en komt alleen van <b>claudeusagemonitor.com</b>. Nieuwe versies en nieuws: {site}</p>
<h2>Privacy</h2>
<p>Geen telemetrie, geen tracking. De claude.ai-login wordt versleuteld alleen op deze computer bewaard; er wordt niets ergens anders heen gestuurd.</p>
<h2>Als er iets misgaat</h2>
<ul>
<li><i>429 / beperkt</i> – de server remt verzoeken af; het programma probeert het zelf opnieuw.</li>
<li>Geen gegevens – controleer de <i>Gegevensbron</i>; bij claude.ai opnieuw inloggen.</li>
<li>De geschiedenis blijft 7 dagen bewaard, ook na herstarts en updates.</li>
<li>Logboeken en instellingen: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>
</ul>
""",
        "ru": """
<h2>Что показывает виджет</h2>
<ul>
<li><b>5-часовой сеанс</b> — какая часть лимита текущего сеанса израсходована. Сбрасывается каждые пять часов; виджет ведёт обратный отсчёт до сброса.</li>
<li><b>Еженедельный лимит</b> — все модели вместе; сбрасывается в фиксированное недельное время вашей учётной записи.</li>
<li><b>Еженедельный лимит модели</b> — третий индикатор, если сервер его сообщает.</li>
<li><b>Темп и скорость расхода</b> — как быстро уходит лимит и хватит ли его до сброса; прогноз на конец недели предупредит заранее.</li>
<li><b>Кредиты использования</b> и значок тарифа — если включить их в меню <i>Значок тарифа и дополнительные лимиты</i>.</li>
</ul>
<h2>Откуда берутся данные</h2>
<ul>
<li><b>claude.ai (все устройства)</b> — запрашивает сервер Anthropic, поэтому учитывается использование на телефоне, в браузере и на других компьютерах. Нужен однократный вход в собственном браузере (меню: <i>Войти</i>). Обновляется каждые 2 минуты, реже, если сервер просит.</li>
<li><b>Локально (только этот ПК)</b> — читает журнал использования Claude Desktop на этом компьютере. Без входа, но знает только этот ПК.</li>
</ul>
<p>Переключение в меню: <i>Источник данных</i>.</p>
<h2>Управление</h2>
<ul>
<li><b>Правый щелчок</b> по виджету (или значку в трее) — полное меню.</li>
<li><b>Двойной щелчок</b> по индикатору — окно <b>История</b>: 6 часов, 24 часа, 7 дней или всё, с пиками, средним за день и прогнозом.</li>
<li><b>Перетаскивание</b> — перемещение; прилипает к краям экрана. <b>Ctrl + колесо мыши</b> — крупнее или мельче.</li>
<li>Макеты: стикер, тонкая полоса, кольца; 6 тем. <i>Закрепить положение</i> и <i>Сквозной щелчок</i> — в Настройках.</li>
</ul>
<h2>Предупреждения</h2>
<p>Жёлтый от 70 %, красный от 90 % (настраивается). Необязательные уведомления при сбросе лимита и когда данные устаревают.</p>
<h2>Резервные копии (необязательно)</h2>
<p>Маленькие лампочки показывают, выполнились ли запланированные копии и завершились ли они. Щёлкните лампочку, чтобы увидеть подробности. Программа только читает журналы — создавать и проверять копии должны вы сами (см. Условия использования).</p>
<h2>Обновления</h2>
<p>Программа сама ищет новые версии и обновляется одним щелчком. Каждый пакет проверяется по SHA-256 и загружается только с <b>claudeusagemonitor.com</b>. Новые версии и новости: {site}</p>
<h2>Конфиденциальность</h2>
<p>Никакой телеметрии и слежки. Вход в claude.ai хранится в зашифрованном виде только на этом компьютере; ничего никуда не отправляется.</p>
<h2>Если что-то не так</h2>
<ul>
<li><i>429 / ограничение</i> — сервер замедляет запросы; программа повторит сама.</li>
<li>Нет данных — проверьте <i>Источник данных</i>; для claude.ai войдите снова.</li>
<li>История хранится 7 дней, в том числе после перезапуска и обновления.</li>
<li>Журналы и настройки: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>
</ul>
""",
        "cs": """
<h2>Co widget ukazuje</h2>
<ul>
<li><b>5hodinová relace</b> – kolik z limitu aktuální relace je spotřebováno. Resetuje se každých pět hodin; widget odpočítává čas do resetu.</li>
<li><b>Týdenní limit</b> – všechny modely dohromady; resetuje se v pevný týdenní čas vašeho účtu.</li>
<li><b>Týdenní limit modelu</b> – třetí ukazatel, pokud ho server hlásí.</li>
<li><b>Tempo a rychlost spotřeby</b> – jak rychle limit ubývá a zda vydrží do resetu; předpověď na konec týdne včas upozorní.</li>
<li><b>Kredity za využití</b> a odznak tarifu – pokud je zapnete v <i>Odznak tarifu a další limity</i>.</li>
</ul>
<h2>Odkud jsou data</h2>
<ul>
<li><b>claude.ai (všechna zařízení)</b> – ptá se serveru Anthropic, takže započítá i využití v telefonu, v prohlížeči a na jiných počítačích. Vyžaduje jednorázové přihlášení ve vlastním prohlížeči (menu: <i>Přihlásit</i>). Obnovuje se každé 2 minuty, pomaleji, když o to server požádá.</li>
<li><b>Místní (jen tento PC)</b> – čte protokol využití Claude Desktop na tomto počítači. Bez přihlášení, ale zná jen tento PC.</li>
</ul>
<p>Přepnutí v menu: <i>Zdroj dat</i>.</p>
<h2>Ovládání</h2>
<ul>
<li><b>Pravé tlačítko</b> na widgetu (nebo ikoně v oznamovací oblasti) – celé menu.</li>
<li><b>Dvojklik</b> na ukazatel – okno <b>Historie</b>: 6 hodin, 24 hodin, 7 dní nebo vše, se špičkami, denním průměrem a předpovědí.</li>
<li><b>Přetažením</b> se přesouvá; přichytí se k okrajům obrazovky. <b>Ctrl + kolečko myši</b> – větší nebo menší.</li>
<li>Rozvržení: lístek, úzký pruh, prstence; 6 motivů. <i>Zamknout polohu</i> a <i>Propouštění kliknutí</i> jsou v Nastavení.</li>
</ul>
<h2>Upozornění</h2>
<p>Žlutá od 70 %, červená od 90 % (nastavitelné). Volitelná oznámení při resetu limitu a když data zastarávají.</p>
<h2>Zálohy (volitelné)</h2>
<p>Malé kontrolky ukazují, zda naplánované zálohy proběhly a skončily. Klikněte na kontrolku pro podrobnosti. Program jen čte protokoly – vytvořit a vyzkoušet zálohy je váš úkol (viz Podmínky používání).</p>
<h2>Aktualizace</h2>
<p>Program sám hledá nové verze a aktualizuje se jedním kliknutím. Každý balíček ověřuje pomocí SHA-256 a stahuje výhradně z <b>claudeusagemonitor.com</b>. Nové verze a novinky: {site}</p>
<h2>Soukromí</h2>
<p>Žádná telemetrie, žádné sledování. Přihlášení ke claude.ai se ukládá šifrovaně jen na tomto počítači; nic se nikam jinam neposílá.</p>
<h2>Když něco nefunguje</h2>
<ul>
<li><i>429 / omezení</i> – server zpomaluje dotazy; program to zkusí znovu sám.</li>
<li>Žádná data – zkontrolujte <i>Zdroj dat</i>; u claude.ai se přihlaste znovu.</li>
<li>Historie se uchovává 7 dní, i po restartu a aktualizaci.</li>
<li>Protokoly a nastavení: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>
</ul>
""",
        "tr": """
<h2>Widget neyi gösterir</h2>
<ul>
<li><b>5 saatlik oturum</b> – mevcut oturum limitinin ne kadarının kullanıldığı. Beş saatte bir sıfırlanır; widget sıfırlanmaya kadar geri sayar.</li>
<li><b>Haftalık limit</b> – tüm modeller birlikte; hesabınıza ait sabit bir haftalık saatte sıfırlanır.</li>
<li><b>Model başına haftalık limit</b> – sunucu bildirirse üçüncü bir gösterge.</li>
<li><b>Tempo ve tüketim hızı</b> – limitin ne kadar hızlı azaldığı ve sıfırlanmaya kadar yetip yetmeyeceği; hafta sonu tahmini zamanında uyarır.</li>
<li><b>Kullanım kredileri</b> ve plan rozeti – <i>Plan rozeti ve ek limitler</i> altında açarsanız.</li>
</ul>
<h2>Veriler nereden gelir</h2>
<ul>
<li><b>claude.ai (tüm cihazlar)</b> – Anthropic sunucusuna sorar; telefonda, tarayıcıda ve diğer bilgisayarlarda yapılan kullanım da dahildir. Kendi tarayıcınızda tek seferlik giriş gerekir (menü: <i>Giriş yap</i>). 2 dakikada bir yenilenir, sunucu isterse daha yavaş.</li>
<li><b>Yerel (yalnızca bu PC)</b> – bu bilgisayardaki Claude Desktop kullanım günlüğünü okur. Giriş gerekmez, ama yalnızca bu PC’yi bilir.</li>
</ul>
<p>Menüden değiştirin: <i>Veri kaynağı</i>.</p>
<h2>Kullanım</h2>
<ul>
<li>Widget’a (veya tepsi simgesine) <b>sağ tıklayın</b> – tam menü.</li>
<li>Bir göstergeye <b>çift tıklayın</b> – <b>Geçmiş</b> penceresi: 6 saat, 24 saat, 7 gün veya tümü; zirveler, günlük ortalama ve tahminle.</li>
<li>Taşımak için <b>sürükleyin</b>; ekran kenarlarına yapışır. <b>Ctrl + fare tekerleği</b> – büyüt veya küçült.</li>
<li>Düzenler: yapışkan not, ince çubuk, halkalar; 6 tema. <i>Konumu kilitle</i> ve <i>Tıklamayı geçir</i> Ayarlar’dadır.</li>
</ul>
<h2>Uyarılar</h2>
<p>%70’ten itibaren sarı, %90’dan itibaren kırmızı (ayarlanabilir). Bir limit sıfırlandığında ve veriler eskidiğinde isteğe bağlı bildirimler.</p>
<h2>Yedekler (isteğe bağlı)</h2>
<p>Küçük lambalar zamanlanmış yedeklerinizin çalışıp bitip bitmediğini gösterir. Ayrıntılar için bir lambaya tıklayın. Program yalnızca günlükleri okur – yedek almak ve denemek sizin sorumluluğunuzdadır (Kullanım koşullarına bakın).</p>
<h2>Güncellemeler</h2>
<p>Program yeni sürümleri kendisi arar ve tek tıkla güncellenir. Her paket SHA-256 ile doğrulanır ve yalnızca <b>claudeusagemonitor.com</b> adresinden gelir. Yeni sürümler ve yenilikler: {site}</p>
<h2>Gizlilik</h2>
<p>Telemetri yok, izleme yok. claude.ai girişi şifrelenmiş olarak yalnızca bu bilgisayarda saklanır; hiçbir şey başka bir yere gönderilmez.</p>
<h2>Bir sorun olursa</h2>
<ul>
<li><i>429 / sınırlandı</i> – sunucu istekleri yavaşlatıyor; program kendisi yeniden dener.</li>
<li>Veri yok – <i>Veri kaynağı</i>nı kontrol edin; claude.ai ile yeniden giriş yapın.</li>
<li>Geçmiş 7 gün saklanır; yeniden başlatma ve güncellemeden sonra da.</li>
<li>Günlükler ve ayarlar: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>
</ul>
""",
    },
}
