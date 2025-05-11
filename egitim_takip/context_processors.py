from .models import SiteAyar

def site_ayar(request):
    try:
        ayar = SiteAyar.objects.first()
    except:
        ayar = None
    return {
        "site_adi": ayar.site_adi if ayar else "Eğitim Takip Sistemi",
        "meta_aciklama": ayar.meta_aciklama if ayar else "",
        "meta_etiketler": ayar.meta_etiketler if ayar else "",
        "footer_yazi": ayar.footer_yazi if ayar else "",
        "tema": ayar.tema if ayar else "koyu",
    }
