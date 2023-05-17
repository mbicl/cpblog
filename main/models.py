from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    body = models.TextField()
    reputation = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return " ".join(self.body.split()[:3])