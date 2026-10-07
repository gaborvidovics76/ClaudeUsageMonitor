# Review notes – Maltese (mt)

Checker: `check_i18n: OK` (358/358; 13 warnings, all deliberate: units h/s, loanwords Backups/Folders/Vault,
"reset", "5H", theme name "Neon").

## Least certain texts

1. **`menu.settings` / `set.title` / help.guide – "Issettjar".** Chosen as Microsoft Maltese terminology
   (Windows LIP "Issettjar tal-PC"). Many Maltese websites simply write "Settings"; if a reviewer finds the
   current Windows 11 Maltese LIP uses "Settings", switch all occurrences (7 keys) consistently.
2. **`menu.layout` / `set.layout` – "Tqassim"** (and "Qsim" for the model split in `detail.local_header`,
   `set.show_local_models`). Microsoft-style; the English loanword "Layout" would also be understood.
3. **`panel.five_hour` – "SESSJONI 5 SIGĦAT".** The grammatical form is "SESSJONI TA' 5 SIGĦAT", but that is
   50 % longer than the English on the tight panel; the label style without "ta'" is shorter but slightly
   telegraphic.
4. **`panel.week_short` – "ĠIMGĦA"** (6 chars vs "WEEK" 4) and `tray.head` "Ġimgħa". Maltese has no
   established abbreviation for "ġimgħa"; check that it fits on the slim bar.
5. **`panel.full_in` – "mimli: {}"** (1 char longer than the English) and **`panel.retry_in` – "jerġa' f'{} s"**
   (elliptical for "jerġa' jipprova f'…"; full form did not fit).
6. **`menu.click_through` / `set.click_through` – "Klikks jgħaddu minnu".** No established Maltese term; a
   descriptive phrase.
7. **`fb.privacy_text`** – legal register follows the Maltese GDPR text (kontrollur, proċessur, tfassil ta'
   profili, Artikolu 6(1)(f)). "E-mail forwarding" was rendered with the loanword "forwarding tal-emails";
   "2 years" as "sentejn" (dual). Authority kept generic as instructed (in Malta: IDPC).
8. **`fb.privacy_hide` – "Aħbi l-Politika"** – shortened from "Aħbi l-Politika tal-Privatezza" to fit the button.
9. **`profile.tier` – "Kategorija tal-limitu tar-rata: {}".** "Rate-limit tier" has no Maltese equivalent;
   "livell" was avoided because it is the glossary word for "threshold".
10. **`backup.files_size`, `backup.snap_kept`, `backup.zip_summary`, `backup.vault_changed`, `backup.zip_new`** –
    noun put before the number ("Fajls: {}") to avoid wrong numeral agreement (Maltese 2–10 plural vs 11+
    singular). `backup.zip_summary` uses numbered placeholders {0}{1}{2}.

## en / hu differences noticed

- `fb.privacy_text`: en links `https://claudeusagemonitor.com/#privacy`, hu links `/hu/#privacy`. Followed
  the English URL.
- `set.notify_reset`: hu adds "(reset)" in parentheses; en does not. Followed the English.
- `set.show_extra_usage`: en explains "(pay-as-you-go)", hu repeats "(usage credits)". Followed the English
  ("ħlas skont l-użu").
- `notify.logout`: en "Switched to local source" (no subject), hu "the panel switched…". Used the hu subject
  ("Il-pannell qaleb għas-sors lokali") because Maltese needs one; meaning identical.
- `menu.help`: hu "Súgó (HELP)…" contains the English word; en is just "Help…". Followed the English.

## Lektor

Overall the translation is idiomatic, orthographically correct (ħ ġ ż ċ, għ, ie, article assimilation,
euphonic i) and consistent in "int". 10 changes:

- `panel.five_hour`: SESSJONI 5 SIGĦAT → SESSJONI TA' 5H – grammatical, fits English length
- `dlg.hint1`: "fil-paġna li tiftaħ" → "fil-paġna li tinfetaħ" – page opens itself, not "you open"
- `backup.disclaimer_short`: "int trid tiċċekkja" → "hija r-responsabbiltà tiegħek li tiċċekkja" – "up to you", matches guide
- `fb.privacy_text`: "ikun irrevedihom" → "ikun eżaminahom" – usual verb for "reviewed"
- `fb.privacy_text`: "fil-kaxxa postali" → "fil-kaxxa tal-email" – postal box ≠ e-mail mailbox
- `help.guide`: "jekk hux se jlaħħaq sar-reset" → "jekk hux se jkun biżżejjed sar-reset" – "will it last" meaning
- `help.guide`: "Logs u issettjar:" → "Il-logs u l-issettjar:" – avoids "u i-" elision problem
- `set.backup_disclaimer`: "ittestja restawr minn żmien għal żmien" → "minn żmien għal żmien ipprova rrestawra backup biex tittestjah" – "restawr" reads as building restoration
- `set.backup_unconfigured`: "L-ebda folder … ma huwa ssettjat" → "Ma ġie ssettjat l-ebda folder…" – natural Maltese word order
- `set.visible`: "Il-pannell fuq l-iskrin jidher" → "Il-pannell jidher fuq l-iskrin" – unnatural word order

Glossary: panel label updated; "kaxxa tal-email" (mailbox) added.

**"Issettjar" verified and kept.** It is the established Maltese software term (Windows 8 Maltese LIP
"Issettjar tal-PC", Google's and Facebook's Maltese UIs), regularly derived from the KNM-accepted verb
"issettja" (cf. "issettjat", already used in this file). Using it as a singular collective noun with the
article ("l-issettjar prestabbilit", "fl-Issettjar") is correct. A web search did not turn up a citable
Microsoft terminology page, so this rests on product usage, not a published glossary.

Still in doubt:
- `panel.week_short` "ĠIMGĦA" (6 vs 4 chars) – no established abbreviation; check on the slim bar.
- `panel.retry_in` "jerġa' f'{} s" – elliptical; "jipprova f'{} s" is clearer but 1 char longer.
- `dlg.intro` "salvati" – fine; Maltese Office uses "issejvja", so "issejvjati" would also do.
- `profile.tier`, `menu.click_through` – descriptive renderings; no established Maltese term.
