from django.contrib import admin
from .models import Comment, Category

# Register your models here.

admin.site.register(Comment)
admin.site.register(Category)