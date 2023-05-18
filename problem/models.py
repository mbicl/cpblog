from django.db import models
from accounts.models import User
# Create your models here.

class Problem(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    reputation = models.IntegerField()
    description = models.TextField()
    difficulty = models.IntegerField()
    is_active = models.BooleanField(default=True)
    owner = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)

    def __str__(self) -> str:
        return self.title