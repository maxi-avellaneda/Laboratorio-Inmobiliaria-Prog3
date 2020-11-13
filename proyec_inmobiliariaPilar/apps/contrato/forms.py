from django import forms
from django.forms import ModelForm
from .models import PropietarioPropiedad, InquilinoPropiedad
from apps.persona.models import Persona
from apps.propiedad.models import Propiedad
import datetime

class PropietarioPropiedadForm(forms.ModelForm):
    class Meta:
        model = PropietarioPropiedad
        fields = '__all__'


class InquilinoPropiedadForm(forms.ModelForm):
    class Meta:
        model = InquilinoPropiedad
        fields = '__all__'
        widgets={
            "vigencia_alquiler": forms.NumberInput(attrs={"type":"date", "class":"form-control"}),
            "cant_personas": forms.NumberInput(attrs={"class":"form-control", "placeholder":"Fecha en la que FINALIZA el contrato"}),
            "importe_total": forms.NumberInput(attrs={"class":"form-control", "placeholder":"Fecha en la que FINALIZA el contrato"}),
            "importe_senia": forms.NumberInput(attrs={"class":"form-control", "placeholder":"Fecha en la que FINALIZA el contrato"}),
        }

    def clean_vigencia_alquiler(self):
        vigencia_alquiler = self.cleaned_data['vigencia_alquiler']

        if vigencia_alquiler < datetime.date.today():
            raise forms.ValidationError("No puede ingresar una fecha menor que la actual")

        return vigencia_alquiler

