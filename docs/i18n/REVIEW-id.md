# Review – Bahasa Indonesia (`id`)

## Lektor

Independent native review of `claude_usage/langs/id.py` (form of address "Anda", EYD V, Microsoft / Apple Indonesian terms).

### Changes

- backup.disclaimer_short: "memastikan cadangan lengkap" → "memeriksa apakah cadangan lengkap" – source says "checking", not "ensuring"
- backup.last_run: "Proses terakhir: {} – {}" → "Terakhir dijalankan: {} – {}" – Task Scheduler wording
- backup.task_row: "proses terakhir {} · …" → "terakhir dijalankan {} · …" – same, consistent
- dlg.err_badcode: "coba lagi masuk lewat browser" → "coba masuk lagi lewat browser" – natural word order
- dlg.err_ratelimit: "(jangan mencoba selama itu)" → "(jangan mencoba lagi selama menunggu)" – clearer, less clumsy
- dlg.intro: "di browser Anda sendiri … sudah bisa dipakai" → "di browser sendiri … langsung bisa dipakai" – double "Anda" removed
- err.loading: "Masuk / mengambil data…" → "Sedang masuk / mengambil data…" – status, not imperative
- fb.intro: "atau sekadar suka?" → "atau sekadar menyukainya?" – "suka" needs an object
- fb.privacy_text: "perseorangan (Hungaria)" → "orang perseorangan (Hungaria)" – legal term (UU PDP)
- fb.privacy_text: "Siapa yang dapat melihat:" → "Siapa yang dapat melihatnya:" – object was missing
- fb.sent_sub: "saya akan membalas ke sana" → "saya akan membalas ke alamat itu" – "ke sana" sounds like a place
- help.guide: "memperingatkan tepat waktu" → "memperingatkan Anda lebih awal" – natural meaning of "warns in time"
- help.guide: "menanyakan ke server Anthropic" → "mengambil data dari server Anthropic" – calque of "asks the server"
- help.guide: "Klik ganda" → "Klik dua kali" – Microsoft term
- help.guide: "70 %, … 90 %" → "70%, … 90%" – EYD: no space before %
- help.guide: "memperbarui dengan satu klik" → "memperbarui diri dengan satu klik" – verb needed an object
- help.site_what: "yang baru" → "apa yang baru" – reads wrongly inside a list
- notify.update: "Program versi {} tersedia." → "Versi program {} tersedia." – correct noun phrase order
- panel.refreshing: "mengambil data" → "memuat data" – shorter, Microsoft "memuat"
- set.backup_disclaimer: "Memastikan cadangan Anda … tanggung jawab masing-masing – ujilah pemulihan" → "Memastikan cadangan … tanggung jawab masing-masing pengguna – uji pemulihan" – mixed address fixed, plainer imperative
- set.backup_unconfigured: "tempat skrip cadangan Anda menulis" → "tempat skrip cadangan Anda menyimpan file" – "menulis" needs an object
- set.data_hint: "Tanpa perlu masuk … program menanyakan ke server" → "Tidak perlu masuk … program mengambil data dari server" – calque removed, grammar
- set.local_models_hint: " - " → " – " – en dash per glossary
- set.local_models_none: "- grup ini hanya tetap tersembunyi. Yang lain tidak terpengaruh." → "– grup ini tetap tersembunyi saja. Bagian lain tidak terpengaruh." – natural "simply stays hidden"
- set.reset_confirm: "Yakin ingin memulihkan …?" → "Apakah Anda yakin ingin memulihkan …?" – Microsoft confirmation pattern
- set.tip: "klik ganda = riwayat" → "klik dua kali = riwayat" – Microsoft term
- update.manual: "folder hanya-baca). Unduh paket baru saja." → "folder baca-saja). Sebagai gantinya, unduh paket yang baru." – "baru saja" meant "just now"; Microsoft "baca-saja"
- update.whats_new: "Yang baru" → "Apa yang baru" – Microsoft term, consistent
- STRINGS_MAC notify.first_run: "ikon di bilah menu" → "ikon di bar menu" – Apple Indonesian term

Glossary updated accordingly: menu bar = "bar menu" (Apple), double-click = "klik dua kali", read-only = "baca-saja",
last run = "terakhir dijalankan", What's new = "Apa yang baru", "%" attached to the number, en dash also where the
English has a hyphen.

### Still in doubt

- panel.five_hour_short "5 JAM" and panel.no_data "Tak ada data" are longer than the English ("5H", "No data"). "5J"
  would not be understood instantly; kept – please check on the real panel at the smallest size.
- panel.updated "diperbarui: {}" is 2 characters longer than "updated: {}"; no shorter natural form.
- STRINGS_MAC menu.autostart "Buka saat masuk": Apple's Dock menu uses this wording; capitalisation in Apple's own UI
  may be "Buka saat Masuk" – worth a look on an Indonesian macOS.
- fb.privacy_title "Kebijakan Privasi" for "Privacy Notice": deliberate (the name Indonesian users know), not a literal
  "Pemberitahuan Privasi".
