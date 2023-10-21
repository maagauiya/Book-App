from django.urls import path, include
from rest_framework import routers

from . import views as views


router = routers.SimpleRouter()

router.register(r'review', views.ReviewViewSet, basename="review")

urlpatterns = [
    path('', include(router.urls)),
]
