# Generated by Django 4.2.1 on 2023-06-12 11:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0004_alter_problem_options_problem_created_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
