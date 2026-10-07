# Review notes – Português (Brasil) (pt-BR)

Module: `claude_usage/langs/pt_BR.py` – 358 keys + 4 macOS keys, `check_i18n: OK` (17 warnings, all "identical to
English" on units, product words and loanwords: `{}d`, `{}h`, `{} h`, ` s`, `Backups`, `Layout`, `Extra`, `Normal`,
`Neon`, `5H`, `{}%/h` – these are the correct Brazilian forms). Form of address: **você** (mostly implicit, imperative
in the 3rd person: "Verifique", "Cole", "Entre novamente"). Privacy document: **Política de Privacidade**.

Texts I am least sure about:

1. **panel.reset** – `zera {}` instead of the loanword `reset {}`. "Zera" (verb: resets to zero) is what Brazilians
   actually say about limits ("o limite zera às 15h"), it fits the space (7 vs 8 chars) and avoids an untranslated
   English word on the panel. Everywhere else the formal "redefinição / redefinido" is used (Microsoft term). If a
   noun is preferred on the panel, `reset {}` is the fallback (it would only produce a checker warning).
2. **panel.* length** – five labels are 1–3 characters longer than the English: `cheio: {}` (+1), `{} SEMANAL` (+1),
   `Sem dados` (+2), `{} vs ritmo` (+1), `atualizado: {}` (+3), `repete em {} s` (+1), `LIMITE SEMANAL` (+2). The
   Hungarian source has the same or larger overruns on these keys, and the old pt-PT texts used `{} SEMANAL` /
   `LIMITE SEMANAL` already, so they are known to render. Shorter alternatives if needed: `{} SEM.`, `LIMITE SEM.`,
   `atual.: {}`.
3. **time.hm / time.m / backup.age_m** – `{}h {}min`, `{}min` (2 chars longer than the English `{}h {}m`). The binding
   note asks for the units s, min, h, d; "2h 30m" is not used in Brazil (ABNT: "min"). Kept `min`.
4. **panel.retry_in** – `repete em {} s` ("repeats in 5 s"). "Nova tentativa em {} s" is the full phrase but far too
   long for the panel. Alternative of the same length: `tenta em {} s`.
5. **fb.privacy_text, article citation** – `art. 6(1)(f) do GDPR (RGPD)` / `art. 6(1)(a)`. The "(RGPD)" is added once
   as the Portuguese name of the regulation; the acronym stays GDPR everywhere else, and the text does not claim
   LGPD compliance. LGPD vocabulary is used only where it is the natural Brazilian legal term (controlador,
   operador, autoridade de controle, tratamento, eliminação). "A autoridade do seu país" kept as asked. The URL is
   the English one (`/#privacy`, not `/hu/#privacy`). Date of the notice written Brazilian style: 06/10/2026.
6. **dlg.intro** – "passkeys" rendered as `chaves de acesso` (the term Google, Apple and Microsoft use in pt-BR).
   If the maintainer prefers the English word to stay recognisable, `chaves de acesso (passkeys)` also fits.
7. **menu.logout vs menu.quit** – both are "Sair" in Brazilian Portuguese (sign out / quit). To keep them apart in
   the same menu: `Sair da conta` (sign out) and `Sair` (quit). The Settings button stays `Sair do claude.ai`.
8. **STRINGS_MAC** – `Abrir ao fazer login` as instructed. Apple's own pt-BR System Settings label the feature
   "Abrir ao Iniciar Sessão" (Apple uses "iniciar sessão" on macOS even in Brazil); the instructed wording is the
   more natural everyday Brazilian phrase and matches "login" used elsewhere in the app, so it was kept.
9. **backup.sec_components** – "What is backed up" → `O que está no backup` (literal "O que é salvo no backup" is
   clumsy). Meaning preserved.
10. **help.guide, 70 % / 90 %** – written `70%` / `90%` without a space, as Brazilian typography does (the English
    has a thin space). All 37 line breaks and every HTML tag are unchanged.

en/hu differences noticed: the Hungarian privacy URL is `/hu/#privacy` (English `/#privacy` was followed);
`menu.help` is "Súgó (HELP)…" in Hungarian but plain "Help…" in English (followed the English: `Ajuda…`);
`menu.locked` is "Pozíció rögzítve" (state) in Hungarian vs "Lock position" (action) in English – followed the
English (`Fixar posição`).

