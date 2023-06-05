from django.forms import ModelForm
from .models import Article


class ArticleCreateForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body", "categories"]
