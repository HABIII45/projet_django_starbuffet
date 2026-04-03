from django.db import models


# Create your models here.
class Traiteur(models.Model):
    nomcomplet=models.CharField(max_length=100,verbose_name='Nom complet')
    specialite=models.TextField(verbose_name='Specialité')
    description=models.TextField(verbose_name='Description')
    adresse=models.CharField(max_length=100,verbose_name='Adresse')
    est_actif=models.BooleanField(default=True,verbose_name='Etat')
    email=models.EmailField(max_length=255,verbose_name='Email')
    date_creation=models.DateField(auto_now_add=True,verbose_name='Date de création')
    telephone=models.CharField(max_length=11,verbose_name='Téléphone')
    image=models.URLField(max_length=300,blank=True,verbose_name='Image')
     