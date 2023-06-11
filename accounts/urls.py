from django.urls import path
from .views import (
    Login,
    SignUpView,
    UserProfileView,
    EditUserView,
    LogoutView,
)

app_name = "accounts"

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("register/", SignUpView.as_view(), name="register"),
    path("edit/", EditUserView.as_view(), name="edit_user"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<str:username>/", UserProfileView.as_view(), name="user_profile"),
]
