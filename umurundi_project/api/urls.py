from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from . views import *

router = routers.DefaultRouter()

router.register("umurundi", UmurundiViewSet)
router.register("administrateur", AdministrateurViewSet)
router.register("lieu-de-naissance", LieuDeNaissanceViewSet)


urlpatterns = [
    path("", include(router.urls)), # Pour rendre les URLS de django rest framework à django
    path("login/", TokenPairView.as_view()),
    path("auth/", include("rest_framework.urls")),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token-refresh")
]