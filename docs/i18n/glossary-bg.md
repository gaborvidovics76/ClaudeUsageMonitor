# Glossary – Bulgarian (bg)

Scope: the whole UI (all 358 keys of `source.json` + the 4 macOS overrides). A fresh Bulgarian
localisation from the English (Hungarian consulted for intent) – not derived from the Russian module.
Bulgarian grammar throughout: postfixed definite articles (-ът/-ят/-та/-то/-те), да-constructions
instead of an infinitive, the full article only for the subject („Сървърът ограничава…“, but
„върху панела“). No Russian-only letters (ы, э) anywhere – the checker enforces it.

## Tone and form of address

- **Friendly singular „ти“** (lowercase), the voice of Apple, Google and the big Bulgarian consumer apps
  (Viber, Revolut, Glovo, bTV apps). Imperative singular for instructions: „Провери“, „Влез отново“,
  „Кликни върху звезда“, „Постави кода тук“. Possessives: „твоя/твоята/твоите“, „акаунта си“.
  Chosen over Microsoft's „Вие“ because the program is a small, personal, single-author tool that speaks
  in the first person („Пиши ми. Всяко съобщение чета лично аз…“) – a „Вие“ would sound like a bank.
  The legal text (`fb.privacy_text`) keeps „ти“ too (as the English keeps „you“), but in the legal
  register: ОРЗД terms, article numbers, no colloquialisms.
- **Gender-neutral phrasing** wherever the past tense would reveal the user's gender: „Провери дали е
  поставен целият код“ instead of „дали си поставил“; „Ако има оставен имейл адрес“ instead of „Ако си
  оставил“; „Не е извършено влизане“ instead of „Не си влязъл“. The 2nd-person aorist („Излезе от
  акаунта“) is neutral and may be used.
- **Menu items, buttons and checkboxes use verbal nouns** (Microsoft Bulgarian convention: „Влизане“,
  „Излизане“, „Затваряне“, „Изпращане“, „Инсталиране сега“, „Проверка сега“, „Показване на панела“);
  „Отказ“ for Cancel, „Изход“ for Quit. Imperative is reserved for sentences addressed to the user.
- **Platform words follow Microsoft Bulgarian** (Windows is what the user sees around the program):
  Влизане / Излизане, Настройки, Известия, лента на задачите, област за известяване, папка,
  актуализация (program), обновяване (data), сървър, изтегляне, менюто „Старт“, Преглед…, крайна точка.
  The four macOS texts follow Apple Bulgarian: лента с менюта, „Отваряне при влизане“.
- **click** = „кликване / кликни“ (Google, Apple and everyday Bulgarian); Microsoft's „щракване“ is
  correct but sounds official and old-fashioned next to „ти“. Right-click = „десен бутон“ / „кликни с
  десния бутон“; double-click = „двойно кликване“; drag = „влачене / влачи“.
- Quotation marks: Bulgarian „…“. Dashes: en-dash with spaces (as the English). Dates: 06.10.2026 г.,
  „21 септември 2026 г.“ in running text.
- Percent: in running text „70 %“ (with space, as the English); next to a placeholder „{}%“ (panel space).
- Count form after numerals for masculine nouns: „{} файла“, „{} нови/обновени ZIP“; „{} бележки“ (fem.).

## Privacy document name

