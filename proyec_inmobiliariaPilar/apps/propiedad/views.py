from django.shortcuts import render
from django.http import HttpResponse
from .models import Propiedad
from .forms import PropiedadCasaForm,PropiedadDptoForm,PropiedadHabitacionForm

# Create your views here.

def ListadoPropiedades(request):
    propiedades= Propiedad.objects.all()
    return render(request,'propiedad/lista_propiedades.html',{'propiedades':propiedades})


def NuevaPropiedadCasa(request):
    data = {
        "form" : PropiedadCasaForm()
    }
    if request.method == 'POST':
        formulario = PropiedadCasaForm(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = 'guardado con exito'

    return render(request, 'propiedad/nueva_propiedad.html', data )

def NuevaPropiedadDpto(request):
    data = {
        "form" : PropiedadDptoForm()
    }
    if request.method == 'POST':
        formulario = PropiedadDptoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = 'guardado con exito'

    return render(request, 'propiedad/nueva_propiedad.html', data )

def NuevaPropiedadHabitacion(request):
    data = {
        "form" : PropiedadHabitacionForm()
    }
    if request.method == 'POST':
        formulario = PropiedadHabitacionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = 'guardado con exito'

    return render(request, 'propiedad/nueva_propiedad.html', data )
