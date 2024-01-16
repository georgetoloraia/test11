# blog/models.py
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    text_color = models.CharField(max_length=7)
    background_color = models.CharField(max_length=7)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    publish_date = models.DateTimeField()
    categories = models.ManyToManyField(Category)
    author = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.title
