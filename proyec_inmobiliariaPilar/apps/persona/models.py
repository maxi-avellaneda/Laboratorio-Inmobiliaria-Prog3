from django.db import models

# Create your models here.

class Persona(models.Model):
    #cod_persona=models.IntegerField(unique=True)
    
    provincia=models.CharField(max_length=20)
    localidad=models.CharField(max_length=20)
    barrio=models.CharField(max_length=20)
    calle=models.CharField(max_length=20)
    numero=models.CharField(max_length=5)
    telefono=models.CharField(max_length=13)
    mail=models.EmailField(max_length=30, unique=True)
    fecha_alta=models.DateTimeField(auto_now_add=True)
    fecha_modificacion=models.DateTimeField(auto_now=True)
    desc_per=models.CharField(max_length=8)

    def __str__(self):
        if PersonaFisica.objects.filter(pk = self.pk).exists():
            persona = PersonaFisica.objects.get(pk = self.pk)
            return '{0},{1} -- {2}'.format(persona.nombre, persona.apellido, persona.cuil)
        if PersonaJuridica.objects.filter(pk = self.pk).exists():
            persona = PersonaJuridica.objects.get(pk = self.pk)
            return '{0} -- {1}'.format(persona.razon_social, persona.cuit)

class PersonaFisica(Persona):
    #CAMPOS PROPIOS DEL MODELO PERSONAFISICA 
    nombre=models.CharField(max_length=50)
    apellido = models.CharField(max_length=40)
    cuil=models.CharField(max_length=11,unique=True)

    def __str__(self):
        return '{0} -- {1}'.format(self.nombre, self.apellido)


class PersonaJuridica(Persona):
    #CAMPOS PROPIOS DEL MODELO PERSONAJURIDICA
    razon_social=models.CharField(max_length=50)
    cuit=models.CharField(max_length=11,unique=True)
    
    def __str__(self):
        return '{0} -- {1}'.format(self.razon_social, self.cuit)