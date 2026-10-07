# Glossary – 繁體中文（台灣）(zh-TW) – Claude Usage Monitor

## Tone and form of address

- **Form of address: 你** everywhere (never 您). This is how Apple's and Microsoft's Taiwanese UI, LINE,
  PChome and the best local consumer software talk to the user. The legal text (`fb.privacy_text`) also
  uses 你 – the privacy policies of the big platforms in Taiwan do the same, so a 你-form notice reads as
  normal, not casual. One form everywhere, as the brief asks.
- **Register:** short, confident, friendly. Labels, menu items, buttons and tab names are nouns or
  verb-object phrases with no final 。; full sentences (dialogs, hints, notifications, errors, help, legal
  text) end with 。.
- **The author (fb.* texts) speaks in the first person** (我), as the English does.
- **Punctuation:** full-width ，。：；（）、 inside Chinese text; quotes 「」; ellipsis is the single
  character …; the range dash is ～ (10～15 分鐘). Half-width digits and Latin product names. Half-width
  `(*.json)` and `(f)` stay half-width (Windows file-filter syntax / GDPR article notation).
- **Spacing:** a half-width space between a Chinese character and a Latin word, product name, URL or digit
  in prose (5 小時, Claude Code 記錄檔, 版本 {}), following Microsoft's zh-TW style guide. No space inside the
  compact time formats on the panel ({}天{}時, {}時{}分, 5小時) and none before % or a unit written as a
  Chinese character that is part of a compact value.
- **Time units:** 秒 / 分 / 小時 / 天. Compact panel formats use 時 for hours when it is combined with 天 or
  分 ({}天{}時, {}時{}分, {}時) – standard in Taiwanese UIs; alone it is 小時.
- **Case:** CJK has no case – the UPPERCASE panel labels are simply short labels; nothing is emphasised
  otherwise.
- **Taiwanese vocabulary only:** 登入 / 登出, 設定, 檔案, 資料, 視窗, 螢幕, 滑鼠, 程式, 網路, 預設, 訊息,
  使用者, 軟體, 重新整理, 工作列, 系統匣, 通知, 伺服器, 資料夾, 更新, 記錄檔, 程式碼, 佈景主題, 工作階段,
  開始功能表, 選單. Never 登錄, 設置, 文件 (for file), 數據, 屏幕, 鼠標, 網絡, 默認, 信息, 用戶, 軟件,
  刷新, 服務器, 代碼, 點擊, 保存, 項目 (OpenCC s2twp rewrites those – the checker rejects them).
- **Privacy document name: 隱私權政策.** This is the term Apple (Apple 隱私權政策), Google, Microsoft, LINE
  and the Taiwanese government (個人資料保護委員會 / NDC guidelines) all use; 隱私政策 is the mainland /
  Hong Kong form and 隱私權聲明 is rarer. The consent sentence works with it unchanged
  (我已閱讀並同意隱私權政策。).

## Fixed terms

