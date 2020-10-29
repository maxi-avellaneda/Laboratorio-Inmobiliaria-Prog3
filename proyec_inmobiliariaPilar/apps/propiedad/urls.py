from django.urls import path
from apps.propiedad import views

urlpatterns = [
    path('casa/',views.NuevaPropiedadCasa, name='nueva_propiedad_casa'),
    path('dpto/',views.NuevaPropiedadDpto, name='nueva_propiedad_dpto'),
    path('habitacion/',views.NuevaPropiedadHabitacion, name='nueva_propiedad_habitacion'),
]