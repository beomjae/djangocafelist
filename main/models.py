from django.db import models
from taggit.managers import TaggableManager

class Cafe(models.Model):
    name = models.CharField(max_length = 50)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    mainphoto = models.ImageField(blank=True, null=True)
    subphoto = models.ImageField(blank=True, null=True)
    content = models.TextField()
    publishedDate = models.DateTimeField(blank=True, null=True)
    modifiedDate = models.DateTimeField(blank=True, null=True)
    tag = TaggableManager(blank=True)
    locate = models.TextField(null=True)
    phone = models.TextField(null=True)
    insta = models.TextField(null=True)

    def __str__(self):
        return self.name
