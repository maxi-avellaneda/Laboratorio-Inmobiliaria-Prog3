from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.contrato.models import InquilinoPropiedad, PropietarioPropiedad
from .models import Propiedad, PropiedadCasa, PropiedadDepto, PropiedadHabitacion, Oferta, Estado
from .forms import PropiedadCasaForm,PropiedadDptoForm,PropiedadHabitacionForm, OfertaForm, EstadoForm, FiltrarPropiedadForm, FiltrarOfertaForm

# Create your views here.

@login_required
def ListadoPropiedades(request):
    if request.user.has_perms('propiedad.can_view_propiedad'):
        propiedades = Propiedad.objects.all()
        form = FiltrarPropiedadForm()
        if request.method == 'POST':
            condicion= request.POST.get('condicion')
            tipo_propiedad = request.POST.get('tipo_propiedad')
            zona = request.POST.get('zona')
            if condicion != "":
                propiedades = propiedades.filter(estado_actual=condicion)    
            if tipo_propiedad != "":
                propiedades = propiedades.filter(tipo_propiedad=tipo_propiedad)
            if zona != "":    
                propiedades = propiedades.filter(zona= zona)

        return render(request,'propiedad/lista_propiedades.html',{'propiedades':propiedades, 'form':form})
    else:
        messages.error(request,'No tienes permisos para visualizar las PROPIEDADES')
        return redirect(to = "index")

@login_required
def detallePropiedad(request,id):
    if request.user.has_perms('propiedad.can_view_propiedad'):
        pro = Propiedad.objects.get(pk=id)
        return render(request,'propiedad/detalles_propiedad.html',{'pro':pro})
    else:
        messages.error(request,'No tienes permiso para visualizar PROPIEDADES')
        return redirect(to = "index")

@login_required
def NuevaPropiedadCasa(request):
    if request.user.has_perms('propiedad.can_add_propiedad'):
        data = {
            "form" : PropiedadCasaForm()
        }
        if request.method == 'POST':
            f = PropiedadCasaForm(request.POST,request.FILES)
            if f.is_valid():
                form = f.save(commit=False)
                form.tipo_propiedad='CASA'
                form.desc_prop = form.desc_prop.upper()
                form.tipo_propiedad = form.tipo_propiedad.upper()
                form.zona = form.zona.upper()
                form.estado_actual = form.estado_actual.upper()
                form.save()
                casa = Propiedad.objects.last()
                GenerarEstado(casa)
            data["form"] = f
                
        return render(request, 'propiedad/nueva_propiedad.html', data)
    else:
        messages.error(request,'No tienes permiso para ingresar PROPIEDADES')
        return redirect(to = "index")

@login_required
def NuevaPropiedadDpto(request):
    if request.user.has_perms('propiedad.can_add_propiedad'):
        data = {
            "form" : PropiedadDptoForm()
        }
        if request.method == 'POST':
            f = PropiedadDptoForm(request.POST,request.FILES)
            if f.is_valid():
                form = f.save(commit=False)
                form.tipo_propiedad ='DEPARTAMENTO'
                form.desc_prop = form.desc_prop.upper()
                form.tipo_propiedad = form.tipo_propiedad.upper() 
                form.zona = form.zona.upper()
                form.estado_actual = form.estado_actual.upper()
                form.save()
                dpto = Propiedad.objects.last()
                GenerarEstado(dpto)
                data["mensaje"]= 'guardado con exito'
            data["form"] = f

        return render(request, 'propiedad/nueva_propiedad.html', data )
    else:
        messages.error(request,'No tienes permiso para el ingreso de PROPIEDADES')
        return redirect(to = "index")

