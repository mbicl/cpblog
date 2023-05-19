from django.urls import path
from .views import ArticlesListView, ArticleDetailedView, ArticleCreateView

urlpatterns = [
    path("", ArticlesListView.as_view(), name="articles_list"),
    path("<int:pk>/", ArticleDetailedView.as_view(), name="article_detail"),
    path("create/", ArticleCreateView.as_view(), name="article_create"),
]
