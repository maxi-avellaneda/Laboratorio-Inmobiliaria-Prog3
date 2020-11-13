from django.db import models
from apps.persona.models import Persona

# Create your models here.

class Propiedad(models.Model):
    opc_tipo_alquiler=(
        ('DIARIO','Diario'),
        ('SEMANAL','Semanal'),
        ('MENSUAL','Mensual'),
    )
    zonas=(
        ('NORTE','Norte'),
        ('SUR','Sur'),
        ('ESTE','Este'),
        ('OESTE','Oeste'),
    )
    estados=(
        ('DISPONIBLE','Disponible'),
        ('OCUPADO','Ocupado'),
        ('EN MANTENIMIENTO','En Mantenimiento'),
    )
    mts=models.CharField(max_length=20)
    mts_semicubiertos=models.CharField(max_length=10)
    capacidad=models.IntegerField()
    cant_ambientes=models.IntegerField()
    cochera=models.BooleanField()
    capacidad_cochera=models.IntegerField(blank=True, null=True)
    cant_banios=models.IntegerField()
    permite_cancelacion=models.BooleanField()
    tipo_alquiler=models.CharField(max_length=7,choices=opc_tipo_alquiler)
    fecha_alta=models.DateTimeField(auto_now_add=True)
    precio=models.IntegerField()
    desc_prop=models.TextField()
    imagen=models.ImageField(upload_to='propiedad')
    tipo_propiedad=models.CharField(max_length=15, blank=False, null=False)
    estado_actual=models.CharField(max_length=16, choices=estados, default='disponible')
    zona=models.CharField(max_length=20,choices=zonas)


    def __str__(self):
        return 'Codigo Propiedad= %s   Tipo Alquiler= %s ' %(self.pk,self.tipo_alquiler)

class PropiedadCasa(Propiedad):
    #tipo_propiedad = 'casa'
    opc=(
        ('SI','Si'),
        ('NO','No'),
    )
    patio=models.CharField(max_length=2,choices=opc)
    pileta=models.CharField(max_length=2,choices=opc)
    terraza=models.CharField(max_length=2,choices=opc)

class PropiedadDepto(Propiedad):
    opc=(
        ('SI','Si'),
        ('NO','No'),
    )
    #prop_depto=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    #tipo_propiedad=models.CharField(max_length=15, default='departamento', editable=False)
    frente=models.CharField(max_length=2,choices=opc)
    contrafrente=models.CharField(max_length=2,choices=opc)
    espacios_comunes=models.CharField(max_length=2,choices=opc)

class PropiedadHabitacion(Propiedad):
    opc=(
        ('SI','Si'),
        ('NO','No'),
    )
    #prop_hab=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    #tipo_propiedad=models.CharField(max_length=15, default='habitacion', editable=False)
    banio_individual=models.CharField(max_length=2,choices=opc)

class Oferta(models.Model):
    
    propiedad=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    cod_oferta=models.CharField(unique=True,max_length=5)
    permite_cancelacion=models.BooleanField()
    #periodo_vigencia=models.CharField(max_length=5)
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField()
    fecha_solicitud=models.DateTimeField(auto_now_add=True)

class Estado(models.Model):

    propiedad=models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    fec_inicio=models.DateField(auto_now_add=True)
    fec_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20)
    band = models.BooleanField()

class FiltrarPropiedad(models.Model):
    zonas=(
        ('NORTE','Norte'),
        ('SUR','Sur'),
        ('ESTE','Este'),
        ('OESTE','Oeste'),
    )
    estados=(
        ('DISPONIBLE','Disponible'),
        ('OCUPADO','Ocupado'),
        ('EN MANTENIMIENTO','En Mantenimiento'),
    )
    opc=(
        ('CASA','Casa'),
        ('DEPARTAMENTO','Departamento'),
        ('HABITACION','Habitacion'),
    )
    condicion = models.CharField(max_length=20,choices=estados, null=True, blank=True)
    tipo_propiedad = models.CharField(max_length=15,choices=opc, null=True, blank=True)
    zona = models.CharField(max_length=10 ,choices=zonas, null=True, blank=True)