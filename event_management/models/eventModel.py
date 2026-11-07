from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)