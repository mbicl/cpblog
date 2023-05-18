from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "name", "email")


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "country", "city", "organization"]
