from typing import Any, Optional
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ArticleCreateForm
from .models import Article
from main.models import Category
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)


class ArticlesListView(ListView):
    model = Article
    template_name = "articles/articles_list.html"
    context_object_name = "articles"
    # def get(self, r):
    #     print(r.GET)
    #     categories = Category.objects.filter(name__in=list(r.GET.keys()))
    #     articles = Article.objects.all().filter(categories__in=categories)
    #     print(r.GET.keys())
    #     return render(r, "articles/articles_list.html", {"articles": articles})


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"
    context_object_name = "article"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    model = Article

    def get(self, r):
        form = ArticleCreateForm
        return render(r, "articles/article_create.html", {"form": form})

    def post(self, r):
        form = ArticleCreateForm(r.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = r.user
            article.save()
            return redirect("article_detail", pk=article.pk)


class ArticleEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ("title", "body")
    login_url = reverse_lazy("login")
    template_name = "articles/article_edit.html"

    def get_success_url(self):
        return reverse_lazy("article_detail", kwargs={"pk": self.get_object().pk})

    def test_func(self):
        return self.request.user.username == self.get_object().owner.username


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    login_url = reverse_lazy("login")
    template_name = "articles/article_delete.html"

    def get_success_url(self):
        return reverse_lazy("articles_list")

    def test_func(self):
        return self.request.user.username == self.get_object().owner.username
