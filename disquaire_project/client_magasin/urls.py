from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^list$',views.listing),
    #url(r'^(?P<ville>[a-zA-Z]+)/$',views.list_producteur_ville),
    url(r'^(?P<id_product>[0-9]+)/$',views.list_producteur_ville),  
    url(r'^producteur/(?P<id_product>[0-9]+)/$',views.list_producteur_marche),   
    url(r'^marche/(?P<id_marche>[0-9]+)/$',views.list_marche_producteur),  
    url(r'^listproducteur$',views.list_producteur), 
    url(r'^listproduit$',views.list_produit), 
    url(r'^listmarche$',views.list_marche),   
]
