from django.db import models
from accounts.models import User
from main.models import Category
from ckeditor_uploader.fields import RichTextUploadingField
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField()
    reputation = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field="object_pk",
        related_query_name="hit_count_generic_relation",
    )
    # plus_users = models.ManyToManyField(User)
    # minus_users = models.ManyToManyField(User)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self) -> str:
        return self.title
