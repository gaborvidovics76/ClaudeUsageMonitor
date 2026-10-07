# Glossary – Turkish (tr) – "Geliştiriciye mesaj" window

Scope: only the 34 keys added by the feedback window (`fb.*`, `menu.feedback`, `set.show_feedback_icon`).
The rest of the Turkish UI lives inline in `claude_usage/i18n*.py`; the terms below follow it.

## Form of address and tone

- **"siz" (polite plural)** – changed by the reviewer (was "sen"). The majority of the inline Turkish uses
  "siz": the whole `help.guide` ("sağ tıklayın", "hesabınıza"), `set.about`, `update.*`, `notify.update`,
  `notify.signin_needed`, `err.signin_needed`, `set.rows_*`, `set.backup_unconfigured`,
  `err.already_running`. It is also what Microsoft, Apple and Google use in Turkish, and the only natural
  register for the GDPR notice ("Haklarınız", "rızanızı geri çekebilirsiniz"). Only a few short core strings
  use "sen" (`set.tip`, `set.reset_confirm`, `err.session_expired*`, the two backup disclaimers) – see
  REVIEW-tr.md. The author still speaks in the first person ("Bana yazın", "bizzat ben okuyorum").
- Short, friendly, confident; imperatives without "lütfen" except in error texts, where "lütfen" softens.
- Capitals: Turkish rule – `İ` from `i`, `I` from `ı` ("İptal", "İletişim").
- Percent sign before the number, as the existing texts do: `%{}`.

## Terms (one fixed translation each)

| English | Türkçe | Note |
|---|---|---|
| Message to the developer | Geliştiriciye mesaj | window title and menu item |
| message | mesaj | not "ileti" – matches everyday app language |
| send / sending | Gönder / Gönderiliyor… | |
| cancel / close | İptal / Kapat | `set.close` already "Kapat" |
| name | Ad | Microsoft TR form field term |
| e-mail / e-mail address | E-posta / e-posta adresi | Microsoft TR term |
| optional | isteğe bağlı | |
| rating (star rating) | puan (yıldız puanı) | "Genel puan" for Overall rating |
| clear (the rating) | temizle | |
| star | yıldız | |
| link | bağlantı | |
| connection | bağlantı | same word; context disambiguates |
| server | sunucu | |
| privacy notice (`fb.privacy_title`) | Gizlilik Bildirimi | see below |
| privacy policy (the full one on the website) | gizlilik politikası | `help.privacy` already "Gizlilik politikası" |
| hide the notice | Bildirimi gizle | |
| consent | rıza | GDPR Turkish wording; not the KVKK-specific "açık rıza" |
| controller | veri sorumlusu | |
| processor | veri işleyen | |
| legitimate interest | meşru menfaat | |
| supervisory authority | denetim makamı | "kendi ülkenin denetim makamı" |
| GDPR Art. 6(1)(f) | GDPR m. 6/1-f | Turkish legal short citation (as in "KVKK m. 5/2-f"); GDPR stays "GDPR" |
| {} of 5 (star tooltip) | 5 üzerinden {} | natural Turkish rating phrase |
| transport (of data) | iletim | not "aktarım" – that is the KVKK word for transfer to third parties |
| hosting provider | barındırma sağlayıcısı | |
| profiling / automated decision-making | profilleme / otomatik karar verme | |
| encrypted connection | şifreli bağlantı | |
| program version / operating system / interface language | program sürümü / işletim sistemi / arayüz dili | "sürüm" as in `set.version` |
| panel header | panel başlığı | as in `set.show_plan_badge` "Başlıkta…" |
| icon | simge | as in `set.tray_value` "Simge değeri" |

## Why "Gizlilik Bildirimi"

The in-app text is a short notice, not the full policy – the full policy is linked from it and is already
called "Gizlilik politikası" in `help.privacy`. Turkish software uses "Gizlilik Bildirimi" for exactly this
kind of embedded statement (Microsoft's "Privacy Statement" is "Gizlilik Bildirimi"), so the two documents
stay distinguishable. The KVKK-era term "Aydınlatma Metni" was avoided on purpose: it would frame the text as
a KVKK Art. 10 disclosure, and this notice is a GDPR notice.
