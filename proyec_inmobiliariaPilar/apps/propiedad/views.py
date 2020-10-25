from django.shortcuts import render
from django.http import HttpResponse
from .models import Propiedad

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
     