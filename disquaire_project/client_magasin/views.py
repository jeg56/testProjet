from django.shortcuts import render
from django.http import HttpResponse
#from .models import MARCHES

# Create your views here.
def index(request):
   message ="Salut tout le monde"
   return HttpResponse(message)


def listing(request):
   detailMarche = ["<li>{} {}</li>".format(marche['lieux'],marche['producteurs']) for marche in MARCHES]
   message = """<ul>{}</ul>""".format("\n".join(detailMarche))
   return HttpResponse(message)

def list_producteur_ville(request,ville):
   list_producteurs=[]
   for marche in MARCHES:
       if ville in marche['lieux'] :
          list_producteurs.append("<li>{}</li>".format(marche['producteurs']))

   message = """<ul>Pour la ville : {} on a les producteurs {} </ul>""".format(ville,"\n".join(list_producteurs))
   return HttpResponse(message)

