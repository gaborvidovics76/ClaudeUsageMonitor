# Sanasto – suomi (fi), Claude Usage Monitor

Kiinteät termit ja sävy `claude_usage/langs/fi.py`-moduulille. Englanti on lähde, unkari näyttää
tarkoituksen; jos ne eroavat, englanti voittaa (ero kirjataan REVIEW-fi.md:hen).

## Sävy ja puhuttelu

- **Sinuttelu** kaikkialla („Kirjaudu sisään", „Tarkista verkkoyhteys", „Sinulla on uusin versio"),
  kuten Microsoftin, Applen ja suomalaisten kuluttajapalvelujen (esim. OP, Elisa, Yle) ohjelmistoissa.
  Ei koskaan teitittelyä. Tilailmoituksissa, joissa ei puhutella ketään, passiivi on luonnollinen:
  „Tarkistetaan…", „Ladataan…", „Lähetetään…".
- Lyhyt, ystävällinen, varma. Ilmoitukset ovat yhden–kahden lauseen mittaisia.
- Microsoftin suomenkielinen Windows-terminologia Windows-asioille; Applen suomi neljässä
  macOS-tekstissä (`STRINGS_MAC`): **valikkorivi**, **Avaa kirjautuessa**, **osoita toissijaisesti**.
- Paneelin tekstit (`panel.*`, `time.*`, `*_short`, `tray.head`) ovat tiukassa tilassa: lyhyet
  muodot ja vakiolyhenteet, isot kirjaimet siellä, missä englannissakin. Paneelissa „data"
  (Ei dataa, haetaan dataa), koska „tiedot/tietoja" ei mahdu; muualla aina **tiedot**.
- Välilyönti prosenttimerkin eteen suomalaisen typografian mukaan („70 %", „{} %/h", „70 %:sta");
  `tray.head`-rivillä erotinvälejä on tiivistetty, jotta pituus pysyy englannin mitassa.
- Ajan yksiköt: **s / min / h / pv**. Tunnin SI-tunnus „h" on lyhyempi kuin „t" ja yleinen
  Windowsissa; päivälle „pv". Tiiviissä muodoissa ilman väliä: „{}pv {}h", „{}h {}min".
- Lainausmerkit: suomalaiset ”…” (help.disclaimer). Päivämäärät suomalaisittain: 21.9.2026.
- Verkko-osoitteen taivutus kierretään rakenteella („sivustoon claudeusagemonitor.com",
  „osoitteesta claudeusagemonitor.com"), ei „claudeusagemonitor.comiin".
- Ohjeteksti puhuu **paneelista** (ei „widget" / „pienoissovellus"), koska samaa sanaa käytetään
  valikoissa ja asetuksissa; „pienoissovellus" sekoittuisi Windowsin Widgetit-näkymään.

## Tietosuoja-asiakirjan nimi

`fb.privacy_title` = **Tietosuojaseloste** (myös `help.privacy`). Tämä on nimi, jolla suomalaiset
verkkopalvelut, sovellukset ja tietosuojavaltuutetun toimisto kutsuvat rekisteröidylle annettavaa
informointiasiakirjaa (GDPR 13 artikla). „Tietosuojakäytäntö" on englannista käännetty muoto, jota
osa kansainvälisistä alustoista käyttää, mutta „tietosuojaseloste" on se termi, jonka suomalainen
käyttäjä tunnistaa suostumusruudusta. Selosteessa GDPR mainitaan ensin muodossa
„tietosuoja-asetus (GDPR)", artiklaviittaukset suomalaisen säädöskielen mukaan („6 artiklan 1 kohdan
f alakohta"). Valvontaviranomainen Suomessa: **tietosuojavaltuutettu** (lisätty sulkuihin
„oman maasi valvontaviranomaiselle" -kohtaan).

Suostumusruutu (`fb.consent`, linkkiteksti tulee paikkamerkkiin nominatiivissa):
„Olen lukenut ja hyväksyn: {}." → „Olen lukenut ja hyväksyn: Tietosuojaseloste." – rakenne
välttää taivutusongelman (paikkamerkkiä ei voi taivuttaa genetiiviin).

## Kiinteät termit

| Englanti | Suomi | Huomautus |
|---|---|---|
| 5-hour session | 5 tunnin istunto | paneelissa isoin kirjaimin 5 H:N ISTUNTO (englannin mitassa), lyhyt: 5H |
| weekly limit | viikkoraja | paneelissa VIIKKORAJA, lyhyt: VKO; mallin raja „{} VIIKKO" |
| per-model (weekly) limit | mallikohtainen viikkoraja | |
| limit | raja | ei „rajoitus" (se on toiminta, ei määrä); „ei rajaa" |
| reset (noun / verb) | nollaus / nollautuu | paneelissa „nollaus {}"; „Aika nollaukseen" |
| pace | tahti | paneelissa „tahti {}" (esim. tahti +12%) |
| full in | täynnä | paneelissa „täynnä {}" |
| burn rate | kulutusnopeus | „%/h, %/pv" |
| usage | käyttö | käyttötiedot, käyttötiedosto, käyttöloki |
| usage credits | käyttökrediitit | pay-as-you-go = käytön mukaan laskutettava |
| plan | tilaus | Pro / Max / Team / Enterprise ei käännetä |
| plan badge | tilausmerkki | paneelin otsikossa |
| gauge | mittari | „{}-mittari" |
| panel / widget | paneeli | kelluva paneeli; myös ohjeessa |
| tray / system tray | ilmoitusalue | Microsoft |
| tray icon | ilmoitusalueen kuvake | |
| menu bar (macOS) | valikkorivi | Apple |
| taskbar | tehtäväpalkki | Microsoft |
| Start menu | Käynnistä-valikko | Microsoft |
| sign in / sign out | kirjaudu sisään / kirjaudu ulos | Microsoft; substantiivi: kirjautuminen |
| sign in to claude.ai | kirjaudu claude.ai-palveluun | ulos: claude.ai-palvelusta |
| start with Windows | käynnistä Windowsin mukana | macOS: Avaa kirjautuessa |
| on / off (state) | käytössä / ei käytössä | Microsoftin tapa |
| settings | asetukset | ikkunan otsikko pienellä: „asetukset" |
| notification / notify | ilmoitus / ilmoita | „Ilmoita, kun …" |
| alert(s) | hälytys / Hälytykset | välilehden nimi |
| threshold | kynnysarvo | Microsoft |
| warning / critical | varoitus / kriittinen | |
| backup(s) | varmuuskopio(t) | |
| backup folder / script | varmuuskopiokansio / varmuuskopioskripti | |
| backup status bar | varmuuskopioiden tilarivi | Microsoft: status bar = tilarivi |
| upload / uploaded | siirtää / siirretty | „Siirretty Nextcloudiin" |
| lamp | merkkivalo | |
| snapshot | tilannevedos | Microsoft |
| vault (Obsidian) | holvi | Obsidianin suomennos |
| scheduled task | ajoitettu tehtävä | Windowsin Tehtävien ajoitus |
| run (backup run) | ajo | viimeisin ajo, testiajo |
| log / log file | loki / lokitiedosto | |
| local log | paikallinen loki | |
| data source | tietolähde | |
| local (this PC only) | paikallinen (vain tämä tietokone) | „PC" = tietokone; ison kirjaimen otsikossa TÄMÄ KONE |
| profile / account | profiili / tili | |
| theme / layout / size / order | teema / asettelu / koko / järjestys | |
| Extra (size) | Erittäin suuri | Windowsin kokoasteikko |
| update (program) | ohjelmapäivitys / päivitys | Tarkista päivitykset, Asenna nyt |
| download | lataa / lataus | lataussivu |
| server / folder | palvelin / kansio | |
| history | historia | Historia ja tilastot |
| projection / forecast | ennuste | |
| peak | huippu | |
| data freshness / stale | tietojen tuoreus / vanhentunut | paneelissa „haettu: {}" |
| message to the developer | viesti kehittäjälle | ikkuna ja valikko |
| author / Made by | tekijä / Ohjelman tekijä | |
| rating / overall rating | arvio / yleisarvio | tähtiarvio |
| clear (rating) | tyhjennä | |
| optional | valinnainen | lomakkeissa „(valinnainen)" |
| privacy notice / policy | tietosuojaseloste | ks. yllä |
| consent | suostumus | |
| controller / processor | rekisterinpitäjä / henkilötietojen käsittelijä | GDPR-termit |
| hosting provider | palvelintilan tarjoaja | |
| legitimate interest | oikeutettu etu | |
| supervisory authority | valvontaviranomainen | Suomessa: tietosuojavaltuutettu |
| terms of use | käyttöehdot | |
| disclaimer | vastuuvapauslauseke | |
| click-through | läpinapsautus | asetuksissa selitys sulkeissa |
| lock position | lukitse sijainti | |
| always on top | aina päällimmäisenä | |
| snap to screen edge | kiinnitä näytön reunaan | |
| opacity | peittävyys | |
| accent color | korostusväri | Windows |
| right-click | napsauta hiiren kakkospainikkeella / kakkospainike | Microsoft; macOS: osoita toissijaisesti |
| double-click | kaksoisnapsautus / kaksoisnapsauta | |
| drag | vedä | |
| mouse wheel | hiiren rulla | Ctrl + rulla |
| passkey | pääsyavain | Apple/Google-suomennos |
| connected apps | yhdistetyt sovellukset | |
| per-surface | käyttöympäristökohtainen | Claude Code, yhdistetyt sovellukset |
| trend curve (sparkline) | trendikäyrä (sparkline) | |
| Browse… / Cancel / Close / Quit | Selaa… / Peruuta / Sulje / Lopeta | Microsoft |
| Restore defaults | Palauta oletukset | |
| What's new | Mitä uutta | Microsoft; sivustoesittelyssä „uutuudet" |
