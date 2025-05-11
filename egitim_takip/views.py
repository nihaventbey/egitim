
from django.shortcuts import render
from .models import EgitimMerkezi, TesisImkani, Yemekhane, Sinif

def ana_sayfa(request):
    merkezler = EgitimMerkezi.objects.all()
    return render(request, "ana_sayfa.html", {"merkezler": merkezler})

def egitim_merkezi_detay(request, pk):
    merkez = EgitimMerkezi.objects.get(pk=pk)
    try:
        tesis = merkez.tesisimkani
        yemekler = Yemekhane.objects.filter(tesis=tesis)
    except:
        tesis = None
        yemekler = []
    siniflar = Sinif.objects.filter(egitim_merkezi=merkez)
    return render(request, "egitim_merkezi_detay.html", {
        "merkez": merkez,
        "tesis": tesis,
        "yemekler": yemekler,
        "siniflar": siniflar
    })

def dashboard(request):
    merkez_sayisi = EgitimMerkezi.objects.count()
    toplam_kontenjan = Sinif.objects.all().aggregate(models.Sum("kontenjan"))["kontenjan__sum"] or 0
    toplam_yemek = Yemekhane.objects.count()
    return render(request, "dashboard.html", {
        "merkez_sayisi": merkez_sayisi,
        "toplam_kontenjan": toplam_kontenjan,
        "toplam_yemek": toplam_yemek,
    })
