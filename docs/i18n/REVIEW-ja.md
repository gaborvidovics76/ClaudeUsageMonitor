# REVIEW – 日本語 (ja)

Module: `claude_usage/langs/ja.py` – 358 keys + 4 STRINGS_MAC. `check_i18n ja` → OK (the warnings are
product and file names, the author's name, PC / EU / IP – all deliberate).
Register: です・ます for sentences, 体言止め for labels/menu items; no second-person pronoun.
Privacy document: プライバシーポリシー (reasoning in `glossary-ja.md`).

Texts I am least sure about (max 10):

1. **`panel.five_hour_short` – 「5時間」.** English “5H” is 2 characters; 「5時間」 is 3 and visually
   wider. There is no shorter Japanese that stays unambiguous (「5時」 reads as *5 o'clock*). Hungarian
   uses 6 characters (“5 ÓRA”), so some slack seems tolerated. If the slim layout clips it, 「5h」
   would be the only shorter option – but it is not Japanese.

2. **`panel.pace` – 「ペース差{}」.** “{} vs pace” inserts a signed percentage (e.g. +5 %). I chose
   ペース差 (*difference from pace*) over ペース比 (*ratio*), because the value is a difference. If the
   inserted value is actually a ratio, change to 「ペース比{}」.

3. **`panel.full_in` – 「上限まで{}」.** I read “full: {}” as *time until the gauge reaches 100 %* and
   wrote *until the limit: {}*. If it means something else (e.g. a clock time), please tell me.

4. **`hist.stat_sessions` – 「5時間セッション数」.** The English plural “5-hour sessions” suggests the
   stat is a *count*; 数 makes that explicit. If the value is not a count, drop the 数.

5. **`set.show_surfaces` – 「利用環境ごとの上限」.** “Surface” (Claude Code, connected apps…) has no
   established Japanese term in Anthropic's UI. 利用環境 (*usage environment*) is the clearest for a
   lay user; サーフェス would be a bare loanword nobody understands.

6. **`set.hours_suffix` / `set.sec_suffix` – 「時間」 / 「秒」 without the leading space.** The English
   “ h” / “ s” carry a space because Latin units take one; Japanese writes 24時間 / 30秒 with no space.
   If the spin box shows a gap anyway, this is still correct.

7. **`backup.storage` – numbered placeholders.** 「{1} 中 {0} を使用、空き {2}」 – Japanese says
   *of total, used* (total first), so I renumbered: {0} = used, {1} = total, {2} = free, as in the
   English order of arguments.

8. **`fb.privacy_text` – legal register.** GDPR article cited as 「GDPR 第6条第1項（f）」 (the form the
   個人情報保護委員会 uses in its translations). Controller/processor = 管理者/処理者. The complaint
   sentence keeps “the authority of your own country” (お住まいの国の当局) – Japan's PPC is not a GDPR
   supervisory authority. The date stays ISO (2026-10-06), which is also the normal Japanese order.

9. **`fb.privacy_hide` – 「ポリシーを非表示」.** Literal “hide the notice” would be 「お知らせを隠す」,
   which a Japanese user would read as *hide the announcement*. The box being hidden is the policy
   text, so I named it ポリシー; short enough for the link.

10. **Spacing between Japanese and Latin text.** The instruction said “no spaces between words”. I
    applied that to Japanese words, but kept Microsoft's rule of one half-width space between Japanese
    and a Latin word / product name / URL / Latin placeholder (「Claude Desktop は」, 「バージョン {}」,
    「この PC」) – this is what every Microsoft and Apple Japanese UI does and what a native reader
    expects. Numbers and their units/counters are attached (5時間, 70%, {}秒). If the project prefers
    no spaces at all, it is a mechanical find-and-replace.

EN/HU differences noticed: `help.guide` HU calls the Help tab “Használat” (Usage) where EN says “How it
works” – I followed EN (「使い方」 covers both). HU `fb.privacy_text` links to `/hu/#privacy`; I kept the
English URL (`/#privacy`) as there is no `/ja/` page that I know of. HU `menu.help` adds “(HELP)”; EN
does not, so neither does the Japanese. `fb.optional`: HU “nem kötelező”, EN “optional” → 「任意」, the
standard Japanese form label.

## Lektor

Independent native review, 2026-10-07. 69 changes in `claude_usage/langs/ja.py` (STRINGS + STRINGS_MAC), glossary
updated to match. `check_i18n ja` → OK.

- backup.cloud_only: オンラインのみの状態です／ダウンロードが発生しないよう → OneDrive のオンライン専用ファイルです／ダウンロードせずに済むよう – OneDrive's own Japanese term
- backup.none_found: なし。 → なし – status word, no 。
- backup.rc_nochange: 最新の状態です。コピーするものはありません → 最新の状態で、コピーするファイルはありません – one status line, no mid 。
- backup.sec_components: バックアップの対象 → バックアップ対象 – tighter heading noun
- backup.sec_log: ログ（末尾の行） → ログ（最後の数行） – natural wording
- backup.state_interrupted: 完了せず → 未完了 – standard status noun
- backup.uploaded: 置換 {} → 上書き {} – files are overwritten, not substituted
- backup.uploaded_groups: フォルダー別のアップロードファイル → アップロードしたファイル（フォルダー別） – avoid noun-stack calque
- backup.uploaded_no: 未完了 → 未実施 – pairs with 済み
- backup.vault_changed: 保管庫で {} 件 → 保管庫で{}件 – counter spacing per glossary
- backup.zip_summary: ノート {}件 → ノート{}件 – counter spacing per glossary
- dlg.err_badcode: コード全体を貼り付けたか…（毎回新しいコードが必要です） → コードをすべて貼り付けたか…（その都度、新しいコードが発行されます） – smoother, clearer meaning
- dlg.err_ratelimit: 短時間にサインインを何度も試行しました…閉じて 10～15分…1 回だけ開始 → 短時間でのサインインの試行回数が多すぎます…閉じて10～15分…1回だけ行ってください – standard error phrasing, spacing
- dlg.open_browser: ブラウザーでサインインを開く → ブラウザーでサインインページを開く – "open sign-in" calque
- dlg.step1 / dlg.step2: 手順 1 / 手順 2 → 手順1 / 手順2 – number spacing consistency
- err.file_unreadable: 使用量ファイルを現在読み取れません。 → 現在、使用量ファイルを読み取れません。 – natural word order
- err.signin_needed: …ください: 右クリック → … → …ください（右クリック → …）。 – no half-width colon mid-sentence
- fb.err_email: このメールアドレスは正しくないようです。 → メールアドレスの形式が正しくないようです。 – usual form-validation wording
- fb.err_network: 接続を確認して → インターネット接続を確認して – unambiguous
- fb.err_server: サーバーが現在…受け付けられませんでした → 現在、サーバーが…受け付けられません – tense mismatch fixed
- fb.intro: …単に気に入ったという感想でも…作者の Vidovics Gábor が自分で読んでいます → …「気に入った」のひと言でも…作者である私 Vidovics Gábor が自分で読んでいます – first person, as in English
- fb.message_ph: うまく動くこと、動かないこと、足りないものは？ → うまく動く点、動かない点、足りない点は？ – parallel, natural
- fb.publish: 評価と（入力した場合は）お名前を → 評価と名前（入力した場合）を – user's own statement, no honorific
- fb.sent: メッセージが届きました！ → メッセージは無事に届きました！ – warmer, natural
- fb.rating_hint: 任意 – 星をクリック → 任意（星をクリック） – Japanese punctuation, no en dash
- fb.privacy_text: お名前（任意）、メールアドレス（任意） → 名前・メールアドレス（いずれも任意） – no nested brackets, legal register
- fb.privacy_text: 返信そのものはご本人の求めに → 返信自体はユーザーの求めに – glossary: neutral ユーザー
- fb.privacy_text: 評価とお名前が → 評価と名前が – legal register, no honorific
- fb.privacy_text: 閲覧者 → 閲覧できる者 – "who can see it"
- fb.privacy_text: 処理の制限、異議申立て…および…当局への申立て → 取扱いの制限、異議の申立て…ならびに…当局への苦情の申立て – PPC GDPR terms (Art. 18, 21, 77)
- help.free: 永久に無料 → ずっと無料 – natural consumer wording
- help.guide (5時間セッション): ウィジェットはリセットまでをカウントダウンします → ウィジェットにはリセットまでの残り時間が表示されます – calque removed
- help.guide (週間上限): アカウントごとに決まった週の時刻に → 毎週、アカウントごとに決まった曜日と時刻に – "fixed weekly time" made clear
- help.guide (モデル別): reordered → 3つ目のゲージ（…）。サーバーから報告がある場合に表示されます – natural order
- help.guide (使用クレジット): …でオンにした場合。 → …でオンにすると表示されます。 – complete sentence
- help.guide (claude.ai): サーバーの要求があればより遅くなります → （サーバーから要求があった場合は間隔が長くなります） – "slower" means longer interval
- help.guide (右クリック): メニュー全体 → すべてのメニュー項目を表示 – calque removed
- help.guide (ダブルクリック): 履歴ウィンドウ: → 履歴ウィンドウを開きます。 – sentence instead of label
- help.guide (アラート): 70%から黄、90%から赤（調整可能） → 70%以上で黄、90%以上で赤（しきい値は変更可能） – precise, natural
- help.guide (更新): ワンクリックで更新します → ワンクリックで更新できます – user clicks, not automatic
- help.guide (問題): データがない → データが表示されない – natural symptom phrasing
- help.site_what: …利用規約とプライバシー – すべてここにまとまっています。 → …利用規約、プライバシーなど、すべての情報をここにまとめています。 – no en dash in sentence
- hist.stat_burn: 1日の平均消費 → 1日あたりの平均消費 – "per day" made explicit
- menu.autostart: Windows の起動時に起動 → Windows と同時に起動 – redundant 起動…起動
- menu.order: 順序 → 表示順 – usual UI term
- notify.autostart_on: Windows の起動時に起動します → Windows と同時に起動します – follows menu wording
- notify.autostart_off: Windows の起動時に起動しません → Windows と同時に起動しなくなります – follows menu, state change
- notify.first_run: …を右クリック = メニュー。 → …を右クリックすると、メニューが開きます。 – no "=" shorthand
- notify.logout: ローカルソースに切り替えました → ローカルのデータソースに切り替えました – glossary term
- notify.reset_done: リセットされました — 新しい期間が始まりました → リセットされ、新しい期間が始まりました – no em dash
- panel.model: {} 週間 → {} 週間上限 – "週間" alone is incomplete
- set.about: Anthropic にはご自身の使用量のみを問い合わせ… → このプログラムは Anthropic にご自身の使用量を問い合わせ… – subject added, natural
- set.always_top: 他のすべてのウィンドウの手前に表示 → ほかのすべてのウィンドウより手前に表示 – ほか consistent, natural particle
- set.backup_disclaimer: 支援として提供する無料の出発点 → 手助けとして無料で提供している出発点（ひな形） – calque removed
- set.backup_disclaimer: 各自の責任です。ときどき復元のテストを行ってください → ご自身の責任で行ってください。ときどき実際に復元をテストしてください – consistent address, natural
- set.data_hint: …正確なリセット時刻とより頻繁な更新で確認できます → …確認でき、リセット時刻も正確で、更新もより頻繁です – calque removed
- set.gauge_order: ゲージの順序 → ゲージの表示順 – matches menu.order
- set.pick_color: 色の選択… → 色を選択… – button takes verb form
- set.rows_available: 現在表示できる項目 – 表示しないものは… → 現在表示できる項目です。表示しない項目は… – no en dash in sentence
- set.show_local_models: この PC の Claude Code ログによるモデル間の内訳 → モデル別の内訳（この PC の Claude Code ログから） – clearer checkbox label
- set.show_model: （claude.ai ソース） → （claude.ai データソース） – glossary term
- set.source_label: 測定ソース → データの取得元 – matches help heading
- set.theme_default: テーマの既定 → テーマの既定値 – button value, Microsoft term
- set.tip: 右クリック = メニュー、ダブルクリック = 履歴。 → 右クリックでメニュー、ダブルクリックで履歴を表示。 – no "=" shorthand
- set.tray_value: 通知領域アイコンの値 → 通知領域のアイコンに表示する値 – clearer label
- update.manual: このコピーは自分自身を更新できません（…実行されています） → この環境では自動更新を利用できません（…実行されているため） – "this copy" calque
- update.verifying: 検証と展開中… → 検証・展開中… – natural progress label
- STRINGS_MAC notify.autostart_off: ログイン時に起動しません → ログイン時に起動しなくなります – state change
- STRINGS_MAC notify.first_run: …を右クリック = メニュー。 → …を右クリックすると、メニューが開きます。 – no "=" shorthand

Glossary (`glossary-ja.md`): start with Windows → Windows と同時に起動; added 表示順, データの取得元, GDPR 取扱い /
苦情の申立て, and the rule that numbers attach to Japanese text and "=" is not used in sentences.

Still in doubt:
- `hist.stat_forecast` / help "週末時点の予測": 週末 can also read as *weekend*; in a business/statistics context it
  is understood as *end of the week*, so I kept it. If users misread it, 「週の終わりの予測」 or 「リセット時の予測」.
- `panel.five_hour_short` 「5時間」 (3 characters vs "5H") – kept; no shorter unambiguous Japanese.
- `panel.pace` 「ペース差{}」 – kept; the inserted value is a signed difference (actual − ideal, from the code), so 差 is right.
- `detail.local_header` keeps "CLAUDE CODE" in capitals to match the uppercase header style of the Latin scripts.
- Microsoft's own Japanese style puts a space between Japanese and numbers (「12 個の項目」); this file follows its glossary
  (numbers attached) consistently instead. Either is acceptable as long as it is consistent.
