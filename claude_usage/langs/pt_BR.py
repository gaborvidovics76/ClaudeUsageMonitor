# -*- coding: utf-8 -*-
"""Português (Brasil) – UI strings of Claude Usage Monitor."""

CODE = "pt-BR"
NAME = "Português (Brasil)"

STRINGS = {
    # --- backup status bar / details window ------------------------------------------------
    "backup.age_d": "{}d",
    "backup.age_h": "{}h",
    "backup.age_m": "{}min",
    "backup.and_more": "…e mais {}",
    "backup.checked_at": "Verificado: {}",
    "backup.checking": "Verificando…",
    "backup.cloud_only": "O instantâneo está disponível somente online no OneDrive; o conteúdo não é listado para não precisar baixá-lo.",
    "backup.comp.cowork": "Logs de conversa do Cowork (um ZIP por sessão)",
    "backup.comp.vault": "Instantâneo do cofre do Obsidian (ZIP)",
    "backup.disclaimer_short": "O monitor só mostra o que os logs de backup informam. Não assumimos responsabilidade pelos backups – verificar se estão completos e se podem ser restaurados é com você.",
    "backup.done": "concluído",
    "backup.dry_run": "(execução de teste, nada foi enviado)",
    "backup.failed": "FALHOU",
    "backup.files_size": "{} arquivos, {}",
    "backup.folders": "Pastas",
    "backup.label_age": "Nome e idade",
    "backup.label_name": "Só o nome",
    "backup.label_none": "Só as luzes",
    "backup.last_ok": "Último backup bem-sucedido: {} (há {})",
    "backup.last_run": "Última execução: {} – {}",
    "backup.legend": "Verde: no máximo {} h · Amarelo: até {} h · Vermelho: mais antigo ou sem backup",
    "backup.level_green": "Recente",
    "backup.level_none": "Nenhum backup encontrado",
    "backup.level_red": "Desatualizado",
    "backup.level_yellow": "Ficando antigo",
    "backup.log_file": "Arquivo de log",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "Pasta de backup não encontrada: {}",
    "backup.none_found": "Nenhum.",
    "backup.open": "abrir",
    "backup.rc_copied": "arquivos novos ou alterados copiados",
    "backup.rc_failed": "FALHOU (código {})",
    "backup.rc_nochange": "atualizado, nada a copiar",
    "backup.recent_notes": "Notas editadas mais recentemente no instantâneo",
    "backup.refresh": "Verificar agora",
    "backup.sec_components": "O que está no backup",
    "backup.sec_contents": "Conteúdo",
    "backup.sec_log": "Log (últimas linhas)",
    "backup.sec_problems": "Erros e avisos",
    "backup.sec_tasks": "Tarefas agendadas",
    "backup.skipped": "ignorado (pasta não encontrada)",
    "backup.snap_kept": "{} instantâneos mantidos, {} no total",
    "backup.snapshot": "Instantâneo mais recente",
    "backup.source": "Origem",
    "backup.state_error": "terminou com erros",
    "backup.state_interrupted": "não terminou",
    "backup.state_ok": "concluído com sucesso",
    "backup.state_running": "em execução agora",
    "backup.storage": "Armazenamento remoto: {} usados de {}, {} livres",
    "backup.target": "Destino",
    "backup.task_event": "em um evento",
    "backup.task_row": "última execução {} · resultado {} · próxima {}",
    "backup.tip_click": "Clique para ver os detalhes",
    "backup.title": "Backups",
    "backup.tray": "Backups: {}",
    "backup.uploaded": "Enviado nesta execução: {} novos, {} substituídos, {} erros",
    "backup.uploaded_files": "Arquivos enviados",
    "backup.uploaded_groups": "Arquivos enviados por pasta",
    "backup.uploaded_no": "Enviado para o Nextcloud: ainda não",
    "backup.uploaded_yes": "Enviado para o Nextcloud: sim ({})",
    "backup.vault": "Cofre",
    "backup.vault_changed": "{} notas alteradas no cofre desde este instantâneo",
    "backup.zip_new": "{} ZIP novos/atualizados",
    "backup.zip_summary": "{} arquivos ({} notas), {} descompactados",
    # --- details rows -----------------------------------------------------------------------
    "detail.extra": "Créditos de uso",
    "detail.local_header": "CLAUDE CODE · ESTE PC · DIVISÃO DESTA SEMANA",
    "detail.off": "desativado",
    "detail.on": "ativado",
    "detail.surface.oauth_apps": "Aplicativos conectados",
    "detail.unlimited": "sem limite",
    # --- sign-in dialog ---------------------------------------------------------------------
    "dlg.cancel": "Cancelar",
    "dlg.checking": "Verificando…",
    "dlg.err_badcode": "O código não foi aceito.\n\n{}\n\nVerifique se você colou o código inteiro ou tente fazer login de novo pelo navegador (sempre com um código novo).",
    "dlg.err_ratelimit": "Muitas tentativas de login em pouco tempo.\n\nO servidor está limitando você temporariamente. Feche esta janela, aguarde 10–15 minutos (sem tentar nesse meio-tempo) e só então faça UM novo login pelo navegador, com um código novo.",
    "dlg.hint1": "Faça login na página que abrir e autorize o acesso. No final, você vai receber um código.",
    "dlg.intro": "Entre na sua conta do claude.ai no seu próprio navegador (suas senhas e chaves de acesso salvas já funcionam lá).",
    "dlg.login_title": "entrar",
    "dlg.open_browser": "Abrir o login no navegador",
    "dlg.paste_label": "Cole aqui o código que você recebeu:",
    "dlg.paste_placeholder": "cole o código aqui",
    "dlg.signin": "Entrar",
    "dlg.step1": "Etapa 1",
    "dlg.step2": "Etapa 2",
    "dlg.unknown_err": "Erro desconhecido.",
    # --- error messages ---------------------------------------------------------------------
    "err.already_running": "O aplicativo já está em execução (veja a bandeja do sistema).",
    "err.bad_token_resp": "resposta inválida do endpoint de token",
    "err.bad_usage_resp": "resposta inválida do endpoint de uso",
    "err.connection": "erro de conexão: {}",
    "err.file_empty": "O arquivo de uso está vazio.",
    "err.file_not_found": "Arquivo de uso não encontrado.\nO Claude Desktop está aberto?",
    "err.file_unreadable": "O arquivo de uso não pode ser lido no momento.",
    "err.loading": "Entrando / consultando…",
    "err.network": "erro de rede: {}",
    "err.no_code": "Nenhum código colado.",
    "err.no_data_profile": "Sem dados para este perfil.",
    "err.no_tray": "Bandeja do sistema indisponível; o ícone da bandeja não será exibido.",
    "err.no_usage_data": "Sem dados de uso.",
    "err.not_signed_in": "Não conectado.",
    "err.query_http": "Erro na consulta (HTTP {}).",
    "err.rate_limited": "O servidor está limitando as requisições (429) – tentando de novo automaticamente.",
    "err.session_expired": "A sessão expirou, entre novamente.",
    "err.session_expired_nl": "A sessão expirou.\nEntre novamente.",
    "err.signin_needed": "O login no claude.ai expirou.\nEntre novamente: botão direito → Entrar no claude.ai",
    "err.unexpected": "Erro inesperado: {}",
    # --- "Message to the developer" window --------------------------------------------------
    "fb.cancel": "Cancelar",
    "fb.close": "Fechar",
    "fb.consent": "Li e aceito a {}.",
    "fb.email": "E-mail",
    "fb.email_hint": "só se você quiser uma resposta",
    "fb.err_consent": "Para enviar, aceite a Política de Privacidade.",
    "fb.err_email": "Este endereço de e-mail não parece válido.",
    "fb.err_empty": "Escreva uma mensagem ou escolha uma avaliação primeiro.",
    "fb.err_links": "Links demais na mensagem.",
    "fb.err_network": "Não foi possível acessar claudeusagemonitor.com. Verifique sua conexão e tente de novo.",
    "fb.err_rate": "Muitas mensagens em pouco tempo – tente de novo mais tarde.",
    "fb.err_server": "O servidor não conseguiu receber a mensagem agora. Tente de novo mais tarde.",
    "fb.intro": "Tem uma ideia, achou um bug ou simplesmente gostou? Me conte. Eu, Vidovics Gábor, o autor, leio todas as mensagens.",
    "fb.message": "Mensagem",
    "fb.message_ph": "O que funciona, o que não funciona, o que está faltando?",
    "fb.meta": "Enviados junto com a mensagem: versão do programa {0}, sistema operacional ({1}), idioma da interface ({2}).",
    "fb.name": "Nome",
    "fb.optional": "(opcional)",
    "fb.privacy_hide": "Ocultar o aviso",
    "fb.privacy_text": (
        "Controlador: Vidovics Gábor, pessoa física (Hungria), autor do Claude Usage Monitor. "
        "A Política de Privacidade completa está no site: https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "O que é enviado: o que você digita aqui – nome (opcional), endereço de e-mail (opcional), mensagem, "
        "avaliação em estrelas – e, para que eu entenda o contexto: a versão do programa, o nome e a versão do "
        "sistema operacional, o idioma da interface e a data e hora do envio. O servidor não armazena endereço IP; "
        "para prevenir abusos, usa apenas um hash que muda diariamente e que não pode ser convertido de volta em "
        "um endereço."
        "\n\n"
        "Finalidade: ler e responder à sua mensagem e melhorar o programa (legítimo interesse, art. 6(1)(f) do "
        "GDPR/RGPD; a resposta em si, a seu pedido). Sua avaliação e seu nome só aparecem no site se você marcar "
        "a caixa específica para isso (consentimento, art. 6(1)(a)), e somente depois de o autor revisá-los; você "
        "pode revogar esse consentimento a qualquer momento."
        "\n\n"
        "Por quanto tempo: as mensagens, por no máximo 2 anos; uma avaliação publicada, até você revogar o "
        "consentimento. Se o autor tiver ativado o encaminhamento por e-mail, uma cópia também chega à caixa de "
        "entrada do autor."
        "\n\n"
        "Quem tem acesso: apenas o controlador e – como operador – o provedor de hospedagem (servidor na UE, Alemanha). "
        "Nada é vendido nem repassado; não há criação de perfis nem decisões automatizadas."
        "\n\n"
        "Seus direitos: acesso, retificação, eliminação, limitação do tratamento, oposição, revogação do "
        "consentimento e reclamação a uma autoridade de controle (na Hungria: NAIH, naih.hu) ou à autoridade do "
        "seu país. Contato: este formulário ou o site."
        "\n\n"
        "Transmissão: criptografada (HTTPS/TLS) para claudeusagemonitor.com. Versão deste aviso: 06/10/2026."
    ),
    "fb.privacy_title": "Política de Privacidade",
    "fb.publish": "Minha avaliação e meu nome (se informado) podem ser exibidos em claudeusagemonitor.com.",
    "fb.rating": "Avaliação geral",
    "fb.rating_clear": "limpar",
    "fb.rating_hint": "opcional – clique em uma estrela",
    "fb.rating_tip": "{} de 5",
    "fb.secure": "Conexão criptografada (HTTPS) com claudeusagemonitor.com.",
    "fb.send": "Enviar",
    "fb.sending": "Enviando…",
    "fb.sent": "Obrigado – sua mensagem chegou!",
    "fb.sent_sub": "Eu leio todas as mensagens. Se você deixou um endereço de e-mail, respondo por lá.",
    "fb.title": "Mensagem para o desenvolvedor",
    # --- Help window ------------------------------------------------------------------------
    "help.disclaimer": "Uma ferramenta independente e gratuita – não foi feita pela Anthropic nem tem vínculo com ela. “Claude” é uma marca registrada da Anthropic.",
    "help.feedback": "Dúvidas, ideias, relatos de bugs: o formulário de mensagem no site.",
    "help.free": "Gratuito para sempre · licença MIT · código aberto · sem telemetria",
    "help.guide": (
        "\n"
        "<h2>O que o widget mostra</h2>\n"
        "<ul>\n"
        "<li><b>Sessão de 5 horas</b> – quanto do limite da sessão atual já foi usado. Ele é redefinido a cada cinco horas; o widget faz a contagem regressiva até a redefinição.</li>\n"
        "<li><b>Limite semanal</b> – o uso de todos os modelos juntos; é redefinido em um horário semanal fixo da sua conta.</li>\n"
        "<li><b>Limite semanal por modelo</b> – um terceiro medidor, quando o servidor informa um (por exemplo, para um modelo específico).</li>\n"
        "<li><b>Ritmo e taxa de consumo</b> – com que rapidez você está gastando o limite e se ele vai durar até a redefinição; a projeção para o fim da semana avisa a tempo.</li>\n"
        "<li><b>Créditos de uso</b> e o selo do seu plano – quando você os ativa em <i>Selo do plano e limites extras</i>.</li>\n"
        "</ul>\n"
        "<h2>De onde vêm os dados</h2>\n"
        "<ul>\n"
        "<li><b>claude.ai (todos os dispositivos)</b> – consulta o servidor da Anthropic, então inclui o uso no celular, no navegador e em outros computadores. Exige fazer login uma única vez no seu próprio navegador (menu: <i>Entrar</i>). Atualiza a cada 2 minutos, mais devagar se o servidor pedir.</li>\n"
        "<li><b>Local (só este PC)</b> – lê o log de uso do Claude Desktop neste computador. Sem login, mas só conhece este PC.</li>\n"
        "</ul>\n"
        "<p>Alterne entre eles no menu: <i>Fonte de dados</i>.</p>\n"
        "<h2>Como usar o widget</h2>\n"
        "<ul>\n"
        "<li><b>Botão direito</b> no widget (ou no ícone da bandeja) – o menu completo.</li>\n"
        "<li><b>Clique duplo</b> em um medidor – a janela <b>Histórico</b>: 6 horas, 24 horas, 7 dias ou tudo, com picos, média diária e projeção.</li>\n"
        "<li><b>Arraste</b> para mover; ele se encaixa nas bordas da tela. <b>Ctrl + roda do mouse</b> – maior ou menor.</li>\n"
        "<li>Layouts: cartão post-it, barra fina, anéis; 6 temas. <i>Fixar posição</i> e <i>Transparente ao mouse</i> ficam nas Configurações.</li>\n"
        "</ul>\n"
        "<h2>Alertas</h2>\n"
        "<p>Amarelo a partir de 70%, vermelho a partir de 90% (ajustável). Notificações opcionais quando um limite é redefinido e quando os dados estão ficando antigos.</p>\n"
        "<h2>Backups (opcional)</h2>\n"
        "<p>As pequenas luzes mostram se os seus backups agendados rodaram e terminaram. Clique em uma luz para ver os detalhes. O monitor só lê os logs de backup – fazer e testar os backups é responsabilidade sua (veja os Termos de Uso).</p>\n"
        "<h2>Atualizações</h2>\n"
        "<p>O programa procura novas versões sozinho e se atualiza com um clique. Cada pacote é verificado com SHA-256 e vem somente de <b>claudeusagemonitor.com</b>. Novas versões e notas de lançamento: {site}</p>\n"
        "<h2>Privacidade</h2>\n"
        "<p>Sem telemetria, sem rastreamento. O login do claude.ai fica armazenado criptografado só neste computador; nada é enviado para nenhum outro lugar.</p>\n"
        "<h2>Se algo der errado</h2>\n"
        "<ul>\n"
        "<li><i>429 / limitação de taxa</i> – o servidor está desacelerando as requisições; o programa tenta de novo sozinho.</li>\n"
        "<li>Sem dados – verifique a <i>Fonte de dados</i>; com o claude.ai, entre novamente.</li>\n"
        "<li>O histórico fica guardado por 7 dias, mesmo após reinicializações e atualizações.</li>\n"
        "<li>Logs e configurações: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Feito por",
    "help.moved": "Novo endereço desde 21 de setembro de 2026 – a antiga página dinorr.hu/claude-usage-monitor redireciona para cá.",
    "help.official": "SITE OFICIAL",
    "help.open_site": "Abrir claudeusagemonitor.com",
    "help.privacy": "Política de Privacidade",
    "help.site_what": "Downloads, atualizações automáticas, novidades, o Claude Backup Kit, termos de uso e privacidade – tudo em um só lugar.",
    "help.source_code": "Código-fonte (GitHub)",
    "help.tab_author": "Autor",
    "help.tab_guide": "Como funciona",
    "help.terms": "Termos de Uso",
    "help.title": "Ajuda",
    "help.version": "Versão",
    # --- History window ---------------------------------------------------------------------
    "hist.legend_5h": "sessão de 5 horas",
    "hist.legend_week": "limite semanal",
    "hist.no_data": "Não há dados suficientes para este período.",
    "hist.range_24h": "24 horas",
    "hist.range_6h": "6 horas",
    "hist.range_7d": "7 dias",
    "hist.range_all": "Tudo",
    "hist.stat_burn": "Consumo médio diário",
    "hist.stat_forecast": "Projeção para o fim da semana",
    "hist.stat_now": "Uso semanal atual",
    "hist.stat_peak": "Pico semanal",
    "hist.stat_sessions": "Sessões de 5 horas",
    "hist.title": "histórico",
    # --- layouts ----------------------------------------------------------------------------
    "layout.compact": "Barra fina",
    "layout.postit": "Cartão post-it",
    "layout.ring": "Anéis",
    # --- context menu -----------------------------------------------------------------------
    "menu.always_top": "Sempre no topo",
    "menu.autostart": "Iniciar com o Windows",
    "menu.backup_bar": "Barra de status dos backups",
    "menu.backups": "Backups…",
    "menu.check_update": "Verificar atualizações do programa…",
    "menu.click_through": "Transparente ao mouse",
    "menu.details": "Selo do plano e limites extras",
    "menu.feedback": "Mensagem para o desenvolvedor…",
    "menu.help": "Ajuda…",
    "menu.history": "Histórico e estatísticas…",
    "menu.language": "Idioma",
    "menu.layout": "Layout",
    "menu.locked": "Fixar posição",
    "menu.login": "Entrar (claude.ai, navegador)…",
    "menu.logout": "Sair da conta",
    "menu.model_gauge": "Medidor {}",
    "menu.order": "Ordem",
    "menu.panel_visible": "Mostrar painel",
    "menu.quit": "Sair",
    "menu.refresh": "Atualizar dados de uso agora",
    "menu.settings": "Configurações…",
    "menu.size": "Tamanho",
    "menu.source": "Fonte de dados",
    "menu.start_menu": "Mostrar no menu Iniciar",
    "menu.theme": "Tema",
    "menu.update_available": "Atualização do programa: instalar a versão {}…",
    # --- desktop notifications --------------------------------------------------------------
    "notify.autostart_fail": "Não foi possível configurar a inicialização automática.",
    "notify.autostart_off": "Desativado: o aplicativo não vai iniciar com o Windows.",
    "notify.autostart_on": "Ativado: o aplicativo inicia com o Windows.",
    "notify.first_run": "O painel apareceu no canto superior direito da tela.\nBotão direito no painel ou no ícone da bandeja = menu.",
    "notify.login_ok": "Conectado – os dados do servidor estão chegando.",
    "notify.logout": "Você saiu da conta. O painel mudou para a fonte local.",
    "notify.reset_done": "{}: redefinido — um novo período começou.",
    "notify.signin_needed": "O login no claude.ai expirou. Clique com o botão direito no painel e entre novamente para continuar vendo o uso de todos os seus dispositivos.",
    "notify.stale_body": "A última leitura foi há {}. O Claude Desktop está aberto?",
    "notify.stale_title": "Dados desatualizados",
    "notify.threshold": "{}: {}% usados.",
    "notify.update": "A versão {} do programa está disponível. Botão direito no painel → Atualização do programa.",
    # --- floating panel labels (tight space, UPPERCASE) -------------------------------------
    "panel.five_hour": "SESSÃO DE 5 H",
    "panel.five_hour_short": "5H",
    "panel.full_in": "cheio: {}",
    "panel.model": "{} SEMANAL",
    "panel.no_data": "Sem dados",
    "panel.pace": "{} vs ritmo",
    "panel.per_day": "{}%/dia",
    "panel.per_hour": "{}%/h",
    "panel.refreshing": "atualizando",
    "panel.reset": "zera {}",
    "panel.retry_in": "repete em {} s",
    "panel.updated": "atualizado: {}",
    "panel.week_short": "SEM.",
    "panel.weekly": "LIMITE SEMANAL",
    # --- profile ----------------------------------------------------------------------------
    "profile.extra": "Créditos de uso: {}",
    "profile.plan": "Plano: {}",
    "profile.since": "Membro desde: {}",
    "profile.tier": "Nível de limite de taxa: {}",
    # --- Settings window --------------------------------------------------------------------
    "set.about": "{}\nSem telemetria. O programa só consulta a Anthropic sobre o seu próprio uso e lê o número da versão no servidor de atualizações.",
    "set.accent": "Cor de destaque",
    "set.always_top": "Acima de todas as outras janelas",
    "set.auto": "automático",
    "set.backup_config": "Configuração do script de backup",
    "set.backup_details": "A janela de detalhes mostra",
    "set.backup_disclaimer": "O Claude Usage Monitor só lê e exibe os logs do seu backup – ele não faz, não verifica nem garante backup nenhum. O Claude Backup Kit é um ponto de partida gratuito, oferecido como ajuda: qualquer pessoa pode alterar os scripts, por isso não é possível garantir a qualidade nem a completude de um backup. Não assumimos nenhuma responsabilidade por backups, perda de dados ou qualquer outro dano. Garantir que os seus backups estejam completos e possam ser restaurados é responsabilidade de cada um – teste uma restauração de vez em quando.",
    "set.backup_disclaimer_h": "Isenção de responsabilidade",
    "set.backup_enabled": "Mostrar a barra de status dos backups no painel",
    "set.backup_found": "Encontrado: {}",
    "set.backup_green": "Verde até",
    "set.backup_label": "Rótulo ao lado da luz",
    "set.backup_lamps": "Luzes",
    "set.backup_root": "Pasta de backup",
    "set.backup_tasks": "Filtro de tarefas agendadas",
    "set.backup_unconfigured": "Nenhuma pasta de backup foi definida, por isso a barra de status fica oculta. Escolha a pasta em que o seu script de backup grava.",
    "set.backup_yellow": "Amarelo até",
    "set.browse": "Procurar…",
    "set.click_through": "Transparente ao mouse (só decorativo, ignora o mouse)",
    "set.close": "Fechar",
    "set.color_hint": "As cores mudam conforme os limiares: verde → amarelo → vermelho.",
    "set.danger": "Crítico",
    "set.data_hint": "Log local: o plan-usage-history.json do Claude Desktop. Sem login, mas mede só este PC e atualiza a cada 5 minutos, aproximadamente.\n\nclaude.ai: depois do login, consulta o servidor. Você vê o uso de todos os seus dispositivos, com horários exatos de redefinição e atualização mais frequente.",
    "set.datafile": "Arquivo de dados",
    "set.default": "Padrão",
    "set.details_api_only": "Estes vêm da fonte de dados claude.ai (exige login); o log local não os contém.",
    "set.file_filter": "JSON (*.json);;Todos os arquivos (*.*)",
    "set.gauge_order": "Ordem dos medidores",
    "set.hours_suffix": " h",
    "set.layout": "Layout",
    "set.local_models_hint": "O servidor só mantém um contador separado para alguns modelos (por exemplo, o Fable). Para os outros, isto mostra como o trabalho desta semana no Claude Code neste PC se divide – uma parcela do seu próprio uso e dos tokens de saída, não uma parcela de um limite. Só o nome do modelo e as contagens de tokens são lidos, nunca a conversa.",
    "set.local_models_none": "Nenhuma pasta de logs do Claude Code foi encontrada – este grupo simplesmente fica oculto. Nada mais é afetado.",
    "set.local_models_path": "Pasta de logs do Claude Code",
    "set.lock": "Fixar posição (não arrastável)",
    "set.login_btn_in": "Sair do claude.ai",
    "set.login_btn_out": "Entrar no claude.ai…",
    "set.model_filter": "Modelo a acompanhar",
    "set.model_scale": "Tamanho do medidor do modelo",
    "set.not_set": "não definido",
    "set.notify_enabled": "Notificar ao cruzar um limiar",
    "set.notify_reset": "Notificar quando um limite for redefinido",
    "set.notify_stale": "Notificar quando os dados ficarem desatualizados",
    "set.opacity": "Opacidade",
    "set.open_config": "Abrir pasta de configurações",
    "set.pick_color": "Escolher cor…",
    "set.pick_file_title": "Escolher o log de uso",
    "set.profile": "Perfil / conta",
    "set.profile_auto": "Automático (último usado)",
    "set.profile_n": "Perfil {} – …{}",
    "set.refresh": "Atualizar a cada",
    "set.reset_confirm": "Tem certeza de que deseja restaurar as configurações padrão?",
    "set.restore": "Restaurar padrões",
    "set.rows_available": "O que pode ser mostrado agora – desmarque o que você não quer ver:",
    "set.rows_none": "No momento, o servidor não envia outros limites para a sua conta. Eles aparecem aqui automaticamente assim que forem enviados.",
    "set.sec_suffix": " s",
    "set.show_age": "Atualidade dos dados",
    "set.show_burn": "Taxa de consumo (%/hora, %/dia)",
    "set.show_extra_usage": "Créditos de uso (pagamento por uso)",
    "set.show_feedback_icon": "Ícone de mensagem no cabeçalho do painel",
    "set.show_five_hour": "Mostrar sessão de 5 horas",
    "set.show_local_models": "Divisão entre os modelos, a partir dos logs do Claude Code neste PC",
    "set.show_model": "Mostrar limite semanal do modelo (fonte claude.ai)",
    "set.show_model_list": "Limites semanais dos outros modelos",
    "set.show_plan_badge": "Selo do plano no cabeçalho (Pro / Max…)",
    "set.show_plan_name": "Mostrar meu nome no selo",
    "set.show_reset": "Contagem regressiva até a redefinição",
    "set.show_spark": "Curva de tendência (sparkline)",
    "set.show_surfaces": "Limites por superfície (Claude Code, aplicativos conectados…)",
    "set.show_weekly": "Mostrar limite semanal",
    "set.size": "Tamanho",
    "set.snap": "Encaixar na borda da tela",
    "set.source_api": "claude.ai – todos os dispositivos (exige login)",
    "set.source_label": "Fonte da medição",
    "set.source_local": "Log local – só este PC",
    "set.tab_alerts": "Alertas",
    "set.tab_appearance": "Aparência",
    "set.tab_content": "Conteúdo",
    "set.tab_data": "Fonte de dados",
    "set.tab_details": "Detalhes",
    "set.tab_system": "Sistema",
    "set.taskbar": "Mostrar na barra de tarefas (como janela)",
    "set.theme": "Tema",
    "set.theme_default": "Padrão do tema",
    "set.tip": "Dica: arraste o painel com o botão esquerdo, Ctrl+roda redimensiona,\nbotão direito = menu, clique duplo = histórico.",
    "set.title": "configurações",
    "set.tray_five": "Sessão de 5 horas",
    "set.tray_max": "O que for maior",
    "set.tray_value": "Valor do ícone da bandeja",
    "set.tray_weekly": "Limite semanal",
    "set.update_check": "Verificar atualizações do programa automaticamente",
    "set.version": "Versão",
    "set.visible": "Painel flutuante visível",
    "set.warn": "Aviso",
    # --- sizes, sources, themes -------------------------------------------------------------
    "size.extra": "Extra",
    "size.large": "Grande",
    "size.normal": "Normal",
    "size.small": "Pequeno",
    "source.api": "claude.ai (todos os dispositivos)",
    "source.local": "Local (só este PC)",
    "theme.claude": "Claude (escuro quente)",
    "theme.graphite": "Grafite",
    "theme.midnight": "Vidro meia-noite",
    "theme.neon": "Neon",
    "theme.paper": "Papel claro",
    "theme.postit": "Amarelo post-it",
    # --- time formats (panel) ---------------------------------------------------------------
    "time.day": "{} d",
    "time.dh": "{}d {}h",
    "time.hm": "{}h {}min",
    "time.hour": "{} h",
    "time.m": "{}min",
    "time.min": "{} min",
    "time.none": "sem dados",
    "time.sec": "{} s",
    # --- tray -------------------------------------------------------------------------------
    "tray.head": "5h: {}%   ·   Sem.: {}%",
    "tray.line": "{}: {}%",
    # --- program update ---------------------------------------------------------------------
    "update.available": "A versão {} está disponível.",
    "update.check_failed": "Não foi possível verificar atualizações: {}",
    "update.check_now": "Verificar agora",
    "update.checking": "Verificando atualizações…",
    "update.downloading": "Baixando… {} de {}",
    "update.failed": "A atualização falhou: {}",
    "update.install": "Instalar agora",
    "update.installed": "Versão instalada: {}",
    "update.later": "Mais tarde",
    "update.manual": "Esta cópia não consegue se atualizar sozinha (ela roda a partir do código-fonte ou de uma pasta somente leitura). Baixe o novo pacote manualmente.",
    "update.open_page": "Abrir página de download",
    "update.restarting": "Instalando – o aplicativo reinicia em instantes.",
    "update.skip": "Pular esta versão",
    "update.title": "Atualização do programa",
    "update.uptodate": "Você já tem a versão mais recente.",
    "update.verifying": "Verificando e descompactando…",
    "update.whats_new": "Novidades",
}

# macOS wording (Apple pt-BR): "abrir ao fazer login" instead of "iniciar com o Windows", menu bar instead of tray
STRINGS_MAC = {
    "menu.autostart": "Abrir ao fazer login",
    "notify.autostart_on": "Ativado: o aplicativo abre quando você faz login.",
    "notify.autostart_off": "Desativado: o aplicativo não vai abrir ao fazer login.",
    "notify.first_run": "O painel apareceu no canto superior direito da tela.\nBotão direito no painel ou no ícone da barra de menus = menu.",
}
