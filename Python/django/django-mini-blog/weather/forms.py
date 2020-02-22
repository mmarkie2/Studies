from django.forms import ModelForm, TextInput
from .models import City

class CityModelForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}