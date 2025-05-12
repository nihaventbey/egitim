
from django.contrib import admin
from .models import EgitimMerkezi, TesisImkani, Yemekhane, Sinif

class YemekhaneInline(admin.TabularInline):
    model = Yemekhane
    extra = 1

class TesisImkaniAdmin(admin.ModelAdmin):
    inlines = [YemekhaneInline]
    list_display = ('egitim_merkezi', 'yatakli_kontenjan', 'yataksiz_kontenjan')

class SinifAdmin(admin.ModelAdmin):
    list_display = ('ad', 'egitim_merkezi', 'kontenjan')
    list_filter = ('egitim_merkezi',)

class EgitimMerkeziAdmin(admin.ModelAdmin):
    list_display = ('ad', 'mudur', 'telefon', 'konum')
    search_fields = ('ad', 'adres')

admin.site.register(EgitimMerkezi, EgitimMerkeziAdmin)
admin.site.register(TesisImkani, TesisImkaniAdmin)
admin.site.register(Sinif, SinifAdmin)

from .models import SiteAyar
admin.site.register(SiteAyar)

from .models import EgitimTuru, Egitim
admin.site.register(EgitimTuru)
admin.site.register(Egitim)

