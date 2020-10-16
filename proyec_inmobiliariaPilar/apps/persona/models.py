from django.db import models

# Create your models here.

class Persona(models.Model):
    cod_persona=models.IntegerField(unique=True)
    
    provincia=models.CharField(max_length=20)
    localidad=models.CharField(max_length=20)
    barrio=models.CharField(max_length=20)
    calle=models.CharField(max_length=20)
    numero=models.CharField(max_length=5)
    telefono=models.CharField(max_length=13)
    mail=models.CharField(max_length=40)
    fecha_alta=models.DateTimeField(auto_now_add=True)
    fecha_modificacion=models.DateTimeField(auto_now=True)

class PersonaFisica(Persona):
    #CAMPOS PROPIOS DEL MODELO PERSONAFISICA 
    nombre_apellido=models.CharField(max_length=50)
    cuil=models.CharField(max_length=11,unique=True)
    desc_per=models.CharField(default='fisica',max_length=6)


class PersonaJuridica(Persona):
    #CAMPOS PROPIOS DEL MODELO PERSONAJURIDICA
    razon_social=models.CharField(max_length=50)
    cuit=models.CharField(max_length=11,unique=True)
    desc_per=models.CharField(default='juridica',max_length=8)