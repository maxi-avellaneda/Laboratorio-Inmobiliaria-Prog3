from django.urls import path
from .views import ListadoPropiedades,buscarPropiedades,paginaBuscar

urlpatterns = [
    path('listadoPropiedades/', ListadoPropiedades,name='listado_propiedades'),
    path('busqueda/', paginaBuscar, name='busqueda'),
    path('busqueda/buscar/', buscarPropiedades,name='buscar_propiedades'),
]