from django.db import models

# Create your models here.

class Problem(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    reputation = models.IntegerField()
    description = models.TextField()
    difficulty = models.IntegerField()

    def __str__(self) -> str:
        return self.title