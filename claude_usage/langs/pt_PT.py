# -*- coding: utf-8 -*-
"""Português (Portugal) – UI strings of Claude Usage Monitor.

European Portuguese, AO90 spelling, Microsoft pt-PT terminology for Windows and Apple pt-PT for
the four macOS texts. Impersonal wording where possible, "tu" where the user must be addressed.
See docs/i18n/glossary-pt-PT.md.
"""

CODE = "pt-PT"
NAME = "Português (Portugal)"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{}d",
    "backup.age_h": "{}h",
    "backup.age_m": "{}min",
    "backup.and_more": "…e mais {}",
    "backup.checked_at": "Verificado: {}",
    "backup.checking": "A verificar…",
    "backup.cloud_only": "O instantâneo está apenas online no OneDrive; o conteúdo não é listado para não ter de ser transferido.",
    "backup.comp.cowork": "Registos de conversas do Cowork (um ZIP por sessão)",
    "backup.comp.vault": "Instantâneo do cofre do Obsidian (ZIP)",
    "backup.disclaimer_short": "O monitor mostra apenas o que os registos das cópias de segurança dizem. Não assumimos qualquer responsabilidade pelas cópias – verificar se estão completas e se podem ser restauradas cabe-te a ti.",
    "backup.done": "concluído",
    "backup.dry_run": "(execução de teste, nada foi enviado)",
    "backup.failed": "FALHOU",
    "backup.files_size": "{} ficheiros, {}",
    "backup.folders": "Pastas",
    "backup.label_age": "Nome e idade",
    "backup.label_name": "Só o nome",
    "backup.label_none": "Só as luzes",
    "backup.last_ok": "Última cópia bem-sucedida: {} (há {})",
    "backup.last_run": "Última execução: {} – {}",
    "backup.legend": "Verde: até {} h · Amarelo: até {} h · Vermelho: mais antiga, ou sem cópia",
    "backup.level_green": "Recente",
    "backup.level_none": "Nenhuma cópia encontrada",
    "backup.level_red": "Desatualizada",
    "backup.level_yellow": "A envelhecer",
    "backup.log_file": "Ficheiro de registo",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Pasta das cópias de segurança não encontrada: {}",
    "backup.none_found": "Nenhum.",
    "backup.open": "abrir",
    "backup.rc_copied": "ficheiros novos ou alterados copiados",
    "backup.rc_failed": "FALHOU (código {})",
    "backup.rc_nochange": "atualizado, nada a copiar",
    "backup.recent_notes": "Notas editadas mais recentemente no instantâneo",
    "backup.refresh": "Verificar agora",
    "backup.sec_components": "O que é guardado",
    "backup.sec_contents": "Conteúdo",
    "backup.sec_log": "Registo (últimas linhas)",
    "backup.sec_problems": "Erros e avisos",
    "backup.sec_tasks": "Tarefas agendadas",
    "backup.skipped": "ignorado (pasta não encontrada)",
    "backup.snap_kept": "{} instantâneos guardados, {} no total",
    "backup.snapshot": "Instantâneo mais recente",
    "backup.source": "Origem",
    "backup.state_error": "terminou com erros",
    "backup.state_interrupted": "não terminou",
    "backup.state_ok": "concluída com êxito",
    "backup.state_running": "em execução",
    "backup.storage": "Armazenamento remoto: {} usados de {}, {} livres",
    "backup.target": "Destino",
    "backup.task_event": "num evento",
    "backup.task_row": "última execução {} · resultado {} · próxima {}",
    "backup.tip_click": "Clica para ver os detalhes",
    "backup.title": "Cópias de segurança",
    "backup.tray": "Cópias: {}",
    "backup.uploaded": "Enviados nesta execução: {} novos, {} substituídos, {} erros",
    "backup.uploaded_files": "Ficheiros enviados",
    "backup.uploaded_groups": "Ficheiros enviados, por pasta",
    "backup.uploaded_no": "Enviado para o Nextcloud: ainda não",
    "backup.uploaded_yes": "Enviado para o Nextcloud: sim ({})",
    "backup.vault": "Cofre",
    "backup.vault_changed": "{} notas alteradas no cofre desde este instantâneo",
    "backup.zip_new": "{} ZIP novos/atualizados",
    "backup.zip_summary": "{} ficheiros ({} notas), {} sem compressão",
    # --- details rows ----------------------------------------------------------------------
    "detail.extra": "Créditos de utilização",
    "detail.local_header": "CLAUDE CODE · ESTE PC · DIVISÃO DESTA SEMANA",
    "detail.off": "desativado",
    "detail.on": "ativado",
    "detail.surface.oauth_apps": "Aplicações ligadas",
    "detail.unlimited": "sem limite",
    # --- sign-in dialog --------------------------------------------------------------------
    "dlg.cancel": "Cancelar",
    "dlg.checking": "A verificar…",
    "dlg.err_badcode": "O código não foi aceite.\n\n{}\n\nVerifica se colaste o código completo ou repete o início de sessão no browser (é sempre preciso um código novo).",
    "dlg.err_ratelimit": "Demasiadas tentativas de início de sessão em pouco tempo.\n\nO servidor está a limitar-te temporariamente. Fecha esta janela, espera 10–15 minutos (sem tentar entretanto) e depois inicia sessão no browser UMA só vez, com um código novo.",
    "dlg.hint1": "Inicia sessão na página que se abre e autoriza o acesso. No fim recebes um código.",
    "dlg.intro": "Inicia sessão na tua conta do claude.ai no teu próprio browser (as palavras-passe e as chaves de acesso guardadas já funcionam lá).",
    "dlg.login_title": "iniciar sessão",
    "dlg.open_browser": "Abrir o início de sessão no browser",
    "dlg.paste_label": "Cola aqui o código que recebeste:",
    "dlg.paste_placeholder": "colar o código aqui",
    "dlg.signin": "Iniciar sessão",
    "dlg.step1": "Passo 1",
    "dlg.step2": "Passo 2",
    "dlg.unknown_err": "Erro desconhecido.",
    # --- error messages --------------------------------------------------------------------
    "err.already_running": "A aplicação já está em execução (vê a área de notificação).",
    "err.bad_token_resp": "resposta inválida do endpoint de token",
    "err.bad_usage_resp": "resposta inválida do endpoint de utilização",
    "err.connection": "erro de ligação: {}",
    "err.file_empty": "O ficheiro de utilização está vazio.",
    "err.file_not_found": "Ficheiro de utilização não encontrado.\nO Claude Desktop está aberto?",
    "err.file_unreadable": "De momento não é possível ler o ficheiro de utilização.",
    "err.loading": "A iniciar sessão / a consultar…",
    "err.network": "erro de rede: {}",
    "err.no_code": "Nenhum código colado.",
    "err.no_data_profile": "Sem dados para este perfil.",
    "err.no_tray": "Área de notificação indisponível; o ícone não é apresentado.",
    "err.no_usage_data": "Sem dados de utilização.",
    "err.not_signed_in": "Sem sessão iniciada.",
    "err.query_http": "Erro na consulta (HTTP {}).",
    "err.rate_limited": "O servidor está a limitar os pedidos (429) – a tentar de novo automaticamente.",
    "err.session_expired": "A sessão expirou, inicia sessão de novo.",
    "err.session_expired_nl": "A sessão expirou.\nInicia sessão de novo.",
    "err.signin_needed": "O início de sessão no claude.ai expirou.\nInicia sessão de novo: botão direito → Iniciar sessão no claude.ai",
    "err.unexpected": "Erro inesperado: {}",
    # --- "Message to the developer" window -------------------------------------------------
    "fb.cancel": "Cancelar",
    "fb.close": "Fechar",
    "fb.consent": "Li e aceito a {}.",
    "fb.email": "E-mail",
    "fb.email_hint": "só se quiseres resposta",
    "fb.err_consent": "Para enviar, é preciso aceitar a Política de Privacidade.",
    "fb.err_email": "Este endereço de e-mail não parece válido.",
    "fb.err_empty": "Escreve primeiro uma mensagem ou escolhe uma avaliação.",
    "fb.err_links": "Demasiadas ligações na mensagem.",
    "fb.err_network": "Não foi possível contactar claudeusagemonitor.com. Verifica a ligação e tenta de novo.",
    "fb.err_rate": "Demasiadas mensagens em pouco tempo – tenta de novo mais tarde.",
    "fb.err_server": "De momento, o servidor não conseguiu receber a mensagem. Tenta de novo mais tarde.",
    "fb.intro": "Uma ideia, um erro ou simplesmente gostas? Diz-me. Leio pessoalmente todas as mensagens – Vidovics Gábor, o autor do programa.",
    "fb.message": "Mensagem",
    "fb.message_ph": "O que funciona, o que não funciona, o que falta?",
    "fb.meta": "Enviado juntamente com a mensagem: versão do programa {0}, sistema operativo ({1}), idioma da interface ({2}).",
    "fb.name": "Nome",
    "fb.optional": "(opcional)",
    "fb.privacy_hide": "Ocultar o aviso",
    "fb.privacy_text": (
        "Responsável pelo tratamento: Vidovics Gábor, pessoa singular (Hungria), autor do Claude Usage Monitor. "
        "A Política de Privacidade completa está no site: https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "O que é enviado: o que escreves aqui – nome (opcional), endereço de e-mail (opcional), mensagem, "
        "avaliação por estrelas – e, para que eu possa perceber o contexto: a versão do programa, o nome e a "
        "versão do sistema operativo, o idioma da interface e a data e hora do envio. O servidor não guarda "
        "nenhum endereço IP; para prevenir abusos usa apenas um valor de hash que muda todos os dias e que não "
        "pode ser convertido de volta num endereço."
        "\n\n"
        "Finalidade: ler e responder à tua mensagem e melhorar o programa (interesse legítimo, artigo 6.º, "
        "n.º 1, alínea f) do RGPD; a resposta em si é dada a teu pedido). A tua avaliação e o teu nome só "
        "aparecem no site se assinalares a caixa própria para isso (consentimento, artigo 6.º, n.º 1, "
        "alínea a) do RGPD) e só depois de o autor os ter revisto; podes retirar esse consentimento a "
        "qualquer momento."
        "\n\n"
        "Prazo de conservação: as mensagens, no máximo 2 anos; uma avaliação publicada, até retirares o "
        "consentimento. Se o autor tiver ativado o reencaminhamento por e-mail, uma cópia chega também à "
        "caixa de correio do autor."
        "\n\n"
        "Quem tem acesso: apenas o responsável pelo tratamento e – na qualidade de subcontratante – o "
        "fornecedor de alojamento (servidor na UE, Alemanha). Nada é vendido nem transmitido a terceiros; "
        "não há definição de perfis nem decisões automatizadas."
        "\n\n"
        "Os teus direitos: acesso, retificação, apagamento, limitação do tratamento, oposição, retirada do "
        "consentimento e apresentação de reclamação a uma autoridade de controlo (na Hungria: NAIH, naih.hu) "
        "ou à autoridade do teu país (em Portugal: CNPD). Contacto: este formulário ou o site."
        "\n\n"
        "Transmissão: encriptada (HTTPS/TLS) para claudeusagemonitor.com. Versão deste aviso: 2026-10-06."
    ),
    "fb.privacy_title": "Política de Privacidade",
    "fb.publish": "A minha avaliação e o meu nome (se indicado) podem ser mostrados em claudeusagemonitor.com.",
    "fb.rating": "Avaliação geral",
    "fb.rating_clear": "limpar",
    "fb.rating_hint": "opcional – clica numa estrela",
    "fb.rating_tip": "{} de 5",
    "fb.secure": "Ligação encriptada (HTTPS) a claudeusagemonitor.com.",
    "fb.send": "Enviar",
    "fb.sending": "A enviar…",
    "fb.sent": "Obrigado – a mensagem chegou!",
    "fb.sent_sub": "Leio todas as mensagens. Se deixaste um endereço de e-mail, respondo-te para esse endereço.",
    "fb.title": "Mensagem ao programador",
    # --- Help window -----------------------------------------------------------------------
    "help.disclaimer": "Uma ferramenta independente e gratuita – não foi criada pela Anthropic nem está associada a ela. «Claude» é uma marca da Anthropic.",
    "help.feedback": "Perguntas, ideias, erros encontrados: o formulário de mensagem no site.",
    "help.free": "Gratuito para sempre · licença MIT · código aberto · sem telemetria",
    "help.guide": (
        "\n<h2>O que o widget mostra</h2>\n<ul>\n"
        "<li><b>Sessão de 5 horas</b> – quanto do limite da sessão atual já foi utilizado. É reposto de cinco em cinco horas; "
        "o widget faz a contagem decrescente até à reposição.</li>\n"
        "<li><b>Limite semanal</b> – a utilização de todos os modelos em conjunto; é reposto todas as semanas a uma hora fixa, própria da tua conta.</li>\n"
        "<li><b>Limite semanal do modelo</b> – um terceiro indicador, se o servidor o fornecer (p. ex. para um modelo específico).</li>\n"
        "<li><b>Ritmo e taxa de consumo</b> – a que velocidade estás a gastar o limite e se vai durar até à reposição; "
        "a previsão para o fim da semana avisa a tempo.</li>\n"
        "<li><b>Créditos de utilização</b> e o emblema do plano – quando os ativas em <i>Emblema do plano e limites extra</i>.</li>\n"
        "</ul>\n<h2>De onde vêm os dados</h2>\n<ul>\n"
        "<li><b>claude.ai (todos os dispositivos)</b> – consulta o servidor da Anthropic, por isso inclui a utilização no telemóvel, "
        "no browser e noutros computadores. Basta iniciar sessão uma vez no teu próprio browser (menu: <i>Iniciar sessão</i>). "
        "Atualiza de 2 em 2 minutos, mais devagar se o servidor o pedir.</li>\n"
        "<li><b>Local (só este PC)</b> – lê o registo de utilização do Claude Desktop neste computador. Não precisa de início de sessão, "
        "mas só conhece este PC.</li>\n"
        "</ul>\n<p>A troca faz-se no menu: <i>Origem dos dados</i>.</p>\n"
        "<h2>Utilizar o widget</h2>\n<ul>\n"
        "<li><b>Botão direito</b> no widget (ou no ícone da área de notificação) – o menu completo.</li>\n"
        "<li><b>Duplo clique</b> num indicador – a janela <b>Histórico</b>: 6 horas, 24 horas, 7 dias ou tudo, com picos, "
        "média diária e previsão.</li>\n"
        "<li><b>Arrastar</b> para mover; encosta às margens do ecrã. <b>Ctrl + roda do rato</b> – maior ou mais pequeno.</li>\n"
        "<li>Esquemas: cartão post-it, barra fina, anéis; 6 temas. <i>Bloquear posição</i> e <i>Transparente aos cliques</i> "
        "estão nas Definições.</li>\n"
        "</ul>\n<h2>Alertas</h2>\n"
        "<p>Amarelo a partir de 70 %, vermelho a partir de 90 % (ajustável). Notificações opcionais quando um limite é reposto "
        "e quando os dados ficam desatualizados.</p>\n"
        "<h2>Cópias de segurança (opcional)</h2>\n"
        "<p>As pequenas luzes mostram se as tuas cópias de segurança agendadas foram executadas e concluídas. Clica numa luz para ver os "
        "detalhes. O monitor só lê os registos das cópias – fazer e testar as cópias é tarefa tua (ver os Termos de Utilização).</p>\n"
        "<h2>Atualizações</h2>\n"
        "<p>O programa procura novas versões sozinho e atualiza-se com um clique. Cada pacote é verificado com SHA-256 e vem "
        "exclusivamente de <b>claudeusagemonitor.com</b>. Novas versões e notas de versão: {site}</p>\n"
        "<h2>Privacidade</h2>\n"
        "<p>Sem telemetria, sem rastreio. Os dados de início de sessão no claude.ai ficam guardados, encriptados, apenas neste computador; "
        "nada é enviado para outro lado.</p>\n"
        "<h2>Se algo estiver mal</h2>\n<ul>\n"
        "<li><i>429 / limitação de pedidos</i> – o servidor está a abrandar os pedidos; o programa tenta de novo sozinho.</li>\n"
        "<li>Sem dados – verifica a <i>Origem dos dados</i>; com o claude.ai, inicia sessão de novo.</li>\n"
        "<li>O histórico é guardado durante 7 dias e mantém-se após reinícios e atualizações.</li>\n"
        "<li>Registos e definições: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Criado por",
    "help.moved": "Novo endereço desde 21 de setembro de 2026 – a antiga página dinorr.hu/claude-usage-monitor redireciona para aqui.",
    "help.official": "SITE OFICIAL",
    "help.open_site": "Abrir claudeusagemonitor.com",
    "help.privacy": "Política de Privacidade",
    "help.site_what": "Transferências, atualizações automáticas, novidades, o Claude Backup Kit, termos de utilização e privacidade – tudo num só lugar.",
    "help.source_code": "Código-fonte (GitHub)",
    "help.tab_author": "Autor",
    "help.tab_guide": "Como funciona",
    "help.terms": "Termos de Utilização",
    "help.title": "Ajuda",
    "help.version": "Versão",
    # --- History window --------------------------------------------------------------------
    "hist.legend_5h": "sessão de 5 h",
    "hist.legend_week": "limite semanal",
    "hist.no_data": "Dados insuficientes para este período.",
    "hist.range_24h": "24 horas",
    "hist.range_6h": "6 horas",
    "hist.range_7d": "7 dias",
    "hist.range_all": "Tudo",
    "hist.stat_burn": "Consumo médio diário",
    "hist.stat_forecast": "Previsão: fim da semana",
    "hist.stat_now": "Semana atual",
    "hist.stat_peak": "Pico semanal",
    "hist.stat_sessions": "Sessões de 5 h",
    "hist.title": "histórico",
    # --- layouts ---------------------------------------------------------------------------
    "layout.compact": "Barra fina",
    "layout.postit": "Cartão post-it",
    "layout.ring": "Anéis",
    # --- context menu ----------------------------------------------------------------------
    "menu.always_top": "Sempre no topo",
    "menu.autostart": "Iniciar com o Windows",
    "menu.backup_bar": "Estado das cópias",
    "menu.backups": "Cópias de segurança…",
    "menu.check_update": "Procurar atualizações do programa…",
    "menu.click_through": "Transparente aos cliques",
    "menu.details": "Emblema do plano e limites extra",
    "menu.feedback": "Mensagem ao programador…",
    "menu.help": "Ajuda…",
    "menu.history": "Histórico e estatísticas…",
    "menu.language": "Idioma",
    "menu.layout": "Esquema",
    "menu.locked": "Bloquear posição",
    "menu.login": "Iniciar sessão (claude.ai, browser)…",
    "menu.logout": "Terminar sessão",
    "menu.model_gauge": "Indicador {}",
    "menu.order": "Ordem",
    "menu.panel_visible": "Mostrar painel",
    "menu.quit": "Sair",
    "menu.refresh": "Atualizar dados agora",
    "menu.settings": "Definições…",
    "menu.size": "Tamanho",
    "menu.source": "Origem dos dados",
    "menu.start_menu": "Mostrar no menu Iniciar",
    "menu.theme": "Tema",
    "menu.update_available": "Atualização do programa: instalar a versão {}…",
    # --- desktop notifications -------------------------------------------------------------
    "notify.autostart_fail": "Não foi possível configurar o arranque automático.",
    "notify.autostart_off": "Desativado: a aplicação não arranca com o Windows.",
    "notify.autostart_on": "Ativado: a aplicação arranca com o Windows.",
    "notify.first_run": "O painel apareceu no canto superior direito.\nBotão direito no painel ou no ícone da área de notificação = menu.",
    "notify.login_ok": "Sessão iniciada – a receber os dados do servidor.",
    "notify.logout": "Sessão terminada. A usar agora a origem local.",
    "notify.reset_done": "{}: reposição — começou um novo período.",
    "notify.signin_needed": "O início de sessão no claude.ai expirou. Clica com o botão direito no painel e inicia sessão de novo para continuares a ver a utilização de todos os teus dispositivos.",
    "notify.stale_body": "A última leitura foi há {}. O Claude Desktop está aberto?",
    "notify.stale_title": "Dados desatualizados",
    "notify.threshold": "{}: {}% utilizado.",
    "notify.update": "Está disponível a versão {} do programa. Botão direito no painel → Atualização do programa.",
    # --- panel labels (tight; UPPERCASE where the English is) ------------------------------
    "panel.five_hour": "SESSÃO DE 5 H",
    "panel.five_hour_short": "5H",
    "panel.full_in": "cheio: {}",
    "panel.model": "{} SEMANAL",
    "panel.no_data": "Sem dados",
    "panel.pace": "{} vs ritmo",
    "panel.per_day": "{}%/dia",
    "panel.per_hour": "{}%/h",
    "panel.refreshing": "a obter dados",
    "panel.reset": "reset {}",
    "panel.retry_in": "de novo em {} s",
    "panel.updated": "atualizado: {}",
    "panel.week_short": "SEM.",
    "panel.weekly": "SEMANAL",
    # --- profile rows ----------------------------------------------------------------------
    "profile.extra": "Créditos de utilização: {}",
    "profile.plan": "Plano: {}",
    "profile.since": "Membro desde: {}",
    "profile.tier": "Nível de limite: {}",
    # --- Settings window -------------------------------------------------------------------
    "set.about": "{}\nSem telemetria. Só pede à Anthropic a tua própria utilização e lê o número da versão no servidor de atualizações.",
    "set.accent": "Cor de destaque",
    "set.always_top": "Por cima de todas as outras janelas",
    "set.auto": "automático",
    "set.backup_config": "Configuração do script de cópias",
    "set.backup_details": "A janela de detalhes mostra",
    "set.backup_disclaimer": "O Claude Usage Monitor apenas lê e mostra os registos das tuas cópias de segurança – não faz, não verifica nem garante nenhuma cópia. O Claude Backup Kit é um ponto de partida gratuito, oferecido como ajuda: qualquer pessoa pode alterar os scripts, pelo que não é possível garantir a qualidade de uma cópia nem que esteja completa. Não assumimos qualquer responsabilidade por cópias de segurança, perda de dados ou quaisquer danos. Garantir que as tuas cópias estão completas e podem ser restauradas é responsabilidade de cada um – faz um teste de restauro de vez em quando.",
    "set.backup_disclaimer_h": "Exclusão de responsabilidade",
    "set.backup_enabled": "Mostrar a barra de estado das cópias no painel",
    "set.backup_found": "Encontrado: {}",
    "set.backup_green": "Verde até",
    "set.backup_label": "Etiqueta junto à luz",
    "set.backup_lamps": "Luzes",
    "set.backup_root": "Pasta das cópias de segurança",
    "set.backup_tasks": "Filtro de tarefas agendadas",
    "set.backup_unconfigured": "Não está definida nenhuma pasta de cópias de segurança, por isso a barra de estado fica oculta. Escolhe a pasta onde o teu script de cópias escreve.",
    "set.backup_yellow": "Amarelo até",
    "set.browse": "Procurar…",
    "set.click_through": "Transparente aos cliques (só decorativo, ignora o rato)",
    "set.close": "Fechar",
    "set.color_hint": "As cores mudam com os limiares: verde → amarelo → vermelho.",
    "set.danger": "Crítico",
    "set.data_hint": "Registo local: o ficheiro plan-usage-history.json do Claude Desktop. Não precisa de início de sessão, mas só mede este PC e atualiza aproximadamente de 5 em 5 minutos.\n\nclaude.ai: depois de iniciares sessão, consulta o servidor. Vês a utilização de todos os teus dispositivos, com horas de reposição exatas e atualizações mais frequentes.",
    "set.datafile": "Ficheiro de dados",
    "set.default": "Predefinido",
    "set.details_api_only": "Estes dados vêm da origem claude.ai (é preciso iniciar sessão); o registo local não os contém.",
    "set.file_filter": "JSON (*.json);;Todos os ficheiros (*.*)",
    "set.gauge_order": "Ordem dos indicadores",
    "set.hours_suffix": " h",
    "set.layout": "Esquema",
    "set.local_models_hint": "O servidor só mantém um contador separado para alguns modelos (p. ex. Fable). Para os restantes, mostra como se reparte o trabalho desta semana no Claude Code neste PC – uma proporção da tua própria utilização e dos tokens de saída, não de um limite. Só são lidos o nome do modelo e as contagens de tokens, nunca a conversa.",
    "set.local_models_none": "Não foi encontrada nenhuma pasta de registos do Claude Code – este grupo fica simplesmente oculto. Nada mais é afetado.",
    "set.local_models_path": "Pasta de registos do Claude Code",
    "set.lock": "Bloquear posição (não arrastável)",
    "set.login_btn_in": "Terminar sessão no claude.ai",
    "set.login_btn_out": "Iniciar sessão no claude.ai…",
    "set.model_filter": "Modelo a acompanhar",
    "set.model_scale": "Tamanho do indicador do modelo",
    "set.not_set": "não definido",
    "set.notify_enabled": "Notificar ao ultrapassar um limiar",
    "set.notify_reset": "Notificar quando um limite é reposto",
    "set.notify_stale": "Notificar quando os dados ficam desatualizados",
    "set.opacity": "Opacidade",
    "set.open_config": "Abrir a pasta de definições",
    "set.pick_color": "Escolher cor…",
    "set.pick_file_title": "Escolher o registo de utilização",
    "set.profile": "Perfil / conta",
    "set.profile_auto": "Automático (último utilizado)",
    "set.profile_n": "Perfil {} – …{}",
    "set.refresh": "Intervalo de atualização",
    "set.reset_confirm": "Queres mesmo repor as predefinições?",
    "set.restore": "Repor predefinições",
    "set.rows_available": "O que pode ser mostrado agora – desmarca o que não queres ver:",
    "set.rows_none": "De momento, o servidor não envia mais limites para a tua conta. Assim que o fizer, aparecem aqui automaticamente.",
    "set.sec_suffix": " s",
    "set.show_age": "Atualidade dos dados",
    "set.show_burn": "Taxa de consumo (%/hora, %/dia)",
    "set.show_extra_usage": "Créditos de utilização (pagamento conforme o consumo)",
    "set.show_feedback_icon": "Ícone de mensagem no cabeçalho do painel",
    "set.show_five_hour": "Mostrar a sessão de 5 horas",
    "set.show_local_models": "Divisão entre modelos, a partir dos registos do Claude Code neste PC",
    "set.show_model": "Mostrar o limite semanal do modelo (origem claude.ai)",
    "set.show_model_list": "Limites semanais dos outros modelos",
    "set.show_plan_badge": "Emblema do plano no cabeçalho (Pro / Max…)",
    "set.show_plan_name": "Mostrar o meu nome no emblema",
    "set.show_reset": "Contagem decrescente até à reposição",
    "set.show_spark": "Curva de tendência (sparkline)",
    "set.show_surfaces": "Limites por superfície (Claude Code, aplicações ligadas…)",
    "set.show_weekly": "Mostrar o limite semanal",
    "set.size": "Tamanho",
    "set.snap": "Encostar à margem do ecrã",
    "set.source_api": "claude.ai – todos os dispositivos (requer início de sessão)",
    "set.source_label": "Origem da medição",
    "set.source_local": "Registo local – só este PC",
    "set.tab_alerts": "Alertas",
    "set.tab_appearance": "Aspeto",
    "set.tab_content": "Conteúdo",
    "set.tab_data": "Origem dos dados",
    "set.tab_details": "Detalhes",
    "set.tab_system": "Sistema",
    "set.taskbar": "Mostrar na barra de tarefas (como janela)",
    "set.theme": "Tema",
    "set.theme_default": "Predefinição do tema",
    "set.tip": "Dica: arrasta o painel com o botão esquerdo, Ctrl+roda redimensiona,\nbotão direito = menu, duplo clique = histórico.",
    "set.title": "definições",
    "set.tray_five": "Sessão de 5 horas",
    "set.tray_max": "O que for mais alto",
    "set.tray_value": "Valor do ícone da área de notificação",
    "set.tray_weekly": "Limite semanal",
    "set.update_check": "Procurar atualizações do programa automaticamente",
    "set.version": "Versão",
    "set.visible": "Painel flutuante visível",
    "set.warn": "Aviso",
    # --- sizes, sources, themes ------------------------------------------------------------
    "size.extra": "Muito grande",
    "size.large": "Grande",
    "size.normal": "Normal",
    "size.small": "Pequeno",
    "source.api": "claude.ai (todos os dispositivos)",
    "source.local": "Local (só este PC)",
    "theme.claude": "Claude (escuro quente)",
    "theme.graphite": "Grafite",
    "theme.midnight": "Vidro da meia-noite",
    "theme.neon": "Néon",
    "theme.paper": "Papel claro",
    "theme.postit": "Amarelo post-it",
    # --- time units (tight) ----------------------------------------------------------------
    "time.day": "{} d",
    "time.dh": "{}d {}h",
    "time.hm": "{}h {}min",
    "time.hour": "{} h",
    "time.m": "{}min",
    "time.min": "{} min",
    "time.none": "sem dados",
    "time.sec": "{} s",
    # --- tray tooltip ----------------------------------------------------------------------
    "tray.head": "5h: {}%   ·   Sem.: {}%",
    "tray.line": "{}: {}%",
    # --- program update --------------------------------------------------------------------
    "update.available": "Está disponível a versão {}.",
    "update.check_failed": "Não foi possível procurar atualizações: {}",
    "update.check_now": "Procurar agora",
    "update.checking": "A procurar atualizações…",
    "update.downloading": "A transferir… {} de {}",
    "update.failed": "A atualização falhou: {}",
    "update.install": "Instalar agora",
    "update.installed": "Versão instalada: {}",
    "update.later": "Mais tarde",
    "update.manual": "Esta cópia não consegue atualizar-se sozinha (é executada a partir do código-fonte ou de uma pasta só de leitura). Em alternativa, transfere o novo pacote.",
    "update.open_page": "Abrir a página de transferências",
    "update.restarting": "A instalar – a aplicação vai reiniciar dentro de instantes.",
    "update.skip": "Ignorar esta versão",
    "update.title": "Atualização do programa",
    "update.uptodate": "Tens a versão mais recente.",
    "update.verifying": "A verificar e a extrair…",
    "update.whats_new": "Novidades",
}

# macOS wording (Apple pt-PT): "Abrir ao iniciar sessão" (login items), "barra de menus" instead of the tray
STRINGS_MAC = {
    "menu.autostart": "Abrir ao iniciar sessão",
    "notify.autostart_on": "Ativado: a aplicação abre ao iniciar sessão.",
    "notify.autostart_off": "Desativado: a aplicação não abre ao iniciar sessão.",
    "notify.first_run": "O painel apareceu no canto superior direito.\nBotão direito no painel ou no ícone da barra de menus = menu.",
}
