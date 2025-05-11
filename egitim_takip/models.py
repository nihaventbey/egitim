
from django.db import models
from django.contrib.auth.models import User

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
