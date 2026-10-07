# Glossary – 한국어 (ko)

Claude Usage Monitor UI, Korean localisation. One fixed translation per term; the module
`claude_usage/langs/ko.py` follows this list.

## Tone and form of address

- **Messages, notifications, hints, help text: 해요체** (friendly polite), e.g. 「로그인했어요」,
  「세션이 만료됐어요. 다시 로그인하세요.」 This is the register of consumer software in Korea
  (Toss, Kakao, Naver, Apple Korea). The user is never called 당신/귀하; when a possessive is
  unavoidable, 「내」 is used (「배지에 내 이름 표시」) – the way Windows and iOS do it.
  Instructions use the polite imperative 「…하세요」, never 「…하십시오」 (too stiff) or 「…해」.
- **Labels and menu items: nouns** (「주간 한도」, 「데이터 소스」, 「기록 및 통계…」).
- **Buttons: short verb nouns** (보내기, 취소, 닫기, 찾아보기…, 새로 고침, 지금 설치, 끝내기).
- **Legal texts** (`fb.privacy_text`, `set.backup_disclaimer`) and the two consent checkboxes
  (`fb.consent`, `fb.publish`): formal 합니다체, as every Korean privacy document and consent
  statement is written. 「귀하」 appears only inside the privacy notice, where it is the standard
  legal term for the data subject.
- Spacing per 국립국어원: digit + unit attached (5시간, 24시간, {}분, {}개, 70%); parentheses
  attached to the preceding word (클릭 통과(장식용…), 로그인(claude.ai, 브라우저)…); auxiliary
  verbs spaced (보여 줘요, 알려 주세요); 「새로 고침」 with a space (Microsoft spelling).
  Because the unit is attached, the Qt spin-box suffixes are 「시간」 and 「초」 without the
  leading space the English has (「24시간」, not 「24 시간」).
- Half-width digits and punctuation; ellipsis is the single character 「…」; en dash 「–」 and
  em dash 「—」 kept as in the English; quotation marks 「“ ”」 kept.
- Loanwords per 외래어 표기법: 세션, 페이스, 게이지, 스냅샷, 스파크라인, 포스트잇, 옐로, 그래파이트,
  텔레메트리, 라이선스, 프로파일링, 리디렉션, 슬림, 레이아웃, 카운트다운.
- Particles after untranslated names follow the pronunciation of the name: claude.ai에 / claude.ai에서,
  Anthropic의 / Anthropic이, Claude Desktop이, OneDrive에, Nextcloud 업로드, Fable의. Where a
  placeholder may end in a digit or a name of unknown ending (version numbers, limit names), the
  sentence is rebuilt so that no particle follows the placeholder: version numbers go before the noun
  「버전」, which then carries the particle (「{} 버전을 사용할 수 있어요」, 「{} 버전 설치…」), and limit
  names are followed by a colon (「{}: 초기화됐어요」).
- 「Claude Backup Kit」 is read 「킷」, so it takes 은/이 (「Claude Backup Kit은」).

## Privacy document name

