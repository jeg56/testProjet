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


class Producteurs(models.Model):
   photo_path='C:\\Users\frup68962\\Documents\\IMG_20191216_125946.jpg'
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



class ref_produits(models.Model):
   nom = models.CharField(max_length=200)
   prenom = models.CharField(max_length=200)
   photo_path='C:\\Users\frup68962\\Documents\\IMG_20191216_125946.jpg'
   photo=models.ImageField(
      upload_to=photo_path,
      #storage=AppEngineBlobStorage(),
      max_length=255,
      blank=False,
   )
   created_at = models.DateTimeField(auto_now_add=True)


class metEnVente(models.Model):
   id_producteur=models.ForeignKey(Producteurs, on_delete=models.CASCADE)
   id_produit= models.ManyToManyField(ref_produits, related_name='produits', blank=True)
   created_at = models.DateTimeField(auto_now_add=True)

class ref_market(models.Model):
   ville = models.CharField(max_length=200)
   heure_deb = models.DateTimeField()
   heure_deb = models.DateTimeField()
   created_at = models.DateTimeField(auto_now_add=True)

class sinstalle(models.Model):
   id_producteur= models.ManyToManyField(Producteurs, related_name='producteurs', blank=True)
   id_market=models.ForeignKey(ref_market, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)