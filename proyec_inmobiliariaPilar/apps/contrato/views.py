from django.shortcuts import render, redirect
from .forms import PropietarioPropiedadForm, InquilinoPropiedadForm
from .models import PropietarioPropiedad,InquilinoPropiedad

# Create your views here.

def NuevoContrato(request):
    if request.path == '/contrato/nuevo_contratoPropietario/':
        data = {
            "form" : PropietarioPropiedadForm()
        }
        if request.method == 'POST':
            formulario = PropietarioPropiedadForm(request.POST)
            if formulario.is_valid:
                formulario.save()
                data['mensaje'] = 'guardado con exito'
        
        return render(request, "contrato/nuevo_contrato.html", data)

    elif request.path == '/contrato/nuevo_contratoInquilino/':
        data = {
            "form" : InquilinoPropiedadForm()
        }
        if request.method == 'POST':
            formulario = InquilinoPropiedadForm(request.POST)
            if formulario.is_valid:
                formulario.save()
                data['mensaje'] = 'guardado con exito'

    return render(request, "contrato/nuevo_contrato.html", data)

def ModificarContrato(request, id):
    if PropietarioPropiedad.objects.filter(pk = id).exists():
        contrato = PropietarioPropiedad.objects.get(pk = id)
        data = {
            "form":PropietarioPropiedadForm(instance=contrato)
        }
        if request.method == 'POST':
            formulario = PropietarioPropiedadForm(data=request.POST, instance=contrato)
            if formulario.is_valid():
                formulario.save()
                data={
                "mensaje":'guardado correctamente',
                "form": PropietarioPropiedadForm(instance=contrato),
            }
    elif InquilinoPropiedad.objects.filter(pk = id).exists():
        contrato = InquilinoPropiedad.objects.get(pk= id)
        data = {
            "form":InquilinoPropiedadForm(instance=contrato)
        }
        if request.method == 'POST':
            formulario = InquilinoPropiedadForm(data=request.POST, instance=contrato)
            if formulario.is_valid():
                formulario.save()
                data={
                "mensaje":'guardado correctamente',
                "form": InquilinoPropiedadForm(instance=contrato),
                } 
    return render(request, "contrato/nuevo_contrato.html", data)     

def EliminarContrato(request, id):
    if PropietarioPropiedad.objects.filter(pk = id).exists():
        contrato = PropietarioPropiedad.objects.get(pk = id)
        contrato.delete()
    elif InquilinoPropiedad.objects.filter(pk = id).exists():
        contrato = InquilinoPropiedad.objects.get(pk= id)
        contrato.delete()     

    return redirect(to='listado_contratos')


def ListadoContrato(request):
    contratosPropietarios = PropietarioPropiedad.objects.all()
    contratosInquilinos = InquilinoPropiedad.objects.all() 
    data = {
        "propietarios" : contratosPropietarios,
        "inquilinos": contratosInquilinos
    }
    return render(request,"contrato/listado_contratos.html", data)