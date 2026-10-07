# REVIEW – Français (fr), fenêtre « Message au développeur »

## Lektor

Relu : les 34 textes, contre EN/HU. Forme d'adresse **vous**, comme les textes inline `set.*`, `notify.*`,
`backup.*` et le site claudeusagemonitor.com/fr/ (« Votre message sert uniquement à vous répondre… »).
Nom du document « Politique de confidentialité » confirmé (= `help.privacy` et pied de page du site).
Tous les faits, articles, durées, droits et l'URL de `fb.privacy_text` sont conservés.

Typographie : les espaces insécables avant : ; ? ! sont des caractères U+00A0 littéraux (23 occurrences,
vérifiées par script : aucune ponctuation haute sans espace insécable). La docstring, qui annonçait à tort des
échappements ` `, a été corrigée pour le dire.

Modifications (12) :

- fb.intro : « …ou vous aimez tout simplement l'appli ? … Chaque message est lu par moi-même, Vidovics Gábor, … » → « …ou l'application vous plaît tout simplement ? … Je lis personnellement chaque message – Vidovics Gábor, … » – « appli » familier, passif lourd
- fb.message_ph : « Qu'est-ce qui marche, … ne marche pas… » → « Qu'est-ce qui fonctionne, … ne fonctionne pas… » – registre homogène avec « vous »
- fb.privacy_hide : « Masquer la politique » → « Masquer le texte » – on masque l'encadré, pas la politique
- fb.secure : « Connexion chiffrée (HTTPS) vers … » → « …avec … » – tournure usuelle
- fb.sending : « Envoi… » → « Envoi en cours… » – formule standard Windows
- fb.sent_sub : « Si vous avez laissé une adresse e-mail, je vous répondrai à cette adresse. » → « Si vous avez indiqué une adresse e-mail, je vous répondrai par e-mail. » – répétition d'« adresse »
- fb.err_consent : « Pour envoyer, veuillez… » → « Pour envoyer le message, veuillez… » – « envoyer » sans complément
- fb.privacy_text : « adresse e-mail (facultatif) » → « adresse e-mail (facultative) » – accord au féminin
- fb.privacy_text : « Ce qui est envoyé » / « Pourquoi » / « Combien de temps » → « Données envoyées » / « Finalités » / « Durée de conservation » – intitulés du registre RGPD/CNIL
- fb.privacy_text : « une empreinte (hash) qui change chaque jour et ne peut pas être reconvertie en adresse » → « une empreinte (hachage) renouvelée chaque jour, qui ne permet pas de retrouver l'adresse » – terme CNIL, calque supprimé ; « stocke » → « conserve »
- fb.privacy_text : « point f) du RGPD ; la réponse elle-même, à votre demande » → « point f), du RGPD ; la réponse elle-même est apportée à votre demande » (idem point a) ; « limitation » → « limitation du traitement » ; « parvient à la boîte de messagerie » → « arrive dans la boîte de réception » – ellipse complétée, terme exact
- fb.privacy_text : « Rien n'est vendu ni transmis à des tiers » → « Rien n'est vendu ni transmis » ; « Version … : 2026-10-06 » → « 6 octobre 2026 » – fidèle à l'anglais ; date à la française

Doutes restants :
- Les textes inline de la fenêtre de connexion (`dlg.*`, `err.session_expired*`, `set.reset_confirm`) tutoient,
  le reste de l'interface vouvoie. Ce module suit la majorité (vous) ; à harmoniser un jour dans les fichiers inline.
- Il n'existe pas de `glossary-fr.md`. La politique complète à l'URL est en anglais pour les visiteurs français
  (le site charge legal/en.html pour toutes les langues sauf le hongrois) ; la notice ne prétend pas le contraire.
