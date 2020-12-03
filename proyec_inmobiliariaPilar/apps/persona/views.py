from django.shortcuts import render, HttpResponse, redirect
from .models import PersonaFisica, Persona, PersonaJuridica
from .forms import PersonaFisicaForm, PersonaJuridicaForm, FiltrarPersonaForm
from apps.contrato.models import InquilinoPropiedad, PropietarioPropiedad
import time
from django.forms import forms
from django.core.exceptions import ValidationError
from django.contrib import messages


# Create your views here.

def Nueva_Persona_Fisica(request):
    data = {
        "form": PersonaFisicaForm()
    }

    if request.method == 'POST':
        print(request.POST)
        formulario = PersonaFisicaForm(request.POST)
        if formulario.is_valid():
            f = formulario.save(commit=False)
            f.provincia = f.provincia.upper()
            f.localidad = f.localidad.upper()
            f.barrio = f.barrio.upper()
            f.calle = f.calle.upper()
            f.nombre = f.nombre.upper()
            f.apellido = f.apellido.upper()
            f.desc_per = 'FISICA'
            f.save()
            messages.success(request,'CLIENTE '+f.nombre+' '+f.apellido+' AGREGADO CORRECTAMENTE')
            return redirect(to='listado_personas')

        data["form"] = formulario
    
    return render(request, "base/nueva_persona.html", data)


def Nueva_Persona_Juridica(request):
    data = {
        "form": PersonaJuridicaForm()
    }

    if request.method == 'POST':
        print(request.POST)
        formulario = PersonaJuridicaForm(request.POST)
        if formulario.is_valid():
            f = formulario.save(commit=False)
            f.provincia = f.provincia.upper()
            f.localidad = f.localidad.upper()
            f.barrio = f.barrio.upper()
            f.calle = f.calle.upper()
            f.razon_social = f.razon_social.upper()
            f.desc_per = 'JURIDICA'
            f.save()
            messages.success(request,'SE AGREGO AL CLIENTE JURIDICO '+f.razon_social+' CORRECTAMENTE')
            return redirect(to='listado_personas')
        data["form"] = formulario 
    
    return render(request, "base/nueva_persona.html", data)


def Modificar_Persona(request, id):
    if PersonaFisica.objects.filter(pk = id).exists():
        persona = PersonaFisica.objects.get(pk = id)
        data = {
            "form":PersonaFisicaForm(instance=persona)
        }
        if request.method == 'POST':
            formulario = PersonaFisicaForm(data=request.POST, instance=persona)
            if formulario.is_valid():
                f = formulario.save(commit=False)
                f.provincia = f.provincia.upper()
                f.localidad = f.localidad.upper()
                f.barrio = f.barrio.upper()
                f.calle = f.calle.upper()
                f.nombre = f.nombre.upper()
                f.apellido = f.apellido.upper()
                f.save()
                data={
                "mensaje":'guardado correctamente',
                "form": PersonaFisicaForm(instance=persona),
                }
            data["form"] = formulario 

    elif PersonaJuridica.objects.filter(pk = id).exists():
        persona = PersonaJuridica.objects.get(pk= id)
        data = {
            "form":PersonaJuridicaForm(instance=persona)
        }
        if request.method == 'POST':
            formulario = PersonaJuridicaForm(data=request.POST, instance=persona)
            if formulario.is_valid():
                f = formulario.save(commit=False)
                f.provincia = f.provincia.upper()
                f.localidad = f.localidad.upper()
                f.barrio = f.barrio.upper()
                f.calle = f.calle.upper()
                f.razon_social = f.razon_social.upper()
                f.save()
                data={
                "mensaje":'guardado correctamente',
                "form": PersonaJuridicaForm(instance=servicio),
                }
            data["form"] = formulario      

    return render(request, "base/nueva_persona.html", data)


