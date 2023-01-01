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

class LieuDeNaissanceViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated,]
    queryset = LieuDeNaissance.objects.all()
    serializer_class = LieuDeNaissanceSerializer
