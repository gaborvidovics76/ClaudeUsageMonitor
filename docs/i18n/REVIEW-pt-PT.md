# REVIEW pt-PT – Claude Usage Monitor

Module: `claude_usage/langs/pt_PT.py` (358 keys + 4 macOS keys). Checker: `check_i18n: OK`, 11 warnings, all
"identical to English" on pure unit strings (`{}d`, `{} h`, `5H`, `Normal`) and on `panel.reset` (see 2).

Form of address: impersonal wherever possible, **"tu"** where the user must be addressed (never "você").
Privacy document: **"Política de Privacidade"**; regulation **RGPD** with "artigo 6.º, n.º 1, alínea f)/a)".

Legacy block: of the 324 old pt texts, 136 were changed (Brazilian forms, "você"/"sua"/"veja"/"clique", mixed
"tu"/3rd person, calques, length), 188 were already correct European Portuguese and were kept as they were.

## The 10 texts I am least sure about

1. **`panel.weekly` = "SEMANAL"** (and `panel.model` = "{} SEMANAL"). The natural label is "LIMITE SEMANAL"
   (the old inline text), but it is 14 characters against 12 in English and the panel elides with "…".
   "SEMANAL" is safe; if the maintainer sees that "LIMITE SEMANAL" fits in the ring/post-it layouts at the
   default size, that is the better reading. `panel.model` is 1 character over ("OPUS SEMANAL" vs "OPUS WEEKLY").
2. **`panel.reset` = "reset {}"** – left as the anglicism, like the Hungarian. The proper noun "reposição"
   is twice as long and "repõe {}" reads oddly without "em". A Portuguese user understands "reset 2h 30min" instantly.
3. **Minutes = "min"** in `time.m`, `time.hm`, `backup.age_m` ("{}min", "{}h {}min"). Two characters longer
   than the English "m", but "m" means metres/month to a Portuguese reader; Windows and Apple pt-PT both write
   "min". If the countdown gets cut off, "{}h {}m" is the fallback.
4. **`panel.updated` = "atualizado: {}"** (+3) and **`panel.retry_in` = "de novo em {} s"** (+2). No shorter
   natural wording; "há {}" would read perfectly but breaks when `fmt_age` returns "sem dados".
5. **"browser"** rather than "navegador" everywhere (`dlg.*`, `menu.login`, `help.guide`). It is the Microsoft
   pt-PT term and the everyday word in Portugal; "navegador" marks a text as Brazilian for many readers.
6. **`fb.title` / `menu.feedback` = "Mensagem ao programador"**. "Programador" is the pt-PT word for developer
   (Windows: "Modo de programador"); "desenvolvedor" is Brazilian. "Mensagem ao autor" would also be fine.
7. **`menu.layout` / `set.layout` = "Esquema"** – Microsoft pt-PT; Apple would say "Disposição". The same
   word is shown on macOS (the key is not in `STRINGS_MAC`), which is acceptable but not Apple-perfect.
8. **`notify.threshold` = "{}: {}% utilizado."** – the first placeholder is a gauge name of either gender
   ("Sessão de 5 horas", "Limite semanal"); "utilizado" agrees with the percentage, not the gauge, so it is
   grammatical in both cases, but a reader might expect "utilizados". `notify.reset_done` was made gender-free
   with the noun "reposição".
9. **`backup.level_red` = "Desatualizada", `backup.level_green` = "Recente"** – feminine, agreeing with
   "cópia (de segurança)". If these words are ever shown next to a masculine noun (e.g. "estado"), they
   would need the masculine form.
10. **`fb.privacy_text`**: I added "(em Portugal: CNPD)" after "à autoridade do teu país", as allowed.
    "Hash" was rendered as "valor de hash" (pt-PT legal/technical usage keeps the English word). The
    paragraph structure, every article number, retention period, right and the URL follow the English.

## en/hu differences noticed (English followed)

- `fb.privacy_text`: the Hungarian links to `https://claudeusagemonitor.com/hu/#privacy`; the English (and this
  module) to `https://claudeusagemonitor.com/#privacy`.
- `menu.help`: hu "Súgó (HELP)…" adds the English word; pt-PT is simply "Ajuda…".
- `menu.panel_visible`: hu "Panel látszik" (state) vs en "Show panel" (action) – pt-PT "Mostrar painel".
- `set.notify_reset`: hu adds "(reset)" after "visszaáll"; pt-PT uses "é reposto" without the anglicism.
- `help.guide` section "Using the widget": hu "Kezelés" (operation); pt-PT "Utilizar o widget".
- `hist.stat_forecast`: en "End-of-week projection" – rendered "Previsão: fim da semana" on purpose
  ("fim de semana" would mean *weekend*).

