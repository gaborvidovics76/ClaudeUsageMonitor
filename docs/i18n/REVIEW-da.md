# Review – Dansk (da)

## Lektor

Ændringer i `claude_usage/langs/da.py`:

- `backup.cloud_only`: „så det ikke behøver at blive downloadet" → „så det ikke skal downloades" – kortere, mere naturligt.
- `backup.disclaimer_short`: „sikkerhedskopiens logs … det er dit eget ansvar at tjekke" → „sikkerhedskopieringens logs … det er op til dig at tjekke" – undgå dobbelt „ansvar"; proces, ikke kopi.
- `dlg.err_badcode`: „prøv login i browseren igen" → „prøv at logge på i browseren igen" – naturligt verbum, Microsoft-term.
- `err.bad_token_resp`: „token-slutpunktet" → „tokenslutpunktet" – dansk sammenskrivning.
- `err.bad_usage_resp`: „forbrugs-slutpunktet" → „forbrugsslutpunktet" – dansk sammenskrivning.
- `fb.consent`: „Jeg har læst og accepterer {}." → „Jeg har læst og accepterer udviklerens {}." – ubestemt titel kræver genitiv.
- `fb.intro`: „Fortæl mig det. Hver eneste besked bliver læst af mig" → „Skriv til mig. Hver eneste besked læses af mig" – mindre oversat, s-passiv.
- `fb.privacy_hide`: „Skjul meddelelsen" → „Skjul teksten" – „meddelelse" = notification i Windows.
- `fb.privacy_text`: „og, så jeg kan forstå sammenhængen:" → „samt, så jeg kan forstå sammenhængen," – forkert tegnsætning rettet.
- `fb.privacy_text`: „hash" → „hashværdi" – dansk fagterm.
- `fb.privacy_text`: „databeskyttelsesforordningen (GDPR) artikel 6, stk. 1, litra f" → „jf. artikel 6, stk. 1, litra f, i databeskyttelsesforordningen, GDPR" – dansk juridisk henvisningsform, ingen dobbelte parenteser.
- `fb.privacy_text`: „selve svaret sker på din anmodning" → „selve svaret sendes på din anmodning" – præcist verbum.
- `fb.privacy_text`: „(samtykke, artikel 6 …)" → „(samtykke, jf. artikel 6 …)" – ensartet henvisning.
- `fb.privacy_text`: „har gennemgået det; … trække samtykket tilbage" → „har gennemgået bedømmelsen; … trække dit samtykke tilbage" – entydig reference.
- `fb.privacy_text`: „lander en kopi også i udviklerens postkasse" → „havner en kopi også i udviklerens indbakke" – mindre talesprog, e-mailterm.
- `fb.privacy_text`: „Version af denne meddelelse" → „Version af denne tekst" – „meddelelse" er notification.
- `fb.sent`: „Tak – den er modtaget!" → „Tak – beskeden er modtaget!" – tydeligt subjekt.
- `fb.sent_sub`: „Har du skrevet en e-mailadresse" → „Har du angivet en e-mailadresse" – formularsprog.
- `help.disclaimer`: „ikke lavet af og ikke tilknyttet" → „hverken lavet af eller tilknyttet" – naturlig dansk konstruktion.
- `help.guide`: „når serveren melder en" → „når serveren rapporterer en" – præcist verbum.
- `help.guide`: „hvor hurtigt du bruger grænsen" → „hvor hurtigt du bruger af grænsen" – idiomatisk dansk.
- `help.guide`: „Kræver et engangslogin … langsommere hvis" → „Kræver, at du logger på én gang … langsommere, hvis" – naturligt verbum, startkomma.
- `help.guide`: „planlagte sikkerhedskopier er kørt og blevet færdige … sikkerhedskopiens logs" → „planlagte sikkerhedskopieringer er kørt og blevet fuldført … sikkerhedskopieringens logs" – proces, ikke selve kopien.
- `help.guide`: „Hvis noget er galt" → „Hvis noget ikke virker" – idiomatisk overskrift.
- `help.guide`: „overlever genstart" → „bevares ved genstart" – mindre anglicistisk.
- `menu.model_gauge`: „{} måler" → „{}-måler" – sammensætning med produktnavn.
- `panel.reset`: „nulstil {}" → „nulst. om {}" – bydeform misforstås; „om" for tidsrum.
- `set.about`: „Den beder kun Anthropic om" → „Programmet spørger kun Anthropic om" – tydeligt subjekt, rigtigt verbum.
- `set.backup_config`: „Konfiguration af sikkerhedskopiscript" → „Sikkerhedskopiscriptets konfigurationsfil" – feltet vælger en fil.
- `set.backup_disclaimer`: „så kvaliteten … kan ikke garanteres" → „og derfor kan kvaliteten … ikke garanteres" – forkert ordstilling rettet.
- `set.local_models_hint`: „output-tokens … token-antallet" → „outputtokens … antallet af tokens" – sammenskrivning, naturlig form.
- `set.local_models_none`: „denne gruppe forbliver bare skjult" → „denne gruppe vises så bare ikke" – mere mundret.
- `set.refresh`: „Opdatering" → „Opdateringsinterval" – sekundfelt; undgå forveksling med programopdatering.
- `set.show_surfaces`: „Grænser pr. flade" → „Grænser pr. platform" – „flade" er kalke af „surface".
- `set.tip`: „Ctrl+rul" → „Ctrl+musehjul" – ensartet med hjælpeteksten.
- `theme.claude`: „varm mørk" → „varmt mørkt" – bøjning efter „tema" (intetkøn).
- `STRINGS_MAC notify.autostart_on/off`: „appen åbner (ikke)" → „appen åbnes (ikke)" – „åbne" er transitivt.

Ordlisten (`glossary-da.md`) er opdateret: „Skjul teksten", `fb.consent`-formuleringen, `panel.reset`,
samt nye rækker for sikkerhedskopiering, platform (surface) og opdateringsinterval.

### Tvivl

- `panel.reset` „nulst. om {}" er en ad hoc-forkortelse; „nulstilles om {}" er bedst, men for langt til panelet.
  Hvis der er plads (teksten tegnes skaleret), kan den fulde form bruges.
- `panel.full_in` „fuld: {}" er beholdt som i kilden; „fuld om {}" ville være mere idiomatisk men 2 tegn længere.
- `fb.consent`: „udviklerens Privatlivspolitik" – stort P midt i sætningen markerer linket/titlen; alternativt kunne
  `fb.privacy_title` skrives med lille begyndelsesbogstav, da den kun bruges som linktekst her.
- `fb.privacy_text`: „i Danmark: Datatilsynet" er en tilføjelse i forhold til kilden (tilladt efter briefen); den
  generelle „tilsynsmyndigheden i dit eget land" er bevaret.
- `time.hm` „{}t {}min" er to tegn længere end „{}h {}m"; „m" bruges ikke for minutter på dansk (= meter).
