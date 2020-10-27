from django.shortcuts import render
from django.http import HttpResponse
from .models import Propiedad

# Create your views here.

def ListadoPropiedades(request):
    propiedades= Propiedad.objects.all()
    return render(request,'propiedad/lista_propiedades.html',{'propiedades':propiedades})

def buscarPropiedades(request):
    if request.GET["palclave"] or request.GET["capacidad"]:
        
        pclave=request.GET["palclave"]
        capacidad=request.GET["capacidad"]
        codprop=Propiedad.objects.filter(cod_propiedad__icontains=pclave)
        capacpro=Propiedad.objects.filter(capacidad__icontains=capacidad,cod_propiedad__icontains=pclave)
        return render(request,'propiedad/resultados_busqueda.html',{'codprop':codprop,
        'query':pclave,'capacidad':capacidad,'capacpro':capacpro})

    else:
        mensaje="No introdujo nada" 

    return HttpResponse(mensaje)

    
     