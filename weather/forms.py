from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
	class Meta:
		model = City
		field = ['name']
		widgets = {'name': TextInput(attrs = {'class' : 'input', 'placeholder' : 'City Name'})}
		exclude = ()