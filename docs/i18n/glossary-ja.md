# Glossary – 日本語 (ja) – Claude Usage Monitor

## Tone and form of address

- **Register:** polite です・ます体 for every full sentence (dialogs, notifications, hints, errors,
  help text, legal text). Labels, menu items, buttons, tab names and status words use 体言止め
  (noun form) with no final 。 – exactly the way the Japanese UI of Windows, Office and macOS works.
- **Addressing the user:** no second-person pronoun. Japanese consumer software avoids あなた;
  requests are made with ～してください, and the user's things are お使いの～ / ご自身の～.
  The legal text uses the neutral ユーザー (never お客様 – the program is a free tool by an
  individual, not a commercial service).
- **The author (fb.* texts) speaks in the first person** without a pronoun and in です・ます form,
  as the English does (“I read every message”).
- **Script and punctuation:** full-width 。、「」（）～ in Japanese text; half-width digits and
  Latin letters. Half-width `:` + space in “label: value” pairs (Windows convention, e.g.
  バージョン: 1.2); a full-width `：` closes a label that ends with a colon.
  Half-width parentheses only in the file-filter string (`JSON (*.json);;すべてのファイル (*.*)`),
  which is Windows syntax. Ellipsis is the single character …. The range dash is ～ (10～15分).
  The en dash “–” of the English (“Installing – the app restarts…”) becomes 。 or 、 in Japanese
  running text; it stays only in label-style strings (“claude.ai – すべてのデバイス”).
- **Spacing:** a half-width space between Japanese and a Latin word, product name, URL or a
  placeholder that inserts Latin text (Claude Desktop は…, バージョン {}), as Microsoft's style
  guide prescribes. No space inside Japanese text, and none between a number and its unit or
  counter (5時間, 24時間, 70%, 2年間, {}秒, {}個). A placeholder that inserts a Japanese time
  string (time.*) is attached without a space (リセットまで{}, {}経過). Numbers and numeric
  placeholders are attached to Japanese text too (10～15分待ち, 1回だけ, 手順1, {}件のノート).
  No “=” shorthand in sentences: 右クリックでメニュー, not 右クリック = メニュー.
  Katakana compounds are written without a space (スタートメニュー, バックアップフォルダー).
- **Katakana:** Microsoft style with the final long vowel – ユーザー, サーバー, フォルダー, エラー,
  ブラウザー, カウンター, フィルター, カラー, コンピューター, ヘッダー.
- **Panel labels:** Japanese has no case; the UPPERCASE English labels become short, clear nouns
  (5時間セッション, 週間上限, 週). They are never longer than the English in characters.

## Fixed terms

| English | 日本語 | Note |
|---|---|---|
| 5-hour session | 5時間セッション | panel, history, settings; count in History = 5時間セッション数 |
| weekly limit | 週間上限 | |
| per-model weekly limit | モデル別の週間上限 | |
| limit (rate limit) | 上限 | “no limit” = 上限なし |
| rate-limit tier | レート制限レベル | |
| reset (noun / verb) | リセット / リセットされる | “reset {}” on the panel = リセットまで{} |
| full (panel countdown) | 上限まで{} | time until the gauge reaches 100 % |
| pace | ペース | “{} vs pace” = ペース差{} (a signed % is inserted) |
| burn rate | 消費速度 | |
| usage | 使用量 | |
| usage credits | 使用クレジット | pay-as-you-go = 従量課金 |
| usage data / usage file / usage log | 使用量データ / 使用量ファイル / 使用量ログ | |
| gauge | ゲージ | |
| panel / floating panel | パネル / フローティングパネル | |
| widget (help text) | ウィジェット | |
| tray / tray icon (Windows) | 通知領域 / 通知領域のアイコン | Microsoft term |
| menu bar icon (macOS) | メニューバーのアイコン | Apple term, STRINGS_MAC only |
| taskbar | タスクバー | |
| Start menu | スタートメニュー | |
| start with Windows / start at login | Windows と同時に起動 / ログイン時に開く | the macOS wording is Apple's “ログイン時に開く”; avoid the redundant 起動時に起動 |
| sign in / sign out | サインイン / サインアウト | Microsoft term |
| session (sign-in) | セッション | |
| notification | 通知 | |
| alert(s) | アラート | settings tab |
| threshold | しきい値 | |
| warning / critical | 警告 / 危険 | threshold names |
| backup | バックアップ | |
| backup status bar | バックアップ状態バー | |
| backup source / destination | バックアップ元 / バックアップ先 | |
| lamp | ランプ | |
| snapshot | スナップショット | |
| vault (Obsidian) | 保管庫 | the term Obsidian's own Japanese UI uses |
| data source | データソース | “Measurement source” label and help heading = データの取得元 |
| order (gauge order) | 表示順 | |
| local log | ローカルログ | |
| local (this PC only) | ローカル（この PC のみ） | |
| surface (per-surface limits) | 利用環境 | Claude Code, connected apps… |
| connected apps | 接続済みアプリ | |
| profile | プロファイル | Microsoft term |
| plan / plan badge | プラン / プランバッジ | |
| member since | 登録日 | |
| theme | テーマ | |
| layout | レイアウト | |
| settings | 設定 | |
| default(s) | 既定 / 既定値 | Microsoft term (not デフォルト) |
| update (program update) | 更新 / プログラムの更新 | |
| install | インストール | |
| version | バージョン | |
| history | 履歴 | |
| projection / forecast | 予測 | |
| peak | ピーク | |
| trend curve (sparkline) | トレンド曲線（スパークライン） | |
| data freshness / stale data | データの鮮度 / 古いデータ | |
| message to the developer | 開発者へのメッセージ | |
| rating / overall rating | 評価 / 総合評価 | |
| privacy policy / privacy notice | プライバシーポリシー | see below |
| consent | 同意 | |
| controller / processor | 管理者 / 処理者 | GDPR terms as used in the official Japanese translations |
| processing (GDPR) / restriction of processing | 取扱い / 取扱いの制限 | PPC translation; not 処理 |
| complaint (to an authority) | 苦情の申立て | GDPR Art. 77 wording |
| legitimate interest | 正当な利益 | |
| supervisory authority | 監督機関 | |
| terms of use | 利用規約 | |
| disclaimer | 免責事項 | |
| click-through | クリック透過 | |
| always on top | 常に手前に表示 | Windows wording |
| lock position | 位置を固定 | |
| snap to screen edge | 画面の端にスナップ | |
| opacity / accent color | 不透明度 / アクセントカラー | |
| scheduled task | スケジュールされたタスク | Microsoft term |
| folder | フォルダー | |
| retry | 再試行 | |
| time units | 秒 / 分 / 時間 / 日 | always attached to the number |

## Name of the privacy document

**プライバシーポリシー** – this is the term every major platform uses in Japan (Microsoft, Apple,
Google, LINE, Yahoo! JAPAN) and the term the 個人情報保護委員会 itself uses when it refers to a
company's published policy. 「個人情報の取り扱いについて」 is the wording of a *notice attached to a
form* (e.g. under a contact form on a corporate site) and would fit a notice embedded in a dialog,
but the program links the same document from the Help window as “Privacy policy” and from the
website, where it is unmistakably a プライバシーポリシー; using one name everywhere is what a
Japanese user expects. The consent line therefore reads 「プライバシーポリシーを読んだうえで同意します。」

The complaint sentence keeps “the authority of your own country” (お住まいの国の当局): Japan's
個人情報保護委員会 is not a GDPR supervisory authority, so naming it would be legally misleading.
GDPR stays “GDPR” (the Japanese press and the PPC use the acronym; 一般データ保護規則 is only the gloss).
