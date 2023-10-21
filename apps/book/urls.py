from django.urls import path, include
from rest_framework import routers

from . import views as views


router = routers.SimpleRouter()

router.register(r'book', views.BookViewSet, basename="book")

urlpatterns = [
    path('', include(router.urls)),
]
