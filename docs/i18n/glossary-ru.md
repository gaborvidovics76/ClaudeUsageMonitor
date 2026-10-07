# Glossary – Russian (ru), "Message to the developer" window

Scope: only the 34 new keys (`fb.*`, `menu.feedback`, `set.show_feedback_icon`). The rest of the Russian UI
lives inline in `claude_usage/i18n*.py`; the terms below follow it.

## Tone and form of address

- **вы** (lowercase, polite plural) – exactly as the existing Russian texts: «войдите снова», «проверьте»,
  «снимите галочку», «ваше собственное использование». Never «Вы» with a capital (that is letter/marketing
  register, not software), never «ты».
- The author speaks in the first person («читаю я сам», «отвечу на него») – same as EN/HU.
- Short, friendly, confident; errors in the Microsoft Russian style (imperative, no exclamation marks).
- Dash: the texts keep the EN/HU en dash «–» with spaces (same as the inline Russian).

## Fixed terms

| English | Русский | Note |
|---|---|---|
| Message to the developer | Сообщение разработчику | window title + menu item |
| message | сообщение | |
| name | имя | |
| e-mail | E-mail (label) / адрес e-mail (in text) | common in Russian software; e-mail is in NO_TRANSLATE |
| optional | необязательно | hint and «(необязательно)» suffix |
| overall rating | общая оценка | |
| star rating | оценка в звёздах | |
| rating | оценка | |
| clear (rating) | сбросить | small link next to the stars |
| send / sending | Отправить / Отправка… | |
| cancel / close | Отмена / Закрыть | «Закрыть» = existing set.close |
| privacy notice (document name) | Политика конфиденциальности | the term Yandex, VK, Microsoft, Apple and Roskomnadzor use; matches the existing help.privacy |
| hide the notice | Скрыть политику | |
| consent | согласие | |
| accept (a notice) | принять | «примите политику конфиденциальности» |
| controller | оператор (контролёр) данных | RF law says «оператор», the EU Russian translation of GDPR says «контролёр»; both given once, then «оператор» |
| processor | обработчик | |
| hosting provider | хостинг-провайдер | |
| legitimate interest | законный интерес | |
| supervisory authority | надзорный орган | «надзорный орган вашей страны» |
| GDPR | Общий регламент ЕС по защите данных, GDPR | expanded once, then «GDPR»; Russian legal citation order article → paragraph → point: «подп. (f) п. 1 ст. 6 GDPR» |
| private individual | физическое лицо | legal term, not «частное лицо» |
| version of this notice | Редакция от ДД.ММ.ГГГГ | Russian legal convention; dates as 06.10.2026 |
| profiling / automated decision-making | профилирование / автоматизированное принятие решений | |
| hash | хеш | |
| encrypted connection | зашифрованное соединение | |
| panel header | заголовок панели | existing: «Значок тарифа в заголовке» |
| icon | значок | existing term (not «иконка») |
| program version | версия программы | existing: «Доступна версия программы {}» |
| interface language | язык интерфейса | |
| link | ссылка | |
| connection | подключение | «Проверьте подключение» |
