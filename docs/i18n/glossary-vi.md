# Bảng thuật ngữ – Tiếng Việt (vi)

Claude Usage Monitor – giao diện người dùng. Một thuật ngữ = một cách dịch cố định, dùng thống nhất
trong toàn bộ mô-đun `claude_usage/langs/vi.py`.

## Giọng văn và cách xưng hô

- **Xưng hô:** người dùng là **"bạn"**, chương trình/tác giả xưng **"tôi"** chỉ trong cửa sổ "Tin nhắn cho
  nhà phát triển" (tác giả nói trực tiếp). Ở mọi nơi khác chương trình không tự xưng.
- **Giọng:** thân thiện, ngắn, tự tin – như tiếng Anh. Câu lệnh dùng động từ trần ("Nhấp chuột phải vào
  bảng", "Hãy đăng nhập lại" khi cần nhấn mạnh), không dùng "xin vui lòng" dày đặc; "vui lòng" chỉ trong
  thông báo lỗi lịch sự.
- **Viết hoa:** viết hoa chữ cái đầu câu; nhãn bảng nổi VIẾT HOA TOÀN BỘ **kèm đầy đủ dấu** (PHIÊN 5 GIỜ,
  GIỚI HẠN TUẦN).
- **Chuẩn hóa:** mọi chuỗi ở dạng NFC (chữ có dấu là một mã điểm: ệ, ở, ữ).
- **Thuật ngữ nền tảng:** theo Microsoft tiếng Việt cho Windows (Đăng nhập / Đăng xuất, Cài đặt, Thông báo,
  thanh tác vụ, khay hệ thống, thư mục, cập nhật, máy chủ, tải xuống, menu Bắt đầu); theo Apple tiếng
  Việt cho 4 chuỗi macOS (thanh menu, "Mở khi đăng nhập").
- **Định dạng ngày:** dd/mm/yyyy (06/10/2026).

## Tên tài liệu pháp lý

| Tiếng Anh | Tiếng Việt | Lý do |
|---|---|---|
| Privacy Notice / Privacy policy | **Chính sách quyền riêng tư** | Thuật ngữ mà Microsoft, Apple, Google, Meta và các nền tảng lớn dùng cho tài liệu này ở Việt Nam; người dùng nhận ra ngay. ("Thông báo bảo mật" là cách dịch sát chữ nhưng không phải tên gọi thông dụng.) |
| Terms of use | Điều khoản sử dụng | |
| Disclaimer | Tuyên bố miễn trừ trách nhiệm | |
| GDPR | GDPR (giữ nguyên, kèm số điều: Điều 6(1)(f)) | Không có tên chính thức tiếng Việt |
| supervisory authority | cơ quan giám sát; "cơ quan có thẩm quyền ở quốc gia của bạn" | |
| controller / processor | bên kiểm soát dữ liệu / bên xử lý dữ liệu | |
| legitimate interest / consent | lợi ích hợp pháp / sự đồng ý | |
| access, rectification, erasure, restriction, objection | truy cập, chỉnh sửa, xóa, hạn chế xử lý, phản đối | |
| profiling / automated decision-making | lập hồ sơ / ra quyết định tự động | |

## Thuật ngữ sản phẩm

| Tiếng Anh | Tiếng Việt |
|---|---|
| 5-hour session | phiên 5 giờ (nhãn bảng: PHIÊN 5 GIỜ; ngắn: 5 GIỜ) |
| weekly limit | giới hạn tuần (GIỚI HẠN TUẦN; ngắn: TUẦN) |
| per-model weekly limit | giới hạn tuần theo mô hình |
| model | mô hình |
| reset | đặt lại |
| pace | nhịp |
| burn rate | tốc độ tiêu hao |
| usage | mức sử dụng |
| usage credits | tín dụng sử dụng |
| pay-as-you-go | trả theo mức dùng |
| plan / plan badge | gói / huy hiệu gói |
| rate-limit tier | bậc giới hạn tốc độ |
| gauge | đồng hồ đo (ngắn: đồng hồ) |
| panel (the floating widget) | bảng (bảng nổi) |
| widget (in help) | tiện ích |
| tray / tray icon | khay hệ thống / biểu tượng khay hệ thống |
| menu bar (macOS) | thanh menu |
| taskbar | thanh tác vụ |
| Start menu | menu Bắt đầu |
| sign in / sign out | đăng nhập / đăng xuất |
| passkey | khóa truy cập |
| notification | thông báo |
| alert | cảnh báo |
| threshold | ngưỡng |
| warning / critical (threshold levels) | cảnh báo / nguy cấp |
| backup | sao lưu (bản sao lưu) |
| backup script | tập lệnh sao lưu |
| snapshot | ảnh chụp nhanh |
| vault (Obsidian) | kho |
| lamp | đèn báo |
| scheduled task | tác vụ đã lên lịch |
| data source | nguồn dữ liệu |
| local log | nhật ký cục bộ |
| log / log file | nhật ký / tệp nhật ký |
| profile | hồ sơ |
| theme | chủ đề |
| layout | bố cục |
| settings | cài đặt |
| update / check for updates | cập nhật / kiểm tra bản cập nhật |
| download | tải xuống |
| upload | tải lên |
| history | lịch sử |
| projection / forecast | dự báo |
| stale data / data freshness | dữ liệu đã cũ / độ mới của dữ liệu |
| fresh / getting old / outdated | mới / đang cũ dần / đã cũ |
| refresh | làm mới |
| server | máy chủ |
| endpoint | điểm cuối |
| folder | thư mục |
| file | tệp |
| message to the developer | tin nhắn cho nhà phát triển |
| rating | đánh giá |
| consent (checkbox) | Tôi đã đọc và chấp nhận … |
| telemetry | thu thập dữ liệu từ xa |
| tracking | theo dõi |
| click-through | nhấp xuyên qua |
| lock position | khóa vị trí |
| always on top | luôn ở trên cùng |
| snap to screen edge | bám vào mép màn hình |
| opacity | độ mờ đục |
| accent color | màu nhấn |
| size: small / normal / large / extra | nhỏ / vừa / lớn / rất lớn |
| slim bar / post-it card / rings | thanh mỏng / thẻ giấy nhớ / vòng tròn |
| connected apps | ứng dụng đã kết nối |
| surface (Claude Code, apps…) | kênh |
| sparkline | đường xu hướng (sparkline) |
| right-click / double-click / drag | nhấp chuột phải / nhấp đúp / kéo |
| mouse wheel | cuộn chuột |

## Đơn vị thời gian

| Tiếng Anh | Đầy đủ | Viết tắt (chỉ nơi tiếng Anh viết tắt) |
|---|---|---|
| day | ngày | n |
| hour | giờ | g |
| minute | phút | ph |
| second | giây | s |

Ví dụ: `{}n {}g`, `{}g {}ph`, `{} giây`, `thử lại sau {} s`.

## Không dịch

Claude, Claude Desktop, Claude Code, claude.ai, Anthropic, Fable, Opus, Sonnet, Haiku, PRO/MAX/TEAM/ENTERPRISE,
OneDrive, Nextcloud, Obsidian, Cowork, rclone, PowerShell, HTTP(S), TLS, JSON, OAuth, SHA-256, DPAPI, GDPR,
NAIH, GitHub, MIT, Claude Backup Kit, claudeusagemonitor.com, Vidovics Gábor, tên tệp và đường dẫn, `*.json`.
