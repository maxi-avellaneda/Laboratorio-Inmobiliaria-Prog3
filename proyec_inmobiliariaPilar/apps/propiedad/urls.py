from django.urls import path
from apps.propiedad import views

urlpatterns = [
    path('listadoPropiedades/', views.ListadoPropiedades,name='listado_propiedades'),
    path('casa/',views.NuevaPropiedadCasa, name='nueva_casa'),
    path('dpto/',views.NuevaPropiedadDpto, name='nuevo_dpto'),
    path('habitacion/',views.NuevaPropiedadHabitacion, name='nueva_habitacion'),
    path('modificar/<id>/',views.ModificarPropiedad, name='modificar_propiedad'),
    path('eliminar/<id>/',views.EliminarPropiedad, name='eliminar_propiedad'),
    path('nuevaOferta/',views.NuevaOferta, name='nueva_oferta'),
    path('Ofertas/',views.MostrarOfertas, name='mostrar_ofertas'),
    path('listadoOfertas/',views.ListarOfertas, name='listado_ofertas'),
    path('modificarOferta/<id>/',views.ModificarOferta, name='modificar_oferta'),
    path('eliminarOferta/<id>/',views.EliminarOferta, name='eliminar_oferta'),
    path('detallesPropiedad/',views.detallePropiedad, name='detalles_propiedad'),
]