@login_required
def NuevaPropiedadHabitacion(request):
    if request.user.has_perms('propiedad.can_add_propiedad'):
        data = {
            "form" : PropiedadHabitacionForm()
        }
        if request.method == 'POST':
            f = PropiedadHabitacionForm(request.POST,request.FILES)
            if f.is_valid():
                form = f.save(commit=False)
                form.tipo_propiedad='HABITACION'
                form.desc_prop = form.desc_prop.upper()
                form.tipo_propiedad = form.tipo_propiedad.upper() 
                form.zona = form.zona.upper()
                form.estado_actual = form.estado_actual.upper()
                form.save()
                habitacion = Propiedad.objects.last()
                GenerarEstado(habitacion)
                data["mensaje"]= 'guardado con exito'
            data["form"] = f

        return render(request, 'propiedad/nueva_propiedad.html', data)
    else:
        messages.error(request,'No tienes permiso para el ingreso de PROPIEDADES')
        return redirect(to = "index")

@login_required
def ModificarPropiedad(request,id):
    if request.user.has_perms('propiedad.can_change_propiedad'):
        propiedad = Propiedad.objects.get(pk=id)
        if InquilinoPropiedad.objects.filter(propiedad = propiedad).exists():
            messages.error(request,'NO SE PUEDE MODIFICAR UNA PROPIEDAD QUE SE ENCUENTRA EN CONTRATO')
            return redirect(to='listado_propiedades')
        if PropietarioPropiedad.objects.filter(propiedad = propiedad).exists():
            messages.error(request,'NO SE PUEDE MODIFICAR UNA PROPIEDAD QUE SE ENCUENTRA EN CONTRATO')
            return redirect(to='listado_propiedades')
        tipo = propiedad.tipo_propiedad
        data = {
            "mensaje" : 'no se puede'
        }
        if tipo == 'CASA':
            casa = PropiedadCasa.objects.get(pk=id)
            cambio = casa.estado_actual
            data = {
                "form": PropiedadCasaForm(instance=propiedad)
            }
            if request.method == 'POST':
                formulario = PropiedadCasaForm(data=request.POST,files=request.FILES, instance=casa)
                if formulario.is_valid():
                    formulario.save()
                    data={
                        "mensaje":'guardado correctamente',
                        "form": PropiedadCasaForm(instance=casa),
                    }
                    casa = Propiedad.objects.get(pk=id)
                    if casa.estado_actual != cambio:
                        GenerarEstado(casa)
                data["form"] = formulario

        elif tipo == 'DEPARTAMENTO':
            dpto = PropiedadDepto.objects.get(pk=id)
            cambio = dpto.estado_actual
            data = {
                "form": PropiedadDptoForm(instance=dpto)
            }
            if request.method == 'POST':
                formulario = PropiedadDptoForm(data=request.POST,files=request.FILES, instance=dpto)
                if formulario.is_valid():
                    formulario.save()
                    data={
                        "mensaje":'guardado correctamente',
                        "form": PropiedadDptoForm(instance=dpto),
                    }  
                    dpto = Propiedad.objects.get(pk=id)
                    if dpto.estado_actual != cambio:
                        GenerarEstado(dpto)
                data["form"] = formulario

        elif tipo =='HABITACION':
            habitacion = PropiedadHabitacion.objects.get(pk=id)
            cambio = habitacion.estado_actual
            data = {
                "form": PropiedadHabitacionForm(instance=habitacion)
            }
            if request.method == 'POST':
                formulario = PropiedadHabitacionForm(data=request.POST,files=request.FILES,instance=habitacion)
                if formulario.is_valid():
                    formulario.save()
                    data={
                        "mensaje":'guardado correctamente',
                        "form": PropiedadHabitacionForm(instance=habitacion),
                    }
                    habitacion = Propiedad.objects.get(pk=id)
                    if habitacion.estado_actual != cambio:
                        GenerarEstado(habitacion)
                data["form"] = formulario

        return render(request, 'propiedad/nueva_propiedad.html', data)
    else:  
        messages.error(request,'No tienes permiso para modificar PROPIEDADES')
        return redirect(to = "index")
    
