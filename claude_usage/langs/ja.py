# -*- coding: utf-8 -*-
"""日本語 – UI strings of Claude Usage Monitor.

Polite です・ます form for sentences, 体言止め (noun form) for labels and menu items.
Microsoft terminology for Windows (サインイン, 通知領域, タスクバー, 既定), Apple's for the
four STRINGS_MAC texts (メニューバー, ログイン時に開く). See docs/i18n/glossary-ja.md.
"""

CODE = "ja"
NAME = "日本語"

STRINGS = {
    # --- backup status bar / details window ----------------------------------------------
    "backup.age_d": "{}日",
    "backup.age_h": "{}時間",
    "backup.age_m": "{}分",
    "backup.and_more": "…ほか{}件",
    "backup.checked_at": "確認: {}",
    "backup.checking": "確認中…",
    "backup.cloud_only": "このスナップショットは OneDrive のオンライン専用ファイルです。ダウンロードせずに済むよう、内容の一覧は表示しません。",
    "backup.comp.cowork": "Cowork のチャットログ（セッションごとに ZIP）",
    "backup.comp.vault": "Obsidian 保管庫のスナップショット（ZIP）",
    "backup.disclaimer_short": "このモニターはバックアップログの内容を表示するだけです。バックアップについて当方は一切の責任を負いません。バックアップが完全で復元できるかどうかの確認は、ご自身で行ってください。",
    "backup.done": "完了",
    "backup.dry_run": "（テスト実行、アップロードなし）",
    "backup.failed": "失敗",
    "backup.files_size": "{}個のファイル、{}",
    "backup.folders": "フォルダー",
    "backup.label_age": "名前と経過時間",
    "backup.label_name": "名前のみ",
    "backup.label_none": "ランプのみ",
    "backup.last_ok": "最後に成功したバックアップ: {}（{}前）",
    "backup.last_run": "最終実行: {} – {}",
    "backup.legend": "緑: {}時間以内 · 黄: {}時間以内 · 赤: それより古い、またはバックアップなし",
    "backup.level_green": "最新",
    "backup.level_none": "バックアップが見つかりません",
    "backup.level_red": "古い",
    "backup.level_yellow": "やや古い",
    "backup.log_file": "ログファイル",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "バックアップフォルダーが見つかりません: {}",
    "backup.none_found": "なし",
    "backup.open": "開く",
    "backup.rc_copied": "新規または変更されたファイルをコピーしました",
    "backup.rc_failed": "失敗（コード {}）",
    "backup.rc_nochange": "最新の状態で、コピーするファイルはありません",
    "backup.recent_notes": "スナップショット内で最近編集されたノート",
    "backup.refresh": "今すぐ確認",
    "backup.sec_components": "バックアップ対象",
    "backup.sec_contents": "内容",
    "backup.sec_log": "ログ（最後の数行）",
    "backup.sec_problems": "エラーと警告",
    "backup.sec_tasks": "スケジュールされたタスク",
    "backup.skipped": "スキップ（フォルダーが見つかりません）",
    "backup.snap_kept": "{}個のスナップショットを保持、合計 {}",
    "backup.snapshot": "最新のスナップショット",
    "backup.source": "バックアップ元",
    "backup.state_error": "エラーで終了",
    "backup.state_interrupted": "未完了",
    "backup.state_ok": "正常に完了",
    "backup.state_running": "実行中",
    "backup.storage": "リモートストレージ: {1} 中 {0} を使用、空き {2}",
    "backup.target": "バックアップ先",
    "backup.task_event": "イベント時",
    "backup.task_row": "最終実行 {} · 結果 {} · 次回 {}",
    "backup.tip_click": "クリックで詳細を表示",
    "backup.title": "バックアップ",
    "backup.tray": "バックアップ: {}",
    "backup.uploaded": "今回のアップロード: 新規 {}、上書き {}、エラー {}",
    "backup.uploaded_files": "アップロードしたファイル",
    "backup.uploaded_groups": "アップロードしたファイル（フォルダー別）",
    "backup.uploaded_no": "Nextcloud へのアップロード: 未実施",
    "backup.uploaded_yes": "Nextcloud へのアップロード: 済み（{}）",
    "backup.vault": "保管庫",
    "backup.vault_changed": "このスナップショット以降に保管庫で{}件のノートが変更されました",
    "backup.zip_new": "新規/更新 ZIP: {}個",
    "backup.zip_summary": "{}個のファイル（ノート{}件）、非圧縮 {}",
    # --- general ----------------------------------------------------------------------------
    "detail.extra": "使用クレジット",
    "detail.local_header": "CLAUDE CODE · この PC · 今週の内訳",
    "detail.off": "オフ",
    "detail.on": "オン",
    "detail.surface.oauth_apps": "接続済みアプリ",
    "detail.unlimited": "上限なし",
    "dlg.cancel": "キャンセル",
    "dlg.checking": "確認中…",
    "dlg.err_badcode": "コードが受け付けられませんでした。\n\n{}\n\nコードをすべて貼り付けたか確認するか、ブラウザーでもう一度サインインしてください（その都度、新しいコードが発行されます）。",
    "dlg.err_ratelimit": "短時間でのサインインの試行回数が多すぎます。\n\nサーバーが一時的にアクセスを制限しています。このウィンドウを閉じて10～15分待ち（その間は再試行しないでください）、新しいコードでブラウザーからのサインインを1回だけ行ってください。",
    "dlg.hint1": "開いたページでサインインし、アクセスを許可してください。最後にコードが表示されます。",
    "dlg.intro": "お使いのブラウザーで claude.ai アカウントにサインインします（保存済みのパスワードやパスキーがそのまま使えます）。",
    "dlg.login_title": "サインイン",
    "dlg.open_browser": "ブラウザーでサインインページを開く",
    "dlg.paste_label": "受け取ったコードをここに貼り付けてください：",
    "dlg.paste_placeholder": "ここにコードを貼り付け",
    "dlg.signin": "サインイン",
    "dlg.step1": "手順1",
    "dlg.step2": "手順2",
    "dlg.unknown_err": "不明なエラーです。",
    # --- error messages ---------------------------------------------------------------------
    "err.already_running": "アプリは既に実行中です（通知領域を確認してください）。",
    "err.bad_token_resp": "トークンエンドポイントからの応答が無効です",
    "err.bad_usage_resp": "使用量エンドポイントからの応答が無効です",
    "err.connection": "接続エラー: {}",
    "err.file_empty": "使用量ファイルが空です。",
    "err.file_not_found": "使用量ファイルが見つかりません。\nClaude Desktop は起動していますか？",
    "err.file_unreadable": "現在、使用量ファイルを読み取れません。",
    "err.loading": "サインイン / データ取得中…",
    "err.network": "ネットワークエラー: {}",
    "err.no_code": "コードが貼り付けられていません。",
    "err.no_data_profile": "このプロファイルのデータはありません。",
    "err.no_tray": "通知領域を利用できないため、通知領域のアイコンは表示されません。",
    "err.no_usage_data": "使用量データがありません。",
    "err.not_signed_in": "サインインしていません。",
    "err.query_http": "問い合わせエラー（HTTP {}）。",
    "err.rate_limited": "サーバーがリクエストを制限しています（429）。自動的に再試行します。",
    "err.session_expired": "セッションの有効期限が切れました。もう一度サインインしてください。",
    "err.session_expired_nl": "セッションの有効期限が切れました。\nもう一度サインインしてください。",
    "err.signin_needed": "claude.ai のサインインの有効期限が切れました。\nもう一度サインインしてください（右クリック → claude.ai にサインイン）。",
    "err.unexpected": "予期しないエラー: {}",
    # --- "Message to the developer" window -------------------------------------------------
    "fb.cancel": "キャンセル",
    "fb.close": "閉じる",
    "fb.consent": "{}を読んだうえで同意します。",
    "fb.email": "メールアドレス",
    "fb.email_hint": "返信をご希望の場合のみ",
    "fb.err_consent": "送信するには、プライバシーポリシーに同意してください。",
    "fb.err_email": "メールアドレスの形式が正しくないようです。",
    "fb.err_empty": "先にメッセージを入力するか、評価を選択してください。",
    "fb.err_links": "メッセージにリンクが多すぎます。",
    "fb.err_network": "claudeusagemonitor.com に接続できませんでした。インターネット接続を確認して、もう一度お試しください。",
    "fb.err_rate": "短時間にメッセージが多すぎます。しばらくしてからもう一度お試しください。",
    "fb.err_server": "現在、サーバーがメッセージを受け付けられません。しばらくしてからもう一度お試しください。",
    "fb.intro": "アイデアや不具合の報告、あるいは「気に入った」のひと言でも、ぜひお聞かせください。メッセージはすべて、作者である私 Vidovics Gábor が自分で読んでいます。",
    "fb.message": "メッセージ",
    "fb.message_ph": "うまく動く点、動かない点、足りない点は？",
    "fb.meta": "メッセージと一緒に送信される情報: プログラムのバージョン {0}、オペレーティングシステム（{1}）、表示言語（{2}）。",
    "fb.name": "お名前",
    "fb.optional": "（任意）",
    "fb.privacy_hide": "ポリシーを非表示",
    "fb.privacy_text": (
        "管理者: Vidovics Gábor、個人（ハンガリー）、Claude Usage Monitor の作者。"
        "プライバシーポリシーの全文はウェブサイトに掲載しています: https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "送信される情報: ここに入力した内容（名前・メールアドレス（いずれも任意）、メッセージ、星評価）と、"
        "状況を把握するための情報（プログラムのバージョン、オペレーティングシステムの名前とバージョン、表示言語、送信日時）。"
        "サーバーは IP アドレスを保存しません。不正利用の防止のために、アドレスに復元できない、日ごとに変わるハッシュ値のみを使用します。"
        "\n\n"
        "目的: メッセージを読んで返信するため、およびプログラムを改善するため（正当な利益、GDPR 第6条第1項（f）。"
        "返信自体はユーザーの求めに応じて行います）。評価と名前がウェブサイトに掲載されるのは、"
        "専用のチェックボックスをオンにした場合（同意、第6条第1項（a））に限られ、かつ作者が内容を確認した後です。"
        "この同意はいつでも撤回できます。"
        "\n\n"
        "保存期間: メッセージは最長2年間。掲載された評価は同意を撤回するまで。"
        "作者がメールへの転送を有効にしている場合は、コピーが作者のメールボックスにも届きます。"
        "\n\n"
        "閲覧できる者: 管理者のみ、および処理者としてのホスティング事業者（サーバーは EU 域内のドイツにあります）。"
        "販売や第三者への提供は一切行わず、プロファイリングや自動化された意思決定も行いません。"
        "\n\n"
        "ユーザーの権利: アクセス、訂正、消去、取扱いの制限、異議の申立て、同意の撤回、"
        "ならびに監督機関（ハンガリーでは NAIH、naih.hu）またはお住まいの国の当局への苦情の申立て。"
        "連絡先: このフォームまたはウェブサイト。"
        "\n\n"
        "通信: claudeusagemonitor.com へ暗号化（HTTPS/TLS）して送信します。本ポリシーのバージョン: 2026-10-06。"
    ),
    "fb.privacy_title": "プライバシーポリシー",
    "fb.publish": "評価と名前（入力した場合）を claudeusagemonitor.com に掲載することに同意します。",
    "fb.rating": "総合評価",
    "fb.rating_clear": "クリア",
    "fb.rating_hint": "任意（星をクリック）",
    "fb.rating_tip": "5点満点中{}点",
    "fb.secure": "claudeusagemonitor.com への暗号化接続（HTTPS）。",
    "fb.send": "送信",
    "fb.sending": "送信中…",
    "fb.sent": "ありがとうございます。メッセージは無事に届きました！",
    "fb.sent_sub": "すべてのメッセージに目を通しています。メールアドレスをご記入いただいた場合は、そちらに返信します。",
    "fb.title": "開発者へのメッセージ",
    # --- Help window ------------------------------------------------------------------------
    "help.disclaimer": "独立した無料のツールです。Anthropic が開発したものではなく、Anthropic との提携関係もありません。「Claude」は Anthropic の商標です。",
    "help.feedback": "ご質問、アイデア、不具合の報告は、ウェブサイトのメッセージフォームへ。",
    "help.free": "ずっと無料 · MIT ライセンス · オープンソース · テレメトリなし",
    "help.guide": (
        "\n<h2>ウィジェットに表示される内容</h2>"
        "\n<ul>"
        "\n<li><b>5時間セッション</b> – 現在のセッション上限のうち、どれだけ使ったか。5時間ごとにリセットされ、ウィジェットにはリセットまでの残り時間が表示されます。</li>"
        "\n<li><b>週間上限</b> – すべてのモデルを合わせた使用量。毎週、アカウントごとに決まった曜日と時刻にリセットされます。</li>"
        "\n<li><b>モデル別の週間上限</b> – 3つ目のゲージ（特定のモデル向けなど）。サーバーから報告がある場合に表示されます。</li>"
        "\n<li><b>ペースと消費速度</b> – 上限をどれだけの速さで消費しているか、リセットまで持つかどうか。週の終わりの予測が早めに警告します。</li>"
        "\n<li><b>使用クレジット</b>とプランバッジ – <i>プランバッジと追加の上限</i>でオンにすると表示されます。</li>"
        "\n</ul>"
        "\n<h2>データの取得元</h2>"
        "\n<ul>"
        "\n<li><b>claude.ai（すべてのデバイス）</b> – Anthropic のサーバーに問い合わせるため、スマートフォン、ブラウザー、ほかのコンピューターでの使用量も含まれます。お使いのブラウザーで一度だけサインインが必要です（メニュー: <i>サインイン</i>）。2分ごとに更新されます（サーバーから要求があった場合は間隔が長くなります）。</li>"
        "\n<li><b>ローカル（この PC のみ）</b> – このコンピューター上の Claude Desktop の使用量ログを読み取ります。サインインは不要ですが、この PC の分しかわかりません。</li>"
        "\n</ul>"
        "\n<p>切り替えはメニューの<i>データソース</i>から。</p>"
        "\n<h2>ウィジェットの操作</h2>"
        "\n<ul>"
        "\n<li>ウィジェット（または通知領域のアイコン）を<b>右クリック</b> – すべてのメニュー項目を表示。</li>"
        "\n<li>ゲージを<b>ダブルクリック</b> – <b>履歴</b>ウィンドウを開きます。6時間、24時間、7日間、または全期間を、ピーク、1日あたりの平均、予測とともに表示します。</li>"
        "\n<li><b>ドラッグ</b>で移動。画面の端にスナップします。<b>Ctrl + マウスホイール</b> – 拡大・縮小。</li>"
        "\n<li>レイアウト: 付箋カード、スリムバー、リング。テーマは6種類。<i>位置を固定</i>と<i>クリック透過</i>は設定にあります。</li>"
        "\n</ul>"
        "\n<h2>アラート</h2>"
        "\n<p>70%以上で黄、90%以上で赤（しきい値は変更可能）。上限がリセットされたときや、データが古くなったときの通知も任意で受け取れます。</p>"
        "\n<h2>バックアップ（任意）</h2>"
        "\n<p>小さなランプは、スケジュールされたバックアップが実行され、完了したかどうかを示します。ランプをクリックすると詳細が表示されます。モニターはバックアップログを読むだけです。バックアップの作成とテストはご自身の責任で行ってください（利用規約を参照）。</p>"
        "\n<h2>更新</h2>"
        "\n<p>プログラムは新しいバージョンを自動的に確認し、ワンクリックで更新できます。すべてのパッケージは SHA-256 で検証され、<b>claudeusagemonitor.com</b> からのみ取得されます。新しいバージョンとリリースノート: {site}</p>"
        "\n<h2>プライバシー</h2>"
        "\n<p>テレメトリもトラッキングもありません。claude.ai のサインイン情報は暗号化してこのコンピューターにのみ保存され、ほかの場所には何も送信されません。</p>"
        "\n<h2>問題が起きたときは</h2>"
        "\n<ul>"
        "\n<li><i>429 / レート制限</i> – サーバーがリクエストを抑えています。プログラムが自動的に再試行します。</li>"
        "\n<li>データが表示されない –<i>データソース</i>を確認してください。claude.ai の場合はもう一度サインインしてください。</li>"
        "\n<li>履歴は7日間保持され、再起動や更新の後も残ります。</li>"
        "\n<li>ログと設定: <code>{cfg}</code>（<code>api.log</code>、<code>update.log</code>）。</li>"
        "\n</ul>"
        "\n"
    ),
    "help.made_by": "作成者",
    "help.moved": "2026年9月21日から新しいアドレスになりました。以前の dinorr.hu/claude-usage-monitor ページはここにリダイレクトされます。",
    "help.official": "公式ウェブサイト",
    "help.open_site": "claudeusagemonitor.com を開く",
    "help.privacy": "プライバシーポリシー",
    "help.site_what": "ダウンロード、自動更新、新機能、Claude Backup Kit、利用規約、プライバシーなど、すべての情報をここにまとめています。",
    "help.source_code": "ソースコード（GitHub）",
    "help.tab_author": "作者",
    "help.tab_guide": "使い方",
    "help.terms": "利用規約",
    "help.title": "ヘルプ",
    "help.version": "バージョン",
    # --- History window ---------------------------------------------------------------------
    "hist.legend_5h": "5時間セッション",
    "hist.legend_week": "週間上限",
    "hist.no_data": "この期間のデータが不足しています。",
    "hist.range_24h": "24時間",
    "hist.range_6h": "6時間",
    "hist.range_7d": "7日間",
    "hist.range_all": "すべて",
    "hist.stat_burn": "1日あたりの平均消費",
    "hist.stat_forecast": "週の終わりの予測",
    "hist.stat_now": "現在の週間使用量",
    "hist.stat_peak": "週間ピーク",
    "hist.stat_sessions": "5時間セッション数",
    "hist.title": "履歴",
    # --- layouts ----------------------------------------------------------------------------
    "layout.compact": "スリムバー",
    "layout.postit": "付箋カード",
    "layout.ring": "リング",
    # --- context menu -----------------------------------------------------------------------
    "menu.always_top": "常に手前に表示",
    "menu.autostart": "Windows と同時に起動",
    "menu.backup_bar": "バックアップ状態バー",
    "menu.backups": "バックアップ…",
    "menu.check_update": "プログラムの更新を確認…",
    "menu.click_through": "クリック透過",
    "menu.details": "プランバッジと追加の上限",
    "menu.feedback": "開発者へのメッセージ…",
    "menu.help": "ヘルプ…",
    "menu.history": "履歴と統計…",
    "menu.language": "言語",
    "menu.layout": "レイアウト",
    "menu.locked": "位置を固定",
    "menu.login": "サインイン（claude.ai、ブラウザー）…",
    "menu.logout": "サインアウト",
    "menu.model_gauge": "{} のゲージ",
    "menu.order": "表示順",
    "menu.panel_visible": "パネルを表示",
    "menu.quit": "終了",
    "menu.refresh": "使用量データを今すぐ更新",
    "menu.settings": "設定…",
    "menu.size": "サイズ",
    "menu.source": "データソース",
    "menu.start_menu": "スタートメニューに表示",
    "menu.theme": "テーマ",
    "menu.update_available": "プログラムの更新: バージョン {} をインストール…",
    # --- desktop notifications --------------------------------------------------------------
    "notify.autostart_fail": "自動起動を設定できませんでした。",
    "notify.autostart_off": "無効: アプリは Windows と同時に起動しなくなります。",
    "notify.autostart_on": "有効: アプリは Windows と同時に起動します。",
    "notify.first_run": "パネルが画面の右上に表示されました。\nパネルまたは通知領域のアイコンを右クリックすると、メニューが開きます。",
    "notify.login_ok": "サインインしました。サーバーのデータを取得しています。",
    "notify.logout": "サインアウトしました。ローカルのデータソースに切り替えました。",
    "notify.reset_done": "{}: リセットされ、新しい期間が始まりました。",
    "notify.signin_needed": "claude.ai のサインインの有効期限が切れました。すべてのデバイスの使用量を引き続き表示するには、パネルを右クリックしてもう一度サインインしてください。",
    "notify.stale_body": "最後の測定から{}経過しています。Claude Desktop は起動していますか？",
    "notify.stale_title": "古いデータ",
    "notify.threshold": "{}: {}%を使用しました。",
    "notify.update": "プログラムのバージョン {} が利用可能です。パネルを右クリック → プログラムの更新。",
    # --- panel labels (tight space) ---------------------------------------------------------
    "panel.five_hour": "5時間セッション",
    "panel.five_hour_short": "5時間",
    "panel.full_in": "上限まで{}",
    "panel.model": "{} 週間上限",
    "panel.no_data": "データなし",
    "panel.pace": "ペース差{}",
    "panel.per_day": "{}%/日",
    "panel.per_hour": "{}%/時",
    "panel.refreshing": "データ取得中",
    "panel.reset": "リセットまで{}",
    "panel.retry_in": "{}秒後に再試行",
    "panel.updated": "更新: {}",
    "panel.week_short": "週",
    "panel.weekly": "週間上限",
    # --- profile ----------------------------------------------------------------------------
    "profile.extra": "使用クレジット: {}",
    "profile.plan": "プラン: {}",
    "profile.since": "登録日: {}",
    "profile.tier": "レート制限レベル: {}",
    # --- Settings window --------------------------------------------------------------------
    "set.about": "{}\nテレメトリはありません。このプログラムは Anthropic にご自身の使用量を問い合わせ、更新サーバーからバージョン番号を読み取るだけです。",
    "set.accent": "アクセントカラー",
    "set.always_top": "ほかのすべてのウィンドウより手前に表示",
    "set.auto": "自動",
    "set.backup_config": "バックアップスクリプトの構成ファイル",
    "set.backup_details": "詳細ウィンドウの表示内容",
    "set.backup_disclaimer": "Claude Usage Monitor はバックアップのログを読み取って表示するだけであり、バックアップの作成、確認、保証は一切行いません。Claude Backup Kit は、手助けとして無料で提供している出発点（ひな形）にすぎません。スクリプトは誰でも変更できるため、バックアップの品質や完全性は保証できません。バックアップ、データの損失、およびあらゆる損害について、当方は一切の責任を負いません。バックアップが完全で復元可能であることの確認は、ご自身の責任で行ってください。ときどき実際に復元をテストしてください。",
    "set.backup_disclaimer_h": "免責事項",
    "set.backup_enabled": "パネルにバックアップ状態バーを表示",
    "set.backup_found": "検出: {}",
    "set.backup_green": "緑: 最長",
    "set.backup_label": "ランプの横のラベル",
    "set.backup_lamps": "ランプ",
    "set.backup_root": "バックアップフォルダー",
    "set.backup_tasks": "スケジュールされたタスクのフィルター",
    "set.backup_unconfigured": "バックアップフォルダーが設定されていないため、状態バーは非表示のままです。バックアップスクリプトの書き込み先フォルダーを選択してください。",
    "set.backup_yellow": "黄: 最長",
    "set.browse": "参照…",
    "set.click_through": "クリック透過（装飾のみ、マウス操作を無視）",
    "set.close": "閉じる",
    "set.color_hint": "色はしきい値に応じて変わります: 緑 → 黄 → 赤。",
    "set.danger": "危険",
    "set.data_hint": "ローカルログ: Claude Desktop の plan-usage-history.json。サインインは不要ですが、この PC の分だけを測定し、更新は約5分ごとです。\n\nclaude.ai: サインイン後にサーバーへ問い合わせます。すべてのデバイスの使用量を確認でき、リセット時刻も正確で、更新もより頻繁です。",
    "set.datafile": "データファイル",
    "set.default": "既定",
    "set.details_api_only": "これらは claude.ai データソースから取得されます（サインインが必要）。ローカルログには含まれません。",
    "set.file_filter": "JSON (*.json);;すべてのファイル (*.*)",
    "set.gauge_order": "ゲージの表示順",
    "set.hours_suffix": "時間",
    "set.layout": "レイアウト",
    "set.local_models_hint": "サーバーが個別のカウンターを持つのは一部のモデル（Fable など）だけです。それ以外のモデルについては、この PC での今週の Claude Code の作業がモデル間でどう分かれているかを示します。これはご自身の使用量と出力トークンに占める割合であり、上限に対する割合ではありません。読み取るのはモデル名とトークン数だけで、会話の内容は一切読み取りません。",
    "set.local_models_none": "Claude Code のログフォルダーが見つかりませんでした。このグループは非表示になるだけで、ほかには何も影響しません。",
    "set.local_models_path": "Claude Code のログフォルダー",
    "set.lock": "位置を固定（ドラッグ不可）",
    "set.login_btn_in": "claude.ai からサインアウト",
    "set.login_btn_out": "claude.ai にサインイン…",
    "set.model_filter": "追跡するモデル",
    "set.model_scale": "モデルゲージのサイズ",
    "set.not_set": "未設定",
    "set.notify_enabled": "しきい値を超えたときに通知",
    "set.notify_reset": "上限がリセットされたときに通知",
    "set.notify_stale": "データが古くなったときに通知",
    "set.opacity": "不透明度",
    "set.open_config": "設定フォルダーを開く",
    "set.pick_color": "色を選択…",
    "set.pick_file_title": "使用量ログの選択",
    "set.profile": "プロファイル / アカウント",
    "set.profile_auto": "自動（最後に使用したもの）",
    "set.profile_n": "プロファイル {} – …{}",
    "set.refresh": "更新",
    "set.reset_confirm": "既定の設定に戻してもよろしいですか？",
    "set.restore": "既定値に戻す",
    "set.rows_available": "現在表示できる項目です。表示しない項目はチェックを外してください：",
    "set.rows_none": "現在、サーバーはこのアカウントに追加の上限を送信していません。送信され次第、ここに自動的に表示されます。",
    "set.sec_suffix": "秒",
    "set.show_age": "データの鮮度",
    "set.show_burn": "消費速度（%/時、%/日）",
    "set.show_extra_usage": "使用クレジット（従量課金）",
    "set.show_feedback_icon": "パネルのヘッダーにメッセージアイコンを表示",
    "set.show_five_hour": "5時間セッションを表示",
    "set.show_local_models": "モデル別の内訳（この PC の Claude Code ログから）",
    "set.show_model": "モデルの週間上限を表示（claude.ai データソース）",
    "set.show_model_list": "その他のモデルの週間上限",
    "set.show_plan_badge": "ヘッダーにプランバッジを表示（Pro / Max…）",
    "set.show_plan_name": "バッジに自分の名前を表示",
    "set.show_reset": "リセットまでのカウントダウン",
    "set.show_spark": "トレンド曲線（スパークライン）",
    "set.show_surfaces": "利用環境ごとの上限（Claude Code、接続済みアプリ…）",
    "set.show_weekly": "週間上限を表示",
    "set.size": "サイズ",
    "set.snap": "画面の端にスナップ",
    "set.source_api": "claude.ai – すべてのデバイス（サインインが必要）",
    "set.source_label": "データの取得元",
    "set.source_local": "ローカルログ – この PC のみ",
    "set.tab_alerts": "アラート",
    "set.tab_appearance": "外観",
    "set.tab_content": "表示内容",
    "set.tab_data": "データソース",
    "set.tab_details": "詳細",
    "set.tab_system": "システム",
    "set.taskbar": "タスクバーに表示（ウィンドウとして）",
    "set.theme": "テーマ",
    "set.theme_default": "テーマの既定値",
    "set.tip": "ヒント: パネルは左ボタンでドラッグ、Ctrl+ホイールでサイズ変更、\n右クリックでメニュー、ダブルクリックで履歴を表示。",
    "set.title": "設定",
    "set.tray_five": "5時間セッション",
    "set.tray_max": "高いほう",
    "set.tray_value": "通知領域のアイコンに表示する値",
    "set.tray_weekly": "週間上限",
    "set.update_check": "プログラムの更新を自動的に確認",
    "set.version": "バージョン",
    "set.visible": "フローティングパネルを表示",
    "set.warn": "警告",
    # --- sizes, sources, themes -------------------------------------------------------------
    "size.extra": "特大",
    "size.large": "大",
    "size.normal": "標準",
    "size.small": "小",
    "source.api": "claude.ai（すべてのデバイス）",
    "source.local": "ローカル（この PC のみ）",
    "theme.claude": "Claude（暖色ダーク）",
    "theme.graphite": "グラファイト",
    "theme.midnight": "ミッドナイトグラス",
    "theme.neon": "ネオン",
    "theme.paper": "ライトペーパー",
    "theme.postit": "付箋イエロー",
    # --- time units (short) -----------------------------------------------------------------
    "time.day": "{}日",
    "time.dh": "{}日{}時間",
    "time.hm": "{}時間{}分",
    "time.hour": "{}時間",
    "time.m": "{}分",
    "time.min": "{}分",
    "time.none": "データなし",
    "time.sec": "{}秒",
    # --- tray -------------------------------------------------------------------------------
    "tray.head": "5時間: {}%   ·   週: {}%",
    "tray.line": "{}: {}%",
    # --- updates ----------------------------------------------------------------------------
    "update.available": "バージョン {} が利用可能です。",
    "update.check_failed": "更新を確認できませんでした: {}",
    "update.check_now": "今すぐ確認",
    "update.checking": "更新を確認中…",
    "update.downloading": "ダウンロード中… {} / {}",
    "update.failed": "更新に失敗しました: {}",
    "update.install": "今すぐインストール",
    "update.installed": "インストール済みのバージョン: {}",
    "update.later": "後で",
    "update.manual": "この環境では自動更新を利用できません（ソースコードから、または読み取り専用のフォルダーから実行されているため）。代わりに新しいパッケージをダウンロードしてください。",
    "update.open_page": "ダウンロードページを開く",
    "update.restarting": "インストール中です。アプリはまもなく再起動します。",
    "update.skip": "このバージョンをスキップ",
    "update.title": "プログラムの更新",
    "update.uptodate": "最新のバージョンをお使いです。",
    "update.verifying": "検証・展開中…",
    "update.whats_new": "新機能",
}

# macOS wording (Apple terminology): "ログイン時に開く" instead of "Windows と同時に起動", メニューバー instead of 通知領域
STRINGS_MAC = {
    "menu.autostart": "ログイン時に開く",
    "notify.autostart_on": "有効: アプリはログイン時に起動します。",
    "notify.autostart_off": "無効: アプリはログイン時に起動しなくなります。",
    "notify.first_run": "パネルが画面の右上に表示されました。\nパネルまたはメニューバーのアイコンを右クリックすると、メニューが開きます。",
}
