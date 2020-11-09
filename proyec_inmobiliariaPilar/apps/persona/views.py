from django.shortcuts import render, HttpResponse, redirect
from .models import PersonaFisica, Persona, PersonaJuridica
from .forms import PersonaFisicaForm, PersonaJuridicaForm
import time
from django.forms import forms
from django.core.exceptions import ValidationError


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
            f.nombre_apellido = f.nombre_apellido.upper()
            f.desc_per = 'FISICA'
            f.save()
            data['mensaje']='guardado con exito'
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
            data['mensaje']='guardado con exito'
    
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
                f.nombre_apellido = f.nombre_apellido.upper()
                f.save()
                data={
                "mensaje":'guardado correctamente',
                "form": PersonaFisicaForm(instance=persona),
            }
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

    return render(request, "base/nueva_persona.html", data)

def Eliminar_Persona(request, id):
    if PersonaFisica.objects.filter(pk = id).exists():
        persona = PersonaFisica.objects.get(pk = id)
        persona.delete()
    elif PersonaJuridica.objects.filter(pk = id).exists():
        persona = PersonaJuridica.objects.get(pk= id)
        persona.delete()     

    return redirect(to='listado_personas')



def Listado_Personas(request):
    personasFisicas = PersonaFisica.objects.all()
    personasJuridicas = PersonaJuridica.objects.all()
    return render(request, "base/listado_personas.html", {"personasFisicas": personasFisicas , "personasJuridicas":personasJuridicas})

def Home(request):
    return render(request, "base/home.html")