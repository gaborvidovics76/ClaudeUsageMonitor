# -*- coding: utf-8 -*-
"""한국어 – UI strings of Claude Usage Monitor.

Friendly polite 해요체 for messages and notifications, nouns for labels, short verb nouns for
buttons, formal 합니다체 for the legal texts. Microsoft terminology for Windows (알림 영역,
작업 표시줄, 로그인/로그아웃), Apple terminology in STRINGS_MAC (메뉴 막대, 로그인 시 열기).
See docs/i18n/glossary-ko.md.
"""

CODE = "ko"
NAME = "한국어"

STRINGS = {
    # --- backup status bar / details window ----------------------------------------------
    "backup.age_d": "{}일",
    "backup.age_h": "{}시간",
    "backup.age_m": "{}분",
    "backup.and_more": "…외 {}개",
    "backup.checked_at": "확인: {}",
    "backup.checking": "확인하는 중…",
    "backup.cloud_only": "이 스냅샷은 OneDrive에 온라인 전용으로 저장되어 있어요. 내려받지 않아도 되도록 내용은 표시하지 않아요.",
    "backup.comp.cowork": "Cowork 대화 로그(세션별 ZIP)",
    "backup.comp.vault": "Obsidian 보관소 스냅샷(ZIP)",
    "backup.disclaimer_short": "모니터는 백업 로그에 기록된 내용만 보여 줘요. 백업에 대한 책임은 지지 않으며, 백업이 완전한지와 복원할 수 있는지는 직접 확인해야 해요.",
    "backup.done": "완료",
    "backup.dry_run": "(테스트 실행, 업로드 없음)",
    "backup.failed": "실패",
    "backup.files_size": "파일 {}개, {}",
    "backup.folders": "폴더",
    "backup.label_age": "이름과 경과 시간",
    "backup.label_name": "이름만",
    "backup.label_none": "표시등만",
    "backup.last_ok": "마지막 성공 백업: {} ({} 전)",
    "backup.last_run": "마지막 실행: {} – {}",
    "backup.legend": "녹색: {}시간 이내 · 노란색: {}시간 이내 · 빨간색: 더 오래됐거나 백업 없음",
    "backup.level_green": "최신",
    "backup.level_none": "백업 없음",
    "backup.level_red": "오래됨",
    "backup.level_yellow": "조금 오래됨",
    "backup.log_file": "로그 파일",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "백업 폴더를 찾을 수 없어요: {}",
    "backup.none_found": "없음.",
    "backup.open": "열기",
    "backup.rc_copied": "새 파일 또는 변경된 파일 복사됨",
    "backup.rc_failed": "실패(코드 {})",
    "backup.rc_nochange": "최신 상태, 복사할 항목 없음",
    "backup.recent_notes": "스냅샷에서 최근에 편집한 노트",
    "backup.refresh": "지금 확인",
    "backup.sec_components": "백업 항목",
    "backup.sec_contents": "내용",
    "backup.sec_log": "로그(마지막 줄)",
    "backup.sec_problems": "오류 및 경고",
    "backup.sec_tasks": "예약된 작업",
    "backup.skipped": "건너뜀(폴더 없음)",
    "backup.snap_kept": "스냅샷 {}개 보관, 총 {}",
    "backup.snapshot": "최신 스냅샷",
    "backup.source": "원본",
    "backup.state_error": "오류와 함께 종료됨",
    "backup.state_interrupted": "완료되지 않음",
    "backup.state_ok": "정상 완료",
    "backup.state_running": "실행 중",
    "backup.storage": "원격 저장소: {1} 중 {0} 사용, {2} 남음",
    "backup.target": "대상",
    "backup.task_event": "이벤트 시",
    "backup.task_row": "마지막 실행 {} · 결과 {} · 다음 {}",
    "backup.tip_click": "클릭하여 자세히 보기",
    "backup.title": "백업",
    "backup.tray": "백업: {}",
    "backup.uploaded": "이번 실행에서 업로드: 새 파일 {}개, 교체 {}개, 오류 {}개",
    "backup.uploaded_files": "업로드한 파일",
    "backup.uploaded_groups": "폴더별 업로드 파일",
    "backup.uploaded_no": "Nextcloud 업로드: 아직 안 됨",
    "backup.uploaded_yes": "Nextcloud 업로드: 완료({})",
    "backup.vault": "보관소",
    "backup.vault_changed": "이 스냅샷 이후 보관소에서 노트 {}개 변경됨",
    "backup.zip_new": "새/갱신 ZIP {}개",
    "backup.zip_summary": "파일 {}개(노트 {}개), 압축 해제 시 {}",
    # --- details ---------------------------------------------------------------------------
    "detail.extra": "사용량 크레딧",
    "detail.local_header": "CLAUDE CODE · 이 PC · 이번 주 모델별 비율",
    "detail.off": "꺼짐",
    "detail.on": "켜짐",
    "detail.surface.oauth_apps": "연결된 앱",
    "detail.unlimited": "한도 없음",
    # --- sign-in dialog --------------------------------------------------------------------
    "dlg.cancel": "취소",
    "dlg.checking": "확인하는 중…",
    "dlg.err_badcode": "코드가 승인되지 않았어요.\n\n{}\n\n코드 전체를 붙여넣었는지 확인하거나, 브라우저 로그인을 다시 시도해 보세요(항상 새 코드가 필요해요).",
    "dlg.err_ratelimit": "짧은 시간에 로그인 시도가 너무 많았어요.\n\n서버가 일시적으로 제한하고 있어요. 이 창을 닫고 10–15분 기다린 뒤(그동안은 시도하지 마세요) 새 코드로 브라우저 로그인을 한 번만 다시 시작하세요.",
    "dlg.hint1": "열리는 페이지에서 로그인하고 접근을 허용하세요. 마지막에 코드를 받게 돼요.",
    "dlg.intro": "내 브라우저에서 claude.ai 계정에 로그인하세요(저장된 비밀번호와 패스키를 그대로 쓸 수 있어요).",
    "dlg.login_title": "로그인",
    "dlg.open_browser": "브라우저에서 로그인 열기",
    "dlg.paste_label": "받은 코드를 여기에 붙여넣으세요:",
    "dlg.paste_placeholder": "여기에 코드 붙여넣기",
    "dlg.signin": "로그인",
    "dlg.step1": "1단계",
    "dlg.step2": "2단계",
    "dlg.unknown_err": "알 수 없는 오류예요.",
    # --- errors ----------------------------------------------------------------------------
    "err.already_running": "앱이 이미 실행 중이에요(알림 영역을 확인하세요).",
    "err.bad_token_resp": "토큰 엔드포인트의 응답이 잘못됐어요",
    "err.bad_usage_resp": "사용량 엔드포인트의 응답이 잘못됐어요",
    "err.connection": "연결 오류: {}",
    "err.file_empty": "사용량 파일이 비어 있어요.",
    "err.file_not_found": "사용량 파일을 찾을 수 없어요.\nClaude Desktop이 실행 중인가요?",
    "err.file_unreadable": "지금은 사용량 파일을 읽을 수 없어요.",
    "err.loading": "로그인 / 조회 중…",
    "err.network": "네트워크 오류: {}",
    "err.no_code": "붙여넣은 코드가 없어요.",
    "err.no_data_profile": "이 프로필에는 데이터가 없어요.",
    "err.no_tray": "알림 영역을 사용할 수 없어 아이콘을 표시하지 않아요.",
    "err.no_usage_data": "사용량 데이터가 없어요.",
    "err.not_signed_in": "로그인되어 있지 않아요.",
    "err.query_http": "조회 오류(HTTP {}).",
    "err.rate_limited": "서버가 요청을 제한하고 있어요(429) – 자동으로 다시 시도해요.",
    "err.session_expired": "세션이 만료됐어요. 다시 로그인하세요.",
    "err.session_expired_nl": "세션이 만료됐어요.\n다시 로그인하세요.",
    "err.signin_needed": "claude.ai 로그인이 만료됐어요.\n다시 로그인하세요: 오른쪽 클릭 → claude.ai에 로그인",
    "err.unexpected": "예기치 않은 오류: {}",
    # --- "Message to the developer" window -------------------------------------------------
    "fb.cancel": "취소",
    "fb.close": "닫기",
    "fb.consent": "{}을 읽었으며 이에 동의합니다.",
    "fb.email": "이메일",
    "fb.email_hint": "답장을 원할 때만",
    "fb.err_consent": "보내려면 개인정보 처리방침에 동의해야 해요.",
    "fb.err_email": "이메일 주소가 올바르지 않은 것 같아요.",
    "fb.err_empty": "먼저 메시지를 쓰거나 평가를 선택하세요.",
    "fb.err_links": "메시지에 링크가 너무 많아요.",
    "fb.err_network": "claudeusagemonitor.com에 연결할 수 없어요. 연결 상태를 확인하고 다시 시도하세요.",
    "fb.err_rate": "짧은 시간에 메시지를 너무 많이 보냈어요 – 나중에 다시 시도하세요.",
    "fb.err_server": "지금은 서버가 메시지를 받을 수 없어요. 나중에 다시 시도하세요.",
    "fb.intro": "아이디어나 버그가 있나요, 아니면 그냥 마음에 드나요? 알려 주세요. 모든 메시지는 제작자인 저, Vidovics Gábor가 직접 읽어요.",
    "fb.message": "메시지",
    "fb.message_ph": "잘 되는 것, 안 되는 것, 아쉬운 것은 무엇인가요?",
    "fb.meta": "메시지와 함께 전송되는 정보: 프로그램 버전 {0}, 운영 체제({1}), 인터페이스 언어({2}).",
    "fb.name": "이름",
    "fb.optional": "(선택)",
    "fb.privacy_hide": "처리방침 숨기기",
    "fb.privacy_text": (
        "개인정보처리자: Vidovics Gábor, 개인(헝가리), Claude Usage Monitor의 제작자. "
        "전체 개인정보 처리방침은 웹사이트에서 확인할 수 있습니다: https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "전송되는 정보: 여기에 입력하는 내용 – 이름(선택), 이메일 주소(선택), 메시지, 별점 – 그리고 맥락을 "
        "파악하기 위한 프로그램 버전, 운영 체제의 이름과 버전, 인터페이스 언어, 전송 시각입니다. 서버는 IP 주소를 "
        "저장하지 않으며, 악용 방지를 위해 주소로 되돌릴 수 없는, 매일 바뀌는 해시값만 사용합니다."
        "\n\n"
        "목적: 귀하의 메시지를 읽고 답변하며 프로그램을 개선하기 위해서입니다(정당한 이익, GDPR 제6조 제1항 (f); "
        "답변 자체는 귀하의 요청에 따른 것입니다). 귀하의 평가와 이름은 별도의 확인란에 체크한 경우에만(동의, "
        "제6조 제1항 (a)), 그리고 제작자가 검토한 후에만 웹사이트에 게시되며, 이 동의는 언제든지 철회할 수 있습니다."
        "\n\n"
        "보유 기간: 메시지는 최대 2년, 게시된 평가는 동의를 철회할 때까지입니다. 제작자가 이메일 전달을 켜 둔 경우 "
        "사본이 제작자의 메일함에도 전달됩니다."
        "\n\n"
        "열람 주체: 개인정보처리자, 그리고 처리 수탁자로서 호스팅 제공업체(서버는 EU 내 독일에 위치)뿐입니다. "
        "어떤 정보도 판매하거나 제3자에게 제공하지 않으며, 프로파일링과 자동화된 의사 결정은 하지 않습니다."
        "\n\n"
        "귀하의 권리: 열람, 정정, 삭제, 처리 제한, 반대, 동의 철회, 그리고 감독 기관(헝가리: NAIH, naih.hu) 또는 "
        "귀하가 거주하는 국가의 감독 기관에 대한 불만 제기. 문의: 이 양식 또는 웹사이트."
        "\n\n"
        "전송: claudeusagemonitor.com으로 암호화(HTTPS/TLS)하여 전송됩니다. 이 처리방침의 버전: 2026-10-06."
    ),
    "fb.privacy_title": "개인정보 처리방침",
    "fb.publish": "내 평가와 이름(입력한 경우)을 claudeusagemonitor.com에 표시하는 데 동의합니다.",
    "fb.rating": "전체 평가",
    "fb.rating_clear": "지우기",
    "fb.rating_hint": "선택 – 별을 클릭하세요",
    "fb.rating_tip": "5점 만점에 {}점",
    "fb.secure": "암호화된 연결(HTTPS)로 claudeusagemonitor.com에 전송돼요.",
    "fb.send": "보내기",
    "fb.sending": "보내는 중…",
    "fb.sent": "고마워요 – 잘 도착했어요!",
    "fb.sent_sub": "모든 메시지를 읽어요. 이메일 주소를 남겼다면 그곳으로 답장할게요.",
    "fb.title": "개발자에게 메시지",
    # --- Help window -----------------------------------------------------------------------
    "help.disclaimer": "Anthropic이 만들거나 Anthropic과 제휴한 도구가 아닌, 독립적인 무료 도구예요. “Claude”는 Anthropic의 상표예요.",
    "help.feedback": "질문, 아이디어, 버그 신고: 웹사이트의 메시지 양식을 이용하세요.",
    "help.free": "영원히 무료 · MIT 라이선스 · 오픈 소스 · 텔레메트리 없음",
    "help.guide": (
        "\n"
        "<h2>위젯이 보여 주는 것</h2>\n"
        "<ul>\n"
        "<li><b>5시간 세션</b> – 현재 세션 한도를 얼마나 사용했는지 보여 줘요. 5시간마다 초기화되며, 위젯은 초기화까지 남은 시간을 카운트다운해요.</li>\n"
        "<li><b>주간 한도</b> – 모든 모델을 합친 사용량이에요. 계정별로 정해진 매주 같은 시각에 초기화돼요.</li>\n"
        "<li><b>모델별 주간 한도</b> – 서버가 보고하는 경우(예: 특정 모델)에 표시되는 세 번째 게이지예요.</li>\n"
        "<li><b>페이스와 소모율</b> – 한도를 얼마나 빨리 쓰고 있는지, 초기화 때까지 버틸 수 있는지 보여 줘요. 주 마감 예측이 미리 알려 줘요.</li>\n"
        "<li><b>사용량 크레딧</b>과 플랜 배지 – <i>플랜 배지 및 추가 한도</i>에서 켜면 표시돼요.</li>\n"
        "</ul>\n"
        "<h2>데이터 출처</h2>\n"
        "<ul>\n"
        "<li><b>claude.ai(모든 기기)</b> – Anthropic 서버에 조회하므로 휴대폰, 브라우저, 다른 컴퓨터에서 쓴 사용량까지 포함돼요. 내 브라우저에서 한 번만 로그인하면 돼요(메뉴: <i>로그인</i>). 2분마다 새로 고치며, 서버가 요청하면 간격이 길어져요.</li>\n"
        "<li><b>로컬(이 PC만)</b> – 이 컴퓨터에 있는 Claude Desktop의 사용량 로그를 읽어요. 로그인은 필요 없지만 이 PC의 사용량만 알 수 있어요.</li>\n"
        "</ul>\n"
        "<p>메뉴의 <i>데이터 소스</i>에서 전환할 수 있어요.</p>\n"
        "<h2>위젯 사용법</h2>\n"
        "<ul>\n"
        "<li>위젯(또는 알림 영역 아이콘)을 <b>오른쪽 클릭</b> – 전체 메뉴가 열려요.</li>\n"
        "<li>게이지를 <b>더블 클릭</b> – <b>기록</b> 창이 열려요: 6시간, 24시간, 7일 또는 전체 기간을 최고치, 일평균, 예측과 함께 볼 수 있어요.</li>\n"
        "<li><b>끌어서</b> 옮길 수 있고, 화면 가장자리에 달라붙어요. <b>Ctrl + 마우스 휠</b> – 크게 또는 작게.</li>\n"
        "<li>레이아웃: 포스트잇 카드, 슬림 바, 링. 테마 6종. <i>위치 잠금</i>과 <i>클릭 통과</i>는 설정에 있어요.</li>\n"
        "</ul>\n"
        "<h2>알림</h2>\n"
        "<p>70%부터 노란색, 90%부터 빨간색이에요(조정 가능). 한도가 초기화될 때와 데이터가 오래될 때 알림을 받도록 선택할 수 있어요.</p>\n"
        "<h2>백업(선택)</h2>\n"
        "<p>작은 표시등은 예약된 백업이 실행되고 완료됐는지 보여 줘요. 표시등을 클릭하면 세부 정보가 열려요. 모니터는 백업 로그를 읽기만 해요 – 백업을 만들고 테스트하는 일은 직접 챙겨야 해요(이용약관 참조).</p>\n"
        "<h2>업데이트</h2>\n"
        "<p>프로그램이 스스로 새 버전을 확인하고 한 번의 클릭으로 업데이트해요. 모든 패키지는 SHA-256으로 검증되며 <b>claudeusagemonitor.com</b>에서만 받아요. 새 버전과 릴리스 노트: {site}</p>\n"
        "<h2>개인정보 보호</h2>\n"
        "<p>텔레메트리도, 추적도 없어요. claude.ai 로그인 정보는 이 컴퓨터에만 암호화되어 저장되고, 다른 곳으로는 아무것도 보내지 않아요.</p>\n"
        "<h2>문제가 있을 때</h2>\n"
        "<ul>\n"
        "<li><i>429 / 요청 제한</i> – 서버가 요청 속도를 늦추고 있어요. 프로그램이 알아서 다시 시도해요.</li>\n"
        "<li>데이터 없음 – <i>데이터 소스</i>를 확인하세요. claude.ai라면 다시 로그인하세요.</li>\n"
        "<li>기록은 7일 동안 보관되며, 다시 시작하거나 업데이트해도 유지돼요.</li>\n"
        "<li>로그와 설정: <code>{cfg}</code>(<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "만든 사람",
    "help.moved": "2026년 9월 21일부터 새 주소를 사용해요 – 이전 dinorr.hu/claude-usage-monitor 페이지는 이곳으로 리디렉션돼요.",
    "help.official": "공식 웹사이트",
    "help.open_site": "claudeusagemonitor.com 열기",
    "help.privacy": "개인정보 처리방침",
    "help.site_what": "다운로드, 자동 업데이트, 새로운 기능, Claude Backup Kit, 이용약관과 개인정보 보호 – 모두 한곳에 있어요.",
    "help.source_code": "소스 코드(GitHub)",
    "help.tab_author": "제작자",
    "help.tab_guide": "사용 방법",
    "help.terms": "이용약관",
    "help.title": "도움말",
    "help.version": "버전",
    # --- History window --------------------------------------------------------------------
    "hist.legend_5h": "5시간 세션",
    "hist.legend_week": "주간 한도",
    "hist.no_data": "이 기간에는 데이터가 충분하지 않아요.",
    "hist.range_24h": "24시간",
    "hist.range_6h": "6시간",
    "hist.range_7d": "7일",
    "hist.range_all": "전체",
    "hist.stat_burn": "일평균 소모",
    "hist.stat_forecast": "주 마감 예측",
    "hist.stat_now": "현재 주간 사용량",
    "hist.stat_peak": "주간 최고치",
    "hist.stat_sessions": "5시간 세션",
    "hist.title": "기록",
    # --- layouts ---------------------------------------------------------------------------
    "layout.compact": "슬림 바",
    "layout.postit": "포스트잇 카드",
    "layout.ring": "링",
    # --- context menu ----------------------------------------------------------------------
    "menu.always_top": "항상 위에 표시",
    "menu.autostart": "Windows 시작 시 자동 실행",
    "menu.backup_bar": "백업 상태 표시줄",
    "menu.backups": "백업…",
    "menu.check_update": "프로그램 업데이트 확인…",
    "menu.click_through": "클릭 통과",
    "menu.details": "플랜 배지 및 추가 한도",
    "menu.feedback": "개발자에게 메시지 보내기…",
    "menu.help": "도움말…",
    "menu.history": "기록 및 통계…",
    "menu.language": "언어",
    "menu.layout": "레이아웃",
    "menu.locked": "위치 잠금",
    "menu.login": "로그인(claude.ai, 브라우저)…",
    "menu.logout": "로그아웃",
    "menu.model_gauge": "{} 게이지",
    "menu.order": "순서",
    "menu.panel_visible": "패널 표시",
    "menu.quit": "끝내기",
    "menu.refresh": "사용량 데이터 지금 새로 고침",
    "menu.settings": "설정…",
    "menu.size": "크기",
    "menu.source": "데이터 소스",
    "menu.start_menu": "시작 메뉴에 표시",
    "menu.theme": "테마",
    "menu.update_available": "프로그램 업데이트: {} 버전 설치…",
    # --- desktop notifications -------------------------------------------------------------
    "notify.autostart_fail": "자동 실행을 설정하지 못했어요.",
    "notify.autostart_off": "꺼짐: 앱이 Windows 시작 시 실행되지 않아요.",
    "notify.autostart_on": "켜짐: 앱이 Windows 시작 시 자동으로 실행돼요.",
    "notify.first_run": "패널이 화면 오른쪽 위에 나타났어요.\n패널이나 알림 영역 아이콘을 오른쪽 클릭하면 메뉴가 열려요.",
    "notify.login_ok": "로그인했어요 – 서버 데이터를 가져오고 있어요.",
    "notify.logout": "로그아웃했어요. 로컬 소스로 전환했어요.",
    "notify.reset_done": "{}: 초기화됐어요 — 새 기간이 시작됐어요.",
    "notify.signin_needed": "claude.ai 로그인이 만료됐어요. 모든 기기의 사용량을 계속 보려면 패널을 오른쪽 클릭하고 다시 로그인하세요.",
    "notify.stale_body": "마지막 측정이 {} 전이에요. Claude Desktop이 실행 중인가요?",
    "notify.stale_title": "오래된 데이터",
    "notify.threshold": "{}: {}% 사용했어요.",
    "notify.update": "프로그램 {} 버전을 사용할 수 있어요. 패널을 오른쪽 클릭하고 프로그램 업데이트를 선택하세요.",
    # --- panel labels (tight space) --------------------------------------------------------
    "panel.five_hour": "5시간 세션",
    "panel.five_hour_short": "5시간",
    "panel.full_in": "소진: {}",
    "panel.model": "{} 주간",
    "panel.no_data": "데이터 없음",
    "panel.pace": "페이스 대비 {}",
    "panel.per_day": "{}%/일",
    "panel.per_hour": "{}%/시간",
    "panel.refreshing": "불러오는 중",
    "panel.reset": "초기화 {}",
    "panel.retry_in": "{}초 후 재시도",
    "panel.updated": "갱신: {}",
    "panel.week_short": "주간",
    "panel.weekly": "주간 한도",
    # --- profile ---------------------------------------------------------------------------
    "profile.extra": "사용량 크레딧: {}",
    "profile.plan": "플랜: {}",
    "profile.since": "가입일: {}",
    "profile.tier": "사용 한도 등급: {}",
    # --- Settings window -------------------------------------------------------------------
    "set.about": "{}\n텔레메트리는 없어요. Anthropic에 내 사용량만 요청하고, 업데이트 서버에서 버전 번호만 읽어요.",
    "set.accent": "강조 색상",
    "set.always_top": "다른 모든 창 위에 표시",
    "set.auto": "자동",
    "set.backup_config": "백업 스크립트 구성",
    "set.backup_details": "세부 정보 창에 표시",
    "set.backup_disclaimer": "Claude Usage Monitor는 백업 로그를 읽어 표시할 뿐이며, 어떤 백업도 생성하거나 검사하거나 보장하지 않습니다. Claude Backup Kit은 도움을 드리고자 무료로 제공하는 출발점입니다. 누구나 스크립트를 수정할 수 있으므로 백업의 품질과 완전성은 보장할 수 없습니다. 백업, 데이터 손실 또는 그 밖의 어떠한 손해에 대해서도 책임을 지지 않습니다. 백업이 완전하고 복원 가능한지 확인하는 것은 각자의 책임입니다. 때때로 복원을 직접 테스트해 보시기 바랍니다.",
    "set.backup_disclaimer_h": "면책 조항",
    "set.backup_enabled": "패널에 백업 상태 표시줄 표시",
    "set.backup_found": "찾음: {}",
    "set.backup_green": "녹색: 최대",
    "set.backup_label": "표시등 옆 레이블",
    "set.backup_lamps": "표시등",
    "set.backup_root": "백업 폴더",
    "set.backup_tasks": "예약된 작업 필터",
    "set.backup_unconfigured": "백업 폴더가 설정되지 않아 상태 표시줄이 숨겨져 있어요. 백업 스크립트가 기록하는 폴더를 선택하세요.",
    "set.backup_yellow": "노란색: 최대",
    "set.browse": "찾아보기…",
    "set.click_through": "클릭 통과(장식용, 마우스 무시)",
    "set.close": "닫기",
    "set.color_hint": "색상은 임계값에 따라 바뀌어요: 녹색 → 노란색 → 빨간색.",
    "set.danger": "위험",
    "set.data_hint": "로컬 로그: Claude Desktop의 plan-usage-history.json. 로그인이 필요 없지만 이 PC만 측정하고 약 5분마다 새로 고쳐요.\n\nclaude.ai: 로그인 후 서버에 조회해요. 모든 기기의 사용량을 정확한 초기화 시각과 함께 더 자주 볼 수 있어요.",
    "set.datafile": "데이터 파일",
    "set.default": "기본값",
    "set.details_api_only": "이 항목은 claude.ai 데이터 소스에서 가져와요(로그인 필요). 로컬 로그에는 들어 있지 않아요.",
    "set.file_filter": "JSON (*.json);;모든 파일 (*.*)",
    "set.gauge_order": "게이지 순서",
    "set.hours_suffix": "시간",
    "set.layout": "레이아웃",
    "set.local_models_hint": "서버는 일부 모델(예: Fable)에 대해서만 별도 카운터를 유지해요. 나머지 모델에 대해서는 이번 주 이 PC에서 한 Claude Code 작업이 어떻게 나뉘는지를 보여 줘요 – 한도의 비율이 아니라 내 사용량의 비율과 출력 토큰이에요. 모델 이름과 토큰 수만 읽고, 대화 내용은 절대 읽지 않아요.",
    "set.local_models_none": "Claude Code 로그 폴더를 찾지 못해 이 그룹은 숨겨져 있어요. 다른 기능에는 영향이 없어요.",
    "set.local_models_path": "Claude Code 로그 폴더",
    "set.lock": "위치 잠금(끌 수 없음)",
    "set.login_btn_in": "claude.ai에서 로그아웃",
    "set.login_btn_out": "claude.ai에 로그인…",
    "set.model_filter": "추적할 모델",
    "set.model_scale": "모델 게이지 크기",
    "set.not_set": "설정 안 됨",
    "set.notify_enabled": "임계값을 넘으면 알림",
    "set.notify_reset": "한도가 초기화되면 알림",
    "set.notify_stale": "데이터가 오래되면 알림",
    "set.opacity": "불투명도",
    "set.open_config": "설정 폴더 열기",
    "set.pick_color": "색상 선택…",
    "set.pick_file_title": "사용량 로그 선택",
    "set.profile": "프로필 / 계정",
    "set.profile_auto": "자동(마지막 사용)",
    "set.profile_n": "프로필 {} – …{}",
    "set.refresh": "새로 고침",
    "set.reset_confirm": "기본 설정으로 되돌릴까요?",
    "set.restore": "기본값 복원",
    "set.rows_available": "지금 표시할 수 있는 항목이에요 – 보고 싶지 않은 항목은 선택을 해제하세요:",
    "set.rows_none": "지금은 서버가 이 계정에 추가 한도를 보내지 않아요. 보내기 시작하면 여기에 자동으로 나타나요.",
    "set.sec_suffix": "초",
    "set.show_age": "데이터 갱신 시각",
    "set.show_burn": "소모율(%/시간, %/일)",
    "set.show_extra_usage": "사용량 크레딧(종량제)",
    "set.show_feedback_icon": "패널 머리글에 메시지 아이콘",
    "set.show_five_hour": "5시간 세션 표시",
    "set.show_local_models": "이 PC의 Claude Code 로그로 본 모델별 비율",
    "set.show_model": "모델 주간 한도 표시(claude.ai 소스)",
    "set.show_model_list": "다른 모델의 주간 한도",
    "set.show_plan_badge": "머리글에 플랜 배지(Pro / Max…)",
    "set.show_plan_name": "배지에 내 이름 표시",
    "set.show_reset": "초기화까지 카운트다운",
    "set.show_spark": "추세 곡선(스파크라인)",
    "set.show_surfaces": "사용 환경별 한도(Claude Code, 연결된 앱…)",
    "set.show_weekly": "주간 한도 표시",
    "set.size": "크기",
    "set.snap": "화면 가장자리에 맞추기",
    "set.source_api": "claude.ai – 모든 기기(로그인 필요)",
    "set.source_label": "측정 소스",
    "set.source_local": "로컬 로그 – 이 PC만",
    "set.tab_alerts": "알림",
    "set.tab_appearance": "모양",
    "set.tab_content": "내용",
    "set.tab_data": "데이터 소스",
    "set.tab_details": "세부 정보",
    "set.tab_system": "시스템",
    "set.taskbar": "작업 표시줄에 표시(창으로)",
    "set.theme": "테마",
    "set.theme_default": "테마 기본값",
    "set.tip": "팁: 왼쪽 버튼으로 패널을 끌어 옮기고, Ctrl+스크롤로 크기를 바꿔요.\n오른쪽 클릭 = 메뉴, 더블 클릭 = 기록.",
    "set.title": "설정",
    "set.tray_five": "5시간 세션",
    "set.tray_max": "더 높은 값",
    "set.tray_value": "알림 영역 아이콘 값",
    "set.tray_weekly": "주간 한도",
    "set.update_check": "프로그램 업데이트 자동 확인",
    "set.version": "버전",
    "set.visible": "플로팅 패널 표시",
    "set.warn": "주의",
    # --- sizes -----------------------------------------------------------------------------
    "size.extra": "특대",
    "size.large": "크게",
    "size.normal": "보통",
    "size.small": "작게",
    # --- data sources ----------------------------------------------------------------------
    "source.api": "claude.ai(모든 기기)",
    "source.local": "로컬(이 PC만)",
    # --- themes ----------------------------------------------------------------------------
    "theme.claude": "Claude(따뜻한 다크)",
    "theme.graphite": "그래파이트",
    "theme.midnight": "미드나이트 글라스",
    "theme.neon": "네온",
    "theme.paper": "라이트 페이퍼",
    "theme.postit": "포스트잇 옐로",
    # --- time units ------------------------------------------------------------------------
    "time.day": "{}일",
    "time.dh": "{}일 {}시간",
    "time.hm": "{}시간 {}분",
    "time.hour": "{}시간",
    "time.m": "{}분",
    "time.min": "{}분",
    "time.none": "데이터 없음",
    "time.sec": "{}초",
    # --- tray tooltip ----------------------------------------------------------------------
    "tray.head": "5시간: {}%   ·   주간: {}%",
    "tray.line": "{}: {}%",
    # --- updater ---------------------------------------------------------------------------
    "update.available": "{} 버전을 사용할 수 있어요.",
    "update.check_failed": "업데이트를 확인할 수 없어요: {}",
    "update.check_now": "지금 확인",
    "update.checking": "업데이트 확인 중…",
    "update.downloading": "다운로드 중… {} / {}",
    "update.failed": "업데이트에 실패했어요: {}",
    "update.install": "지금 설치",
    "update.installed": "설치된 버전: {}",
    "update.later": "나중에",
    "update.manual": "이 복사본은 스스로 업데이트할 수 없어요(소스에서 실행 중이거나 읽기 전용 폴더에 있음). 대신 새 패키지를 다운로드하세요.",
    "update.open_page": "다운로드 페이지 열기",
    "update.restarting": "설치 중 – 잠시 후 앱이 다시 시작돼요.",
    "update.skip": "이 버전 건너뛰기",
    "update.title": "프로그램 업데이트",
    "update.uptodate": "최신 버전을 사용하고 있어요.",
    "update.verifying": "검증하고 압축을 푸는 중…",
    "update.whats_new": "새로운 기능",
}

# macOS wording: "start at login" (Apple: 로그인 시 열기) instead of "start with Windows", menu bar
# (메뉴 막대) instead of the notification area.
STRINGS_MAC = {
    "menu.autostart": "로그인 시 열기",
    "notify.autostart_on": "켜짐: 로그인하면 앱이 자동으로 실행돼요.",
    "notify.autostart_off": "꺼짐: 로그인 시 앱이 실행되지 않아요.",
    "notify.first_run": "패널이 화면 오른쪽 위에 나타났어요.\n패널이나 메뉴 막대 아이콘을 오른쪽 클릭하면 메뉴가 열려요.",
}
