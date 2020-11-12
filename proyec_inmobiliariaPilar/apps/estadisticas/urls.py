from django.urls import path
from .views import zonaMenorAlquiler,porcentajeOcupacion,preferencia_zona_tipoPropiedad,preferencia_zona_tipoAlquiler,tiempoSinAlquilar

urlpatterns = [
    path('zona_menosAlquiler/', zonaMenorAlquiler,name='zona_menorAlquiler'),
    path('porcentaje_ocupacion/', porcentajeOcupacion,name='porcentaje_ocupacion'),
    path('preferencia_zona_tipoPropiedad/', preferencia_zona_tipoPropiedad,name='preferencia_zona_tipoPropiedad'),
    path('preferencia_zona_tipoAlquiler/', preferencia_zona_tipoAlquiler,name='preferencia_zona_tipoAlquiler'),
    path('tiempoSinAlquilar/', tiempoSinAlquilar,name='tiempoSinAlquilar'),
]