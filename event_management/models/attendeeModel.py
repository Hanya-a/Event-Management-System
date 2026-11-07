from django.db import models
from django.contrib.auth.models import User

class Attendee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="attendee")
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    birthday = models.DateField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)