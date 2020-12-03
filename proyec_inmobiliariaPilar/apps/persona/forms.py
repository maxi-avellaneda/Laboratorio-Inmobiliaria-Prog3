from django import forms
from django.forms import ModelForm
from .models import PersonaFisica, PersonaJuridica

class PersonaFisicaForm(ModelForm):
    
    class Meta:
        model = PersonaFisica
        exclude = ['desc_per']
        widgets = {
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "apellido": forms.TextInput(attrs={"class":"form-control"}),
            "provincia": forms.TextInput(attrs={"class":"form-control"}),
            "localidad": forms.TextInput(attrs={"class":"form-control"}),
            "barrio": forms.TextInput(attrs={"class":"form-control"}),
            "calle": forms.TextInput(attrs={"class":"form-control"}),
            "numero": forms.NumberInput(attrs={"class":"form-control"}),
            "mail": forms.EmailInput(attrs={"class":"form-control"}),
            "telefono": forms.NumberInput(attrs={"class":"form-control"}),
            "nombre_apellido": forms.TextInput(attrs={"class":"form-control"}),
            "cuil": forms.NumberInput(attrs={"class":"form-control"}),
            "desc_per": forms.TextInput(attrs={"class":"form-control"}),
        }

class PersonaJuridicaForm(ModelForm):

    class Meta:
        model = PersonaJuridica
        exclude = ['desc_per']
        widgets = {
            "provincia": forms.TextInput(attrs={"class":"form-control"}),
            "localidad": forms.TextInput(attrs={"class":"form-control"}),
            "barrio": forms.TextInput(attrs={"class":"form-control"}),
            "calle": forms.TextInput(attrs={"class":"form-control"}),
            "numero": forms.NumberInput(attrs={"class":"form-control"}),
            "mail": forms.EmailInput(attrs={"class":"form-control"}),
            "telefono": forms.NumberInput(attrs={"class":"form-control"}),
            "razon_social": forms.TextInput(attrs={"class":"form-control"}),
            "cuit": forms.NumberInput(attrs={"class":"form-control"}),
            "desc_per": forms.TextInput(attrs={"class":"form-control"}),
        }
    

class FiltrarPersonaForm(forms.Form):
    opc = (
        ('',''),
        ('FISICA', 'Fisica'),
        ('JURIDICA', 'Juridica'),
    )

    tipo = forms.ChoiceField(choices=opc, required=False, widget=forms.Select(attrs={"class":"form-control"}))