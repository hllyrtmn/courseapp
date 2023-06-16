from typing import Iterable, Optional
from django.utils import timezone
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    categoryName = models.CharField(max_length=20)
    slug = models.SlugField(max_length=30,null=False,unique=True,db_index=True)


    def __str__(self) -> str:
        return f"{self.categoryName}"



class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date= models.DateTimeField(auto_now=True)
    isActive = models.BooleanField()
    slug = models.SlugField(default="",unique=True,db_index=True,blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}"


