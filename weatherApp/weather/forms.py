from django.forms import ModelForm, TextInput
from .models import City
# to allow the user to add a city directly in the form instead of pulling from the DB only
class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder
