from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserEditForm
from .models import User


class Login(LoginView):
    template_name = "registration/login.html"

    def get_success_url(self):
        if self.request.GET.get("next"):
            return self.request.GET.get("next")
        return reverse_lazy("articles_list")

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


class SignUpView(CreateView):
    form_class = UserRegistrationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class UserProfileView(CreateView):
    model = User

    def get(self, r, username) -> HttpResponse:
        user = self.model.objects.get(username=username)
        return render(r, "registration/profile.html", {"user": user})


class EditUserView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")

    def get(self, r):
        form = UserEditForm(instance=r.user)
        return render(r, "registration/edit_user.html", {"form": form})

    def post(self, r):
        user_form = UserEditForm(instance=r.user, data=r.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("user_profile")


class LogoutView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")

    def get(self, r):
        logout(request=r)
        return redirect("articles_list")
