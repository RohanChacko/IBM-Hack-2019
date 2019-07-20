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
    quantity = models.PositiveIntegerField()
    power_rating = models.PositiveIntegerField(choices=RATING)


class MonthlyBill(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    month_year = models.DateField()
    bill_amount = models.PositiveIntegerField()
    power_consumed = models.FloatField()


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)


class UserLocation(models.Model):

    HOUSE_TYPE = (
        ('apartment', 'Apartment'),
        ('villa', 'Villa'),
        ('bungalow', 'Bungalow'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    building = models.CharField("Building", max_length=60)
    street = models.CharField("Street Address", max_length=60)
    city = models.CharField("City", max_length=60)
    state = models.CharField("State", max_length=60)
    house_type = models.CharField(
        "House Type", max_length=60, choices=HOUSE_TYPE, default='Apartment')
    pincode = models.PositiveIntegerField()

    num_room = models.PositiveIntegerField("Number of Rooms")
    area = models.PositiveIntegerField("Area (Square Feet)")


class DisaggregationResults(models.Model):
    total_aggregate = models.FloatField()
    fridge = models.FloatField()
    ac = models.FloatField()
    washing_machine = models.FloatField()