@login_required
def EliminarPropiedad(request, id):
    if request.user.has_perms('propiedad.can_delete_propiedad'):
        if PropiedadCasa.objects.filter(pk=id).exists():
            propiedad = PropiedadCasa.objects.get(pk=id)
            if InquilinoPropiedad.objects.filter(propiedad = propiedad).exists():
                messages.error(request, 'NO SE PUEDE ELIMINAR A UNA PROPIEDAD CON UN CONTRATO VIGENTE')
                return redirect(to='listado_propiedades')
            if PropietarioPropiedad.objects.filter(propiedad = propiedad).exists():
                messages.error(request, 'NO SE PUEDE ELIMINAR A UNA PROPIEDAD CON UN CONTRATO VIGENTE')
                return redirect(to='listado_propiedades') 
            propiedad.delete()
            messager.success(request, 'ELIMINADO CON EXITO')
        elif PropiedadDepto.objects.filter(pk=id).exists():
            propiedad = PropiedadDepto.objects.get(pk=id)
            if InquilinoPropiedad.objects.filter(propiedad = propiedad).exists():
                messages.error(request, 'NO SE PUEDE ELIMINAR A UNA PROPIEDAD CON UN CONTRATO VIGENTE')
                return redirect(to='listado_propiedades')
            if PropietarioPropiedad.objects.filter(propiedad = propiedad).exists():
                messages.error(request, 'NO SE PUEDE ELIMINAR A UNA PROPIEDAD CON UN CONTRATO VIGENTE')
                return redirect(to='listado_propiedades') 
            propiedad.delete()
            messager.success(request, 'ELIMINADO CON EXITO')
        elif PropiedadHabitacion.objects.filter(pk=id).exists():
            propiedad = PropiedadHabitacion.objects.get(pk=id)
            if InquilinoPropiedad.objects.filter(propiedad = propiedad).exists():
                messages.error(request, 'NO SE PUEDE ELIMINAR A UNA PROPIEDAD CON UN CONTRATO VIGENTE')
                return redirect(to='listado_propiedades')
            if PropietarioPropiedad.objects.filter(propiedad = propiedad).exists():
                messages.error(request, 'NO SE PUEDE ELIMINAR A UNA PROPIEDAD CON UN CONTRATO VIGENTE')
                return redirect(to='listado_propiedades') 
            propiedad.delete()
            messager.success(request, 'ELIMINADO CON EXITO')    

        return redirect(to='listado_propiedades')
    else:
        messages.error(request,'No tienes permiso para eliminar PROPIEDADES')    
        return redirect(to = "index")

@login_required
def NuevaOferta(request):
    if request.user.has_perms('oferta.can_add_oferta'):
        data = {
            "form" : OfertaForm()
        }
        if request.method == 'POST':
            f = OfertaForm(request.POST)
            if f.is_valid():
                f.save()
                data["mensaje"] = 'guardado con exito'
            data["form"] = f

        return render(request, 'propiedad/nueva_propiedad.html', data)
    else:
        messages.error(request,'No tienes permisos para el ingreso de OFERTAS')
        return redirect(to = "index")

@login_required
def ModificarOferta(request,id):
    if request.user.has_perms('oferta.can_change_oferta'):
        oferta = Oferta.objects.get(pk = id)
        data = {
            "form" : OfertaForm(instance=oferta)
        }
        if request.method == 'POST':
            f = OfertaForm(data=request.POST, instance=oferta)
            if f.is_valid():
                f.save()
                data = {
                    "mensaje":'guardado correctamente',
                    "form": OfertaForm(instance=oferta)
                }

        return render(request, 'propiedad/nueva_propiedad.html', data)
    else:
        messages.error(request, 'No tienes permisos para modifcar OFERTAS')
        return redirect(to = "index")

@login_required
def EliminarOferta(request,id):
    if request.user.has_perms('oferta.can_delete_oferta'):
        if Oferta.objects.filter(pk = id).exists():
            oferta = Oferta.objects.get(pk = id)
            oferta.delete()
        return redirect(to='listado_ofertas')
    else:
        messages.error(request,'No tienes permiso para eliminar OFERTAS')
        return redirect(to="index")

