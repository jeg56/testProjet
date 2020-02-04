from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^list$',views.listing),
    #url(r'^(?P<ville>[a-zA-Z]+)/$',views.list_producteur_ville),
    url(r'^(?P<id_product>[0-9]+)/$',views.list_producteur_ville),   

]
