# Generated by Django 4.2.1 on 2023-05-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_owner_alter_article_reputation'),
        ('problem', '0004_alter_problem_options_problem_created_time_and_more'),
        ('main', '0003_alter_category_articles_alter_category_problems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='articles',
            field=models.ManyToManyField(to='article.article'),
        ),
        migrations.AlterField(
            model_name='category',
            name='problems',
            field=models.ManyToManyField(to='problem.problem'),
        ),
    ]