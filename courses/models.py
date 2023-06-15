from typing import Iterable, Optional
from django.utils import timezone
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date= models.DateTimeField(default=timezone.now)
    isActive = models.BooleanField()
    slug = models.SlugField(default="",unique=True,db_index=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)

        return super().save(args,kwargs)


class Category(models.Model):
    categoryName = models.CharField(max_length=20)
    slug = models.CharField(max_length=30)