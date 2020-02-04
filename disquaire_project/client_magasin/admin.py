from django.contrib import admin

# Register your models here.

from .models import refMarket,metEnVente,refProduit,producteur,sInstalle,marche


admin.site.register(refMarket)
admin.site.register(metEnVente)
admin.site.register(refProduit)
admin.site.register(producteur)
admin.site.register(sInstalle)
admin.site.register(marche)

