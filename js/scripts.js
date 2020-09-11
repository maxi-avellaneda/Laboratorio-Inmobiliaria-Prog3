

function formularioCasa()   {
    let formulario_principal = document.getElementById("form_general");
    let boton_casa = document.getElementById("opc_casa").value;
    let formulario_casa = document.getElementById("opciones_casa");
    let formulario_departamento = document.getElementById("opciones_dpto");
    let formulario_habitacion = document.getElementById("opciones_hab");
    if(boton_casa == 1){
        formulario_principal.style.display = "block";
        formulario_casa.style.display = "block";
        formulario_departamento.style.display = "none";
        formulario_habitacion.style.display = "none";
    }else{
        formulario_principal.style.display = "none";
        formulario_casa.style.display = "none";
    }
}

function formularioDpto()   {
    let boton_casa = document.getElementById("opc_dpto").value;
    let formulario_principal = document.getElementById("form_general");;
    let formulario_departamento = document.getElementById("opciones_dpto");
    let formulario_habitacion = document.getElementById("opciones_hab");
    let formulario_casa = document.getElementById("opciones_casa");
    if(boton_casa == 2){
        formulario_principal.style.display = "block";
        formulario_departamento.style.display = "block";
        formulario_casa.style.display= "none";
        formulario_habitacion.style.display = "none";
    }else{
        formulario_principal.style.display = "none";
        formulario_departamento.style.display = "none";
    }
}

function formularioHab()    {
    let boton_casa = document.getElementById("opc_hab").value;
    let formulario_principal = document.getElementById("form_general");;
    let formulario_habitacion = document.getElementById("opciones_hab");
    let formulario_departamento = document.getElementById("opciones_dpto");
    let formulario_casa = document.getElementById("opciones_casa");
    if(boton_casa == 3){
        formulario_principal.style.display = "block";
        formulario_habitacion.style.display = "block";
        formulario_departamento.style.display ="none";
        formulario_casa.style.display = "none";
    }else{
        formulario_principal.style.display = "none";
        formulario_habitacion.style.display = "none";
    }
}