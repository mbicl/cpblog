from django.db import models
from accounts.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    reputation = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self) -> str:
        return self.title
