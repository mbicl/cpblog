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
from hitcount.views import HitCountDetailView
from .models import Problem
from .forms import ProblemCreateForm

# Create your views here.


class ProblemListView(ListView):
    model = Problem
    context_object_name = "problems"
    template_name = "problems/problem_list.html"


class ProblemDetailView(UpdateView, HitCountDetailView):
    model = Problem
    context_object_name = "problem"
    template_name = "problems/problem_detail.html"
    fields = ["reputation"]
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == "POST":
            print(self.request.POST)
            plus = self.request.POST.get("plus")
            minus = self.request.POST.get("minus")
            if minus:
                problem = self.get_object()
                problem.reputation -= 1
                # problem.owner.reputation -= 1
                problem.save()
            if plus:
                problem = self.get_object()
                problem.reputation += 1
                # problem.owner.reputation += 1
                problem.save()
        return context


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
        return (
            self.request.user.username == self.get_object().owner.username
            or self.request.user.is_superuser
        )


class ProblemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Problem
    template_name = "problems/problem_delete.html"
    login_url = reverse_lazy("accounts:login")
    success_url = reverse_lazy("problem:problems_list")

    def test_func(self):
        return (
            self.request.user.username == self.get_object().owner.username
            or self.request.user.is_superuser
        )
