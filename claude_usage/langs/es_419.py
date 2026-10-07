# -*- coding: utf-8 -*-
"""Español (Latinoamérica) – UI strings of Claude Usage Monitor.

Neutral Latin American Spanish (es-419): "tú", no voseo, Microsoft/Apple es-419 terminology
(computadora, mouse, Configuración, Iniciar sesión / Cerrar sesión). See docs/i18n/glossary-es-419.md.
"""

CODE = "es-419"
NAME = "Español (Latinoamérica)"

STRINGS = {
    # --- backup status bar / details window --------------------------------------------------
    "backup.age_d": "{}d",
    "backup.age_h": "{}h",
    "backup.age_m": "{}min",
    "backup.and_more": "…y {} más",
    "backup.checked_at": "Verificado: {}",
    "backup.checking": "Verificando…",
    "backup.cloud_only": "La instantánea está solo en línea en OneDrive; no se muestra su contenido para que no haya que descargarla.",
    "backup.comp.cowork": "Registros de chat de Cowork (un ZIP por sesión)",
    "backup.comp.vault": "Instantánea de la bóveda de Obsidian (ZIP)",
    "backup.disclaimer_short": "El monitor solo muestra lo que dicen los registros de la copia de seguridad. No asumimos responsabilidad por las copias: verificar que estén completas y se puedan restaurar depende de ti.",
    "backup.done": "listo",
    "backup.dry_run": "(prueba, no se subió nada)",
    "backup.failed": "ERROR",
    "backup.files_size": "{} archivos, {}",
    "backup.folders": "Carpetas",
    "backup.label_age": "Nombre y antigüedad",
    "backup.label_name": "Solo el nombre",
    "backup.label_none": "Solo indicadores",
    "backup.last_ok": "Última copia correcta: {} (hace {})",
    "backup.last_run": "Última ejecución: {} – {}",
    "backup.legend": "Verde: {} h o menos · Amarillo: hasta {} h · Rojo: más antigua, o sin copia",
    "backup.level_green": "Reciente",
    "backup.level_none": "No se encontró ninguna copia",
    "backup.level_red": "Desactualizada",
    "backup.level_yellow": "Algo antigua",
    "backup.log_file": "Archivo de registro",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "No se encontró la carpeta de copias de seguridad: {}",
    "backup.none_found": "Ninguno.",
    "backup.open": "abrir",
    "backup.rc_copied": "archivos nuevos o modificados copiados",
    "backup.rc_failed": "ERROR (código {})",
    "backup.rc_nochange": "al día, nada que copiar",
    "backup.recent_notes": "Notas editadas más recientemente en la instantánea",
    "backup.refresh": "Verificar ahora",
    "backup.sec_components": "Qué se incluye en la copia",
    "backup.sec_contents": "Contenido",
    "backup.sec_log": "Registro (últimas líneas)",
    "backup.sec_problems": "Errores y advertencias",
    "backup.sec_tasks": "Tareas programadas",
    "backup.skipped": "omitido (carpeta no encontrada)",
    "backup.snap_kept": "{} instantáneas conservadas, {} en total",
    "backup.snapshot": "Última instantánea",
    "backup.source": "Origen",
    "backup.state_error": "terminó con errores",
    "backup.state_interrupted": "no terminó",
    "backup.state_ok": "completada correctamente",
    "backup.state_running": "en ejecución",
    "backup.storage": "Almacenamiento remoto: {} usados de {}, {} libres",
    "backup.target": "Destino",
    "backup.task_event": "por evento",
    "backup.task_row": "última ejecución {} · resultado {} · próxima {}",
    "backup.tip_click": "Haz clic para ver los detalles",
    "backup.title": "Copias de seguridad",
    "backup.tray": "Copias: {}",
    "backup.uploaded": "Subidos en esta ejecución: {} nuevos, {} reemplazados, {} errores",
    "backup.uploaded_files": "Archivos subidos",
    "backup.uploaded_groups": "Archivos subidos por carpeta",
    "backup.uploaded_no": "Subido a Nextcloud: todavía no",
    "backup.uploaded_yes": "Subido a Nextcloud: sí ({})",
    "backup.vault": "Bóveda",
    "backup.vault_changed": "{} notas cambiaron en la bóveda desde esta instantánea",
    "backup.zip_new": "{} ZIP nuevos/actualizados",
    "backup.zip_summary": "{} archivos ({} notas), {} sin comprimir",
    # --- details ---------------------------------------------------------------------------
    "detail.extra": "Créditos de uso",
    "detail.local_header": "CLAUDE CODE · ESTA COMPUTADORA · DISTRIBUCIÓN DE LA SEMANA",
    "detail.off": "desactivado",
    "detail.on": "activado",
    "detail.surface.oauth_apps": "Apps conectadas",
    "detail.unlimited": "sin límite",
    # --- sign-in dialog --------------------------------------------------------------------
    "dlg.cancel": "Cancelar",
    "dlg.checking": "Verificando…",
    "dlg.err_badcode": "El código no fue aceptado.\n\n{}\n\nRevisa que hayas pegado el código completo o vuelve a iniciar sesión en el navegador (siempre con un código nuevo).",
    "dlg.err_ratelimit": "Demasiados intentos de inicio de sesión en poco tiempo.\n\nEl servidor te está limitando temporalmente. Cierra esta ventana, espera de 10 a 15 minutos (no lo intentes mientras tanto) y luego vuelve a iniciar sesión en el navegador UNA sola vez, con un código nuevo.",
    "dlg.hint1": "Inicia sesión en la página que se abre y autoriza el acceso. Al final recibirás un código.",
    "dlg.intro": "Inicia sesión en tu cuenta de claude.ai en tu propio navegador (ahí ya funcionan tus contraseñas y llaves de acceso guardadas).",
    "dlg.login_title": "iniciar sesión",
    "dlg.open_browser": "Abrir el inicio de sesión en el navegador",
    "dlg.paste_label": "Pega aquí el código que recibiste:",
    "dlg.paste_placeholder": "pega el código aquí",
    "dlg.signin": "Iniciar sesión",
    "dlg.step1": "Paso 1",
    "dlg.step2": "Paso 2",
    "dlg.unknown_err": "Error desconocido.",
    # --- errors ----------------------------------------------------------------------------
    "err.already_running": "La app ya se está ejecutando (revisa la bandeja del sistema).",
    "err.bad_token_resp": "respuesta no válida del endpoint de token",
    "err.bad_usage_resp": "respuesta no válida del endpoint de uso",
    "err.connection": "error de conexión: {}",
    "err.file_empty": "El archivo de uso está vacío.",
    "err.file_not_found": "No se encontró el archivo de uso.\n¿Claude Desktop está abierto?",
    "err.file_unreadable": "El archivo de uso no se puede leer en este momento.",
    "err.loading": "Iniciando sesión / consultando…",
    "err.network": "error de red: {}",
    "err.no_code": "No se pegó ningún código.",
    "err.no_data_profile": "No hay datos para este perfil.",
    "err.no_tray": "La bandeja del sistema no está disponible; se omite el ícono.",
    "err.no_usage_data": "No hay datos de uso.",
    "err.not_signed_in": "No has iniciado sesión.",
    "err.query_http": "Error de consulta (HTTP {}).",
    "err.rate_limited": "El servidor está limitando las solicitudes (429): se reintenta automáticamente.",
    "err.session_expired": "La sesión expiró; vuelve a iniciar sesión.",
    "err.session_expired_nl": "La sesión expiró.\nVuelve a iniciar sesión.",
    "err.signin_needed": "La sesión de claude.ai expiró.\nVuelve a iniciar sesión: clic derecho → Iniciar sesión en claude.ai",
    "err.unexpected": "Error inesperado: {}",
    # --- "Message to the developer" window -------------------------------------------------
    "fb.cancel": "Cancelar",
    "fb.close": "Cerrar",
    "fb.consent": "He leído y acepto la {}.",
    "fb.email": "Correo electrónico",
    "fb.email_hint": "solo si quieres recibir respuesta",
    "fb.err_consent": "Para enviar, acepta la Política de privacidad.",
    "fb.err_email": "Esta dirección de correo electrónico no parece válida.",
    "fb.err_empty": "Primero escribe un mensaje o elige una calificación.",
    "fb.err_links": "Hay demasiados enlaces en el mensaje.",
    "fb.err_network": "No se pudo conectar con claudeusagemonitor.com. Revisa tu conexión e inténtalo de nuevo.",
    "fb.err_rate": "Demasiados mensajes en poco tiempo. Inténtalo de nuevo más tarde.",
    "fb.err_server": "El servidor no pudo recibir el mensaje en este momento. Inténtalo de nuevo más tarde.",
    "fb.intro": "¿Una idea, un error o simplemente te gusta? Cuéntame. Cada mensaje lo leo yo, Vidovics Gábor, el autor del programa.",
    "fb.message": "Mensaje",
    "fb.message_ph": "¿Qué funciona, qué no y qué falta?",
    "fb.meta": "Junto con el mensaje se envían: la versión del programa ({0}), el sistema operativo ({1}) y el idioma de la interfaz ({2}).",
    "fb.name": "Nombre",
    "fb.optional": "(opcional)",
    "fb.privacy_hide": "Ocultar el aviso",
    "fb.privacy_text": (
        "Responsable del tratamiento: Vidovics Gábor, persona física (Hungría), autor de Claude Usage Monitor. "
        "La política de privacidad completa está en el sitio web: https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "Qué se envía: lo que escribes aquí –nombre (opcional), correo electrónico (opcional), mensaje y "
        "calificación con estrellas– y, para que yo pueda entender el contexto: la versión del programa, el nombre "
        "y la versión del sistema operativo, el idioma de la interfaz y la hora de envío. El servidor no almacena "
        "ninguna dirección IP; para prevenir abusos usa únicamente un hash que cambia cada día y que no puede "
        "convertirse de nuevo en una dirección."
        "\n\n"
        "Para qué: para leer y responder tu mensaje y para mejorar el programa (interés legítimo, art. 6.1, "
        "letra f) del RGPD; la respuesta en sí, a solicitud tuya). Tu calificación y tu nombre aparecen en el sitio "
        "web solo si marcas la casilla específica para ello (consentimiento, art. 6.1, letra a) del RGPD) y solo "
        "después de que el autor los haya revisado; puedes retirar ese consentimiento en cualquier momento."
        "\n\n"
        "Por cuánto tiempo: los mensajes, 2 años como máximo; una calificación publicada, hasta que retires tu "
        "consentimiento. Si el autor activó el reenvío por correo electrónico, también llega una copia a su buzón."
        "\n\n"
        "Quién lo ve: solo el responsable del tratamiento y, como encargado del tratamiento, el proveedor de "
        "hosting (servidor en la UE, Alemania). Nada se vende ni se cede a terceros; no hay elaboración de perfiles "
        "ni decisiones automatizadas."
        "\n\n"
        "Tus derechos: acceso, rectificación, supresión, limitación del tratamiento, oposición, retiro del "
        "consentimiento y presentación de una reclamación ante una autoridad de control (en Hungría: NAIH, naih.hu) "
        "o ante la autoridad de tu país. Contacto: este formulario o el sitio web."
        "\n\n"
        "Transmisión: cifrada (HTTPS/TLS) hacia claudeusagemonitor.com. Versión de este aviso: 6 de octubre de 2026."
    ),
    "fb.privacy_title": "Política de privacidad",
    "fb.publish": "Mi calificación y mi nombre (si lo indiqué) pueden mostrarse en claudeusagemonitor.com.",
    "fb.rating": "Calificación general",
    "fb.rating_clear": "borrar",
    "fb.rating_hint": "opcional: haz clic en una estrella",
    "fb.rating_tip": "{} de 5",
    "fb.secure": "Conexión cifrada (HTTPS) con claudeusagemonitor.com.",
    "fb.send": "Enviar",
    "fb.sending": "Enviando…",
    "fb.sent": "¡Gracias, tu mensaje llegó!",
    "fb.sent_sub": "Leo todos los mensajes. Si dejaste un correo electrónico, te responderé ahí.",
    "fb.title": "Mensaje al desarrollador",
    # --- Help window -----------------------------------------------------------------------
    "help.disclaimer": "Una herramienta independiente y gratuita: no fue creada por Anthropic ni está afiliada a ella. “Claude” es una marca de Anthropic.",
    "help.feedback": "Preguntas, ideas, reportes de errores: el formulario de mensajes del sitio web.",
    "help.free": "Gratis para siempre · licencia MIT · código abierto · sin telemetría",
    "help.guide": (
        "\n"
        "<h2>Qué muestra el widget</h2>\n"
        "<ul>\n"
        "<li><b>Sesión de 5 horas</b> – qué parte del límite de tu sesión actual ya usaste. Se reinicia cada cinco horas; "
        "el widget lleva la cuenta regresiva hasta el reinicio.</li>\n"
        "<li><b>Límite semanal</b> – el uso de todos los modelos juntos; se reinicia a una hora fija de la semana, "
        "propia de tu cuenta.</li>\n"
        "<li><b>Límite semanal por modelo</b> – un tercer indicador cuando el servidor informa uno (p. ej., para un "
        "modelo específico).</li>\n"
        "<li><b>Ritmo y velocidad de consumo</b> – qué tan rápido estás usando el límite y si te alcanzará hasta el "
        "reinicio; la proyección al cierre de la semana te avisa a tiempo.</li>\n"
        "<li><b>Créditos de uso</b> y la insignia de tu plan – cuando los activas en <i>Insignia del plan y límites "
        "adicionales</i>.</li>\n"
        "</ul>\n"
        "<h2>De dónde vienen los datos</h2>\n"
        "<ul>\n"
        "<li><b>claude.ai (todos los dispositivos)</b> – consulta el servidor de Anthropic, así que incluye el uso en "
        "tu celular, en el navegador y en otras computadoras. Requiere iniciar sesión una sola vez en tu propio "
        "navegador (menú: <i>Iniciar sesión</i>). Se actualiza cada 2 minutos, o con menos frecuencia si el servidor lo pide.</li>\n"
        "<li><b>Local (solo esta computadora)</b> – lee el registro de uso de Claude Desktop en esta computadora. "
        "No requiere iniciar sesión, pero solo conoce esta computadora.</li>\n"
        "</ul>\n"
        "<p>Cambia entre ambos en el menú: <i>Fuente de datos</i>.</p>\n"
        "<h2>Cómo usar el widget</h2>\n"
        "<ul>\n"
        "<li><b>Clic derecho</b> en el widget (o en el ícono de la bandeja) – el menú completo.</li>\n"
        "<li><b>Doble clic</b> en un indicador – la ventana <b>Historial</b>: 6 horas, 24 horas, 7 días o todo, con "
        "picos, promedio diario y una proyección.</li>\n"
        "<li><b>Arrástralo</b> para moverlo; se ajusta a los bordes de la pantalla. <b>Ctrl + rueda del mouse</b> – "
        "más grande o más pequeño.</li>\n"
        "<li>Diseños: tarjeta post-it, barra delgada, anillos; 6 temas. <i>Fijar posición</i> e <i>Ignorar clics</i> "
        "están en Configuración.</li>\n"
        "</ul>\n"
        "<h2>Alertas</h2>\n"
        "<p>Amarillo a partir del 70 %, rojo a partir del 90 % (ajustable). Notificaciones opcionales cuando un límite "
        "se reinicia y cuando los datos se están quedando desactualizados.</p>\n"
        "<h2>Copias de seguridad (opcional)</h2>\n"
        "<p>Los pequeños indicadores luminosos muestran si tus copias de seguridad programadas se ejecutaron y "
        "terminaron. Haz clic en un indicador para ver los detalles. El monitor solo lee los registros de las copias: "
        "hacer y probar las copias es tu responsabilidad (consulta los Términos de uso).</p>\n"
        "<h2>Actualizaciones</h2>\n"
        "<p>El programa busca versiones nuevas por sí solo y se actualiza con un clic. Cada paquete se verifica con "
        "SHA-256 y proviene únicamente de <b>claudeusagemonitor.com</b>. Versiones nuevas y notas de la versión: {site}</p>\n"
        "<h2>Privacidad</h2>\n"
        "<p>Sin telemetría ni rastreo. El inicio de sesión de claude.ai se guarda cifrado solo en esta computadora; "
        "no se envía nada a ningún otro lugar.</p>\n"
        "<h2>Si algo no funciona</h2>\n"
        "<ul>\n"
        "<li><i>429 / limitado</i> – el servidor está frenando las solicitudes; el programa reintenta por sí solo.</li>\n"
        "<li>Sin datos – revisa la <i>Fuente de datos</i>; con claude.ai, vuelve a iniciar sesión.</li>\n"
        "<li>El historial se conserva 7 días y sobrevive a reinicios y actualizaciones.</li>\n"
        "<li>Registros y configuración: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Creado por",
    "help.moved": "Nueva dirección desde el 21 de septiembre de 2026: la antigua página dinorr.hu/claude-usage-monitor redirige aquí.",
    "help.official": "SITIO WEB OFICIAL",
    "help.open_site": "Abrir claudeusagemonitor.com",
    "help.privacy": "Política de privacidad",
    "help.site_what": "Descargas, actualizaciones automáticas, novedades, el Claude Backup Kit, términos de uso y privacidad: todo en un solo lugar.",
    "help.source_code": "Código fuente (GitHub)",
    "help.tab_author": "Autor",
    "help.tab_guide": "Cómo funciona",
    "help.terms": "Términos de uso",
    "help.title": "Ayuda",
    "help.version": "Versión",
    # --- History window --------------------------------------------------------------------
    "hist.legend_5h": "sesión de 5 h",
    "hist.legend_week": "límite semanal",
    "hist.no_data": "No hay datos suficientes para este período.",
    "hist.range_24h": "24 horas",
    "hist.range_6h": "6 horas",
    "hist.range_7d": "7 días",
    "hist.range_all": "Todo",
    "hist.stat_burn": "Consumo diario promedio",
    "hist.stat_forecast": "Proyección al cierre de la semana",
    "hist.stat_now": "Semana actual",
    "hist.stat_peak": "Pico semanal",
    "hist.stat_sessions": "Sesiones de 5 h",
    "hist.title": "historial",
    # --- layouts ---------------------------------------------------------------------------
    "layout.compact": "Barra delgada",
    "layout.postit": "Tarjeta post-it",
    "layout.ring": "Anillos",
    # --- context menu ----------------------------------------------------------------------
    "menu.always_top": "Siempre visible",
    "menu.autostart": "Iniciar con Windows",
    "menu.backup_bar": "Barra de estado de copias",
    "menu.backups": "Copias de seguridad…",
    "menu.check_update": "Buscar actualizaciones del programa…",
    "menu.click_through": "Ignorar clics",
    "menu.details": "Insignia del plan y límites adicionales",
    "menu.feedback": "Mensaje al desarrollador…",
    "menu.help": "Ayuda…",
    "menu.history": "Historial y estadísticas…",
    "menu.language": "Idioma",
    "menu.layout": "Diseño",
    "menu.locked": "Fijar posición",
    "menu.login": "Iniciar sesión (claude.ai, navegador)…",
    "menu.logout": "Cerrar sesión",
    "menu.model_gauge": "Indicador de {}",
    "menu.order": "Orden",
    "menu.panel_visible": "Mostrar panel",
    "menu.quit": "Salir",
    "menu.refresh": "Actualizar datos de uso ahora",
    "menu.settings": "Configuración…",
    "menu.size": "Tamaño",
    "menu.source": "Fuente de datos",
    "menu.start_menu": "Mostrar en el menú Inicio",
    "menu.theme": "Tema",
    "menu.update_available": "Actualización del programa: instalar la versión {}…",
    # --- desktop notifications -------------------------------------------------------------
    "notify.autostart_fail": "No se pudo configurar el inicio automático.",
    "notify.autostart_off": "Desactivado: la app no se iniciará con Windows.",
    "notify.autostart_on": "Activado: la app se inicia con Windows.",
    "notify.first_run": "El panel apareció en la esquina superior derecha.\nClic derecho en el panel o en el ícono de la bandeja = menú.",
    "notify.login_ok": "Sesión iniciada: ya llegan los datos del servidor.",
    "notify.logout": "Sesión cerrada. Se cambió a la fuente local.",
    "notify.reset_done": "{}: se reinició — comenzó un nuevo período.",
    "notify.signin_needed": "La sesión de claude.ai expiró. Haz clic derecho en el panel y vuelve a iniciar sesión para seguir viendo el uso de todos tus dispositivos.",
    "notify.stale_body": "La última lectura es de hace {}. ¿Claude Desktop está abierto?",
    "notify.stale_title": "Datos desactualizados",
    "notify.threshold": "{}: {}% usado.",
    "notify.update": "Está disponible la versión {} del programa. Clic derecho en el panel → Actualización del programa.",
    # --- panel labels (tight space, UPPERCASE where the English is) ------------------------
    "panel.five_hour": "SESIÓN DE 5 H",
    "panel.five_hour_short": "5H",
    "panel.full_in": "lleno: {}",
    "panel.model": "{} SEMANAL",
    "panel.no_data": "Sin datos",
    "panel.pace": "{} vs ritmo",
    "panel.per_day": "{}%/día",
    "panel.per_hour": "{}%/h",
    "panel.refreshing": "actualizando",
    "panel.reset": "reinicio {}",
    "panel.retry_in": "reintento en {} s",
    "panel.updated": "actualizado: {}",
    "panel.week_short": "SEM.",
    "panel.weekly": "LÍMITE SEMANAL",
    # --- profile ---------------------------------------------------------------------------
    "profile.extra": "Créditos de uso: {}",
    "profile.plan": "Plan: {}",
    "profile.since": "Miembro desde: {}",
    "profile.tier": "Nivel de límite de uso: {}",
    # --- Settings window -------------------------------------------------------------------
    "set.about": "{}\nSin telemetría. Solo le pide a Anthropic tu propio uso y lee el número de versión del servidor de actualizaciones.",
    "set.accent": "Color de énfasis",
    "set.always_top": "Sobre todas las demás ventanas",
    "set.auto": "automático",
    "set.backup_config": "Configuración del script de copias",
    "set.backup_details": "La ventana de detalles muestra",
    "set.backup_disclaimer": "Claude Usage Monitor solo lee y muestra los registros de tu copia de seguridad: no crea, verifica ni garantiza ninguna copia. El Claude Backup Kit es un punto de partida gratuito que se ofrece como ayuda: cualquiera puede modificar los scripts, por lo que no se puede garantizar la calidad ni la integridad de una copia. No asumimos ninguna responsabilidad por las copias de seguridad, la pérdida de datos ni ningún daño. Asegurarse de que las copias estén completas y se puedan restaurar es responsabilidad de cada usuario: prueba una restauración de vez en cuando.",
    "set.backup_disclaimer_h": "Descargo de responsabilidad",
    "set.backup_enabled": "Mostrar la barra de estado de copias en el panel",
    "set.backup_found": "Encontrado: {}",
    "set.backup_green": "Verde hasta",
    "set.backup_label": "Etiqueta junto al indicador",
    "set.backup_lamps": "Indicadores",
    "set.backup_root": "Carpeta de copias de seguridad",
    "set.backup_tasks": "Filtro de tareas programadas",
    "set.backup_unconfigured": "No hay una carpeta de copias configurada, así que la barra de estado permanece oculta. Elige la carpeta en la que escribe tu script de copias.",
    "set.backup_yellow": "Amarillo hasta",
    "set.browse": "Examinar…",
    "set.click_through": "Ignorar clics (solo decorativo, no responde al mouse)",
    "set.close": "Cerrar",
    "set.color_hint": "Los colores cambian según los umbrales: verde → amarillo → rojo.",
    "set.danger": "Crítico",
    "set.data_hint": "Registro local: el archivo plan-usage-history.json de Claude Desktop. No requiere iniciar sesión, pero solo mide esta computadora y se actualiza cada 5 minutos aproximadamente.\n\nclaude.ai: después de iniciar sesión, consulta el servidor. Ves el uso de todos tus dispositivos, con horas de reinicio exactas y actualizaciones más frecuentes.",
    "set.datafile": "Archivo de datos",
    "set.default": "Predeterminado",
    "set.details_api_only": "Estos datos vienen de la fuente claude.ai (requiere iniciar sesión); el registro local no los incluye.",
    "set.file_filter": "JSON (*.json);;Todos los archivos (*.*)",
    "set.gauge_order": "Orden de los indicadores",
    "set.hours_suffix": " h",
    "set.layout": "Diseño",
    "set.local_models_hint": "El servidor solo lleva un contador aparte para algunos modelos (p. ej., Fable). Para los demás, esto muestra cómo se distribuye el trabajo de Claude Code de esta semana en esta computadora: una proporción de tu propio uso y de los tokens de salida, no una parte de un límite. Solo se leen el nombre del modelo y los recuentos de tokens, nunca la conversación.",
    "set.local_models_none": "No se encontró ninguna carpeta de registros de Claude Code: este grupo simplemente queda oculto. Nada más se ve afectado.",
    "set.local_models_path": "Carpeta de registros de Claude Code",
    "set.lock": "Fijar posición (no se puede arrastrar)",
    "set.login_btn_in": "Cerrar sesión de claude.ai",
    "set.login_btn_out": "Iniciar sesión en claude.ai…",
    "set.model_filter": "Modelo a monitorear",
    "set.model_scale": "Tamaño del indicador del modelo",
    "set.not_set": "sin definir",
    "set.notify_enabled": "Notificar al cruzar un umbral",
    "set.notify_reset": "Notificar cuando un límite se reinicie",
    "set.notify_stale": "Notificar cuando los datos estén desactualizados",
    "set.opacity": "Opacidad",
    "set.open_config": "Abrir la carpeta de configuración",
    "set.pick_color": "Elegir color…",
    "set.pick_file_title": "Elegir el registro de uso",
    "set.profile": "Perfil / cuenta",
    "set.profile_auto": "Automático (el último usado)",
    "set.profile_n": "Perfil {} – …{}",
    "set.refresh": "Intervalo de actualización",
    "set.reset_confirm": "¿Seguro que quieres restablecer la configuración predeterminada?",
    "set.restore": "Restablecer predeterminados",
    "set.rows_available": "Lo que se puede mostrar ahora (desmarca lo que no quieras ver):",
    "set.rows_none": "Por ahora el servidor no envía más límites para tu cuenta. Aparecerán aquí automáticamente en cuanto lo haga.",
    "set.sec_suffix": " s",
    "set.show_age": "Antigüedad de los datos",
    "set.show_burn": "Velocidad de consumo (%/h, %/día)",
    "set.show_extra_usage": "Créditos de uso (pago por uso)",
    "set.show_feedback_icon": "Ícono de mensaje en el encabezado del panel",
    "set.show_five_hour": "Mostrar la sesión de 5 horas",
    "set.show_local_models": "Distribución entre modelos, según los registros de Claude Code en esta computadora",
    "set.show_model": "Mostrar el límite semanal del modelo (fuente claude.ai)",
    "set.show_model_list": "Límites semanales de los demás modelos",
    "set.show_plan_badge": "Insignia del plan en el encabezado (Pro / Max…)",
    "set.show_plan_name": "Mostrar mi nombre en la insignia",
    "set.show_reset": "Cuenta regresiva hasta el reinicio",
    "set.show_spark": "Curva de tendencia (minigráfico)",
    "set.show_surfaces": "Límites por producto (Claude Code, apps conectadas…)",
    "set.show_weekly": "Mostrar el límite semanal",
    "set.size": "Tamaño",
    "set.snap": "Ajustar al borde de la pantalla",
    "set.source_api": "claude.ai – todos los dispositivos (requiere iniciar sesión)",
    "set.source_label": "Fuente de medición",
    "set.source_local": "Registro local – solo esta computadora",
    "set.tab_alerts": "Alertas",
    "set.tab_appearance": "Apariencia",
    "set.tab_content": "Contenido",
    "set.tab_data": "Fuente de datos",
    "set.tab_details": "Detalles",
    "set.tab_system": "Sistema",
    "set.taskbar": "Mostrar en la barra de tareas (como ventana)",
    "set.theme": "Tema",
    "set.theme_default": "Según el tema",
    "set.tip": "Consejo: arrastra el panel con el botón izquierdo, Ctrl+rueda cambia el tamaño,\nclic derecho = menú, doble clic = historial.",
    "set.title": "configuración",
    "set.tray_five": "Sesión de 5 horas",
    "set.tray_max": "El que sea mayor",
    "set.tray_value": "Valor del ícono de la bandeja",
    "set.tray_weekly": "Límite semanal",
    "set.update_check": "Buscar actualizaciones del programa automáticamente",
    "set.version": "Versión",
    "set.visible": "Panel flotante visible",
    "set.warn": "Advertencia",
    # --- sizes, sources, themes ------------------------------------------------------------
    "size.extra": "Extra",
    "size.large": "Grande",
    "size.normal": "Normal",
    "size.small": "Pequeño",
    "source.api": "claude.ai (todos los dispositivos)",
    "source.local": "Local (solo esta computadora)",
    "theme.claude": "Claude (oscuro cálido)",
    "theme.graphite": "Grafito",
    "theme.midnight": "Cristal de medianoche",
    "theme.neon": "Neón",
    "theme.paper": "Papel claro",
    "theme.postit": "Amarillo post-it",
    # --- time units ------------------------------------------------------------------------
    "time.day": "{} d",
    "time.dh": "{}d {}h",
    "time.hm": "{}h {}min",
    "time.hour": "{} h",
    "time.m": "{}min",
    "time.min": "{} min",
    "time.none": "sin datos",
    "time.sec": "{} s",
    # --- tray ------------------------------------------------------------------------------
    "tray.head": "5 h: {}%   ·   Sem.: {}%",
    "tray.line": "{}: {}%",
    # --- updater ---------------------------------------------------------------------------
    "update.available": "La versión {} está disponible.",
    "update.check_failed": "No se pudieron buscar actualizaciones: {}",
    "update.check_now": "Buscar ahora",
    "update.checking": "Buscando actualizaciones…",
    "update.downloading": "Descargando… {} de {}",
    "update.failed": "La actualización falló: {}",
    "update.install": "Instalar ahora",
    "update.installed": "Versión instalada: {}",
    "update.later": "Más tarde",
    "update.manual": "Esta copia no puede actualizarse sola (se ejecuta desde el código fuente o desde una carpeta de solo lectura). Descarga el paquete nuevo.",
    "update.open_page": "Abrir la página de descarga",
    "update.restarting": "Instalando: la app se reiniciará en un momento.",
    "update.skip": "Omitir esta versión",
    "update.title": "Actualización del programa",
    "update.uptodate": "Tienes la versión más reciente.",
    "update.verifying": "Verificando y descomprimiendo…",
    "update.whats_new": "Novedades",
}

# macOS wording (Apple es-419 terminology): "Abrir al iniciar sesión" instead of "Iniciar con Windows",
# "barra de menús" instead of the tray
STRINGS_MAC = {
    "menu.autostart": "Abrir al iniciar sesión",
    "notify.autostart_on": "Activado: la app se abre al iniciar sesión.",
    "notify.autostart_off": "Desactivado: la app no se abrirá al iniciar sesión.",
    "notify.first_run": "El panel apareció en la esquina superior derecha.\nClic derecho en el panel o en el ícono de la barra de menús = menú.",
}
