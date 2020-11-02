from django.shortcuts import render, HttpResponse
from apps.propiedad.models import Propiedad,PropiedadCasa,PropiedadDepto,PropiedadHabitacion

# Create your views here.

def paginaBuscar(request):
    return render(request,'busqueda/buscar.html')

def buscarPropiedades(request):
    idpro=request.GET["idpro"]
    tipo_propiedad=request.GET["tipo_propiedad"]
    capacidad=request.GET["capacidad"]
    precio1=request.GET["precio1"]
    dormitorios=request.GET["dormitorios"]
    cant_banios=request.GET["cant_banios"]
    zona=request.GET["zona"]

    #SI TODOS LOS CAMPOS ESTAN VACIOS

    if request.GET["idpro"] == '' and request.GET["tipo_propiedad"] == "ninguna" and request.GET["capacidad"]=='' and request.GET["precio1"]==''  and request.GET["precio2"]==''  and request.GET["dormitorios"]==''  and request.GET["cant_banios"] =='' and request.GET["zona"] =='':
        return HttpResponse('VUELVA ATRAS Y RELLENE ALGUN CAMPO PARA PODER BUSCAR')

    #BUSQUEDAS QUE IMPLICAN TODOS LOS CAMPOS

    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["precio1"] and request.GET["dormitorios"] and request.GET["cant_banios"] !='' and request.GET["zona"] !='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,propiedadcasa__tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona__desc_zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,propiedaddepto__tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona__desc_zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,propiedadhabitacion__tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona__desc_zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    #BUSQUEDAS QUE IMPLICAN 6 CAMPOS

    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["precio1"] and request.GET["dormitorios"] and request.GET["cant_banios"] !='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["precio1"] and request.GET["dormitorios"]  and request.GET["zona"] !='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})
    
    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["precio1"] and request.GET["cant_banios"]  and request.GET["zona"] !='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["dormitorios"] and request.GET["cant_banios"]  and request.GET["zona"] !='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["precio1"] and request.GET["dormitorios"] and request.GET["cant_banios"]  and request.GET["zona"] !='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"] and request.GET["capacidad"]  and request.GET["precio1"] and request.GET["dormitorios"] and request.GET["cant_banios"]  and request.GET["zona"] !='':
       
        propiedades=Propiedad.objects.filter(id=idpro,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
           
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["tipo_propiedad"] and request.GET["capacidad"]  and request.GET["precio1"] and request.GET["dormitorios"] and request.GET["cant_banios"]  and request.GET["zona"] !='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    #BUSQUEDAS QUE IMPLICAN CINCO CAMPOS

    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["precio1"] and request.GET["dormitorios"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["precio1"] and request.GET["zona"]!='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["cant_banios"] and request.GET["zona"]!='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["dormitorios"] and request.GET["cant_banios"] and request.GET["zona"]!='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] and request.GET["precio1"]  and request.GET["dormitorios"] and request.GET["cant_banios"] and request.GET["zona"]!='':
            
        propiedades=Propiedad.objects.filter(id=idpro,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
               

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"] and request.GET["capacidad"]  and request.GET["dormitorios"] and request.GET["cant_banios"] and request.GET["zona"]!='':
                
        propiedades=Propiedad.objects.filter(id=idpro,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
            

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] and request.GET["capacidad"]  and request.GET["precio1"] and request.GET["cant_banios"] and request.GET["zona"]!='':
                
        propiedades=Propiedad.objects.filter(id=idpro,capacidad=capacidad,precio=precio1,cant_banios=cant_banios,zona=zona)
            

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"] and request.GET["capacidad"]  and request.GET["precio1"] and request.GET["dormitorios"] and request.GET["zona"]!='':
                
        propiedades=Propiedad.objects.filter(id=idpro,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,zona=zona)
            

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] and request.GET["capacidad"]  and request.GET["precio1"] and request.GET["dormitorios"] and request.GET["cant_banios"]!='':
                
        propiedades=Propiedad.objects.filter(id=idpro,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)
            

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["precio1"] and request.GET["cant_banios"] and request.GET["zona"]!='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["precio1"] and request.GET["dormitorios"] and request.GET["zona"]!='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["precio1"] and request.GET["dormitorios"] and request.GET["cant_banios"]!='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["dormitorios"] and request.GET["zona"]!='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["dormitorios"] and request.GET["cant_banios"]!='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["precio1"] and request.GET["cant_banios"]!='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    #tipo de propiedad fija

 
    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["precio1"] and request.GET["dormitorios"] and request.GET["cant_banios"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["dormitorios"] and request.GET["cant_banios"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["precio1"] and request.GET["cant_banios"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["precio1"] and request.GET["dormitorios"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["precio1"] and request.GET["dormitorios"] and request.GET["cant_banios"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    #capacidad

    if  request.GET["capacidad"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["dormitorios"] and request.GET["cant_banios"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(capacidad=capacidad,tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(capacidad=capacidad,tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(capacidad=capacidad,tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if  request.GET["capacidad"] and request.GET["precio1"]  and  request.GET["dormitorios"] and request.GET["cant_banios"] and request.GET["zona"]:
        
        propiedades=Propiedad.objects.filter(capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
           

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    
    if  request.GET["capacidad"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["precio1"] and request.GET["cant_banios"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(capacidad=capacidad,tipo_propiedad=tipo_propiedad,precio=precio1,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(capacidad=capacidad,tipo_propiedad=tipo_propiedad,precio=precio1,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(capacidad=capacidad,tipo_propiedad=tipo_propiedad,precio=precio1,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if  request.GET["capacidad"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["precio1"] and request.GET["dormitorios"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(capacidad=capacidad,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(capacidad=capacidad,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(capacidad=capacidad,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})



    if  request.GET["capacidad"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["precio1"] and request.GET["dormitorios"] and request.GET["cant_banios"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(capacidad=capacidad,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(capacidad=capacidad,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(capacidad=capacidad,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    #precio

    if  request.GET["precio1"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["capacidad"] and request.GET["cant_banios"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(precio=precio1,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(precio=precio1,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(precio=precio1,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if  request.GET["precio1"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["dormitorios"] and request.GET["cant_banios"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(precio=precio1,tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(precio=precio1,tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(precio=precio1,tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if  request.GET["precio1"] and request.GET["capacidad"]   and  request.GET["dormitorios"] and request.GET["cant_banios"] and request.GET["zona"]:
        
        propiedades=Propiedad.objects.filter(precio=precio1,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)
          
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    
    if  request.GET["precio1"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["capacidad"] and request.GET["dormitorios"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(precio=precio1,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(precio=precio1,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(precio=precio1,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if  request.GET["precio1"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["capacidad"] and request.GET["dormitorios"] and request.GET["cant_banios"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(precio=precio1,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(precio=precio1,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(precio=precio1,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    #dormitorios

    if  request.GET["dormitorios"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["capacidad"] and request.GET["precio1"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if  request.GET["dormitorios"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["capacidad"] and request.GET["cant_banios"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if  request.GET["dormitorios"] and request.GET["capacidad"]  and  request.GET["precio1"] and request.GET["cant_banios"] and request.GET["zona"]:
        
        propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,capacidad=capacidad,precio=precio1,cant_banios=cant_banios,zona=zona)
           
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if  request.GET["dormitorios"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["precio1"] and request.GET["cant_banios"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad,precio=precio1,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad,precio=precio1,cant_banios=cant_banios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad,precio=precio1,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if  request.GET["dormitorios"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["capacidad"] and request.GET["precio1"] and request.GET["cant_banios"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    #banios

    if  request.GET["cant_banios"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["capacidad"] and request.GET["precio1"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(cant_banios=cant_banios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(cant_banios=cant_banios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(cant_banios=cant_banios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if  request.GET["cant_banios"] and request.GET["capacidad"] != "ninguna"  and  request.GET["precio1"] and request.GET["dormitorios"] and request.GET["zona"]:
        
        propiedades=Propiedad.objects.filter(cant_banios=cant_banios,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,zona=zona)
           

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if  request.GET["cant_banios"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["precio1"] and request.GET["dormitorios"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(cant_banios=cant_banios,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(cant_banios=cant_banios,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(cant_banios=cant_banios,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if  request.GET["cant_banios"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["capacidad"] and request.GET["dormitorios"] and request.GET["zona"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(cant_banios=cant_banios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(cant_banios=cant_banios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(cant_banios=cant_banios,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    #zona

    if  request.GET["zona"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["capacidad"] and request.GET["precio1"] and request.GET["dormitorios"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(zona=zona,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(zona=zona,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(zona=zona,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})
    

    if  request.GET["zona"] and request.GET["capacidad"]   and  request.GET["precio1"] and request.GET["dormitorios"] and request.GET["cant_banios"]:
        
        propiedades=Propiedad.objects.filter(zona=zona,capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)
          
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if  request.GET["zona"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["precio1"] and request.GET["dormitorios"] and request.GET["cant_banios"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(zona=zona,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(zona=zona,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(zona=zona,tipo_propiedad=tipo_propiedad,precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if  request.GET["zona"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["capacidad"] and request.GET["dormitorios"] and request.GET["cant_banios"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(zona=zona,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(zona=zona,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(zona=zona,tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if  request.GET["zona"] and request.GET["tipo_propiedad"] != "ninguna"  and  request.GET["capacidad"] and request.GET["precio1"] and request.GET["cant_banios"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(zona=zona,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(zona=zona,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(zona=zona,tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})



    #---------------------------------------------------------------------------------------------------------
    #BUSQUEDAS QUE IMPLICAN TRES CAMPOS

    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,capacidad=capacidad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["precio1"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,precio=precio1)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})



    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["dormitorios"]:
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["cant_banios"] !='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna" and request.GET["zona"] !='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["precio1"] :
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,precio=precio1)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})



    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["dormitorios"] :
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_ambientes=dormitorios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["cant_banios"] !='' :
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1}) 


    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"] and request.GET["zona"] !='' :
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1}) 

    if request.GET["capacidad"] and request.GET["precio1"] and request.GET["idpro"] :
        
        propiedades=Propiedad.objects.filter(capacidad=capacidad,precio=precio1,id=idpro)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["capacidad"] and request.GET["precio1"] and request.GET["dormitorios"] :
        
        propiedades=Propiedad.objects.filter(capacidad=capacidad,precio=precio1,cant_ambientes=dormitorios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["capacidad"] and request.GET["precio1"] and request.GET["cant_banios"] !='' :
        
        propiedades=Propiedad.objects.filter(capacidad=capacidad,precio=precio1,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["capacidad"] and request.GET["precio1"] and request.GET["zona"] !='' :
        
        propiedades=Propiedad.objects.filter(capacidad=capacidad,precio=precio1,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["precio1"] and request.GET["dormitorios"] and request.GET["idpro"]  :
        
        propiedades=Propiedad.objects.filter(precio=precio1,cant_ambientes=dormitorios,id=idpro)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["precio1"]  and request.GET["dormitorios"] and request.GET["tipo_propiedad"] !='' :
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(precio=precio1,cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(precio=precio1,cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(precio=precio1,cant_ambientes=dormitorios,tipo_propiedad=tipo_propiedad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["precio1"] and request.GET["dormitorios"] and request.GET["cant_banios"] !='' :
        
        propiedades=Propiedad.objects.filter(precio=precio1,cant_ambientes=dormitorios,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["precio1"] and request.GET["dormitorios"] and request.GET["zona"] !='' :
        
        propiedades=Propiedad.objects.filter(precio=precio1,cant_ambientes=dormitorios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["dormitorios"] and request.GET["cant_banios"] !='' and request.GET["idpro"] :
        
        propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,cant_banios=cant_banios,id=idpro)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["dormitorios"]  and request.GET["cant_banios"] and request.GET["tipo_propiedad"] !='' :
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,cant_banios=cant_banios,tipo_propiedad=tipo_propiedad)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,cant_banios=cant_banios,tipo_propiedad=tipo_propiedad)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,cant_banios=cant_banios,tipo_propiedad=tipo_propiedad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["dormitorios"] and request.GET["cant_banios"] !='' and request.GET["capacidad"] :
        
        propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,cant_banios=cant_banios,capacidad=capacidad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["dormitorios"] and request.GET["cant_banios"] !='' and request.GET["zona"] !='' :
        
        propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["cant_banios"] !='' and request.GET["zona"] !='' and request.GET["idpro"] :
        
        propiedades=Propiedad.objects.filter(cant_banios=cant_banios,zona=zona,id=idpro)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["cant_banios"] and request.GET["zona"] !='' and request.GET["tipo_propiedad"] !='' :
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(cant_banios=cant_banios,zona=zona,tipo_propiedad=tipo_propiedad)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(cant_banios=cant_banios,zona=zona,tipo_propiedad=tipo_propiedad)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(cant_banios=cant_banios,zona=zona,tipo_propiedad=tipo_propiedad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["cant_banios"] !='' and request.GET["zona"] !='' and request.GET["capacidad"] :
        
        propiedades=Propiedad.objects.filter(cant_banios=cant_banios,zona=zona,capacidad=capacidad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["cant_banios"] !='' and request.GET["zona"] !='' and request.GET["precio1"] :
        
        propiedades=Propiedad.objects.filter(cant_banios=cant_banios,zona=zona,precio=precio1)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] !='' and request.GET["capacidad"]  and request.GET["dormitorios"] :
        
        propiedades=Propiedad.objects.filter(id=idpro,capacidad=capacidad,cant_ambientes=dormitorios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] !='' and request.GET["capacidad"]  and request.GET["cant_banios"]!='' :
        
        propiedades=Propiedad.objects.filter(id=idpro,capacidad=capacidad,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] !='' and request.GET["capacidad"]  and request.GET["zona"]!='' :
        
        propiedades=Propiedad.objects.filter(id=idpro,capacidad=capacidad,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] !='' and request.GET["precio1"]  and request.GET["cant_banios"]!='' :
        
        propiedades=Propiedad.objects.filter(id=idpro,precio=precio1,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"]  and request.GET["precio1"]  and request.GET["zona"]!='' :
        
        propiedades=Propiedad.objects.filter(id=idpro,precio=precio1,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"]  and request.GET["dormitorios"]  and request.GET["capacidad"] :
        
        propiedades=Propiedad.objects.filter(id=idpro,cant_ambientes=dormitorios,capacidad=capacidad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"]  and request.GET["dormitorios"]  and request.GET["zona"]!='' :
        
        propiedades=Propiedad.objects.filter(id=idpro,cant_ambientes=dormitorios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"]  and request.GET["cant_banios"]  and request.GET["capacidad"] :
        
        propiedades=Propiedad.objects.filter(id=idpro,cant_banios=cant_banios,capacidad=capacidad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"]  and request.GET["cant_banios"]  and request.GET["precio1"] :
        
        propiedades=Propiedad.objects.filter(id=idpro,cant_banios=cant_banios,precio=precio1)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"]  and request.GET["zona"]!='' and request.GET["capacidad"]:
        
        propiedades=Propiedad.objects.filter(id=idpro,zona=zona,capacidad=capacidad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"]  and request.GET["zona"]!='' and request.GET["precio1"]:
        
        propiedades=Propiedad.objects.filter(id=idpro,zona=zona,precio=precio1)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["tipo_propiedad"] !='' and request.GET["precio1"] and request.GET["cant_banios"] !='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,precio=precio1,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,precio=precio1,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,precio=precio1,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["tipo_propiedad"] !='' and request.GET["precio1"] and request.GET["zona"] !='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,precio=precio1,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,precio=precio1,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,precio=precio1,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["tipo_propiedad"] !='' and request.GET["dormitorios"] and request.GET["zona"] !='':
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["capacidad"]  and request.GET["dormitorios"] and request.GET["zona"] !='':
        
        propiedades=Propiedad.objects.filter(capacidad=capacidad,cant_ambientes=dormitorios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})



    #--------------------------------------------------------------------------------------------------------
    #BUSQUEDAS POR DOS CAMPOS

    if request.GET["idpro"] and request.GET["tipo_propiedad"] != "ninguna":
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(id=idpro,tipo_propiedad=tipo_propiedad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] and request.GET["capacidad"]:
        
        propiedades=Propiedad.objects.filter(id=idpro,capacidad=capacidad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] and request.GET["precio1"]:
        
        propiedades=Propiedad.objects.filter(id=idpro,precio=precio1)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["idpro"] and request.GET["dormitorios"]:
        
        propiedades=Propiedad.objects.filter(id=idpro,cant_ambientes=dormitorios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["idpro"] and request.GET["cant_banios"] != '':
        
        propiedades=Propiedad.objects.filter(id=idpro,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})
    
    if request.GET["idpro"] and request.GET["zona"] != '':
        
        propiedades=Propiedad.objects.filter(id=idpro,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["capacidad"]:
        
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,capacidad=capacidad)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["precio1"]:
        
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,precio=precio1)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,precio=precio1)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,precio=precio1)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["dormitorios"]:
        
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,cant_ambientes=dormitorios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["cant_banios"] != '':
        
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,cant_banios=cant_banios)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,cant_banios=cant_banios)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["tipo_propiedad"] != "ninguna" and request.GET["zona"] != '':
        
        if tipo_propiedad=='casa':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,zona=zona)
        if tipo_propiedad=='departamento':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,zona=zona)
        if tipo_propiedad=='habitacion':

            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["capacidad"] and request.GET["precio1"]:

        propiedades=Propiedad.objects.filter(capacidad=capacidad,precio=precio1)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})
        

    if request.GET["capacidad"] and request.GET["dormitorios"]:

        propiedades=Propiedad.objects.filter(capacidad=capacidad,cant_ambientes=dormitorios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["capacidad"] and request.GET["cant_banios" ] != '':

        propiedades=Propiedad.objects.filter(capacidad=capacidad,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["capacidad"] and request.GET["zona"] !='':
        
        propiedades=Propiedad.objects.filter(capacidad=capacidad,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})


    if request.GET["precio1"] and request.GET["dormitorios"]:

        propiedades=Propiedad.objects.filter(precio=precio1,cant_ambientes=dormitorios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1}) 

    if request.GET["precio1"] and request.GET["cant_banios"] != '':

        propiedades=Propiedad.objects.filter(precio=precio1,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})     

    if request.GET["precio1"] and request.GET["zona"] != '':

        propiedades=Propiedad.objects.filter(precio=precio1,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})   
    

    if request.GET["dormitorios"] and request.GET["cant_banios"] !='':

        propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,cant_banios=cant_banios)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["dormitorios"] and request.GET["zona"] !='':

        propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1}) 


    if request.GET["cant_banios"] !='' and request.GET["zona"] !='':

        propiedades=Propiedad.objects.filter(cant_banios=cant_banios,zona=zona)    

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    #------------------------------------------------------------------------------------------------------
    #BUSQUEDAS POR UN CAMPO

    if request.GET["idpro"]:

        propiedades=Propiedad.objects.filter(id=idpro)
        

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["tipo_propiedad"]:
        if tipo_propiedad=='casa':
            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad)

            return render(request,'busqueda/resultados_busqueda.html',
            {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
            'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})
        if tipo_propiedad=='departamento':
            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad)

            return render(request,'busqueda/resultados_busqueda.html',
            {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
            'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1}) 
        if tipo_propiedad=='habitacion':
            propiedades=Propiedad.objects.filter(tipo_propiedad=tipo_propiedad)

            return render(request,'busqueda/resultados_busqueda.html',
            {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
            'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["capacidad"]:
        propiedades=Propiedad.objects.filter(capacidad=capacidad)
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})
    

    if request.GET["precio1"] :
        propiedades=Propiedad.objects.filter(precio=precio1)
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})
   


    if request.GET["dormitorios"]:
        propiedades=Propiedad.objects.filter(cant_ambientes=dormitorios)
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})

    if request.GET["cant_banios"]:
        propiedades=Propiedad.objects.filter(cant_banios=cant_banios)
        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1}) 

    if request.GET["zona"]:

        propiedades=Propiedad.objects.filter(zona=zona)

        return render(request,'busqueda/resultados_busqueda.html',
        {'idpro':idpro,'propiedades':propiedades,'capacidad':capacidad,'tipo_propiedad':tipo_propiedad,
        'dormitorios':dormitorios,'cant_banios':cant_banios,'zona':zona,'precio1':precio1})