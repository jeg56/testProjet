from django.contrib import admin

# Register your models here.

from .models import refMarket,refProduit,producteur,sInstalle,vend


admin.site.register(refMarket)
admin.site.register(refProduit)
admin.site.register(producteur)
admin.site.register(sInstalle)
admin.site.register(vend)
