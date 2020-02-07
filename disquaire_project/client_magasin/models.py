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
   nom = models.CharField(max_length=200,unique=True)
   prenom = models.CharField(max_length=200)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.nom
      
   class Meta:
      db_table = 'producteur'

class refProduit(models.Model):
   nom = models.CharField(max_length=200)
   type = models.CharField(max_length=200)
   created_at = models.DateTimeField(auto_now_add=True)
   imgfile =   models.ImageField(upload_to="gallery")

   def __str__(self):
      return self.nom
   class Meta:
      db_table = 'refproduit'

class refMarket(models.Model):
   ville = models.CharField(max_length=200)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.ville

   class Meta:
      db_table = 'refmarket'

      



class sInstalle(models.Model):
   producteur= models.ManyToManyField(producteur, related_name='sinstalleproducteur', blank=True)
   #producteur= models.ForeignKey('producteur', on_delete=models.CASCADE)
   market= models.ManyToManyField(refMarket, related_name='refmarket', blank=True)
   #market= models.ForeignKey('refmarket', on_delete=models.CASCADE)
 
   #id_market=models.ForeignKey(refMarket, on_delete=models.CASCADE) #Relation 1 à plusieurs
   created_at = models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return '{} - {}' .format(self.producteur,self.market)
   class Meta:
      db_table = 'sinstalle'

class vend(models.Model):
   producteur= models.ForeignKey('producteur', on_delete=models.CASCADE)
   produit= models.ManyToManyField(refProduit, related_name='produit', blank=True)
   def __str__(self):
      return '{} - {}' .format(self.producteur,self.produit)
   class Meta:
      db_table = 'vend'