**„Политика за поверителност“** (`fb.privacy_title`, `help.privacy`). This is the name every major platform
uses in Bulgarian (Google, Microsoft, Apple, Meta, Viber) and the term users expect on a link and a consent
checkbox. „Декларация за поверителност“ (Microsoft's older term) and „Уведомление за поверителност“
(the literal GDPR „privacy notice“) exist but are rarer and feel like paperwork. In `fb.consent` the
inserted title (a link) follows a colon – „Прочетох и приемам: {}.“ – the usual Bulgarian form-checkbox
pattern, grammatical without having to inflect the inserted title („Политиката…“ would need the article).
The GDPR itself is **ОРЗД** (Общ регламент относно защитата на данните – the official Bulgarian name); the
sub-paragraph letters follow the official Bulgarian text of the Regulation, which uses Cyrillic letters:
Art. 6(1)(f) = „чл. 6, пар. 1, буква „е“ от ОРЗД“, Art. 6(1)(a) = „чл. 6, пар. 1, буква „а““.
Supervisory authority: kept generic as the English („до надзорния орган в твоята държава“), next to NAIH.
The Bulgarian one would be КЗЛД (Комисия за защита на личните данни, cpdp.bg) – not inserted, because the
legal text must keep exactly the facts of the English; noted in REVIEW-bg.md.
Date in the notice: „06.10.2026 г.“ (Bulgarian date format, same date).

## Terms

| English | Bulgarian | Note |
|---|---|---|
| 5-hour session | 5-часова сесия | panel: 5-ЧАСОВА СЕСИЯ; short: 5Ч; plural: 5-часови сесии |
| weekly limit | седмичен лимит | panel: СЕДМИЧЕН ЛИМИТ; short: СЕДМ.; tray: Седм. |
| per-model weekly limit | седмичен лимит по модел | panel: „{} СЕДМИЧНО“ (FABLE СЕДМИЧНО) |
| full in … (panel) | пълен: {} | the gauge's limit (masc.) will be full after {} |
| retry in … (panel) | опит след {} с | |
| fetching data (panel) | обновяване | |
| reset happened (notification) | „{}: нулиране – започва нов период.“ | noun form avoids gender agreement with {} |
| limit | лимит | not „ограничение“ (that is rate limiting) |
| rate limit / rate limiting | ограничение на заявките | „Ниво на ограничение на заявките“, „429 / ограничение на заявките“ |
| reset (noun / verb) | нулиране / нулира се | panel: „нулиране {}“; „Обратно броене до нулирането“ |
| pace | темпо | panel: „темпо {}“ ({} = „+12%“) – „vs“ is not Bulgarian |
| burn rate | скорост на изразходване | hist: „Средно дневно изразходване“ |
| projection / forecast | прогноза | „Прогноза за края на седмицата“ |
| usage | използване | „данни за използването“, „файлът с данни за използването“ |
| usage credits | кредити за използване | pay-as-you-go = „плащане според употребата“ |
| gauge | индикатор | „Индикатор {}“, „Подредба на индикаторите“ |
| panel | панел | „Плаващият панел“; masculine → sizes „Малък / Нормален / Голям / Много голям“ (Extra) |
| widget | уиджет | help text only |
| tray / notification area | област за известяване | tray icon = „иконата в областта за известяване“ |
| menu bar (macOS) | лента с менюта | STRINGS_MAC |
| taskbar | лента на задачите | |
| Start menu | менюто „Старт“ | |
| sign in / sign out | влизане / излизане | buttons: „Влизане“, „Излизане“; verb: „влез отново“ |
| sign-in (the stored session) | влизането (в claude.ai) | „Влизането в claude.ai е изтекло.“ |
| session (login) | сесия | „Сесията е изтекла.“ |
| passkey | ключ за достъп | Apple / Google Bulgarian |
| notification | известие | „Известие при…“ |
| alert(s) (tab) | сигнали | „Сигнали“ tab; warning = „Предупреждение“, critical = „Критично“ |
| threshold | праг | „преминаване на праг“, „според праговете“ |
| stale data | остарели данни | „Известие при остаряване на данните“ |
| data freshness | актуалност на данните | |
| backup (noun) | резервно копие (pl. резервни копия) | window: „Резервни копия“ |
| backup (process) | архивиране | „Последно успешно архивиране“, „скрипт за архивиране“ |
| backup status bar | лента на архивирането | menu + settings |
| backup logs | дневниците от архивирането | |
| lamp | лампичка | „Само лампички“, „Етикет до лампичката“ |
| snapshot | моментна снимка | |
| vault (Obsidian) | трезор | |
| data source | източник на данни | menu + tab |
| local log | локален дневник | log = дневник, log file = файл на дневника |
| profile / account | профил / акаунт | „Профил / акаунт“ |
| plan / plan badge | план / значка на плана | plan names stay (Pro, Max…) |
| theme | тема | |
| layout | оформление | post-it card = лепящо листче, slim bar = тънка лента, rings = пръстени |
| settings | настройки | window title lowercase „настройки“ as the English |
| default(s) | по подразбиране | „Възстановяване по подразбиране“ |
| update (program) | актуализация | „Актуализация на програмата“, „Инсталиране сега“ |
| refresh (data) | обновяване | „Обновяване на данните сега“, panel: „обновено: {}“ |
| download | изтегляне | |
| what's new / release notes | какво ново / бележки по изданията | |
| history | хронология | Microsoft term; „Хронология и статистика…“ |
| trend curve | крива на тенденцията | „(sparkline)“ kept in brackets |
| token | токен | „изходните токени“, „крайната точка за токени“ |
| message to the developer | съобщение до разработчика | |
| rating / overall rating | оценка / обща оценка | star = звезда |
| privacy notice | Политика за поверителност | see above |
| terms of use | Условия за ползване | |
| consent | съгласие | „оттегляне на съгласието“ |
| controller / processor | администратор / обработващ лични данни | ОРЗД terms |
| supervisory authority | надзорен орган | КЗЛД in Bulgaria |
| legitimate interest | легитимен интерес | ОРЗД wording |
| hosting provider | хостинг доставчик | |
| hash | хеш | |
| encrypted | криптиран | „Криптирана връзка (HTTPS)“ |
| endpoint | крайна точка | Microsoft term |
| server | сървър | |
| folder | папка | |
| always on top | винаги отгоре | settings: „Над всички други прозорци“ |
| lock position | заключване на позицията | |
| click-through | прозрачен за кликване | |
| snap to screen edge | прилепване към ръба на екрана | |
| opacity | непрозрачност | |
| accent color | цвят на акцента | |
| connected apps | свързани приложения | |
| per-surface limits | лимити по платформа | Claude Code, connected apps… |
| scheduled tasks | планирани задачи | Windows Task Scheduler wording |
| this PC | този компютър | „PC“ is not used in Bulgarian UI |
| destination | местоназначение | Microsoft term |
| cancel / close / quit | Отказ / Затваряне / Изход | Microsoft |
| browse… | Преглед… | Microsoft |
| optional | незадължително | „(незадължително)“ |
| time units | с / мин / ч / д | „{}ч {}мин“, „{} с“, „{}д {}ч“ |
