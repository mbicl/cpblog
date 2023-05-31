from django.db import models

# from problem.models import Problem
# from article.models import Article
# from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


# class ArticleComment(models.Model):
#     body = models.TextField()
#     reputation = models.IntegerField()
#     is_active = models.BooleanField(default=True)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return " ".join(self.body.split()[:3])


# class ProblemComment(models.Model):
#     body = models.TextField()
#     reputation = models.IntegerField()
#     is_active = models.BooleanField(default=True)
#     problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return " ".join(self.body.split()[:3])
