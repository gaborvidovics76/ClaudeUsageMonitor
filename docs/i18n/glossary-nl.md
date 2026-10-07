# Glossary – Nederlands (nl)

Covers only the new "Message to the developer" keys; the rest of the Dutch UI lives inline in
`claude_usage/i18n*.py` and sets the tone this module follows.

## Form of address and tone

- **je / jij** everywhere (never *u*). The existing Dutch strings use *je* consistently
  (`dlg.intro`, `notify.signin_needed`, `set.backup_disclaimer`), the way Dutch consumer software does.
  The privacy notice keeps *je* too, so the window reads as one voice; its register stays legal
  (verwerkingsverantwoordelijke, verwerker, gerechtvaardigd belang, inzage, rectificatie, wissing …).
- Short, friendly, confident. Error texts: one sentence saying what happened, one saying what to do.
- Dutch compounds are written as one word (programmaversie, sterrenbeoordeling, hostingprovider,
  berichtpictogram, e-mailadres).

## Terms

| English | Nederlands | Note |
|---|---|---|
| Message to the developer | Bericht aan de ontwikkelaar | window title and menu item |
| message | bericht | |
| rating / overall rating | beoordeling / algemene beoordeling | not "waardering" |
| star rating | sterrenbeoordeling | |
| clear (the rating) | wissen | |
| optional | optioneel | consistent with Windows/Office wording |
| Send / Sending… | Verzenden / Verzenden… | |
| Cancel / Close | Annuleren / Sluiten | `dlg.cancel` already uses Annuleren |
| e-mail address | e-mailadres | |
| privacy notice | **privacyverklaring** | the term Dutch websites, apps and the Autoriteit Persoonsgegevens use for the notice shown to the data subject; `help.privacy` ("Privacybeleid") names the policy page on the website |
| controller | verwerkingsverantwoordelijke | AVG term |
| processor | verwerker | AVG term |
| legitimate interest | gerechtvaardigd belang | |
| consent / withdraw consent | toestemming / toestemming intrekken | |
| GDPR Art. 6(1)(f) | art. 6 lid 1 onder f AVG | Dutch citation style |
| supervisory authority | toezichthoudende autoriteit; "de toezichthouder in je eigen land" | NL: Autoriteit Persoonsgegevens |
| access, rectification, erasure, restriction, objection | inzage, rectificatie, wissing, beperking, bezwaar | AVG wording |
| hosting provider | hostingprovider | |
| encrypted connection | versleutelde verbinding | |
| panel header | de kop van het paneel | matches `set.show_plan_badge` ("in de kop") |
| interface language | taal van de interface | |
| author (of the program) | de maker (van het programma) | |