| English | 繁體中文（台灣） | Note |
|---|---|---|
| 5-hour session | 5 小時工作階段 | panel short form: 5小時 |
| session (sign-in session) | 工作階段 / 登入 | "the session has expired" = 登入已過期 |
| weekly limit | 每週上限 | |
| per-model weekly limit | 各模型每週上限 | |
| limit (rate limit) | 上限 | "no limit" = 無上限 |
| reset (noun / verb) | 重設 | "reset {}" on the panel = 重設 {} |
| pace | 步調 | "{} vs pace" = 較步調 {} |
| burn rate | 消耗速率 | "avg daily burn" = 日均消耗 |
| usage | 使用量 | |
| usage credits | 使用額度 | pay-as-you-go = 隨用隨付 |
| usage data / usage file / usage log | 使用量資料 / 使用量檔案 / 使用量記錄檔 | |
| gauge | 儀表 | "{} gauge" = {} 儀表 |
| panel / floating panel | 面板 / 浮動面板 | |
| widget (help text) | 小工具 | the Windows term for a widget |
| tray / tray icon (Windows) | 系統匣 / 系統匣圖示 | Microsoft term |
| menu bar / menu bar icon (macOS) | 選單列 / 選單列圖示 | Apple term, STRINGS_MAC only |
| taskbar | 工作列 | |
| Start menu | 開始功能表 | Microsoft term |
| start with Windows / start at login | 隨 Windows 啟動 / 登入時開啟 | Apple's Dock wording is 登入時打開, but OpenCC rewrites 打開 → 開啟 |
| sign in / sign out | 登入 / 登出 | |
| notification | 通知 | |
| alert(s) | 警示 | settings tab |
| threshold | 門檻 | |
| warning / critical | 警告 / 嚴重 | threshold names (Microsoft severity term) |
| the monitor (= this app) | 本程式 | never 監視器 (reads as a display / CCTV) |
| end-of-week projection | 本週最終預估 | never 週末 (= weekend in Taiwan) |
| disclaimer (heading) | 免責條款 | 免責聲明 is rewritten by OpenCC to 免責宣告 |
| is available (new version) | 已推出 | not the calque 已可用 |
| backup | 備份 | |
| backup status bar | 備份狀態列 | |
| lamp | 燈號 | green / yellow / red lamp = 綠燈 / 黃燈 / 紅燈 |
| snapshot | 快照 | |
| vault (Obsidian) | 儲存庫 | the term Obsidian's own zh-TW UI uses |
| data source | 資料來源 | |
| local log | 本機記錄檔 | |
| local (this PC only) | 本機（僅此電腦） | |
| profile | 設定檔 | Microsoft term |
| account | 帳戶 | |
| plan / plan badge | 方案 / 方案標章 | |
| theme | 佈景主題 | Microsoft term (Windows "Themes") |
| layout | 版面配置 | |
| settings | 設定 | |
| default(s) | 預設 / 預設值 | |
| update (program update) | 更新 / 程式更新 | |
| install | 安裝 | |
| version | 版本 | |
| history | 歷史記錄 | |
| projection / forecast | 預估 | |
| peak | 峰值 | |
| trend curve (sparkline) | 趨勢曲線（走勢圖） | |
| data freshness / stale data | 資料新鮮度 / 資料過時 | |
| refresh | 重新整理 | |
| check now | 立即檢查 | |
| message to the developer | 傳訊息給開發者 | window title and menu item |
| rating / overall rating | 評分 / 整體評分 | |
| star | 星星 | "{} of 5" = {} / 5 |
| privacy notice / privacy policy | 隱私權政策 | see above |
| consent | 同意 | |
| controller / processor (GDPR) | 資料控管者 / 資料處理者 | Taiwanese legal translations of GDPR |
| GDPR | GDPR | unchanged (no official Taiwanese short name) |
| legitimate interest | 正當利益 | |
| supervisory authority | 監督機關 | |
| hosting provider | 主機代管服務商 | |
| hash | 雜湊值 | |
| IP address | IP 位址 | |
| e-mail | 電子郵件 | |
| optional | 選填 | form convention in Taiwan |
| click-through | 滑鼠穿透 | |
| always on top | 永遠置頂 | |
| lock position | 鎖定位置 | |
| snap to screen edge | 貼齊螢幕邊緣 | |
| opacity | 不透明度 | |
| accent color | 強調色 | |
| right-click / double-click / drag | 按右鍵 / 按兩下 / 拖曳 | Microsoft zh-TW terms |
| Ctrl + mouse wheel | Ctrl + 滑鼠滾輪 | |
| scheduled task | 排程工作 | Windows 工作排程器 |
| remote storage | 遠端儲存空間 | |
| quit / close / cancel / send | 結束 / 關閉 / 取消 / 傳送 | |
| what's new | 新功能 | |
| terms of use | 使用條款 | |
| source code | 原始碼 | |
| open source | 開放原始碼 | |
| telemetry | 遙測 | |
