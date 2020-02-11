from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import refMarket
from django.db import connection
from django.template import loader

def index(request):
   context={
      'listMarket':refMarket.objects.all()
   }
   return render(request, 'market/index.html', context)



def upsert(request):
   messages=''
   title=''

   if request.method == 'POST':
      ville = request.POST.get('ville')
      action = request.POST.get('action')
      

      verifVille = refMarket.objects.filter(ville=ville)
      if verifVille.exists():
         # Attention le marché existe déja
         messages='Sauf erreur de ma part ce marché existe déjà...'
         title= "ECHEC !!!!"
      else:
         ajoutVille = refMarket.objects.create(
            ville=ville
            )
         ajoutVille.save()
         messages='Ok c est bon !!...'
         title='SUCCESSSS !!!!'
   else:
      title= "Déclaration d'une nouvelle ville"
      
   context={
      'title':title,
      'messages':messages
   }

   return render(request, 'market/upsert.html', context)
