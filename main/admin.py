from django.contrib import admin
from .models import ArticleComment, ProblemComment, Category

# Register your models here.

admin.site.register(ArticleComment)
admin.site.register(ProblemComment)
admin.site.register(Category)