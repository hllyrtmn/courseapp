# Generated by Django 4.2.2 on 2023-06-15 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_delete_coursecategory_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
