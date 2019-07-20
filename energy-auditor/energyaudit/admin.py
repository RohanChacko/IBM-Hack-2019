from django.contrib import admin
from energyaudit.models import Friend, Appliance, MonthlyBill, UserLocation

# Register your models here.
admin.site.register(Appliance)
admin.site.register(MonthlyBill)
admin.site.register(Friend)
admin.site.register(UserLocation)
