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
   nom = models.CharField(max_length=200,unique=True)
   prenom = models.CharField(max_length=200)
   photo=models.ImageField(
        upload_to=photo_path,
        #storage=AppEngineBlobStorage(),
        max_length=255,
        blank=False,
    )
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.nom
      
   class Meta:
      db_table = 'producteur'

class marche(models.Model):
    created_at = models.DateTimeField('date de création', auto_now_add=True)
    ville = models.CharField('ville', max_length=200)
    producteur = models.ManyToManyField(producteur, related_name='producteur', blank=True)
   
    class Meta:
        verbose_name = "marché!!"
        db_table = 'marche'

    def __str__(self):
        return str(self.ville)+'-'+str(self.producteur)

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

   def __str__(self):
      return self.nom
   class Meta:
      db_table = 'produit'

class refMarket(models.Model):
   ville = models.CharField(max_length=200)
   heure_deb = models.DateTimeField()
   heure_deb = models.DateTimeField()
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.ville

   class Meta:
      db_table = 'refmarket'


class metEnVente(models.Model):
   id_producteur=models.ForeignKey(producteur, on_delete=models.CASCADE)#Relation 1 à plusieurs
   id_produit= models.ManyToManyField(refProduit, related_name='produits', blank=True)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.id_producteur
   class Meta:
      db_table = 'metenvente'


class sInstalle(models.Model):
   id_producteur= models.ForeignKey('producteur', on_delete=models.CASCADE)
   id_market= models.ForeignKey('refmarket', on_delete=models.CASCADE)
 
   #id_market=models.ForeignKey(refMarket, on_delete=models.CASCADE) #Relation 1 à plusieurs
   created_at = models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return '{} - {}' .format(self.id_producteur,self.id_market)
   class Meta:
      db_table = 'sinstalle'
