from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import PersonaFisica, Persona, PersonaJuridica
from .forms import PersonaFisicaForm, PersonaJuridicaForm, FiltrarPersonaForm
from apps.contrato.models import InquilinoPropiedad, PropietarioPropiedad
import time
from django.forms import forms
from django.core.exceptions import ValidationError
from django.contrib import messages


# Create your views here.

@login_required
def Nueva_Persona_Fisica(request):
    if request.user.has_perms('persona.can_add_persona'):
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
    else:
        messages.error(request, 'No tienes permisos para agregar clientes')
        return redirect(to = "index")

@login_required
def Nueva_Persona_Juridica(request):
    if request.user.has_perms('persona.can_add_persona'):
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
    else:  
        messages.error(request,'No tienes permisos para agregar clientes')
        return redirect(to = "index")

@login_required
def Modificar_Persona(request, id):
    if request.user.has_perms('persona.can_change_persona'):
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
                    persona = PersonaFisica.objects.get(pk=persona.pk)
                    data = {
                        "id" : persona.id,
                        "nombre": persona.nombre + ' ' + persona.apellido,
                        "numero": persona.cuil ,
                        "direccion": persona.provincia + ' - ' + persona.localidad + ' - ' + persona.calle + ' - ' + persona.numero,
                        "telefono": persona.telefono,
                        "mail": persona.mail,
                        "tipo":persona.desc_per
                    }
                    messages.success(request,'El cliente se modifico correctamente')
                    return render(request,"base/mostrar_persona.html", data)
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
                    persona = PersonaJuridica.objects.get(pk = persona.pk)
                    data = {
                        "id" : persona.id,
                        "nombre": persona.razon_social,
                        "numero": persona.cuit ,
                        "direccion": persona.provincia + ' - ' + persona.localidad + ' - ' + persona.calle + ' - ' + persona.numero,
                        "telefono": persona.telefono,
                        "mail": persona.mail,
                        "tipo": persona.desc_per
                    }
                    messages.success(request,'El cliente se modifico correctamente')
                    return render(request,"base/mostrar_persona.html", data)
                data["form"] = formulario      

        return render(request, "base/nueva_persona.html", data)
    else:
        messages.error(request,'No tienes permiso para modificar CLIENTES')
        return redirect(to = "index")

@login_required
def Eliminar_Persona(request, id):
    if request.user.has_perms('persona.can_delete_persona'):
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
    else:
        messages.error(request,'No tienes permisos para eliminar CLIENTES')
        return redirect(to = "index")

@login_required
def Listado_Personas(request):
    if request.user.has_perms('persona.can_view_persona'):
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
    else:
        messages.error(request,'No tienes permisos para visualizar los CLIENTES')
        return redirect(to = "index")

@login_required
def MostrarPersona(request, id):
    if request.user.has_perms('persona.can_view_persona'):
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
    else:
        messages.error(request,'No cuentas con permiso para visualizar los clientes')
        return redirect(to="index")

@login_required
def ConfirmarPersona(request, id):
    if request.user.has_perms('persona.can_delete_persona'):
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
    else:
        messages.error(request,'No cuenta con permisos para eliminar CLIENTES')
        return redirect(to = "index")