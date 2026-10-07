# Glossário pt-BR – Claude Usage Monitor

Português do Brasil, registro de software de consumo (padrão Microsoft/Apple pt-BR). Uma única tradução fixa
por termo; o módulo `claude_usage/langs/pt_BR.py` segue esta lista.

## Tom e forma de tratamento

- **Tratamento: "você"**, sempre implícito quando possível (imperativo na 3.ª pessoa: "Verifique", "Cole",
  "Clique", "Entre novamente"). Nunca "tu", nunca "o senhor". Possessivos: "seu / sua".
- Tom curto, amigável e seguro, como o inglês. Frases diretas; sem calques ("a + infinitivo" nunca; formas
  contínuas com gerúndio: "Verificando…", "Enviando…", "Baixando…").
- Vocabulário obrigatoriamente brasileiro: arquivo, tela, mouse, Configurações, aplicativo, Entrar / Sair,
  senha, baixar, notificação, barra de tarefas, bandeja do sistema, pasta, atualização, servidor, usuário,
  log/registro. **Proibidos** (formas europeias): ficheiro, ecrã, rato, Definições, aplicação, Iniciar sessão,
  palavra-passe, transferir, utilizador, registo.
- Rótulos do painel em MAIÚSCULAS como no inglês; unidades de tempo à brasileira: **s, min, h, d**
  (ex.: "2h30min", "3 min", "1 d"). Porcentagem sem espaço: "{}%".
- Nomes próprios ficam como estão: Claude, Claude Desktop, Claude Code, claude.ai, Anthropic, Fable, Opus, Sonnet,
  Haiku, PRO/MAX/TEAM/ENTERPRISE, OneDrive, Nextcloud, Obsidian, Cowork, rclone, PowerShell, HTTP(S), JSON,
  OAuth, SHA-256, DPAPI, GDPR, NAIH, GitHub, claudeusagemonitor.com, Vidovics Gábor, Claude Backup Kit.

## Nome do documento de privacidade

**"Política de Privacidade"** (`fb.privacy_title`, `help.privacy`). É o nome que as grandes plataformas usam
no Brasil (Google, Apple, Microsoft, Meta, Nubank, Mercado Livre) e o termo que a ANPD emprega ao falar do
aviso público de um serviço. "Aviso de Privacidade" existe no jargão da LGPD, mas no software de consumo o
usuário espera "Política de Privacidade". Com inicial maiúscula nas duas palavras, como nas plataformas.

No texto legal (`fb.privacy_text`) o regulamento citado continua sendo o **GDPR** (a base legal do autor,
na Hungria); acrescento "(RGPD)" uma vez como nome em português. O app **não** afirma cumprir a LGPD – o
vocabulário usado (controlador, operador, autoridade de controle) é só o que o leitor brasileiro conhece.

## Termos fixos

