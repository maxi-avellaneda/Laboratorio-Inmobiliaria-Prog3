from django.db import models
from apps.propiedad.models import Propiedad, Persona

# Create your models here.

class PropietarioPropiedad(models.Model):
    propiedad=models.OneToOneField(Propiedad,on_delete=models.CASCADE, unique=True)
    propietario=models.ForeignKey(Persona,on_delete=models.CASCADE)
    escritura=models.CharField(max_length=300)
    autorizacion_poder=models.CharField(max_length=150)
    fecha_alta=models.DateTimeField(auto_now_add=True)

class InquilinoPropiedad(models.Model):
    propiedad=models.OneToOneField(Propiedad,on_delete=models.CASCADE)
    inquilino=models.ForeignKey(Persona,on_delete=models.CASCADE)
    fecha_alta=models.DateTimeField(auto_now_add=True)
    vigencia_alquiler=models.DateField()
    cant_personas=models.IntegerField()
    importe_total=models.DecimalField(max_digits=10,decimal_places=2)
    importe_senia=models.DecimalField(max_digits=10,decimal_places=2)