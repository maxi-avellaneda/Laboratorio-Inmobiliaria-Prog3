from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from .models import Propiedad, PropiedadCasa, PropiedadDepto, PropiedadHabitacion, Oferta, Estado
from .forms import PropiedadCasaForm,PropiedadDptoForm,PropiedadHabitacionForm, OfertaForm, EstadoForm

# Create your views here.

def ListadoPropiedades(request):
    propiedades= Propiedad.objects.all()
    return render(request,'propiedad/lista_propiedades.html',{'propiedades':propiedades})

def detallePropiedad(request,id):
    pro = Propiedad.objects.get(pk=id)

    
    return render(request,'propiedad/detalles_propiedad.html',{'pro':pro})


def NuevaPropiedadCasa(request):
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
            Estado.objects.create(
            propiedad = casa, 
            fec_inicio= casa.fecha_alta, 
            fec_fin='2000-10-10',
            estado=casa.estado_actual,
            band=True)
            
    return render(request, 'propiedad/nueva_propiedad.html', data)

def NuevaPropiedadDpto(request):
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
            Estado.objects.create(
            propiedad = dpto, 
            fec_inicio= dpto.fecha_alta, 
            fec_fin='2000-10-10',
            estado=dpto.estado_actual,
            band=True)
            data["mensaje"]= 'guardado con exito'

    return render(request, 'propiedad/nueva_propiedad.html', data )

def NuevaPropiedadHabitacion(request):
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
            dpto = Propiedad.objects.last()
            Estado.objects.create(
            propiedad = dpto, 
            fec_inicio= dpto.fecha_alta, 
            fec_fin='2000-10-10',
            estado=dpto.estado_actual,
            band=True)
            data["mensaje"]= 'guardado con exito'

    return render(request, 'propiedad/nueva_propiedad.html', data)

def ModificarPropiedad(request,id):
    propiedad = Propiedad.objects.get(pk=id)
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
                    estado_anterior = Estado.objects.filter(propiedad=casa).last()
                    estado_anterior.fec_fin = datetime.now()
                    estado_anterior.band = False
                    estado_anterior.save()
                    Estado.objects.create(propiedad=casa,fec_inicio=datetime.now(), fec_fin='2020-01-01', estado=casa.estado_actual,band=True)

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
                    estado_anterior = Estado.objects.filter(propiedad=dpto).last()
                    estado_anterior.fec_fin = datetime.now()
                    estado_anterior.band = False
                    estado_anterior.save()
                    Estado.objects.create(propiedad=dpto,fec_inicio=datetime.now(), fec_fin='2020-01-01', estado=dpto.estado_actual,band=True)


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
                    estado_anterior = Estado.objects.filter(propiedad=habitacion).last()
                    estado_anterior.fec_fin = datetime.now()
                    estado_anterior.band = False
                    estado_anterior.save()
                    Estado.objects.create(propiedad=habitacion,fec_inicio=datetime.now(), fec_fin='2020-01-01', estado=habitacion.estado_actual,band=True)

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

def NuevaOferta(request):
    data = {
        "form" : OfertaForm()
    }
    if request.method == 'POST':
        f = OfertaForm(request.POST)
        if f.is_valid():
            f.save()
            data["mensaje"] = 'guardado con exito'

    return render(request, 'propiedad/nueva_propiedad.html', data)

def ModificarOferta(request,id):
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

def EliminarOferta(request,id):
    if Oferta.objects.filter(pk = id).exists():
        oferta = Oferta.objects.get(pk = id)
        oferta.delete()
    return redirect(to='listado_ofertas')


def MostrarOfertas(request):
    ofertas = Oferta.objects.all()
    return render(request,'oferta/ofertas.html', {"ofertas": ofertas})

def ListarOfertas(request):
    ofertas = Oferta.objects.all()
    return render(request,'oferta/listado_ofertas.html', {"ofertas": ofertas})