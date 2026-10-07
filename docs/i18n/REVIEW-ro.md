# REVIEW ro – texts to check

`check_i18n.py ro`: 358 / 358, **OK**. The 7 warnings are correct and intentional: unit symbols that are the
same in Romanian (`{}h`, `{}%/h`, ` h`, ` s`, `{} h`, `5H`) and the theme name `Neon`.

Form of address: **tu** (no „dumneavoastră” anywhere). Privacy document: **„Politica de confidențialitate”**.

## Least certain texts (≤ 10)

1. **`panel.model` – „{} SĂPTĂMÂNAL”** (13 chars vs 9). Literal „OPUS SĂPTĂMÂNAL” reads as a label but is a
   bit elliptic; „{} SĂPT.” would be shorter but cryptic next to the full „LIMITĂ SĂPTĂMÂNALĂ”. Check on the real
   panel width.
2. **`panel.five_hour` / `panel.weekly` – „SESIUNE DE 5 ORE” / „LIMITĂ SĂPTĂMÂNALĂ”** are longer than the English
   (16/18 vs 14/12). Prescribed by LANGUAGE-NOTES; a visual check of the narrowest layout is needed.
3. **`panel.full_in` – „plin: {}”.** Short and parallel to de/fr/it („voll”, „plein”), but a Romanian user may
   prefer „epuizat în {}” (too long for the panel).
4. **`panel.reset` – „resetare {}”** (11 vs 8) and **`panel.retry_in` – „din nou în {} s”** (15 vs 13): slightly
   longer than English; „reset {}” would be shorter but is a slang noun.
5. **`time.*` / `backup.age_*` – „z” for days, „min” for minutes** („{}z {}h”, „{}h {}min”). „z” is the usual
   short form but less universal than „h”; „min” chosen over „m” (SI; „m” = metre), costing 2 characters.
6. **`set.show_surfaces` – „Limite pe produs (Claude Code, aplicații conectate…)”.** „Surface” has no natural
   Romanian equivalent („suprafață” would be a calque); „produs” matches how users think of Claude Code vs apps.
7. **Count texts rewritten as „label: {}”** (`backup.files_size`, `snap_kept`, `vault_changed`, `zip_new`,
   `zip_summary`, `uploaded`) to avoid wrong plurals („1 fișiere”, „25 fișiere” without „de”). Meaning is
   identical, word order differs from English.
8. **`hist.stat_now` – „Nivel săptămânal actual”** for „Current weekly”; an alternative is „Săptămâna în curs”.
9. **`fb.privacy_text`** – ANSPDCP (dataprotection.ro) is **added** as the Romanian example authority next to NAIH,
   as LANGUAGE-NOTES allows; „the authority of your own country” is kept. The URL is the English one
   (`/#privacy`) because no `/ro/` page is known – change it if a Romanian page is published.
10. **`theme.midnight` – „Sticlă de noapte”** and **`theme.paper` – „Hârtie deschisă”**: theme names, free
    adaptations („Midnight glass”, „Light paper”); a native designer may prefer „Sticlă bleumarin” / „Hârtie albă”.

## en / hu differences noticed (English followed)

- `fb.privacy_text`: hu links `/hu/#privacy`, en `/#privacy`.
- `menu.locked`: en „Lock position” (action), hu „Pozíció rögzítve” (state). `menu.panel_visible`: en „Show panel”,
  hu „Panel látszik” (state). Romanian follows the English action form.
- `menu.help`: hu „Súgó (HELP)…” adds the English word; en „Help…”.
- `detail.surface.oauth_apps` / `set.show_surfaces`: en „Connected apps”, hu „Külső alkalmazások” (external apps).
- `set.show_extra_usage`: en „(pay-as-you-go)”, hu „(usage credits)”.
- `help.guide`: hu drops „e.g. for a specific model”; en keeps it (kept in ro).
- `set.notify_reset`: hu adds „(reset)”; en does not.

## Lektor

