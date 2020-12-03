from django import forms
from django.forms import ModelForm
from .models import PropietarioPropiedad, InquilinoPropiedad
from apps.persona.models import Persona
from apps.propiedad.models import Propiedad
import datetime

class PropietarioPropiedadForm(forms.ModelForm):
    class Meta:
        model = PropietarioPropiedad
        exclude = ['cancelacion', 'fecha_cancelacion']
        widgets={
            "propiedad": forms.Select(attrs={"class":"form-control", "placeholder":"Seleccione una propiedad"}),
            "propietario": forms.Select(attrs={"class":"form-control"}),
            "fecha_inicio": forms.NumberInput(attrs={"type":"date", "class":"form-control"}),
            "fecha_fin": forms.NumberInput(attrs={"type":"date", "class":"form-control"}),
            "comision": forms.Select(attrs={"class":"form-control", "placeholder":"Importe total"}),
        }


class InquilinoPropiedadForm(forms.ModelForm):
    class Meta:
        model = InquilinoPropiedad
        exclude = ['cancelacion', 'fecha_cancelacion']
        widgets={
            "propiedad": forms.Select(attrs={"class":"form-control", "placeholder":"Seleccione una propiedad"}),
            "inquilino": forms.Select(attrs={"class":"form-control"}),
            "fecha_inicio": forms.NumberInput(attrs={"type":"date", "class":"form-control"}),
            "fecha_fin": forms.NumberInput(attrs={"type":"date", "class":"form-control"}),
            "cant_personas": forms.NumberInput(attrs={"class":"form-control", "placeholder":"Cantidad de personas que habitaran la propiedad"}),
            "importe_total": forms.NumberInput(attrs={"class":"form-control", "placeholder":"Importe total"}),
            "importe_senia": forms.NumberInput(attrs={"class":"form-control", "placeholder":"Fecha en la que FINALIZA el contrato"}),
        }

    def clean_fecha_inicio(self):
        fecha_inicio = self.cleaned_data['fecha_inicio']

        if fecha_inicio < datetime.date.today():
            raise forms.ValidationError("No puede ingresar una fecha menor que la actual")

        return fecha_inicio

    def clean_fecha_fin(self):
        fecha_fin = self.cleaned_data['fecha_fin']

        if fecha_fin < datetime.date.today():
            raise forms.ValidationError("No puede ingresar una fecha menor que la actual")

        return fecha_fin

