from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.validators import UnicodeUsernameValidator
from . models import *


class TokenPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(TokenPairSerializer, self).validate(attrs)
        data["groups"] = [
            {"id": group.id, "name": group.name}
            for group in self.user.groups.all()
        ]
        data["is_superuser"] = self.user.is_superuser
        data["id"] = self.user.id
        data["username"] = self.user.username
        data["first_name"] = self.user.first_name
        data["last_name"] = self.user.last_name
        return data




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )
        extra_kwargs = {
            "username": {"validators": [UnicodeUsernameValidator()]},
            "password": {"write_only": True},
        }


class AdministrateurSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user"] = UserSerializer(instance.user, many=False).data
        return representation
    class Meta:
        model = Admnistrateur
        fields = "__all__"


class UmurundiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Umurundi
        fields =  [
            "id", "nom", "prenom", "sexe", "date_naissance", 
            "cni_pere", "cni_mere", "lieu_de_naissance"
        ]


class LieuDeNaissanceSerializer(serializers.ModelSerializer):

   
    class Meta:
        model = LieuDeNaissance
        fields = [
            "type_lieu_de_naissance", "nom", "commune",
            "province", "pays"
        ]