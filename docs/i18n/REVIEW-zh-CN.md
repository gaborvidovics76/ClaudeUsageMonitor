# Review – 简体中文 (zh-CN) – Claude Usage Monitor

Checker: `python tools/check_i18n.py zh-CN` → `check_i18n: OK` (358 / 358 keys + 4 macOS keys, OpenCC
t2s unchanged). The 13 warnings are all Latin words that must stay: Cowork, Vidovics Gábor, IP,
`#privacy` in the URL, `api.log`, `update.log`, `dinorr.hu/claude-usage-monitor`,
`plan-usage-history.json`, token.

Form of address: 你 everywhere (including the privacy policy). Privacy document: 隐私政策.

## Texts I am least sure about

1. **`panel.five_hour_short` = `5小时`** (en `5H`, 2 chars). No readable Chinese short form fits in
   2 Latin widths; `5时` alone is not idiomatic. `5小时` is roughly the width of the Hungarian `5 ÓRA`.
   If it clips, `5h` (Latin, understood by every Chinese Claude user) is the fallback.
2. **`hist.stat_forecast` = `本周结束预测`** and the matching phrase in `help.guide`. The literal
   `周末预测` would be read as "weekend forecast" by every mainland reader, so I spelled out
   "end of this week". Slightly longer than the English stat label.
3. **`panel.pace` = `较进度 {}`** – the placeholder moved in front: in Chinese the comparison word
   must precede the value ("vs pace +5%" → "较进度 +5%"). Reads naturally only if the inserted value
   carries its own sign; if it is a bare number the English order `{} 较进度` would be wrong too.
4. **`set.backup_green` / `set.backup_yellow` = `绿色上限` / `黄色上限`** ("Green up to"). The label sits
   before a spin box that appends ` 小时`; "上限" (upper bound) is what reads best in that position,
   but it is not a word-for-word rendering.
5. **`backup.sec_components` = `备份了哪些内容`** vs **`backup.sec_contents` = `内容`**. Both English
   headings contain "contents"; I made the first one a question-style heading so the two sections stay
   distinct. A terser `备份项目` is possible if the heading row is narrow.
6. **`help.made_by` = `开发者`** and **`help.tab_author` = `作者`**. Two different words for the same
   person so that the "Made by" line does not simply repeat the tab title; 开发者 also matches
   `fb.title` 给开发者留言.
7. **`fb.consent` = `我已阅读并同意《{}》。`** – the book-title marks 《》 are placed outside the
   placeholder. If the UI renders `{}` as a styled link, the marks stay plain text around it, which is
   the normal look on Chinese sites; if the placeholder is ever replaced by something that is not a
   document title, the marks would look odd.
8. **`fb.privacy_text`** – legal register in 你 (not 您), following WeChat/Apple practice. GDPR article
   notation kept half-width as `第 6 条第 1 款 (f) 项`; "controller/processor" rendered with the terms
   used in Chinese GDPR literature (数据控制者 / 数据处理者). "The authority of your own country" is kept
   as 你所在国家/地区的监管机构 – no mainland GDPR authority is named. 2 years, NAIH, naih.hu, the
   URL and the date are all preserved; paragraph breaks identical to the English (6 × `\n\n`).
9. **`time.dh` / `time.hm` = `{}天{}时` / `{}时{}分`** – compact forms with 时 instead of 小时 to fit
   the panel; standard in Chinese clocks and countdowns, but `backup.age_h` alone uses the full
   `{}小时` because a lone `3时` is unidiomatic.
10. **`set.tray_max` = `取较高者`** ("Whichever is higher") – short option text for the tray-value
    radio group; `较高者` is slightly formal but unambiguous in a settings list.

## en / hu differences noticed

- `menu.help`: hu adds "(HELP)"; followed the English (`帮助…`).
- `menu.locked`: hu is a state ("Pozíció rögzítve" = position locked), en an action ("Lock position");
  followed the English (`锁定位置`), which works for a checkable menu item either way.
- `menu.panel_visible`: hu "Panel látszik" (state) vs en "Show panel" (action) – followed the English.
- `fb.privacy_text`: hu links to `/hu/#privacy`; kept the English URL `https://claudeusagemonitor.com/#privacy`
  (there is no zh-CN page).
- `set.show_extra_usage`: hu keeps "(usage credits)" in English; the English says "(pay-as-you-go)" –
  followed the English (`按量付费`).
- `backup.storage`: hu "{} / {} foglalt" vs en "{} used of {}" – rendered as `已用 {} / 共 {}` (same
  placeholder order as the English).

## Lektor

