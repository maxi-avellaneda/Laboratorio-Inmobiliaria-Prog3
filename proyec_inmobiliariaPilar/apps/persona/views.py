from django.shortcuts import render, HttpResponse, redirect
from .models import PersonaFisica
from .forms import PersonaFisicaForm

# Create your views here.

def Nueva_persona(request):
    data = {
        "form": PersonaFisicaForm()
    }

    if request.method == 'POST':
        print(request.POST)
        formulario = PersonaFisicaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data += {
                "mensaje": 'Guardado con exito'
            }
    
    return render(request, "base/nueva_persona.html", data)

def Home(request):
    return render(request, "base/home.html")