from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField()
    cover = models.ImageField()
    description = models.TextField()
    