from django.shortcuts import render
from django.http import HttpResponse
from .models import producteur, refProduit, refMarket,sInstalle,vend
from django.db import connection
from django.template import loader
#from .models import MARCHES

# Create your views here.
def index(request):
   messageFinal=[]
   results = producteur.objects.get(pk=2)
   results2=sInstalle.objects.filter(producteur=results)
   for item in results2:
      val1=item.market.all()
      for item2 in val1:
         message = "Le producteur {} est au maché {}".format(results, item2)
         messageFinal.append("<li>{}</li>".format(message))

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
   print('-------------------------------------------')
   monMarche = refMarket.objects.get(pk=1)
   print('-------------------------------------------')
   print('-------------------------------------------')
#   results = sInstalle.objects.all()
#   messageFinal=[]
#   for item in results:
#      val1=item.producteur.all()
#      for item2 in val1:
#        
#         message = "Le nom du producteur {}. Il a été écrit par {}".format(item2, monMarche)
#         messageFinal.append("<li>{}</li>".format(message))
#         print(messageFinal)
#   return HttpResponse('<ul>{}</ul>'.format("".join(messageFinal)))
   messageFinal=[]
   results = producteur.objects.get(pk=2)
   results2=sInstalle.objects.filter(producteur=results)
   for item in results2:
      val1=item.market.all()
      for item2 in val1:
         message = "Le producteur {} est au maché {}".format(results, item2)
         messageFinal.append("<li>{}</li>".format(message))
   return HttpResponse('<ul>{}</ul>'.format("".join(messageFinal)))

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

def list_producteur_marche(request,id_product):
   messageFinal=[]
   results = producteur.objects.get(pk=id_product)
   results2=sInstalle.objects.filter(producteur=results)
   for item in results2:
      val1=item.market.all()
      for item2 in val1:
         message = "Le producteur {} est au marché {}".format(results, item2)
         messageFinal.append("<li>{}</li>".format(message))
   messageFinal.append('<br>')
   results2=vend.objects.filter(producteur=results)
   for item in results2:
      val1=item.produit.all()
      for item2 in val1:
         message = "Le producteur {} vend {}".format(results, item2)
         messageFinal.append("<li>{}</li>".format(message))

   return HttpResponse('<ul>{}</ul>'.format("".join(messageFinal)))

   
def list_marche_producteur(request,id_marche):
   messageFinal=[]
   results = refMarket.objects.get(pk=id_marche)
   results2=sInstalle.objects.filter(market=results)
   for item in results2:
      val1=item.producteur.all()
      for item2 in val1:
         message = "Le producteur {} est au marché {}".format(item2, results)
         messageFinal.append("<li>{}</li>".format(message))
   return HttpResponse('<ul>{}</ul>'.format("".join(messageFinal)))



def list_producteur(request):
   messageFinal=[]
   results = producteur.objects.all()
   for item in results:
      messageFinal.append("<li>{}-{}</li>".format(item.nom,item.prenom))
   return HttpResponse('Liste des producteurs :<ul>{}</ul>'.format("".join(messageFinal)))


def list_marche(request):
   messageFinal=[]
   results = refMarket.objects.all()
   for item in results:
      messageFinal.append("<li>{}</li>".format(item.ville))
   return HttpResponse('Liste des marchés :<ul>{}</ul>'.format("".join(messageFinal)))


def list_produit(request):
   messageFinal=[]
   results = refProduit.objects.all()
   for item in results:
      messageFinal.append("<li>{} - {}</li>".format(item.nom,item.type))
   return HttpResponse('Liste des produits :<ul>{}</ul>'.format("".join(messageFinal)))