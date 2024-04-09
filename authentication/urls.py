from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path("", views.getRoutes),
    path("signup/", views.UserCreateView.as_view(), name="signup")
]
