from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField(max_length=200, null=True)

    def __str__(self):
        return f'{self.Title} ({self.publish_date})'
# Create your models here.
