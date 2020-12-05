from datetime import date
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.propiedad.models import Propiedad,Estado
from apps.contrato.models import PropietarioPropiedad,InquilinoPropiedad


# Create your views here.

@login_required
def zonaMenorAlquiler(request):

    alquiladas_zonaNorte = InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Norte').count()
    alquiladas_zonaSur = InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Sur').count()
    alquiladas_zonaEste = InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Este').count()
    alquiladas_zonaOeste = InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Oeste').count()

    datos=[ alquiladas_zonaNorte , alquiladas_zonaSur , alquiladas_zonaEste , alquiladas_zonaOeste ]

    return render(request,'estadisticas/zona_menorAlquiler.html',{'datos':datos,
    'alquiladas_zonaNorte':alquiladas_zonaNorte,'alquiladas_zonaSur':alquiladas_zonaSur,
    'alquiladas_zonaEste':alquiladas_zonaEste,'alquiladas_zonaOeste':alquiladas_zonaOeste})

@login_required
def porcentajeOcupacion(request):

    total = Propiedad.objects.all().count()

    ocupadas= Propiedad.objects.filter(estado_actual__icontains='Ocupado').count()
    disponibles = Propiedad.objects.filter(estado_actual__icontains='Disponible').count()
    mantenimiento= Propiedad.objects.filter(estado_actual__icontains='En Mantenimiento').count()

    if total==0:
        total='NO HAY PROPIEDADES EN LA BD'
        porcentaje_ocupadas=0
        porcentaje_disponibles=0
        porcentaje_mantenimiento=0
    else:
        porcentaje_ocupadas = (ocupadas * 100) / total
        porcentaje_disponibles = (disponibles * 100) / total
        porcentaje_mantenimiento = (mantenimiento * 100) / total
    
    return render(request,'estadisticas/porcentaje_ocupacion.html',
    {'porcentaje_ocupadas':porcentaje_ocupadas,'porcentaje_disponibles':porcentaje_disponibles,
    'porcentaje_mantenimiento':porcentaje_mantenimiento,'total':total})

@login_required
def preferencia_zona_tipoPropiedad(request):

    alquiladas_zonaNorteYtipoCasa=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Norte',propiedad__tipo_propiedad__icontains='Casa').count()
    alquiladas_zonaNorteYtipoDepto=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Norte',propiedad__tipo_propiedad__icontains='Departamento').count()
    alquiladas_zonaNorteYtipoHabi=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Norte',propiedad__tipo_propiedad__icontains='Habitacion').count()

    alquiladas_zonaSurYtipoCasa=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Sur',propiedad__tipo_propiedad__icontains='Casa').count()
    alquiladas_zonaSurYtipoDepto=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Sur',propiedad__tipo_propiedad__icontains='Departamento').count()
    alquiladas_zonaSurYtipoHabi=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Sur',propiedad__tipo_propiedad__icontains='Habitacion').count()
    
    alquiladas_zonaEsteYtipoCasa=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Este',propiedad__tipo_propiedad__icontains='Casa').count()
    alquiladas_zonaEsteYtipoDepto=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Este',propiedad__tipo_propiedad__icontains='Departamento').count()
    alquiladas_zonaEsteYtipoHabi=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Este',propiedad__tipo_propiedad__icontains='Habitacion').count()

    alquiladas_zonaOesteYtipoCasa=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Oeste',propiedad__tipo_propiedad__icontains='Casa').count()
    alquiladas_zonaOesteYtipoDepto=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Oeste',propiedad__tipo_propiedad__icontains='Departamento').count()
    alquiladas_zonaOesteYtipoHabi=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Oeste',propiedad__tipo_propiedad__icontains='Habitacion').count()

    datosCasa = [alquiladas_zonaNorteYtipoCasa , alquiladas_zonaSurYtipoCasa , alquiladas_zonaEsteYtipoCasa , alquiladas_zonaOesteYtipoCasa]
    datosDepto = [alquiladas_zonaNorteYtipoDepto, alquiladas_zonaSurYtipoDepto , alquiladas_zonaEsteYtipoDepto , alquiladas_zonaOesteYtipoDepto]
    datosHabi = [alquiladas_zonaNorteYtipoHabi , alquiladas_zonaSurYtipoHabi , alquiladas_zonaEsteYtipoHabi , alquiladas_zonaOesteYtipoHabi]

    return render(request,'estadisticas/preferencia_zona_tipoPropiedad.html',
    {'alquiladas_zonaNorteYtipoCasa':alquiladas_zonaNorteYtipoCasa,
    'alquiladas_zonaNorteYtipoDepto':alquiladas_zonaNorteYtipoDepto,
    'alquiladas_zonaNorteYtipoHabi':alquiladas_zonaNorteYtipoHabi,
    'alquiladas_zonaSurYtipoCasa':alquiladas_zonaSurYtipoCasa,
    'alquiladas_zonaSurYtipoDepto':alquiladas_zonaSurYtipoDepto,
    'alquiladas_zonaSurYtipoHabi':alquiladas_zonaSurYtipoHabi,
    'alquiladas_zonaEsteYtipoCasa':alquiladas_zonaEsteYtipoCasa,
    'alquiladas_zonaEsteYtipoDepto':alquiladas_zonaEsteYtipoDepto,
    'alquiladas_zonaEsteYtipoHabi':alquiladas_zonaEsteYtipoHabi,
    'alquiladas_zonaOesteYtipoCasa':alquiladas_zonaOesteYtipoCasa,
    'alquiladas_zonaOesteYtipoDepto':alquiladas_zonaOesteYtipoDepto,
    'alquiladas_zonaOesteYtipoHabi':alquiladas_zonaOesteYtipoHabi,
    'datosCasa':datosCasa,'datosDepto':datosDepto,'datosHabi':datosHabi})

