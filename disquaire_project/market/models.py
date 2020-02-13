from django.db import models

# Create your models here.



class refPlageHoraire(models.Model):
   JOURS_DE_LA_SEMAINE = (
         (1,'Lundi'),
         (2,'Mardi'),
         )
   jour=models.IntegerField(verbose_name="Jours du marché",choices=JOURS_DE_LA_SEMAINE)
   hDebut= models.TimeField(verbose_name="Heure d'ouverture du marché", help_text="Heure d'ouverture du marché",blank=False)  
   hFin= models.TimeField(verbose_name="Heure de fermeture du marché", help_text="Heure de fermeture du marché",blank=False) 
   label= models.CharField(verbose_name="Libellé de la tranche horaire", max_length=50,blank=True) 
   created_at = models.DateTimeField(auto_now_add=True)

   def getJour(self):
      return '%s' %  (self.get_jour_display())
   def __str__(self):
      description=''
      if self.label=='' :
         description = '%s - %s  %s <-> %s' % (self.id, self.get_jour_display(), self.hDebut,self.hFin)
      else:
         description = '%s - %s  %s' % (self.id, self.get_jour_display(),self.label)
         
      return description

   class Meta:
      db_table = 'refplagehoraire'

class refMarket(models.Model):
   nom = models.CharField(verbose_name='Nom du marché',max_length=200)
   adresse = models.CharField(verbose_name='adresse',max_length=200)
   cp = models.CharField(verbose_name='Code postal',max_length=5)
   ville = models.CharField(verbose_name='Ville',max_length=200)
   latitude =models.DecimalField(verbose_name='Coordonnée latitude', help_text='Coordonnée latitude du marché',blank=True,null=True,max_digits=15,decimal_places=11) 
   longitude =models.DecimalField(verbose_name='Coordonnée longitude', help_text='Coordonnée longitude du marché',blank=True,null=True,max_digits=15,decimal_places=11) 
   plageHoraire = models.ForeignKey(refPlageHoraire, on_delete=models.CASCADE) 
   created_at = models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return '%s - %s' % (self.id, self.nom)

   class Meta:
      db_table = 'refmarket'

class producteur(models.Model):
   nom = models.CharField(max_length=200,unique=True)
   prenom = models.CharField(max_length=200)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.nom
      
   class Meta:
      db_table = 'producteur'



class sInstalle(models.Model):
   #producteur= models.ManyToManyField(producteur, related_name='sinstalleproducteur', blank=True)
   producteur= models.ForeignKey('producteur', related_name='sinstalleproducteur', on_delete=models.CASCADE)
   market= models.ManyToManyField(refMarket, related_name='refmarket', blank=True)
   #market= models.ForeignKey('refmarket', on_delete=models.CASCADE)
 
   #id_market=models.ForeignKey(refMarket, on_delete=models.CASCADE) #Relation 1 à plusieurs
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return "%s - %s" % (
            self.producteur.nom,
            ", ".join(mark.nom for mark in self.market.all()),
        )

   class Meta:
      db_table = 'sinstalle'     
