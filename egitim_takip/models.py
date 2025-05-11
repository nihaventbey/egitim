
from django.db import models
from django.contrib.auth.models import User
# egitim_takip/models.py
from django.db import models
from django.conf import settings


class ThemeConfiguration(models.Model):
    THEME_CHOICES = [
        ('light', 'Açık'),
        ('dark', 'Koyu'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    theme = models.CharField(max_length=5, choices=THEME_CHOICES, default='light')


class EgitimMerkezi(models.Model):
    ad = models.CharField(max_length=200)
    mudur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="mudur_egitim_merkezleri")
    sef_1 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sef1_egitim_merkezleri")
    sef_2 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sef2_egitim_merkezleri")
    sef_3 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sef3_egitim_merkezleri")
    istatistik_sef = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="istatistik_egitim_merkezleri")
    adres = models.TextField()
    telefon = models.CharField(max_length=20)
    konum = models.CharField(max_length=255)

    def __str__(self):
        return self.ad

class TesisImkani(models.Model):
    egitim_merkezi = models.OneToOneField(EgitimMerkezi, on_delete=models.CASCADE)
    yatakli_kontenjan = models.PositiveIntegerField()
    yataksiz_kontenjan = models.PositiveIntegerField()

    def __str__(self):
        return f"Tesis ({self.egitim_merkezi.ad})"

class Yemekhane(models.Model):
    tesis = models.ForeignKey(TesisImkani, on_delete=models.CASCADE)
    ogun_adi = models.CharField(max_length=100)
    fiyat = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.ogun_adi} - {self.fiyat}₺"

class Sinif(models.Model):
    egitim_merkezi = models.ForeignKey(EgitimMerkezi, on_delete=models.CASCADE)
    ad = models.CharField(max_length=100)
    kontenjan = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.ad} ({self.kontenjan} kişi)"


   
class SiteAyar(models.Model):
    site_adi = models.CharField("Site adı", max_length=200, default="Eğitim Takip Sistemi")
    meta_baslik = models.CharField("Meta başlık", max_length=200, blank=True)
    meta_aciklama = models.TextField("Meta açıklama", blank=True)
    meta_etiketler = models.CharField("Meta etiketler", max_length=300, blank=True)
    header_logo = models.ImageField("Header logosu", upload_to="logo/", blank=True, null=True)
    footer_yazi = models.CharField("Alt bilgi yazısı", max_length=255, blank=True)
    iletisim_email = models.EmailField("İletişim e-posta", blank=True)
    iletisim_telefon = models.CharField("İletişim telefonu", max_length=20, blank=True)
    tema = models.CharField("Tema", max_length=10, choices=[("acik", "Açık"), ("koyu", "Koyu")], default="koyu")

    class Meta:
        verbose_name = "Site Ayarı"
        verbose_name_plural = "Site Ayarları"

    def __str__(self):
        return self.site_adi
