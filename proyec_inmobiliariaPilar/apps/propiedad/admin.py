from django.contrib import admin
from apps.propiedad.models import Propiedad,PropiedadCasa,PropiedadDepto,PropiedadHabitacion,Zona,EstadoPropiedad,Oferta,PropietarioPropiedad,InquilinoPropiedad

# Register your models here.

class PropiedadesAdmin(admin.ModelAdmin):
    list_display=('cod_propiedad','tipo_alquiler','mts','capacidad')
    search_fields=('cod_propiedad','tipo_alquiler')

admin.site.register(Propiedad,PropiedadesAdmin)
admin.site.register(PropiedadCasa)
admin.site.register(PropiedadDepto)
admin.site.register(PropiedadHabitacion)
admin.site.register(Zona)
admin.site.register(EstadoPropiedad)
admin.site.register(Oferta)
admin.site.register(PropietarioPropiedad)
admin.site.register(InquilinoPropiedad)