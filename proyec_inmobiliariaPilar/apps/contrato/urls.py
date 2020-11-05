from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.contrato import views

urlpatterns=[
    path('nuevo_contratoPropietario/', views.NuevoContrato, name='nuevo_contrato_propietario'),
    path('nuevo_contratoInquilino/', views.NuevoContrato, name='nuevo_contrato_inquilino'),
    path('listado_contratos/', views.ListadoContrato, name='listado_contratos'),
    path('modificar_contrato/<id>/', views.ModificarContrato, name='modificar_contrato'),
    path('eliminar_contrato/<id>/', views.EliminarContrato, name='eliminar_contrato'),
]