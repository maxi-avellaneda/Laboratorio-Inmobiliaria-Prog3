from django.shortcuts import render, redirect
import datetime
from .forms import PropietarioPropiedadForm, InquilinoPropiedadForm
from apps.propiedad.models import Propiedad, Estado
from .models import PropietarioPropiedad,InquilinoPropiedad
from apps.propiedad.views import GenerarEstado
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from pilar.settings import LOGIN_REDIRECT_URL

# Create your views here.


@login_required
def NuevoContrato(request):
    if request.user.has_perms('contrato.can_add_inquilinopropiedad', 'contrato.can_add_propietariopropiedad'):
        if request.path == '/contrato/nuevo_contratoPropietario/':
            data = {
                "form" : PropietarioPropiedadForm()
            }
            if request.method == 'POST':
                formulario = PropietarioPropiedadForm(request.POST)
                if formulario.is_valid():
                    f = formulario.save(commit=False)
                    f.cancelacion = False
                    f.fecha_cancelacion = None
                    f.save()
                    contrato = PropietarioPropiedad.objects.last()
                    data = {
                        "contrato":contrato
                    }
                    messages.success(request,'El contrato se generó correctamente')
                    return render(request, "contrato/mostrar_contrato.html", data)
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
                    if f.propiedad.estado_actual == 'OCUPADO':
                        messages.error(request, 'La propiedad '+str(f.propiedad.id)+' se encuentra actualmente OCUPADA, actualice los datos de la propiedad')
                        return redirect(to='listado_propiedades')
                    if f.propiedad.estado_actual == 'EN MANTENIMIENTO':
                        messages.error(request, 'La propiedad '+str(f.propiedad.id)+' se encuentra actualmente EN MANTENIMIENTO, actualice los datos de la propiedad')
                        return redirect(to='listado_propiedades')
                    f.cancelacion = False
                    f.fecha_cancelacion = None
                    propiedad = Propiedad.objects.get(pk=f.propiedad.id)
                    propiedad.estado_actual = 'OCUPADO'
                    propiedad.save()
                    GenerarEstado(propiedad)
                    f.save()
                    contrato = InquilinoPropiedad.objects.last()
                    data = {
                        "contrato":contrato
                    }
                    messages.success(request,'El contrato se generó correctamente')
                    return render(request, "contrato/mostrar_contrato.html", data)
                data["form"] = formulario

        return render(request, "contrato/nuevo_contrato.html", data)
    
    else:
        messages.error(request,'No cuenta con permiso para agregar contratos')
        return redirect(to='index')


@login_required
def ModificarContrato(request, id):
    if request.user.has_perms('contrato.can_change_inquilinopropiedad', 'contrato.can_change_propietariopropiedad'): 
        if PropietarioPropiedad.objects.filter(pk = id).exists():
            contrato = PropietarioPropiedad.objects.get(pk = id)
            if contrato.cancelacion:
                messages.error(request, 'No se puede modificar un contrato cancelado')
                return redirect(to='listado_contratos')
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
            if contrato.cancelacion:
                messages.error(request, 'No se puede modificar un contrato cancelado')
                return redirect(to='listado_contratos')
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
    else:
        messages.error(request,'No cuenta con permiso para modificar contratos')
        return redirect(to='index')


@login_required
def MostrarContrato(request, id):
    if request.user.has_perms('contrato.can_view_inquilinopropiedad', 'contrato.can_view_propietariopropiedad'):
        data={
            "queti":'qwqweeqwes'
        }
        if InquilinoPropiedad.objects.filter(pk=id).exists():
            contrato = InquilinoPropiedad.objects.get(pk=id)
            data = {
                "id": contrato.id,
                "cliente": contrato.inquilino,
                "tipo": contrato.inquilino.desc_per,
                "direccion" : contrato.inquilino.provincia+', '+contrato.inquilino.localidad+', '+contrato.inquilino.calle+', '+contrato.inquilino.numero,
                "propiedad": contrato.propiedad,
                "cant_personas": contrato.cant_personas,
                "importe_total": contrato.importe_total,
                "fecha_inicio": contrato.fecha_inicio,
                "fecha_fin": contrato.fecha_fin
            }
        return render(request, 'contrato/mostrar_contrato.html', data)
    else:
        messages.error(request,'No cuenta con permiso para visualizar los contratos')
        return redirect(to="index")


