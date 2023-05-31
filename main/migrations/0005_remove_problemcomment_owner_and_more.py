# Generated by Django 4.2.1 on 2023-05-25 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_category_articles_alter_category_problems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problemcomment',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='problemcomment',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='category',
            name='articles',
        ),
        migrations.RemoveField(
            model_name='category',
            name='problems',
        ),
        migrations.DeleteModel(
            name='ArticleComment',
        ),
        migrations.DeleteModel(
            name='ProblemComment',
        ),
    ]
