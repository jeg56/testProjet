from django.db import models

# Create your models here.
#PRODUCTEURS={
#   1:{'name':'Arnaud Jégoux'},
#  2:{'name':'Stéphanie demay'}
#}

#MARCHES=[
#   {'lieux':'OSSE','producteurs':PRODUCTEURS[1].get('name')},
#   {'lieux':'OSSE','producteurs':PRODUCTEURS[2].get('name')},
#   {'lieux':'CHATEAUGIRON','producteurs':PRODUCTEURS[1].get('name')}
#]


class producteur(models.Model):
   photo_path='.\\decouvrez_django\\disquaire_project\\client_magasin\\templates\\img\\Koala.jpg'
   nom_societe= models.CharField(max_length=200, unique=True)
   nom = models.CharField(max_length=200)
   prenom = models.CharField(max_length=200)
   photo=models.ImageField(
        upload_to=photo_path,
        #storage=AppEngineBlobStorage(),
        max_length=255,
        blank=False,
    )
   created_at = models.DateTimeField(auto_now_add=True)



class refProduit(models.Model):
   nom = models.CharField(max_length=200)
   photo_path='.\\decouvrez_django\\disquaire_project\\client_magasin\\templates\\img\\Koala.jpg'
   photo=models.ImageField(
      upload_to=photo_path,
      #storage=AppEngineBlobStorage(),
      max_length=255,
      blank=False,
   )
   created_at = models.DateTimeField(auto_now_add=True)


class metEnVente(models.Model):
   id_producteur=models.ForeignKey(producteur, on_delete=models.CASCADE)
   id_produit= models.ManyToManyField(refProduit, related_name='produits', blank=True)
   created_at = models.DateTimeField(auto_now_add=True)

class refMarket(models.Model):
   ville = models.CharField(max_length=200)
   heure_deb = models.DateTimeField()
   heure_deb = models.DateTimeField()
   created_at = models.DateTimeField(auto_now_add=True)

class sInstalle(models.Model):
   id_producteur= models.ManyToManyField(producteur, related_name='producteurs', blank=True)
   id_market=models.ForeignKey(refMarket, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)