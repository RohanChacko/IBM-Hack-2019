from django.contrib import admin
from energyaudit.models import Friend, Appliance, MonthlyBill, UserLocation, DisaggregationResults

# Register your models here.
admin.site.register(Appliance)
admin.site.register(MonthlyBill)
admin.site.register(Friend)
admin.site.register(UserLocation)
admin.site.register(DisaggregationResults)
