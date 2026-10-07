# Glossary – Polish (pl)

Scope: only the "Message to the developer" window (`fb.*`, `menu.feedback`, `set.show_feedback_icon`).
The rest of the Polish UI already lives inline in `claude_usage/i18n*.py`; these terms follow it.

## Tone and form of address

- **Informal "ty"**, as the existing Polish strings do ("Zaloguj się…", "Sprawdź połączenie", "spróbuj ponownie").
- **Capitalised courtesy forms** – "Ty", "Twój", "Twoja", "Ci", "Ciebie" – as in the existing backup texts
  ("dzienniki Twojej kopii zapasowej", "należy do Ciebie"). This is the standard polite spelling of Polish
  consumer software and legal notices. (One older inline string uses lowercase "twoje" – see REVIEW.)
- Gendered past-tense forms are avoided where a neutral phrasing exists ("jeśli zostało podane", "jeśli w
  formularzu jest adres e-mail"); where unavoidable, the usual "(-am)" suffix is used ("Przeczytałem(-am)").
- Short, friendly, confident; the author speaks in the first person ("Napisz do mnie", "czytam osobiście").

## Privacy document name

**Polityka prywatności** – the term used by every major platform in Polish (Google, Microsoft, Apple, Meta)
and by the Polish supervisory authority (UODO). "Informacja o przetwarzaniu danych" / "klauzula informacyjna"
are the RODO-technical names, but users recognise and expect "Polityka prywatności" on a link and a checkbox.

## Terms

| English | Polish | Note |
|---|---|---|
| Message to the developer | Wiadomość do autora | "autor programu" matches the intro; "deweloper" is Google-Play jargon, "twórca" is the alternative |
| developer / author | autor (programu) | first person in the intro: "Vidovics Gábor, autor programu" |
| message | wiadomość | |
| rating / overall rating | ocena / ocena ogólna | |
| star rating | ocena w gwiazdkach | |
| click a star | kliknij gwiazdkę | |
| clear (rating) | wyczyść | lowercase, small link |
| optional | opcjonalnie / (opcjonalnie) | not "nieobowiązkowe" |
| name | imię | first name is what a Polish feedback form asks for; "imię i nazwisko" would be formal |
| e-mail / e-mail address | e-mail / adres e-mail | hyphenated, per PWN |
| send / sending… | Wyślij / Wysyłanie… | |
| cancel / close | Anuluj / Zamknij | Microsoft Polish terminology |
| privacy notice | Polityka prywatności | see above |
| hide the notice | Ukryj politykę | short button; full name stays in title/link |
| consent | zgoda | "wycofać zgodę" = withdraw consent |
| I have read and accept | Przeczytałem(-am) i akceptuję | |
| controller | administrator (danych) | RODO term |
| processor | podmiot przetwarzający | RODO term |
| hosting provider | dostawca hostingu | |
| legitimate interest | prawnie uzasadniony interes | RODO art. 6 ust. 1 lit. f |
| GDPR Art. 6(1)(f) | art. 6 ust. 1 lit. f RODO | Polish citation style |
| supervisory authority | organ nadzorczy | in Poland: Prezes UODO |
| profiling / automated decision-making | profilowanie / zautomatyzowane podejmowanie decyzji | RODO wording |
| rights: access, rectification, erasure, restriction, objection | dostęp do danych, sprostowanie, usunięcie, ograniczenie przetwarzania, sprzeciw | RODO art. 15–21 wording |
| hash | skrót (hash) | |
| encrypted connection | szyfrowane połączenie | |
| program version / operating system / interface language | wersja programu / system operacyjny / język interfejsu | |
| panel header | nagłówek panelu | |
| message icon | ikona wiadomości | |
| link | link | not "odnośnik" – matches everyday software Polish |
| try again later | spróbuj ponownie później | |
