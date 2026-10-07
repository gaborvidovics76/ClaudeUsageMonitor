# REVIEW – 繁體中文（台灣）(zh-TW) – Claude Usage Monitor

358 / 358 keys + 4 STRINGS_MAC keys. `check_i18n.py zh-TW` → `check_i18n: OK` (only expected warnings:
Latin words that are product / file names, the author's name, "IP", "token"). Form of address: 你.
Privacy document: 隱私權政策.

The texts I am least sure about (max. 10), and why:

1. **`panel.pace` – 「較步調 {}」** ("{} vs pace"). The English puts the value first; in Chinese the
   comparison word has to come first ("compared to pace: +12%"). 較步調 is compact (3 characters) but a
   little terse. A longer, friendlier alternative is 「與步調相比 {}」; if the panel has room, consider it.

2. **`panel.five_hour_short` – 「5小時」** ("5H"). Written without the usual space so it stays as short as
   possible; 「5時」 would be misread as five o'clock. Three characters are still wider than "5H" – if the
   compact layout clips, 「5h」 (Latin) would be the only shorter option, and Taiwanese users do read it.

3. **The OAuth "code" – 授權碼.** The sign-in dialog's "code" is the authorization code; 代碼 is rewritten
   by OpenCC s2twp to 程式碼 (source code), which would be wrong, so I used 授權碼 (authorization code)
   consistently (dlg.*, err.no_code). 驗證碼 (verification code) is the other common choice; 授權碼 is more
   precise for OAuth.

4. **`set.backup_disclaimer_h` – 「免責事項」** instead of the more usual 「免責聲明」. OpenCC s2twp rewrites
   聲明 → 宣告 (an OpenCC quirk, not Taiwanese usage), and the checker requires the text to survive the
   conversion unchanged. 免責事項 is also perfectly standard Taiwanese legal/UI wording, so nothing is lost.

5. **OpenCC-driven choices elsewhere:** 檢視 instead of 查看 (查看 → 檢視), 這部電腦 instead of 這台電腦
   (台 → 臺), 瞭解 instead of 了解, 連線 instead of 連接, 分佈 / 佔比 with the 人-radical forms. All of these
   are accepted Taiwanese forms (檢視 is Microsoft's term), but a native reviewer might prefer 查看 / 這台 in
   casual text. They cannot be used while the s2twp check is in place.

6. **`fb.privacy_text` – legal terms.** 資料控管者 / 資料處理者 (controller / processor), 正當利益 (legitimate
   interest), 監督機關 (supervisory authority), 剖析 (profiling) follow the Taiwanese translations of the
   GDPR commonly used by law firms and the NDC. GDPR itself is kept as "GDPR" (no official Taiwanese short
   name). The article is written 「GDPR 第 6 條第 1 項第 f 款」, the Taiwanese way of citing 6(1)(f). The
   URL is kept as in the English (`/#privacy`); the Hungarian points at `/hu/#privacy` – if a zh-TW page
   exists, change the URL in the module. The date is written 2026 年 10 月 6 日; switch back to ISO if it
   is compared by machine.

7. **`fb.privacy_hide` – 「隱藏隱私權政策」** ("Hide the notice"). Seven characters for a 15-character
   English link; 「隱藏說明」 would be shorter but ambiguous next to the Help window. If the link looks
   heavy, 「收合」 (collapse) is a common Taiwanese UI alternative.

8. **`set.backup_green` / `set.backup_yellow` – 「綠色至多」 / 「黃色至多」** ("Green up to" + spin box + " h").
   The label reads 「綠色至多 24 小時」 with the suffix, which is natural; on its own it is slightly elliptical.
   Alternative: 「綠色（不超過）」.

9. **`set.local_models_hint` – "token" kept in Latin.** Taiwanese AI users say "token"; the Chinese 詞元 is
   known but far less common in product UIs. The checker only warns. 權杖 is deliberately reserved for the
   OAuth token in `err.bad_token_resp` (Microsoft's term), so the two meanings never collide.

10. **`theme.claude` – 「Claude（暖色深色）」** ("warm dark"). 暖色 + 深色 next to each other is a bit
    stacked; 「Claude（暖調深色）」 is an alternative with the same meaning.

EN/HU differences noticed: the Hungarian privacy URL is `/hu/#privacy` (EN `/#privacy` – followed the
English). HU `menu.help` adds "(HELP)" – not reproduced. HU `set.notify_reset` adds "(reset)" in
parentheses – not needed in Chinese, 重設 is unambiguous. HU `fb.optional` = "not mandatory"; the Taiwanese
form convention is 選填.

## Lektor

Native zh-TW review, 2026-10-07. 40 edits in 35 STRINGS keys + 1 STRINGS_MAC key; `check_i18n.py zh-TW` → `check_i18n: OK` (only the earlier
Latin-word warnings remain).

- backup.age_h: {}時 → {}小時 – 「5時」 reads as five o'clock
- backup.checked_at: 已檢查：{} → 檢查時間：{} – natural label for a timestamp
- backup.cloud_only: 僅線上提供；為避免必須下載… → 為「僅限線上」檔案；為了不必下載… – OneDrive's own zh-TW term
- backup.disclaimer_short: 本監視器…不承擔任何責任 → 本程式…概不負責 – 監視器 means display/CCTV
- backup.legend: 綠色／黃色／紅色 → 綠燈／黃燈／紅燈 – they are lamps
- backup.tip_click: 按一下檢視詳細資料 → 按一下以檢視詳細資料 – Microsoft zh-TW pattern
- dlg.err_badcode: 授權碼未被接受 → 授權碼驗證失敗; 再次進行瀏覽器登入 → 重新在瀏覽器中登入 – passive calque removed
- dlg.err_ratelimit: 用新的授權碼重新進行一次瀏覽器登入 → 只在瀏覽器中重新登入一次，並使用新的授權碼 – keeps the "ONE" emphasis
- dlg.unknown_err: 未知的錯誤。 → 發生未知的錯誤。 – full sentence, standard wording
- err.already_running: 請檢視系統匣 → 請檢查系統匣 – 檢視 = view, wrong verb
- err.no_tray: 系統匣無法使用，將略過系統匣圖示 → 無法使用系統匣，因此不會顯示系統匣圖示 – 略過 is a calque of "skipped"
- fb.privacy_text: 訊息最長 2 年 → 訊息最長保留 2 年 – verb was missing
- fb.sent_sub: 每一則訊息我都會看…我會回覆到那裡 → 我都會親自閱讀…我會寄信回覆你 – "reply there" calque
- help.disclaimer: 獨立、免費的工具：並非… → 這是一款獨立的免費工具，並非… – full sentence, not a fragment
- help.guide: 倒數到重設為止 → 倒數計時到重設為止 – usual term
- help.guide: 週末預估會及時提醒你 → 本週最終預估會及早提醒你 – 週末 means weekend
- help.guide: 按兩下：<b>歷史記錄</b>視窗： → 按兩下：開啟<b>歷史記錄</b>視窗， – double colon, missing verb
- help.guide: 本監視器只讀取備份記錄檔 → 本程式只讀取備份記錄檔 – 監視器 means display/CCTV
- help.guide: 如果出了問題 → 發生問題時 – idiomatic help heading
- hist.stat_forecast: 週末預估 → 本週最終預估 – 週末 means weekend
- hist.stat_now: 本週目前 → 本週目前用量 – fragment, noun missing
- notify.first_run (+ STRINGS_MAC): 按右鍵 = 選單 → 按右鍵即可開啟選單 – "=" reads as English shorthand
- notify.login_ok: 伺服器資料即將送達 → 正在取得伺服器資料 – natural progress wording
- notify.stale_body: 上次讀取已是 {} 前 → 距上次讀取已過 {} – idiomatic
- notify.update: 已可用 → 已推出 – "is available" calque
- set.backup_disclaimer: 作為協助而提供的免費起點：任何人都可以修改這些指令碼 → 免費提供的入門範本，僅供協助：任何人都能修改其中的指令碼; 請不時測試一次還原 → 請不時實際測試一次還原 – calque removed, meaning kept
- set.backup_disclaimer_h: 免責事項 → 免責條款 – 免責事項 is Japanese usage
- set.backup_green / set.backup_yellow: 綠色至多 / 黃色至多 → 綠燈：最多 / 黃燈：最多 – reads naturally with the spin box
- set.danger: 危險 → 嚴重 – Microsoft term for "Critical"
- set.data_hint: 只測量這部電腦 → 只計算這部電腦的使用量 – "measures a PC" sounds odd
- set.local_models_hint: 其他模型則顯示…是你自身使用量與輸出 token 的佔比 → 至於其他模型，這裡顯示的是…這是在你自己的使用量與輸出 token 中所佔的比例 – clearer subject, smoother
- set.model_filter: 追蹤的模型 → 要追蹤的模型 – label for a choice
- set.show_local_models: 各模型之間的分佈，來自… → 各模型用量分佈（取自…） – shorter checkbox label
- set.show_reset: 重設倒數 → 重設倒數計時 – usual term
- set.theme_default: 佈景主題預設 → 佈景主題預設值 – 預設 alone is an adjective
- theme.claude: Claude（暖色深色） → Claude（暖色系深色） – stacked adjectives smoothed
- update.available: {} 版已可用。 → {} 版已推出。 – "is available" calque
- update.uptodate: 你已使用最新版本。 → 你使用的已是最新版本。 – idiomatic

Glossary updated: critical = 嚴重; the monitor = 本程式; end-of-week projection = 本週最終預估;
disclaimer = 免責條款; "is available" = 已推出; lamp colours = 綠燈 / 黃燈 / 紅燈; note on 登入時打開.

Still in doubt:
- STRINGS_MAC 「登入時開啟」: Apple's own Dock wording is 「登入時打開」, but OpenCC s2twp rewrites 打開 → 開啟,
  so the checker rejects it. 開啟 is fine; switch to 打開 only if the check ever allows it.
- panel.five_hour_short 「5小時」 is wider than "5H"; if the compact layout clips, use 「5h」.
- panel.pace 「較步調 {}」 is terse; acceptable on the panel, but 「與步調相比 {}」 is friendlier if there is room.
- panel.per_hour 「{}%/時」 vs set.show_burn 「%/小時」: kept on purpose (tight panel vs. explanatory label).
- set.backup_config 「備份指令碼設定檔」: 設定檔 is also the glossary term for "profile" (Microsoft); in context
  it is unambiguous, so kept.
