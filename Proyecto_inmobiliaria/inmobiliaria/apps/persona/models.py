from django.db import models

# Create your models here.

class Persona(models.Model):
    opc_tipoPersona=(
        ('fisica','F'),
        ('juridica','J'),
    )
    cod_persona=models.DecimalField(unique=True,max_digits=2,decimal_places=0)
    
    tipo_persona=models.CharField(max_length=8,choices=opc_tipoPersona)
    provincia=models.CharField(max_length=20)
    localidad=models.CharField(max_length=20)
    barrio=models.CharField(max_length=20)
    calle=models.CharField(max_length=20)
    numero=models.CharField(max_length=5)
    telefono=models.CharField(max_length=13)
    mail=models.CharField(max_length=40)
    fecha_alta=models.DateTimeField(auto_now_add=True)
    fecha_modificacion=models.DateTimeField(auto_now=True)

class PersonaFisica(models.Model):
    #defino una relacion uno a uno entre Persona y PersonaFisica
    persona=models.OneToOneField(Persona,on_delete=models.CASCADE)
    #CAMPOS PROPIOS DEL MODELO PERSONAFISICA 
    nombre_apellido=models.CharField(max_length=50)
    cuil=models.CharField(max_length=11,unique=True)
    #desc_per=models.CharField(default='fisica')


class PersonaJuridica(models.Model):
    #defino una relacion uno a uno entre Persona y PersonaJuridica
    persona=models.OneToOneField(Persona,on_delete=models.CASCADE)
    #CAMPOS PROPIOS DEL MODELO PERSONAJURIDICA
    razon_social=models.CharField(max_length=50)
    cuit=models.CharField(max_length=11,unique=True)
    #desc_per=models.CharField(default='juridica')

    


