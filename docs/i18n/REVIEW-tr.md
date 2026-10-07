# Review – Turkish (tr) – feedback-window keys

Texts I am least sure about (34 keys in `claude_usage/langs/tr.py`; checker: OK).

1. **Form of address.** The inline Turkish is mixed: the core strings (menus, settings tip, reset confirm,
   session-expired, backup disclaimers) use "sen", the later additions (`update.*`, `set.rows_*`,
   `set.about`, `notify.signin_needed`, `err.already_running`) use "siz". I followed "sen" (the older core
   and the Hungarian source). If "siz" is preferred, the texts to change are: fb.email_hint, fb.err_consent,
   fb.err_network, fb.err_rate, fb.err_server, fb.intro, fb.err_empty, fb.rating_hint, fb.sent, fb.sent_sub
   and the second person forms in fb.privacy_text.

2. **fb.privacy_title = "Gizlilik Bildirimi".** Chosen over "Gizlilik Politikası" so the in-app notice and
   the linked full policy (`help.privacy` "Gizlilik politikası") have different names, and over the
   KVKK term "Aydınlatma Metni" to avoid implying KVKK framing. "Aydınlatma Metni" is what Turkish users see
   most often for such consent notices, so a Turkish reviewer might still prefer it.

3. **fb.consent = "{} metnini okudum ve kabul ediyorum."** The placeholder is the (linked) title; Turkish
   needs an accusative suffix on it. Instead of attaching "'ni" to the placeholder (would break if the title
   changes) I put the suffix on a following noun "metnini" ("the text of …"). Natural, slightly longer.

4. **fb.privacy_text, "consent" = "rıza".** KVKK texts use "açık rıza" (explicit consent); the GDPR
   consent here (Art. 6(1)(a)) is "rıza" in Turkish GDPR translations. Also "a daily-changing hash" is
   rendered as "her gün değişen … bir karma (hash) değeri" – "karma" alone is unfamiliar, so "hash" is kept
   in parentheses.

5. **fb.meta.** Follows the Hungarian form with all three values in parentheses ("program sürümü ({0})"),
   where the English has the first one without. Pure style; the placeholders are numbered as in the English.

en/hu difference noticed: `fb.privacy_text` – the Hungarian links to `/hu/#privacy`, the English to
`/#privacy`; the Turkish keeps the English URL (no Turkish page exists).

## Lektor

**Form of address changed from "sen" to "siz".** Most of the inline Turkish uses "siz" – the whole
`help.guide` ("sağ tıklayın", "hesabınıza"), `set.about`, `update.*`, `notify.update`, `notify.signin_needed`,
`err.signin_needed`, `set.rows_*`, `set.backup_unconfigured`, `err.already_running`; only a few short core
strings use "sen". "siz" is also what Microsoft/Apple/Google use in Turkish, and a GDPR notice written with
"sen" ("Hakların", "rızanı") reads off-register. Glossary updated. Back-translation of `fb.privacy_text`:
all facts, articles, the 2-year period, the rights, NAIH and the URL are present. İ/ı checked ("İptal",
"İletişim", "İletim"); no `%` in these keys.

- fb.email_hint: "yalnızca yanıt istiyorsan" → "yalnızca yanıt almak istiyorsanız" – siz, more natural
- fb.err_consent: "… kabul et." → "… kabul edin." – siz
- fb.err_empty: "Önce bir mesaj yaz ya da bir puan seç." → "Önce bir mesaj yazın veya bir puan seçin." – siz
- fb.err_network: "Bağlantını kontrol edip yeniden dene." → "Bağlantınızı kontrol edip yeniden deneyin." – siz
- fb.err_rate / fb.err_server: "yeniden dene" → "yeniden deneyin" – siz
- fb.intro: "Bir fikrin mi var, … Bana yaz. Her mesajı programın yazarı olarak ben, Vidovics Gábor, okuyorum." → "Bir fikriniz mi var, bir hata mı buldunuz, yoksa programı sadece beğendiniz mi? Bana yazın. Her mesajı bizzat ben okuyorum – Vidovics Gábor, programın yazarı." – siz, awkward word order
- fb.rating_hint: "bir yıldıza tıkla" → "bir yıldıza tıklayın" – siz
- fb.rating_tip: "{} / 5" → "5 üzerinden {}" – natural Turkish rating phrase
- fb.sent: "mesajın ulaştı!" → "mesajınız ulaştı!" – siz
- fb.sent_sub: "E-posta adresi bıraktıysan oradan yanıt vereceğim." → "E-posta adresinizi bıraktıysanız o adrese yanıt vereceğim." – siz; "oradan" = "from there"
- fb.privacy_text: all second-person forms → siz ("yazdıklarınız", "mesajınızı", "Puanınız ve adınız", "rızanızı … geri çekebilirsiniz", "Haklarınız", "kendi ülkenizin") – siz, legal register
- fb.privacy_text: "Claude Usage Monitor'un yazarı" → "Claude Usage Monitor programının yazarı"; "yer alır" → "yer almaktadır" – formal register
- fb.privacy_text: "Sunucu IP adresi saklamaz" → "Sunucu IP adresini saklamaz" – accusative needed
- fb.privacy_text: "GDPR 6. madde 1. fıkra (f) bendi" / "6. madde 1. fıkra (a) bendi" → "GDPR m. 6/1-f" / "GDPR m. 6/1-a" – standard Turkish legal citation
- fb.privacy_text: "yayımlanan bir puan rızanı geri çekene kadar" → "yayımlanan puan, rızanızı geri çekene kadar" – clarity, siz
- fb.privacy_text: "Almanya'da bulunur" → "Almanya'dadır"; "otomatik karar verme yoktur" → "… yapılmaz" – more idiomatic
- fb.privacy_text: "Aktarım:" → "İletim:" – "aktarım" means transfer to third parties
- fb.privacy_text: "Bu bildirimin sürümü: 2026-10-06." → "… 6 Ekim 2026." – Turkish date format

Still in doubt:
- A few inline core strings still use "sen" (`set.tip`, `set.reset_confirm`, `err.session_expired*`,
  `set.backup_disclaimer`, `backup.disclaimer_short`); they are out of scope here but should be moved to
  "siz" in a later pass so the whole Turkish UI is consistent.
- fb.publish ("Puanım ve adım (verdiysem) …") stays first person – it is the user's own statement.
- "Gizlilik Bildirimi" kept; "Aydınlatma Metni" would frame it as a KVKK notice.
