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
        (0, '0 Star'),
        (1, '1 Star'),
        (2, '2 Star'),
        (3, '3 Star'),
        (4, '4 Star'),
        (5, '5 Star'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Appliance", max_length=60, choices=APPLIANCES)
    quantity = models.PositiveIntegerField(default=1)
    power_rating = models.PositiveIntegerField(choices=RATING)


class MonthlyBill(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    month_year = models.DateField()
    bill_amount = models.IntegerField()
    power_consumed = models.FloatField()
