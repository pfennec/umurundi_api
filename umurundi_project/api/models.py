from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

genres = [
    ["Masculin", "Masculin"],
    ["Feminin", "Feminin"]
]

type_lieu_de_naissances = [
    ["Hopital", "Hopital"],
    ["Centre de santé", "Centre de santé"],
    ["À Domicile", "À Domicile"],
]

type_roles = [
    ["IT Manager", "IT Manager"],
    ["IT Technician", "IT Technician"],
    ["Chef de zone", "Chef de zone"],
]

class Admnistrateur(models.Model):
    user = models.OneToOneField(User, to_field="username", on_delete=models.PROTECT) #Lien avec le User par défaut de django
    role = models.CharField(max_length=60, choices=type_roles)

class Umurundi(models.Model):
    admnistrateur = models.ForeignKey("Admnistrateur", on_delete=models.PROTECT)

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
    admnistrateur = models.ForeignKey("Admnistrateur", on_delete=models.PROTECT)

    type_lieu_de_naissance = models.CharField(max_length=30, choices=type_lieu_de_naissances)
    nom = models.CharField(max_length=100, unique=True)
    commune = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    pays = models.CharField(max_length=100)


    def __str__(self):
     return self.type_lieu_de_naissance + " " + self.nom
   
