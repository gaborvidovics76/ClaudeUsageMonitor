# Review notes – Español (España) – `es-ES`

Module: `claude_usage/langs/es_ES.py` – 358 keys + 4 macOS overrides. Checker: `check_i18n: OK`
(9 warnings, all for texts that are rightly identical to the English: the unit symbols `{}d`, `{}h`,
`{} d`, `{} h`, ` h`, ` s`, `{}d {}h`, and the words *Plan*, *Normal*).

Legacy: 140 of the 324 old `es-ES` lines were changed; 184 were already correct and consistent with the
glossary and were kept as they were. The main systematic changes: *Ajustes* → **Configuración** (Microsoft
es-ES), *bandeja* → **área de notificación**, *indicador* (gauge) → **medidor** and *indicadores* (lamps) →
**luces**, *insignia* → **distintivo**, *PC* → **equipo**, preterite → **present perfect** (*ha caducado*,
*se ha reiniciado*), Latin-American *expiró / no finalizó / se encontró* → peninsular forms, consistent
**space before %** (`{} %`), and *sesión de 5 horas* shortened to *5 h* on the panel.

## Texts I am least sure about

1. **panel.\* length** – Spanish is longer than English and several panel labels exceed the English by a
   few characters even after shortening: `LÍMITE SEMANAL` (+2), `actualizado: {}` (+4), `reintento en {} s`
   (+4), `reinicio {}` (+3), `Sin datos` (+2), `lleno: {}`, `{} SEMANAL`, `{} vs ritmo` (+1 each).
   `SESIÓN DE 5 H` is shorter than the English. If a label is clipped on the smallest panel size, the
   candidates to shorten are `actualizado: {}` → `act.: {}` and `reintento en {} s` → `reintento: {} s`.
   I preferred readable Spanish over abbreviations the user would have to guess.
2. **tray.head** – `5 h: {} %   ·   Sem.: {} %` is 3 characters longer than the English because of the
   two spaces before `%` (RAE and Microsoft style) and the space in `5 h`. The three-space separators were
   kept as in the English. If the tooltip must stay exactly as short, drop the period of `Sem.`.
3. **time.hm / time.m / backup.age_m** – `{}h {}min` and `{}min` instead of `{}h {}m` / `{}m`: the binding
   project note asks for the units *s, min, h, d*, and *m* means metre in Spanish. This makes those three
   forms 2 characters longer than the English.
4. **menu.click_through / set.click_through** – *Ignorar el ratón* instead of a calque of "click-through"
   (the old *Clic transparente* was unclear). The help text uses the same wording so the user can find the
   setting. If a closer rendering is preferred: *Transparente a los clics*.
5. **Lamps → luces** – the small coloured backup lights are *luces* (`Luces`, `Solo las luces`, `Etiqueta
   junto a la luz`, `Haz clic en una luz`). *Indicador* was dropped because it collided with the gauges
   (now *medidor*). *Piloto* would be very Spanish but unusual in software.
6. **set.show_surfaces** – *Límites por herramienta* for "per-surface limits": *superficie* is a calque with
   no meaning for a Spanish user. If Anthropic's own Spanish UI settles on a term, use that one.
7. **hist.stat_forecast** – *Previsión al final de la semana* (long for a stats label) because the old
   *Proyección fin de semana* reads as "weekend forecast". If space is tight: *Previsión semanal*.
8. **fb.privacy_text** – the supervisory-authority sentence names the Hungarian NAIH (as in the English) and
   adds the Spanish AEPD (aepd.es) as the local example, keeping *la autoridad de tu país*. Citations use the
   Spanish style `art. 6.1.f) del RGPD`; the notice date is written *6 de octubre de 2026*. The URL is the
   English one (`/#privacy`), not the Hungarian `/hu/#privacy`.
9. **size.extra** – *Extragrande* instead of the identical *Extra*: in a size list Spanish users expect
   *Pequeño / Normal / Grande / Extragrande*; plain *Extra* would read as an unrelated word.
10. **set.refresh** – rendered as *Actualización* (the English label is just "Refresh", presumably followed by
    an interval and the ` s` suffix). If the widget is a button rather than a label, it should become
    *Actualizar*.

## en/hu differences noticed

- `menu.help`: HU says *Súgó (HELP)…*; the English is plain *Help…* – followed the English (*Ayuda…*).
- `hist.stat_forecast`: HU *Hét végére – előrejelzés* (to the end of the week) confirms the intent is the end
  of the calendar week, not the weekend – hence the explicit *final de la semana*.
- `set.show_extra_usage`: HU keeps the English *usage credits* in brackets; the English says *pay-as-you-go*
  – followed the English (*pago por uso*).
- `fb.meta`: HU puts the version in parentheses, the English does not; the Spanish uses parentheses for all
  three values for symmetry, same placeholders `{0} {1} {2}`.
- `fb.privacy_text`: HU links to `/hu/#privacy`; the Spanish uses the English `/#privacy`.

## Lektor

Independent native review (es-ES). The translation was already solid (tú, Microsoft/Apple es-ES terms,
peninsular present perfect, RGPD citations); 21 keys changed (30 edits), mostly naturalness and RAE typography.
Checker after the review: `check_i18n: OK` (the same 9 warnings for unit symbols, *Plan*, *Normal*).

