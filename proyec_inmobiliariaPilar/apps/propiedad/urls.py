from django.urls import path
from .views import ListadoPropiedades,buscarPropiedades

urlpatterns = [
    path('listadoPropiedades/',ListadoPropiedades,name='listado_propiedades'),
    path('buscar/',buscarPropiedades,name='buscar_propiedades'),
]