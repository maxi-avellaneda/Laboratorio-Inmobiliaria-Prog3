from django.db import models
from apps.persona.models import Persona

# Create your models here.

class Propiedad(models.Model):
    opc_tipo_alquiler=(
        ('diario','Diario'),
        ('semanal','Semanal'),
        ('mensual','Mensual'),
    )
    zonas=(
        ('norte','Norte'),
        ('sur','Sur'),
        ('este','Este'),
        ('oeste','Oeste'),
    )
    estados=(
        ('ocupado','Ocupado'),
        ('disponible','Disponible'),
        ('en mantenimiento','En Mantenimiento'),
    )
    mts=models.CharField(max_length=20)
    mts_semicubiertos=models.CharField(max_length=10)
    capacidad=models.IntegerField()
    cant_ambientes=models.IntegerField()
    cochera=models.BooleanField()
    capacidad_cochera=models.IntegerField(blank=True)
    cant_banios=models.IntegerField()
    permite_cancelacion=models.BooleanField()
    tipo_alquiler=models.CharField(max_length=7,choices=opc_tipo_alquiler)
    fecha_alta=models.DateTimeField(auto_now_add=True)
    precio=models.IntegerField()
    desc_prop=models.TextField()
    imagen=models.ImageField(upload_to='propiedad')
    tipo_propiedad=models.CharField(max_length=15, blank=False, null=False)
    estado=models.CharField(max_length=16, choices=estados, default='disponible')
    zona=models.CharField(max_length=20,choices=zonas)


    def __str__(self):
        return 'Codigo Propiedad= %s   Tipo Alquiler= %s ' %(self.pk,self.tipo_alquiler)

class PropiedadCasa(Propiedad):
    #tipo_propiedad = 'casa'
    opc=(
        ('si','Si'),
        ('no','No'),
    )
    patio=models.CharField(max_length=2,choices=opc)
    pileta=models.CharField(max_length=2,choices=opc)
    terraza=models.CharField(max_length=2,choices=opc)

class PropiedadDepto(Propiedad):
    opc=(
        ('si','Si'),
        ('no','No'),
    )
    #prop_depto=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    #tipo_propiedad=models.CharField(max_length=15, default='departamento', editable=False)
    frente=models.CharField(max_length=2,choices=opc)
    contrafrente=models.CharField(max_length=2,choices=opc)
    espacios_comunes=models.CharField(max_length=2,choices=opc)

class PropiedadHabitacion(Propiedad):
    opc=(
        ('si','Si'),
        ('no','No'),
    )
    #prop_hab=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    #tipo_propiedad=models.CharField(max_length=15, default='habitacion', editable=False)
    banio_individual=models.CharField(max_length=2,choices=opc)

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