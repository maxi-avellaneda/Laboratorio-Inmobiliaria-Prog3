from django.db import models
from apps.propiedad.models import Propiedad, Persona

# Create your models here.

class PropietarioPropiedad(models.Model):
    estados=(
        ('5','5%'),
        ('10','10%'),
        ('15','15%'),
        ('20','20%'),
        ('25','25%'),
        ('30','30%'),
    )

    propiedad=models.OneToOneField(Propiedad,on_delete=models.CASCADE, unique=True)
    propietario=models.ForeignKey(Persona,on_delete=models.CASCADE)
    condiciones = models.TextField()
    comision = models.CharField(max_length=5 ,choices=estados)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_alta=models.DateTimeField(auto_now_add=True)
    cancelacion = models.BooleanField(default=False)
    fecha_cancelacion = models.DateField(blank=True, null=True)

class InquilinoPropiedad(models.Model):
    propiedad=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    inquilino=models.ForeignKey(Persona,on_delete=models.CASCADE)
    fecha_alta=models.DateTimeField(auto_now_add=True)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    cant_personas=models.IntegerField()
    importe_total=models.DecimalField(max_digits=10,decimal_places=2)
    cancelacion = models.BooleanField(default=False)
    fecha_cancelacion = models.DateField(blank=True, null=True)
