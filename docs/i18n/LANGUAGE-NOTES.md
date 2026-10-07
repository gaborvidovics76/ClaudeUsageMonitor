# Per-language notes (binding for translators and reviewers)

Read together with [TRANSLATOR-BRIEF.md](TRANSLATOR-BRIEF.md). Module format example: `claude_usage/langs/pt_BR.py`.

## ro – Română
- ș ț ALWAYS with comma below (U+0219, U+021B, Ș U+0218, Ț U+021A), never cedilla ş ţ (the checker rejects it). â/î per DOOM (sunt).
- Address: choose "tu" (friendly consumer software) or "dumneavoastră" (Microsoft); keep consistent; explain in the glossary.
- Microsoft: Conectare / Deconectare, Setări, Notificări, bara de activități, zona de notificare, folder, actualizare, server, descărcare. macOS: bara de meniu, „Deschide la autentificare”.
- Panel labels in capitals with diacritics (SESIUNE DE 5 ORE, LIMITĂ SĂPTĂMÂNALĂ). Units s / min / h / z.
- GDPR → RGPD („art. 6 alin. (1) lit. f) RGPD”); authority generic (ANSPDCP may be the Romanian example).
- Privacy document: „Politica de confidențialitate”.

## bg – Български
- A fresh Bulgarian translation, NOT an adaptation of the Russian texts (do not read them). Bulgarian grammar (definite articles, да-constructions). No ы / э (checker).
- Address: "ти" or "Вие" (Microsoft) – choose, keep, explain.
- Microsoft: Влизане / Излизане, Настройки, Известия, лента на задачите, област за известяване, папка, актуализация, сървър, изтегляне. macOS: лента с менюта, „Отваряне при влизане“.
- Panel: 5-ЧАСОВА СЕСИЯ, СЕДМИЧЕН ЛИМИТ. Units с / мин / ч / д.
- GDPR → ОРЗД; authority generic (КЗЛД as Bulgarian example). Privacy document: „Политика за поверителност“.

## sk – Slovenčina
- A fresh Slovak translation – do NOT transcribe the Czech texts (do not read them). ä ô ĺ ŕ, rhythmic law.
- Address: "ty" or "vy" (Microsoft) – choose, keep, explain.
- Microsoft: Prihlásiť sa / Odhlásiť sa, Nastavenia, Oznámenia, panel úloh, oblasť oznámení, priečinok, aktualizácia, server, stiahnuť. macOS: lišta ponúk, „Otvoriť pri prihlásení“.
- Panel: 5-HODINOVÁ RELÁCIA, TÝŽDENNÝ LIMIT. Units s / min / h / d.
- GDPR stays GDPR („čl. 6 ods. 1 písm. f) GDPR“); authority generic (ÚOOÚ SR). Privacy document: „Zásady ochrany osobných údajov“.

## hr – Hrvatski
- Standard Croatian (not Serbian): ijekavian; tjedan, sat, računalo, datoteka, mapa, poslužitelj, postavke, obavijest, korisnik, preuzimanje, ažuriranje.
- Address: "ti" or "Vi" (Microsoft) – choose, keep, explain.
- Microsoft: Prijava / Odjava, Postavke, Obavijesti, programska traka, područje obavijesti. macOS: traka izbornika, „Otvori pri prijavi”.
- Panel: SESIJA OD 5 SATI, TJEDNO OGRANIČENJE. Units s / min / h / d.
- GDPR: „Opća uredba o zaštiti podataka (GDPR)” once, then GDPR; authority generic (AZOP). Privacy document: „Pravila privatnosti” or „Politika privatnosti” – choose what Croatian platforms use, explain.

## sv – Svenska
- Address "du". Friendly, short; Swedish words over anglicisms.
- Microsoft: Logga in / Logga ut, Inställningar, Aviseringar, aktivitetsfältet, meddelandefältet, mapp, uppdatering, server, ladda ned. macOS: menyraden, ”Öppna vid inloggning”.
- Panel: 5-TIMMARSSESSION, VECKOGRÄNS. Units s / min / h / d.
- GDPR (dataskyddsförordningen) „artikel 6.1 f”; authority generic (IMY). Privacy document: ”Integritetspolicy”.

## fi – Suomi
- "sinä" forms. Panel labels are tight: panel.*, time.*, *_short no longer than English (e.g. VIIKKORAJA).
- Microsoft: Kirjaudu sisään / Kirjaudu ulos, Asetukset, Ilmoitukset, tehtäväpalkki, ilmoitusalue, kansio, päivitys, palvelin, lataa. macOS: valikkorivi, ”Avaa kirjautuessa”.
- Units s / min / h / pv.
- GDPR: „tietosuoja-asetus (GDPR)” once; „6 artiklan 1 kohdan f alakohta”; authority generic (tietosuojavaltuutettu). Privacy document: ”Tietosuojaseloste”.

