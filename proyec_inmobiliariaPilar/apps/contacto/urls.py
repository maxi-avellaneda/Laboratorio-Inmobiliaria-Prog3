from django.urls import path
from .views import contacto,mail

urlpatterns = [
    path('alquilar/', contacto,name='contacto'),
    path('mailEnviado/',mail, name='mail'),
    
]