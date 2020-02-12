from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import refMarket,refPlageHoraire
from django.db import connection
from django.template import loader
import requests
from geopy.geocoders import Nominatim

def index(request):
   listMarket=refMarket.objects.all()
   market=listMarket.filter()[:1].get()
   if request.method == 'POST':
      ville = request.POST.get('ville')
      listMarket=refMarket.objects.filter(ville__icontains=ville)

      if listMarket.exists():
         market=listMarket[:1].get()
     
 
      
   context={
      'listMarket':listMarket,
      'market':market
   }
   return render(request, 'market/index.html', context)


_geolocator = Nominatim()   
def upsert(request):
   messages=''
   title=''
   showMap=''
   latitude=None
   longitude=None
   latitude_fus=None
   longitude_fus=None
   nom=None
   adresse=None
   cp=None
   ville=None

   if request.method == 'POST':
      nom = request.POST.get('nom')
      adresse = request.POST.get('adresse')
      cp = request.POST.get('cp')
      ville = request.POST.get('ville')
      plageHoraire= refPlageHoraire.objects.get(id=1)
      

      location = _geolocator.geocode(adresse+' '+cp +' '+ville, timeout=5)
      if not location:
         latitude=None
         longitude=None
      else:
         latitude=location.latitude
         longitude=location.longitude

      verifNomMarche = refMarket.objects.filter(nom=nom)

      if verifNomMarche.exists():
         # Attention le marché existe déja
         messages='Sauf erreur de ma part ce marché existe déjà...'
         title= "ECHEC !!!!"
      else:
         ajoutVille = refMarket.objects.create(
            nom=nom,
            adresse=adresse,
            cp=cp,
            ville=ville,
            plageHoraire=plageHoraire,
            latitude=latitude,
            longitude=longitude
            )

            
         ajoutVille.save()
         messages='Ok c est bon !!...'
         title='SUCCESSSS !!!!'
         showMap='1'
         longitude_fus=str(longitude).replace(',','.')
         latitude_fus=str(latitude).replace(',','.')
   else:
      title= "Déclaration d'une nouvelle ville"
      
   context={
      'title':title,
      'messages':messages,
      'showMap':showMap,
      'latitude':latitude_fus,
      'longitude':longitude_fus,
      'adresse':'%s %s %s' % (adresse,cp,ville),
      'nom':nom
   }

   return render(request, 'market/upsert.html', context)
