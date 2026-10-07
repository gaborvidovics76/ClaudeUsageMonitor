# -*- coding: utf-8 -*-
"""Türkçe – UI strings of Claude Usage Monitor (only the keys missing from the inline tables)."""

CODE = "tr"
NAME = "Türkçe"

STRINGS = {
    # "Geliştiriciye mesaj" window
    "fb.cancel": "İptal",
    "fb.close": "Kapat",
    "fb.consent": "{} metnini okudum ve kabul ediyorum.",
    "fb.email": "E-posta",
    "fb.email_hint": "yalnızca yanıt almak istiyorsanız",
    "fb.err_consent": "Göndermek için lütfen Gizlilik Bildirimi'ni kabul edin.",
    "fb.err_email": "Bu e-posta adresi geçerli görünmüyor.",
    "fb.err_empty": "Önce bir mesaj yazın veya bir puan seçin.",
    "fb.err_links": "Mesajda çok fazla bağlantı var.",
    "fb.err_network": "claudeusagemonitor.com'a ulaşılamadı. Bağlantınızı kontrol edip yeniden deneyin.",
    "fb.err_rate": "Kısa sürede çok fazla mesaj gönderildi – lütfen daha sonra yeniden deneyin.",
    "fb.err_server": "Sunucu mesajı şu anda alamadı. Lütfen daha sonra yeniden deneyin.",
    "fb.intro": (
        "Bir fikriniz mi var, bir hata mı buldunuz, yoksa programı sadece beğendiniz mi? Bana yazın. "
        "Her mesajı bizzat ben okuyorum – Vidovics Gábor, programın yazarı."
    ),
    "fb.message": "Mesaj",
    "fb.message_ph": "Ne çalışıyor, ne çalışmıyor, ne eksik?",
    "fb.meta": "Mesajla birlikte gönderilenler: program sürümü ({0}), işletim sistemi ({1}), arayüz dili ({2}).",
    "fb.name": "Ad",
    "fb.optional": "(isteğe bağlı)",
    "fb.privacy_hide": "Bildirimi gizle",
    "fb.privacy_text": (
        "Veri sorumlusu: Vidovics Gábor, gerçek kişi (Macaristan), Claude Usage Monitor programının yazarı. "
        "Gizlilik politikasının tam metni web sitesinde yer almaktadır: https://claudeusagemonitor.com/#privacy"
        "\n\n"
        "Gönderilen veriler: buraya yazdıklarınız – ad (isteğe bağlı), e-posta adresi (isteğe bağlı), mesaj, "
        "yıldız puanı – ve bağlamı anlayabilmem için: program sürümü, işletim sisteminin adı ve sürümü, "
        "arayüz dili ve gönderim zamanı. Sunucu IP adresini saklamaz; kötüye kullanımı önlemek için yalnızca "
        "her gün değişen ve adrese geri dönüştürülemeyen bir karma (hash) değeri kullanır."
        "\n\n"
        "Amaç: mesajınızı okumak ve yanıtlamak ile programı geliştirmek (meşru menfaat, GDPR m. 6/1-f; "
        "yanıtın kendisi sizin talebiniz üzerine). Puanınız ve adınız web sitesinde yalnızca bunun için "
        "ayrılan kutuyu işaretlerseniz (rıza, GDPR m. 6/1-a) ve ancak yazar inceledikten sonra görünür; bu "
        "rızanızı istediğiniz zaman geri çekebilirsiniz."
        "\n\n"
        "Saklama süresi: mesajlar en fazla 2 yıl; yayımlanan puan, rızanızı geri çekene kadar. Yazar e-posta "
        "yönlendirmesini açmışsa bir kopya yazarın posta kutusuna da ulaşır."
        "\n\n"
        "Kimler görür: yalnızca veri sorumlusu ve – veri işleyen sıfatıyla – barındırma sağlayıcısı (sunucu "
        "AB'de, Almanya'dadır). Hiçbir veri satılmaz veya üçüncü kişilere aktarılmaz; profilleme ve otomatik "
        "karar verme yapılmaz."
        "\n\n"
        "Haklarınız: erişim, düzeltme, silme, işlemenin kısıtlanması, itiraz, rızanın geri çekilmesi ve bir "
        "denetim makamına (Macaristan'da: NAIH, naih.hu) ya da kendi ülkenizin denetim makamına şikâyette "
        "bulunma. İletişim: bu form veya web sitesi."
        "\n\n"
        "İletim: claudeusagemonitor.com'a şifreli bağlantıyla (HTTPS/TLS). Bu bildirimin sürümü: 6 Ekim 2026."
    ),
    "fb.privacy_title": "Gizlilik Bildirimi",
    "fb.publish": "Puanım ve adım (verdiysem) claudeusagemonitor.com'da gösterilebilir.",
    "fb.rating": "Genel puan",
    "fb.rating_clear": "temizle",
    "fb.rating_hint": "isteğe bağlı – bir yıldıza tıklayın",
    "fb.rating_tip": "5 üzerinden {}",
    "fb.secure": "claudeusagemonitor.com'a şifreli bağlantı (HTTPS).",
    "fb.send": "Gönder",
    "fb.sending": "Gönderiliyor…",
    "fb.sent": "Teşekkürler – mesajınız ulaştı!",
    "fb.sent_sub": "Her mesajı okuyorum. E-posta adresinizi bıraktıysanız o adrese yanıt vereceğim.",
    "fb.title": "Geliştiriciye mesaj",
    # menu / settings
    "menu.feedback": "Geliştiriciye mesaj…",
    "set.show_feedback_icon": "Panel başlığında mesaj simgesi",
}

# the four macOS-worded keys already exist inline in i18n_mac.py
STRINGS_MAC = {}
