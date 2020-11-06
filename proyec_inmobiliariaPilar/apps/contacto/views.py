from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contacto(request):

    return render(request,"contacto/contacto.html")


def mail(request):

    if request.method == 'POST':

        asunto = request.POST["asunto"]
        mensaje = request.POST["mensaje"] + "\n mail del cliente: (" + request.POST["email"] + ")"
        mail_from = settings.EMAIL_HOST_USER
        mail_receptor = ["programacion3django@gmail.com"] 

        send_mail(asunto,mensaje,mail_from,mail_receptor)

        return render(request,"contacto/mail_enviado.html")

    return render(request,"contacto/contacto.html")