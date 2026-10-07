# Glossário pt-PT – Claude Usage Monitor

Português europeu, ortografia do Acordo Ortográfico de 1990 (AO90), registo de software de consumo
(terminologia Microsoft pt-PT para o Windows, Apple pt-PT para os quatro textos de macOS). Uma única
tradução fixa por termo; o módulo `claude_usage/langs/pt_PT.py` segue esta lista.

## Tom e forma de tratamento

- **Preferência pelo impessoal**: infinitivo nos itens de menu e botões («Iniciar sessão», «Procurar
  atualizações»), frases sem sujeito nas dicas e nos erros («Não foi possível…», «É preciso…»).
- **Quando é inevitável dirigir-se ao utilizador: «tu»**, sempre e só «tu» (imperativo da 2.ª pessoa:
  «Verifica», «Cola», «Inicia sessão», «Clica»; possessivos «teu / tua»). É o registo das melhores
  aplicações de consumo em Portugal e o único que soa pessoal nas mensagens do autor («Diz-me», «Leio
  todas as mensagens»). **Nunca «você»**, nunca «o senhor», nunca a 3.ª pessoa disfarçada («Verifique»).
- Tom curto, simpático e seguro, como o inglês. Sem decalques do inglês nem do português do Brasil.
- **Formas contínuas com «a + infinitivo»**: «A verificar…», «A enviar…», «A transferir…». Nunca o gerúndio.
- **Vocabulário europeu obrigatório**: ficheiro, ecrã, rato, Definições, aplicação, Iniciar sessão /
  Terminar sessão, palavra-passe, transferir, área de notificação, barra de tarefas, pasta, atualização,
  servidor, utilizador, registo (log), browser. **Proibidos** (formas brasileiras): arquivo, tela, mouse,
  Configurações, aplicativo, Entrar/Sair (para sessão), senha, baixar, usuário, «você», gerúndio contínuo.
- Rótulos do painel em MAIÚSCULAS como no inglês; unidades de tempo **s, min, h, d** («2h 30min»,
  «3 min», «1 d»). Percentagem colada ao número como no inglês: «{}%».
- Aspas: «…» (angulares, uso corrente em Portugal) no texto corrido; nos literais Python usam-se « » para
  não precisar de escapes.
- Nomes próprios ficam como estão: Claude, Claude Desktop, Claude Code, claude.ai, Anthropic, Fable, Opus,
  Sonnet, Haiku, PRO/MAX/TEAM/ENTERPRISE, OneDrive, Nextcloud, Obsidian, Cowork, rclone, PowerShell,
  HTTP(S), JSON, OAuth, SHA-256, DPAPI, NAIH, GitHub, claudeusagemonitor.com, Vidovics Gábor,
  Claude Backup Kit, PC («este PC», como no Windows pt-PT).

## Nome do documento de privacidade

**«Política de Privacidade»** (`fb.privacy_title`, `help.privacy`). É o nome que as grandes plataformas usam
em Portugal (Microsoft, Apple, Google, CTT, MEO, NOS, bancos) e que a CNPD emprega quando fala do documento
público de um serviço. «Aviso de privacidade» e «Declaração de privacidade» existem (a Microsoft usa
«Declaração» para o documento corporativo), mas numa aplicação de consumo o utilizador procura
«Política de Privacidade». Iniciais maiúsculas nas duas palavras, como nas plataformas. `fb.privacy_hide`
fala em «aviso» porque esconde o texto na janela, não o documento.

No texto legal (`fb.privacy_text`) o regulamento é o **RGPD** (nome oficial português do GDPR) com os
artigos no formato jurídico português: «artigo 6.º, n.º 1, alínea f) do RGPD». Vocabulário oficial da versão
portuguesa do regulamento: responsável pelo tratamento, subcontratante, autoridade de controlo, titular dos
dados, direito de acesso / retificação / apagamento / limitação do tratamento / oposição. A autoridade
mantém-se genérica («a autoridade do teu país»), com a CNPD como exemplo português.

## Termos fixos

