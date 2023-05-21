from django.forms import ModelForm
from .models import Problem


class ProblemCreateForm(ModelForm):
    class Meta:
        model = Problem
        fields = ("title", "url", "description", "difficulty")
