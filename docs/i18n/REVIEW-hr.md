# REVIEW hr – texts I am least sure about

Module: `claude_usage/langs/hr.py` (358 + 4 mac keys). `check_i18n.py hr` → OK; the 9 warnings are the
unit symbols h / d / s (and `5H`), which the binding language notes prescribe – they are right.
Form of address: **vi** (lowercase, as Croatian Microsoft / Apple / Google UIs). Privacy document:
**Pravila privatnosti**.

| # | Key | Croatian | Why unsure |
|---|---|---|---|
| 1 | `panel.five_hour`, `panel.weekly` | SESIJA OD 5 SATI / TJEDNO OGRANIČENJE | Prescribed by LANGUAGE-NOTES, but 16 / 18 chars vs 14 / 12 in English – please check they fit the narrowest layout at the smallest size. Fallback if they clip: „5-SATNA SESIJA” / „TJEDNI LIMIT”. |
| 2 | `panel.reset` | reset za {} | „reset” is the usual colloquial IT word; „za” (= “in”) makes it read naturally but is 3 chars longer than English. Plain „reset {}” would be identical to English. |
| 3 | `panel.full_in` | 100% za {} | Croatian has no short natural equivalent of “full: 1h 20min” for a neuter noun (ograničenje); „100% za …” is unambiguous on a percentage gauge. Two chars longer. |
| 4 | `panel.week_short` | TJED. | „TJ.” would be shorter but universally means „to jest” (“i.e.”). One char longer than WEEK. |
| 5 | `panel.pace` | {} vs tempo | „vs” is an anglicism, but widely understood and the only form short enough. |
| 6 | `fb.privacy_text` | (whole text) | Added the Croatian authority as an example: „ili nadzornom tijelu vlastite države (u Hrvatskoj: AZOP, azop.hr)”. Version date localised to „6. listopada 2026.”. Kept the English URL `/#privacy` (no `/hr/` page known). GDPR article form „čl. 6. st. 1. t. (f)”. |
| 7 | `fb.consent` | Pročitao/la sam i prihvaćam {}. | 1st-person past tense is gendered in Croatian; „/la” is the standard form on Croatian web forms. |
| 8 | `fb.publish` | Pristajem da se moja ocjena i ime (ako je upisano) prikažu na … | Rephrased as an explicit consent („I agree that …”) instead of a literal “may be shown”, because it is the label of the consent checkbox. |
| 9 | `backup.files_size`, `backup.uploaded`, `backup.zip_summary`, `backup.vault_changed`, `backup.snap_kept` | „datoteka: {}, …”, „novih: {}, …” | Number moved after a colon to avoid wrong noun forms (1 datoteka / 2 datoteke / 5 datoteka). Slightly more formal than the English. |
| 10 | `menu.refresh` | Osvježi podatke sada | Shortened (dropped “usage”) to stay within ~30 % of the English menu width; the full form would be „Osvježi podatke o potrošnji sada”. |

## en / hu differences noticed

- `fb.privacy_text`: the English URL is `https://claudeusagemonitor.com/#privacy`, the Hungarian one
  `https://claudeusagemonitor.com/hu/#privacy`. I followed the English.
- `fb.consent`: English “I have read and accept the {}.” vs Hungarian “Elolvastam és elfogadom: {}.” – same
  meaning, followed the English structure.
- `fb.privacy_hide`: English “Hide the notice”, Hungarian “Tájékoztató elrejtése”; translated as
  „Sakrij pravila privatnosti” to match the chosen document name.
- `menu.help`: Hungarian has „Súgó (HELP)…”, English “Help…”; followed the English („Pomoć…”).
- `set.show_extra_usage`: English explains “(pay-as-you-go)”, Hungarian repeats “(usage credits)”; followed the
  English („plaćanje po potrošnji”).
- `help.guide` / data source item: English “Local (this PC only) – reads the usage log of Claude Desktop”,
  Hungarian omits “usage”; followed the English.

