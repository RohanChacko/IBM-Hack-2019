from django.db import models
from django.contrib.auth.models import User
# Create your models here
class Appliance(models.Model):
    APPLIANCES = (
        ('fridge', 'Fridge'),
        ('air conditioner', 'Air Conditioner'),
        ('washing machine', 'Washing Machine'),
    )
    RATING = (
        (1, '1 Star'),
        (2, '2 Star'),
        (3, '3 Star'),
        (4, '4 Star'),
        (5, '5 Star'),
        (6, '6 Star'),
    )
    

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Appliance",max_length=60, choices=APPLIANCES)
    quantity = models.IntegerField()
    power_rating = models.IntegerField(choices = RATING)
