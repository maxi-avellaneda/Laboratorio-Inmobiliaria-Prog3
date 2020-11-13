from django.shortcuts import render, HttpResponse
from apps.propiedad.models import Propiedad,PropiedadCasa,PropiedadDepto,PropiedadHabitacion

# Create your views here.

def paginaBuscar(request):
    return render(request,'busqueda/buscar.html')

def buscarPropiedades(request):
    if request.method == 'GET':

        idpro=request.GET["idpro"]
        tipo_propiedad=request.GET["tipo_propiedad"]
        capacidad=request.GET["capacidad"]
        precio1=request.GET["precio1"]
        dormitorios=request.GET["dormitorios"]
        cant_banios=request.GET["cant_banios"]
        zona=request.GET["zona"]
        propiedades = Propiedad.objects.all()

        if idpro != '':
            propiedades = propiedades.filter(id=idpro)
        if tipo_propiedad != 'ninguna':
            propiedades = propiedades.filter(tipo_propiedad__icontains=tipo_propiedad)
        if capacidad != '':
            propiedades = propiedades.filter(capacidad=capacidad)
        if precio1 != '':
            propiedades = propiedades.filter(precio=precio1)
        if dormitorios != '':
            propiedades = propiedades.filter(cant_ambientes=dormitorios)
        if cant_banios != '':
            propiedades = propiedades.filter(cant_banios=cant_banios)
        if zona != '':
            propiedades = propiedades.filter(zona__icontains=zona) 

    return render(request,'busqueda/resultados_busqueda.html',
    {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
    'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})
