from django.db import models
from apps.persona.models import Persona

# Create your models here.

class Propiedad(models.Model):
    opc_tipo_alquiler=(
        ('diario','Diario'),
        ('semanal','Semanal'),
        ('mensual','Mensual'),
    )
    cod_propiedad=models.IntegerField(unique=True)
    mts=models.CharField(max_length=20)
    mts_semicubiertos=models.CharField(max_length=20)
    capacidad=models.IntegerField()
    cant_ambientes=models.IntegerField()
    cochera=models.BooleanField()
    capacidad_cochera=models.IntegerField(blank=True)
    cant_banios=models.IntegerField()
    permite_cancelacion=models.BooleanField()
    tipo_alquiler=models.CharField(max_length=7,choices=opc_tipo_alquiler)
    fecha_alta=models.DateTimeField(auto_now_add=True)

class PropiedadCasa(Propiedad):
    opc=(
        ('si','Si'),
        ('no','No'),
    )
    #prop_casa=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    tipo_propiedad=models.CharField(default='casa',max_length=5)
    patio=models.CharField(max_length=2,choices=opc)
    pileta=models.CharField(max_length=2,choices=opc)
    terraza=models.CharField(max_length=2,choices=opc)

class PropiedadDepto(Propiedad):
    opc=(
        ('si','Si'),
        ('no','No'),
    )
    #prop_depto=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    tipo_propiedad=models.CharField(default='departamento',max_length=12)
    frente=models.CharField(max_length=2,choices=opc)
    contrafrente=models.CharField(max_length=2,choices=opc)
    espacios_comunes=models.CharField(max_length=2,choices=opc)

class PropiedadHabitacion(Propiedad):
    opc=(
        ('si','Si'),
        ('no','No'),
    )
    #prop_hab=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    tipo_propiedad=models.CharField(default='habitacion',max_length=10)
    banio_individual=models.CharField(max_length=2,choices=opc)

class Zona(models.Model):
    propiedad=models.ForeignKey(Propiedad,on_delete=models.CASCADE)
    opc_cod=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    )
    opc_desc=(
        ('norte','Norte'),
        ('sur','Sur'),
        ('este','Este'),
        ('oeste','Oeste'),
    )
    cod_zona=models.CharField(max_length=1,choices=opc_cod)
    desc_zona=models.CharField(max_length=20,choices=opc_desc)


class EstadoPropiedad(models.Model):
    opc_estado=(
        ('ocupado','Ocupado'),
        ('disponible','Disponible'),
        ('en mantenimiento','En Mantenimiento'),
    )
    propiedad=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    desc_estado=models.CharField(max_length=15)
    #faltan mas campos, que son relacionados a datos-estadisticas en cuanto a rangos de tiempos
    


class Oferta(models.Model):
    
    propiedad=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    cod_oferta=models.CharField(unique=True,max_length=5)
    permite_cancelacion=models.BooleanField()
    periodo_vigencia=models.CharField(max_length=5)
    fecha_solicitud=models.DateTimeField(auto_now_add=True)

class PropietarioPropiedad(models.Model):
    propiedad=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    propietario=models.OneToOneField(Persona,on_delete=models.CASCADE)
    escritura=models.CharField(max_length=300)
    autorizacion_poder=models.CharField(max_length=150)
    fecha_alta=models.DateTimeField(auto_now_add=True)

class InquilinoPropiedad(models.Model):
    propiedad=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    inquilino=models.OneToOneField(Persona,on_delete=models.CASCADE)
    vigencia_alquiler=models.CharField(max_length=10)
    cant_personas=models.IntegerField()
    importe_total=models.DecimalField(max_digits=10,decimal_places=2)
    importe_senia=models.DecimalField(max_digits=10,decimal_places=2)