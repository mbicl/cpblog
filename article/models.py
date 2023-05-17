from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    reputation = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title