from django.db import models
from accounts.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Problem(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    reputation = models.IntegerField(default=0)
    description = models.TextField()
    difficulty = models.IntegerField(
        default=1, validators=(MinValueValidator(1), MaxValueValidator(100))
    )
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self) -> str:
        return self.title