**개인정보 처리방침** (`fb.privacy_title`, `help.privacy`). This is the term required by the
Personal Information Protection Act (개인정보 보호법 제30조 「개인정보 처리방침」), used by the
Personal Information Protection Commission (개인정보보호위원회) and by every large Korean platform
(Naver, Kakao, Coupang, Samsung, Apple Korea, Microsoft Korea). Older sites use 「개인정보
취급방침」; that wording was replaced in the Act in 2011 and is no longer used. Inside the notice
the controller is called 개인정보처리자 (the Act's own term, written without a space) and the
processor 처리 수탁자. GDPR stays 「GDPR」 (Korean legal texts cite it by the English acronym);
articles are cited as 「GDPR 제6조 제1항 (f)」. The supervisory authority stays as the English has
it: NAIH (Hungary) or the authority of the user's own country – the Korean PIPC is not named
because the controller is in Hungary.

## Fixed terms

| English | 한국어 | Note |
|---|---|---|
| 5-hour session | 5시간 세션 | panel label 5시간 세션, short 5시간 |
| weekly limit | 주간 한도 | panel 주간 한도, short 주간 |
| per-model weekly limit | 모델별 주간 한도 | |
| limit | 한도 | never 제한 for a quota |
| reset (of a limit) | 초기화 | 「초기화 {}」 on the panel, 「한도가 초기화되면 알림」 |
| full (limit exhausted) | 소진 | panel 「소진: {}」 |
| pace | 페이스 | 「페이스 대비 {}」 |
| burn rate | 소모율 | 「소모율(%/시간, %/일)」 |
| usage | 사용량 | |
| usage credits | 사용량 크레딧 | pay-as-you-go = 종량제 |
| usage file / usage log | 사용량 파일 / 사용량 로그 | |
| plan / plan badge | 플랜 / 플랜 배지 | the word claude.ai uses in Korean |
| gauge | 게이지 | |
| panel / floating panel | 패널 / 플로팅 패널 | |
| widget | 위젯 | help text only |
| header (of the panel) | 머리글 | Microsoft term |
| tray / tray icon (Windows) | 알림 영역 / 알림 영역 아이콘 | Microsoft term for the notification area |
| menu bar (macOS) | 메뉴 막대 | Apple term, STRINGS_MAC only |
| taskbar | 작업 표시줄 | Microsoft |
| Start menu | 시작 메뉴 | Microsoft |
| start with Windows | Windows 시작 시 자동 실행 | |
| start at login (macOS) | 로그인 시 열기 | Apple's 「로그인 시 열기」 |
| sign in / sign out | 로그인 / 로그아웃 | Microsoft; never 접속 |
| quit | 끝내기 | Microsoft menu term |
| settings | 설정 | |
| notification | 알림 | |
| alert(s) (tab, help section) | 알림 | Korean apps use one word for both |
| threshold | 임계값 | Microsoft |
| Warning / Critical (thresholds) | 주의 / 위험 | the Korean traffic-light terms |
| backup | 백업 | |
| backup status bar | 백업 상태 표시줄 | |
| lamp | 표시등 | the little status lights |
| data source | 데이터 소스 | Office says 데이터 원본, but 소스 is the consumer word and keeps 「측정 소스」 natural |
| measurement source | 측정 소스 | |
| local log | 로컬 로그 | |
| profile / account | 프로필 / 계정 | |
| theme | 테마 | |
| layout | 레이아웃 | 포스트잇 카드 / 슬림 바 / 링 |
| size | 크기 | Small/Normal/Large/Extra = 작게/보통/크게/특대 |
| opacity | 불투명도 | |
| accent color | 강조 색상 | |
| always on top | 항상 위에 표시 | |
| lock position | 위치 잠금 | |
| click-through | 클릭 통과 | |
| snap to screen edge | 화면 가장자리에 맞추기 | |
| update (program) | 업데이트 | 프로그램 업데이트 |
| check for updates | 업데이트 확인 | |
| What's new | 새로운 기능 | |
| history | 기록 | window 기록, menu 기록 및 통계… |
| projection / forecast | 예측 | end-of-week projection = 주 마감 예측 |
| trend curve (sparkline) | 추세 곡선(스파크라인) | |
| stale data | 오래된 데이터 | |
| data freshness | 데이터 갱신 시각 | |
| refresh | 새로 고침 | Microsoft spelling with a space |
| fetch / query | 불러오기 / 조회 | |
| message to the developer | 개발자에게 메시지 | menu: 개발자에게 메시지 보내기… |
| rating / star rating | 평가 / 별점 | 「전체 평가」, 「5점 만점에 {}점」 |
| privacy notice / policy | 개인정보 처리방침 | see above |
| consent | 동의 | 「동의합니다」, 「동의 철회」 |
| terms of use | 이용약관 | |
| disclaimer | 면책 조항 | |
| controller / processor | 개인정보처리자 / 처리 수탁자 | PIPA wording |
| supervisory authority | 감독 기관 | |
| snapshot | 스냅샷 | |
| vault (Obsidian) | 보관소 | Obsidian's own Korean UI term |
| note (Obsidian) | 노트 | |
| scheduled task | 예약된 작업 | Windows Task Scheduler |
| log file | 로그 파일 | |
| folder | 폴더 | |
| connected apps | 연결된 앱 | |
| per-surface limits | 사용 환경별 한도 | Claude Code, connected apps… |
| rate-limit tier | 사용 한도 등급 | |
| member since | 가입일 | |
| telemetry | 텔레메트리 | |
| open source | 오픈 소스 | |
| right-click / double-click | 오른쪽 클릭 / 더블 클릭 | Microsoft: 마우스 오른쪽 단추 클릭 → shortened to 오른쪽 클릭 in the panel |
| Ctrl + mouse wheel | Ctrl + 마우스 휠 | |
| time units | 초 / 분 / 시간 / 일 | attached to the digit: {}초, {}분, {}시간, {}일 |
| no data | 데이터 없음 | |
| on / off | 켜짐 / 꺼짐 | |
| done / failed | 완료 / 실패 | backup results |
