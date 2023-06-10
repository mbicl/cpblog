from typing import Any, Optional
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Problem
from .forms import ProblemCreateForm

# Create your views here.


class ProblemListView(ListView):
    model = Problem
    context_object_name = "problems"
    template_name = "problems/problem_list.html"


class ProblemDetailView(DetailView):
    model = Problem
    context_object_name = "problem"
    template_name = "problems/problem_detail.html"

    def get_object(self, queryset=None):
        problem = super().get_object(queryset)
        problem.reputation += 1
        problem.save()
        return problem


class ProblemCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("accounts:login")
    model = Problem

    def get(self, r):
        form = ProblemCreateForm
        return render(r, "problems/problem_create.html", {"form": form})

    def post(self, r):
        form = ProblemCreateForm(r.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.owner = self.request.user
            problem.save()
            return redirect("problem:problem_detail", pk=problem.pk)


class ProblemEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Problem
    login_url = reverse_lazy("accounts:login")
    template_name = "problems/problem_edit.html"
    fields = ("title", "url", "description", "difficulty")

    def get_success_url(self) -> str:
        return reverse("problem:problem_detail", kwargs={"pk": self.get_object().pk})

    def test_func(self):
        return self.request.user.username == self.get_object().owner.username


class ProblemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Problem
    template_name = "problems/problem_delete.html"
    login_url = reverse_lazy("accounts:login")
    success_url = reverse_lazy("problem:problems_list")

    def test_func(self):
        return self.request.user.username == self.get_object().owner.username
