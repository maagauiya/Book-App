from django.urls import path, include
from rest_framework import routers

from . import views as views


router = routers.SimpleRouter()

router.register(r'genre', views.GenreViewSet, basename="genre")

urlpatterns = [
    path('', include(router.urls)),
]
