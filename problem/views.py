from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class ProblemCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
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
            return redirect("problem_detail", pk=problem.pk)


class ProblemEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Problem
    login_url = reverse_lazy("login")
    template_name = "problems/problem_edit.html"
    fields = ("title", "url", "description", "difficulty")

    def get_success_url(self) -> str:
        return reverse("problem_detail", kwargs={"pk": self.get_object().pk})

    def test_func(self):
        return self.request.user.username == self.get_object().owner.username


class ProblemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Problem
    template_name = "problems/problem_delete.html"
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("problems_list")

    def test_func(self):
        return self.request.user.username == self.get_object().owner.username
