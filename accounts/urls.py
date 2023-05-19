from django.urls import path
from .views import (
    Login,
    SignUpView,
    UserProfileView,
    EditUserView,
    LogoutView,
)

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("register/", SignUpView.as_view(), name="signup"),
    path("edit/", EditUserView.as_view(), name="edit_user"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<str:username>/", UserProfileView.as_view(), name="user_profile"),
]
