# REVIEW – es-419 (Español, Latinoamérica)

Checker: `check_i18n: OK`, 358/358 keys + 4 macOS keys. 12 warnings, all deliberate: time-unit
abbreviations (`{}d`, `{}h`, `{} h`, `{} d`, ` s`, `{}%/h`), `5H`, and the words *Plan*, *Normal*,
*Extra*, which are spelled the same in Spanish.

Form of address: **tú** everywhere (no voseo, no *vosotros*). Privacy document: **Política de
privacidad** (see the glossary for why not *Aviso de privacidad*).

## The texts I am least sure about

1. **`panel.weekly` = "LÍMITE SEMANAL"** (14 chars vs "WEEKLY LIMIT" 12). The natural Spanish label is
   two characters longer than the English. In a proportional font the width is nearly the same
   (W and Y are wide, Í and T are narrow). If it does not fit on the smallest panel, the fallback is
   "LÍM. SEMANAL" (12) or just "SEMANAL". Same remark for `panel.model` "{} SEMANAL" (+1).

2. **Panel texts slightly longer than the English** (all lowercase status lines, not labels):
   `panel.updated` "actualizado: {}" (+4), `panel.retry_in` "reintento en {} s" (+4),
   `panel.reset` "reinicio {}" (+3), `panel.no_data` "Sin datos" (+2), `panel.full_in` "lleno: {}" (+1),
   `panel.pace` "{} vs ritmo" (+1). Spanish simply has no shorter natural words here. If a line is cut,
   shorten in this order: "act.: {}", "reintento {} s", "reinicio {}" stays.

3. **`panel.five_hour_short` = "5H"**. Correct Spanish typography is "5 h" (space, lowercase), but the
   length rule (not longer than the English 2 characters) wins. On the 14-char label I used "SESIÓN DE
   5 H" with the space, so the two forms differ slightly; acceptable in my judgement.

4. **Minutes = "min", never "m"**: `time.m` "{}min", `time.hm` "{}h {}min", `backup.age_m` "{}min".
   This makes `time.m` and `time.hm` two characters longer than the English. "m" is metres in Spanish
   and the binding brief says *s, min, h, d*; "4h 32min" is what every Spanish-speaking user expects.
   If the panel is too tight, "{}h {}m" is understood but looks wrong to a native.

5. **`panel.refreshing` = "actualizando"** for "fetching data". Not literal ("obteniendo datos" would
   be 16 chars), but it fits (12 ≤ 13) and is exactly what Spanish apps show while they refresh.

6. **"ícono" with accent.** Latin America says and writes *ícono* (Apple and Google es-419); Microsoft's
   Windows UI writes *icono* (the Spain form). I chose *ícono* for the native feel; if the maintainer
   prefers strict Microsoft Windows wording, a global replace *ícono → icono* (`Ícono → Icono`) is safe.

7. **"esta computadora" instead of "este PC".** "PC" changes gender by country (*la PC* in Mexico and
   Argentina, *el PC* in Chile and Colombia), so "ESTE PC" would look foreign to half the region.
   "ESTA COMPUTADORA" makes `detail.local_header` longer than the English
   ("CLAUDE CODE · ESTA COMPUTADORA · DISTRIBUCIÓN DE LA SEMANA"); this is a details-window header,
   not a panel label, so it should have room.

8. **`err.bad_token_resp` / `err.bad_usage_resp`: "endpoint" kept in English.** Microsoft translates it
   as "punto de conexión", but Latin American developers (the people who will ever see these two
   low-level errors) say *endpoint*. "servicio" would be less precise.

9. **`hist.stat_forecast` = "Proyección al cierre de la semana".** The literal "fin de semana" means
   *weekend* in Spanish, so I had to paraphrase; the result is long for a stat box (34 chars vs 22).
   Shorter alternative if it overflows: "Proyección semanal".

10. **`fb.privacy_text` article citations: "art. 6.1, letra f) del RGPD".** This is the form used in the
    official Spanish text of the GDPR ("artículo 6, apartado 1, letra f)") compressed the way Spanish
    privacy policies usually write it. Rights use the official Spanish RGPD vocabulary (*supresión*,
    *limitación del tratamiento*, *oposición*, *autoridad de control*). The notice stays in "tú" like
    the rest of the app, as the English does, but in legal register. Date written out
    ("6 de octubre de 2026") because numeric dates are read differently across the region.

