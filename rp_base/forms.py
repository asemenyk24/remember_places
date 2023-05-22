from django import forms
from .models import Place
from mapwidgets.widgets import GooglePointFieldWidget


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'description', 'location')
        widgets = {
            'location': GooglePointFieldWidget,
        }
