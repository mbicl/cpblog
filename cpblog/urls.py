from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("accounts.urls")),
    path("", include("article.urls")),
    path("problems/", include("problem.urls")),
]