## en / hu differences noticed

- `fb.privacy_text`: the Hungarian links to `/hu/#privacy`; I kept the English URL
  `https://claudeusagemonitor.com/#privacy` (no es-419 page exists).
- `menu.help`: Hungarian adds "(HELP)"; followed the English ("Ayuda…").
- `menu.locked`: English "Lock position" (action), Hungarian "Pozíció rögzítve" (state); followed the
  English: "Fijar posición".
- `notify.logout`: Hungarian says "the panel switched to the local source"; English just "Switched to
  local source" – kept the English: "Se cambió a la fuente local."
- `set.show_extra_usage`: Hungarian keeps "(usage credits)" in English; I used the English's
  "(pay-as-you-go)" → "(pago por uso)".
- `help.guide`, Updates: English says the program "checks" packages with SHA-256; Hungarian says it
  "downloads only from" the site – the Spanish has both, as the English does.

## Lektor

Overall a solid, neutral es-419 translation (tú, no voseo, computadora/mouse/Configuración/Iniciar sesión
throughout; no *ordenador, ratón, vale, coger, vosotros, os*). 12 changes:

- help.guide (5-hour session): "cuánto has usado del límite de tu sesión actual" → "qué parte del límite de tu sesión actual ya usaste" – LatAm preterite, not perfect.
- help.guide (pace): "si alcanzará hasta el reinicio" → "si te alcanzará hasta el reinicio" – natural "will it last".
- help.guide (data source): "o más lento si el servidor lo pide" → "o con menos frecuencia si el servidor lo pide" – refresh rate, not speed.
- help.guide (updates): "Versiones nuevas y novedades" → "Versiones nuevas y notas de la versión" – "release notes", avoid repetition.
- dlg.err_ratelimit: "inicia UN solo inicio de sesión nuevo en el navegador con un código nuevo" → "vuelve a iniciar sesión en el navegador UNA sola vez, con un código nuevo" – removes "inicia… inicio" clash.
- dlg.err_badcode: "vuelve a intentar el inicio de sesión en el navegador" → "vuelve a iniciar sesión en el navegador" – shorter, idiomatic.
- fb.privacy_text: "a petición tuya" → "a solicitud tuya" – usual LatAm legal wording.
- set.backup_disclaimer: "responsabilidad de cada quien" → "responsabilidad de cada usuario" – "cada quien" sounds Mexican/colloquial.
- hist.stat_now: "Semanal actual" → "Semana actual" – dangling adjective as label.
- set.refresh: "Actualización" → "Intervalo de actualización" – spinner in seconds; avoids "update" clash.
- set.show_surfaces: "Límites por superficie" → "Límites por producto" – "superficie" is a calque (glossary updated).
- fb.err_email: "Este correo electrónico no parece válido." → "Esta dirección de correo electrónico no parece válida." – it validates the address.

Glossary: added *per-surface limits = límites por producto* and *refresh interval = intervalo de actualización*.

Back-translation check of help.guide, err.*, notify.*, fb.intro, fb.privacy_text, set.backup_disclaimer and
backup.disclaimer_short: no omissions or additions; the privacy notice keeps the controller, URL, all data items,
the IP/hash statement, Art. 6(1)(f) and 6(1)(a), 2-year retention, forwarding, processor (EU, Germany), no
sale/profiling, all rights, NAIH/naih.hu, the own-country authority and the version date.

Still in doubt:
- Percent spacing: the glossary says "70 %" (RAE), which help.guide follows, but the panel/tray/notify strings
  use "{}%" with no space ("{}: {}% usado."). Compact is fine on the panel; most LatAm apps write "70%" anyway.
  If strict consistency is wanted, change `notify.threshold` to "{}: {} % usado.".
- `tray.head` "5 h: {}%   ·   Sem.: {}%" is 1 character longer than the English; it is a tooltip, so I kept the
  correct "5 h". Fallback: "5h:".
- `panel.full_in` "lleno: {}" reads slightly abrupt; "lleno en {}" would be clearer but +3 characters on the panel.
- `fb.privacy_hide` "Ocultar el aviso" / "Versión de este aviso": "aviso" is used for the short in-app notice and
  "Política de privacidad" for the title and the full document; acceptable, but a strict reader may want one term.
