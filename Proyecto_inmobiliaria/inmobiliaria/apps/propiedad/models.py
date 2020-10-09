from django.db import models
from apps.persona.models import Persona

# Create your models here.

class Propiedad(models.Model):
    opc_tipo_prop=(
        ('casa','Casa'),
        ('departamento','Departamento'),
        ('habitacion','Habitacion'),
    )
    opc_tipo_alquiler=(
        ('diario','Diario'),
        ('semanal','Semanal'),
        ('mensual','Mensual'),
    )
    cod_propiedad=models.DecimalField(unique=True,max_digits=2,decimal_places=1)
    tipo_propiedad=models.CharField(max_length=12,choices=opc_tipo_prop)
    descrip_prop=models.CharField(max_length=100)
    fecha_alta=models.DateTimeField(auto_now_add=True)
    mts=models.CharField(max_length=5)
    mts_semicubiertos=models.CharField(max_length=5)
    capacidad=models.DecimalField(max_digits=2,decimal_places=2)
    cant_ambientes=models.DecimalField(max_digits=2,decimal_places=2)
    cochera=models.BooleanField()
    capacidad_cochera=models.DecimalField(max_digits=2,decimal_places=2,blank=True)
    cant_banios=models.DecimalField(max_digits=2,decimal_places=2)
    permite_cancelacion=models.BooleanField()
    tipo_alquiler=models.CharField(max_length=7,choices=opc_tipo_alquiler)

class PropiedadCasa(models.Model):
    opc=(
        ('si','Si'),
        ('no','No'),
    )
    prop_casa=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    patio=models.CharField(max_length=2,choices=opc)
    pileta=models.CharField(max_length=2,choices=opc)
    terraza=models.CharField(max_length=2,choices=opc)

class PropiedadDepto(models.Model):
    opc=(
        ('si','Si'),
        ('no','No'),
    )
    prop_depto=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    frente=models.CharField(max_length=2,choices=opc)
    contrafrente=models.CharField(max_length=2,choices=opc)
    espacios_comunes=models.CharField(max_length=2,choices=opc)

class PropiedadHabitacion(models.Model):
    opc=(
        ('si','Si'),
        ('no','No'),
    )
    prop_hab=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    banio_individual=models.CharField(max_length=2,choices=opc)

class PropiedadZona(models.Model):
    prop_zona=models.ForeignKey(Propiedad,on_delete=models.CASCADE)
    cod_zona=models.DecimalField(unique=True,max_digits=1,decimal_places=1)
    desc_zona=models.CharField(max_length=10)


class EstadoPropiedad(models.Model):
    opc_estado=(
        ('ocupado','Ocupado'),
        ('disponible','Disponible'),
        ('en mantenimiento','En Mantenimiento'),
    )
    estado_propiedad=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    desc_estado=models.CharField(max_length=15)


class PropiedadOferta(models.Model):
    
    prop_oferta=models.OneToOneField(EstadoPropiedad,on_delete=models.CASCADE)
    cod_oferta=models.DecimalField(unique=True,max_digits=3,decimal_places=1)
    permite_cancelacion=models.BooleanField()
    periodo_vigencia=models.CharField(max_length=5)
    fecha_solicitud=models.DateTimeField(auto_now_add=True)

class PropietarioPropiedad(models.Model):
    propiedad=models.ForeignKey(Propiedad,on_delete=models.CASCADE)
    propietario=models.ForeignKey(Persona,on_delete=models.CASCADE)
    fecha_alta=models.DateTimeField(auto_now_add=True)
    escritura=models.CharField(max_length=300)
    autorizacion_poder=models.CharField(max_length=150)

class InquilinoPropiedad(models.Model):
    propiedad=models.ForeignKey(Propiedad,on_delete=models.CASCADE)
    inquilino=models.ForeignKey(Persona,on_delete=models.CASCADE)
    vigencia_alquiler=models.CharField(max_length=10)
    cant_personas=models.DecimalField(max_digits=2,decimal_places=1)
    importe_total=models.DecimalField(max_digits=6,decimal_places=2)
    importe_senia=models.DecimalField(max_digits=3,decimal_places=2)