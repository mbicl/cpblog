from django.db import models
from accounts.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor_uploader.fields import RichTextUploadingField
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.


class Problem(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    reputation = models.IntegerField(default=0)
    description = RichTextUploadingField()
    difficulty = models.IntegerField(
        default=1, validators=(MinValueValidator(1), MaxValueValidator(100))
    )
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field="object_pk",
        related_query_name="hit_count_generic_relation",
    )

    class Meta:
        ordering = ["-created_time"]

    def __str__(self) -> str:
        return self.title
