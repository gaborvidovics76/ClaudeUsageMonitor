# REVIEW – Slovak (sk)

Module: `claude_usage/langs/sk.py` – 358 / 358 keys + 4 macOS keys, `check_i18n: OK`.
Form of address: informal „ty" (see glossary-sk.md). Privacy document: „Zásady ochrany osobných údajov".
The 10 checker warnings are all intended: SI unit symbols (`{}d`, `{}h`, `{} h`, ` s`, `{}%/h`…), `5H`, `Extra`.

## The texts I am least sure about

1. **`panel.five_hour` „5-HODINOVÁ RELÁCIA"** and **`panel.weekly` „TÝŽDENNÝ LIMIT"** – both prescribed by
   LANGUAGE-NOTES, but 4 and 2 characters longer than the English. Please check that they fit the smallest
   panel size; the fallback would be „5 H RELÁCIA".
2. **`panel.model` „{} TÝŽDEŇ"** – a literal „{} TÝŽDENNÝ" would need a noun to agree with; the noun „TÝŽDEŇ"
   keeps the length of „WEEKLY". An alternative is „{} – TÝŽ.".
3. **`time.hm` „{}h {}min" / `time.m` / `backup.age_m` „{}min"** – Slovak has no „m" for minute (it means meter),
   so these are 2 characters longer than the English „{}h {}m". Check the countdown on the slim-bar layout.
4. **`panel.full_in` „plný: {}"** – I read it as „the limit will be full in …"; the adjective agrees with
   „limit". If the value can be a clock time, „plný o: {}" would be more exact.
5. **`panel.no_data` „Bez údajov"** – 3 characters longer than „No data"; there is no shorter natural form.
6. **`tray.head` „5h: {}%   ·   Týž.: {}%"** – „Týždeň" would make the tooltip 2 characters longer than the
   English, so the abbreviation is used; it is understandable but a little terse.
7. **`fb.consent` „Prečítal/a som si dokument {} a súhlasím s ním."** – Slovak needs a case after „súhlasím s";
   inserting the word „dokument" lets the title stay in the nominative. „Prečítal/a" is the only gendered form
   in the UI.
8. **`fb.privacy_text`** – I added „(na Slovensku: Úrad na ochranu osobných údajov SR)" after „the authority
   of your own country", and wrote „čl. 6 ods. 1 písm. a) GDPR" where the English says only „Art. 6(1)(a)". The date is
   given as „6. 10. 2026". Every other fact, article, period and the URL is unchanged; please have it checked
   legally.
9. **`detail.extra` / `profile.extra` / `set.show_extra_usage` „Kredity na využitie"** – Anthropic has no
   official Slovak name for „usage credits"; this matches the „využitie" = usage term used everywhere.
10. **`backup.comp.vault` „Trezor Obsidian – snímka (ZIP)"** – reordered to avoid the uncertain genitive
    „trezora / trezoru"; „trezor" for an Obsidian vault is the usual Slovak community term.

## en / hu differences noticed

- `menu.help`: hu „Súgó (HELP)…" adds „(HELP)"; followed the English („Pomocník…").
- `fb.privacy_text`: hu links to `https://claudeusagemonitor.com/hu/#privacy`, en to `…/#privacy`; the English URL
  is kept.
- `err.rate_limited`: hu is first person („újrapróbálom"), en impersonal; Slovak uses the first person
  („automaticky to skúsim znova"), matching the author's voice used elsewhere (`fb.intro`, `fb.sent_sub`).
- `set.notify_reset`: hu adds „(reset)" in brackets; the English has none and neither does Slovak.
- `set.show_extra_usage`: hu repeats the English „(usage credits)", en says „(pay-as-you-go)"; followed the English.

## Lektor

Changes (18, in 16 keys):

- `backup.cloud_only`: „vo OneDrive" → „v OneDrive" – „vo" not before vowel
- `backup.comp.vault`: „Trezor Obsidian – snímka (ZIP)" → „Snímka trezora Obsidian (ZIP)" – natural order, genitive trezora
- `err.session_expired`: „Relácia vypršala, …" → „Platnosť relácie vypršala, …" – Microsoft SK standard wording
- `err.session_expired_nl`: „Relácia vypršala.\n…" → „Platnosť relácie vypršala.\n…" – same, consistent
- `err.signin_needed`: „Prihlásenie na claude.ai vypršalo." → „Platnosť prihlásenia na claude.ai vypršala." – idiomatic expiry phrase
- `notify.signin_needed`: same change as `err.signin_needed` – consistency
- `fb.consent`: „Prečítal/a som si dokument {} a súhlasím s ním." → „Prečítal/a som si {} a súhlasím s nimi." – „Zásady" accusative = nominative, no filler
- `fb.err_server`: „nemohol správu prijať" → „nemôže správu prijať" – tense fits „momentálne"
- `fb.intro`: „Nápad, chyba, alebo…" → „Nápad, chyba alebo…" – no comma before alebo
- `fb.privacy_text`: „Kto k údajom má prístup" → „Kto má prístup k údajom" – natural Slovak word order
- `help.guide`: „resetuje sa v pevnom týždennom čase tvojho účtu" → „resetuje sa raz týždenne v čase pevne stanovenom pre tvoj účet" – calque, unclear meaning
- `help.guide`: „každé 2 minúty, pomalšie, ak…" → „každé 2 minúty, zriedkavejšie, ak…" – frequency, not speed
- `help.guide`: „Prepínaš ich v ponuke: …" → „Prepínať medzi nimi môžeš v ponuke …" – smoother instruction
- `notify.reset_done`: „začína sa nové obdobie" → „začalo sa nové obdobie" – matches „has started"
- `panel.pace`: „{} k tempu" → „tempo {}" – calque; shorter, clear
- `set.about`: „vyžiada len tvoje vlastné využitie" → „vyžiada len údaje o tvojom vlastnom využití" – one requests data, not usage
- `set.local_models_hint`: „Načítava sa len názov modelu…, nikdy nie konverzácia." → „Načítavajú sa len názvy modelov…, nikdy nie obsah konverzácie." – agreement; source says conversation content
- `update.manual`: „z priečinka iba na čítanie" → „z priečinka určeného iba na čítanie" – elliptical phrase completed

Glossary updated: pace („tempo {}"), session/sign-in expired („platnosť … vypršala").

Checked and kept: informal „ty" is consistent everywhere; no bohemisms found (priečinok, údaje, pomocník,
kontrolka, začiarknutie, prehliadač all Slovak; „doraziť", „potom, ako" are codified Slovak); ä/ô/ĺ/ŕ and the
rhythmic law are correct (exceptions like „čítam", „prichádzajú" are regular). Privacy notice back-translated:
every fact, article, period, right and the URL are present.

Still in doubt:

- `menu.autostart` / `notify.autostart_*` „s Windowsom" – declined „Windows" is common in Slovak tech press, but
  Microsoft SK writes „so systémom Windows". The menu item would then exceed the +30 % limit, so I kept it.
- `panel.full_in` „plný: {}" – {} is a duration (fmt_delta); „plný za {}" would be more exact but 2 characters
  longer than the English.
- `panel.pace` „tempo +12%" – please check on the panel that it reads as a deviation from the ideal pace.
