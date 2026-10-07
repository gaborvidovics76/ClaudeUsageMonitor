# -*- coding: utf-8 -*-
"""Bahasa Indonesia – UI strings of Claude Usage Monitor."""

CODE = "id"
NAME = "Bahasa Indonesia"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{}h",
    "backup.age_h": "{}j",
    "backup.age_m": "{}m",
    "backup.and_more": "…dan {} lainnya",
    "backup.checked_at": "Diperiksa: {}",
    "backup.checking": "Memeriksa…",
    "backup.cloud_only": "Snapshot ini hanya tersedia online di OneDrive; isinya tidak ditampilkan agar tidak perlu diunduh.",
    "backup.comp.cowork": "Log percakapan Cowork (ZIP per sesi)",
    "backup.comp.vault": "Snapshot vault Obsidian (ZIP)",
    "backup.disclaimer_short": "Monitor hanya menampilkan apa yang tercatat di log cadangan. Kami tidak bertanggung jawab atas cadangan – memeriksa apakah cadangan lengkap dan dapat dipulihkan adalah tanggung jawab Anda.",
    "backup.done": "selesai",
    "backup.dry_run": "(uji coba, tidak ada yang diunggah)",
    "backup.failed": "GAGAL",
    "backup.files_size": "{} file, {}",
    "backup.folders": "Folder",
    "backup.label_age": "Nama dan usia",
    "backup.label_name": "Hanya nama",
    "backup.label_none": "Hanya lampu",
    "backup.last_ok": "Cadangan terakhir yang berhasil: {} ({} yang lalu)",
    "backup.last_run": "Terakhir dijalankan: {} – {}",
    "backup.legend": "Hijau: tidak lebih dari {} jam · Kuning: hingga {} jam · Merah: lebih lama, atau tidak ada cadangan",
    "backup.level_green": "Segar",
    "backup.level_none": "Cadangan tidak ditemukan",
    "backup.level_red": "Usang",
    "backup.level_yellow": "Mulai usang",
    "backup.log_file": "File log",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Folder cadangan tidak ditemukan: {}",
    "backup.none_found": "Tidak ada.",
    "backup.open": "buka",
    "backup.rc_copied": "file baru atau yang berubah telah disalin",
    "backup.rc_failed": "GAGAL (kode {})",
    "backup.rc_nochange": "sudah mutakhir, tidak ada yang perlu disalin",
    "backup.recent_notes": "Catatan yang terakhir diedit dalam snapshot",
    "backup.refresh": "Periksa sekarang",
    "backup.sec_components": "Yang dicadangkan",
    "backup.sec_contents": "Isi",
    "backup.sec_log": "Log (baris terakhir)",
    "backup.sec_problems": "Kesalahan dan peringatan",
    "backup.sec_tasks": "Tugas terjadwal",
    "backup.skipped": "dilewati (folder tidak ditemukan)",
    "backup.snap_kept": "{} snapshot disimpan, total {}",
    "backup.snapshot": "Snapshot terbaru",
    "backup.source": "Sumber",
    "backup.state_error": "selesai dengan kesalahan",
    "backup.state_interrupted": "tidak selesai",
    "backup.state_ok": "berhasil diselesaikan",
    "backup.state_running": "sedang berjalan",
    "backup.storage": "Penyimpanan jarak jauh: {} terpakai dari {}, {} kosong",
    "backup.target": "Tujuan",
    "backup.task_event": "saat peristiwa",
    "backup.task_row": "terakhir dijalankan {} · hasil {} · berikutnya {}",
    "backup.tip_click": "Klik untuk melihat detail",
    "backup.title": "Cadangan",
    "backup.tray": "Cadangan: {}",
    "backup.uploaded": "Diunggah pada proses ini: {} baru, {} diganti, {} kesalahan",
    "backup.uploaded_files": "File yang diunggah",
    "backup.uploaded_groups": "File yang diunggah per folder",
    "backup.uploaded_no": "Diunggah ke Nextcloud: belum",
    "backup.uploaded_yes": "Diunggah ke Nextcloud: ya ({})",
    "backup.vault": "Vault",
    "backup.vault_changed": "{} catatan berubah di vault sejak snapshot ini",
    "backup.zip_new": "{} ZIP baru/diperbarui",
    "backup.zip_summary": "{} file ({} catatan), {} tanpa kompresi",
    # --- details rows -----------------------------------------------------------------------
    "detail.extra": "Kredit penggunaan",
    "detail.local_header": "CLAUDE CODE · PC INI · PEMBAGIAN MINGGU INI",
    "detail.off": "nonaktif",
    "detail.on": "aktif",
    "detail.surface.oauth_apps": "Aplikasi terhubung",
    "detail.unlimited": "tanpa batas",
    # --- sign-in dialog ---------------------------------------------------------------------
    "dlg.cancel": "Batal",
    "dlg.checking": "Memeriksa…",
    "dlg.err_badcode": "Kode tidak diterima.\n\n{}\n\nPastikan Anda menempelkan seluruh kode, atau coba masuk lagi lewat browser (selalu dengan kode baru).",
    "dlg.err_ratelimit": "Terlalu banyak upaya masuk dalam waktu singkat.\n\nServer membatasi Anda untuk sementara. Tutup jendela ini, tunggu 10–15 menit (jangan mencoba lagi selama menunggu), lalu mulai SATU proses masuk baru lewat browser dengan kode baru.",
    "dlg.hint1": "Masuk di halaman yang terbuka dan setujui aksesnya. Di akhir, Anda akan mendapat kode.",
    "dlg.intro": "Masuk ke akun claude.ai Anda di browser sendiri (kata sandi dan kunci sandi yang tersimpan di sana langsung bisa dipakai).",
    "dlg.login_title": "masuk",
    "dlg.open_browser": "Buka halaman masuk di browser",
    "dlg.paste_label": "Tempelkan kode yang Anda terima di sini:",
    "dlg.paste_placeholder": "tempel kode di sini",
    "dlg.signin": "Masuk",
    "dlg.step1": "Langkah 1",
    "dlg.step2": "Langkah 2",
    "dlg.unknown_err": "Kesalahan tidak dikenal.",
    # --- error messages ---------------------------------------------------------------------
    "err.already_running": "Aplikasi sudah berjalan (periksa baki sistem).",
    "err.bad_token_resp": "respons tidak valid dari endpoint token",
    "err.bad_usage_resp": "respons tidak valid dari endpoint penggunaan",
    "err.connection": "kesalahan koneksi: {}",
    "err.file_empty": "File penggunaan kosong.",
    "err.file_not_found": "File penggunaan tidak ditemukan.\nApakah Claude Desktop berjalan?",
    "err.file_unreadable": "File penggunaan saat ini tidak dapat dibaca.",
    "err.loading": "Sedang masuk / mengambil data…",
    "err.network": "kesalahan jaringan: {}",
    "err.no_code": "Belum ada kode yang ditempel.",
    "err.no_data_profile": "Tidak ada data untuk profil ini.",
    "err.no_tray": "Baki sistem tidak tersedia; ikon baki dilewati.",
    "err.no_usage_data": "Tidak ada data penggunaan.",
    "err.not_signed_in": "Belum masuk.",
    "err.query_http": "Kesalahan kueri (HTTP {}).",
    "err.rate_limited": "Server membatasi permintaan (429) – mencoba lagi secara otomatis.",
    "err.session_expired": "Sesi telah berakhir, masuk lagi.",
    "err.session_expired_nl": "Sesi telah berakhir.\nMasuk lagi.",
    "err.signin_needed": "Sesi masuk claude.ai telah kedaluwarsa.\nMasuk lagi: klik kanan → Masuk ke claude.ai",
    "err.unexpected": "Kesalahan tak terduga: {}",
    # --- "Message to the developer" window --------------------------------------------------
    "fb.cancel": "Batal",
    "fb.close": "Tutup",
    "fb.consent": "Saya telah membaca dan menyetujui {}.",
    "fb.email": "Email",
    "fb.email_hint": "hanya jika Anda ingin dibalas",
    "fb.err_consent": "Untuk mengirim, harap setujui Kebijakan Privasi.",
    "fb.err_email": "Alamat email ini tampaknya tidak valid.",
    "fb.err_empty": "Tulis pesan atau pilih penilaian terlebih dahulu.",
    "fb.err_links": "Terlalu banyak tautan dalam pesan.",
    "fb.err_network": "Tidak dapat menghubungi claudeusagemonitor.com. Periksa koneksi Anda dan coba lagi.",
    "fb.err_rate": "Terlalu banyak pesan dalam waktu singkat – silakan coba lagi nanti.",
    "fb.err_server": "Server tidak dapat menerima pesan saat ini. Silakan coba lagi nanti.",
    "fb.intro": "Punya ide, menemukan bug, atau sekadar menyukainya? Sampaikan kepada saya. Setiap pesan saya baca sendiri – Vidovics Gábor, pembuat program ini.",
    "fb.message": "Pesan",
    "fb.message_ph": "Apa yang berfungsi, apa yang tidak, apa yang kurang?",
    "fb.meta": "Dikirim bersama pesan: versi program {0}, sistem operasi ({1}), bahasa antarmuka ({2}).",
    "fb.name": "Nama",
    "fb.optional": "(opsional)",
    "fb.privacy_hide": "Sembunyikan kebijakan",
    "fb.privacy_text": (
        "Pengendali data: Vidovics Gábor, orang perseorangan (Hungaria), pembuat Claude Usage Monitor. "
        "Kebijakan Privasi selengkapnya tersedia di situs web: https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "Data yang dikirim: apa yang Anda ketik di sini – nama (opsional), alamat email (opsional), pesan, "
        "penilaian bintang – dan, agar saya dapat memahami konteksnya: versi program, nama dan versi sistem "
        "operasi, bahasa antarmuka, serta waktu pengiriman. Server tidak menyimpan alamat IP; untuk mencegah "
        "penyalahgunaan, server hanya menggunakan hash yang berubah setiap hari dan tidak dapat diubah kembali "
        "menjadi alamat."
        "\n\n"
        "Tujuan: untuk membaca dan menjawab pesan Anda serta untuk menyempurnakan program (kepentingan yang sah, "
        "GDPR Pasal 6 ayat (1) huruf f; balasan itu sendiri atas permintaan Anda). Penilaian dan nama Anda hanya "
        "ditampilkan di situs web jika Anda mencentang kotak terpisah untuk itu (persetujuan, Pasal 6 ayat (1) "
        "huruf a), dan hanya setelah ditinjau oleh pembuat; Anda dapat menarik persetujuan tersebut kapan saja."
        "\n\n"
        "Jangka waktu penyimpanan: pesan paling lama 2 tahun; penilaian yang dipublikasikan sampai Anda menarik "
        "persetujuan. Jika pembuat mengaktifkan penerusan email, salinannya juga masuk ke kotak surat pembuat."
        "\n\n"
        "Siapa yang dapat melihatnya: hanya pengendali data, dan – sebagai pemroses data – penyedia hosting (server "
        "di Uni Eropa, Jerman). Tidak ada data yang dijual atau diteruskan; tidak ada pemrofilan dan tidak ada "
        "pengambilan keputusan otomatis."
        "\n\n"
        "Hak Anda: akses, perbaikan, penghapusan, pembatasan, keberatan, penarikan persetujuan, serta pengaduan "
        "kepada otoritas pengawas (di Hungaria: NAIH, naih.hu) atau otoritas di negara Anda. Kontak: formulir ini "
        "atau situs web."
        "\n\n"
        "Transmisi: terenkripsi (HTTPS/TLS) ke claudeusagemonitor.com. Versi kebijakan ini: 6 Oktober 2026."
    ),
    "fb.privacy_title": "Kebijakan Privasi",
    "fb.publish": "Penilaian dan nama saya (jika diisi) boleh ditampilkan di claudeusagemonitor.com.",
    "fb.rating": "Penilaian keseluruhan",
    "fb.rating_clear": "hapus",
    "fb.rating_hint": "opsional – klik salah satu bintang",
    "fb.rating_tip": "{} dari 5",
    "fb.secure": "Koneksi terenkripsi (HTTPS) ke claudeusagemonitor.com.",
    "fb.send": "Kirim",
    "fb.sending": "Mengirim…",
    "fb.sent": "Terima kasih – pesan Anda telah diterima!",
    "fb.sent_sub": "Saya membaca setiap pesan. Jika Anda mencantumkan alamat email, saya akan membalas ke alamat itu.",
    "fb.title": "Pesan untuk pengembang",
    # --- Help window ------------------------------------------------------------------------
    "help.disclaimer": "Alat independen dan gratis – tidak dibuat oleh dan tidak berafiliasi dengan Anthropic. “Claude” adalah merek dagang Anthropic.",
    "help.feedback": "Pertanyaan, ide, laporan bug: formulir pesan di situs web.",
    "help.free": "Gratis selamanya · Lisensi MIT · sumber terbuka · tanpa telemetri",
    "help.guide": (
        "\n"
        "<h2>Yang ditampilkan widget</h2>\n"
        "<ul>\n"
        "<li><b>Sesi 5 jam</b> – seberapa banyak batas sesi Anda saat ini yang sudah terpakai. Direset setiap lima jam; widget menghitung mundur hingga reset.</li>\n"
        "<li><b>Batas mingguan</b> – penggunaan di semua model; direset pada waktu mingguan tetap sesuai akun Anda.</li>\n"
        "<li><b>Batas mingguan per model</b> – indikator ketiga saat server melaporkannya (mis. untuk model tertentu).</li>\n"
        "<li><b>Tempo dan laju pemakaian</b> – seberapa cepat Anda memakai batas dan apakah akan bertahan hingga reset; perkiraan akhir minggu memperingatkan Anda lebih awal.</li>\n"
        "<li><b>Kredit penggunaan</b> dan lencana paket Anda – bila Anda mengaktifkannya di <i>Lencana paket dan batas tambahan</i>.</li>\n"
        "</ul>\n"
        "<h2>Dari mana datanya</h2>\n"
        "<ul>\n"
        "<li><b>claude.ai (semua perangkat)</b> – mengambil data dari server Anthropic, sehingga penggunaan di ponsel, browser, dan komputer lain ikut dihitung. Perlu masuk satu kali di browser Anda sendiri (menu: <i>Masuk</i>). Disegarkan setiap 2 menit, lebih lambat jika server memintanya.</li>\n"
        "<li><b>Lokal (hanya PC ini)</b> – membaca log penggunaan Claude Desktop di komputer ini. Tanpa perlu masuk, tetapi hanya mengenal PC ini.</li>\n"
        "</ul>\n"
        "<p>Beralih di antara keduanya lewat menu: <i>Sumber data</i>.</p>\n"
        "<h2>Menggunakan widget</h2>\n"
        "<ul>\n"
        "<li><b>Klik kanan</b> widget (atau ikon baki) – menu lengkap.</li>\n"
        "<li><b>Klik dua kali</b> sebuah indikator – jendela <b>Riwayat</b>: 6 jam, 24 jam, 7 hari, atau semuanya, dengan puncak, rata-rata harian, dan perkiraan.</li>\n"
        "<li><b>Seret</b> untuk memindahkannya; panel menempel ke tepi layar. <b>Ctrl + roda mouse</b> – memperbesar atau memperkecil.</li>\n"
        "<li>Tata letak: kartu Post-it, bilah ramping, cincin; 6 tema. <i>Kunci posisi</i> dan <i>Tembus klik</i> ada di Pengaturan.</li>\n"
        "</ul>\n"
        "<h2>Peringatan</h2>\n"
        "<p>Kuning mulai 70%, merah mulai 90% (dapat disesuaikan). Pemberitahuan opsional saat suatu batas direset dan saat data mulai usang.</p>\n"
        "<h2>Cadangan (opsional)</h2>\n"
        "<p>Lampu-lampu kecil menunjukkan apakah cadangan terjadwal Anda berjalan dan selesai. Klik sebuah lampu untuk melihat detailnya. Monitor hanya membaca log cadangan – membuat dan menguji cadangan adalah tugas Anda (lihat Ketentuan Penggunaan).</p>\n"
        "<h2>Pembaruan</h2>\n"
        "<p>Program memeriksa versi baru secara otomatis dan memperbarui diri dengan satu klik. Setiap paket diverifikasi dengan SHA-256 dan hanya berasal dari <b>claudeusagemonitor.com</b>. Versi baru dan catatan rilis: {site}</p>\n"
        "<h2>Privasi</h2>\n"
        "<p>Tanpa telemetri, tanpa pelacakan. Data masuk claude.ai disimpan terenkripsi hanya di komputer ini; tidak ada yang dikirim ke tempat lain.</p>\n"
        "<h2>Jika ada yang tidak beres</h2>\n"
        "<ul>\n"
        "<li><i>429 / rate limited</i> – server memperlambat permintaan; program mencoba lagi secara otomatis.</li>\n"
        "<li>Tidak ada data – periksa <i>Sumber data</i>; untuk claude.ai, masuk lagi.</li>\n"
        "<li>Riwayat disimpan selama 7 hari dan tetap ada setelah mulai ulang maupun pembaruan.</li>\n"
        "<li>Log dan pengaturan: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Dibuat oleh",
    "help.moved": "Alamat baru sejak 21 September 2026 – halaman lama dinorr.hu/claude-usage-monitor dialihkan ke sini.",
    "help.official": "SITUS WEB RESMI",
    "help.open_site": "Buka claudeusagemonitor.com",
    "help.privacy": "Kebijakan Privasi",
    "help.site_what": "Unduhan, pembaruan otomatis, apa yang baru, Claude Backup Kit, ketentuan penggunaan, dan privasi – semuanya di satu tempat.",
    "help.source_code": "Kode sumber (GitHub)",
    "help.tab_author": "Pembuat",
    "help.tab_guide": "Cara kerja",
    "help.terms": "Ketentuan Penggunaan",
    "help.title": "Bantuan",
    "help.version": "Versi",
    # --- History window ---------------------------------------------------------------------
    "hist.legend_5h": "sesi 5 jam",
    "hist.legend_week": "batas mingguan",
    "hist.no_data": "Data tidak cukup untuk periode ini.",
    "hist.range_24h": "24 jam",
    "hist.range_6h": "6 jam",
    "hist.range_7d": "7 hari",
    "hist.range_all": "Semua",
    "hist.stat_burn": "Rata-rata pemakaian harian",
    "hist.stat_forecast": "Proyeksi akhir minggu",
    "hist.stat_now": "Mingguan saat ini",
    "hist.stat_peak": "Puncak mingguan",
    "hist.stat_sessions": "Sesi 5 jam",
    "hist.title": "riwayat",
    # --- layouts ----------------------------------------------------------------------------
    "layout.compact": "Bilah ramping",
    "layout.postit": "Kartu Post-it",
    "layout.ring": "Cincin",
    # --- context menu -----------------------------------------------------------------------
    "menu.always_top": "Selalu di atas",
    "menu.autostart": "Mulai bersama Windows",
    "menu.backup_bar": "Bilah status cadangan",
    "menu.backups": "Cadangan…",
    "menu.check_update": "Periksa pembaruan program…",
    "menu.click_through": "Tembus klik",
    "menu.details": "Lencana paket dan batas tambahan",
    "menu.feedback": "Pesan untuk pengembang…",
    "menu.help": "Bantuan…",
    "menu.history": "Riwayat & statistik…",
    "menu.language": "Bahasa",
    "menu.layout": "Tata letak",
    "menu.locked": "Kunci posisi",
    "menu.login": "Masuk (claude.ai, browser)…",
    "menu.logout": "Keluar dari akun",
    "menu.model_gauge": "Indikator {}",
    "menu.order": "Urutan",
    "menu.panel_visible": "Tampilkan panel",
    "menu.quit": "Keluar",
    "menu.refresh": "Segarkan data penggunaan sekarang",
    "menu.settings": "Pengaturan…",
    "menu.size": "Ukuran",
    "menu.source": "Sumber data",
    "menu.start_menu": "Tampilkan di menu Mulai",
    "menu.theme": "Tema",
    "menu.update_available": "Pembaruan program: instal versi {}…",
    # --- desktop notifications --------------------------------------------------------------
    "notify.autostart_fail": "Tidak dapat menyiapkan mulai otomatis.",
    "notify.autostart_off": "Dinonaktifkan: aplikasi tidak akan mulai bersama Windows.",
    "notify.autostart_on": "Diaktifkan: aplikasi mulai bersama Windows.",
    "notify.first_run": "Panel muncul di pojok kanan atas layar.\nKlik kanan panel atau ikon baki = menu.",
    "notify.login_ok": "Berhasil masuk – data server segera tiba.",
    "notify.logout": "Anda telah keluar. Beralih ke sumber lokal.",
    "notify.reset_done": "{}: direset — periode baru dimulai.",
    "notify.signin_needed": "Sesi masuk claude.ai telah kedaluwarsa. Klik kanan panel dan masuk lagi agar penggunaan dari semua perangkat Anda tetap terlihat.",
    "notify.stale_body": "Pembacaan terakhir sudah {} yang lalu. Apakah Claude Desktop berjalan?",
    "notify.stale_title": "Data usang",
    "notify.threshold": "{}: {}% terpakai.",
    "notify.update": "Versi program {} tersedia. Klik kanan panel → Pembaruan program.",
    # --- floating panel labels (tight space, UPPERCASE) -------------------------------------
    "panel.five_hour": "SESI 5 JAM",
    "panel.five_hour_short": "5 JAM",
    "panel.full_in": "penuh: {}",
    "panel.model": "{} MINGGUAN",
    "panel.no_data": "Tak ada data",
    "panel.pace": "{} vs tempo",
    "panel.per_day": "{}%/hari",
    "panel.per_hour": "{}%/jam",
    "panel.refreshing": "memuat data",
    "panel.reset": "reset {}",
    "panel.retry_in": "ulangi {} dtk",
    "panel.updated": "diperbarui: {}",
    "panel.week_short": "MGG",
    "panel.weekly": "BATAS MINGGUAN",
    # --- profile ----------------------------------------------------------------------------
    "profile.extra": "Kredit penggunaan: {}",
    "profile.plan": "Paket: {}",
    "profile.since": "Anggota sejak: {}",
    "profile.tier": "Tingkat batas laju: {}",
    # --- Settings window --------------------------------------------------------------------
    "set.about": "{}\nTanpa telemetri. Program ini hanya meminta data penggunaan Anda sendiri dari Anthropic dan membaca nomor versi dari server pembaruan.",
    "set.accent": "Warna aksen",
    "set.always_top": "Di atas semua jendela lain",
    "set.auto": "otomatis",
    "set.backup_config": "Konfigurasi skrip cadangan",
    "set.backup_details": "Jendela detail menampilkan",
    "set.backup_disclaimer": "Claude Usage Monitor hanya membaca dan menampilkan log cadangan Anda – tidak membuat, memeriksa, atau menjamin cadangan apa pun. Claude Backup Kit adalah titik awal gratis yang ditawarkan sebagai bantuan: siapa pun dapat mengubah skripnya, sehingga kualitas dan kelengkapan cadangan tidak dapat dijamin. Kami tidak bertanggung jawab atas cadangan, kehilangan data, atau kerusakan apa pun. Memastikan cadangan lengkap dan dapat dipulihkan adalah tanggung jawab masing-masing pengguna – uji pemulihan dari waktu ke waktu.",
    "set.backup_disclaimer_h": "Penafian",
    "set.backup_enabled": "Tampilkan bilah status cadangan di panel",
    "set.backup_found": "Ditemukan: {}",
    "set.backup_green": "Hijau hingga",
    "set.backup_label": "Label di samping lampu",
    "set.backup_lamps": "Lampu",
    "set.backup_root": "Folder cadangan",
    "set.backup_tasks": "Filter tugas terjadwal",
    "set.backup_unconfigured": "Folder cadangan belum ditentukan, jadi bilah status tetap tersembunyi. Pilih folder tempat skrip cadangan Anda menyimpan file.",
    "set.backup_yellow": "Kuning hingga",
    "set.browse": "Telusuri…",
    "set.click_through": "Tembus klik (hanya hiasan, mengabaikan mouse)",
    "set.close": "Tutup",
    "set.color_hint": "Warna berubah sesuai ambang batas: hijau → kuning → merah.",
    "set.danger": "Kritis",
    "set.data_hint": "Log lokal: file plan-usage-history.json milik Claude Desktop. Tidak perlu masuk, tetapi hanya mengukur PC ini dan disegarkan kira-kira setiap 5 menit.\n\nclaude.ai: setelah masuk, program mengambil data dari server. Anda melihat penggunaan dari semua perangkat Anda, dengan waktu reset yang tepat dan penyegaran yang lebih sering.",
    "set.datafile": "File data",
    "set.default": "Bawaan",
    "set.details_api_only": "Data ini berasal dari sumber data claude.ai (perlu masuk); log lokal tidak memuatnya.",
    "set.file_filter": "JSON (*.json);;Semua file (*.*)",
    "set.gauge_order": "Urutan indikator",
    "set.hours_suffix": " jam",
    "set.layout": "Tata letak",
    "set.local_models_hint": "Server hanya menyimpan penghitung terpisah untuk model tertentu (mis. Fable). Untuk model lainnya, bagian ini menunjukkan pembagian pekerjaan Claude Code minggu ini di PC ini – porsi dari penggunaan Anda sendiri dan token keluaran, bukan porsi dari suatu batas. Hanya nama model dan jumlah token yang dibaca, tidak pernah isi percakapan.",
    "set.local_models_none": "Folder log Claude Code tidak ditemukan – grup ini tetap tersembunyi saja. Bagian lain tidak terpengaruh.",
    "set.local_models_path": "Folder log Claude Code",
    "set.lock": "Kunci posisi (tidak dapat diseret)",
    "set.login_btn_in": "Keluar dari claude.ai",
    "set.login_btn_out": "Masuk ke claude.ai…",
    "set.model_filter": "Model yang dipantau",
    "set.model_scale": "Ukuran indikator model",
    "set.not_set": "belum diatur",
    "set.notify_enabled": "Beri tahu saat melewati ambang batas",
    "set.notify_reset": "Beri tahu saat suatu batas direset",
    "set.notify_stale": "Beri tahu saat data menjadi usang",
    "set.opacity": "Opasitas",
    "set.open_config": "Buka folder pengaturan",
    "set.pick_color": "Pilih warna…",
    "set.pick_file_title": "Pilih log penggunaan",
    "set.profile": "Profil / akun",
    "set.profile_auto": "Otomatis (terakhir digunakan)",
    "set.profile_n": "Profil {} – …{}",
    "set.refresh": "Penyegaran",
    "set.reset_confirm": "Apakah Anda yakin ingin memulihkan pengaturan bawaan?",
    "set.restore": "Pulihkan bawaan",
    "set.rows_available": "Yang dapat ditampilkan saat ini – hapus centang yang tidak ingin Anda lihat:",
    "set.rows_none": "Saat ini server tidak mengirim batas lain untuk akun Anda. Batas tersebut akan muncul di sini secara otomatis begitu dikirim.",
    "set.sec_suffix": " dtk",
    "set.show_age": "Kesegaran data",
    "set.show_burn": "Laju pemakaian (%/jam, %/hari)",
    "set.show_extra_usage": "Kredit penggunaan (bayar sesuai pemakaian)",
    "set.show_feedback_icon": "Ikon pesan di header panel",
    "set.show_five_hour": "Tampilkan sesi 5 jam",
    "set.show_local_models": "Pembagian antarmodel, dari log Claude Code di PC ini",
    "set.show_model": "Tampilkan batas mingguan model (sumber claude.ai)",
    "set.show_model_list": "Batas mingguan model lainnya",
    "set.show_plan_badge": "Lencana paket di header (Pro / Max…)",
    "set.show_plan_name": "Tampilkan nama saya di lencana",
    "set.show_reset": "Hitung mundur hingga reset",
    "set.show_spark": "Kurva tren (sparkline)",
    "set.show_surfaces": "Batas per platform (Claude Code, aplikasi terhubung…)",
    "set.show_weekly": "Tampilkan batas mingguan",
    "set.size": "Ukuran",
    "set.snap": "Tempel ke tepi layar",
    "set.source_api": "claude.ai – semua perangkat (perlu masuk)",
    "set.source_label": "Sumber pengukuran",
    "set.source_local": "Log lokal – hanya PC ini",
    "set.tab_alerts": "Peringatan",
    "set.tab_appearance": "Tampilan",
    "set.tab_content": "Konten",
    "set.tab_data": "Sumber data",
    "set.tab_details": "Detail",
    "set.tab_system": "Sistem",
    "set.taskbar": "Tampilkan di bilah tugas (sebagai jendela)",
    "set.theme": "Tema",
    "set.theme_default": "Bawaan tema",
    "set.tip": "Tips: seret panel dengan tombol kiri, Ctrl+gulir mengubah ukuran,\nklik kanan = menu, klik dua kali = riwayat.",
    "set.title": "pengaturan",
    "set.tray_five": "Sesi 5 jam",
    "set.tray_max": "Mana yang lebih tinggi",
    "set.tray_value": "Nilai ikon baki",
    "set.tray_weekly": "Batas mingguan",
    "set.update_check": "Periksa pembaruan program secara otomatis",
    "set.version": "Versi",
    "set.visible": "Panel mengambang terlihat",
    "set.warn": "Peringatan",
    # --- sizes, sources, themes -------------------------------------------------------------
    "size.extra": "Ekstra",
    "size.large": "Besar",
    "size.normal": "Normal",
    "size.small": "Kecil",
    "source.api": "claude.ai (semua perangkat)",
    "source.local": "Lokal (hanya PC ini)",
    "theme.claude": "Claude (gelap hangat)",
    "theme.graphite": "Grafit",
    "theme.midnight": "Kaca tengah malam",
    "theme.neon": "Neon",
    "theme.paper": "Kertas terang",
    "theme.postit": "Kuning Post-it",
    # --- time formats (panel) ---------------------------------------------------------------
    "time.day": "{} hr",
    "time.dh": "{}h {}j",
    "time.hm": "{}j {}m",
    "time.hour": "{} jam",
    "time.m": "{}m",
    "time.min": "{} mnt",
    "time.none": "tak ada data",
    "time.sec": "{} dtk",
    # --- tray -------------------------------------------------------------------------------
    "tray.head": "5 jam: {}%   ·   Mgg: {}%",
    "tray.line": "{}: {}%",
    # --- program update ---------------------------------------------------------------------
    "update.available": "Versi {} tersedia.",
    "update.check_failed": "Tidak dapat memeriksa pembaruan: {}",
    "update.check_now": "Periksa sekarang",
    "update.checking": "Memeriksa pembaruan…",
    "update.downloading": "Mengunduh… {} dari {}",
    "update.failed": "Pembaruan gagal: {}",
    "update.install": "Instal sekarang",
    "update.installed": "Versi terinstal: {}",
    "update.later": "Nanti",
    "update.manual": "Salinan ini tidak dapat memperbarui dirinya sendiri (berjalan dari kode sumber atau folder baca-saja). Sebagai gantinya, unduh paket yang baru.",
    "update.open_page": "Buka halaman unduhan",
    "update.restarting": "Menginstal – aplikasi akan dimulai ulang sebentar lagi.",
    "update.skip": "Lewati versi ini",
    "update.title": "Pembaruan program",
    "update.uptodate": "Anda sudah memakai versi terbaru.",
    "update.verifying": "Memverifikasi dan mengekstrak…",
    "update.whats_new": "Apa yang baru",
}

# macOS wording (Apple Bahasa Indonesia): "Buka saat masuk" instead of "Mulai bersama Windows", bar menu instead of baki
STRINGS_MAC = {
    "menu.autostart": "Buka saat masuk",
    "notify.autostart_on": "Diaktifkan: aplikasi dibuka saat Anda masuk.",
    "notify.autostart_off": "Dinonaktifkan: aplikasi tidak akan dibuka saat masuk.",
    "notify.first_run": "Panel muncul di pojok kanan atas layar.\nKlik kanan panel atau ikon di bar menu = menu.",
}
