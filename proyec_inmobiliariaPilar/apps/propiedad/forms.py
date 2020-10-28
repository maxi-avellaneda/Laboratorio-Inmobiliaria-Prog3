from django import forms
from django.forms import ModelForm
from .models import PropiedadCasa, PropiedadDepto, PropiedadHabitacion

class PropiedadCasaForm(ModelForm):
    class Meta:
        model = PropiedadCasa
        fields = '__all__'
        widgets = {
            "mts": forms.NumberInput(attrs={"class":"form-control"}),
            "mts_semicubiertos": forms.NumberInput(attrs={"class":"form-control"}),
            "capacidad": forms.NumberInput(attrs={"class":"form-control"}),
            "cant_ambientes": forms.NumberInput(attrs={"class":"form-control"}),
            #"numero": forms.NumberInput(attrs={"class":"form-control"}),
            "capacidad_cochera": forms.NumberInput(attrs={"class":"form-control"}),
            "cant_banios": forms.NumberInput(attrs={"class":"form-control"}),
            "tipo_propiedad": forms.TextInput(attrs={"class":"form-control"}),
        }

class PropiedadDptoForm(ModelForm):
    class Meta:
        model = PropiedadDepto
        fields = '__all__'
        widgets = {
            "mts": forms.NumberInput(attrs={"class":"form-control"}),
            "mts_semicubiertos": forms.NumberInput(attrs={"class":"form-control"}),
            "capacidad": forms.NumberInput(attrs={"class":"form-control"}),
            "cant_ambientes": forms.NumberInput(attrs={"class":"form-control"}),
            #"numero": forms.NumberInput(attrs={"class":"form-control"}),
            "capacidad_cochera": forms.NumberInput(attrs={"class":"form-control"}),
            "cant_banios": forms.NumberInput(attrs={"class":"form-control"}),
            "tipo_propiedad": forms.TextInput(attrs={"class":"form-control"}),
        }

class PropiedadHabitacionForm(ModelForm):
    class Meta:
        model = PropiedadHabitacion
        fields = '__all__'
        widgets = {
            "mts": forms.NumberInput(attrs={"class":"form-control"}),
            "mts_semicubiertos": forms.NumberInput(attrs={"class":"form-control"}),
            "capacidad": forms.NumberInput(attrs={"class":"form-control"}),
            "cant_ambientes": forms.NumberInput(attrs={"class":"form-control"}),
            #"numero": forms.NumberInput(attrs={"class":"form-control"}),
            "capacidad_cochera": forms.NumberInput(attrs={"class":"form-control"}),
            "cant_banios": forms.NumberInput(attrs={"class":"form-control"}),
            "tipo_propiedad": forms.TextInput(attrs={"class":"form-control"}),
        }

