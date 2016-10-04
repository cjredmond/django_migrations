from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=2)
    country = models.CharField(max_length=20)
    rating = models.IntegerField()
    age = models.IntegerField()
