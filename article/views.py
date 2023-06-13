from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ArticleCreateForm
from .models import Article
from hitcount.views import HitCountDetailView
from django.views import View
from django.views.generic import (
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)


class ArticlesListView(View):
    def get(self, request):
        articles = Article.objects.all()
        category = request.GET.get("category")
        # print(category)
        if category:
            category = list(category.split(","))
            for i in category:
                articles = articles.filter(categories__name=i)
        return render(request, "articles/articles_list.html", {"articles": articles})


class ArticleDetailView(UpdateView, HitCountDetailView):
    model = Article
    template_name = "articles/article_detail.html"
    context_object_name = "article"
    fields = ["reputation"]
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == "POST":
            print(self.request.POST)
            plus = self.request.POST.get("plus")
            minus = self.request.POST.get("minus")
            if minus:
                article = self.get_object()
                article.reputation -= 1
                # article.owner.reputation -= 1
                article.save()
            if plus:
                article = self.get_object()
                article.reputation += 1
                # article.owner.reputation += 1
                article.save()

        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("accounts:login")
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
            return redirect("article:article_detail", pk=article.pk)


class ArticleEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ("title", "body")
    login_url = reverse_lazy("accounts:login")
    template_name = "articles/article_edit.html"

    def get_success_url(self):
        return reverse_lazy(
            "article:article_detail", kwargs={"pk": self.get_object().pk}
        )

    def test_func(self):
        return (
            self.request.user.username == self.get_object().owner.username
            or self.request.user.is_superuser
        )


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    login_url = reverse_lazy("accounts:login")
    template_name = "articles/article_delete.html"

    def get_success_url(self):
        return reverse_lazy("article:articles_list")

    def test_func(self):
        return (
            self.request.user.username == self.get_object().owner.username
            or self.request.user.is_superuser
        )
