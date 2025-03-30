from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import login_user, register, logout

urlpatterns = [
    # path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", login_user, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
]