def Eliminar_Persona(request, id):
    if PersonaFisica.objects.filter(pk = id).exists():
        persona = PersonaFisica.objects.get(pk = id)
        if InquilinoPropiedad.objects.filter(inquilino = persona, cancelacion = False).exists():
            messages.error(request, 'NO SE PUEDE ELIMINAR A UN CLIENTE CON UN CONTRATO VIGENTE')
            return redirect(to='listado_personas')
        if PropietarioPropiedad.objects.filter(propietario = persona).exists():
            messages.error(request, 'NO SE PUEDE ELIMINAR A UN CLIENTE CON UN CONTRATO VIGENTE')
            return redirect(to='listado_personas')
        persona.delete()
        messages.success(request, 'SE HA ELIMINADO AL CLIENTE ' + persona.nombre + ' ' + persona.apellido+ ' CORRECTAMENTE')
    elif PersonaJuridica.objects.filter(pk = id).exists():
        persona = PersonaJuridica.objects.get(pk= id)
        if InquilinoPropiedad.objects.filter(inquilino = persona, cancelacion=False).exists():
            messages.error(request, 'NO SE PUEDE ELIMINAR A UN CLIENTE CON UN CONTRATO VIGENTE')
            return redirect(to='listado_personas')
        if PropietarioPropiedad.objects.filter(propietario = persona).exists():
            messages.error(request, 'NO SE PUEDE ELIMINAR A UN CLIENTE CON UN CONTRATO VIGENTE')
            return redirect(to='listado_personas')
        persona.delete()
        messages.success(request, 'SE HA ELIMINADO AL CLIENTE ' + persona.razon_social + ' CORRECTAMENTE')     

    return redirect(to='listado_personas')


def Listado_Personas(request):
    data = {
            "form": FiltrarPersonaForm(),
            "personas": Persona.objects.all(),
            #personasJuridicas":PersonaJuridica.objects.all()
    }
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        if tipo != "":
            if tipo == 'FISICA':
                personasFisicas = PersonaFisica.objects.all()
                data = {
                    "form": FiltrarPersonaForm(data=request.POST),
                    "personas": personasFisicas
                }
            else:
                personasJuridicas= PersonaJuridica.objects.all()
                data = {
                    "form": FiltrarPersonaForm(data=request.POST),
                    "personas": personasJuridicas,
                }
    
    return render(request, "base/listado_personas.html", data)


def MostrarPersona(request, id):
    data = {
        "id" : "no se puede mostrar"
    }
    if PersonaFisica.objects.filter(pk = id).exists():
        persona = PersonaFisica.objects.get(pk = id)
        data = {
            "id" : persona.id,
            "nombre": persona.nombre + ' ' + persona.apellido,
            "numero": persona.cuil ,
            "direccion": persona.provincia + ' - ' + persona.localidad + ' - ' + persona.calle + ' - ' + persona.numero,
            "telefono": persona.telefono,
            "mail": persona.mail,
            "tipo":persona.desc_per
        }
    if PersonaJuridica.objects.filter(pk = id).exists():
        persona = PersonaJuridica.objects.get(pk = id)
        data = {
            "id" : persona.id,
            "nombre": persona.razon_social,
            "numero": persona.cuit ,
            "direccion": persona.provincia + ' - ' + persona.localidad + ' - ' + persona.calle + ' - ' + persona.numero,
            "telefono": persona.telefono,
            "mail": persona.mail,
            "tipo": persona.desc_per
        }
    
    
    return render(request, "base/mostrar_persona.html", data)


def ConfirmarPersona(request, id):
    data = {
        "id" : "no se puede mostrar"
    }
    if PersonaFisica.objects.filter(pk = id).exists():
        persona = PersonaFisica.objects.get(pk = id)
        data = {
            "id" : persona.id,
            "nombre": persona.nombre + ' ' + persona.apellido,
            "numero": persona.cuil ,
            "direccion": persona.provincia + ' - ' + persona.localidad + ' - ' + persona.calle + ' - ' + persona.numero,
            "telefono": persona.telefono,
            "mail": persona.mail,
            "tipo":persona.desc_per
        }
    if PersonaJuridica.objects.filter(pk = id).exists():
        persona = PersonaJuridica.objects.get(pk = id)
        data = {
            "id" : persona.id,
            "nombre": persona.razon_social,
            "numero": persona.cuit ,
            "direccion": persona.provincia + ' - ' + persona.localidad + ' - ' + persona.calle + ' - ' + persona.numero,
            "telefono": persona.telefono,
            "mail": persona.mail,
            "tipo": persona.desc_per
        }
    
    
    return render(request, "base/eliminar_persona.html", data)