@login_required
def preferencia_zona_tipoAlquiler(request):

    alquiladas_zonaNorteYtipoDiario=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Norte',propiedad__tipo_alquiler__icontains='Diario').count()
    alquiladas_zonaNorteYtipoSemanal=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Norte',propiedad__tipo_alquiler__icontains='Semanal').count()
    alquiladas_zonaNorteYtipoMensual=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Norte',propiedad__tipo_alquiler__icontains='Mensual').count()

    alquiladas_zonaSurYtipoDiario=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Sur',propiedad__tipo_alquiler__icontains='Diario').count()
    alquiladas_zonaSurYtipoSemanal=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Sur',propiedad__tipo_alquiler__icontains='Semanal').count()
    alquiladas_zonaSurYtipoMensual=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Sur',propiedad__tipo_alquiler__icontains='Mensual').count()
    
    alquiladas_zonaEsteYtipoDiario=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Este',propiedad__tipo_alquiler__icontains='Diario').count()
    alquiladas_zonaEsteYtipoSemanal=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Este',propiedad__tipo_alquiler__icontains='Semanal').count()
    alquiladas_zonaEsteYtipoMensual=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Este',propiedad__tipo_alquiler__icontains='Mensual').count()

    alquiladas_zonaOesteYtipoDiario=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Oeste',propiedad__tipo_alquiler__icontains='Diario').count()
    alquiladas_zonaOesteYtipoSemanal=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Oeste',propiedad__tipo_alquiler__icontains='Semanal').count()
    alquiladas_zonaOesteYtipoMensual=InquilinoPropiedad.objects.filter(propiedad__zona__icontains='Oeste',propiedad__tipo_alquiler__icontains='Mensual').count()

    datosDiario = [alquiladas_zonaNorteYtipoDiario , alquiladas_zonaSurYtipoDiario , alquiladas_zonaEsteYtipoDiario , alquiladas_zonaOesteYtipoDiario]
    datosSemanal = [alquiladas_zonaNorteYtipoSemanal, alquiladas_zonaSurYtipoSemanal , alquiladas_zonaEsteYtipoSemanal , alquiladas_zonaOesteYtipoSemanal]
    datosMensual = [alquiladas_zonaNorteYtipoMensual , alquiladas_zonaSurYtipoMensual , alquiladas_zonaEsteYtipoMensual , alquiladas_zonaOesteYtipoMensual]

    return render(request,'estadisticas/preferencia_zona_tipoAlquiler.html',
    {'alquiladas_zonaNorteYtipoDiario':alquiladas_zonaNorteYtipoDiario,
    'alquiladas_zonaNorteYtipoSemanal':alquiladas_zonaNorteYtipoSemanal,
    'alquiladas_zonaNorteYtipoMensual':alquiladas_zonaNorteYtipoMensual,
    'alquiladas_zonaSurYtipoDiario':alquiladas_zonaSurYtipoDiario,
    'alquiladas_zonaSurYtipoSemanal':alquiladas_zonaSurYtipoSemanal,
    'alquiladas_zonaSurYtipoMensual':alquiladas_zonaSurYtipoMensual,
    'alquiladas_zonaEsteYtipoDiario':alquiladas_zonaEsteYtipoDiario,
    'alquiladas_zonaEsteYtipoSemanal':alquiladas_zonaEsteYtipoSemanal,
    'alquiladas_zonaEsteYtipoMensual':alquiladas_zonaEsteYtipoMensual,
    'alquiladas_zonaOesteYtipoDiario':alquiladas_zonaOesteYtipoDiario,
    'alquiladas_zonaOesteYtipoSemanal':alquiladas_zonaOesteYtipoSemanal,
    'alquiladas_zonaOesteYtipoMensual':alquiladas_zonaOesteYtipoMensual,
    'datosDiario':datosDiario,'datosSemanal':datosSemanal,'datosMensual':datosMensual})

@login_required
def tiempoSinAlquilar(request):

    sinAlquilar = Estado.objects.exclude(estado__icontains='OCUPADO')

    return render(request,'estadisticas/tiempoSinAlquilar.html',
    {'sinAlquilar':sinAlquilar})