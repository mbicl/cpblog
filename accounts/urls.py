from django.urls import path
from .views import Login, SignUpView

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("register/", SignUpView.as_view(), name="signup"),
]
