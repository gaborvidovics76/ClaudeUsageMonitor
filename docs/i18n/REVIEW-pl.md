# REVIEW – Polish (pl), "Message to the developer" keys

Checker: `python tools/check_i18n.py pl` → `check_i18n: OK` (the 9 warnings are pre-existing inline strings
identical to English – units, "Plan:", "System", "Neon" – and are correct).

Texts I am least sure about:

1. **fb.title / menu.feedback – "Wiadomość do autora"**. English says "developer"; I chose "autor", because the
   intro text introduces the person as "autor programu" and a single-person project reads more naturally this
   way. If "developer" must be literal: "Wiadomość do dewelopera" (Google Play / Microsoft Store wording) or
   "Wiadomość do twórcy".

2. **fb.consent – "Przeczytałem(-am) i akceptuję: {}."** The placeholder is the link text in nominative
   ("Polityka prywatności"), so the colon construction of the Hungarian was kept to avoid a case clash.
   The "(-am)" suffix is the usual gender-neutral device in Polish forms; a fully neutral alternative is
   "Znam i akceptuję: {}."

3. **fb.name – "Imię"** (first name). English "Name" is broader; "Imię i nazwisko" would be the formal full-name
   label but is heavier than a feedback form needs. The privacy text uses "imię" consistently.

4. **fb.privacy_hide – "Ukryj politykę prywatności"** is ~70 % longer than "Hide the notice". A plain "Ukryj"
   would fit anywhere but loses the object; shorten if the control is tight.

5. **Form of address**: the new texts use the capitalised "Ty/Twój/Ci" convention of the inline Polish backup
   texts. One older inline string (`…o twoje własne użycie…`, the no-telemetry line) uses lowercase "twoje";
   it is outside this task's scope and was not touched, but it could be unified to "Twoje".

en/hu differences noticed: the Hungarian privacy URL is `…/hu/#privacy`, the English `…/#privacy` – the
English (language-neutral) URL was kept. No other content difference.

## Lektor

Form of address checked against the inline Polish (`Sprawdź`, `zaloguj się`, `Twojej kopii`): "ty" with the
capitalised courtesy forms is correct and kept. Back-translation of `fb.privacy_text`: all facts, articles
(art. 6 ust. 1 lit. f / lit. a RODO), the 2-year period, the rights, NAIH and the URL are present.

- fb.intro: "a może po prostu Ci się podoba" → "a może program po prostu Ci się podoba" – missing subject, sounded clipped
- fb.publish: "Moja ocena i moje imię (jeśli zostało podane) mogą być widoczne na claudeusagemonitor.com." → "Moja ocena i imię (jeśli je podano) mogą być widoczne na stronie claudeusagemonitor.com." – lighter, "na stronie" idiomatic
- fb.privacy_hide: "Ukryj politykę prywatności" → "Ukryj politykę" – button ~70 % too long
- fb.privacy_text: "wiadomości – najwyżej 2 lata; … do wycofania zgody" → "nie dłużej niż 2 lata; … do czasu wycofania zgody" – legal register for retention
- fb.privacy_text: "przekazywanie na e-mail, kopia trafia także do skrzynki pocztowej autora" → "przekazywanie wiadomości na e-mail, kopia trafia także do jego skrzynki pocztowej" – object missing, repetition
- fb.privacy_text: "Nic nie jest sprzedawane …; nie ma profilowania ani zautomatyzowanego podejmowania decyzji" → "Dane nie są sprzedawane …; nie podlegają profilowaniu ani zautomatyzowanemu podejmowaniu decyzji" – RODO wording (art. 22)
- fb.privacy_text: "skarga do organu nadzorczego" → "wniesienie skargi do organu nadzorczego" – RODO term (art. 77)
- fb.privacy_text: "(w Polsce: Prezes UODO)" → "(w Polsce: Prezes UODO, uodo.gov.pl)" – parallel to "NAIH, naih.hu"
- fb.privacy_text: "Przesyłanie: szyfrowane …" → "Przesyłanie danych: szyfrowane …" – clearer heading
- fb.privacy_text: "Wersja tej polityki: 2026-10-06." → "Wersja tej polityki: 6 października 2026 r." – Polish date format
- fb.sent_sub: "Jeśli w formularzu jest adres e-mail, odpowiem właśnie tam." → "Jeśli podano adres e-mail, odpowiem na niego." – "właśnie tam" unidiomatic
- fb.err_consent: "Aby wysłać, zaakceptuj …" → "Aby wysłać wiadomość, zaakceptuj …" – dangling verb
- fb.err_links: "Zbyt wiele linków w wiadomości." → "Wiadomość zawiera zbyt wiele linków." – full sentence, error style
- fb.err_server: "Serwer nie mógł teraz przyjąć wiadomości." → "Serwer nie może teraz przyjąć wiadomości." – tense with "teraz"
- glossary-pl.md: "hide the notice" row updated to "Ukryj politykę".

Still in doubt:
- "Wiadomość do autora" for "Message to the developer" is a sound localisation choice; "Wiadomość do twórcy" would
  be equally natural. Left as is.
- fb.consent "Przeczytałem(-am) i akceptuję: {}." – the colon is needed because the link text is nominative;
  the standard legal phrase "Zapoznałem(-am) się z Polityką prywatności" would need the instrumental case.
