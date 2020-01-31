from django.contrib import admin

# Register your models here.

from .models import refMarket,metEnVente,refProduit,producteur,sInstalle


#admin.site.register(refMarket)
admin.site.register(metEnVente)
admin.site.register(refProduit)
admin.site.register(producteur)
admin.site.register(sInstalle)


class RefMarketInline(admin.TabularInline):
    model = refMarket.ville # the query goes through an intermediate table.
    extra = 1


@admin.register(refMarket)
class RefMarketAdmin(admin.ModelAdmin):
    inlines = [RefMarketInline,]