from django.forms import ModelForm,ChoiceField,Select
from .models import Appliance

class ApplianceForm(ModelForm):

	class Meta:
		model = Appliance
		fields = ['name','quantity','power_rating']
