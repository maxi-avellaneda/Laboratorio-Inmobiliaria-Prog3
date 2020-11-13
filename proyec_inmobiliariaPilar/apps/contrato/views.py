from django.shortcuts import render, redirect
from .forms import PropietarioPropiedadForm, InquilinoPropiedadForm
from apps.propiedad.models import Propiedad, Estado
from .models import PropietarioPropiedad,InquilinoPropiedad
from apps.propiedad.views import GenerarEstado

# Create your views here.

def NuevoContrato(request):
    if request.path == '/contrato/nuevo_contratoPropietario/':
        data = {
            "form" : PropietarioPropiedadForm()
        }
        if request.method == 'POST':
            formulario = PropietarioPropiedadForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = 'guardado con exito'
            data["form"] = formulario
        
        return render(request, "contrato/nuevo_contrato.html", data)

    elif request.path == '/contrato/nuevo_contratoInquilino/':
        data = {
            "form" : InquilinoPropiedadForm()
        }
        if request.method == 'POST':
            formulario = InquilinoPropiedadForm(request.POST)
            if formulario.is_valid():
                f = formulario.save(commit=False)
                propiedad = Propiedad.objects.get(pk=f.propiedad.id)
                propiedad.estado_actual = 'OCUPADO'
                propiedad.save()
                GenerarEstado(propiedad)
                f.save()
                data['mensaje'] = 'guardado con exito'
            data["form"] = formulario

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
            data["form"] = formulario        

    elif InquilinoPropiedad.objects.filter(pk = id).exists():
        contrato = InquilinoPropiedad.objects.get(pk= id)
        prop_ant = Propiedad.objects.get(pk = contrato.propiedad.id)
        data = {
            "form":InquilinoPropiedadForm(instance=contrato)
        }
        if request.method == 'POST':
            formulario = InquilinoPropiedadForm(data=request.POST, instance=contrato)
            if formulario.is_valid():
                f = formulario.save(commit=False)
                prop_nueva = f.propiedad
                if prop_ant != prop_nueva:
                    prop_ant.estado_actual = 'DISPONIBLE'
                    prop_ant.save()
                    GenerarEstado(prop_ant)
                    prop_nueva.estado_actual = 'OCUPADO'
                    prop_nueva.save()
                    GenerarEstado(prop_nueva)
                f.save()
                data={
                "mensaje":'guardado correctamente',
                "form": InquilinoPropiedadForm(instance=contrato),
                }
            data["form"] = formulario
    return render(request, "contrato/nuevo_contrato.html", data)     

def EliminarContrato(request, id):
    if PropietarioPropiedad.objects.filter(pk = id).exists():
        contrato = PropietarioPropiedad.objects.get(pk = id)
        contrato.delete()
    elif InquilinoPropiedad.objects.filter(pk = id).exists():
        contrato = InquilinoPropiedad.objects.get(pk= id)
        propiedad = Propiedad.objects.get(pk=contrato.propiedad.id)
        propiedad.estado_actual = 'DISPONIBLE'
        propiedad.save()
        GenerarEstado(propiedad)
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