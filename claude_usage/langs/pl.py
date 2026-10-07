# -*- coding: utf-8 -*-
"""Polski – UI strings of Claude Usage Monitor (only the keys missing from the inline i18n*.py tables)."""

CODE = "pl"
NAME = "Polski"

STRINGS = {
    "menu.feedback": "Wiadomość do autora…",
    "set.show_feedback_icon": "Ikona wiadomości w nagłówku panelu",
    "fb.title": "Wiadomość do autora",
    "fb.intro": "Pomysł, błąd, a może program po prostu Ci się podoba? Napisz do mnie. Każdą wiadomość czytam osobiście – Vidovics Gábor, autor programu.",
    "fb.name": "Imię",
    "fb.email": "E-mail",
    "fb.email_hint": "tylko jeśli chcesz otrzymać odpowiedź",
    "fb.optional": "(opcjonalnie)",
    "fb.message": "Wiadomość",
    "fb.message_ph": "Co działa, co nie działa, czego brakuje?",
    "fb.rating": "Ocena ogólna",
    "fb.rating_hint": "opcjonalnie – kliknij gwiazdkę",
    "fb.rating_tip": "{} z 5",
    "fb.rating_clear": "wyczyść",
    "fb.publish": "Moja ocena i imię (jeśli je podano) mogą być widoczne na stronie claudeusagemonitor.com.",
    "fb.consent": "Przeczytałem(-am) i akceptuję: {}.",
    "fb.privacy_title": "Polityka prywatności",
    "fb.privacy_hide": "Ukryj politykę",
    "fb.privacy_text": (
        "Administrator danych: Vidovics Gábor, osoba fizyczna (Węgry), autor programu Claude Usage Monitor. "
        "Pełna polityka prywatności znajduje się na stronie internetowej: https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "Co jest wysyłane: to, co tutaj wpiszesz – imię (opcjonalnie), adres e-mail (opcjonalnie), wiadomość, "
        "ocena w gwiazdkach – oraz, abym mógł zrozumieć kontekst: wersja programu, nazwa i wersja systemu "
        "operacyjnego, język interfejsu i czas wysłania. Serwer nie przechowuje adresu IP; w celu zapobiegania "
        "nadużyciom używa jedynie zmieniającego się codziennie skrótu (hasha), którego nie da się odwrócić "
        "do postaci adresu."
        "\n\n"
        "W jakim celu: aby przeczytać Twoją wiadomość i na nią odpowiedzieć oraz aby ulepszać program "
        "(prawnie uzasadniony interes, art. 6 ust. 1 lit. f RODO; sama odpowiedź – na Twoją prośbę). "
        "Twoja ocena i Twoje imię pojawią się na stronie internetowej tylko wtedy, gdy zaznaczysz osobne "
        "pole wyboru (zgoda, art. 6 ust. 1 lit. a RODO), i dopiero po sprawdzeniu przez autora; zgodę możesz "
        "wycofać w dowolnym momencie."
        "\n\n"
        "Jak długo: wiadomości – nie dłużej niż 2 lata; opublikowana ocena – do czasu wycofania zgody. Jeśli "
        "autor włączył przekazywanie wiadomości na e-mail, kopia trafia także do jego skrzynki pocztowej."
        "\n\n"
        "Kto ma dostęp: wyłącznie administrator oraz – jako podmiot przetwarzający – dostawca hostingu "
        "(serwer w UE, w Niemczech). Dane nie są sprzedawane ani przekazywane dalej; nie podlegają "
        "profilowaniu ani zautomatyzowanemu podejmowaniu decyzji."
        "\n\n"
        "Twoje prawa: dostęp do danych, ich sprostowanie, usunięcie, ograniczenie przetwarzania, sprzeciw, "
        "wycofanie zgody oraz wniesienie skargi do organu nadzorczego (na Węgrzech: NAIH, naih.hu) lub do "
        "organu nadzorczego w Twoim kraju (w Polsce: Prezes UODO, uodo.gov.pl). Kontakt: ten formularz lub "
        "strona internetowa."
        "\n\n"
        "Przesyłanie danych: szyfrowane (HTTPS/TLS) do claudeusagemonitor.com. Wersja tej polityki: "
        "6 października 2026 r."
    ),
    "fb.secure": "Szyfrowane połączenie (HTTPS) z claudeusagemonitor.com.",
    "fb.meta": "Razem z wiadomością wysyłane są: wersja programu ({0}), system operacyjny ({1}), język interfejsu ({2}).",
    "fb.send": "Wyślij",
    "fb.sending": "Wysyłanie…",
    "fb.cancel": "Anuluj",
    "fb.close": "Zamknij",
    "fb.sent": "Dziękuję – wiadomość dotarła!",
    "fb.sent_sub": "Czytam każdą wiadomość. Jeśli podano adres e-mail, odpowiem na niego.",
    "fb.err_empty": "Najpierw napisz wiadomość lub wybierz ocenę.",
    "fb.err_consent": "Aby wysłać wiadomość, zaakceptuj politykę prywatności.",
    "fb.err_email": "Ten adres e-mail wygląda na nieprawidłowy.",
    "fb.err_links": "Wiadomość zawiera zbyt wiele linków.",
    "fb.err_rate": "Zbyt wiele wiadomości w krótkim czasie – spróbuj ponownie później.",
    "fb.err_network": "Nie można połączyć się z claudeusagemonitor.com. Sprawdź połączenie i spróbuj ponownie.",
    "fb.err_server": "Serwer nie może teraz przyjąć wiadomości. Spróbuj ponownie później.",
}

# The four macOS keys already have their Polish wording inline in i18n_mac.py – nothing to add here.
STRINGS_MAC = {}
