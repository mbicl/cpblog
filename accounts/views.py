from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegistrationForm


class Login(LoginView):
    template_name = "registration/login.html"

    def get_success_url(self):
        return reverse_lazy("articles_list")

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


class SignUpView(CreateView):
    form_class = UserRegistrationForm
    template_name = "registration/signup.html"

    def get_success_url(self):
        return reverse_lazy("login")
