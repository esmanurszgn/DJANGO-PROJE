from django.contrib import admin
from .models import     Yazar, KullaniciMesaj,Dergi


admin.site.register(Yazar)
admin.site.register(Dergi)

@admin.register(KullaniciMesaj)
class MesajAdmin(admin.ModelAdmin):
    list_display =  ('isim','soyisim','mail','yazi')