- help.guide: "<b>…</b> – explicación" (×9 list items) → "<b>…</b>: explicación" – colon, not English dash
- help.guide: "se reinicia a una hora fija de la semana, propia de tu cuenta" → "se reinicia cada semana a una hora fija que depende de tu cuenta" – clumsy apposition, unnatural
- help.guide: "Clic derecho … – el menú completo" / "Doble clic … – la ventana Historial: 6 horas…" → "…: abre el menú completo" / "…: abre la ventana Historial (6 horas…)" – verbless fragment reads translated
- help.guide: "Ctrl + rueda del ratón – más grande o más pequeño" → "Ctrl + rueda del ratón: lo agranda o lo reduce" – natural verb phrase
- help.guide: "tarjeta post-it, barra fina, anillos" → "tarjeta pósit, barra fina y anillos" – RAE spelling, list conjunction
- help.guide: "El inicio de sesión de claude.ai se guarda cifrado" → "Los datos de inicio de sesión de claude.ai se guardan cifrados" – an action can't be stored
- help.guide: "el programa lo reintenta por sí solo" → "el programa vuelve a intentarlo por sí solo" – more idiomatic
- help.guide: "sobrevive a reinicios y actualizaciones" → "se mantiene tras reinicios y actualizaciones" – calque of "survives"
- help.guide: "la previsión … avisa a tiempo" → "la previsión … te avisa a tiempo" – direct address, more natural
- fb.privacy_text: "lo que escribes aquí – nombre … estrellas – y" → "lo que escribes aquí —nombre … estrellas— y" – RAE raya for inciso
- fb.privacy_text: "leer y responder tu mensaje" → "leer y responder a tu mensaje" – responder takes "a"
- dlg.err_ratelimit: "El servidor te está limitando temporalmente … espera 10–15 minutos (sin intentarlo mientras tanto) y luego inicia UNA sola sesión nueva en el navegador con un código nuevo." → "El servidor ha bloqueado los intentos temporalmente … espera entre 10 y 15 minutos (no lo intentes mientras tanto) y luego vuelve a iniciar sesión en el navegador UNA sola vez, con un código nuevo." – calque; Spanish range; clearer
- err.rate_limited: "(429): se reintenta automáticamente." → "(429); se volverá a intentar automáticamente." – "reintentar" impersonal sounds technical
- notify.reset_done: "{}: reiniciado — ha empezado un nuevo periodo." → "{}: se ha reiniciado y empieza un nuevo periodo." – gender clash (sesión/límite); spaced em dash
- notify.threshold: "{}: {} % usado." → "{}: has usado el {} %." – natural, friendly notification
- fb.email_hint: "solo si quieres respuesta" → "solo si quieres que te responda" – missing article, abrupt
- fb.err_empty: "Escribe un mensaje o elige una valoración primero." → "Primero escribe un mensaje o elige una valoración." – English word order
- fb.intro: "Cada mensaje lo leo yo personalmente: Vidovics Gábor, el autor del programa." → "Todos los mensajes los leo yo, Vidovics Gábor, el autor." – redundant, closer to source
- fb.sent_sub: "te responderé ahí" → "te responderé a esa dirección" – "ahí" for an address is colloquial
- help.feedback: "Preguntas, ideas, errores" → "Preguntas, ideas, avisos de fallos" – bug reports, glossary "fallo"
- hist.stat_now: "Semanal actual" → "Uso semanal actual" – adjective without noun
- layout.postit / theme.postit: "Tarjeta post-it" / "Amarillo post-it" → "Tarjeta pósit" / "Amarillo pósit" – RAE (DLE) generic spelling
- set.about: "Solo pide a Anthropic tu propio uso y lee el número de versión del servidor" → "Solo consulta tu propio uso a Anthropic y lee el número de versión en el servidor" – "pedir el uso" unnatural
- set.backup_disclaimer: "Asegurarse de que las copias están completas y se pueden restaurar" → "…estén completas y se puedan restaurar" – subjunctive after "asegurarse de que"
- set.local_models_hint: "una proporción de tu propio uso … no una parte de un límite" → "es una parte de tu propio uso … no de un límite" – inconsistent proporción/parte
- set.local_models_none: "Nada más se ve afectado." → "No afecta a nada más." – passive calque
- set.profile_auto: "Automático (último usado)" → "Automático (el último usado)" – missing article
- set.refresh: "Actualización" → "Intervalo de actualización" – it labels a seconds spin box (settings_dialog.py)
- update.check_failed: "No se ha podido buscar actualizaciones: {}" → "Error al buscar actualizaciones: {}" – avoids the RAE concord issue (*se han podido buscar*)
- glossary-es-ES.md: added *pósit*; dash rule rewritten (colon / raya / *entre X y Y*; spaced en dash only inside short labels).

### Still in doubt
- `panel.updated` (`actualizado: {}`, +4) and `panel.retry_in` (+4) remain longer than the English; left readable.
  If clipped on the smallest size: `act.: {}` / `reintento: {} s`.
- `panel.full_in` `lleno: {}` (masculine, agrees with *límite*) – it also follows the 5-hour *sesión*; *al 100 %: {}*
  would be gender-neutral but longer. Kept.
- `set.source_api` / `set.source_local` / `set.profile_n` keep the spaced en dash as a label separator, as Windows
  es-ES does in option lists.
- `fb.privacy_text` names the AEPD (aepd.es) next to the NAIH – correct authority for Spain, but an addition to the
  English; remove it if the notice must stay strictly identical in content across languages.
- `hist.stat_forecast` (*Previsión al final de la semana*) is long for a stats label; *Previsión semanal* if space is tight.
