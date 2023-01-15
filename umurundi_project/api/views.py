from .models import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import mixins
from . serializers import *


class TokenPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer



class AdministrateurViewSet(
                            mixins.CreateModelMixin, 
                            mixins.ListModelMixin, 
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet
                            ):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated,]
    queryset = Admnistrateur.objects.all()
    serializer_class = AdministrateurSerializer


class UmurundiViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated,]
    queryset = Umurundi.objects.all()
    serializer_class = UmurundiSerializer


    def get_queryset(self, *args, **kwargs):
        administrateur_yatowe = Admnistrateur.objects.get(user=self.request.user)
        list_umurundi = Umurundi.objects.filter(admnistrateur=administrateur_yatowe)
        return list_umurundi


    
    def perform_create(self, serializer):
        administrateur_yatowe = Admnistrateur.objects.get(user=self.request.user)
        serializer.save(admnistrateur=administrateur_yatowe)

        return Response(status=200)

    def perform_update(self, serializer):
        administrateur_yatowe = Admnistrateur.objects.get(user=self.request.user)
        serializer.save(admnistrateur=administrateur_yatowe)

    def destroy(self, request, *args, **kwargs):
        administrateur_yatowe = Admnistrateur.objects.get(user=self.request.user)
        umurundi_id = int(kwargs["pk"])
        Umurundi.objects.get(admnistrateur=administrateur_yatowe, id=umurundi_id).delete()
        
        return Response(data={"success": "Effacé avec succès"}, status=200)

        



class LieuDeNaissanceViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated,]
    queryset = LieuDeNaissance.objects.all()
    serializer_class = LieuDeNaissanceSerializer


    def get_queryset(self, *args, **kwargs):
        administrateur_yatowe = Admnistrateur.objects.get(user=self.request.user)
        list_lieu_de_naissance = LieuDeNaissance.objects.filter(admnistrateur=administrateur_yatowe)
        return list_lieu_de_naissance


    
    def perform_create(self, serializer):
        administrateur_yatowe = Admnistrateur.objects.get(user=self.request.user)
        serializer.save(admnistrateur=administrateur_yatowe)

        return Response(status=200)

    def perform_update(self, serializer):
        administrateur_yatowe = Admnistrateur.objects.get(user=self.request.user)
        serializer.save(admnistrateur=administrateur_yatowe)

    def destroy(self, request, *args, **kwargs):
        administrateur_yatowe = Admnistrateur.objects.get(user=self.request.user)
        lieu_de_naissance_id = int(kwargs["pk"])
        LieuDeNaissance.objects.get(
                                    admnistrateur=administrateur_yatowe, 
                                    id=lieu_de_naissance_id
                                    ).delete()
        
        return Response(data={"success": "Effacé avec succès"}, status=200)