| Inglês | pt-PT | Observação |
|---|---|---|
| 5-hour session | sessão de 5 horas | painel: SESSÃO DE 5 H; curto: 5H; histórico: «sessão de 5 h» |
| weekly limit | limite semanal | painel: SEMANAL (não cabe «LIMITE SEMANAL»); curto: SEM. |
| per-model weekly limit | limite semanal do modelo | painel: «{} SEMANAL» (OPUS SEMANAL) |
| gauge | indicador | «Indicador Opus», «ordem dos indicadores» |
| reset (noun) | reposição | «contagem decrescente até à reposição»; termo Microsoft (repor) |
| reset (verb, a limit resets) | repor / é reposto | «quando um limite é reposto» |
| reset (panel label, tight) | reset | anglicismo corrente e sem alternativa curta; o húngaro faz o mesmo |
| pace | ritmo | «{} vs ritmo» |
| burn rate | taxa de consumo | «Taxa de consumo (%/hora, %/dia)» |
| usage | utilização | «dados de utilização», «ficheiro de utilização» |
| usage credits | créditos de utilização | |
| plan badge | emblema do plano | «emblema» = badge na terminologia Microsoft pt-PT |
| plan | plano | Pro / Max ficam como estão |
| rate-limit tier | nível de limite | |
| panel / floating panel | painel / painel flutuante | |
| widget | widget | termo corrente em Portugal |
| tray / system tray | área de notificação | ícone: «ícone da área de notificação» (Windows pt-PT) |
| menu bar (macOS) | barra de menus | só em STRINGS_MAC |
| taskbar | barra de tarefas | |
| Start menu | menu Iniciar | |
| Settings | Definições | janela, separador e item de menu |
| sign in / sign out | Iniciar sessão / Terminar sessão | «Iniciar sessão no claude.ai…», «Terminar sessão no claude.ai» |
| sign-in (noun) | início de sessão | «o início de sessão expirou», «requer início de sessão» |
| signed in / not signed in | sessão iniciada / sem sessão iniciada | |
| quit | Sair | último item do menu; sem conflito porque sair da conta é «Terminar sessão» |
| browser | browser | termo Microsoft pt-PT; «navegador» não se usa |
| notification | notificação | |
| notify | notificar | |
| alert | alerta | separador «Alertas» |
| threshold | limiar | «ao ultrapassar um limiar»; níveis: Aviso / Crítico |
| warning / critical | Aviso / Crítico | |
| backup | cópia de segurança | termo Microsoft; «cópias» quando o contexto já é claro («Estado das cópias») |
| snapshot | instantâneo | |
| vault (Obsidian) | cofre | termo da tradução pt do Obsidian |
| lamp | luz | «Luzes», «só as luzes», «etiqueta junto à luz» |
| data source | origem dos dados | Microsoft pt-PT: origem de dados |
| measurement source | origem da medição | |
| local log | registo local | |
| log / log file | registo / ficheiro de registo | |
| profile / account | perfil / conta | |
| theme | tema | |
| layout | esquema | termo Microsoft pt-PT |
| accent color | cor de destaque | Windows pt-PT |
| opacity | opacidade | |
| always on top | sempre no topo | definição: «Por cima de todas as outras janelas» |
| lock position | bloquear posição | |
| click-through | transparente aos cliques | «(só decorativo, ignora o rato)» |
| snap to screen edge | encostar à margem do ecrã | |
| update (program) | atualização | «Atualização do programa», «Procurar atualizações» |
| download | transferir / transferência | verbo: transferir; substantivo: transferência |
| install | instalar | |
| history | histórico | janela «Histórico» |
| projection / forecast | previsão | «Previsão: fim da semana» (nunca «fim de semana» = weekend) |
| peak | pico | |
| avg daily burn | consumo médio diário | |
| stale data | dados desatualizados | |
| data freshness | atualidade dos dados | |
| message to the developer | mensagem ao programador | «programador» = developer (Microsoft pt-PT) |
| rating | avaliação | «Avaliação geral», estrelas |
| privacy notice | Política de Privacidade | ver acima |
| consent | consentimento | «Li e aceito a Política de Privacidade.» |
| controller / processor | responsável pelo tratamento / subcontratante | RGPD, versão portuguesa |
| supervisory authority | autoridade de controlo | em Portugal: CNPD |
| terms of use | Termos de Utilização | |
| disclaimer | Exclusão de responsabilidade | termo Microsoft pt-PT |
| connected apps | aplicações ligadas | |
| scheduled task | tarefa agendada | |
| folder | pasta | |
| file | ficheiro | |
| screen | ecrã | |
| mouse wheel | roda do rato | |
| right-click | botão direito / clicar com o botão direito | curto nas notificações: «Botão direito no painel» |
| double-click | duplo clique | |
| drag | arrastar | |
| e-mail | e-mail | com hífen, minúsculo; rótulo «E-mail» |
| server | servidor | |
| request | pedido | «a limitar os pedidos (429)» |
| endpoint | endpoint | jargão técnico, fica como no húngaro |
| link | ligação | «Demasiadas ligações na mensagem.» |
| check (updates / backups) | verificar / procurar | cópias: «Verificar agora»; atualizações: «Procurar atualizações» |
| refresh (data) | atualizar | «Atualizar dados agora»; intervalo em segundos: «Intervalo de atualização» |
| passkey | chave de acesso | termo Windows / Google pt-PT |
| release notes | notas de versão | termo Microsoft pt-PT |
| on event (scheduled task) | num evento | Agendador de Tarefas pt-PT |
| done / completed | concluído | |
| failed | FALHOU / falhou | |
| no data | sem dados | |
| not set | não definido | |
| default | predefinição / predefinido | «Repor predefinições» |
| optional | opcional | |
| size: small / normal / large / extra | Pequeno / Normal / Grande / Muito grande | |
| running (app) | em execução | |
| Claude Desktop running? | O Claude Desktop está aberto? | mais natural do que «em execução» numa notificação |