## Lektor

Independent native review (pt-BR). 19 changes; `check_i18n: OK` (17 warnings, all correct identical units/loanwords).
No European-Portuguese leakage found (no ficheiro, ecrã, rato, Definições, aplicação, palavra-passe, transferir,
utilizador, registo, "a + infinitivo"); form of address "você" is consistent throughout.

- backup.cloud_only: `disponível só online … para que não seja preciso baixá-lo` → `disponível somente online … para não precisar baixá-lo` – Microsoft OneDrive term, lighter syntax
- backup.disclaimer_short: `completos e podem ser restaurados` → `completos e se podem ser restaurados` – second indirect question needs "se"
- backup.task_event: `por evento` → `em um evento` – Task Scheduler pt-BR trigger name
- dlg.err_badcode: `tente o login pelo navegador de novo` → `tente fazer login de novo pelo navegador` – natural verb, word order
- dlg.err_ratelimit: `inicie UM único login novo` → `só então faça UM novo login` – "iniciar login" unidiomatic, redundant "único"
- dlg.hint1: `Entre na página que se abre … você recebe` → `Faça login na página que abrir … você vai receber` – "Entre na página" = visit, ambiguous
- err.no_tray: `o ícone da bandeja será ignorado` → `o ícone da bandeja não será exibido` – "ignorado" calque of "skipped"
- fb.intro: `Uma ideia, um bug ou você simplesmente gostou? … Cada mensagem é lida por mim, …` → `Tem uma ideia, achou um bug ou simplesmente gostou? … Eu, Vidovics Gábor, o autor, leio todas as mensagens.` – passive voice calque, natural question
- fb.privacy_text: `art. 6(1)(f) do GDPR (RGPD);` → `art. 6(1)(f) do GDPR/RGPD;` – avoid nested parentheses
- fb.privacy_text: `Quem vê:` → `Quem tem acesso:` – standard privacy-notice heading
- help.guide: `Exige um login único` → `Exige fazer login uma única vez` – "login único" means SSO in BR
- help.guide: `verifica novas versões sozinho e atualiza com um clique` → `procura novas versões sozinho e se atualiza com um clique` – idiomatic verb, missing reflexive
- help.guide: `é mantido por 7 dias e sobrevive a reinícios e atualizações` → `fica guardado por 7 dias, mesmo após reinicializações e atualizações` – "sobrevive" is a calque
- hist.stat_now: `Semanal atual` → `Uso semanal atual` – adjective without noun is broken
- set.about: `Ele só pede à Anthropic o seu próprio uso` → `O programa só consulta a Anthropic sobre o seu próprio uso` – unclear subject, unidiomatic "pedir uso"
- set.backup_disclaimer: `a qualidade e a integridade de um backup não podem ser garantidas` → `não é possível garantir a qualidade nem a completude de um backup` – "integridade" ≠ completeness; active phrasing
- set.refresh: `Atualização` → `Atualizar a cada` – label of a seconds spin box; clashes with program update
- set.rows_none: `aparecem aqui sozinhos assim que isso acontecer` → `aparecem aqui automaticamente assim que forem enviados` – "sozinhos" colloquial-odd, vague "isso"
- update.manual: `Baixe o novo pacote.` → `Baixe o novo pacote manualmente.` – restores "instead" meaning

Still in doubt:
- STRINGS_MAC `Abrir ao fazer login`: Apple's own pt-BR wording is "Abrir ao Iniciar Sessão" (Dock menu, Login Items).
  Kept the translator's choice because the glossary bans "iniciar sessão" and the app says "login" everywhere; if the
  maintainer wants Apple's exact term, change `menu.autostart` and the two notifications.
- panel.reset `zera {}` (often "zera ~2h 30min") and panel.retry_in `repete em {} s`: telegraphic but within length;
  `zera em {}` / `nova tentativa em {} s` read better if the panel has 2–8 more characters.
- panel.full_in `cheio: {}` is understandable; `100% em {}` would be clearer but 2 characters longer.
- "bandeja do sistema" kept as instructed; current Windows 11 pt-BR UI says "área de notificação" / "estouro da barra de tarefas".
