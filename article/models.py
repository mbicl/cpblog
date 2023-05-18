from django.db import models
from accounts.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    reputation = models.IntegerField()
    is_active = models.BooleanField(default=True)
    owner = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)

    def __str__(self) -> str:
        return self.title