from django import forms
from django.forms import ModelForm
from .models import PersonaFisica

class PersonaFisicaForm(ModelForm):

    class Meta:
        model = PersonaFisica
        fields = '__all__'
        widgets = {
            "provincia": forms.TextInput(attrs={"class":"form-control"}),
            "localidad": forms.TextInput(attrs={"class":"form-control"}),
            "barrio": forms.TextInput(attrs={"class":"form-control"}),
            "calle": forms.TextInput(attrs={"class":"form-control"}),
            "numero": forms.TextInput(attrs={"class":"form-control"}),
            "mail": forms.TextInput(attrs={"class":"form-control"}),
            "telefono": forms.TextInput(attrs={"class":"form-control"}),
            "nombre_apellido": forms.TextInput(attrs={"class":"form-control"}),
            "cuil": forms.TextInput(attrs={"class":"form-control"}),
            "desc_per": forms.TextInput(attrs={"class":"form-control"}),
        }