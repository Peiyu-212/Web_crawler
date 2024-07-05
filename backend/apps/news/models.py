from django.db import models
from django.db.models.functions import Now

# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    filepath = models.ImageField(upload_to='images/')


class News(models.Model):
    content = models.TextField(null=False)
    news_time = models.DateTimeField(null=False)
    authority = models.CharField(null=False, max_length=200)
    created_time = models.DateTimeField(db_default=Now())
    title = models.CharField(null=False, max_length=300)
    photo = models.ForeignKey('Image', related_name='news_photo', on_delete=models.CASCADE)
