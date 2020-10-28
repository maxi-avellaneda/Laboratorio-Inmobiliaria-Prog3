from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.persona import views

urlpatterns=[
    path('nueva-persona-fisica/', views.Nueva_Persona_Fisica, name='nueva_persona_fisica'),
    path('nueva-persona-juridica/', views.Nueva_Persona_Juridica, name='nueva_persona_juridica'),
    path('listado-personas/', views.Listado_Personas, name='listado_personas'),
    path('modificar-persona/<id>/', views.Modificar_Persona, name='modificar_persona'),
    path('eliminar-persona/<id>/', views.Eliminar_Persona, name='eliminar_persona'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)