@login_required
def ConfirmarEliminarContrato(request, id):
    if request.user.has_perms('contrato.can_delete_inquilinopropiedad', 'contrato.can_delete_propietariopropiedad'):
        data={
            "queti":'qwqweeqwes'
        }
        if InquilinoPropiedad.objects.filter(pk=id).exists():
            contrato = InquilinoPropiedad.objects.get(pk=id)
            data = {
                "contrato":contrato
            }
        if PropietarioPropiedad.objects.filter(pk=id).exists():
            contrato = PropietarioPropiedad.objects.get(pk=id)
            data = {
                "contrato":contrato
            }
        return render(request, 'contrato/eliminar_contrato.html', data)
    else:
        messages.error(request,'No tienes permisos para eliminar contratos')
        return redirect(to = "index")


@login_required
def EliminarContrato(request, id):
    if request.user.has_perms('contrato.can_delete_inquilinopropiedad','contrato.can_delete_propietariopropiedad'):
        if PropietarioPropiedad.objects.filter(pk = id).exists():
            contrato = PropietarioPropiedad.objects.get(pk = id)
            if contrato.cancelacion:
                messages.error(request,'No se puede eliminar un contrato cancelado')
                return redirect(to='listado_contratos')
            contrato.delete()
            messages.success(request,'SE HA ELIMINADO CON EXITO')
        elif InquilinoPropiedad.objects.filter(pk = id).exists():
            contrato = InquilinoPropiedad.objects.get(pk= id)
            if contrato.cancelacion:
                messages.error(request,'No se puede eliminar un contrato cancelado')
                return redirect(to='listado_contratos')
            propiedad = Propiedad.objects.get(pk=contrato.propiedad.id)
            propiedad.estado_actual = 'DISPONIBLE'
            propiedad.save()
            GenerarEstado(propiedad)
            contrato.delete()
            messages.success(request,'SE HA ELIMINADO CON EXITO')     

        return redirect(to='listado_contratos')
    else:
        messages.error(request,'No tienen permiso para eliminar contratos')
        return redirect(to="index")


@login_required
def ListadoContrato(request):
    if request.user.has_perms('contrato.can_view_inquilinopropiedad', 'contrato.can_view_propietariopropiedad'):
        contratosPropietarios = PropietarioPropiedad.objects.all()
        contratosInquilinos = InquilinoPropiedad.objects.all() 
        data = {
            "propietarios" : contratosPropietarios,
            "inquilinos": contratosInquilinos
        }
        return render(request,"contrato/listado_contratos.html", data)
    else:
        messages.error(request,'No cuentas con permisos para visualizar los contratos')
        return redirect(to = "index")

@login_required
def ConfirmarCancelacion(request,id):
    if request.user.has_perms('contrato.can_change_inquilinopropiedad', 'contrato.can_change_propietariopropiedad'):
        data={
            "queti":'qwqweeqwes'
        }
        if InquilinoPropiedad.objects.filter(pk=id).exists():
            contrato = InquilinoPropiedad.objects.get(pk=id)
            if contrato.cancelacion:
                messages.error(request, 'Este contrato ya fue cancelado')
                return redirect(to='listado_contratos')
            data = {
                "id": contrato.id,
                "cliente": contrato.inquilino,
                "tipo": contrato.inquilino.desc_per,
                "direccion" : contrato.inquilino.provincia+', '+contrato.inquilino.localidad+', '+contrato.inquilino.calle+', '+contrato.inquilino.numero,
                "propiedad": contrato.propiedad,
                "cant_personas": contrato.cant_personas,
                "importe_total": contrato.importe_total,
                "fecha_inicio": contrato.fecha_inicio,
                "fecha_fin": contrato.fecha_fin
            }
        return render(request, 'contrato/cancelar_contrato.html', data)
    else:  
        messages.error(request,'No cuentas con permiso para modificar contratos')
        return redirect(to = "index")

@login_required
def CancelarContrato(request, id):
    if request.user.has_perms('contrato.can_change_inquilinopropiedad', 'contrato.can_change_propietariopropiedad'):
        if InquilinoPropiedad.objects.filter(pk=id).exists():
            contrato = InquilinoPropiedad.objects.get(pk=id)
            if contrato.cancelacion:
                messages.error(request, 'Este contrato ya fue cancelado')
                return redirect(to='listado_contratos')
            contrato.cancelacion = True
            contrato.fecha_cancelacion = datetime.date.today()
            contrato.save()
            #Liberar propiedad
            propiedad = contrato.propiedad
            propiedad.estado_actual = 'DISPONIBLE'
            propiedad.save()
            GenerarEstado(propiedad)
            messages.success(request, 'Se ha cancelado correctamente el contrato')
            return redirect(to='listado_contratos')
        
        messages.error(request,'No se encuentra el contrato')
        return redirect(to='listado_contratos')
    else:
        messages.error(request,'No cuentas con permisos para modificar contratos')
        return redirect(to = "index")