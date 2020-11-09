from django import forms
from django.forms import ModelForm
from .models import PropiedadCasa, PropiedadDepto, PropiedadHabitacion, Oferta, Estado

class PropiedadCasaForm(ModelForm):
    class Meta:
        model = PropiedadCasa
        exclude = ['tipo_propiedad',]
        widgets = {
            "mts": forms.NumberInput(attrs={"class":"form-control","placeholder":"Metros de la propiedad"}),
            "mts_semicubiertos": forms.NumberInput(attrs={"class":"form-control","placeholder":"Metros Semi-Cubiertos de la propiedad"}),
            "capacidad": forms.NumberInput(attrs={"class":"form-control","placeholder":"Numero maximo de personas que pueden vivir en la propiedad"}),
            "cant_ambientes": forms.NumberInput(attrs={"class":"form-control","placeholder":"Cantidad de ambientes de la propiedad"}),
            "cochera": forms.CheckboxInput(attrs={"class":"form-check-input", "onclick":"mostrar()"}),
            "capacidad_cochera": forms.NumberInput(attrs={"class":"form-control","placeholder":"Cantidad de coches que entran en la cochera"}),
            "cant_banios": forms.NumberInput(attrs={"class":"form-control","placeholder":"Cantidad de baños"}),
            #"tipo_propiedad": forms.TextInput(attrs={"class":"form-control"}),
            "desc_prop": forms.Textarea(attrs={"class":"form-control", "rows":"4","placeholder":"Descripcion completa de la propiedad"}),
            "precio" : forms.NumberInput(attrs={"class":"form-control","placeholder":"Precio con el que se publicara la propiedad"})
        }
        labels = {
            "mts" : "Metros:",
            "mts_semicubiertos": "Metros Semi-Cubiertos:", 
            "capacidad": "Capacidad:",
            "cant_ambientes": "Cantidad de ambientes:",
            "cochera": "¿Dispone de cochera?",
            "capacidad_cochera": "Capacidad de cochera:",
            "cant_banios": "Cantidad de baños:",
            "permite_cancelacion" : "¿Permite cancelacion?",
            "tipo_alquiler" : "Forma de alquiler:",
            "precio" : "Precio de la propiedad",
            "desc_prop" : "Descripcion de la propiedad:",
            "imagen" : "Imagen de la propiedad:",
            "estado" : "En que estado se encuentra la propiedad:",
            "zona" : "¿En que zona esta ubicada la propiedad?",
        }

class PropiedadDptoForm(ModelForm):
    class Meta:
        model = PropiedadDepto
        exclude = ['tipo_propiedad',]
        widgets = {
            "mts": forms.NumberInput(attrs={"class":"form-control","placeholder":"Metros de la propiedad"}),
            "mts_semicubiertos": forms.NumberInput(attrs={"class":"form-control","placeholder":"Metros Semi-Cubiertos de la propiedad"}),
            "capacidad": forms.NumberInput(attrs={"class":"form-control","placeholder":"Numero maximo de personas que pueden vivir en la propiedad"}),
            "cant_ambientes": forms.NumberInput(attrs={"class":"form-control","placeholder":"Cantidad de ambientes de la propiedad"}),
            "cochera": forms.CheckboxInput(attrs={"class":"form-check-input", "onclick":"mostrar()"}),
            "capacidad_cochera": forms.NumberInput(attrs={"class":"form-control","placeholder":"Cantidad de coches que entran en la cochera"}),
            "cant_banios": forms.NumberInput(attrs={"class":"form-control","placeholder":"Cantidad de baños"}),
            #"tipo_propiedad": forms.TextInput(attrs={"class":"form-control"}),
            "desc_prop": forms.Textarea(attrs={"class":"form-control", "rows":"4","placeholder":"Descripcion completa de la propiedad"}),
            "precio" : forms.NumberInput(attrs={"class":"form-control","placeholder":"Precio con el que se publicara la propiedad"})
        }
        labels = {
            "mts" : "Metros:",
            "mts_semicubiertos": "Metros Semi-Cubiertos:", 
            "capacidad": "Capacidad:",
            "cant_ambientes": "Cantidad de ambientes:",
            "cochera": "¿Dispone de cochera?",
            "capacidad_cochera": "Capacidad de cochera:",
            "cant_banios": "Cantidad de baños:",
            "permite_cancelacion" : "¿Permite cancelacion?",
            "tipo_alquiler" : "Forma de alquiler:",
            "precio" : "Precio de la propiedad",
            "desc_prop" : "Descripcion de la propiedad:",
            "imagen" : "Imagen de la propiedad:",
            "estado" : "En que estado se encuentra la propiedad:",
            "zona" : "¿En que zona esta ubicada la propiedad?",
        }

class PropiedadHabitacionForm(ModelForm):
    class Meta:
        model = PropiedadHabitacion
        exclude = ['tipo_propiedad',]
        widgets = {
            "mts": forms.NumberInput(attrs={"class":"form-control","placeholder":"Metros de la propiedad"}),
            "mts_semicubiertos": forms.NumberInput(attrs={"class":"form-control","placeholder":"Metros Semi-Cubiertos de la propiedad"}),
            "capacidad": forms.NumberInput(attrs={"class":"form-control","placeholder":"Numero maximo de personas que pueden vivir en la propiedad"}),
            "cant_ambientes": forms.NumberInput(attrs={"class":"form-control","placeholder":"Cantidad de ambientes de la propiedad"}),
            "cochera": forms.CheckboxInput(attrs={"class":"form-check-input", "onclick":"mostrar()"}),
            "capacidad_cochera": forms.NumberInput(attrs={"class":"form-control","placeholder":"Cantidad de coches que entran en la cochera"}),
            "cant_banios": forms.NumberInput(attrs={"class":"form-control","placeholder":"Cantidad de baños"}),
            #"tipo_propiedad": forms.TextInput(attrs={"class":"form-control"}),
            "desc_prop": forms.Textarea(attrs={"class":"form-control", "rows":"4","placeholder":"Descripcion completa de la propiedad"}),
            "precio" : forms.NumberInput(attrs={"class":"form-control","placeholder":"Precio con el que se publicara la propiedad"})
        }
        labels = {
            "mts" : "Metros:",
            "mts_semicubiertos": "Metros Semi-Cubiertos:", 
            "capacidad": "Capacidad:",
            "cant_ambientes": "Cantidad de ambientes:",
            "cochera": "¿Dispone de cochera?",
            "capacidad_cochera": "Capacidad de cochera:",
            "cant_banios": "Cantidad de baños:",
            "permite_cancelacion" : "¿Permite cancelacion?",
            "tipo_alquiler" : "Forma de alquiler:",
            "precio" : "Precio de la propiedad",
            "desc_prop" : "Descripcion de la propiedad:",
            "imagen" : "Imagen de la propiedad:",
            "estado" : "En que estado se encuentra la propiedad:",
            "zona" : "¿En que zona esta ubicada la propiedad?",
        }

class OfertaForm(ModelForm):
    class Meta:
        model= Oferta
        exclude=['fecha_solicitud', 'fecha_inicio']
        widgets = {
            "propiedad": forms.Select(attrs={"class":"form-control"}),
            "cod_oferta": forms.TextInput(attrs={"class":"form-control"}),
            "fecha_fin": forms.NumberInput(attrs={"type":"date", "class":"form-control"})
        }

class EstadoForm(ModelForm):
    class Meta:
        model = Estado
        exclude = ['fec_inicio',]