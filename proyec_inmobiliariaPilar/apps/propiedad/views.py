from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Propiedad, PropiedadCasa, PropiedadDepto, PropiedadHabitacion
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
        print(request.POST)
        f = PropiedadCasaForm(request.POST,request.FILES)
        if f.is_valid():
            form = f.save(commit=False)
            form.tipo_propiedad='casa'
            form.save()
            data["mensaje"] = 'guardado con exito'

    return render(request, 'propiedad/nueva_propiedad.html', data )

def NuevaPropiedadDpto(request):
    data = {
        "form" : PropiedadDptoForm()
    }
    if request.method == 'POST':
        f = PropiedadDptoForm(request.POST,request.FILES)
        if f.is_valid():
            form = f.save(commit=False)
            form.tipo_propiedad='departamento'
            form.save()
            data["mensaje"] = 'guardado con exito'

    return render(request, 'propiedad/nueva_propiedad.html', data )

def NuevaPropiedadHabitacion(request):
    data = {
        "form" : PropiedadHabitacionForm()
    }
    if request.method == 'POST':
        f = PropiedadHabitacionForm(request.POST,request.FILES)
        if f.is_valid():
            form = f.save(commit=False)
            form.tipo_propiedad='habitacion'
            form.save()
            data["mensaje"] = 'guardado con exito'

    return render(request, 'propiedad/nueva_propiedad.html', data)

def ModificarPropiedad(request,id):
    propiedad = Propiedad.objects.get(pk=id)
    tipo = propiedad.tipo_propiedad
    data = {
        "mensaje" : 'no se puede'
    }
    if tipo == 'casa':
        casa = PropiedadCasa.objects.get(pk=id)
        data = {
            "form": PropiedadCasaForm(instance=propiedad)
        }
        if request.method == 'POST':
            formulario = PropiedadCasaForm(data=request.POST, instance=casa)
            if formulario.is_valid():
                formulario.save()
                data={
                    "mensaje":'guardado correctamente',
                    "form": PropiedadCasaForm(instance=casa),
                }

    elif tipo == 'departamento':
        dpto = PropiedadDepto.objects.get(pk=id)
        data = {
            "form": PropiedadDptoForm(instance=dpto)
        }
        if request.method == 'POST':
            formulario = PropiedadDptoForm(data=request.POST, instance=dpto)
            if formulario.is_valid():
                formulario.save()
                data={
                    "mensaje":'guardado correctamente',
                    "form": PropiedadDptoForm(instance=dpto),
                }  
    elif tipo =='habitacion':
        habitacion = PropiedadHabitacion.objects.get(pk=id)
        data = {
            "form": PropiedadHabitacionForm(instance=habitacion)
        }
        if request.method == 'POST':
            formulario = PropiedadHabitacionForm(data=request.POST, instance=habitacion)
            if formulario.is_valid():
                formulario.save()
                data={
                    "mensaje":'guardado correctamente',
                    "form": PropiedadHabitacionForm(instance=habitacion),
                }

    return render(request, 'propiedad/nueva_propiedad.html', data)

def EliminarPropiedad(request, id):

    if PropiedadCasa.objects.filter(pk=id).exists():
        propiedad = PropiedadCasa.objects.get(pk=id)
        propiedad.delete()
    elif PropiedadDepto.objects.filter(pk=id).exists():
        propiedad = PropiedadDepto.objects.get(pk=id)
        propiedad.delete()
    elif PropiedadHabitacion.objects.filter(pk=id).exists():
        propiedad = PropiedadHabitacion.objects.get(pk=id)
        propiedad.delete()    

    return redirect(to='listado_propiedades')        
