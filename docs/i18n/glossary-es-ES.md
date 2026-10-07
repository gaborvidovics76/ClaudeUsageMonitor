# Glossary – Español (España) – `es-ES`

Scope: the whole UI of Claude Usage Monitor (all 358 keys of `source.json` + the 4 macOS overrides),
written into `claude_usage/langs/es_ES.py`. The old `legacy → es-ES` texts were only a starting point;
every line was reviewed against the English and brought in line with this glossary.

## Tone and form of address

- **tú**, everywhere, without exception (`Comprueba tu conexión`, `Inténtalo de nuevo`, `es cosa tuya`).
  Never *usted*, never *vosotros* (the user is one person). This is how Microsoft, Apple, Google and the
  big Spanish consumer apps speak to the user in Spain today.
- Imperatives in the 2nd person singular: *Inicia sesión*, *Comprueba*, *Elige*, *Pega aquí*.
- The author speaks in the first person where the English does (*Cuéntamelo*, *Leo todos los mensajes*).
- Peninsular grammar: present perfect for recent events (*ha caducado*, *se ha reiniciado*, *no se ha
  encontrado*) – not the Latin-American preterite (*caducó*, *se reinició*). *Ordenador*, *ratón*,
  *archivo*, *carpeta*, *contraseña*, *descargar*, *móvil*, *vale*-register avoided in UI.
- **Microsoft es-ES terminology** for everything Windows: *Configuración*, *Iniciar sesión / Cerrar sesión*,
  *barra de tareas*, *área de notificación*, *menú Inicio*, *Examinar…*, *Restaurar valores predeterminados*,
  *Color de énfasis*, *Siempre visible*, *punto de conexión*, *distintivo*, *actualizar* (refresh),
  *clic con el botón derecho* (short form *clic derecho* in tight notifications).
- **Apple es-ES terminology** for the four `STRINGS_MAC` texts: *Abrir al iniciar sesión* (login items),
  *barra de menús*.
- Short, friendly, confident – like the English. Error texts are plain sentences, no exclamation marks
  except the single *¡Gracias!* after sending a message.
- Punctuation and typography of Spain: opening *¿ ¡*, «comillas latinas» for the trademark quote; where the
  English uses a dash, a colon for "term – explanation" (help lists, hints), the RAE *raya* attached to the
  inciso (*—nombre, … estrellas—*) for parentheticals, and *entre 10 y 15* for ranges in running text; the
  spaced en dash *–* only as a separator inside short labels (*Registro local – solo este equipo*), a **space before the percent sign** (*70 %*, *{} %*), the same space
  before unit symbols (*5 h*, *{} min*, *{} s*) except in the compact packed forms (`{}h {}min`) that mirror
  the English spacing. Decimal and date formats are not in the strings; the notice date is written
  *6 de octubre de 2026*.

## Name of the privacy document

**Política de privacidad.** It is the term every large platform uses in Spain (Microsoft, Apple, Google,
Amazon, El Corte Inglés, the banks), the one the AEPD itself uses on its website and in its guides, and the
one Spanish users look for in a footer. *Aviso de privacidad* is the Mexican term; *Información sobre
protección de datos* is the AEPD's name for the layered article-13 text, too long for a link. The body of
the notice is called *aviso* only where the English says "notice" (*Ocultar el aviso*, *Versión de este aviso*).
GDPR = **RGPD** (Reglamento General de Protección de Datos), with the Spanish citation style
*art. 6.1.f) del RGPD*. The Spanish supervisory authority (AEPD, aepd.es) is named as the local example
next to the Hungarian NAIH; the generic *la autoridad de tu país* is kept.

## Fixed terms

