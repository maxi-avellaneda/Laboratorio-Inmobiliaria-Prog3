from django.shortcuts import render
from django.http import HttpResponse
from .models import Propiedad,PropiedadCasa,PropiedadDepto,PropiedadHabitacion

# Create your views here.

def ListadoPropiedades(request):
    propiedades= Propiedad.objects.all()
    return render(request,'propiedad/lista_propiedades.html',{'propiedades':propiedades})

def buscarPropiedades(request):
    codpropiedad=request.GET["codpropiedad"]
    tipo_propiedad=request.GET["tipo_propiedad"]
    capacidad=request.GET["capacidad"]
    dormitorio=request.GET["dormitorios"]
    cant_banios=request.GET["cant_banios"]
    zona=request.GET["zona"]
    if request.GET["codpropiedad"]:

        codpropiedad=request.GET["codpropiedad"]
        propiedades=Propiedad.objects.filter(cod_propiedad=codpropiedad)


        return render(request,'propiedad/resultados_busqueda.html',
        {'codpropiedad':codpropiedad,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorio':dormitorio,'cant_banios':cant_banios,'zona':zona})
    

    """
    if request.GET["codpropiedad"] or request.GET["capacidad"] or request.GET["cant_banios"] or request.GET["tipo_propiedad"] or request.GET["dormitorios"] or request.GET["zona"]:
        
        codpropiedad=request.GET["codpropiedad"]
        tipo_propiedad=request.GET["tipo_propiedad"]
        capacidad=request.GET["capacidad"]
        dormitorio=request.GET["dormitorios"]
        cant_banios=request.GET["cant_banios"]
        zona=request.GET["zona"]

        if tipo_propiedad=='casa':
            resultados=PropiedadCasa.objects.filter(capacidad__icontains=capacidad,
            cod_propiedad__icontains=codpropiedad,cant_ambientes__icontains=dormitorio,
            cant_banios__icontains=cant_banios,zona__desc_zona__icontains=zona)

        if tipo_propiedad=='departamento':
            resultados=PropiedadDepto.objects.filter(capacidad__icontains=capacidad,
            cod_propiedad__icontains=codpropiedad,cant_ambientes__icontains=dormitorio,
            cant_banios__icontains=cant_banios,zona__desc_zona__icontains=zona)

        if tipo_propiedad=='ninguna':

            resultados=Propiedad.objects.filter(capacidad__icontains=capacidad,
            cod_propiedad__icontains=codpropiedad,cant_ambientes__icontains=dormitorio,
            cant_banios__icontains=cant_banios,zona__desc_zona__icontains=zona)

        return render(request,'propiedad/resultados_busqueda.html',
        {'codpropiedad':codpropiedad,'capacidad':capacidad,
        'resultados':resultados,'tipo_propiedad':tipo_propiedad,
        'dormitorio':dormitorio,'cant_banios':cant_banios,'zona':zona})
    """
    

    
     