from django.shortcuts import render
from apps.propiedad.models import Propiedad,PropiedadCasa,PropiedadDepto,PropiedadHabitacion

# Create your views here.

def ListadoPropiedades(request):
    propiedades= Propiedad.objects.all()
    return render(request,'busqueda/lista_propiedades.html',{'propiedades':propiedades})

def paginaBuscar(request):
    return render(request,'busqueda/buscar.html')

def buscarPropiedades(request):
    idpro=request.GET["idpro"]
    tipo_propiedad=request.GET["tipo_propiedad"]
    capacidad=request.GET["capacidad"]
    precio1=request.GET["precio1"]
    precio2=request.GET["precio2"]
    dormitorios=request.GET["dormitorios"]
    cant_banios=request.GET["cant_banios"]
    zona=request.GET["zona"]
    

    #BUSQUEDAS POR DOS CAMPOS

    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna":
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,propiedadcasa__tipo_propiedad=tipo_propiedad)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,propiedaddepto__tipo_propiedad=tipo_propiedad)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,propiedadhabitacion__tipo_propiedad=tipo_propiedad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["idpro"] and request.GET["capacidad"]:
        
        propiedades=Propiedad.objects.filter(id=idpro,capacidad=capacidad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["idpro"] and request.GET["precio1"]:
        
        propiedades=Propiedad.objects.filter(id=idpro,precio=precio1)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["idpro"] and request.GET["precio2"]:
        
        propiedades=Propiedad.objects.filter(id=idpro,precio=precio2)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["idpro"] and request.GET["precio1"] and request.GET["precio2"]:
        
        propiedades=Propiedad.objects.filter(id=idpro,precio__range=[precio1,precio2])    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["idpro"] and request.GET["dormitorios"]:
        
        propiedades=Propiedad.objects.filter(id=idpro,cant_ambientes=dormitorios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["idpro"] and request.GET["cant_banios"] != '':
        
        propiedades=Propiedad.objects.filter(id=idpro,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})
    
    if request.GET["idpro"] and request.GET["zona"]:
        
        propiedades=Propiedad.objects.filter(id=idpro,zona__desc_zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"]:
        
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(propiedadcasa__tipo_propiedad=tipo_propiedad,capacidad=capacidad)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(propiedaddepto__tipo_propiedad=tipo_propiedad,capacidad=capacidad)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(propiedadhabitacion__tipo_propiedad=tipo_propiedad,capacidad=capacidad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["precio1"]:
        
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(propiedadcasa__tipo_propiedad=tipo_propiedad,precio=precio1)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(propiedaddepto__tipo_propiedad=tipo_propiedad,precio=precio1)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(propiedadhabitacion__tipo_propiedad=tipo_propiedad,precio=precio1)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["precio2"]:
        
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(propiedadcasa__tipo_propiedad=tipo_propiedad,precio=precio2)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(propiedaddepto__tipo_propiedad=tipo_propiedad,precio=precio2)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(propiedadhabitacion__tipo_propiedad=tipo_propiedad,precio=precio2)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["precio1"] and request.GET["precio2"]:
        
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(propiedadcasa__tipo_propiedad=tipo_propiedad,precio__range=(precio1,precio2))
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(propiedaddepto__tipo_propiedad=tipo_propiedad,precio__range=[precio1,precio2])
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(propiedadhabitacion__tipo_propiedad=tipo_propiedad,precio__range=[precio1,precio2])    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["dormitorios"]:
        
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(propiedadcasa__tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(propiedaddepto__tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(propiedadhabitacion__tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["cant_banios"] != '':
        
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(propiedadcasa__tipo_propiedad=tipo_propiedad,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(propiedaddepto__tipo_propiedad=tipo_propiedad,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(propiedadhabitacion__tipo_propiedad=tipo_propiedad,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["zona"] != '':
        
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(propiedadcasa__tipo_propiedad=tipo_propiedad,zona__desc_zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(propiedaddepto__tipo_propiedad=tipo_propiedad,zona__desc_zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(propiedadhabitacion__tipo_propiedad=tipo_propiedad,zona__desc_zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})



        

    #BUSQUEDAS POR UN CAMPO

    if request.GET["idpro"]:

        propiedades=Propiedad.objects.filter(id=idpro)
        #zonaprueba=Propiedad.objects.filter(zona__desc_zona=zona)

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["tipo_propiedad"]:
        if tipo_propiedad=='casa':
            propiedades=PropiedadCasa.objects.all()
            return render(request,'busqueda/resultados_busqueda.html',
            {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
            'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})
        if tipo_propiedad=='departamento':
            propiedades=PropiedadDepto.objects.all()
            return render(request,'busqueda/resultados_busqueda.html',
            {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
            'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2}) 
        if tipo_propiedad=='habitacion':
            propiedades=PropiedadHabitacion.objects.all()
            return render(request,'busqueda/resultados_busqueda.html',
            {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
            'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["capacidad"]:
        propiedades=Propiedad.objects.filter(capacidad=capacidad)
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})
    
    if request.GET["precio1"] and request.GET["precio2"]:
        propiedades=Propiedad.objects.filter(precio__range=[precio1,precio2])
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["precio1"] :
        propiedades=Propiedad.objects.filter(precio=precio1)
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})
    if request.GET["precio2"] :
        propiedades=Propiedad.objects.filter(precio=precio2)
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    

    if request.GET["dormitorios"]:
        propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios)
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})

    if request.GET["cant_banios"]:
        propiedades=Propiedad.objects.filter(cant_banios=cant_banios)
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2}) 

    if request.GET["zona"]:
        propiedades=Propiedad.objects.filter(zona__desc_zona=zona)
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1,'precio2':precio2})