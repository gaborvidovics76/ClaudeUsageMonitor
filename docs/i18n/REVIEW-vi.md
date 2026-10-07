# REVIEW – Tiếng Việt (vi)

## Lektor

Independent native review. The translation was already solid (correct Microsoft terms, consistent "bạn",
uppercase panel labels with full diacritics, NFC everywhere). The changes fix calques, ambiguous wording
and a few unnatural word orders. The glossary needed no change.

### Changes

- backup.disclaimer_short: "…– việc kiểm tra chúng có đầy đủ và khôi phục được hay không là của bạn." → "…– bạn cần tự kiểm tra xem chúng có đầy đủ và khôi phục được hay không." – awkward "là của bạn" ending
- backup.rc_nochange: "đã cập nhật, không có gì để sao chép" → "đã đồng bộ, không có gì để sao chép" – "đã cập nhật" means "updated"
- backup.snap_kept: "Giữ {} ảnh chụp nhanh, tổng cộng {}" → "Đang giữ {} ảnh chụp nhanh, tổng cộng {}" – bare "Giữ" reads as command
- backup.state_error: "kết thúc với lỗi" → "kết thúc nhưng có lỗi" – calque of "with errors"
- backup.task_event: "theo sự kiện" → "khi có sự kiện" – fits "lần tới …" context
- backup.uploaded_yes: "Đã tải lên Nextcloud: rồi ({})" → "Đã tải lên Nextcloud: có ({})" – "rồi" too colloquial
- dlg.intro: "Đăng nhập tài khoản claude.ai của bạn trong trình duyệt của chính bạn (…)" → "Đăng nhập vào tài khoản claude.ai ngay trong trình duyệt của bạn (…)" – double "của bạn" removed
- err.signin_needed: "Đăng nhập claude.ai đã hết hạn.\n…" → "Phiên đăng nhập claude.ai đã hết hạn.\n…" – a session expires, not "sign-in"
- notify.signin_needed: "Đăng nhập claude.ai đã hết hạn. …" → "Phiên đăng nhập claude.ai đã hết hạn. …" – same as above
- err.unexpected: "Lỗi không mong muốn: {}" → "Lỗi không mong đợi: {}" – Microsoft Vietnamese standard term
- fb.err_server: "Máy chủ hiện không nhận được tin nhắn." → "Máy chủ hiện chưa thể nhận tin nhắn." – "không nhận được" = "did not receive"
- fb.intro: "Một ý tưởng, một lỗi, hay đơn giản là bạn thích nó? … Mọi tin nhắn đều do chính tôi, Vidovics Gábor, tác giả, đọc." → "Bạn có ý tưởng, phát hiện lỗi, hay đơn giản là thấy thích? … Tôi, Vidovics Gábor – tác giả – tự mình đọc mọi tin nhắn." – verb-final stacked appositive unnatural
- fb.message_ph: "Điều gì hoạt động tốt, điều gì chưa, còn thiếu gì?" → "Điều gì ổn, điều gì chưa ổn, còn thiếu gì?" – shorter, more idiomatic
- fb.privacy_hide: "Ẩn thông báo" → "Ẩn chính sách" – match title; avoid "notification" sense
- fb.privacy_text: "Phiên bản của thông báo này" → "Phiên bản của văn bản này" – title is "Chính sách", not "thông báo"
- fb.sent: "Cảm ơn bạn – tin nhắn đã đến!" → "Cảm ơn bạn – tôi đã nhận được tin nhắn!" – natural, author's own voice
- help.guide: "kèm đỉnh, trung bình ngày" → "kèm mức đỉnh, trung bình ngày" – bare "đỉnh" too terse
- help.guide: "Tùy chọn thông báo khi…" → "Có thể bật thông báo khi…" – "Tùy chọn" sentence lacked verb
- help.moved: "trang dinorr.hu/claude-usage-monitor cũ sẽ chuyển hướng về đây" → "trang cũ dinorr.hu/claude-usage-monitor tự động chuyển hướng về đây" – "sẽ" wrongly implied future
- hist.stat_now: "Tuần hiện tại" → "Tuần này đến nay" – means current usage, not week
- notify.stale_body: "Lần đọc gần nhất đã cách đây {}." → "Lần đọc gần nhất cách đây {}." – redundant "đã" with "cách đây"
- set.always_top: "Trên tất cả cửa sổ khác" → "Luôn nằm trên mọi cửa sổ khác" – fragment lacked verb
- set.backup_disclaimer: "nên chất lượng và tính đầy đủ của bản sao lưu không thể được bảo đảm" → "nên không thể bảo đảm chất lượng và tính đầy đủ của bản sao lưu" – passive calque removed
- set.backup_disclaimer: "thỉnh thoảng hãy thử khôi phục một lần" → "hãy thỉnh thoảng thử khôi phục" – "một lần" contradicts "thỉnh thoảng"
- set.data_hint: "claude.ai: sau khi đăng nhập sẽ truy vấn máy chủ." → "claude.ai: sau khi đăng nhập, chương trình truy vấn máy chủ." – missing subject
- set.local_models_none: "nhóm này chỉ đơn giản là ẩn đi. Không có gì khác bị ảnh hưởng." → "nhóm này chỉ đơn giản được ẩn đi. Mọi thứ khác không bị ảnh hưởng." – smoother, natural phrasing
- set.theme_default: "Theo chủ đề" → "Mặc định của chủ đề" – clearer as colour option
- set.tip: "bằng nút trái chuột" → "bằng nút chuột trái" – correct Vietnamese word order
- set.tray_value: "Giá trị biểu tượng khay" → "Giá trị trên biểu tượng khay" – missing preposition
- update.manual: "Hãy tải gói mới về." → "Thay vào đó, hãy tải xuống gói mới." – glossary "tải xuống"; keeps "instead"

### Still in doubt

- Time abbreviations `{}n {}g`, `{}g {}ph`, `{}n` (time.dh, time.hm, backup.age_d): "g" (giờ) and "ph" (phút) are the
  newspaper-style abbreviations and read fine; "n" for ngày is not an established abbreviation. Kept for panel
  width and glossary consistency; if space allows, `{} ngày {}g` would be clearer.
- panel.no_data / time.none "Không có dữ liệu" and panel.five_hour_short "5 GIỜ" are longer than the English;
  Vietnamese has no shorter natural form ("5G" would be unreadable). The panel line shrinks to fit.
- panel.reset "đặt lại {}": "đặt lại sau {}" would be more natural but longer; kept short for the panel.
- backup.label_age "Tên và thời gian": "age" has no neat Vietnamese option label ("tuổi" / "độ cũ" sound odd).
- theme.midnight "Kính nửa đêm": a literal but acceptable theme name.
