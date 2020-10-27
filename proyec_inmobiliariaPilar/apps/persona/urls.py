from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.persona import views

urlpatterns=[
    path('nueva-persona/', views.Nueva_persona, name='nueva_persona'),
    path('', views.Home , name='home'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)