Independent native review (2026-10-07). 20 changes; diacritics checked (0 × ş/ţ with cedilla, 0 × „dumneavoastră”,
„tu” consistent everywhere); `check_i18n.py ro` → **OK** (same 7 correct warnings). Glossary unchanged (still valid).

- `backup.disclaimer_short`: „să verifici că sunt complete” → „să verifici dacă sunt complete” – „verifici dacă”, not calque
- `backup.storage`: „ocupat {} din {}” → „utilizat {} din {}” – Microsoft „spațiu utilizat”
- `detail.local_header`: „REPARTIZAREA SĂPTĂMÂNII” → „REPARTIZAREA DIN SĂPTĂMÂNA ACEASTA” – „this week's”, not „the week's”
- `dlg.err_badcode`: „codul întreg” → „codul complet” – more natural collocation
- `dlg.intro`: „în propriul browser” → „în browserul tău” – calque of „your own”
- `fb.intro`: „O idee, o eroare sau pur și simplu îți place? … Fiecare mesaj îl citesc eu, Vidovics Gábor, autorul.” →
  „Ai o idee, ai găsit o eroare sau pur și simplu îți place programul? … Citesc personal fiecare mesaj – sunt
  Vidovics Gábor, autorul.” – verbless fragment sounded foreign
- `fb.meta`: „Odată cu mesajul” → „Împreună cu mesajul” – „odată cu” is temporal
- `fb.privacy_text`: „autorul Claude Usage Monitor” → „autorul aplicației Claude Usage Monitor” – genitive of uninflected name
- `fb.privacy_text`: „nu are loc nicio creare de profiluri” → „nu se creează profiluri” – nominal calque, heavy
- `fb.sent`: „Mulțumesc – a ajuns!” → „Mulțumesc – mesajul a ajuns!” – subject missing in Romanian
- `help.guide`: „în propriul browser” → „în browserul tău” – calque of „your own”
- `help.guide`: „jurnalul de utilizare al Claude Desktop” → „… al aplicației Claude Desktop” – genitive of uninflected name
- `hist.stat_forecast`: „Estimare la sfârșitul săptămânii” → „Estimare pentru sfârșitul săptămânii” – projection, not timing
- `hist.stat_now`: „Nivel săptămânal actual” → „Utilizare săptămânală actuală” – glossary term „utilizare”
- `set.data_hint`: „plan-usage-history.json al Claude Desktop” → „… al aplicației Claude Desktop” – genitive of uninflected name
- `set.data_hint`: „de resetare și reîmprospătare mai frecventă” → „de resetare și cu reîmprospătare mai frecventă” – removes ambiguous coordination
- `set.local_models_hint`: „PC - o parte” → „PC – o parte” – Romanian dash, not hyphen
- `set.local_models_none`: „Claude Code - acest grup” → „Claude Code – acest grup” – Romanian dash, not hyphen
- `set.taskbar`: „Afișează pe bara de activități” → „Afișează în bara de activități” – Microsoft preposition („în”)
- `update.manual`: „rulează din sursă” → „rulează din codul sursă” – „din sursă” is unclear

### Still in doubt

- `panel.five_hour` (16), `panel.weekly` (18), `panel.model` „{} SĂPTĂMÂNAL” (13) are longer than the English
  (14 / 12 / 9). Kept because LANGUAGE-NOTES prescribes the full labels; if the narrowest layout clips them, the
  fallback is „{} SĂPT.” for `panel.model` (matches `panel.week_short`). Needs a screenshot check.
- `panel.full_in` „plin: {}” – understandable next to a gauge, but „epuizat: {}” may be clearer if space allows.
- `fb.privacy_text` – ANSPDCP (dataprotection.ro) added as the Romanian example authority (allowed by
  LANGUAGE-NOTES); URL is still the English `/#privacy` – switch if a `/ro/` page is published.
- `help.disclaimer` „afiliat cu aceasta” – common usage; the normative form is „afiliat la”. Left as is.
- `theme.midnight` „Sticlă de noapte” / `theme.paper` „Hârtie deschisă” – free adaptations, acceptable.
