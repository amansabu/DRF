from django.db import models

# Create your models here.

#MOdel Definition
class Movie(models.Model):
    title=models.CharField(max_length=30)
    director=models.CharField(max_length=30)
    language=models.CharField(max_length=30)
    year=models.IntegerField()
    rating=models.FloatField()
    runtime=models.IntegerField()



