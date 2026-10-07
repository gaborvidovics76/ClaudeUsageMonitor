# Glossary – Czech (cs)

Scope: the "Message to the developer" window (`fb.*`, `menu.feedback`, `set.show_feedback_icon`).
The rest of the Czech UI already lives inline in `claude_usage/i18n*.py`; this glossary follows its wording.

## Form of address and tone

- **Vykání (vy / vaše / zkuste / klikněte)** – this is what the existing Czech strings use
  (`notify.signin_needed` "Klepněte pravým tlačítkem…", `set.backup_unconfigured` "Vyberte složku…",
  `set.about` "vaše vlastní využití", `set.rows_none` "pro váš účet", `help.guide`). Only the two backup
  disclaimer texts tykají; they are the exception, not the rule (see REVIEW-cs.md).
- Czech consumer software (Microsoft, Google, Apple in Czech, Seznam, Alza) also addresses the user with **vy**.
- Tone: short, friendly, confident; imperatives in the 2nd person plural ("Napište mi", "Zkuste to prosím později").
- The author speaks in the 1st person singular where the English does ("Každou zprávu čtu já").

## Privacy document name

**Zásady ochrany osobních údajů** – the term used by the big platforms in Czech (Google, Microsoft, Seznam,
Alza) and already used by the existing key `help.privacy`. "Informace o zpracování osobních údajů" is the
ÚOOÚ/legal wording for an Art. 13 notice and appears mostly in contracts and public-sector forms; in an app
window users expect "Zásady ochrany osobních údajů". GDPR stays "GDPR"; article citations follow the Czech
legal style: "čl. 6 odst. 1 písm. f) GDPR".

## Fixed terms

| English | Czech | Note |
|---|---|---|
| Message to the developer | Zpráva pro vývojáře | window title and menu item |
| message | zpráva | |
| overall rating | celkové hodnocení | |
| star rating | hodnocení hvězdičkami | |
| click a star | klikněte na hvězdičku | |
| clear (the rating) | vymazat | not "zrušit" – that is Cancel |
| Send / Sending… | Odeslat / Odesílání… | |
| Cancel / Close | Zrušit / Zavřít | `set.close` is already "Zavřít" |
| Name | Jméno | |
| E-mail / e-mail address | E-mail / e-mailová adresa | Czech spelling: "e-mail" with hyphen |
| (optional) | (nepovinné) | |
| reply | odpověď / odpovím | |
| privacy notice | zásady ochrany osobních údajů | lower-case inside a sentence |
| consent | souhlas | withdraw consent = odvolat souhlas |
| accept (the notice) | přijmout | "přijměte zásady" |
| controller | správce | GDPR term |
| processor | zpracovatel | GDPR term |
| legitimate interest | oprávněný zájem | |
| supervisory authority | dozorový úřad | CZ: ÚOOÚ |
| hosting provider | poskytovatel hostingu | |
| hash | hash | established Czech IT term |
| profiling / automated decision-making | profilování / automatizované rozhodování | GDPR term |
| access, rectification, erasure, restriction, objection | přístup, oprava, výmaz, omezení zpracování, námitka | GDPR rights, Czech official wording |
| encrypted connection | šifrované připojení | |
| program version | verze programu | |
| interface language | jazyk rozhraní | |
| panel header | záhlaví panelu | as in `set.show_plan_badge` |
| icon | ikona | |
| link | odkaz | |
| server | server | |
| website | web | short form, used by Czech software |
| author | autor | the English "the author" |
