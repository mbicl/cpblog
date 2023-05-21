# Generated by Django 4.2.1 on 2023-05-21 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problem', '0002_alter_problem_difficulty_alter_problem_reputation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
