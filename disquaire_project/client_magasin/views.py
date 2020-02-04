from django.shortcuts import render
from django.http import HttpResponse
from .models import producteur, refProduit, refMarket, metEnVente, sInstalle, marche
from django.db import connection
from django.template import loader
#from .models import MARCHES

# Create your views here.
def index(request):
    template = loader.get_template('client_magasin/index.html')
    return HttpResponse(template.render(request=request))


def listing(request):
   #MARCHES=refMarket.objects.all()

   #album = Album.objects.get(pk=album_id)
   #artists = " ".join([artist.name for artist in album.artists.all()])
   #message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)


   print('-------------------------------------------')
   print('-------------------------------------------')
   print(sInstalle.objects.all().query)
   markets = marche.objects.get(pk=1)
   artists = marche.producteur.all()
   producteurs = producteur.objects.all()
   listeProd = " ".join([aaaa.nom for aaaa in producteurs.markets.all()])
   message = "Le marché {} possede les producteurs  {}".format(markets.nom, listeProd)

   print('*******' +message)

   print(sInstalle.objects.filter(id_producteur__nom__contains='toto').query)
   
   print('-------------------------------------------')
   print('-------------------------------------------')
   print('-------------------------------------------')
   MARCHES=sInstalle.objects.filter(id_producteur__nom__contains='toto').all()
   MARCHES=sInstalle.objects.filter(id_producteur_id=True).all()
   #MARCHES=producteur.objects.filter(sInstalle__id_producteur__isnull=True)
   with connection.cursor() as cursor:
      cursor.execute("select A.nom as nom,C.ville as ville from producteur A left join sinstalle B on A.id=B.id_producteur_id left join refmarket C on C.id=B.id_market_id;")
      rows = cursor.fetchall()	
   detailMarche=[]
   for row in rows:
      nom=row[0]
      ville=row[1]
      detailMarche.append("<li>{} est à {}</li>".format(nom,ville))

   message = """<ul>{}</ul>""".format("\n".join(detailMarche))
   return HttpResponse(message)


def list_producteur_ville(request,id_product):
   with connection.cursor() as cursor:
      cursor.execute("select A.nom as nom,C.ville as ville from producteur A left join sinstalle B on A.id=B.id_producteur_id left join refmarket C on C.id=B.id_market_id where A.id=%s;"% (id_product))
      rows = cursor.fetchall()	
   list_producteurs=[]
   for row in rows:
      nom=row[0]
      ville=row[1]
      list_producteurs.append("<li>{} est à {}</li>".format(nom,ville))
      
   message = """<ul>Le producteur n° : {} - {} </ul>""".format(id_product,"\n".join(list_producteurs))
   return HttpResponse(message)

