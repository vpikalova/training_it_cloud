from django.db import models

# Create your models here.

class Quadratic(models.Model):
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()