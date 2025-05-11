
from django.contrib.auth.models import User
from egitim_takip.models import EgitimMerkezi, TesisImkani, Yemekhane, Sinif

# Kullanıcılar
admin = User.objects.create_superuser(username="admin", password="admin123", email="admin@example.com")
mudur = User.objects.create_user(username="mudur", password="mudur123")
sef1 = User.objects.create_user(username="sef1", password="sef123")
sef2 = User.objects.create_user(username="sef2", password="sef123")
sef3 = User.objects.create_user(username="sef3", password="sef123")
istat = User.objects.create_user(username="istatistikci", password="istat123")

# Eğitim Merkezi
merkez = EgitimMerkezi.objects.create(
    ad="Ankara Eğitim Merkezi",
    mudur=mudur,
    sef_1=sef1,
    sef_2=sef2,
    sef_3=sef3,
    istatistik_sef=istat,
    adres="Çankaya, Ankara",
    telefon="0312 123 45 67",
    konum="39.9208, 32.8541"
)

# Tesis ve Yemekhane
tesis = TesisImkani.objects.create(
    egitim_merkezi=merkez,
    yatakli_kontenjan=50,
    yataksiz_kontenjan=100
)

Yemekhane.objects.create(tesis=tesis, ogun_adi="Kahvaltı", fiyat=35.00)
Yemekhane.objects.create(tesis=tesis, ogun_adi="Öğle Yemeği", fiyat=50.00)
Yemekhane.objects.create(tesis=tesis, ogun_adi="Akşam Yemeği", fiyat=45.00)

# Sınıflar
Sinif.objects.create(egitim_merkezi=merkez, ad="Sınıf A", kontenjan=30)
Sinif.objects.create(egitim_merkezi=merkez, ad="Sınıf B", kontenjan=25)
