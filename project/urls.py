
from django.contrib import admin
from django.urls import path

from apps.user.register import views

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/register_by_email/', views.RegisterByEmailView.as_view(), name='register_by_email'),
    path('api/v1/user_activate/<slug:token>/', views.UserActivateView.as_view(), name="user_activate"),
    path('api/v1/login_by_email/', views.LoginByEmailView.as_view(), name='login_by_email'),
]
