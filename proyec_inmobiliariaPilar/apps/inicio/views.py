from django.shortcuts import render
from apps.propiedad.models import Propiedad,Oferta

# Create your views here.

def Home(request):
    propofertas=Oferta.objects.all()
    return render(request, 'inicio/home.html',{'propofertas':propofertas})


    