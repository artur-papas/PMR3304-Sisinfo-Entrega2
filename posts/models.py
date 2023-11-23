from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField(max_length=200, null=True)

    def __str__(self):
        return f'{self.title} ({self.publish_date})'

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return f'{self.name}'
# Create your models here.
