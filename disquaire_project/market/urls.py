from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$',views.index, name='index'),
   url(r'^change/(?P<ville>[a-zA-Z]+)/$',views.upsert,name='upsert'),
   url(r'^new/$',views.upsert, name='upsert'),
   url(r'^list/$',views.listMarket, name='list'),
]