## Lektor

Independent native review (standard Croatian, ijekavian, „vi”, Microsoft/Apple hr terms). No Serbian forms found
(no nedjelja/nedelja, računar, fajl, podešavanja, sedmica). Glossary left unchanged – it was right. 20 changes:

- `backup.disclaimer_short`: „Ne preuzimamo odgovornost za sigurnosne kopije – provjera jesu li potpune i mogu li se vratiti na vama je.” → „Za sigurnosne kopije ne preuzimamo odgovornost – na vama je da provjerite jesu li potpune i mogu li se vratiti.” – inverted, stiff word order
- `backup.recent_notes`: „Posljednje uređene bilješke u snimci” → „Nedavno uređene bilješke u snimci” – natural “most recently edited”
- `dlg.err_ratelimit`: „Poslužitelj vas privremeno ograničava.” → „Poslužitelj vam je privremeno ograničio pristup.” – “limits you” sounded odd
- `dlg.intro`: „(ondje već rade vaše spremljene lozinke …)” → „(u njemu su vam već dostupne spremljene lozinke …)” – calque “work there”
- `fb.privacy_text`: „Tko ih vidi:” → „Tko vidi podatke:” – unclear pronoun antecedent
- `fb.privacy_text`: „pružatelj usluge smještaja (hostinga) (poslužitelj …)” → „pružatelj usluge hostinga (poslužitelj …)” – double brackets, clumsy
- `help.disclaimer`: „nije ga izradio Anthropic niti je s njim povezan” → „nije proizvod tvrtke Anthropic niti je s njom povezan” – subject switch was ambiguous
- `help.guide`: „hoće li ono potrajati do reseta” → „hoće li vam dostajati do reseta” – idiomatic “will it last”
- `help.guide`: „ali zna samo za ovo računalo” → „ali obuhvaća samo ovo računalo” – calque “only knows this PC”
- `help.guide`: „Upotreba widgeta” → „Korištenje widgeta” – usual Microsoft heading wording
- `help.guide`: „izrada i testiranje kopija vaš su posao” → „za izradu i testiranje kopija odgovorni ste vi” – “your job” too blunt
- `help.guide`: „uz claude.ai ponovno se prijavite” → „ako koristite claude.ai, ponovno se prijavite” – “uz” unclear here
- `hist.stat_now`: „Trenutačno tjedno” → „Ovaj tjedan” – adverb-like, unclear label
- `menu.refresh`: „Osvježi podatke sada” → „Osvježi podatke o potrošnji” – restores “usage”, within length
- `notify.logout`: „Prebačeno na lokalni izvor.” → „Sada se koristi lokalni izvor.” – subjectless participle sounded machine-made
- `notify.reset_done`: „—” → „–” – Croatian dash typography
- `set.data_hint`: „ali mjeri samo ovo računalo” → „ali mjeri samo potrošnju na ovom računalu” – “measures this PC” calque
- `set.local_models_hint`: „u vašoj vlastitoj potrošnji” → „u vašoj potrošnji” – redundant pleonasm
- `set.rows_available`: „uklonite kvačicu s onoga …” → „poništite odabir onoga …” – Microsoft checkbox wording
- `set.theme_default`: „Zadano za temu” → „Zadano prema temi” – natural “theme default”

Still in doubt:
- `panel.five_hour` / `panel.weekly` (SESIJA OD 5 SATI / TJEDNO OGRANIČENJE) are longer than English but prescribed;
  check they fit at the smallest size.
- `time.m`, `time.hm`, `backup.age_m` use „min” (2 chars longer than English „m”); „m” would read as metre, so kept.
- `panel.pace` „{} vs tempo” – „vs” is an anglicism, accepted for space.
- `fb.privacy_text` names AZOP in addition to the generic authority (allowed by LANGUAGE-NOTES); the date
  „6. listopada 2026.” and „IP adresu” (no hyphen, as in Microsoft hr) kept.