## lt – Lietuvių
- ą č ę ė į š ų ū ž everywhere. Address "tu" or "jūs" (Microsoft) – choose, keep, explain.
- Microsoft: Prisijungti / Atsijungti, Parametrai (Microsoft) or Nustatymai (Apple/Google) – choose, explain; Pranešimai, užduočių juosta, pranešimų sritis, aplankas, naujinimas, serveris, atsisiųsti. macOS: meniu juosta, „Atidaryti prisijungus“.
- Panel: SAVAITĖS LIMITAS. Units s / min / val. / d.
- GDPR → BDAR („6 str. 1 d. f p.“); authority generic (VDAI). Privacy document: „Privatumo politika“.

## sl – Slovenščina
- Standard Slovenian (not Croatian). The dual exists – phrase number + noun so it cannot be wrong (abbreviated units).
- Address "ti" or "vi" (Microsoft) – choose, keep, explain.
- Microsoft: Vpis / Izpis or Prijava / Odjava (check Microsoft's, explain), Nastavitve, Obvestila, opravilna vrstica, območje za obvestila, mapa, posodobitev, strežnik, prenos. macOS: menijska vrstica, »Odpri ob prijavi«.
- Panel: TEDENSKA OMEJITEV. Units s / min / h / d.
- GDPR: „Splošna uredba o varstvu podatkov (GDPR)” once; „člen 6(1)(f)”; authority generic (Informacijski pooblaščenec). Privacy document: „Politika zasebnosti”.

## lv – Latviešu
- ā ē ī ū, ģ ķ ļ ņ everywhere. Address "tu" or "jūs" (Microsoft) – choose, keep, explain.
- Microsoft: Pierakstīties / Izrakstīties, Iestatījumi, Paziņojumi, uzdevumjosla, paziņojumu apgabals, mape, atjauninājums, serveris, lejupielādēt. macOS: izvēļņu josla, “Atvērt pierakstoties”.
- Panel: NEDĒĻAS LIMITS. Units s / min / h / d.
- GDPR → VDAR („6. panta 1. punkta f) apakšpunkts”); authority generic (Datu valsts inspekcija). Privacy document: “Privātuma politika”.

## et – Eesti
- "sina" forms. Panel labels tight (NÄDALALIMIIT).
- Microsoft: Logi sisse / Logi välja, Sätted (Microsoft) or Seaded – choose, explain; Teatised, tegumiriba, teavitusala, kaust, värskendus, server, laadi alla. macOS: menüüriba, „Ava sisselogimisel“.
- Units s / min / h / p.
- GDPR: „isikuandmete kaitse üldmäärus (GDPR)” once; „artikli 6 lõike 1 punkt f”; authority generic (Andmekaitse Inspektsioon). Privacy document: „Privaatsuspoliitika“ (or „Isikuandmete töötlemise teave“ – choose, explain).

## mt – Malti
- ħ ġ ż ċ, għ, ie; standard Maltese orthography; technical loanwords as Microsoft Maltese / EU translations use them.
- Address singular "int", consistent.
- Microsoft (Windows Maltese LIP): Idħol / Oħroġ, Settings term as Microsoft/EU Maltese uses (explain), Notifiki, taskbar, folder, aġġornament, server, niżżel. macOS: menu bar, "Iftaħ mal-login".
- Panel: LIMITU TAL-ĠIMGĦA. Units s / min / h / j.
- GDPR (Regolament Ġenerali dwar il-Protezzjoni tad-Data) „Artikolu 6(1)(f)”; authority generic (IDPC). Privacy document: "Politika tal-Privatezza".

## ga – Gaeilge
- An Caighdeán Oifigiúil; initial mutations (séimhiú, urú) and prefixed-capital rule (an tSeachtain, na hUaireanta, i nGaeilge); in UPPERCASE labels the prefix stays lowercase where the rule says so (AN tSEACHTAIN).
- Address singular "tú".
- Microsoft (Windows Irish LIP / tearma.ie): Sínigh isteach / Sínigh amach, Socruithe, Fógraí, tascbharra, limistéar na bhfógraí, fillteán, nuashonrú, freastalaí, íoslódáil. macOS: barra roghchláir, "Oscail ar logáil isteach".
- Units s / nóim / u / l.
- GDPR → RGCS („Airteagal 6(1)(f)”); authority generic (An Coimisiún um Chosaint Sonraí). Privacy document: "Polasaí Príobháideachais" or "Ráiteas Príobháideachais" – choose, explain.
