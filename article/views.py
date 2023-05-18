from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

class ArticlesListView(ListView):
    template_name = 'articles/articles_list.html'
    model = Article