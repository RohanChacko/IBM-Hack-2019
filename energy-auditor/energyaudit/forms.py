from django.forms import ModelForm, SelectDateWidget, Select
from .models import Appliance, MonthlyBill


class ApplianceForm(ModelForm):

    class Meta:
        model = Appliance
        fields = ['name', 'quantity', 'power_rating']


class MonthlyBillForm(ModelForm):

    class Meta:
        model = MonthlyBill
        exclude = ('owner',)
        widgets = {
            'month_year': SelectDateWidget(years=['2018', '2019']),
        }