| English | Español (España) | Note |
|---|---|---|
| 5-hour session | sesión de 5 horas; short: *sesión de 5 h*; panel: *SESIÓN DE 5 H* / *5 H* | |
| weekly limit | límite semanal; panel: *LÍMITE SEMANAL*, *SEM.* | |
| per-model weekly limit | límite semanal por modelo | |
| gauge | medidor | *indicador* is reserved for nothing – avoid; lamps are *luces* |
| lamp (backup status light) | luz (de estado); *Luces*, *Solo las luces* | not *piloto*, not *indicador* |
| reset (noun / verb) | reinicio / se reinicia; panel: *reinicio {}* | not the anglicism *reset* |
| countdown | cuenta atrás | Spain; not *cuenta regresiva* |
| pace | ritmo; panel: *{} vs ritmo* | |
| burn rate | velocidad de consumo; *Consumo (%/h, %/día)*; avg daily burn = *Consumo medio diario* | |
| projection / forecast | previsión (*Previsión al final de la semana*) | never *fin de semana* (= weekend) |
| usage | uso; usage data = *datos de uso*; usage file = *archivo de uso*; usage log = *registro de uso* | |
| usage credits (pay-as-you-go) | créditos de uso (pago por uso) | |
| plan / plan badge | plan / distintivo del plan | Microsoft: badge = *distintivo* |
| rate-limit tier | nivel de límite de uso | |
| rate limited (429) | el servidor está limitando las solicitudes (429) | |
| panel / floating panel | panel / panel flotante | |
| post-it (layout, theme) | pósit (*Tarjeta pósit*, *Amarillo pósit*) | RAE (DLE) spelling of the generic word; not the trademark *Post-it* |
| widget | widget | only in the help text, as in the English |
| panel header | cabecera del panel | Spain: *cabecera*, not *encabezado* |
| tray / tray icon | área de notificación / icono del área de notificación | Microsoft es-ES |
| taskbar | barra de tareas | |
| Start menu | menú Inicio | |
| menu bar (macOS) | barra de menús | Apple es-ES |
| start with Windows / at login | Iniciar con Windows / Abrir al iniciar sesión (macOS) | |
| sign in / sign out | iniciar sesión / cerrar sesión; sign-in (noun) = *inicio de sesión* | Microsoft es-ES |
| session expired | la sesión ha caducado | *caducar*, not *expirar* |
| passkeys | claves de acceso | Microsoft/Apple es-ES |
| notification / notify | notificación / avisar (*Avisar al cruzar un umbral*) | |
| alert (tab) | alerta (*Alertas*) | |
| threshold | umbral | |
| warning / critical (thresholds) | Advertencia / Crítico | |
| stale data | datos desactualizados | |
| data freshness | antigüedad de los datos | |
| backup | copia de seguridad; plural short form: *copias* | Microsoft; never *respaldo* |
| backup status bar | barra de estado de las copias | |
| snapshot | instantánea | |
| vault (Obsidian) | bóveda | the word Obsidian's own Spanish UI uses |
| data source | origen de datos | Microsoft es-ES |
| local log | registro local | log = *registro*; log file = *archivo de registro* |
| this PC / this computer | este equipo / este ordenador | *equipo* where the English says PC |
| connected apps | aplicaciones conectadas | |
| per-surface limits | límites por herramienta | *superficie* would be a calque |
| split (between models) | reparto | |
| profile / account | perfil / cuenta | |
| theme | tema | |
| layout | diseño | Microsoft es-ES |
| settings | Configuración (window, menu item, tab) | Microsoft es-ES; not *Ajustes* (Apple/Android) |
| restore defaults | Restaurar valores predeterminados | |
| update (program) | actualización; check for updates = *buscar actualizaciones* | |
| refresh | actualizar (*Actualizar los datos de uso ahora*) | |
| history | historial | |
| always on top | Siempre visible | the Windows term |
| lock position | bloquear posición | |
| click-through | ignorar el ratón | clearer than a calque of *click-through* |
| snap to screen edge | ajustar a los bordes de la pantalla | |
| opacity / accent color | opacidad / color de énfasis | Windows Settings wording |
| sparkline | minigráfico | the Excel es-ES term |
| message to the developer | Mensaje al desarrollador | window title and menu item |
| rating / overall rating | valoración / valoración general; star rating = *valoración con estrellas* | Spain: *valoración*, not *calificación* |
| clear (rating) | borrar | |
| optional | (opcional) | |
| e-mail | correo electrónico; *dirección de correo* | |
| link | enlace | |
| bug | fallo | *Una idea, un fallo…* |
| send / sending… | Enviar / Enviando… | |
| cancel / close / quit | Cancelar / Cerrar / Salir | |
| privacy notice / policy | Política de privacidad | see above |
| consent | consentimiento | |
| controller / processor | responsable del tratamiento / encargado del tratamiento | official RGPD/LOPDGDD terms |
| supervisory authority | autoridad de control (AEPD, aepd.es) | |
| legitimate interest | interés legítimo | |
| rights | acceso, rectificación, supresión, limitación del tratamiento, oposición | official names |
| profiling / automated decision-making | elaboración de perfiles / decisiones automatizadas | |
| encrypted (HTTPS) | cifrado/a | Microsoft es-ES; not *encriptado* |
| hosting provider | proveedor de alojamiento | |
| time units | d, h, min, s (*{} d*, *{} h*, *{} min*, *{} s*; packed: *{}d {}h*, *{}h {}min*) | |
| check now / checking… | Comprobar ahora / Comprobando… | *comprobar*, not *verificar* (except the SHA-256 step) |
