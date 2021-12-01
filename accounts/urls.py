from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import(
    Register
)

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
]
