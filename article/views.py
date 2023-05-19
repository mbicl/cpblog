from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from django.shortcuts import render, redirect
from .forms import ArticleCreateForm


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


class ArticleCreateView(CreateView):
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
