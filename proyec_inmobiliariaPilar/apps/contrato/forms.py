from django import forms
from django.forms import ModelForm
from .models import PropietarioPropiedad, InquilinoPropiedad

class PropietarioPropiedadForm(forms.ModelForm):
    class Meta:
        model = PropietarioPropiedad
        fields = '__all__'

class InquilinoPropiedadForm(forms.ModelForm):
    class Meta:
        model = InquilinoPropiedad
        fields = '__all__'

