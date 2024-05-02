from django.db import models

# Create your models here.


class VoyageEvent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='voyage_events/')
