# Glossary – Italian (it) – "Message to the developer" window

Scope: only the 34 keys that live in `claude_usage/langs/it.py` (`fb.*`, `menu.feedback`,
`set.show_feedback_icon`). The rest of the Italian UI is inline in `claude_usage/i18n*.py`;
this glossary follows its existing choices.

## Form of address and tone

- **tu** (informal singular), as everywhere else in the existing Italian UI
  (`Accedi al tuo account…`, `Chiudi questa finestra`, `spetta a te`). Never "Lei" / "voi".
- Imperatives in the second person singular: *Scrivi*, *Controlla*, *Riprova*, *Accetta*.
- The author speaks in the first person where the English does (*Scrivimi*, *Leggo ogni messaggio*).
- Microsoft Italian terminology for UI actions: *fai clic*, *Annulla*, *Chiudi*, *Invia*.
- The legal notice keeps the *tu* form but uses the GDPR's official Italian vocabulary.

## Fixed terms

| English | Italian | Note |
|---|---|---|
| Message to the developer | Messaggio allo sviluppatore | window title and menu item |
| message | messaggio | |
| rating / overall rating | valutazione / valutazione complessiva | star rating = *valutazione a stelle* |
| clear (the rating) | cancella | lowercase, as the English |
| optional | facoltativo | not *opzionale* (more natural in forms) |
| e-mail (field) | Indirizzo e-mail | hyphenated *e-mail* as in the rest of the UI |
| send / sending… | Invia / Invio in corso… | |
| cancel / close | Annulla / Chiudi | Microsoft wording |
| privacy notice | Informativa sulla privacy | the term Italian software, websites and the Garante use (*informativa* = art. 13 GDPR) |
| consent | consenso | |
| controller | titolare del trattamento | official Italian GDPR term |
| processor | responsabile del trattamento | official Italian GDPR term |
| supervisory authority | autorità di controllo | official Italian GDPR term; example given: Garante per la protezione dei dati personali |
| legitimate interest | legittimo interesse | |
| GDPR Art. 6(1)(f) | art. 6, par. 1, lett. f) GDPR | Italian citation style; "GDPR" kept, as is customary in Italy |
| withdraw consent | revocare il consenso | |
| access, rectification, erasure, restriction, objection | accesso, rettifica, cancellazione, limitazione, opposizione | the official names of the rights |
| profiling / automated decision-making | profilazione / processo decisionale automatizzato | |
| encrypted (HTTPS) | crittografato/a | Microsoft term; used in both `fb.secure` and the notice |
| panel header | intestazione del pannello | |
| link | link | the loanword is standard in Italian UI |
| bug | bug | the loanword is standard; *errore* would be ambiguous |
