from django.shortcuts import render
from django.http import HttpResponse
from .models import Propiedad
from .forms import PropiedadCasaForm,PropiedadDptoForm,PropiedadHabitacionForm

# Create your views here.

def ListadoPropiedades(request):
    propiedades= Propiedad.objects.all()
    return render(request,'propiedad/lista_propiedades.html',{'propiedades':propiedades})

def buscarPropiedades(request):
    if request.GET["palclave"]:

        mensaje="Se busco : %r" %request.GET["palclave"] 
        pclave=request.GET["palclave"]
        propiedades=Propiedad.objects.filter(cod_propiedad__icontains=pclave)
        return render(request,'propiedad/resultados_busqueda.html',{'propiedades':propiedades,'query':pclave})

    else:
        mensaje="No introdujo nada" 

    return HttpResponse(mensaje)

def NuevaPropiedadCasa(request):
    data = {
        "form" : PropiedadCasaForm()
    }
    if request.method == 'POST':
        formulario = PropiedadCasaForm(request.POST)
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
