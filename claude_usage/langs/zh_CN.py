# -*- coding: utf-8 -*-
"""简体中文 – UI strings of Claude Usage Monitor."""

CODE = "zh-CN"
NAME = "简体中文"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{}天",
    "backup.age_h": "{}小时",
    "backup.age_m": "{}分",
    "backup.and_more": "…还有 {} 个",
    "backup.checked_at": "上次检查：{}",
    "backup.checking": "正在检查…",
    "backup.cloud_only": "该快照在 OneDrive 中为“仅联机”文件；为避免触发下载，不列出其内容。",
    "backup.comp.cowork": "Cowork 聊天记录（每个会话一个 ZIP）",
    "backup.comp.vault": "Obsidian 仓库快照（ZIP）",
    "backup.disclaimer_short": "本程序只显示备份日志中记录的内容。我们不对备份承担任何责任；备份是否完整、能否恢复，需要你自行检查。",
    "backup.done": "完成",
    "backup.dry_run": "（测试运行，未上传任何内容）",
    "backup.failed": "失败",
    "backup.files_size": "{} 个文件，{}",
    "backup.folders": "文件夹",
    "backup.label_age": "名称和时间",
    "backup.label_name": "仅名称",
    "backup.label_none": "仅指示灯",
    "backup.last_ok": "上次成功备份：{}（{}前）",
    "backup.last_run": "上次运行：{} – {}",
    "backup.legend": "绿色：不超过 {} 小时 · 黄色：不超过 {} 小时 · 红色：更早，或没有备份",
    "backup.level_green": "最新",
    "backup.level_none": "未找到备份",
    "backup.level_red": "过旧",
    "backup.level_yellow": "较旧",
    "backup.log_file": "日志文件",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "未找到备份文件夹：{}",
    "backup.none_found": "无。",
    "backup.open": "打开",
    "backup.rc_copied": "已复制新增或更改的文件",
    "backup.rc_failed": "失败（代码 {}）",
    "backup.rc_nochange": "已是最新，无需复制",
    "backup.recent_notes": "快照中最近编辑的笔记",
    "backup.refresh": "立即检查",
    "backup.sec_components": "备份了哪些内容",
    "backup.sec_contents": "内容",
    "backup.sec_log": "日志（最后几行）",
    "backup.sec_problems": "错误和警告",
    "backup.sec_tasks": "计划任务",
    "backup.skipped": "已跳过（未找到文件夹）",
    "backup.snap_kept": "已保留 {} 个快照，共 {}",
    "backup.snapshot": "最新快照",
    "backup.source": "来源",
    "backup.state_error": "已完成，但有错误",
    "backup.state_interrupted": "未完成",
    "backup.state_ok": "已成功完成",
    "backup.state_running": "正在运行",
    "backup.storage": "远程存储：已用 {}（共 {}），可用 {}",
    "backup.target": "目标",
    "backup.task_event": "事件触发",
    "backup.task_row": "上次运行 {} · 结果 {} · 下次运行 {}",
    "backup.tip_click": "点击查看详情",
    "backup.title": "备份",
    "backup.tray": "备份：{}",
    "backup.uploaded": "本次运行已上传：新增 {} 个，替换 {} 个，出错 {} 个",
    "backup.uploaded_files": "已上传的文件",
    "backup.uploaded_groups": "已上传的文件（按文件夹）",
    "backup.uploaded_no": "上传到 Nextcloud：尚未",
    "backup.uploaded_yes": "上传到 Nextcloud：是（{}）",
    "backup.vault": "仓库",
    "backup.vault_changed": "自此快照以来，仓库中有 {} 条笔记已更改",
    "backup.zip_new": "{} 个新增/更新的 ZIP",
    "backup.zip_summary": "{} 个文件（{} 条笔记），解压后 {}",
    # --- details ---------------------------------------------------------------------------
    "detail.extra": "用量额度",
    "detail.local_header": "CLAUDE CODE · 本机 · 本周分布",
    "detail.off": "关",
    "detail.on": "开",
    "detail.surface.oauth_apps": "已连接的应用",
    "detail.unlimited": "无限额",
    # --- sign-in dialog --------------------------------------------------------------------
    "dlg.cancel": "取消",
    "dlg.checking": "正在检查…",
    "dlg.err_badcode": "代码未被接受。\n\n{}\n\n请检查是否粘贴了完整的代码，或重新在浏览器中登录（每次都会生成新代码）。",
    "dlg.err_ratelimit": "短时间内登录尝试次数过多。\n\n服务器已暂时限制你的请求。请关闭此窗口，等待 10–15 分钟（期间不要再尝试），然后只发起一次新的浏览器登录，并使用新代码。",
    "dlg.hint1": "在打开的页面中登录并授权访问。完成后你会获得一个代码。",
    "dlg.intro": "在你自己的浏览器中登录 claude.ai 账户（已保存的密码和通行密钥可直接使用）。",
    "dlg.login_title": "登录",
    "dlg.open_browser": "在浏览器中打开登录页面",
    "dlg.paste_label": "把收到的代码粘贴到这里：",
    "dlg.paste_placeholder": "在此粘贴代码",
    "dlg.signin": "登录",
    "dlg.step1": "第 1 步",
    "dlg.step2": "第 2 步",
    "dlg.unknown_err": "未知错误。",
    # --- errors ----------------------------------------------------------------------------
    "err.already_running": "程序已在运行（请查看系统托盘）。",
    "err.bad_token_resp": "令牌端点返回了无效响应",
    "err.bad_usage_resp": "用量端点返回了无效响应",
    "err.connection": "连接错误：{}",
    "err.file_empty": "用量文件为空。",
    "err.file_not_found": "未找到用量文件。\nClaude Desktop 正在运行吗？",
    "err.file_unreadable": "用量文件当前无法读取。",
    "err.loading": "正在登录 / 查询…",
    "err.network": "网络错误：{}",
    "err.no_code": "未粘贴代码。",
    "err.no_data_profile": "此配置文件没有数据。",
    "err.no_tray": "系统托盘不可用，将不显示托盘图标。",
    "err.no_usage_data": "没有用量数据。",
    "err.not_signed_in": "未登录。",
    "err.query_http": "查询错误（HTTP {}）。",
    "err.rate_limited": "服务器正在限制请求频率（429），将自动重试。",
    "err.session_expired": "会话已过期，请重新登录。",
    "err.session_expired_nl": "会话已过期。\n请重新登录。",
    "err.signin_needed": "claude.ai 登录已过期。\n请重新登录：右键 → 登录 claude.ai",
    "err.unexpected": "意外错误：{}",
    # --- "Message to the developer" window -------------------------------------------------
    "fb.cancel": "取消",
    "fb.close": "关闭",
    "fb.consent": "我已阅读并同意《{}》。",
    "fb.email": "邮箱",
    "fb.email_hint": "仅在希望收到回复时填写",
    "fb.err_consent": "发送前请先同意《隐私政策》。",
    "fb.err_email": "这个邮箱地址似乎不正确。",
    "fb.err_empty": "请先填写留言或选择评分。",
    "fb.err_links": "留言中的链接太多。",
    "fb.err_network": "无法连接到 claudeusagemonitor.com。请检查网络连接后重试。",
    "fb.err_rate": "短时间内发送的留言太多，请稍后再试。",
    "fb.err_server": "服务器暂时无法接收留言。请稍后再试。",
    "fb.intro": "有想法、发现了问题，或者只是喜欢这个程序？告诉我吧。每一条留言都由我——作者 Vidovics Gábor——亲自阅读。",
    "fb.message": "留言",
    "fb.message_ph": "哪些好用，哪些不好用，还缺什么？",
    "fb.meta": "随留言一同发送：程序版本 {0}、操作系统（{1}）、界面语言（{2}）。",
    "fb.name": "姓名",
    "fb.optional": "（可选）",
    "fb.privacy_hide": "收起隐私政策",
    "fb.privacy_text": (
        "数据控制者：Vidovics Gábor，自然人（匈牙利），Claude Usage Monitor 的作者。"
        "完整的隐私政策见官方网站：https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "发送的内容：你在此填写的信息——姓名（可选）、电子邮件地址（可选）、留言、星级评分——"
        "以及用于帮助我了解上下文的信息：程序版本、操作系统名称和版本、界面语言和发送时间。"
        "服务器不存储 IP 地址；为防止滥用，仅使用一个每日更换、且无法还原为地址的哈希值。"
        "\n\n"
        "目的：阅读并回复你的留言，以及改进程序（正当利益，GDPR 第 6 条第 1 款 (f) 项；回复本身基于你的请求）。"
        "只有当你另外勾选相应的选项（同意，第 6 条第 1 款 (a) 项），并经作者审核后，你的评分和姓名才会显示在网站上；"
        "你可以随时撤回该同意。"
        "\n\n"
        "保存期限：留言最多保存 2 年；已发布的评分保存至你撤回同意为止。"
        "如果作者开启了电子邮件转发，副本也会发送到作者的邮箱。"
        "\n\n"
        "谁能看到：仅数据控制者，以及作为数据处理者的托管服务提供商（服务器位于欧盟境内的德国）。"
        "不会出售或转交任何信息；不进行用户画像，也不进行自动化决策。"
        "\n\n"
        "你的权利：访问、更正、删除、限制处理、反对、撤回同意，以及向监管机构投诉"
        "（在匈牙利：NAIH，naih.hu）或向你所在国家/地区的监管机构投诉。联系方式：本表单或官方网站。"
        "\n\n"
        "传输：通过加密连接（HTTPS/TLS）发送至 claudeusagemonitor.com。本政策版本：2026-10-06。"
    ),
    "fb.privacy_title": "隐私政策",
    "fb.publish": "我的评分和姓名（如已填写）可以显示在 claudeusagemonitor.com 上。",
    "fb.rating": "总体评分",
    "fb.rating_clear": "清除",
    "fb.rating_hint": "可选，点击一颗星即可",
    "fb.rating_tip": "{} / 5",
    "fb.secure": "与 claudeusagemonitor.com 之间使用加密连接（HTTPS）。",
    "fb.send": "发送",
    "fb.sending": "正在发送…",
    "fb.sent": "谢谢，已收到！",
    "fb.sent_sub": "每一条留言我都会读。如果你留了邮箱，我会通过邮件回复你。",
    "fb.title": "给开发者留言",
    # --- Help window -----------------------------------------------------------------------
    "help.disclaimer": "这是一款独立的免费工具，并非由 Anthropic 开发，也与其没有任何关联。“Claude”是 Anthropic 的商标。",
    "help.feedback": "问题、想法、错误报告：请使用网站上的留言表单。",
    "help.free": "永久免费 · MIT 许可证 · 开源 · 无遥测",
    "help.guide": (
        "\n"
        "<h2>小组件显示什么</h2>\n"
        "<ul>\n"
        "<li><b>5 小时会话</b>——当前会话限额已用去多少。每五小时重置一次；小组件会倒计时到重置时刻。</li>\n"
        "<li><b>每周限额</b>——所有模型的总用量；在你账户固定的每周时间点重置。</li>\n"
        "<li><b>模型每周限额</b>——当服务器提供此数据时显示的第三个仪表（例如针对某个特定模型）。</li>\n"
        "<li><b>进度和消耗速率</b>——限额消耗得有多快、能否撑到重置；本周结束时的预测会提前提醒你。</li>\n"
        "<li><b>用量额度</b>和套餐徽章——在<i>套餐徽章和额外限额</i>中开启后显示。</li>\n"
        "</ul>\n"
        "<h2>数据来自哪里</h2>\n"
        "<ul>\n"
        "<li><b>claude.ai（所有设备）</b>——向 Anthropic 的服务器查询，因此手机、浏览器和其他电脑上的用量也包括在内。"
        "需要在你自己的浏览器中登录一次（菜单：<i>登录</i>）。每 2 分钟刷新一次；如果服务器要求，则会放慢。</li>\n"
        "<li><b>本地（仅本机）</b>——读取这台电脑上 Claude Desktop 的用量日志。无需登录，但只知道本机的情况。</li>\n"
        "</ul>\n"
        "<p>在菜单中切换：<i>数据源</i>。</p>\n"
        "<h2>使用小组件</h2>\n"
        "<ul>\n"
        "<li><b>右键点击</b>小组件（或托盘图标）——打开完整菜单。</li>\n"
        "<li><b>双击</b>某个仪表——打开<b>历史记录</b>窗口：6 小时、24 小时、7 天或全部，含峰值、日均和预测。</li>\n"
        "<li><b>拖动</b>可移动位置，会自动吸附到屏幕边缘。<b>Ctrl + 鼠标滚轮</b>——放大或缩小。</li>\n"
        "<li>布局：便利贴卡片、细条、圆环；6 种主题。<i>锁定位置</i>和<i>鼠标穿透</i>在“设置”中。</li>\n"
        "</ul>\n"
        "<h2>提醒</h2>\n"
        "<p>70% 起显示黄色，90% 起显示红色（可调整）。可选择在限额重置和数据过旧时接收通知。</p>\n"
        "<h2>备份（可选）</h2>\n"
        "<p>小指示灯显示你的计划备份任务是否已运行并完成。点击指示灯查看详情。"
        "本程序只读取备份日志——创建和测试备份由你自己负责（见使用条款）。</p>\n"
        "<h2>更新</h2>\n"
        "<p>程序会自动检查新版本，一键即可更新。每个安装包都经过 SHA-256 校验，且只来自 <b>claudeusagemonitor.com</b>。"
        "新版本和更新说明：{site}</p>\n"
        "<h2>隐私</h2>\n"
        "<p>无遥测，无跟踪。claude.ai 登录信息经加密后仅保存在这台电脑上；不会发送到其他任何地方。</p>\n"
        "<h2>出了问题怎么办</h2>\n"
        "<ul>\n"
        "<li><i>429 / 已限流</i>——服务器正在限制请求频率；程序会自动重试。</li>\n"
        "<li>没有数据——检查<i>数据源</i>；使用 claude.ai 时，请重新登录。</li>\n"
        "<li>历史记录保存 7 天，重启或更新后不会丢失。</li>\n"
        "<li>日志和设置：<code>{cfg}</code>（<code>api.log</code>、<code>update.log</code>）。</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "开发者",
    "help.moved": "自 2026 年 9 月 21 日起启用新地址——原 dinorr.hu/claude-usage-monitor 页面会重定向到这里。",
    "help.official": "官方网站",
    "help.open_site": "打开 claudeusagemonitor.com",
    "help.privacy": "隐私政策",
    "help.site_what": "下载、自动更新、更新内容、Claude Backup Kit、使用条款和隐私政策——全都在一个地方。",
    "help.source_code": "源代码（GitHub）",
    "help.tab_author": "作者",
    "help.tab_guide": "使用说明",
    "help.terms": "使用条款",
    "help.title": "帮助",
    "help.version": "版本",
    # --- History window --------------------------------------------------------------------
    "hist.legend_5h": "5 小时会话",
    "hist.legend_week": "每周限额",
    "hist.no_data": "此时段的数据不足。",
    "hist.range_24h": "24 小时",
    "hist.range_6h": "6 小时",
    "hist.range_7d": "7 天",
    "hist.range_all": "全部",
    "hist.stat_burn": "日均消耗",
    "hist.stat_forecast": "本周结束预测",
    "hist.stat_now": "当前每周用量",
    "hist.stat_peak": "每周峰值",
    "hist.stat_sessions": "5 小时会话数",
    "hist.title": "历史记录",
    # --- layouts ---------------------------------------------------------------------------
    "layout.compact": "细条",
    "layout.postit": "便利贴卡片",
    "layout.ring": "圆环",
    # --- context menu ----------------------------------------------------------------------
    "menu.always_top": "始终置顶",
    "menu.autostart": "随 Windows 启动",
    "menu.backup_bar": "备份状态栏",
    "menu.backups": "备份…",
    "menu.check_update": "检查程序更新…",
    "menu.click_through": "鼠标穿透",
    "menu.details": "套餐徽章和额外限额",
    "menu.feedback": "给开发者留言…",
    "menu.help": "帮助…",
    "menu.history": "历史记录和统计…",
    "menu.language": "语言",
    "menu.layout": "布局",
    "menu.locked": "锁定位置",
    "menu.login": "登录（claude.ai，浏览器）…",
    "menu.logout": "退出登录",
    "menu.model_gauge": "{} 仪表",
    "menu.order": "顺序",
    "menu.panel_visible": "显示面板",
    "menu.quit": "退出",
    "menu.refresh": "立即刷新用量数据",
    "menu.settings": "设置…",
    "menu.size": "大小",
    "menu.source": "数据源",
    "menu.start_menu": "在“开始”菜单中显示",
    "menu.theme": "主题",
    "menu.update_available": "程序更新：安装版本 {}…",
    # --- desktop notifications -------------------------------------------------------------
    "notify.autostart_fail": "无法设置自动启动。",
    "notify.autostart_off": "已关闭：程序不会随 Windows 启动。",
    "notify.autostart_on": "已开启：程序会随 Windows 启动。",
    "notify.first_run": "面板已显示在屏幕右上角。\n右键点击面板或托盘图标即可打开菜单。",
    "notify.login_ok": "登录成功，正在获取服务器数据。",
    "notify.logout": "已退出登录，并已切换到本地数据源。",
    "notify.reset_done": "{}：已重置，新的周期开始了。",
    "notify.signin_needed": "claude.ai 登录已过期。右键点击面板并重新登录，即可继续查看所有设备的用量。",
    "notify.stale_body": "上次读数是在 {}前。Claude Desktop 正在运行吗？",
    "notify.stale_title": "数据过旧",
    "notify.threshold": "{}：已用 {}%。",
    "notify.update": "新版本 {} 已发布。右键点击面板 → 程序更新。",
    # --- panel labels (tight space) --------------------------------------------------------
    "panel.five_hour": "5 小时会话",
    "panel.five_hour_short": "5小时",
    "panel.full_in": "{}后用尽",
    "panel.model": "{} 每周",
    "panel.no_data": "无数据",
    "panel.pace": "较进度 {}",
    "panel.per_day": "{}%/天",
    "panel.per_hour": "{}%/时",
    "panel.refreshing": "正在获取数据",
    "panel.reset": "重置 {}",
    "panel.retry_in": "{} 秒后重试",
    "panel.updated": "更新于 {}",
    "panel.week_short": "本周",
    "panel.weekly": "每周限额",
    # --- profile ---------------------------------------------------------------------------
    "profile.extra": "用量额度：{}",
    "profile.plan": "套餐：{}",
    "profile.since": "加入时间：{}",
    "profile.tier": "速率限制等级：{}",
    # --- Settings window -------------------------------------------------------------------
    "set.about": "{}\n无遥测。仅向 Anthropic 查询你自己的用量，并从更新服务器读取版本号。",
    "set.accent": "强调色",
    "set.always_top": "置于所有窗口之上",
    "set.auto": "自动",
    "set.backup_config": "备份脚本配置",
    "set.backup_details": "详情窗口显示",
    "set.backup_disclaimer": "Claude Usage Monitor 只读取并显示你的备份日志——它不会创建、检查或保证任何备份。Claude Backup Kit 是免费提供的辅助起点：任何人都可以修改其中的脚本，因此无法保证备份的质量和完整性。我们对备份、数据丢失或任何损失不承担任何责任。确保备份完整且可以恢复，是每个人自己的责任——请定期测试恢复。",
    "set.backup_disclaimer_h": "免责声明",
    "set.backup_enabled": "在面板上显示备份状态栏",
    "set.backup_found": "已找到：{}",
    "set.backup_green": "绿色上限",
    "set.backup_label": "指示灯旁的标签",
    "set.backup_lamps": "指示灯",
    "set.backup_root": "备份文件夹",
    "set.backup_tasks": "计划任务筛选",
    "set.backup_unconfigured": "尚未设置备份文件夹，因此状态栏保持隐藏。请选择备份脚本写入的文件夹。",
    "set.backup_yellow": "黄色上限",
    "set.browse": "浏览…",
    "set.click_through": "鼠标穿透（仅作装饰，不响应鼠标）",
    "set.close": "关闭",
    "set.color_hint": "颜色随阈值变化：绿色 → 黄色 → 红色。",
    "set.danger": "严重",
    "set.data_hint": "本地日志：Claude Desktop 的 plan-usage-history.json。无需登录，但只统计本机，且大约每 5 分钟刷新一次。\n\nclaude.ai：登录后向服务器查询。可以看到所有设备的用量、精确的重置时间，刷新也更频繁。",
    "set.datafile": "数据文件",
    "set.default": "默认",
    "set.details_api_only": "这些数据来自 claude.ai 数据源（需要登录）；本地日志中没有。",
    "set.file_filter": "JSON (*.json);;所有文件 (*.*)",
    "set.gauge_order": "仪表顺序",
    "set.hours_suffix": " 小时",
    "set.layout": "布局",
    "set.local_models_hint": "服务器只为部分模型（例如 Fable）单独计数。对于其他模型，这里显示的是本周本机上 Claude Code 工作的分布——占你自身用量的比例和输出 token 数，而不是占某个限额的比例。只读取模型名称和 token 数量，绝不读取对话内容。",
    "set.local_models_none": "未找到 Claude Code 日志文件夹——此组会直接隐藏。其他功能不受影响。",
    "set.local_models_path": "Claude Code 日志文件夹",
    "set.lock": "锁定位置（不可拖动）",
    "set.login_btn_in": "退出 claude.ai 登录",
    "set.login_btn_out": "登录 claude.ai…",
    "set.model_filter": "要跟踪的模型",
    "set.model_scale": "模型仪表大小",
    "set.not_set": "未设置",
    "set.notify_enabled": "超过阈值时通知",
    "set.notify_reset": "限额重置时通知",
    "set.notify_stale": "数据过旧时通知",
    "set.opacity": "不透明度",
    "set.open_config": "打开设置文件夹",
    "set.pick_color": "选择颜色…",
    "set.pick_file_title": "选择用量日志",
    "set.profile": "配置文件 / 账户",
    "set.profile_auto": "自动（最近使用）",
    "set.profile_n": "配置文件 {} – …{}",
    "set.refresh": "刷新",
    "set.reset_confirm": "确定要恢复默认设置吗？",
    "set.restore": "恢复默认设置",
    "set.rows_available": "当前可显示的项目——取消勾选你不想看到的：",
    "set.rows_none": "服务器目前没有为你的账户提供其他限额。一旦提供，会自动显示在这里。",
    "set.sec_suffix": " 秒",
    "set.show_age": "数据时效",
    "set.show_burn": "消耗速率（%/小时、%/天）",
    "set.show_extra_usage": "用量额度（按量付费）",
    "set.show_feedback_icon": "面板标题栏中的留言图标",
    "set.show_five_hour": "显示 5 小时会话",
    "set.show_local_models": "各模型用量分布（来自本机 Claude Code 日志）",
    "set.show_model": "显示模型每周限额（claude.ai 数据源）",
    "set.show_model_list": "其他模型的每周限额",
    "set.show_plan_badge": "标题栏中的套餐徽章（Pro / Max…）",
    "set.show_plan_name": "在徽章上显示我的名字",
    "set.show_reset": "重置倒计时",
    "set.show_spark": "趋势曲线（迷你图）",
    "set.show_surfaces": "各渠道限额（Claude Code、已连接的应用…）",
    "set.show_weekly": "显示每周限额",
    "set.size": "大小",
    "set.snap": "吸附到屏幕边缘",
    "set.source_api": "claude.ai – 所有设备（需要登录）",
    "set.source_label": "测量来源",
    "set.source_local": "本地日志 – 仅本机",
    "set.tab_alerts": "提醒",
    "set.tab_appearance": "外观",
    "set.tab_content": "内容",
    "set.tab_data": "数据源",
    "set.tab_details": "详情",
    "set.tab_system": "系统",
    "set.taskbar": "在任务栏中显示（作为窗口）",
    "set.theme": "主题",
    "set.theme_default": "跟随主题",
    "set.tip": "提示：按住左键拖动面板，Ctrl + 滚轮调整大小，\n右键点击打开菜单，双击打开历史记录。",
    "set.title": "设置",
    "set.tray_five": "5 小时会话",
    "set.tray_max": "取较高值",
    "set.tray_value": "托盘图标数值",
    "set.tray_weekly": "每周限额",
    "set.update_check": "自动检查程序更新",
    "set.version": "版本",
    "set.visible": "显示悬浮面板",
    "set.warn": "警告",
    # --- sizes -----------------------------------------------------------------------------
    "size.extra": "特大",
    "size.large": "大",
    "size.normal": "标准",
    "size.small": "小",
    # --- data sources ----------------------------------------------------------------------
    "source.api": "claude.ai（所有设备）",
    "source.local": "本地（仅本机）",
    # --- themes ----------------------------------------------------------------------------
    "theme.claude": "Claude（暖色深色）",
    "theme.graphite": "石墨",
    "theme.midnight": "午夜玻璃",
    "theme.neon": "霓虹",
    "theme.paper": "浅色纸张",
    "theme.postit": "便利贴黄",
    # --- time units ------------------------------------------------------------------------
    "time.day": "{}天",
    "time.dh": "{}天{}时",
    "time.hm": "{}时{}分",
    "time.hour": "{}小时",
    "time.m": "{}分",
    "time.min": "{}分钟",
    "time.none": "无数据",
    "time.sec": "{}秒",
    # --- tray ------------------------------------------------------------------------------
    "tray.head": "5 小时：{}%   ·   本周：{}%",
    "tray.line": "{}：{}%",
    # --- updater ---------------------------------------------------------------------------
    "update.available": "新版本 {} 已发布。",
    "update.check_failed": "无法检查更新：{}",
    "update.check_now": "立即检查",
    "update.checking": "正在检查更新…",
    "update.downloading": "正在下载… {} / {}",
    "update.failed": "更新失败：{}",
    "update.install": "立即安装",
    "update.installed": "已安装版本：{}",
    "update.later": "稍后",
    "update.manual": "此副本无法自行更新（它是从源代码或只读文件夹运行的）。请手动下载新的安装包。",
    "update.open_page": "打开下载页面",
    "update.restarting": "正在安装，程序稍后会自动重启。",
    "update.skip": "跳过此版本",
    "update.title": "程序更新",
    "update.uptodate": "你使用的已是最新版本。",
    "update.verifying": "正在校验并解压…",
    "update.whats_new": "更新内容",
}

# macOS wording: Apple zh-CN terms – 登录时打开 (login items), 菜单栏 (menu bar)
STRINGS_MAC = {
    "menu.autostart": "登录时打开",
    "notify.autostart_on": "已开启：程序会在你登录时打开。",
    "notify.autostart_off": "已关闭：程序不会在登录时打开。",
    "notify.first_run": "面板已显示在屏幕右上角。\n右键点击面板或菜单栏图标即可打开菜单。",
}
