# Generated by Django 4.2.2 on 2023-06-16 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]