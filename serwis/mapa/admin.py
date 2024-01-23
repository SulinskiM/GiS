from django.contrib import admin

# Register your models here.
from .models import Kategoria
from .models import Obiekt

class KategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'iloscObiektow')

    def iloscObiektow(self, obj):
        return len(Obiekt.objects.all().filter(kategoria=obj))

admin.site.register(Kategoria, KategoriaAdmin)

class ObiektAdmin(admin.ModelAdmin):
    list_display = ('title', 'opis', 'latitude', 'longitude', 'kategoria')
    list_filter = ('kategoria', )

admin.site.register(Obiekt, ObiektAdmin)