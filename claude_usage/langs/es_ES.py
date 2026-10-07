# -*- coding: utf-8 -*-
"""Español (España) – UI strings of Claude Usage Monitor.

Every key of docs/i18n/source.json. Form of address: tú. Microsoft es-ES terminology for Windows,
Apple es-ES for the four macOS texts. Terms fixed in docs/i18n/glossary-es-ES.md.
"""

CODE = "es-ES"
NAME = "Español (España)"

STRINGS = {
    # --- backup status bar / details window ---------------------------------------------------
    "backup.age_d": "{}d",
    "backup.age_h": "{}h",
    "backup.age_m": "{}min",
    "backup.and_more": "…y {} más",
    "backup.checked_at": "Comprobado: {}",
    "backup.checking": "Comprobando…",
    "backup.cloud_only": "La instantánea está solo en línea en OneDrive; no se muestra su contenido para que no haga falta descargarla.",
    "backup.comp.cowork": "Registros de chat de Cowork (un ZIP por sesión)",
    "backup.comp.vault": "Instantánea de la bóveda de Obsidian (ZIP)",
    "backup.disclaimer_short": "El monitor solo muestra lo que dicen los registros de la copia de seguridad. No asumimos ninguna responsabilidad por las copias: comprobar que están completas y se pueden restaurar es cosa tuya.",
    "backup.done": "completado",
    "backup.dry_run": "(ejecución de prueba, no se ha subido nada)",
    "backup.failed": "ERROR",
    "backup.files_size": "{} archivos, {}",
    "backup.folders": "Carpetas",
    "backup.label_age": "Nombre y antigüedad",
    "backup.label_name": "Solo el nombre",
    "backup.label_none": "Solo las luces",
    "backup.last_ok": "Última copia correcta: {} (hace {})",
    "backup.last_run": "Última ejecución: {} – {}",
    "backup.legend": "Verde: {} h como máximo · Amarillo: hasta {} h · Rojo: más antigua o sin copia",
    "backup.level_green": "Reciente",
    "backup.level_none": "Sin copia de seguridad",
    "backup.level_red": "Demasiado antigua",
    "backup.level_yellow": "Algo antigua",
    "backup.log_file": "Archivo de registro",
    "backup.name.nextcloud": "Nextcloud",
    "backup.name.obsidian": "Obsidian",
    "backup.name.onedrive": "OneDrive",
    "backup.no_root": "No se ha encontrado la carpeta de copias de seguridad: {}",
    "backup.none_found": "Ninguno.",
    "backup.open": "abrir",
    "backup.rc_copied": "archivos nuevos o modificados copiados",
    "backup.rc_failed": "ERROR (código {})",
    "backup.rc_nochange": "al día, nada que copiar",
    "backup.recent_notes": "Últimas notas editadas en la instantánea",
    "backup.refresh": "Comprobar ahora",
    "backup.sec_components": "Qué se copia",
    "backup.sec_contents": "Contenido",
    "backup.sec_log": "Registro (últimas líneas)",
    "backup.sec_problems": "Errores y advertencias",
    "backup.sec_tasks": "Tareas programadas",
    "backup.skipped": "omitido (carpeta no encontrada)",
    "backup.snap_kept": "{} instantáneas conservadas, {} en total",
    "backup.snapshot": "Última instantánea",
    "backup.source": "Origen",
    "backup.state_error": "finalizada con errores",
    "backup.state_interrupted": "no ha finalizado",
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
    "backup.vault_changed": "{} notas han cambiado en la bóveda desde esta instantánea",
    "backup.zip_new": "{} ZIP nuevos o actualizados",
    "backup.zip_summary": "{} archivos ({} notas), {} sin comprimir",
    # --- details ----------------------------------------------------------------------------
    "detail.extra": "Créditos de uso",
    "detail.local_header": "CLAUDE CODE · ESTE EQUIPO · REPARTO DE LA SEMANA",
    "detail.off": "desactivado",
    "detail.on": "activado",
    "detail.surface.oauth_apps": "Aplicaciones conectadas",
    "detail.unlimited": "sin límite",
    # --- sign-in dialog ---------------------------------------------------------------------
    "dlg.cancel": "Cancelar",
    "dlg.checking": "Comprobando…",
    "dlg.err_badcode": "El código no se ha aceptado.\n\n{}\n\nComprueba que has pegado el código completo o vuelve a iniciar sesión en el navegador (siempre con un código nuevo).",
    "dlg.err_ratelimit": "Demasiados intentos de inicio de sesión en poco tiempo.\n\nEl servidor ha bloqueado los intentos temporalmente. Cierra esta ventana, espera entre 10 y 15 minutos (no lo intentes mientras tanto) y luego vuelve a iniciar sesión en el navegador UNA sola vez, con un código nuevo.",
    "dlg.hint1": "Inicia sesión en la página que se abre y autoriza el acceso. Al final recibirás un código.",
    "dlg.intro": "Inicia sesión en tu cuenta de claude.ai desde tu propio navegador (allí ya funcionan tus contraseñas y claves de acceso guardadas).",
    "dlg.login_title": "iniciar sesión",
    "dlg.open_browser": "Abrir el inicio de sesión en el navegador",
    "dlg.paste_label": "Pega aquí el código que has recibido:",
    "dlg.paste_placeholder": "pega aquí el código",
    "dlg.signin": "Iniciar sesión",
    "dlg.step1": "Paso 1",
    "dlg.step2": "Paso 2",
    "dlg.unknown_err": "Error desconocido.",
    # --- errors -----------------------------------------------------------------------------
    "err.already_running": "El programa ya se está ejecutando (mira en el área de notificación).",
    "err.bad_token_resp": "respuesta no válida del punto de conexión del token",
    "err.bad_usage_resp": "respuesta no válida del punto de conexión de uso",
    "err.connection": "error de conexión: {}",
    "err.file_empty": "El archivo de uso está vacío.",
    "err.file_not_found": "No se encuentra el archivo de uso.\n¿Está abierto Claude Desktop?",
    "err.file_unreadable": "El archivo de uso no se puede leer en este momento.",
    "err.loading": "Iniciando sesión / consultando…",
    "err.network": "error de red: {}",
    "err.no_code": "No has pegado ningún código.",
    "err.no_data_profile": "No hay datos para este perfil.",
    "err.no_tray": "El área de notificación no está disponible; se omite el icono.",
    "err.no_usage_data": "No hay datos de uso.",
    "err.not_signed_in": "No has iniciado sesión.",
    "err.query_http": "Error de consulta (HTTP {}).",
    "err.rate_limited": "El servidor está limitando las solicitudes (429); se volverá a intentar automáticamente.",
    "err.session_expired": "La sesión ha caducado; vuelve a iniciar sesión.",
    "err.session_expired_nl": "La sesión ha caducado.\nVuelve a iniciar sesión.",
    "err.signin_needed": "El inicio de sesión en claude.ai ha caducado.\nVuelve a iniciar sesión: clic derecho → Iniciar sesión en claude.ai",
    "err.unexpected": "Error inesperado: {}",
    # --- "Message to the developer" window --------------------------------------------------
    "fb.cancel": "Cancelar",
    "fb.close": "Cerrar",
    "fb.consent": "He leído y acepto la {}.",
    "fb.email": "Correo electrónico",
    "fb.email_hint": "solo si quieres que te responda",
    "fb.err_consent": "Para enviar, acepta la Política de privacidad.",
    "fb.err_email": "Esta dirección de correo no parece válida.",
    "fb.err_empty": "Primero escribe un mensaje o elige una valoración.",
    "fb.err_links": "Demasiados enlaces en el mensaje.",
    "fb.err_network": "No se ha podido conectar con claudeusagemonitor.com. Comprueba tu conexión y vuelve a intentarlo.",
    "fb.err_rate": "Demasiados mensajes en poco tiempo. Inténtalo de nuevo más tarde.",
    "fb.err_server": "El servidor no ha podido recibir el mensaje en este momento. Inténtalo de nuevo más tarde.",
    "fb.intro": "¿Una idea, un fallo o simplemente te gusta? Cuéntamelo. Todos los mensajes los leo yo, Vidovics Gábor, el autor.",
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
        "Qué se envía: lo que escribes aquí —nombre (opcional), dirección de correo electrónico (opcional), "
        "mensaje y valoración con estrellas— y, para que pueda entender el contexto: la versión del programa, "
        "el nombre y la versión del sistema operativo, el idioma de la interfaz y la hora del envío. El servidor "
        "no almacena ninguna dirección IP; para evitar abusos utiliza únicamente un hash que cambia a diario y "
        "que no permite recuperar la dirección."
        "\n\n"
        "Finalidad: leer y responder a tu mensaje y mejorar el programa (interés legítimo, art. 6.1.f) del RGPD; "
        "la propia respuesta, a petición tuya). Tu valoración y tu nombre solo aparecen en el sitio web si marcas "
        "la casilla específica para ello (consentimiento, art. 6.1.a) del RGPD) y solo después de que el autor los "
        "haya revisado; puedes retirar ese consentimiento en cualquier momento."
        "\n\n"
        "Plazo de conservación: los mensajes, 2 años como máximo; una valoración publicada, hasta que retires tu "
        "consentimiento. Si el autor ha activado el reenvío por correo electrónico, también llega una copia al "
        "buzón del autor."
        "\n\n"
        "Quién lo ve: únicamente el responsable del tratamiento y, como encargado del tratamiento, el proveedor de "
        "alojamiento (servidor en la UE, Alemania). No se vende ni se cede nada; no hay elaboración de perfiles ni "
        "decisiones automatizadas."
        "\n\n"
        "Tus derechos: acceso, rectificación, supresión, limitación del tratamiento, oposición, retirada del "
        "consentimiento y reclamación ante una autoridad de control (en Hungría: NAIH, naih.hu; en España: AEPD, "
        "aepd.es) o ante la autoridad de tu país. Contacto: este formulario o el sitio web."
        "\n\n"
        "Transmisión: cifrada (HTTPS/TLS) a claudeusagemonitor.com. Versión de este aviso: 6 de octubre de 2026."
    ),
    "fb.privacy_title": "Política de privacidad",
    "fb.publish": "Mi valoración y mi nombre (si lo indico) pueden mostrarse en claudeusagemonitor.com.",
    "fb.rating": "Valoración general",
    "fb.rating_clear": "borrar",
    "fb.rating_hint": "opcional: haz clic en una estrella",
    "fb.rating_tip": "{} de 5",
    "fb.secure": "Conexión cifrada (HTTPS) con claudeusagemonitor.com.",
    "fb.send": "Enviar",
    "fb.sending": "Enviando…",
    "fb.sent": "¡Gracias! Tu mensaje ha llegado.",
    "fb.sent_sub": "Leo todos los mensajes. Si has dejado una dirección de correo, te responderé a esa dirección.",
    "fb.title": "Mensaje al desarrollador",
    # --- Help window ------------------------------------------------------------------------
    "help.disclaimer": "Herramienta independiente y gratuita: no la ha creado Anthropic ni está vinculada a ella. «Claude» es una marca de Anthropic.",
    "help.feedback": "Preguntas, ideas, avisos de fallos: el formulario de mensajes del sitio web.",
    "help.free": "Gratis para siempre · licencia MIT · código abierto · sin telemetría",
    "help.guide": (
        "\n"
        "<h2>Qué muestra el widget</h2>\n"
        "<ul>\n"
        "<li><b>Sesión de 5 horas</b>: cuánto has consumido del límite de la sesión actual. Se reinicia cada cinco horas; el widget hace una cuenta atrás hasta el reinicio.</li>\n"
        "<li><b>Límite semanal</b>: el uso de todos los modelos juntos; se reinicia cada semana a una hora fija que depende de tu cuenta.</li>\n"
        "<li><b>Límite semanal por modelo</b>: un tercer medidor cuando el servidor informa de uno (por ejemplo, para un modelo concreto).</li>\n"
        "<li><b>Ritmo y velocidad de consumo</b>: a qué velocidad estás gastando el límite y si te durará hasta el reinicio; la previsión para el final de la semana te avisa a tiempo.</li>\n"
        "<li><b>Créditos de uso</b> y el distintivo de tu plan: si los activas en <i>Distintivo del plan y límites adicionales</i>.</li>\n"
        "</ul>\n"
        "<h2>De dónde salen los datos</h2>\n"
        "<ul>\n"
        "<li><b>claude.ai (todos los dispositivos)</b>: consulta el servidor de Anthropic, así que incluye el uso en el móvil, en el navegador y en otros ordenadores. Requiere iniciar sesión una sola vez en tu propio navegador (menú: <i>Iniciar sesión</i>). Se actualiza cada 2 minutos, o más despacio si el servidor lo pide.</li>\n"
        "<li><b>Local (solo este equipo)</b>: lee el registro de uso de Claude Desktop en este ordenador. No requiere iniciar sesión, pero solo conoce este equipo.</li>\n"
        "</ul>\n"
        "<p>Cambia de uno a otro en el menú: <i>Origen de datos</i>.</p>\n"
        "<h2>Cómo usar el widget</h2>\n"
        "<ul>\n"
        "<li><b>Clic derecho</b> en el widget (o en el icono del área de notificación): abre el menú completo.</li>\n"
        "<li><b>Doble clic</b> en un medidor: abre la ventana <b>Historial</b> (6 horas, 24 horas, 7 días o todo), con máximos, media diaria y previsión.</li>\n"
        "<li><b>Arrástralo</b> para moverlo; se ajusta a los bordes de la pantalla. <b>Ctrl + rueda del ratón</b>: lo agranda o lo reduce.</li>\n"
        "<li>Diseños: tarjeta pósit, barra fina y anillos; 6 temas. <i>Bloquear posición</i> e <i>Ignorar el ratón</i> están en Configuración.</li>\n"
        "</ul>\n"
        "<h2>Alertas</h2>\n"
        "<p>Amarillo a partir del 70 %, rojo a partir del 90 % (ajustable). Notificaciones opcionales cuando un límite se reinicia y cuando los datos se quedan desactualizados.</p>\n"
        "<h2>Copias de seguridad (opcional)</h2>\n"
        "<p>Las pequeñas luces muestran si tus copias de seguridad programadas se han ejecutado y han terminado. Haz clic en una luz para ver los detalles. El monitor solo lee los registros de las copias: hacerlas y probarlas es cosa tuya (consulta las Condiciones de uso).</p>\n"
        "<h2>Actualizaciones</h2>\n"
        "<p>El programa busca nuevas versiones por sí solo y se actualiza con un clic. Cada paquete se comprueba con SHA-256 y procede únicamente de <b>claudeusagemonitor.com</b>. Nuevas versiones y novedades: {site}</p>\n"
        "<h2>Privacidad</h2>\n"
        "<p>Sin telemetría ni seguimiento. Los datos de inicio de sesión de claude.ai se guardan cifrados únicamente en este ordenador; no se envía nada a ningún otro sitio.</p>\n"
        "<h2>Si algo no va bien</h2>\n"
        "<ul>\n"
        "<li><i>429 / limitado</i>: el servidor está frenando las solicitudes; el programa vuelve a intentarlo por sí solo.</li>\n"
        "<li>Sin datos: revisa el <i>Origen de datos</i>; con claude.ai, vuelve a iniciar sesión.</li>\n"
        "<li>El historial se conserva 7 días y se mantiene tras reinicios y actualizaciones.</li>\n"
        "<li>Registros y configuración: <code>{cfg}</code> (<code>api.log</code>, <code>update.log</code>).</li>\n"
        "</ul>\n"
    ),
    "help.made_by": "Creado por",
    "help.moved": "Nueva dirección desde el 21 de septiembre de 2026: la antigua página dinorr.hu/claude-usage-monitor redirige aquí.",
    "help.official": "SITIO WEB OFICIAL",
    "help.open_site": "Abrir claudeusagemonitor.com",
    "help.privacy": "Política de privacidad",
    "help.site_what": "Descargas, actualizaciones automáticas, novedades, el Claude Backup Kit, condiciones de uso y privacidad: todo en un solo sitio.",
    "help.source_code": "Código fuente (GitHub)",
    "help.tab_author": "Autor",
    "help.tab_guide": "Cómo funciona",
    "help.terms": "Condiciones de uso",
    "help.title": "Ayuda",
    "help.version": "Versión",
    # --- History window ---------------------------------------------------------------------
    "hist.legend_5h": "sesión de 5 h",
    "hist.legend_week": "límite semanal",
    "hist.no_data": "No hay datos suficientes para este periodo.",
    "hist.range_24h": "24 horas",
    "hist.range_6h": "6 horas",
    "hist.range_7d": "7 días",
    "hist.range_all": "Todo",
    "hist.stat_burn": "Consumo medio diario",
    "hist.stat_forecast": "Previsión al final de la semana",
    "hist.stat_now": "Uso semanal actual",
    "hist.stat_peak": "Máximo semanal",
    "hist.stat_sessions": "Sesiones de 5 h",
    "hist.title": "historial",
    # --- layouts ----------------------------------------------------------------------------
    "layout.compact": "Barra fina",
    "layout.postit": "Tarjeta pósit",
    "layout.ring": "Anillos",
    # --- context menu -----------------------------------------------------------------------
    "menu.always_top": "Siempre visible",
    "menu.autostart": "Iniciar con Windows",
    "menu.backup_bar": "Barra de estado de las copias",
    "menu.backups": "Copias de seguridad…",
    "menu.check_update": "Buscar actualizaciones del programa…",
    "menu.click_through": "Ignorar el ratón",
    "menu.details": "Distintivo del plan y límites adicionales",
    "menu.feedback": "Mensaje al desarrollador…",
    "menu.help": "Ayuda…",
    "menu.history": "Historial y estadísticas…",
    "menu.language": "Idioma",
    "menu.layout": "Diseño",
    "menu.locked": "Bloquear posición",
    "menu.login": "Iniciar sesión (claude.ai, navegador)…",
    "menu.logout": "Cerrar sesión",
    "menu.model_gauge": "Medidor de {}",
    "menu.order": "Orden",
    "menu.panel_visible": "Mostrar el panel",
    "menu.quit": "Salir",
    "menu.refresh": "Actualizar los datos de uso ahora",
    "menu.settings": "Configuración…",
    "menu.size": "Tamaño",
    "menu.source": "Origen de datos",
    "menu.start_menu": "Mostrar en el menú Inicio",
    "menu.theme": "Tema",
    "menu.update_available": "Actualización del programa: instalar la versión {}…",
    # --- desktop notifications --------------------------------------------------------------
    "notify.autostart_fail": "No se ha podido configurar el inicio automático.",
    "notify.autostart_off": "Desactivado: el programa no se iniciará con Windows.",
    "notify.autostart_on": "Activado: el programa se inicia con Windows.",
    "notify.first_run": "El panel ha aparecido en la esquina superior derecha.\nClic derecho en el panel o en el icono del área de notificación = menú.",
    "notify.login_ok": "Sesión iniciada: ya llegan los datos del servidor.",
    "notify.logout": "Sesión cerrada. Se ha cambiado al origen local.",
    "notify.reset_done": "{}: se ha reiniciado y empieza un nuevo periodo.",
    "notify.signin_needed": "El inicio de sesión en claude.ai ha caducado. Haz clic con el botón derecho en el panel y vuelve a iniciar sesión para seguir viendo el uso de todos tus dispositivos.",
    "notify.stale_body": "La última lectura es de hace {}. ¿Está abierto Claude Desktop?",
    "notify.stale_title": "Datos desactualizados",
    "notify.threshold": "{}: has usado el {} %.",
    "notify.update": "Ya está disponible la versión {} del programa. Clic derecho en el panel → Actualización del programa.",
    # --- floating panel labels (tight) ------------------------------------------------------
    "panel.five_hour": "SESIÓN DE 5 H",
    "panel.five_hour_short": "5 H",
    "panel.full_in": "lleno: {}",
    "panel.model": "{} SEMANAL",
    "panel.no_data": "Sin datos",
    "panel.pace": "{} vs ritmo",
    "panel.per_day": "{} %/día",
    "panel.per_hour": "{} %/h",
    "panel.refreshing": "actualizando",
    "panel.reset": "reinicio {}",
    "panel.retry_in": "reintento en {} s",
    "panel.updated": "actualizado: {}",
    "panel.week_short": "SEM.",
    "panel.weekly": "LÍMITE SEMANAL",
    # --- profile ----------------------------------------------------------------------------
    "profile.extra": "Créditos de uso: {}",
    "profile.plan": "Plan: {}",
    "profile.since": "Miembro desde: {}",
    "profile.tier": "Nivel de límite de uso: {}",
    # --- Settings window --------------------------------------------------------------------
    "set.about": "{}\nSin telemetría. Solo consulta tu propio uso a Anthropic y lee el número de versión en el servidor de actualizaciones.",
    "set.accent": "Color de énfasis",
    "set.always_top": "Por encima de las demás ventanas",
    "set.auto": "automático",
    "set.backup_config": "Configuración del script de copia",
    "set.backup_details": "La ventana de detalles muestra",
    "set.backup_disclaimer": "Claude Usage Monitor solo lee y muestra los registros de tu copia de seguridad: no crea, comprueba ni garantiza ninguna copia. El Claude Backup Kit es un punto de partida gratuito que se ofrece como ayuda: cualquiera puede modificar los scripts, por lo que no se puede garantizar la calidad ni la integridad de una copia. No asumimos ninguna responsabilidad por las copias de seguridad, la pérdida de datos ni ningún otro daño. Asegurarse de que las copias estén completas y se puedan restaurar es responsabilidad de cada uno: prueba una restauración de vez en cuando.",
    "set.backup_disclaimer_h": "Exención de responsabilidad",
    "set.backup_enabled": "Mostrar la barra de estado de las copias en el panel",
    "set.backup_found": "Encontrado: {}",
    "set.backup_green": "Verde hasta",
    "set.backup_label": "Etiqueta junto a la luz",
    "set.backup_lamps": "Luces",
    "set.backup_root": "Carpeta de copias de seguridad",
    "set.backup_tasks": "Filtro de tareas programadas",
    "set.backup_unconfigured": "No hay ninguna carpeta de copias configurada, así que la barra de estado permanece oculta. Elige la carpeta en la que escribe tu script de copia.",
    "set.backup_yellow": "Amarillo hasta",
    "set.browse": "Examinar…",
    "set.click_through": "Ignorar el ratón (solo decorativo, no recibe clics)",
    "set.close": "Cerrar",
    "set.color_hint": "Los colores cambian con los umbrales: verde → amarillo → rojo.",
    "set.danger": "Crítico",
    "set.data_hint": "Registro local: el archivo plan-usage-history.json de Claude Desktop. No requiere iniciar sesión, pero solo mide este equipo y se actualiza cada 5 minutos aproximadamente.\n\nclaude.ai: tras iniciar sesión, consulta el servidor. Ves el uso de todos tus dispositivos, con las horas de reinicio exactas y una actualización más frecuente.",
    "set.datafile": "Archivo de datos",
    "set.default": "Predeterminado",
    "set.details_api_only": "Estos datos proceden del origen claude.ai (requiere iniciar sesión); el registro local no los contiene.",
    "set.file_filter": "JSON (*.json);;Todos los archivos (*.*)",
    "set.gauge_order": "Orden de los medidores",
    "set.hours_suffix": " h",
    "set.layout": "Diseño",
    "set.local_models_hint": "El servidor solo lleva un contador aparte para algunos modelos (p. ej., Fable). Para los demás, esto muestra cómo se reparte el trabajo de Claude Code de esta semana en este equipo: es una parte de tu propio uso y de los tokens de salida, no de un límite. Solo se leen el nombre del modelo y los recuentos de tokens, nunca la conversación.",
    "set.local_models_none": "No se ha encontrado ninguna carpeta de registros de Claude Code; este grupo simplemente permanece oculto. No afecta a nada más.",
    "set.local_models_path": "Carpeta de registros de Claude Code",
    "set.lock": "Bloquear posición (no se puede arrastrar)",
    "set.login_btn_in": "Cerrar sesión en claude.ai",
    "set.login_btn_out": "Iniciar sesión en claude.ai…",
    "set.model_filter": "Modelo que mostrar",
    "set.model_scale": "Tamaño del medidor del modelo",
    "set.not_set": "sin configurar",
    "set.notify_enabled": "Avisar al cruzar un umbral",
    "set.notify_reset": "Avisar cuando se reinicie un límite",
    "set.notify_stale": "Avisar cuando los datos se queden desactualizados",
    "set.opacity": "Opacidad",
    "set.open_config": "Abrir la carpeta de configuración",
    "set.pick_color": "Elegir color…",
    "set.pick_file_title": "Elegir el registro de uso",
    "set.profile": "Perfil / cuenta",
    "set.profile_auto": "Automático (el último usado)",
    "set.profile_n": "Perfil {} – …{}",
    "set.refresh": "Intervalo de actualización",
    "set.reset_confirm": "¿Seguro que quieres restaurar la configuración predeterminada?",
    "set.restore": "Restaurar valores predeterminados",
    "set.rows_available": "Lo que se puede mostrar ahora mismo (desmarca lo que no quieras ver):",
    "set.rows_none": "Ahora mismo el servidor no envía más límites para tu cuenta. Aparecerán aquí por sí solos en cuanto lo haga.",
    "set.sec_suffix": " s",
    "set.show_age": "Antigüedad de los datos",
    "set.show_burn": "Velocidad de consumo (%/h, %/día)",
    "set.show_extra_usage": "Créditos de uso (pago por uso)",
    "set.show_feedback_icon": "Icono de mensaje en la cabecera del panel",
    "set.show_five_hour": "Mostrar la sesión de 5 horas",
    "set.show_local_models": "Reparto entre modelos, según los registros de Claude Code de este equipo",
    "set.show_model": "Mostrar el límite semanal del modelo (origen claude.ai)",
    "set.show_model_list": "Límites semanales de los demás modelos",
    "set.show_plan_badge": "Distintivo del plan en la cabecera (Pro / Max…)",
    "set.show_plan_name": "Mostrar mi nombre en el distintivo",
    "set.show_reset": "Cuenta atrás hasta el reinicio",
    "set.show_spark": "Curva de tendencia (minigráfico)",
    "set.show_surfaces": "Límites por herramienta (Claude Code, aplicaciones conectadas…)",
    "set.show_weekly": "Mostrar el límite semanal",
    "set.size": "Tamaño",
    "set.snap": "Ajustar a los bordes de la pantalla",
    "set.source_api": "claude.ai – todos los dispositivos (requiere iniciar sesión)",
    "set.source_label": "Origen de la medición",
    "set.source_local": "Registro local – solo este equipo",
    "set.tab_alerts": "Alertas",
    "set.tab_appearance": "Apariencia",
    "set.tab_content": "Contenido",
    "set.tab_data": "Origen de datos",
    "set.tab_details": "Detalles",
    "set.tab_system": "Sistema",
    "set.taskbar": "Mostrar en la barra de tareas (como una ventana)",
    "set.theme": "Tema",
    "set.theme_default": "Según el tema",
    "set.tip": "Consejo: arrastra el panel con el botón izquierdo; Ctrl + rueda cambia el tamaño,\nclic derecho = menú, doble clic = historial.",
    "set.title": "configuración",
    "set.tray_five": "Sesión de 5 horas",
    "set.tray_max": "El mayor de los dos",
    "set.tray_value": "Valor del icono del área de notificación",
    "set.tray_weekly": "Límite semanal",
    "set.update_check": "Buscar actualizaciones del programa automáticamente",
    "set.version": "Versión",
    "set.visible": "Panel flotante visible",
    "set.warn": "Advertencia",
    # --- sizes ------------------------------------------------------------------------------
    "size.extra": "Extragrande",
    "size.large": "Grande",
    "size.normal": "Normal",
    "size.small": "Pequeño",
    # --- data sources -----------------------------------------------------------------------
    "source.api": "claude.ai (todos los dispositivos)",
    "source.local": "Local (solo este equipo)",
    # --- themes -----------------------------------------------------------------------------
    "theme.claude": "Claude (oscuro cálido)",
    "theme.graphite": "Grafito",
    "theme.midnight": "Cristal de medianoche",
    "theme.neon": "Neón",
    "theme.paper": "Papel claro",
    "theme.postit": "Amarillo pósit",
    # --- time units -------------------------------------------------------------------------
    "time.day": "{} d",
    "time.dh": "{}d {}h",
    "time.hm": "{}h {}min",
    "time.hour": "{} h",
    "time.m": "{}min",
    "time.min": "{} min",
    "time.none": "sin datos",
    "time.sec": "{} s",
    # --- tray -------------------------------------------------------------------------------
    "tray.head": "5 h: {} %   ·   Sem.: {} %",
    "tray.line": "{}: {} %",
    # --- updates ----------------------------------------------------------------------------
    "update.available": "La versión {} ya está disponible.",
    "update.check_failed": "Error al buscar actualizaciones: {}",
    "update.check_now": "Buscar ahora",
    "update.checking": "Buscando actualizaciones…",
    "update.downloading": "Descargando… {} de {}",
    "update.failed": "La actualización ha fallado: {}",
    "update.install": "Instalar ahora",
    "update.installed": "Versión instalada: {}",
    "update.later": "Más tarde",
    "update.manual": "Esta copia no puede actualizarse sola (se ejecuta desde el código fuente o desde una carpeta de solo lectura). Descarga el paquete nuevo.",
    "update.open_page": "Abrir la página de descarga",
    "update.restarting": "Instalando: el programa se reiniciará enseguida.",
    "update.skip": "Omitir esta versión",
    "update.title": "Actualización del programa",
    "update.uptodate": "Tienes la última versión.",
    "update.verifying": "Verificando y descomprimiendo…",
    "update.whats_new": "Novedades",
}

# macOS wording (Apple es-ES): login items instead of "start with Windows", menu bar instead of tray
STRINGS_MAC = {
    "menu.autostart": "Abrir al iniciar sesión",
    "notify.autostart_on": "Activado: el programa se abre al iniciar sesión.",
    "notify.autostart_off": "Desactivado: el programa no se abrirá al iniciar sesión.",
    "notify.first_run": "El panel ha aparecido en la esquina superior derecha.\nClic derecho en el panel o en el icono de la barra de menús = menú.",
}
