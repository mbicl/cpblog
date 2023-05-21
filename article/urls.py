from django.urls import path
from .views import (
    ArticlesListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleEditView,
    ArticleDeleteView,
)

urlpatterns = [
    path("", ArticlesListView.as_view(), name="articles_list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/edit/", ArticleEditView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("create/", ArticleCreateView.as_view(), name="article_create"),
]
