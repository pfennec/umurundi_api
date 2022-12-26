from django.db import models

# Create your models here.


class Umurundi(models.Model):
   id = models.BigAutoField()
   nom = models.CharField(max_length=200)
   prenom = models.CharField(max_length=200)
   sexe = models.CharField(max_length=10)
   date_naissance = models.DateField(auto_now=False)
   hopital = models.CharField(max_length=200)
   lieu_naissance = models.CharField(max_length=200)
   nom_pere = models.CharField(max_length=200)
   prenom_pere = models.CharField(max_length=200)
   nom_mere = models.CharField(max_length=200)
   prenom_mere = models.CharField(max_length=200)
   residence = models.DateTimeField('date published')

class Hopital(models.Model):
    id = models.AutoField()
    name= models.charfild(max_length=100)
    commune = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    pays=models.CharField(max_length=100)