## Lektor

Independent native pt-PT review. No Brazilian forms, no "você" and no gerund found; the "tu" form was already
consistent. 30 changes, mostly naturalness and two meaning fixes (`set.refresh`, `set.backup_disclaimer`).

- backup.task_event: por evento → num evento – Task Scheduler pt-PT wording
- dlg.err_badcode: «completo, ou repete» → «completo ou repete» – no comma before «ou»
- dlg.err_ratelimit: «inicia UM único início de sessão no browser» → «inicia sessão no browser UMA só vez» – removes iniciar/início repetition
- dlg.intro: «conta claude.ai» / «passkeys» → «conta do claude.ai» / «chaves de acesso» – Windows pt-PT passkey term
- err.no_tray: «o ícone fica de fora» → «o ícone não é apresentado» – colloquial, unclear
- err.rate_limited: «a repetir automaticamente» → «a tentar de novo automaticamente» – natural retry wording
- fb.intro: «um erro, ou simplesmente» → «um erro ou simplesmente» – no comma before «ou»
- fb.rating_tip: {} em 5 → {} de 5 – usual pt-PT rating form
- fb.sent_sub: «respondo-te por aí» → «respondo-te para esse endereço» – «por aí» ambiguous
- help.guide (weekly): «a uma hora semanal fixa da tua conta» → «todas as semanas a uma hora fixa, própria da tua conta» – calque
- help.guide (per-model): «quando o servidor comunica um» → «se o servidor o fornecer» – calque of "reports one"
- help.guide (pace): «se ele chega até à reposição» → «se vai durar até à reposição» – "will last" meaning
- help.guide (claude.ai): «Requer um início de sessão único» → «Basta iniciar sessão uma vez» – avoids "single sign-on" reading
- help.guide (backups): «correram e terminaram» → «foram executadas e concluídas» – colloquial «correram»
- help.guide (updates): «notas de lançamento» → «notas de versão» – Microsoft pt-PT term
- help.guide (privacy): «O início de sessão … fica guardado encriptado» → «Os dados de início de sessão … ficam guardados, encriptados» – a sign-in is not stored
- help.guide (troubleshooting): «sobrevive a reinícios» → «mantém-se após reinícios» – calque of "survives"
- hist.stat_now: Semanal atual → Semana atual – adjective without noun
- menu.refresh: Atualizar dados de utilização agora → Atualizar dados agora – 60 % longer than English
- notify.logout: «Passou para a origem local.» → «A usar agora a origem local.» – missing subject
- set.backup_disclaimer: «a qualidade e a integridade de uma cópia não podem ser garantidas» → «não é possível garantir a qualidade de uma cópia nem que esteja completa» – "completeness", not integrity
- set.backup_disclaimer: «as cópias» → «as tuas cópias» – source says "your backups"
- set.backup_disclaimer: «testa um restauro» → «faz um teste de restauro» – more natural
- set.data_hint: «mais ou menos de 5 em 5» → «aproximadamente de 5 em 5» – too colloquial
- set.details_api_only: «Estes vêm da origem de dados claude.ai» → «Estes dados vêm da origem claude.ai» – subject, glossary term
- set.local_models_hint: «Para os outros, isto mostra como se divide … uma parte … não uma parte de um limite» → «Para os restantes, mostra como se reparte … uma proporção … não de um limite» – repetitive calque
- set.refresh: Atualização → Intervalo de atualização – it is the seconds spinbox
- set.rows_none: «aparecem aqui sozinhos» → «aparecem aqui automaticamente» – natural software wording
- update.manual: «corre a partir … Transfere antes o novo pacote» → «é executada a partir … Em alternativa, transfere o novo pacote» – «antes» read as "beforehand"
- update.restarting: «reinicia num instante» → «vai reiniciar dentro de instantes» – standard pt-PT phrasing

Glossary: added passkey = chave de acesso, release notes = notas de versão, on event = num evento; updated the
refresh row.

Still in doubt:
- `notify.threshold` «{}: {}% utilizado.» – agreement is acceptable, but «utilizados» is also common; left as is.
- `menu.always_top` «Sempre no topo» – common in Portuguese apps; Windows itself mostly says «Sempre visível».
- `time.m` / `time.hm` «min» (2 characters over the English) – right for the reader, but check for truncation.
- `menu.layout` «Esquema» is the Microsoft term; on macOS Apple would say «Disposição».
