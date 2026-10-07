# Glossary – 简体中文 (zh-CN) – Claude Usage Monitor

## Tone and form of address

- **Form of address: 你** (never 您). This is how the best mainland consumer software talks to the user
  (WeChat, Apple's zh-CN UI, most Windows 11 strings). 你 is used everywhere, including the privacy
  policy – WeChat's own privacy policy is written with 你, so a legal text in 你 is familiar and not
  out of place. One form everywhere, as the brief asks.
- Short, confident, friendly. No calques from English, no "请您…" bureaucratic register. 请 is used
  only where a real request is made to the user (请重新登录, 请稍后再试).
- Punctuation: full-width ，。：；（）、 inside Chinese text; quotes “”; ellipsis … (one character);
  half-width digits and Latin product names. The English dash “–” inside a sentence becomes the
  Chinese dash ——, a full-width ；/， or is dropped; between two values in a label it stays “–”
  (上次运行：{} – {}). A half-width space between a digit / Latin word and a Chinese character in
  prose ("5 小时", "Claude Code 日志"), none inside compact time formats on the panel
  ("3时20分", "2天", "5小时").
- Half-width `(*.json)` and `(f)` stay half-width (file filter syntax, GDPR article notation).
- Time units: 秒 / 分 / 小时 / 天. Compact panel formats use 时 for hours when followed by 分 or
  preceded by 天 ("3时20分", "2天3时" – unambiguous and standard in Chinese UIs); alone it is 小时.
- Percent: digits + % with no space (70%, {}%/天).
- CJK has no case: the UPPERCASE panel labels are simply short labels.
- Mainland vocabulary throughout: 登录 / 退出登录, 设置, 文件, 数据, 窗口, 屏幕, 鼠标, 网络, 默认,
  用户, 刷新, 任务栏, 系统托盘, 通知, 服务器, 文件夹, 更新, 软件, 账户, 哈希值, 链接, 点击.

## Name of the privacy document: 隐私政策

`fb.privacy_title` = **隐私政策**. This is the term every major mainland platform uses for the document
a user "reads and accepts" (Apple, Tencent/WeChat, Alibaba, ByteDance, Xiaomi: 《隐私政策》), the
term the PIPL-era regulators (CAC) use in their app-compliance rules, and the term Apple's App Store
uses for the "Privacy Policy" link. Microsoft's own documents are called 隐私声明 (Privacy Statement),
but that word is Microsoft-specific and not what the user expects in a consent checkbox. The consent
sentence wraps it in 《》, the standard way to cite a document title: 我已阅读并同意《隐私政策》。
`help.privacy` uses the same word. The complaint sentence keeps "the authority of your own country"
(你所在国家/地区的监管机构): China has no GDPR supervisory authority, so none is named.

## Fixed terms (one translation each)

| English | 简体中文 | Note |
|---|---|---|
| 5-hour session | 5 小时会话 | panel: 5 小时会话; short: 5小时 |
| weekly limit | 每周限额 | panel: 每周限额; short: 本周 |
| per-model weekly limit | 模型每周限额 | |
| limit | 限额 | never 限制 for the quota itself; "no limit" = 无限额 |
| reset (noun / verb) | 重置 | |
| countdown to reset | 重置倒计时 | |
| pace | 进度 | panel: 较进度 {} |
| burn rate | 消耗速率 | |
| usage | 用量 | usage data / file / log = 用量数据 / 用量文件 / 用量日志 |
| usage credits | 用量额度 | |
| pay-as-you-go | 按量付费 | |
| plan | 套餐 | |
| plan badge | 套餐徽章 | |
| gauge | 仪表 | |
| panel | 面板 | |
| floating panel | 悬浮面板 | |
| widget (help text) | 小组件 | |
| tray / system tray | 系统托盘 | Microsoft zh-CN |
| tray icon | 托盘图标 | |
| taskbar | 任务栏 | |
| Start menu | “开始”菜单 | Microsoft zh-CN style |
| menu bar (macOS) | 菜单栏 | Apple zh-CN |
| start at login (macOS) | 登录时打开 | Apple zh-CN "登录项" wording |
| start with Windows | 随 Windows 启动 | |
| sign in | 登录 | |
| sign out | 退出登录 | |
| session (sign-in) | 会话 | 会话已过期 |
| notification | 通知 | |
| alert(s) (tab, help heading) | 提醒 | |
| threshold | 阈值 | |
| warning / critical (levels) | 警告 / 严重 | |
| backup | 备份 | |
| backup status bar | 备份状态栏 | |
| lamp | 指示灯 | |
| snapshot | 快照 | |
| vault (Obsidian) | 仓库 | Obsidian's official zh-CN word |
| scheduled task | 计划任务 | Windows 任务计划程序 |
| data source | 数据源 | |
| measurement source (settings label) | 测量来源 | |
| local log | 本地日志 | |
| this PC | 本机 | |
| all devices | 所有设备 | |
| profile | 配置文件 | |
| account | 账户 | |
| theme | 主题 | |
| accent color | 强调色 | not 主题色, to keep it apart from "theme" |
| layout | 布局 | |
| opacity | 不透明度 | |
| always on top | 始终置顶 | |
| lock position | 锁定位置 | |
| click-through | 鼠标穿透 | |
| snap to screen edge | 吸附到屏幕边缘 | |
| settings | 设置 | |
| default(s) | 默认 / 默认设置 | |
| update (program) | 更新 / 程序更新 | |
| install | 安装 | |
| version | 版本 | |
| what's new | 更新内容 | |
| history | 历史记录 | |
| projection / forecast | 预测 | end-of-week projection = 本周结束预测 (not 周末, which means weekend) |
| daily average | 日均 | |
| peak | 峰值 | |
| trend curve (sparkline) | 趋势曲线（迷你图） | Excel zh-CN: 迷你图 |
| data freshness | 数据时效 | |
| stale data | 数据过旧 | |
| refresh | 刷新 | |
| retry | 重试 | |
| folder | 文件夹 | |
| message to the developer | 给开发者留言 | the form field "Message" = 留言 |
| e-mail (form field) / e-mail address | 邮箱 / 邮箱地址 | legal text keeps 电子邮件地址 |
| new version available | 新版本 {} 已发布 | not the calque 已可用 |
| size: Normal | 标准 | 小 / 标准 / 大 / 特大 |
| theme default (accent) | 跟随主题 | |
| author | 作者 | |
| rating | 评分 | |
| privacy notice / policy | 隐私政策 | |
| consent | 同意 | "accept" in the checkbox = 同意 |
| controller / processor | 数据控制者 / 数据处理者 | GDPR terms in Chinese legal usage |
| legitimate interest | 正当利益 | |
| profiling | 用户画像 | |
| supervisory authority | 监管机构 | |
| hash | 哈希值 | |
| token (OAuth) | 令牌 | API token endpoint |
| token (LLM) | token | kept, as in Chinese AI products |
| passkey | 通行密钥 | Apple / Google zh-CN |
| connected apps | 已连接的应用 | |
| per-surface limits | 各渠道限额 | |
| rate-limit tier | 速率限制等级 | |
| terms of use | 使用条款 | |
| disclaimer | 免责声明 | |
| open source / telemetry | 开源 / 遥测 | |
| post-it (layout / theme) | 便利贴 | |
