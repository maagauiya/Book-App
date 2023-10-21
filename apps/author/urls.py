from django.urls import path, include
from rest_framework import routers

from . import views as views


router = routers.SimpleRouter()

router.register(r'author', views.AuthorViewSet, basename="author")

urlpatterns = [
    path('', include(router.urls)),
]
