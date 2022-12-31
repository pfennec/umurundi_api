from django.db import models

# Create your models here.

genres = [
    ["Masculin", "M"],
    ["Feminin", "F"]
]

type_lieu_de_naissances = [
    ["Hopital", "H"],
    ["Centre de santé", "CDS"],
    ["À Domicile", "D"],
]

class Umurundi(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    sexe = models.CharField(max_length=10, choices=genres)
    date_naissance = models.DateTimeField(auto_now=False)
    cni_pere = models.CharField(max_length=30, unique=True)
    cni_mere = models.CharField(max_length=30, unique=True)
    lieu_de_naissance = models.ForeignKey("LieuDeNaissance", on_delete=models.PROTECT)

    def __str__(self):
        return self.nom + " " + self.prenom




class LieuDeNaissance(models.Model):
    type_lieu_de_naissance = models.CharField(max_length=30, choices=type_lieu_de_naissances)
    nom = models.CharField(max_length=100, unique=True)
    commune = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    pays = models.CharField(max_length=100)


    def __str__(self):
     return self.type_lieu_de_naissance + " " + self.nom
   
