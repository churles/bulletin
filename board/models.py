from django.db import models
from django.urls import re_path as url
# Create your models here.

app_name = 'boards'


class Article(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.content

    def snippet(self):
        return self.content[:50]       
