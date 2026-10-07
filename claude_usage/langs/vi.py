# -*- coding: utf-8 -*-
"""Tiếng Việt – UI strings of Claude Usage Monitor."""

CODE = "vi"
NAME = "Tiếng Việt"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{}n",
    "backup.age_h": "{}g",
    "backup.age_m": "{}ph",
    "backup.and_more": "…và {} mục nữa",
    "backup.checked_at": "Đã kiểm tra: {}",
    "backup.checking": "Đang kiểm tra…",
    "backup.cloud_only": "Ảnh chụp nhanh chỉ có trực tuyến trong OneDrive; không liệt kê nội dung để khỏi phải tải xuống.",
    "backup.comp.cowork": "Nhật ký trò chuyện Cowork (mỗi phiên một ZIP)",
    "backup.comp.vault": "Ảnh chụp nhanh kho Obsidian (ZIP)",
    "backup.disclaimer_short": "Trình giám sát chỉ hiển thị những gì nhật ký sao lưu ghi lại. Chúng tôi không chịu trách nhiệm về các bản sao lưu – bạn cần tự kiểm tra xem chúng có đầy đủ và khôi phục được hay không.",
    "backup.done": "xong",
    "backup.dry_run": "(chạy thử, không tải lên gì)",
    "backup.failed": "LỖI",
    "backup.files_size": "{} tệp, {}",
    "backup.folders": "Thư mục",
    "backup.label_age": "Tên và thời gian",
    "backup.label_name": "Chỉ tên",
    "backup.label_none": "Chỉ đèn báo",
    "backup.last_ok": "Sao lưu thành công gần nhất: {} ({} trước)",
    "backup.last_run": "Lần chạy gần nhất: {} – {}",
    "backup.legend": "Xanh lục: không quá {} giờ · Vàng: đến {} giờ · Đỏ: cũ hơn, hoặc không có bản sao lưu",
    "backup.level_green": "Mới",
    "backup.level_none": "Không tìm thấy bản sao lưu",
    "backup.level_red": "Đã cũ",
    "backup.level_yellow": "Đang cũ dần",
    "backup.log_file": "Tệp nhật ký",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Không tìm thấy thư mục sao lưu: {}",
    "backup.none_found": "Không có.",
    "backup.open": "mở",
    "backup.rc_copied": "đã sao chép các tệp mới hoặc đã thay đổi",
    "backup.rc_failed": "LỖI (mã {})",
    "backup.rc_nochange": "đã đồng bộ, không có gì để sao chép",
    "backup.recent_notes": "Ghi chú được sửa gần đây nhất trong ảnh chụp nhanh",
    "backup.refresh": "Kiểm tra ngay",
    "backup.sec_components": "Những gì được sao lưu",
    "backup.sec_contents": "Nội dung",
    "backup.sec_log": "Nhật ký (các dòng cuối)",
    "backup.sec_problems": "Lỗi và cảnh báo",
    "backup.sec_tasks": "Tác vụ đã lên lịch",
    "backup.skipped": "đã bỏ qua (không tìm thấy thư mục)",
    "backup.snap_kept": "Đang giữ {} ảnh chụp nhanh, tổng cộng {}",
    "backup.snapshot": "Ảnh chụp nhanh mới nhất",
    "backup.source": "Nguồn",
    "backup.state_error": "kết thúc nhưng có lỗi",
    "backup.state_interrupted": "chưa hoàn tất",
    "backup.state_ok": "hoàn tất thành công",
    "backup.state_running": "đang chạy",
    "backup.storage": "Lưu trữ từ xa: đã dùng {} / {}, còn trống {}",
    "backup.target": "Đích",
    "backup.task_event": "khi có sự kiện",
    "backup.task_row": "chạy gần nhất {} · kết quả {} · lần tới {}",
    "backup.tip_click": "Nhấp để xem chi tiết",
    "backup.title": "Sao lưu",
    "backup.tray": "Sao lưu: {}",
    "backup.uploaded": "Đã tải lên trong lần chạy này: {} mới, {} thay thế, {} lỗi",
    "backup.uploaded_files": "Tệp đã tải lên",
    "backup.uploaded_groups": "Tệp đã tải lên theo thư mục",
    "backup.uploaded_no": "Đã tải lên Nextcloud: chưa",
    "backup.uploaded_yes": "Đã tải lên Nextcloud: có ({})",
    "backup.vault": "Kho",
    "backup.vault_changed": "{} ghi chú trong kho đã thay đổi kể từ ảnh chụp nhanh này",
    "backup.zip_new": "{} ZIP mới/đã cập nhật",
    "backup.zip_summary": "{} tệp ({} ghi chú), {} chưa nén",
    # --- details rows -----------------------------------------------------------------------
    "detail.extra": "Tín dụng sử dụng",
    "detail.local_header": "CLAUDE CODE · MÁY NÀY · PHÂN CHIA TUẦN NÀY",
    "detail.off": "tắt",
    "detail.on": "bật",
    "detail.surface.oauth_apps": "Ứng dụng đã kết nối",
    "detail.unlimited": "không giới hạn",
    # --- sign-in dialog ---------------------------------------------------------------------
    "dlg.cancel": "Hủy",
    "dlg.checking": "Đang kiểm tra…",
    "dlg.err_badcode": "Mã không được chấp nhận.\n\n{}\n\nHãy kiểm tra xem bạn đã dán toàn bộ mã chưa, hoặc thử đăng nhập lại qua trình duyệt (luôn dùng mã mới).",
    "dlg.err_ratelimit": "Quá nhiều lần thử đăng nhập trong thời gian ngắn.\n\nMáy chủ đang tạm thời giới hạn bạn. Hãy đóng cửa sổ này, chờ 10–15 phút (đừng thử trong lúc đó), rồi bắt đầu MỘT lần đăng nhập mới qua trình duyệt với mã mới.",
    "dlg.hint1": "Đăng nhập trên trang vừa mở và cho phép truy cập. Cuối cùng bạn sẽ nhận được một mã.",
    "dlg.intro": "Đăng nhập vào tài khoản claude.ai ngay trong trình duyệt của bạn (mật khẩu và khóa truy cập đã lưu ở đó vẫn dùng được).",
    "dlg.login_title": "đăng nhập",
    "dlg.open_browser": "Mở trang đăng nhập trong trình duyệt",
    "dlg.paste_label": "Dán mã bạn nhận được vào đây:",
    "dlg.paste_placeholder": "dán mã vào đây",
    "dlg.signin": "Đăng nhập",
    "dlg.step1": "Bước 1",
    "dlg.step2": "Bước 2",
    "dlg.unknown_err": "Lỗi không xác định.",
    # --- error messages ---------------------------------------------------------------------
    "err.already_running": "Ứng dụng đang chạy rồi (xem khay hệ thống).",
    "err.bad_token_resp": "phản hồi không hợp lệ từ điểm cuối token",
    "err.bad_usage_resp": "phản hồi không hợp lệ từ điểm cuối mức sử dụng",
    "err.connection": "lỗi kết nối: {}",
    "err.file_empty": "Tệp mức sử dụng trống.",
    "err.file_not_found": "Không tìm thấy tệp mức sử dụng.\nClaude Desktop có đang chạy không?",
    "err.file_unreadable": "Hiện không đọc được tệp mức sử dụng.",
    "err.loading": "Đang đăng nhập / truy vấn…",
    "err.network": "lỗi mạng: {}",
    "err.no_code": "Chưa dán mã nào.",
    "err.no_data_profile": "Không có dữ liệu cho hồ sơ này.",
    "err.no_tray": "Khay hệ thống không khả dụng; bỏ qua biểu tượng khay.",
    "err.no_usage_data": "Không có dữ liệu sử dụng.",
    "err.not_signed_in": "Chưa đăng nhập.",
    "err.query_http": "Lỗi truy vấn (HTTP {}).",
    "err.rate_limited": "Máy chủ đang giới hạn tốc độ yêu cầu (429) – sẽ tự động thử lại.",
    "err.session_expired": "Phiên đã hết hạn, hãy đăng nhập lại.",
    "err.session_expired_nl": "Phiên đã hết hạn.\nHãy đăng nhập lại.",
    "err.signin_needed": "Phiên đăng nhập claude.ai đã hết hạn.\nĐăng nhập lại: nhấp chuột phải → Đăng nhập claude.ai",
    "err.unexpected": "Lỗi không mong đợi: {}",
    # --- "Message to the developer" window --------------------------------------------------
    "fb.cancel": "Hủy",
    "fb.close": "Đóng",
    "fb.consent": "Tôi đã đọc và chấp nhận {}.",
    "fb.email": "Email",
    "fb.email_hint": "chỉ khi bạn muốn nhận phản hồi",
    "fb.err_consent": "Để gửi, vui lòng chấp nhận Chính sách quyền riêng tư.",
    "fb.err_email": "Địa chỉ email này có vẻ không đúng.",
    "fb.err_empty": "Hãy viết tin nhắn hoặc chọn mức đánh giá trước.",
    "fb.err_links": "Tin nhắn có quá nhiều liên kết.",
    "fb.err_network": "Không kết nối được với claudeusagemonitor.com. Hãy kiểm tra kết nối và thử lại.",
    "fb.err_rate": "Quá nhiều tin nhắn trong thời gian ngắn – vui lòng thử lại sau.",
    "fb.err_server": "Máy chủ hiện chưa thể nhận tin nhắn. Vui lòng thử lại sau.",
    "fb.intro": "Bạn có ý tưởng, phát hiện lỗi, hay đơn giản là thấy thích? Hãy cho tôi biết. Tôi, Vidovics Gábor – tác giả – tự mình đọc mọi tin nhắn.",
    "fb.message": "Tin nhắn",
    "fb.message_ph": "Điều gì ổn, điều gì chưa ổn, còn thiếu gì?",
    "fb.meta": "Gửi kèm tin nhắn: phiên bản chương trình {0}, hệ điều hành ({1}), ngôn ngữ giao diện ({2}).",
    "fb.name": "Tên",
    "fb.optional": "(không bắt buộc)",
    "fb.privacy_hide": "Ẩn chính sách",
    "fb.privacy_text": (
        "Bên kiểm soát dữ liệu: Vidovics Gábor, cá nhân (Hungary), tác giả của Claude Usage Monitor. "
        "Chính sách quyền riêng tư đầy đủ có trên trang web: https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "Dữ liệu được gửi: những gì bạn nhập ở đây – tên (không bắt buộc), địa chỉ email (không bắt buộc), "
        "tin nhắn, đánh giá sao – và, để tôi hiểu được bối cảnh: phiên bản chương trình, tên và phiên bản "
        "hệ điều hành, ngôn ngữ giao diện và thời điểm gửi. Máy chủ không lưu địa chỉ IP; để ngăn lạm dụng, "
        "máy chủ chỉ dùng một mã băm thay đổi hằng ngày và không thể chuyển ngược lại thành địa chỉ."
        "\n\n"
        "Mục đích: để đọc và trả lời tin nhắn của bạn và để cải thiện chương trình (lợi ích hợp pháp, GDPR "
        "Điều 6(1)(f); bản thân việc trả lời là theo yêu cầu của bạn). Đánh giá và tên của bạn chỉ xuất hiện "
        "trên trang web nếu bạn đánh dấu vào ô riêng dành cho việc đó (sự đồng ý, Điều 6(1)(a)), và chỉ sau "
        "khi tác giả đã xem xét; bạn có thể rút lại sự đồng ý đó bất cứ lúc nào."
        "\n\n"
        "Thời gian lưu trữ: tin nhắn tối đa 2 năm; đánh giá đã công bố cho đến khi bạn rút lại sự đồng ý. "
        "Nếu tác giả đã bật tính năng chuyển tiếp email, một bản sao cũng sẽ được gửi tới hộp thư của tác giả."
        "\n\n"
        "Ai được xem: chỉ bên kiểm soát dữ liệu và – với tư cách bên xử lý dữ liệu – nhà cung cấp dịch vụ "
        "lưu trữ (máy chủ đặt tại EU, Đức). Không có dữ liệu nào bị bán hoặc chuyển giao; không lập hồ sơ "
        "và không ra quyết định tự động."
        "\n\n"
        "Quyền của bạn: truy cập, chỉnh sửa, xóa, hạn chế xử lý, phản đối, rút lại sự đồng ý, và khiếu nại "
        "lên cơ quan giám sát (tại Hungary: NAIH, naih.hu) hoặc cơ quan có thẩm quyền ở quốc gia của bạn. "
        "Liên hệ: biểu mẫu này hoặc trang web."
        "\n\n"
        "Truyền tải: được mã hóa (HTTPS/TLS) tới claudeusagemonitor.com. Phiên bản của văn bản này: 06/10/2026."
    ),
    "fb.privacy_title": "Chính sách quyền riêng tư",
    "fb.publish": "Đánh giá và tên của tôi (nếu có) có thể được hiển thị trên claudeusagemonitor.com.",
    "fb.rating": "Đánh giá chung",
    "fb.rating_clear": "xóa",
    "fb.rating_hint": "không bắt buộc – nhấp vào một ngôi sao",
    "fb.rating_tip": "{} trên 5",
    "fb.secure": "Kết nối được mã hóa (HTTPS) tới claudeusagemonitor.com.",
    "fb.send": "Gửi",
    "fb.sending": "Đang gửi…",
    "fb.sent": "Cảm ơn bạn – tôi đã nhận được tin nhắn!",
    "fb.sent_sub": "Tôi đọc mọi tin nhắn. Nếu bạn để lại địa chỉ email, tôi sẽ trả lời qua đó.",
    "fb.title": "Tin nhắn cho nhà phát triển",
    # --- Help window ------------------------------------------------------------------------
    "help.disclaimer": "Một công cụ độc lập, miễn phí – không do Anthropic tạo ra và không liên kết với Anthropic. “Claude” là nhãn hiệu của Anthropic.",
    "help.feedback": "Câu hỏi, ý tưởng, báo lỗi: biểu mẫu tin nhắn trên trang web.",
    "help.free": "Miễn phí mãi mãi · giấy phép MIT · mã nguồn mở · không thu thập dữ liệu từ xa",
    "help.guide": (
        "\n"
        "<h2>Tiện ích hiển thị gì</h2>\n"
        "<ul>\n"
        "<li><b>Phiên 5 giờ</b> – bạn đã dùng bao nhiêu trong giới hạn của phiên hiện tại. Giới hạn này được đặt lại sau mỗi năm giờ; tiện ích đếm ngược đến lúc đặt lại.</li>\n"
        "<li><b>Giới hạn tuần</b> – mức sử dụng của tất cả mô hình gộp lại; được đặt lại vào một thời điểm cố định hằng tuần của tài khoản bạn.</li>\n"
        "<li><b>Giới hạn tuần theo mô hình</b> – đồng hồ đo thứ ba khi máy chủ báo có (ví dụ cho một mô hình cụ thể).</li>\n"
        "<li><b>Nhịp và tốc độ tiêu hao</b> – bạn đang dùng giới hạn nhanh đến đâu và liệu có đủ đến lúc đặt lại không; dự báo cuối tuần sẽ cảnh báo kịp thời.</li>\n"
        "<li><b>Tín dụng sử dụng</b> và huy hiệu gói của bạn – khi bạn bật chúng trong <i>Huy hiệu gói và giới hạn bổ sung</i>.</li>\n"
        "</ul>\n"
        "<h2>Dữ liệu đến từ đâu</h2>\n"
        "<ul>\n"
        "<li><b>claude.ai (mọi thiết bị)</b> – hỏi máy chủ của Anthropic, nên mức sử dụng trên điện thoại, trong trình duyệt và trên các máy tính khác đều được tính. Cần đăng nhập một lần trong trình duyệt của chính bạn (menu: <i>Đăng nhập</i>). Làm mới 2 phút một lần, chậm hơn nếu máy chủ yêu cầu.</li>\n"
        "<li><b>Cục bộ (chỉ máy này)</b> – đọc nhật ký sử dụng của Claude Desktop trên máy tính này. Không cần đăng nhập, nhưng chỉ biết máy này.</li>\n"
        "</ul>\n"
        "<p>Chuyển đổi giữa hai nguồn trong menu: <i>Nguồn dữ liệu</i>.</p>\n"
        "<h2>Cách dùng tiện ích</h2>\n"
        "<ul>\n"
        "<li><b>Nhấp chuột phải</b> vào tiện ích (hoặc biểu tượng khay hệ thống) – menu đầy đủ.</li>\n"
        "<li><b>Nhấp đúp</b> vào một đồng hồ đo – cửa sổ <b>Lịch sử</b>: 6 giờ, 24 giờ, 7 ngày hoặc tất cả, kèm mức đỉnh, trung bình ngày và dự báo.</li>\n"
        "<li><b>Kéo</b> để di chuyển; tiện ích bám vào mép màn hình. <b>Ctrl + cuộn chuột</b> – to hơn hoặc nhỏ hơn.</li>\n"
        "<li>Bố cục: thẻ giấy nhớ, thanh mỏng, vòng tròn; 6 chủ đề. <i>Khóa vị trí</i> và <i>Nhấp xuyên qua</i> nằm trong Cài đặt.</li>\n"
        "</ul>\n"
        "<h2>Cảnh báo</h2>\n"
        "<p>Vàng từ 70 %, đỏ từ 90 % (có thể điều chỉnh). Có thể bật thông báo khi một giới hạn được đặt lại và khi dữ liệu đang cũ dần.</p>\n"
        "<h2>Sao lưu (tùy chọn)</h2>\n"
        "<p>Các đèn báo nhỏ cho biết các bản sao lưu đã lên lịch của bạn có chạy và hoàn tất hay không. Nhấp vào một đèn để xem chi tiết. Trình giám sát chỉ đọc nhật ký sao lưu – việc tạo và kiểm tra bản sao lưu là việc của bạn (xem Điều khoản sử dụng).</p>\n"
        "<h2>Cập nhật</h2>\n"
        "<p>Chương trình tự kiểm tra phiên bản mới và cập nhật chỉ với một lần nhấp. Mọi gói đều được kiểm tra bằng SHA-256 và chỉ đến từ <b>claudeusagemonitor.com</b>. Phiên bản mới và ghi chú phát hành: {site}</p>\n"
        "<h2>Quyền riêng tư</h2>\n"
        "<p>Không thu thập dữ liệu từ xa, không theo dõi. Thông tin đăng nhập claude.ai được lưu mã hóa chỉ trên máy tính này; không gửi gì đi nơi khác.</p>\n"
        "<h2>Nếu có gì đó không ổn</h2>\n"
        "<ul>\n"
        "<li><i>429 / giới hạn tốc độ</i> – máy chủ đang làm chậm các yêu cầu; chương trình sẽ tự thử lại.</li>\n"
        "<li>Không có dữ liệu – kiểm tra <i>Nguồn dữ liệu</i>; với claude.ai, hãy đăng nhập lại.</li>\n"
        "<li>Lịch sử được giữ 7 ngày và không mất khi khởi động lại hay cập nhật.</li>\n"
        "<li>Nhật ký và cài đặt: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Phát triển bởi",
    "help.moved": "Địa chỉ mới từ ngày 21 tháng 9 năm 2026 – trang cũ dinorr.hu/claude-usage-monitor tự động chuyển hướng về đây.",
    "help.official": "TRANG WEB CHÍNH THỨC",
    "help.open_site": "Mở claudeusagemonitor.com",
    "help.privacy": "Chính sách quyền riêng tư",
    "help.site_what": "Tải xuống, cập nhật tự động, có gì mới, Claude Backup Kit, điều khoản sử dụng và quyền riêng tư – tất cả ở một nơi.",
    "help.source_code": "Mã nguồn (GitHub)",
    "help.tab_author": "Tác giả",
    "help.tab_guide": "Cách hoạt động",
    "help.terms": "Điều khoản sử dụng",
    "help.title": "Trợ giúp",
    "help.version": "Phiên bản",
    # --- History window ---------------------------------------------------------------------
    "hist.legend_5h": "phiên 5 giờ",
    "hist.legend_week": "giới hạn tuần",
    "hist.no_data": "Không đủ dữ liệu cho khoảng thời gian này.",
    "hist.range_24h": "24 giờ",
    "hist.range_6h": "6 giờ",
    "hist.range_7d": "7 ngày",
    "hist.range_all": "Tất cả",
    "hist.stat_burn": "Tiêu hao TB mỗi ngày",
    "hist.stat_forecast": "Dự báo cuối tuần",
    "hist.stat_now": "Tuần này đến nay",
    "hist.stat_peak": "Đỉnh tuần",
    "hist.stat_sessions": "Phiên 5 giờ",
    "hist.title": "lịch sử",
    # --- layouts ----------------------------------------------------------------------------
    "layout.compact": "Thanh mỏng",
    "layout.postit": "Thẻ giấy nhớ",
    "layout.ring": "Vòng tròn",
    # --- context menu -----------------------------------------------------------------------
    "menu.always_top": "Luôn ở trên cùng",
    "menu.autostart": "Khởi động cùng Windows",
    "menu.backup_bar": "Thanh trạng thái sao lưu",
    "menu.backups": "Sao lưu…",
    "menu.check_update": "Kiểm tra bản cập nhật chương trình…",
    "menu.click_through": "Nhấp xuyên qua",
    "menu.details": "Huy hiệu gói và giới hạn bổ sung",
    "menu.feedback": "Gửi tin nhắn cho nhà phát triển…",
    "menu.help": "Trợ giúp…",
    "menu.history": "Lịch sử và thống kê…",
    "menu.language": "Ngôn ngữ",
    "menu.layout": "Bố cục",
    "menu.locked": "Khóa vị trí",
    "menu.login": "Đăng nhập (claude.ai, trình duyệt)…",
    "menu.logout": "Đăng xuất",
    "menu.model_gauge": "Đồng hồ {}",
    "menu.order": "Thứ tự",
    "menu.panel_visible": "Hiện bảng",
    "menu.quit": "Thoát",
    "menu.refresh": "Làm mới dữ liệu sử dụng ngay",
    "menu.settings": "Cài đặt…",
    "menu.size": "Kích cỡ",
    "menu.source": "Nguồn dữ liệu",
    "menu.start_menu": "Hiện trong menu Bắt đầu",
    "menu.theme": "Chủ đề",
    "menu.update_available": "Cập nhật chương trình: cài đặt phiên bản {}…",
    # --- desktop notifications --------------------------------------------------------------
    "notify.autostart_fail": "Không thiết lập được khởi động tự động.",
    "notify.autostart_off": "Đã tắt: ứng dụng sẽ không khởi động cùng Windows.",
    "notify.autostart_on": "Đã bật: ứng dụng khởi động cùng Windows.",
    "notify.first_run": "Bảng đã xuất hiện ở góc trên bên phải màn hình.\nNhấp chuột phải vào bảng hoặc biểu tượng khay hệ thống = menu.",
    "notify.login_ok": "Đã đăng nhập – đang nhận dữ liệu từ máy chủ.",
    "notify.logout": "Đã đăng xuất. Đã chuyển sang nguồn cục bộ.",
    "notify.reset_done": "{}: đã đặt lại — một chu kỳ mới đã bắt đầu.",
    "notify.signin_needed": "Phiên đăng nhập claude.ai đã hết hạn. Nhấp chuột phải vào bảng và đăng nhập lại để tiếp tục xem mức sử dụng từ mọi thiết bị của bạn.",
    "notify.stale_body": "Lần đọc gần nhất cách đây {}. Claude Desktop có đang chạy không?",
    "notify.stale_title": "Dữ liệu đã cũ",
    "notify.threshold": "{}: đã dùng {}%.",
    "notify.update": "Đã có phiên bản {} của chương trình. Nhấp chuột phải vào bảng → Cập nhật chương trình.",
    # --- floating panel labels (tight space, UPPERCASE) -------------------------------------
    "panel.five_hour": "PHIÊN 5 GIỜ",
    "panel.five_hour_short": "5 GIỜ",
    "panel.full_in": "đầy: {}",
    "panel.model": "{} TUẦN",
    "panel.no_data": "Không có dữ liệu",
    "panel.pace": "{} so với nhịp",
    "panel.per_day": "{}%/ngày",
    "panel.per_hour": "{}%/giờ",
    "panel.refreshing": "đang tải dữ liệu",
    "panel.reset": "đặt lại {}",
    "panel.retry_in": "thử lại sau {} s",
    "panel.updated": "cập nhật: {}",
    "panel.week_short": "TUẦN",
    "panel.weekly": "GIỚI HẠN TUẦN",
    # --- profile ----------------------------------------------------------------------------
    "profile.extra": "Tín dụng sử dụng: {}",
    "profile.plan": "Gói: {}",
    "profile.since": "Thành viên từ: {}",
    "profile.tier": "Bậc giới hạn tốc độ: {}",
    # --- Settings window --------------------------------------------------------------------
    "set.about": "{}\nKhông thu thập dữ liệu từ xa. Chương trình chỉ hỏi Anthropic về mức sử dụng của chính bạn và đọc số phiên bản từ máy chủ cập nhật.",
    "set.accent": "Màu nhấn",
    "set.always_top": "Luôn nằm trên mọi cửa sổ khác",
    "set.auto": "tự động",
    "set.backup_config": "Cấu hình tập lệnh sao lưu",
    "set.backup_details": "Cửa sổ chi tiết hiển thị",
    "set.backup_disclaimer": "Claude Usage Monitor chỉ đọc và hiển thị nhật ký sao lưu của bạn – chương trình không tạo, không kiểm tra và không bảo đảm bất kỳ bản sao lưu nào. Claude Backup Kit là một điểm khởi đầu miễn phí được cung cấp để hỗ trợ: ai cũng có thể sửa các tập lệnh, nên không thể bảo đảm chất lượng và tính đầy đủ của bản sao lưu. Chúng tôi không chịu trách nhiệm về các bản sao lưu, dữ liệu bị mất hay bất kỳ thiệt hại nào. Bảo đảm các bản sao lưu đầy đủ và có thể khôi phục là trách nhiệm của mỗi người – hãy thỉnh thoảng thử khôi phục.",
    "set.backup_disclaimer_h": "Tuyên bố miễn trừ trách nhiệm",
    "set.backup_enabled": "Hiện thanh trạng thái sao lưu trên bảng",
    "set.backup_found": "Đã tìm thấy: {}",
    "set.backup_green": "Xanh lục đến",
    "set.backup_label": "Nhãn cạnh đèn báo",
    "set.backup_lamps": "Đèn báo",
    "set.backup_root": "Thư mục sao lưu",
    "set.backup_tasks": "Bộ lọc tác vụ đã lên lịch",
    "set.backup_unconfigured": "Chưa đặt thư mục sao lưu nên thanh trạng thái vẫn ẩn. Hãy chọn thư mục mà tập lệnh sao lưu của bạn ghi vào.",
    "set.backup_yellow": "Vàng đến",
    "set.browse": "Duyệt…",
    "set.click_through": "Nhấp xuyên qua (chỉ để trang trí, bỏ qua chuột)",
    "set.close": "Đóng",
    "set.color_hint": "Màu thay đổi theo ngưỡng: xanh lục → vàng → đỏ.",
    "set.danger": "Nguy cấp",
    "set.data_hint": "Nhật ký cục bộ: tệp plan-usage-history.json của Claude Desktop. Không cần đăng nhập, nhưng chỉ đo máy này và làm mới khoảng 5 phút một lần.\n\nclaude.ai: sau khi đăng nhập, chương trình truy vấn máy chủ. Bạn thấy mức sử dụng từ mọi thiết bị của mình, với thời điểm đặt lại chính xác và làm mới thường xuyên hơn.",
    "set.datafile": "Tệp dữ liệu",
    "set.default": "Mặc định",
    "set.details_api_only": "Những mục này đến từ nguồn dữ liệu claude.ai (cần đăng nhập); nhật ký cục bộ không chứa chúng.",
    "set.file_filter": "JSON (*.json);;Tất cả tệp (*.*)",
    "set.gauge_order": "Thứ tự đồng hồ đo",
    "set.hours_suffix": " giờ",
    "set.layout": "Bố cục",
    "set.local_models_hint": "Máy chủ chỉ giữ bộ đếm riêng cho một số mô hình (ví dụ Fable). Với các mô hình khác, mục này cho thấy công việc Claude Code tuần này trên máy này được phân chia thế nào - tỷ lệ trong mức sử dụng của chính bạn và số token đầu ra, không phải tỷ lệ của một giới hạn. Chỉ đọc tên mô hình và số lượng token, không bao giờ đọc nội dung hội thoại.",
    "set.local_models_none": "Không tìm thấy thư mục nhật ký Claude Code - nhóm này chỉ đơn giản được ẩn đi. Mọi thứ khác không bị ảnh hưởng.",
    "set.local_models_path": "Thư mục nhật ký Claude Code",
    "set.lock": "Khóa vị trí (không kéo được)",
    "set.login_btn_in": "Đăng xuất khỏi claude.ai",
    "set.login_btn_out": "Đăng nhập claude.ai…",
    "set.model_filter": "Mô hình cần theo dõi",
    "set.model_scale": "Kích cỡ đồng hồ mô hình",
    "set.not_set": "chưa đặt",
    "set.notify_enabled": "Thông báo khi vượt ngưỡng",
    "set.notify_reset": "Thông báo khi một giới hạn được đặt lại",
    "set.notify_stale": "Thông báo khi dữ liệu đã cũ",
    "set.opacity": "Độ mờ đục",
    "set.open_config": "Mở thư mục cài đặt",
    "set.pick_color": "Chọn màu…",
    "set.pick_file_title": "Chọn nhật ký sử dụng",
    "set.profile": "Hồ sơ / tài khoản",
    "set.profile_auto": "Tự động (dùng gần nhất)",
    "set.profile_n": "Hồ sơ {} – …{}",
    "set.refresh": "Làm mới",
    "set.reset_confirm": "Bạn có chắc muốn khôi phục cài đặt mặc định không?",
    "set.restore": "Khôi phục mặc định",
    "set.rows_available": "Những gì có thể hiển thị ngay bây giờ – bỏ chọn mục bạn không muốn thấy:",
    "set.rows_none": "Hiện máy chủ không gửi thêm giới hạn nào cho tài khoản của bạn. Khi có, chúng sẽ tự xuất hiện ở đây.",
    "set.sec_suffix": " giây",
    "set.show_age": "Độ mới của dữ liệu",
    "set.show_burn": "Tốc độ tiêu hao (%/giờ, %/ngày)",
    "set.show_extra_usage": "Tín dụng sử dụng (trả theo mức dùng)",
    "set.show_feedback_icon": "Biểu tượng tin nhắn trên đầu bảng",
    "set.show_five_hour": "Hiện phiên 5 giờ",
    "set.show_local_models": "Phân chia giữa các mô hình, từ nhật ký Claude Code trên máy này",
    "set.show_model": "Hiện giới hạn tuần của mô hình (nguồn claude.ai)",
    "set.show_model_list": "Giới hạn tuần của các mô hình khác",
    "set.show_plan_badge": "Huy hiệu gói trên đầu bảng (Pro / Max…)",
    "set.show_plan_name": "Hiện tên tôi trên huy hiệu",
    "set.show_reset": "Đếm ngược đến lúc đặt lại",
    "set.show_spark": "Đường xu hướng (sparkline)",
    "set.show_surfaces": "Giới hạn theo kênh (Claude Code, ứng dụng đã kết nối…)",
    "set.show_weekly": "Hiện giới hạn tuần",
    "set.size": "Kích cỡ",
    "set.snap": "Bám vào mép màn hình",
    "set.source_api": "claude.ai – mọi thiết bị (cần đăng nhập)",
    "set.source_label": "Nguồn đo",
    "set.source_local": "Nhật ký cục bộ – chỉ máy này",
    "set.tab_alerts": "Cảnh báo",
    "set.tab_appearance": "Giao diện",
    "set.tab_content": "Nội dung",
    "set.tab_data": "Nguồn dữ liệu",
    "set.tab_details": "Chi tiết",
    "set.tab_system": "Hệ thống",
    "set.taskbar": "Hiện trên thanh tác vụ (dưới dạng cửa sổ)",
    "set.theme": "Chủ đề",
    "set.theme_default": "Mặc định của chủ đề",
    "set.tip": "Mẹo: kéo bảng bằng nút chuột trái, Ctrl+cuộn để đổi kích cỡ,\nnhấp chuột phải = menu, nhấp đúp = lịch sử.",
    "set.title": "cài đặt",
    "set.tray_five": "Phiên 5 giờ",
    "set.tray_max": "Giá trị cao hơn",
    "set.tray_value": "Giá trị trên biểu tượng khay",
    "set.tray_weekly": "Giới hạn tuần",
    "set.update_check": "Tự động kiểm tra bản cập nhật chương trình",
    "set.version": "Phiên bản",
    "set.visible": "Hiện bảng nổi",
    "set.warn": "Cảnh báo",
    # --- sizes, sources, themes -------------------------------------------------------------
    "size.extra": "Rất lớn",
    "size.large": "Lớn",
    "size.normal": "Vừa",
    "size.small": "Nhỏ",
    "source.api": "claude.ai (mọi thiết bị)",
    "source.local": "Cục bộ (chỉ máy này)",
    "theme.claude": "Claude (tối ấm)",
    "theme.graphite": "Than chì",
    "theme.midnight": "Kính nửa đêm",
    "theme.neon": "Neon",
    "theme.paper": "Giấy sáng",
    "theme.postit": "Vàng giấy nhớ",
    # --- time formats (panel) ---------------------------------------------------------------
    "time.day": "{} ngày",
    "time.dh": "{}n {}g",
    "time.hm": "{}g {}ph",
    "time.hour": "{} giờ",
    "time.m": "{}ph",
    "time.min": "{} phút",
    "time.none": "không có dữ liệu",
    "time.sec": "{} giây",
    # --- tray -------------------------------------------------------------------------------
    "tray.head": "5 giờ: {}%   ·   Tuần: {}%",
    "tray.line": "{}: {}%",
    # --- program update ---------------------------------------------------------------------
    "update.available": "Đã có phiên bản {}.",
    "update.check_failed": "Không kiểm tra được bản cập nhật: {}",
    "update.check_now": "Kiểm tra ngay",
    "update.checking": "Đang kiểm tra bản cập nhật…",
    "update.downloading": "Đang tải xuống… {} / {}",
    "update.failed": "Cập nhật không thành công: {}",
    "update.install": "Cài đặt ngay",
    "update.installed": "Phiên bản đã cài: {}",
    "update.later": "Để sau",
    "update.manual": "Bản này không thể tự cập nhật (chạy từ mã nguồn hoặc thư mục chỉ đọc). Thay vào đó, hãy tải xuống gói mới.",
    "update.open_page": "Mở trang tải xuống",
    "update.restarting": "Đang cài đặt – ứng dụng sẽ khởi động lại trong giây lát.",
    "update.skip": "Bỏ qua phiên bản này",
    "update.title": "Cập nhật chương trình",
    "update.uptodate": "Bạn đang dùng phiên bản mới nhất.",
    "update.verifying": "Đang kiểm tra và giải nén…",
    "update.whats_new": "Có gì mới",
}

# macOS wording (Apple tiếng Việt): "Mở khi đăng nhập" instead of "Khởi động cùng Windows", thanh menu instead of khay
STRINGS_MAC = {
    "menu.autostart": "Mở khi đăng nhập",
    "notify.autostart_on": "Đã bật: ứng dụng mở khi bạn đăng nhập.",
    "notify.autostart_off": "Đã tắt: ứng dụng sẽ không mở khi đăng nhập.",
    "notify.first_run": "Bảng đã xuất hiện ở góc trên bên phải màn hình.\nNhấp chuột phải vào bảng hoặc biểu tượng trên thanh menu = menu.",
}
