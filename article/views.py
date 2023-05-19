from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ArticleCreateForm
from .models import Article


class ArticlesListView(ListView):
    template_name = "articles/articles_list.html"
    model = Article
    context_object_name = "articles"

    def get(self, r):
        return super().get(r)


class ArticleDetailedView(DetailView):
    model = Article
    template_name = "articles/article.html"
    context_object_name = "article"
    fields = "__all__"


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
