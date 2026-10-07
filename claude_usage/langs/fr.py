# -*- coding: utf-8 -*-
"""Français – UI strings of Claude Usage Monitor (only the keys that are not inline in i18n*.py).

French typography: a no-break space (U+00A0, a literal character – it looks like a normal space in an editor)
stands before every : ; ? ! so that the punctuation can never be wrapped onto the next line. Keep it when editing.
Form of address: "vous", as in the existing inline set.*, notify.* texts and on claudeusagemonitor.com/fr/.
"""

CODE = "fr"
NAME = "Français"

STRINGS = {
    # --- 'Message to the developer' window ---------------------------------------------------
    "fb.title": "Message au développeur",
    "fb.intro": "Une idée, un bug, ou l'application vous plaît tout simplement ? Écrivez-moi. Je lis personnellement chaque message – Vidovics Gábor, l'auteur du programme.",
    "fb.rating": "Note globale",
    "fb.rating_clear": "effacer",
    "fb.rating_hint": "facultatif – cliquez sur une étoile",
    "fb.rating_tip": "{} sur 5",
    "fb.name": "Nom",
    "fb.optional": "(facultatif)",
    "fb.email": "Adresse e-mail",
    "fb.email_hint": "seulement si vous souhaitez une réponse",
    "fb.message": "Message",
    "fb.message_ph": "Qu'est-ce qui fonctionne, qu'est-ce qui ne fonctionne pas, qu'est-ce qui manque ?",
    "fb.consent": "J'ai lu et j'accepte la {}.",
    "fb.privacy_title": "Politique de confidentialité",
    "fb.privacy_hide": "Masquer le texte",
    "fb.publish": "Ma note et mon nom (s'il est indiqué) peuvent être affichés sur claudeusagemonitor.com.",
    "fb.meta": "Envoyés avec le message : la version du programme ({0}), le système d'exploitation ({1}) et la langue de l'interface ({2}).",
    "fb.secure": "Connexion chiffrée (HTTPS) avec claudeusagemonitor.com.",
    "fb.cancel": "Annuler",
    "fb.send": "Envoyer",
    "fb.sending": "Envoi en cours…",
    "fb.sent": "Merci – votre message est bien arrivé !",
    "fb.sent_sub": "Je lis chaque message. Si vous avez indiqué une adresse e-mail, je vous répondrai par e-mail.",
    "fb.close": "Fermer",
    "fb.err_empty": "Écrivez d'abord un message ou choisissez une note.",
    "fb.err_email": "Cette adresse e-mail ne semble pas valide.",
    "fb.err_links": "Trop de liens dans le message.",
    "fb.err_consent": "Pour envoyer le message, veuillez accepter la politique de confidentialité.",
    "fb.err_network": "Impossible de joindre claudeusagemonitor.com. Vérifiez votre connexion et réessayez.",
    "fb.err_rate": "Trop de messages en peu de temps – veuillez réessayer plus tard.",
    "fb.err_server": "Le serveur n'a pas pu recevoir le message pour le moment. Veuillez réessayer plus tard.",
    "fb.privacy_text": (
        "Responsable du traitement : Vidovics Gábor, personne physique (Hongrie), auteur de Claude Usage Monitor. "
        "La politique de confidentialité complète est disponible sur le site web : https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "Données envoyées : ce que vous saisissez ici – nom (facultatif), adresse e-mail (facultative), message, "
        "note en étoiles – ainsi que, pour que je puisse comprendre le contexte : la version du programme, le nom "
        "et la version du système d'exploitation, la langue de l'interface, ainsi que la date et l'heure de l'envoi. "
        "Le serveur ne conserve aucune adresse IP ; pour prévenir les abus, il utilise uniquement une empreinte "
        "(hachage) renouvelée chaque jour, qui ne permet pas de retrouver l'adresse."
        "\n\n"
        "Finalités : lire votre message et y répondre, et améliorer le programme (intérêt légitime, "
        "art. 6, par. 1, point f), du RGPD ; la réponse elle-même est apportée à votre demande). Votre note et "
        "votre nom n'apparaissent sur le site web que si vous cochez la case distincte prévue à cet effet "
        "(consentement, art. 6, par. 1, point a), du RGPD), et seulement après vérification par l'auteur ; "
        "vous pouvez retirer ce consentement à tout moment."
        "\n\n"
        "Durée de conservation : les messages, 2 ans au maximum ; une note publiée, jusqu'au retrait de "
        "votre consentement. Si l'auteur a activé le transfert par e-mail, une copie arrive également dans la "
        "boîte de réception de l'auteur."
        "\n\n"
        "Qui y a accès : uniquement le responsable du traitement et – en qualité de sous-traitant – l'hébergeur "
        "(serveur dans l'UE, en Allemagne). Rien n'est vendu ni transmis ; il n'y a ni profilage "
        "ni prise de décision automatisée."
        "\n\n"
        "Vos droits : accès, rectification, effacement, limitation du traitement, opposition, retrait du "
        "consentement, ainsi que le droit d'introduire une réclamation auprès d'une autorité de contrôle (en "
        "Hongrie : la NAIH, naih.hu ; en France : la CNIL, cnil.fr) ou auprès de l'autorité de votre pays. "
        "Contact : ce formulaire ou le site web."
        "\n\n"
        "Transmission : chiffrée (HTTPS/TLS) vers claudeusagemonitor.com. Version de la présente politique : 6 octobre 2026."
    ),
    # --- context menu / Settings --------------------------------------------------------------
    "menu.feedback": "Message au développeur…",
    "set.show_feedback_icon": "Icône de message dans l'en-tête du panneau",
}

# macOS wording: nothing to override – the four mac keys are inline in i18n_mac.py
STRINGS_MAC = {}
