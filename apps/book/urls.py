from django.urls import path, include
from rest_framework import routers

from . import views as views
from . import actions as actions


router = routers.SimpleRouter()

router.register(r'book', views.BookViewSet, basename="book")

urlpatterns = [
    path('', include(router.urls)),
    path('my-bookmark/', views.my_bookmark, name='my_bookmark'),  # SEO Friendly
    path('bookmark/<int:pk>/do/<slug:action>/', actions.BookMarkActionHandler.as_view(), name="add_to_bookmark"),

]