Independent native review (mainland zh-CN). Checker after the review: `check_i18n: OK` (358 / 358; the
same 13 Latin-word warnings, all legitimate). No Taiwanese terms or traditional characters found; 你
used consistently; full-width punctuation and “” quotes confirmed.

- backup.snap_kept: 保留 {} 个快照，共 {} → 已保留 {} 个快照，共 {} – state reads as completed
- backup.storage: 远程存储：已用 {}，共 {}，{} 可用 → 远程存储：已用 {}（共 {}），可用 {} – parallel, clearer structure
- backup.task_row: …· 下次 {} → …· 下次运行 {} – bare 下次 is incomplete
- backup.uploaded: {} 个新增，{} 个替换，{} 个错误 → 新增 {} 个，替换 {} 个，出错 {} 个 – natural Chinese count order
- err.no_tray: 已跳过托盘图标 → 将不显示托盘图标 – "skipped" was a calque
- fb.email: 电子邮件 → 邮箱 – standard mainland form label
- fb.err_email: 这个电子邮件地址看起来不正确 → 这个邮箱地址似乎不正确 – matches label, less calque
- fb.err_empty: 请先写下留言… → 请先填写留言… – standard form wording
- fb.sent_sub: 如果你留了电子邮件地址，我会回复到那里 → 如果你留了邮箱，我会通过邮件回复你 – "reply there" calque
- help.guide: 当服务器报告时 → 当服务器提供此数据时 – "report" calque
- help.guide: ——完整菜单 / ——<b>历史记录</b>窗口 → ——打开完整菜单 / ——打开<b>历史记录</b>窗口 – verb was missing
- help.guide: 本监视器…制作和测试备份是你自己的事 → 本程序…创建和测试备份由你自己负责 – 监视器 means hardware; tone
- help.guide: 服务器正在减慢请求 → 服务器正在限制请求频率 – matches err.rate_limited
- help.guide: 历史记录保留 7 天，重启和更新后仍然保留 → 历史记录保存 7 天，重启或更新后不会丢失 – repeated 保留 removed
- notify.first_run (+ STRINGS_MAC): …图标 = 菜单 → …图标即可打开菜单 – "= menu" unnatural in prose
- notify.logout: 已退出登录。已切换到本地数据源 → 已退出登录，并已切换到本地数据源 – smoother single sentence
- notify.stale_body: 上次读数已是 {} 前 → 上次读数是在 {}前 – fixes stray space, idiom
- notify.update: 程序版本 {} 已可用 → 新版本 {} 已发布 – 已可用 is a calque
- update.available: 版本 {} 已可用 → 新版本 {} 已发布 – same, consistent with notify
- panel.full_in: 用尽：{} → {}后用尽 – value is a duration
- set.backup_disclaimer: 不会制作…作为帮助提供的免费起点…请不时测试一次恢复 → 不会创建…免费提供的辅助起点…请定期测试恢复 – calques removed, meaning kept
- set.notify_enabled: 越过阈值时通知 → 超过阈值时通知 – usual Chinese verb
- set.rows_none: 没有…发送更多限额。一旦发送，它们会… → 没有…提供其他限额。一旦提供，会… – less literal
- set.show_local_models: 各模型之间的分布，来自本机 Claude Code 的日志 → 各模型用量分布（来自本机 Claude Code 日志） – checkbox-style, tighter
- set.taskbar: 在任务栏上显示 → 在任务栏中显示 – Microsoft zh-CN wording
- set.theme_default: 主题默认 → 跟随主题 – idiomatic button text
- set.tip: 右键 = 菜单，双击 = 历史记录 → 右键点击打开菜单，双击打开历史记录 – natural prose
- set.tray_max: 取较高者 → 取较高值 – values, less formal
- size.normal: 正常 → 标准 – standard size-option word
- update.manual: 它从源代码…运行）。请改为下载… → 它是从源代码…运行的）。请手动下载… – natural phrasing

Glossary updated: 邮箱 (form) / 电子邮件地址 (legal), 新版本 {} 已发布, size 标准, 跟随主题.

Still in doubt:
- `backup.age_m` / `time.m` = `{}分` – compact and fine next to `3时20分`, but alone ("5分") a mainland
  reader may pause; `{}分钟` is clearer if the status bar / panel has the room.
- `panel.pace` = `较进度 {}` – understandable, but if space allows `比进度快/慢 {}` would read better
  (needs a code change, since the sign is in the value).
- `fb.privacy_text` – kept as is (all facts, articles, 2 years, NAIH, URL, date verified); 访问/更正/删除…
  matches Chinese GDPR literature.
