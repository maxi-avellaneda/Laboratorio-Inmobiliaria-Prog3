from django.urls import path
from .views import buscarPropiedades,paginaBuscar

urlpatterns = [
    path('', paginaBuscar, name='busqueda'),
    path('buscar/', buscarPropiedades,name='buscar_propiedades'),
]