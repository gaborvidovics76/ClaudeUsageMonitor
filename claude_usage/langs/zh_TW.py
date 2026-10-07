# -*- coding: utf-8 -*-
"""繁體中文（台灣） – UI strings of Claude Usage Monitor.

你-form, Microsoft / Apple Taiwanese terminology, full-width punctuation.
See docs/i18n/glossary-zh-TW.md for the fixed terms.
"""

CODE = "zh-TW"
NAME = "繁體中文"

STRINGS = {
    # --- backup status bar / details window -------------------------------------------------
    "backup.age_d": "{}天",
    "backup.age_h": "{}小時",
    "backup.age_m": "{}分",
    "backup.and_more": "…還有 {} 個",
    "backup.checked_at": "檢查時間：{}",
    "backup.checking": "檢查中…",
    "backup.cloud_only": "此快照在 OneDrive 中為「僅限線上」檔案；為了不必下載，不會列出其內容。",
    "backup.comp.cowork": "Cowork 聊天記錄（每個工作階段一個 ZIP）",
    "backup.comp.vault": "Obsidian 儲存庫快照（ZIP）",
    "backup.disclaimer_short": "本程式只顯示備份記錄檔中的內容。我們對備份概不負責：備份是否完整、能否還原，需由你自行確認。",
    "backup.done": "完成",
    "backup.dry_run": "（試執行，未上傳任何內容）",
    "backup.failed": "失敗",
    "backup.files_size": "{} 個檔案，{}",
    "backup.folders": "資料夾",
    "backup.label_age": "名稱與時間",
    "backup.label_name": "僅名稱",
    "backup.label_none": "僅燈號",
    "backup.last_ok": "上次成功備份：{}（{} 前）",
    "backup.last_run": "上次執行：{} – {}",
    "backup.legend": "綠燈：{} 小時內 · 黃燈：{} 小時內 · 紅燈：更舊或沒有備份",
    "backup.level_green": "最新",
    "backup.level_none": "找不到備份",
    "backup.level_red": "過舊",
    "backup.level_yellow": "稍舊",
    "backup.log_file": "記錄檔",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "找不到備份資料夾：{}",
    "backup.none_found": "無。",
    "backup.open": "開啟",
    "backup.rc_copied": "已複製新增或變更的檔案",
    "backup.rc_failed": "失敗（錯誤碼 {}）",
    "backup.rc_nochange": "已是最新，無需複製",
    "backup.recent_notes": "快照中最近編輯的筆記",
    "backup.refresh": "立即檢查",
    "backup.sec_components": "備份範圍",
    "backup.sec_contents": "內容",
    "backup.sec_log": "記錄檔（最後幾行）",
    "backup.sec_problems": "錯誤與警告",
    "backup.sec_tasks": "排程工作",
    "backup.skipped": "已略過（找不到資料夾）",
    "backup.snap_kept": "保留 {} 個快照，共 {}",
    "backup.snapshot": "最新快照",
    "backup.source": "來源",
    "backup.state_error": "完成但有錯誤",
    "backup.state_interrupted": "未完成",
    "backup.state_ok": "成功完成",
    "backup.state_running": "執行中",
    "backup.storage": "遠端儲存空間：已用 {} / {}，剩餘 {}",
    "backup.target": "目的地",
    "backup.task_event": "事件觸發",
    "backup.task_row": "上次執行 {} · 結果 {} · 下次 {}",
    "backup.tip_click": "按一下以檢視詳細資料",
    "backup.title": "備份",
    "backup.tray": "備份：{}",
    "backup.uploaded": "本次執行已上傳：{} 個新增、{} 個取代、{} 個錯誤",
    "backup.uploaded_files": "已上傳的檔案",
    "backup.uploaded_groups": "已上傳的檔案（依資料夾）",
    "backup.uploaded_no": "已上傳至 Nextcloud：尚未",
    "backup.uploaded_yes": "已上傳至 Nextcloud：是（{}）",
    "backup.vault": "儲存庫",
    "backup.vault_changed": "自此快照以來，儲存庫中有 {} 則筆記已變更",
    "backup.zip_new": "{} 個新增/更新的 ZIP",
    "backup.zip_summary": "{} 個檔案（{} 則筆記），未壓縮 {}",
    # --- details ---------------------------------------------------------------------------
    "detail.extra": "使用額度",
    "detail.local_header": "CLAUDE CODE · 此電腦 · 本週分佈",
    "detail.off": "關閉",
    "detail.on": "開啟",
    "detail.surface.oauth_apps": "已連線的應用程式",
    "detail.unlimited": "無上限",
    # --- sign-in dialog --------------------------------------------------------------------
    "dlg.cancel": "取消",
    "dlg.checking": "檢查中…",
    "dlg.err_badcode": "授權碼驗證失敗。\n\n{}\n\n請確認已貼上完整的授權碼，或重新在瀏覽器中登入（每次都會取得新的授權碼）。",
    "dlg.err_ratelimit": "短時間內登入嘗試次數過多。\n\n伺服器暫時限制了你的請求。請關閉此視窗，等待 10～15 分鐘（期間不要再嘗試），然後只在瀏覽器中重新登入一次，並使用新的授權碼。",
    "dlg.hint1": "在開啟的頁面登入並允許存取，最後你會收到一組授權碼。",
    "dlg.intro": "在你自己的瀏覽器中登入 claude.ai 帳戶（那裡已可使用你儲存的密碼與密碼金鑰）。",
    "dlg.login_title": "登入",
    "dlg.open_browser": "在瀏覽器中開啟登入頁面",
    "dlg.paste_label": "將收到的授權碼貼在這裡：",
    "dlg.paste_placeholder": "在此貼上授權碼",
    "dlg.signin": "登入",
    "dlg.step1": "步驟 1",
    "dlg.step2": "步驟 2",
    "dlg.unknown_err": "發生未知的錯誤。",
    # --- error messages --------------------------------------------------------------------
    "err.already_running": "程式已在執行中（請檢查系統匣）。",
    "err.bad_token_resp": "權杖端點的回應無效",
    "err.bad_usage_resp": "使用量端點的回應無效",
    "err.connection": "連線錯誤：{}",
    "err.file_empty": "使用量檔案是空的。",
    "err.file_not_found": "找不到使用量檔案。\nClaude Desktop 正在執行嗎？",
    "err.file_unreadable": "目前無法讀取使用量檔案。",
    "err.loading": "登入／查詢中…",
    "err.network": "網路錯誤：{}",
    "err.no_code": "尚未貼上授權碼。",
    "err.no_data_profile": "此設定檔沒有資料。",
    "err.no_tray": "無法使用系統匣，因此不會顯示系統匣圖示。",
    "err.no_usage_data": "沒有使用量資料。",
    "err.not_signed_in": "尚未登入。",
    "err.query_http": "查詢錯誤（HTTP {}）。",
    "err.rate_limited": "伺服器正在限制請求速率（429），將自動重試。",
    "err.session_expired": "登入已過期，請重新登入。",
    "err.session_expired_nl": "登入已過期。\n請重新登入。",
    "err.signin_needed": "claude.ai 登入已過期。\n請重新登入：按右鍵 → 登入 claude.ai",
    "err.unexpected": "非預期的錯誤：{}",
    # --- "Message to the developer" window -------------------------------------------------
    "fb.cancel": "取消",
    "fb.close": "關閉",
    "fb.consent": "我已閱讀並同意{}。",
    "fb.email": "電子郵件",
    "fb.email_hint": "只有希望收到回覆時才需填寫",
    "fb.err_consent": "傳送前請先同意隱私權政策。",
    "fb.err_email": "這個電子郵件地址看起來不正確。",
    "fb.err_empty": "請先寫下訊息或選擇評分。",
    "fb.err_links": "訊息中的連結太多。",
    "fb.err_network": "無法連線到 claudeusagemonitor.com。請檢查網路連線後再試一次。",
    "fb.err_rate": "短時間內傳送的訊息太多，請稍後再試。",
    "fb.err_server": "伺服器目前無法接收訊息，請稍後再試。",
    "fb.intro": "有想法、發現了錯誤，或者只是喜歡這個程式？告訴我吧。每一則訊息都由作者 Vidovics Gábor（也就是我）親自閱讀。",
    "fb.message": "訊息",
    "fb.message_ph": "哪些功能好用、哪些不好用、還缺什麼？",
    "fb.meta": "隨訊息一併傳送：程式版本 {0}、作業系統（{1}）、介面語言（{2}）。",
    "fb.name": "姓名",
    "fb.optional": "（選填）",
    "fb.privacy_hide": "隱藏隱私權政策",
    "fb.privacy_text": (
        "資料控管者：Vidovics Gábor，自然人（匈牙利），Claude Usage Monitor 的作者。完整的隱私權政策請見網站："
        "https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "傳送的內容：你在此輸入的資料，即姓名（選填）、電子郵件地址（選填）、訊息、星級評分，以及為了讓我瞭解背景脈絡"
        "而附帶的：程式版本、作業系統名稱與版本、介面語言和傳送時間。伺服器不儲存 IP 位址；為防止濫用，僅使用一組每日"
        "更換、無法反推回位址的雜湊值。"
        "\n\n"
        "目的：閱讀並回覆你的訊息，以及改進本程式（正當利益，GDPR 第 6 條第 1 項第 f 款；回覆本身則是依你的請求進行）。"
        "只有在你另外勾選專屬的核取方塊（同意，第 6 條第 1 項第 a 款），且經作者審閱之後，你的評分與姓名才會顯示在"
        "網站上；你可以隨時撤回該同意。"
        "\n\n"
        "保留期限：訊息最長保留 2 年；已公開的評分保留至你撤回同意為止。若作者已開啟電子郵件轉寄，副本也會送達作者的信箱。"
        "\n\n"
        "誰會看到：只有資料控管者，以及作為資料處理者的主機代管服務商（伺服器位於歐盟境內的德國）。不會出售或轉交給"
        "任何人；不會進行剖析，也不會進行自動化決策。"
        "\n\n"
        "你的權利：查閱、更正、刪除、限制處理、反對、撤回同意，以及向監督機關（匈牙利：NAIH，naih.hu）或你所在國家的"
        "主管機關提出申訴。聯絡方式：本表單或網站。"
        "\n\n"
        "傳輸：以加密方式（HTTPS/TLS）傳送至 claudeusagemonitor.com。本政策版本：2026 年 10 月 6 日。"
    ),
    "fb.privacy_title": "隱私權政策",
    "fb.publish": "我的評分和姓名（若有填寫）可以顯示在 claudeusagemonitor.com 上。",
    "fb.rating": "整體評分",
    "fb.rating_clear": "清除",
    "fb.rating_hint": "選填，按一下星星即可",
    "fb.rating_tip": "{} / 5",
    "fb.secure": "與 claudeusagemonitor.com 之間為加密連線（HTTPS）。",
    "fb.send": "傳送",
    "fb.sending": "傳送中…",
    "fb.sent": "謝謝你，訊息已送達！",
    "fb.sent_sub": "每一則訊息我都會親自閱讀。如果你留下了電子郵件地址，我會寄信回覆你。",
    "fb.title": "傳訊息給開發者",
    # --- Help window -----------------------------------------------------------------------
    "help.disclaimer": "這是一款獨立的免費工具，並非由 Anthropic 製作，也與 Anthropic 無任何隸屬關係。「Claude」是 Anthropic 的商標。",
    "help.feedback": "問題、想法、錯誤回報：請使用網站上的訊息表單。",
    "help.free": "永久免費 · MIT 授權 · 開放原始碼 · 無遙測",
    "help.guide": (
        "\n"
        "<h2>小工具顯示的內容</h2>\n"
        "<ul>\n"
        "<li><b>5 小時工作階段</b>：目前工作階段的上限已用了多少。每五小時重設一次；小工具會倒數計時到重設為止。</li>\n"
        "<li><b>每週上限</b>：所有模型合計的使用量；在你帳戶固定的每週時間重設。</li>\n"
        "<li><b>各模型每週上限</b>：當伺服器回報時顯示的第三個儀表（例如針對特定模型）。</li>\n"
        "<li><b>步調與消耗速率</b>：你消耗上限的速度，以及能否撐到重設；本週最終預估會及早提醒你。</li>\n"
        "<li><b>使用額度</b>與你的方案標章：在<i>方案標章與額外上限</i>中開啟後顯示。</li>\n"
        "</ul>\n"
        "<h2>資料來源</h2>\n"
        "<ul>\n"
        "<li><b>claude.ai（所有裝置）</b>：向 Anthropic 的伺服器查詢，因此手機、瀏覽器和其他電腦上的使用量也包含在內。"
        "需要在你自己的瀏覽器中登入一次（選單：<i>登入</i>）。每 2 分鐘重新整理一次；若伺服器要求，則會放慢。</li>\n"
        "<li><b>本機（僅此電腦）</b>：讀取這部電腦上 Claude Desktop 的使用量記錄檔。不必登入，但只知道這部電腦的情況。</li>\n"
        "</ul>\n"
        "<p>可在選單的<i>資料來源</i>中切換。</p>\n"
        "<h2>操作小工具</h2>\n"
        "<ul>\n"
        "<li>在小工具（或系統匣圖示）上<b>按右鍵</b>：完整選單。</li>\n"
        "<li>在儀表上<b>按兩下</b>：開啟<b>歷史記錄</b>視窗，6 小時、24 小時、7 天或全部，含峰值、每日平均與預估。</li>\n"
        "<li><b>拖曳</b>即可移動；會貼齊螢幕邊緣。<b>Ctrl + 滑鼠滾輪</b>：放大或縮小。</li>\n"
        "<li>版面配置：便利貼卡片、精簡橫條、環形；6 種佈景主題。<i>鎖定位置</i>與<i>滑鼠穿透</i>在「設定」中。</li>\n"
        "</ul>\n"
        "<h2>警示</h2>\n"
        "<p>達 70% 時變黃色，達 90% 時變紅色（可調整）。可選擇在上限重設時以及資料過時時收到通知。</p>\n"
        "<h2>備份（選用）</h2>\n"
        "<p>小燈號顯示你的排程備份是否已執行並完成。按一下燈號可檢視詳細資料。本程式只讀取備份記錄檔，"
        "製作與測試備份是你的責任（請參閱使用條款）。</p>\n"
        "<h2>更新</h2>\n"
        "<p>程式會自行檢查新版本，並可一鍵更新。每個套件都經過 SHA-256 驗證，且只來自 <b>claudeusagemonitor.com</b>。"
        "新版本與版本資訊：{site}</p>\n"
        "<h2>隱私權</h2>\n"
        "<p>無遙測、無追蹤。claude.ai 的登入資訊只會加密儲存在這部電腦上；不會傳送到其他任何地方。</p>\n"
        "<h2>發生問題時</h2>\n"
        "<ul>\n"
        "<li><i>429 / 速率限制</i>：伺服器正在放慢請求；程式會自行重試。</li>\n"
        "<li>沒有資料：請檢查<i>資料來源</i>；使用 claude.ai 時請重新登入。</li>\n"
        "<li>歷史記錄會保留 7 天，重新啟動與更新後仍會保留。</li>\n"
        "<li>記錄檔與設定：<code>{cfg}</code>（<code>api.log</code>、<code>update.log</code>）。</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "製作者",
    "help.moved": "自 2026 年 9 月 21 日起使用新網址：原本的 dinorr.hu/claude-usage-monitor 頁面會重新導向到這裡。",
    "help.official": "官方網站",
    "help.open_site": "開啟 claudeusagemonitor.com",
    "help.privacy": "隱私權政策",
    "help.site_what": "下載、自動更新、新功能、Claude Backup Kit、使用條款與隱私權，全都在同一個地方。",
    "help.source_code": "原始碼（GitHub）",
    "help.tab_author": "作者",
    "help.tab_guide": "使用說明",
    "help.terms": "使用條款",
    "help.title": "說明",
    "help.version": "版本",
    # --- History window --------------------------------------------------------------------
    "hist.legend_5h": "5 小時工作階段",
    "hist.legend_week": "每週上限",
    "hist.no_data": "此期間的資料不足。",
    "hist.range_24h": "24 小時",
    "hist.range_6h": "6 小時",
    "hist.range_7d": "7 天",
    "hist.range_all": "全部",
    "hist.stat_burn": "日均消耗",
    "hist.stat_forecast": "本週最終預估",
    "hist.stat_now": "本週目前用量",
    "hist.stat_peak": "本週峰值",
    "hist.stat_sessions": "5 小時工作階段",
    "hist.title": "歷史記錄",
    # --- layouts ---------------------------------------------------------------------------
    "layout.compact": "精簡橫條",
    "layout.postit": "便利貼卡片",
    "layout.ring": "環形",
    # --- context menu ----------------------------------------------------------------------
    "menu.always_top": "永遠置頂",
    "menu.autostart": "隨 Windows 啟動",
    "menu.backup_bar": "備份狀態列",
    "menu.backups": "備份…",
    "menu.check_update": "檢查程式更新…",
    "menu.click_through": "滑鼠穿透",
    "menu.details": "方案標章與額外上限",
    "menu.feedback": "傳訊息給開發者…",
    "menu.help": "說明…",
    "menu.history": "歷史記錄與統計…",
    "menu.language": "語言",
    "menu.layout": "版面配置",
    "menu.locked": "鎖定位置",
    "menu.login": "登入（claude.ai，瀏覽器）…",
    "menu.logout": "登出",
    "menu.model_gauge": "{} 儀表",
    "menu.order": "順序",
    "menu.panel_visible": "顯示面板",
    "menu.quit": "結束",
    "menu.refresh": "立即重新整理使用量資料",
    "menu.settings": "設定…",
    "menu.size": "大小",
    "menu.source": "資料來源",
    "menu.start_menu": "顯示在開始功能表",
    "menu.theme": "佈景主題",
    "menu.update_available": "程式更新：安裝 {} 版…",
    # --- desktop notifications -------------------------------------------------------------
    "notify.autostart_fail": "無法設定自動啟動。",
    "notify.autostart_off": "已停用：程式不會隨 Windows 啟動。",
    "notify.autostart_on": "已啟用：程式會隨 Windows 啟動。",
    "notify.first_run": "面板已出現在螢幕右上角。\n在面板或系統匣圖示上按右鍵即可開啟選單。",
    "notify.login_ok": "已登入，正在取得伺服器資料。",
    "notify.logout": "已登出。已切換至本機來源。",
    "notify.reset_done": "{}：已重設，新的週期開始了。",
    "notify.signin_needed": "claude.ai 登入已過期。請在面板上按右鍵並重新登入，才能繼續檢視所有裝置的使用量。",
    "notify.stale_body": "距上次讀取已過 {}。Claude Desktop 正在執行嗎？",
    "notify.stale_title": "資料過時",
    "notify.threshold": "{}：已使用 {}%。",
    "notify.update": "程式 {} 版已推出。請在面板上按右鍵 → 程式更新。",
    # --- panel labels (tight space) --------------------------------------------------------
    "panel.five_hour": "5 小時工作階段",
    "panel.five_hour_short": "5小時",
    "panel.full_in": "用盡：{}",
    "panel.model": "{} 每週",
    "panel.no_data": "無資料",
    "panel.pace": "較步調 {}",
    "panel.per_day": "{}%/天",
    "panel.per_hour": "{}%/時",
    "panel.refreshing": "取得資料中",
    "panel.reset": "重設 {}",
    "panel.retry_in": "{} 秒後重試",
    "panel.updated": "更新：{}",
    "panel.week_short": "週",
    "panel.weekly": "每週上限",
    # --- profile ---------------------------------------------------------------------------
    "profile.extra": "使用額度：{}",
    "profile.plan": "方案：{}",
    "profile.since": "加入日期：{}",
    "profile.tier": "速率限制等級：{}",
    # --- Settings window -------------------------------------------------------------------
    "set.about": "{}\n無遙測。只會向 Anthropic 查詢你自己的使用量，並從更新伺服器讀取版本號。",
    "set.accent": "強調色",
    "set.always_top": "顯示在所有視窗之上",
    "set.auto": "自動",
    "set.backup_config": "備份指令碼設定檔",
    "set.backup_details": "詳細資料視窗顯示",
    "set.backup_disclaimer": "Claude Usage Monitor 只會讀取並顯示你備份的記錄檔，不會製作、檢查或保證任何備份。Claude Backup Kit 是免費提供的入門範本，僅供協助：任何人都能修改其中的指令碼，因此無法保證備份的品質與完整性。我們對備份、資料遺失或任何損害概不負責。確保備份完整且可還原是每個人自己的責任，請不時實際測試一次還原。",
    "set.backup_disclaimer_h": "免責條款",
    "set.backup_enabled": "在面板上顯示備份狀態列",
    "set.backup_found": "已找到：{}",
    "set.backup_green": "綠燈：最多",
    "set.backup_label": "燈號旁的標籤",
    "set.backup_lamps": "燈號",
    "set.backup_root": "備份資料夾",
    "set.backup_tasks": "排程工作篩選條件",
    "set.backup_unconfigured": "尚未設定備份資料夾，因此狀態列保持隱藏。請選擇備份指令碼寫入的資料夾。",
    "set.backup_yellow": "黃燈：最多",
    "set.browse": "瀏覽…",
    "set.click_through": "滑鼠穿透（僅作裝飾，忽略滑鼠）",
    "set.close": "關閉",
    "set.color_hint": "色彩會隨門檻變化：綠色 → 黃色 → 紅色。",
    "set.danger": "嚴重",
    "set.data_hint": "本機記錄檔：Claude Desktop 的 plan-usage-history.json。不必登入，但只計算這部電腦的使用量，且約每 5 分鐘重新整理一次。\n\nclaude.ai：登入後向伺服器查詢。你會看到所有裝置的使用量，有精確的重設時間，重新整理也更頻繁。",
    "set.datafile": "資料檔案",
    "set.default": "預設",
    "set.details_api_only": "這些來自 claude.ai 資料來源（需要登入）；本機記錄檔中沒有這些資料。",
    "set.file_filter": "JSON (*.json);;所有檔案 (*.*)",
    "set.gauge_order": "儀表順序",
    "set.hours_suffix": " 小時",
    "set.layout": "版面配置",
    "set.local_models_hint": "伺服器只為部分模型（例如 Fable）保留獨立的計數器。至於其他模型，這裡顯示的是本週在這部電腦上的 Claude Code 工作如何分佈：這是在你自己的使用量與輸出 token 中所佔的比例，而不是上限的佔比。只會讀取模型名稱與 token 數量，絕不讀取對話內容。",
    "set.local_models_none": "找不到 Claude Code 記錄檔資料夾，這個群組會直接保持隱藏。其他功能不受影響。",
    "set.local_models_path": "Claude Code 記錄檔資料夾",
    "set.lock": "鎖定位置（無法拖曳）",
    "set.login_btn_in": "登出 claude.ai",
    "set.login_btn_out": "登入 claude.ai…",
    "set.model_filter": "要追蹤的模型",
    "set.model_scale": "模型儀表大小",
    "set.not_set": "未設定",
    "set.notify_enabled": "超過門檻時通知",
    "set.notify_reset": "上限重設時通知",
    "set.notify_stale": "資料過時時通知",
    "set.opacity": "不透明度",
    "set.open_config": "開啟設定資料夾",
    "set.pick_color": "選擇色彩…",
    "set.pick_file_title": "選擇使用量記錄檔",
    "set.profile": "設定檔／帳戶",
    "set.profile_auto": "自動（最近使用）",
    "set.profile_n": "設定檔 {} – …{}",
    "set.refresh": "重新整理",
    "set.reset_confirm": "確定要還原預設設定嗎？",
    "set.restore": "還原預設值",
    "set.rows_available": "目前可顯示的內容，請取消勾選你不想看到的：",
    "set.rows_none": "伺服器目前未為你的帳戶傳送其他上限。一旦傳送，就會自動顯示在這裡。",
    "set.sec_suffix": " 秒",
    "set.show_age": "資料新鮮度",
    "set.show_burn": "消耗速率（%/小時、%/天）",
    "set.show_extra_usage": "使用額度（隨用隨付）",
    "set.show_feedback_icon": "面板標題列中的訊息圖示",
    "set.show_five_hour": "顯示 5 小時工作階段",
    "set.show_local_models": "各模型用量分佈（取自這部電腦的 Claude Code 記錄檔）",
    "set.show_model": "顯示模型每週上限（claude.ai 來源）",
    "set.show_model_list": "其他模型的每週上限",
    "set.show_plan_badge": "標題列中的方案標章（Pro / Max…）",
    "set.show_plan_name": "在標章上顯示我的名字",
    "set.show_reset": "重設倒數計時",
    "set.show_spark": "趨勢曲線（走勢圖）",
    "set.show_surfaces": "各介面的上限（Claude Code、已連線的應用程式…）",
    "set.show_weekly": "顯示每週上限",
    "set.size": "大小",
    "set.snap": "貼齊螢幕邊緣",
    "set.source_api": "claude.ai – 所有裝置（需要登入）",
    "set.source_label": "測量來源",
    "set.source_local": "本機記錄檔 – 僅此電腦",
    "set.tab_alerts": "警示",
    "set.tab_appearance": "外觀",
    "set.tab_content": "內容",
    "set.tab_data": "資料來源",
    "set.tab_details": "詳細資料",
    "set.tab_system": "系統",
    "set.taskbar": "顯示在工作列（作為視窗）",
    "set.theme": "佈景主題",
    "set.theme_default": "佈景主題預設值",
    "set.tip": "提示：用滑鼠左鍵拖曳面板，Ctrl + 滾輪調整大小，\n按右鍵 = 選單，按兩下 = 歷史記錄。",
    "set.title": "設定",
    "set.tray_five": "5 小時工作階段",
    "set.tray_max": "以較高者為準",
    "set.tray_value": "系統匣圖示數值",
    "set.tray_weekly": "每週上限",
    "set.update_check": "自動檢查程式更新",
    "set.version": "版本",
    "set.visible": "顯示浮動面板",
    "set.warn": "警告",
    # --- sizes, sources, themes ------------------------------------------------------------
    "size.extra": "特大",
    "size.large": "大",
    "size.normal": "標準",
    "size.small": "小",
    "source.api": "claude.ai（所有裝置）",
    "source.local": "本機（僅此電腦）",
    "theme.claude": "Claude（暖色系深色）",
    "theme.graphite": "石墨",
    "theme.midnight": "午夜玻璃",
    "theme.neon": "霓虹",
    "theme.paper": "淺色紙張",
    "theme.postit": "便利貼黃",
    # --- time formats ----------------------------------------------------------------------
    "time.day": "{} 天",
    "time.dh": "{}天{}時",
    "time.hm": "{}時{}分",
    "time.hour": "{} 小時",
    "time.m": "{}分",
    "time.min": "{} 分鐘",
    "time.none": "無資料",
    "time.sec": "{} 秒",
    # --- tray ------------------------------------------------------------------------------
    "tray.head": "5小時：{}%   ·   週：{}%",
    "tray.line": "{}: {}%",
    # --- program update --------------------------------------------------------------------
    "update.available": "{} 版已推出。",
    "update.check_failed": "無法檢查更新：{}",
    "update.check_now": "立即檢查",
    "update.checking": "正在檢查更新…",
    "update.downloading": "下載中… {} / {}",
    "update.failed": "更新失敗：{}",
    "update.install": "立即安裝",
    "update.installed": "已安裝版本：{}",
    "update.later": "稍後",
    "update.manual": "此副本無法自行更新（從原始碼或唯讀資料夾執行）。請改為下載新的套件。",
    "update.open_page": "開啟下載頁面",
    "update.restarting": "安裝中，程式即將重新啟動。",
    "update.skip": "略過此版本",
    "update.title": "程式更新",
    "update.uptodate": "你使用的已是最新版本。",
    "update.verifying": "驗證與解壓縮中…",
    "update.whats_new": "新功能",
}

# macOS wording: Apple terminology – "login items" instead of "start with Windows", menu bar instead of tray
STRINGS_MAC = {
    "menu.autostart": "登入時開啟",
    "notify.autostart_on": "已啟用：程式會在你登入時開啟。",
    "notify.autostart_off": "已停用：程式不會在登入時開啟。",
    "notify.first_run": "面板已出現在螢幕右上角。\n在面板或選單列圖示上按右鍵即可開啟選單。",
}
