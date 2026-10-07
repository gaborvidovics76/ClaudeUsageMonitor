# Review notes – 한국어 (ko)

Module: `claude_usage/langs/ko.py` – 358 keys + 4 macOS keys. `python tools/check_i18n.py ko` → `check_i18n: OK`
(the warnings are only the untranslatable Latin names: PC, Cowork, Vidovics Gábor, file names, URLs).

Form of address: friendly polite **해요체** for messages, notifications, hints and the help text; nouns for labels and
menu items; short verb nouns for buttons; formal **합니다체** for the privacy notice, the backup disclaimer and the two
consent checkboxes. Privacy document name: **개인정보 처리방침** (the term of 개인정보 보호법 제30조 and of every large
Korean platform; see `glossary-ko.md`).

## The texts I am least sure about

| # | Key | Korean | Why |
|---|---|---|---|
| 1 | `panel.per_hour` | `{}%/시간` | One character wider than the English `{}%/h`. Korean has no accepted one-letter abbreviation for "hour" (`시` alone reads as "o'clock"). The Hungarian source (`{}%/óra`) is also longer, so I kept the clear form. If the panel clips, `{}%/h` would be understood by Korean users too. |
| 2 | `panel.pace` | `페이스 대비 {}` | Wider than `{} vs pace` because the value has to come last in Korean (「페이스 대비 +5%」). A shorter `{} / 페이스` would be unnatural. |
| 3 | `panel.full_in` | `소진: {}` | "full" = the moment the limit is used up. Literal 「가득」 would sound like a container; 「소진」 (exhausted) is what Korean usage dashboards say. |
| 4 | `hist.stat_forecast` | `주 마감 예측` | "End-of-week projection". 「주말」 would mean *weekend*, so I used 「주 마감」 (close of the week). |
| 5 | `backup.level_yellow` | `조금 오래됨` | "Getting old" has no idiomatic one-word equivalent; 「조금 오래됨」 ("somewhat old") sits between 「최신」 and 「오래됨」. |
| 6 | `set.hours_suffix`, `set.sec_suffix` | `시간`, `초` (no leading space) | The English has ` h` / ` s` with a space; Korean attaches the unit to the digit (24시간, 30초) per 국립국어원, so the space is deliberately dropped. The labels before the spin boxes read 「녹색: 최대 [24시간]」. |
| 7 | `fb.consent` | `{}을 읽었으며 이에 동의합니다.` | The particle 을 is correct only because the placeholder is always 「개인정보 처리방침」 (ends in a consonant). If the inserted text ever changes, the particle must be checked. |
| 8 | `notify.update`, `update.available` | `프로그램 버전 {} 사용 가능 – …`, `버전 {} 사용 가능.` | Rebuilt as noun phrases so that no particle follows the version number (「2.3.1을/를」 would need a lookup). Slightly terser than the English sentence. |
| 9 | `menu.quit` | `끝내기` | Microsoft's term for Exit/Quit in menus; many Korean tray apps use 「종료」. Both are fine; I followed Microsoft as the brief asks. |
| 10 | `fb.privacy_text` | GDPR citations `GDPR 제6조 제1항 (f)` | Korean legal texts cite the GDPR by its English acronym (no official Korean name), with article/paragraph in Korean style and the letter in parentheses. The supervisory authority is kept as "NAIH or the authority of your own country" (귀하가 거주하는 국가의 감독 기관); the Korean PIPC is not named, as the brief allows. |

## en / hu differences noticed

- `fb.privacy_text`: the Hungarian links to `/hu/#privacy`; I followed the English `/#privacy`.
- `menu.help`: hu `Súgó (HELP)…`, en `Help…` – followed the English (`도움말…`).
- `menu.locked`: hu is a state (`Pozíció rögzítve`), en an action (`Lock position`) – followed the English (`위치 잠금`).
- `set.show_extra_usage`: hu repeats the English term in parentheses; the Korean uses 「종량제」 for pay-as-you-go instead.
- `help.guide` "Alerts": the English writes `70 %` with a space; Korean typography attaches the percent sign (`70%`).

