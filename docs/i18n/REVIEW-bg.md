# Review – Bulgarian (bg)

Module: `claude_usage/langs/bg.py` – 358/358 keys + 4 macOS keys, `check_i18n: OK`.
Form of address: „ти“ (see glossary-bg.md). Privacy document: „Политика за поверителност“.

## The 10 texts I am least sure about

| # | Key | Bulgarian | Why unsure |
|---|---|---|---|
| 1 | `panel.model` | `{} СЕДМИЧНО` | English „FABLE WEEKLY“ is elliptical; Bulgarian has no equally short noun-less adjective. „СЕДМИЧНО“ (adverb, „weekly“) reads naturally on the label; alternative „{} – СЕДМИЦА“. |
| 2 | `panel.pace` | `темпо {}` | {} is „+12%“. „vs“ is not Bulgarian; „спрямо темпото“ is too long for the panel. Word order changed („темпо +12%“). |
| 3 | `panel.full_in` | `пълен: {}` | {} is a duration (time until the gauge is full). „пълен“ agrees with the implied „лимит“; the precise „100% след {}“ / „изчерпан след {}“ exceed the English length. |
| 4 | `panel.week_short` | `СЕДМ.` | 5 characters vs „WEEK“ (4), the dot is narrow; „СЕДМ“ without the abbreviation dot would look wrong in Bulgarian. Same abbreviation in `tray.head` („Седм.“). |
| 5 | `panel.reset` | `нулиране {}` | Shown as „(нулиране 2ч 10мин)“. „нулиране след {}“ would be more grammatical but 3 characters longer on the panel. |
| 6 | `fb.consent` | `Прочетох и приемам: {}.` | {} is the linked title „Политика за поверителност“; the colon avoids inflecting it („Политиката…“). Common on Bulgarian forms, but slightly more formal than a plain sentence. |
| 7 | `fb.privacy_text` | (whole text) | Legal register checked against ОРЗД wording (администратор, обработващ лични данни, легитимен интерес, буква „е“/„а“ – the Bulgarian official text uses Cyrillic letters for the points). The supervisory authority is kept generic as in the English; the Bulgarian authority would be КЗЛД (cpdp.bg) if the author wants to name it. Date written as „06.10.2026 г.“. |
| 8 | `menu.click_through` / `set.click_through` | `Прозрачен за кликване` | No established Microsoft Bulgarian term; alternative „Пропускане на кликванията“. |
| 9 | `backup.label_age` | `Име и изминало време` | „възраст“ (age) sounds odd for files; „изминало време“ (elapsed time) follows the Hungarian intent. |
| 10 | `notify.reset_done` | `{}: нулиране — започва нов период.` | Noun form chosen because {} can be feminine („5-часова сесия“) or masculine („седмичен лимит“) – a participle („нулиран/а“) would not agree with both. |

## en / hu differences noticed

- `fb.privacy_text`: the English URL is `https://claudeusagemonitor.com/#privacy`, the Hungarian `…/hu/#privacy`. Followed the English (there is no Bulgarian page).
- `err.signin_needed`: English names the menu item „Sign in to claude.ai“, while the real context-menu item (`menu.login`) is „Sign in (claude.ai, browser)…“. Followed the English wording („Влизане в claude.ai“, which matches `set.login_btn_out`).
- `menu.help`: Hungarian „Súgó (HELP)…“ adds „HELP“; English and Bulgarian do not.
- `fb.consent`: Hungarian already uses the colon pattern („Elolvastam és elfogadom: {}.“); Bulgarian follows it for grammatical reasons.
- `set.show_extra_usage`: English explains „(pay-as-you-go)“, Hungarian repeats „(usage credits)“; followed the English („плащане според употребата“).

## Lektor

Independent native review. Overall: genuine Bulgarian, no Russianisms, articles (full/short) correct, „ти“ consistent,
ОРЗД terms and article letters correct. 18 changes:

- `dlg.err_badcode`: „опитай отново влизането през браузъра“ → „опитай отново да влезеш през браузъра“ – verb more natural than noun
- `dlg.open_browser`: „Отваряне на влизането в браузъра“ → „Влизане през браузъра“ – awkward calque, shorter button
- `err.no_tray`: „иконата в нея се пропуска“ → „иконата няма да се показва там“ – „пропуска“ sounds machine-translated
- `fb.err_email`: „не изглежда правилен“ → „изглежда неправилен“ – natural Bulgarian negation
- `fb.err_network`: „Няма връзка с … Провери връзката си“ → „Няма достъп до … Провери връзката си“ – avoids „връзка“ repetition
- `fb.privacy_text`: „Връзка: тази форма или уебсайтът.“ → „Контакт: този формуляр или уебсайтът.“ – legal register, „връзка“ ambiguous
- `fb.publish`: „може да бъдат показани“ → „могат да бъдат показани“ – normative plural agreement
- `help.feedback`: „формата за съобщения на уебсайта“ → „формата за контакт на уебсайта“ – usual Bulgarian web term
- `help.guide` (Local): „но знае само за този компютър“ → „но отчита само този компютър“ – less colloquial, matches set.data_hint
- `help.guide` (troubleshooting): „се пази 7 дни и се запазва след…“ → „се пази 7 дни и не се губи при…“ – removes пази/запазва tautology
- `hist.stat_now`: „Текущ седмичен“ → „Текущо седмично използване“ – noun-less adjective is a calque
- `menu.check_update`: „Проверка за актуализации на програмата…“ → „Проверка за актуализации…“ – menu item was 54 % longer
- `notify.reset_done`: „започва нов период“ → „започна нов период“ – English „has started“
- `notify.signin_needed`: „за да виждаш“ → „за да продължиш да виждаш“ – restores „keep seeing“
- `set.backup_disclaimer`: „Всеки сам отговаря резервните му копия да са…“ → „Всеки сам носи отговорност за това резервните му копия да са…“ – ungrammatical construction fixed
- `set.local_models_hint`: „…броят на токените, никога разговорът.“ → „…броят на токените – никога самият разговор.“ – clearer emphasis
- `set.model_filter`: „Следен модел“ → „Проследяван модел“ – „следен“ unidiomatic here
- `set.profile_auto`: „(последно използван)“ → „(последно използваният)“ – definite form needed („the last used“)

Back-translation of `help.guide`, `err.*`, `notify.*`, `fb.privacy_text`, `fb.intro`, `set.backup_disclaimer`,
`backup.disclaimer_short`: no remaining meaning shift; the privacy text keeps every fact, Art. 6(1)(f)/(a) as
„буква „е“/„а““, 2-year retention, all rights, NAIH and the URL.

Still in doubt:
- `set.accent` „Цвят на акцента“ – Windows 11 Bulgarian may say „Цвят на акцентиране“; left per glossary, worth checking against the live Windows UI.
- `set.restore` „Възстановяване по подразбиране“ – slightly elliptical (Microsoft often writes „Възстановяване на настройките по подразбиране“), kept for button length.
- `err.not_signed_in` „Не е извършено влизане.“ – correct and gender-neutral, but a bit official; a gendered „Не си влязъл“ was avoided on purpose.
- `panel.full_in` „пълен: {}“ – as ambiguous as the English; acceptable on the panel.
- `detail.local_header` is ~35 % longer than the English; no shorter natural wording keeps „split“.
