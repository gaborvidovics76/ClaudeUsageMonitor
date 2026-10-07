# Review notes – Russian (ru), "Message to the developer" keys

Texts I am least sure about, with reasons. Everything else follows the glossary and the existing inline Russian.

1. **fb.consent** – «Я прочитал(а) и принимаю: {}.» Russian past tense is gendered; the «(а)» form is the
   usual gender-neutral checkbox wording. The colon construction (as in HU) avoids having to inflect the
   inserted document title («Политика конфиденциальности» stays in the nominative, so it can be a link).
   Alternative without the colon: «Я принимаю условия: {}.»

2. **fb.privacy_text, "Controller"** – «Оператор (контролёр) данных». Russian Federation law uses «оператор»,
   the Russian translation of the EU regulation uses «контролёр». Both are given once at the start; later the
   text says only «оператор». Cut the parenthesis if one term is preferred.

3. **fb.privacy_text, URL** – kept the English `https://claudeusagemonitor.com/#privacy` (HU points at
   `/hu/#privacy`). If a `/ru/` page exists, change it.

4. **fb.email** – «E-mail» as the field label (very common on Russian sites, matches «адрес e-mail» in the
   other texts). Microsoft's own term would be «Электронная почта» – longer; use it if the label has room.

5. **fb.privacy_hide** – «Скрыть политику» (hides the privacy text block). If the button hides something
   other than the policy text, «Скрыть текст» is the safer wording.

EN/HU differences noticed: only the privacy URL (`/#privacy` vs `/hu/#privacy`); HU «értékelés»/«Általános
értékelés» = EN «rating»/«Overall rating», no conflict.

## Lektor

Form of address checked against the inline Russian («войдите снова», «проверьте», «ваше собственное
использование»): lowercase «вы» is correct and kept. Back-translation of `fb.privacy_text`: all facts,
articles, the 2-year period, the rights, NAIH and the URL are present.

- fb.intro: «Идея, ошибка или просто нравится? … читаю я сам, Vidovics Gábor, автор программы.» → «Есть идея, нашли ошибку или программа просто нравится? … Каждое сообщение я читаю сам – Vidovics Gábor, автор программы.» – subjectless calque of EN/HU
- fb.publish: «могут быть показаны на claudeusagemonitor.com» → «могут отображаться на сайте claudeusagemonitor.com» – natural UI wording
- fb.err_consent: «Чтобы отправить, примите …» → «Чтобы отправить сообщение, примите …» – dangling verb
- fb.err_server: «Сервер сейчас не смог принять сообщение.» → «Сервер сейчас не может принять сообщение.» – tense with «сейчас»
- fb.privacy_text: «частное лицо» → «физическое лицо» – correct legal term
- fb.privacy_text: «автор Claude Usage Monitor» → «автор программы Claude Usage Monitor» – smoother, matches fb.intro
- fb.privacy_text: «хеш, который невозможно обратно преобразовать в адрес» → «хеш, по которому невозможно восстановить адрес» – idiomatic
- fb.privacy_text: «ст. 6 п. 1 (f) GDPR (Общий регламент ЕС по защите данных)» → «подп. (f) п. 1 ст. 6 Общего регламента ЕС по защите данных, GDPR» – Russian legal citation order
- fb.privacy_text: «(согласие, ст. 6 п. 1 (a) GDPR)» → «(согласие, подп. (a) п. 1 ст. 6 GDPR)» – same citation style
- fb.privacy_text: «в почтовый ящик автора» → «в его почтовый ящик» – avoid repetition
- fb.privacy_text: «(сервер в ЕС, Германия)» → «(сервер в ЕС, в Германии)» – grammatical parallel
- fb.privacy_text: «Ничего не продаётся и не передаётся третьим лицам» → «Данные не продаются и не передаются третьим лицам» – legal register
- fb.privacy_text: «Версия этого уведомления: 2026-10-06.» → «Редакция от 06.10.2026.» – Russian legal convention and date format
- glossary-ru.md: GDPR citation style, «физическое лицо», «Редакция от» added.

Still in doubt:
- «Оператор (контролёр) данных» – kept both terms (RF law vs. EU translation); fine for a GDPR notice.
- Dash: the en dash «–» follows the inline Russian; strict Russian typography would use the em dash «—».