## Lektor

Independent native review. Overall the translation was already idiomatic and consistent with the glossary; 17
edits in 13 keys, plus the glossary note on version placeholders and the Kit particle.

- `set.backup_disclaimer`: `Claude Backup Kit는` → `Claude Backup Kit은` – Kit(킷) ends in consonant.
- `set.backup_disclaimer`: `도움을 드리기 위해 제공하는 무료 출발점` → `도움을 드리고자 무료로 제공하는 출발점` – smoother legal register.
- `set.backup_disclaimer`: `백업, 데이터 손실 및 그로 인한 어떠한 손해` → `백업, 데이터 손실 또는 그 밖의 어떠한 손해` – "any damage", no added causation.
- `set.backup_disclaimer`: `때때로 복원을 직접 테스트해 보세요.` → `때때로 복원을 직접 테스트해 보시기 바랍니다.` – keep 합니다체 throughout.
- `backup.tip_click`: `클릭하면 자세히 볼 수 있어요` → `클릭하여 자세히 보기` – tooltip style, noun phrase.
- `err.no_tray`: `…알림 영역 아이콘을 건너뛰어요.` → `…아이콘을 표시하지 않아요.` – "건너뛰다" unnatural; no repetition.
- `fb.secure`: `claudeusagemonitor.com과 암호화된 연결(HTTPS)이에요.` → `암호화된 연결(HTTPS)로 claudeusagemonitor.com에 전송돼요.` – awkward copula, now natural.
- `help.disclaimer`: `독립적인 무료 도구이며, Anthropic이 만들지 않았고 Anthropic과 제휴 관계도 없어요.` → `Anthropic이 만들거나 Anthropic과 제휴한 도구가 아닌, 독립적인 무료 도구예요.` – one clause, less clunky.
- `help.guide`: `계정에 정해진 주간 시각에 초기화돼요` → `계정별로 정해진 매주 같은 시각에 초기화돼요` – "주간 시각" not idiomatic.
- `help.guide`: `서버가 요청하면 더 느리게 새로 고쳐요` → `서버가 요청하면 간격이 길어져요` – avoid repeated 새로 고치다.
- `help.guide`: `이 PC만 알아요` → `이 PC의 사용량만 알 수 있어요` – calque of "only knows".
- `help.guide`: `사용자의 몫이에요` → `직접 챙겨야 해요` – no third-person 사용자 address.
- `hist.stat_now`: `현재 주간` → `현재 주간 사용량` – bare adjective-noun was incomplete.
- `menu.refresh`: `지금 사용량 데이터 새로 고침` → `사용량 데이터 지금 새로 고침` – adverb next to verb noun.
- `menu.update_available`: `프로그램 업데이트: 버전 {} 설치…` → `프로그램 업데이트: {} 버전 설치…` – natural Korean "2.3.1 버전".
- `notify.update`: `프로그램 버전 {} 사용 가능 – …` → `프로그램 {} 버전을 사용할 수 있어요. …` – full 해요체 sentence, particle on 버전.
- `update.available`: `버전 {} 사용 가능.` → `{} 버전을 사용할 수 있어요.` – full sentence, particle-safe.
- `glossary-ko.md`: placeholder rule now says "version before 버전" and records the Kit은 particle.

Still in doubt:
- `panel.per_hour` `{}%/시간` stays wider than `{}%/h`; if the panel clips, `{}%/h` is the fallback (Korean users read it).
- `panel.pace` `페이스 대비 {}` – also wider than the English; I know no shorter natural form.
- `fb.sent` `고마워요` is friendly but slightly casual from a developer to a user; `감사해요` would be the safer choice if the author prefers it.
- `backup.state_error` `오류와 함께 종료됨` follows Windows' own wording (「오류와 함께 완료되었습니다」), so I kept it even though it is close to a calque.