| Inglês | pt-BR | Observação |
|---|---|---|
| 5-hour session | sessão de 5 horas | painel: SESSÃO DE 5 H; curto: 5H |
| weekly limit | limite semanal | painel: LIMITE SEMANAL; curto: SEM. |
| per-model weekly limit | limite semanal por modelo | |
| gauge | medidor | "Medidor Opus", "ordem dos medidores" |
| reset (noun) | redefinição | "contagem regressiva até a redefinição" |
| reset (verb, a limit resets) | redefinir / é redefinido | notificação: "redefinido — um novo período começou" |
| reset (panel label, tight) | zera {} | "zera 2h 30min": verbo coloquial brasileiro, cabe no espaço e evita o anglicismo cru |
| pace | ritmo | "{} vs ritmo" |
| burn rate | taxa de consumo | "%/hora, %/dia" |
| usage | uso | "dados de uso", "arquivo de uso" |
| usage credits | créditos de uso | |
| plan badge | selo do plano | |
| plan | plano | Pro / Max ficam como estão |
| rate-limit tier | nível de limite de taxa | |
| panel / floating panel | painel / painel flutuante | |
| widget | widget | termo corrente no Brasil |
| tray / system tray | bandeja do sistema | ícone: "ícone da bandeja" |
| menu bar (macOS) | barra de menus | só em STRINGS_MAC |
| taskbar | barra de tarefas | |
| Start menu | menu Iniciar | |
| Settings | Configurações | janela e item de menu |
| sign in / sign out | Entrar / Sair | "Entrar no claude.ai…", "Sair do claude.ai"; item de menu: "Sair da conta" |
| signed in | conectado | "Não conectado." |
| sign-in (noun) | login | "o login expirou", "exige login" |
| quit | Sair | item final do menu |
| notification | notificação | |
| notify | notificar | |
| alert | alerta | aba "Alertas" |
| threshold | limiar | "ao cruzar um limiar"; níveis: Aviso / Crítico |
| warning / critical | Aviso / Crítico | |
| backup | backup | nunca "cópia de segurança"; "pasta de backup", "script de backup" |
| snapshot | instantâneo | |
| vault (Obsidian) | cofre | termo da comunidade Obsidian em pt-BR |
| lamp | luz | "Luzes", "só as luzes", "rótulo ao lado da luz" |
| data source | fonte de dados | |
| measurement source | fonte da medição | |
| local log | log local | |
| log / log file | log / arquivo de log | |
| profile / account | perfil / conta | |
| theme | tema | |
| layout | layout | termo corrente (Microsoft pt-BR) |
| accent color | cor de destaque | |
| opacity | opacidade | |
| always on top | sempre no topo | |
| lock position | fixar posição | |
| click-through | transparente ao mouse | |
| snap to screen edge | encaixar na borda da tela | |
| update (program) | atualização | "Atualização do programa", "verificar atualizações" |
| download | baixar / download | verbo: baixar; substantivo: download |
| install | instalar | |
| history | histórico | janela "Histórico" |
| projection / forecast | projeção | "projeção para o fim da semana" |
| peak | pico | |
| avg daily burn | consumo médio diário | |
| stale data | dados desatualizados | |
| data freshness | atualidade dos dados | |
| message to the developer | mensagem para o desenvolvedor | |
| rating | avaliação | "avaliação geral", estrelas |
| privacy notice | Política de Privacidade | ver acima |
| consent | consentimento | "Li e aceito a Política de Privacidade." |
| controller / processor | controlador / operador | vocabulário da LGPD, familiar ao leitor |
| supervisory authority | autoridade de controle | |
| terms of use | Termos de Uso | |
| disclaimer | isenção de responsabilidade | |
| connected apps | aplicativos conectados | |
| scheduled task | tarefa agendada | |
| folder | pasta | |
| file | arquivo | |
| screen | tela | |
| mouse wheel | roda do mouse | |
| right-click | botão direito / clique com o botão direito | curto nas notificações |
| double-click | clique duplo | |
| drag | arrastar | |
| e-mail | e-mail | com hífen, minúsculo; rótulo "E-mail" |
| server | servidor | |
| request | requisição | "limitando as requisições (429)" |
| endpoint | endpoint | |
| check (updates / backups) | verificar | "Verificar agora", "Verificando…" |
| refresh (data) | atualizar | "Atualizar dados de uso agora" |
| done / completed | concluído | |
| failed | FALHOU / falhou | |
| no data | sem dados | |
| not set | não definido | |
| default | padrão | "Restaurar padrões" |
| optional | opcional | |
| size: small / normal / large / extra | Pequeno / Normal / Grande / Extra | "Extra" é corrente em pt-BR e respeita o limite de comprimento do menu |
| time formats (panel) | {}h {}min · {}d {}h · {} min · {} s · {} d | "2h 30min" é a forma brasileira (ABNT); nunca "2h 30m" |
| passkey | chave de acesso (passkey) | termo do Google/Apple/Microsoft pt-BR |
| step 1 / step 2 | Etapa 1 / Etapa 2 | terminologia Microsoft pt-BR |
| fetching data (panel) | atualizando | curto, cabe no painel |
| retry in {} s (panel) | repete em {} s | curto, cabe no painel |