@login_required
def MostrarOfertas(request):
    if request.user.has_perms('oferta.can_view_oferta'):
        ofertas = Oferta.objects.all()
        return render(request,'oferta/ofertas.html', {"ofertas": ofertas})
    else:
        messages.error(request,'No tienes permiso para visualizar las OFERTAS')
        return redirect(to = "index")

@login_required
def ListarOfertas(request):
    if request.user.has_perms('oferta.can_view_oferta'):
        data = {
            "form": FiltrarOfertaForm(),
            "ofertas":Oferta.objects.all()
        }
        if request.method == 'POST':
            cod_oferta= request.POST.get('cod_oferta')
            permite_cancelacion = request.POST.get('permite_cancelacion')
            ofertas = Oferta.objects.all()
            if cod_oferta != '':
                ofertas = ofertas.filter(cod_oferta=cod_oferta)
            if permite_cancelacion != '':
                if permite_cancelacion == 'SI':
                    ofertas = ofertas.filter(permite_cancelacion=True)
                else:
                    ofertas = ofertas.filter(permite_cancelacion = False)
            data["ofertas"] = ofertas
            data["form"] = FiltrarOfertaForm(data=request.POST)
        return render(request,'oferta/listado_ofertas.html', data)
    else:
        messages.error(request,'No tienes permiso para visualizar las OFERTAS')
        return redirect(to = "index")


def GenerarEstado(propiedad):
    if Estado.objects.filter(propiedad=propiedad).exists():
        estado_anterior = Estado.objects.filter(propiedad=propiedad).last()
        estado_anterior.fec_fin = datetime.now()
        estado_anterior.band = False
        estado_anterior.save()
        Estado.objects.create(propiedad=propiedad,fec_inicio=datetime.now(), fec_fin=None, estado=propiedad.estado_actual,band=True)
    else:
        Estado.objects.create(propiedad =propiedad, fec_inicio= propiedad.fecha_alta, fec_fin=None,estado=propiedad.estado_actual,band=True)

@login_required
def MostrarPropiedad(request,id):
    if request.user.has_perms('propiedad.can_view_propiedad'):
        if PropiedadCasa.objects.filter(pk=id).exists():
            propiedad = PropiedadCasa.objects.get(pk = id)
            data = {
                "id": propiedad.id,
                "mts": propiedad.mts,
                "mts_semicubiertos": propiedad.mts_semicubiertos,
                "patio": propiedad.propiedadcasa.patio ,
            }
            return render(request, 'propiedad/mostrar_propiedad.html', data)
        
        return redirect(to='listado_propiedades')
    else:
        messages.error(request,'No tienes permisos para visualizar PROPIEDADES')
        return redirect(to = "index")

@login_required
def ConfirmarPropiedad(request,id):
    if request.user.has_perms('propiedad.can_delete_propiedad'):
        if PropiedadCasa.objects.filter(pk=id).exists():
            propiedad = PropiedadCasa.objects.get(pk = id)
            data = {
                "id": propiedad.id,
                "mts": propiedad.mts,
                "mts_semicubiertos": propiedad.mts_semicubiertos,
                "patio": propiedad.propiedadcasa.patio ,
            }
            return render(request, 'propiedad/eliminar_propiedad.html', data)

        if PropiedadHabitacion.objects.filter(pk=id).exists():
            propiedad = PropiedadHabitacion.objects.get(pk = id)
            data = {
                "id": propiedad.id,
                "mts": propiedad.mts,
                "mts_semicubiertos": propiedad.mts_semicubiertos,
            }
            return render(request, 'propiedad/eliminar_propiedad.html', data)

        if PropiedadDepto.objects.filter(pk=id).exists():
            propiedad = PropiedadDepto.objects.get(pk = id)
            data = {
                "id": propiedad.id,
                "mts": propiedad.mts,
                "mts_semicubiertos": propiedad.mts_semicubiertos,
            }
            return render(request, 'propiedad/eliminar_propiedad.html', data)
        
        return redirect(to='listado_propiedades')
    else:
        messages.error(request,'No tienes permisos para eliminar PROPIEDADES')
        return redirect(to = "index")    