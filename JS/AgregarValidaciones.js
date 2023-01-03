//HAGO MIS FUNCIONES PARA VALIDAR CADA UNO DE LOS CAMPOS CON JS


//Función general para validar. Va acumulando en un string los errores de validación.
//al final muestra estos errores en una alarma. Si no hay errores, hace visible una
//casilla que originalmente estaba oculta, la cual pregunta si se está seguro de que se quiere
//enviar el formulario.

function Validar(){
	//Hago mis variables para poder contener errores y ponerle comas
	let errors = '';
	let comas=0;
    
    
    //Primera parte. Estos son los valores correspondiente a la primera parte
	Com=document.getElementById('comunas').value;
	Reg=document.getElementById('regiones').value;
	Secto=document.getElementById('sector').value;

	

	//valido la primera parte.
	if (!validarRegion(Reg,Com)){
		if (comas ==0){
            errors +=' Elección de región y/o comuna';
        }else{
            errors+=', elección de región y/o comuna';
        }
        comas+=+1
	}

    if (!validarSector(Secto)){
		if (comas ==0){
            errors +=' Largo Sector';
        }else{
            errors+=', largo sector';
        }
        comas+=+1
	}


	//Parte dos: organizador
    //Obtengo los valores a validar.
	Nombre=document.getElementById('nombre_organizador').value;
	valor=document.getElementById('email_organizador').value;
	numero=document.getElementById('celular_organizador').value;
	red=document.getElementById('contacto_organizador').value;
    inp= document.getElementById('@red').value;
    
    //Nombre obligatorio y largo máximo 200 carácteres.
	if (!validarNombre(Nombre)){
		if (comas ==0){
            errors +=' Nombre organizador';
        }else{
            errors+=', nombre organizador';
        }
        comas+=+1
	}
    // Email obligatorio. Formato de usuario@algo.algo
	if (!validarEmail(valor)){
		if (comas ==0){
            errors +=' Email';
        }else{c
            errors+=', email';
        }
        comas+=+1
	}

    //Veo que el celular tenga números. No uso otra validación para que acepte cualquier cantidad de números
    //y no limitarlo a un país ya que en el enunciado no se especifica.
    if (!validarCelular(numero)){
		if (comas ==0){
            errors +=' Solo se aceptan números para en contacto de celular';
        }else{c
            errors+=', solo se aceptan números para en contacto de celular';
        }
        comas+=+1
	}

    //Ahora valido las redes sociales. me pongo en casos para ver si tengo todas las posibles (max5).
    //muestro problemas si selecciono en la casilla pero no pongo el @.
    //No muestro problemas si el select y el @ están vacíos.
    //si hay @, debe tener cierto largo min y max. 
    if (!validarContacto(red,inp)){
            if (comas ==0){
                errors +=' Error en red social n°1';
            }else{c
                errors+=', error en red social n°1';
            }
            comas+=+1
    }

    if (document.getElementById('cloned-box1') != null){
        red=document.getElementById('cloned-box1').value;
        inpu=document.getElementById('cloned-input1').value;

        if(!validarContacto(red,inpu)){

            if (comas ==0){
                errors +=' Error en red social n°2';
            }else{c
                errors+=', error en red social n°2';
            }
            comas+=+1
        }
    }

    if (document.getElementById('cloned-box2') != null){
        red=document.getElementById('cloned-box2').value;
        inpu=document.getElementById('cloned-input2').value;

        if(!validarContacto(red,inpu)){

            if (comas ==0){
                errors +=' Error en red social n°3';
            }else{c
                errors+=', error en red social n°3';
            }
            comas+=+1
        }
    }

    if (document.getElementById('cloned-box3') != null){
        red=document.getElementById('cloned-box3').value;
        inpu=document.getElementById('cloned-input3').value;

        if(!validarContacto(red,inpu)){

            if (comas ==0){
                errors +=' Error en red social n°4';
            }else{c
                errors+=', error en red social n°4';
            }
            comas+=+1
        }
    }


    if (document.getElementById('cloned-box4') != null){
        red=document.getElementById('cloned-box4').value;
        inpu=document.getElementById('cloned-input4').value;

        if(!validarContacto(red,inpu)){

            if (comas ==0){
                errors +=' Error en red social n°5';
            }else{c
                errors+=', error en red social n°5';
            }
            comas+=+1
        }
    }

    //PARTE 3:CUANDO Y DE QUE TRATA
    //obtengo los valores de esta sección.
    inicio= document.getElementById('fecha_inicio').value;
    fin= document.getElementById('fecha_termino').value;
    tema= document.getElementById("temas").value;
    archivo=document.getElementById("archivp").value;

    //valido la fecha de inicio en el formato. No se aceptan espacios donde no van.
    if (!validarFecha2(inicio)){
        if (comas ==0){
            errors +=' Error formato fecha de inicio';
        }else{
            errors+=', error formato fecha de inicio';
        }
        comas+=+1
    }
    //valido la fecha de inicio en el formato. No se aceptan espacios donde no van.
    if (!fin==''){
        if (!validarFecha2(fin)){
            if (comas ==0){
                errors +=' Error formato fecha de término';
            }else{
                errors+=', error formato fecha de término';
            }
            comas+=+1
    }
    }

    
    //veo que haya un tema seleccionado, y si se pone otro, entonces me aseguro de escribirlo
    //con los largos indicados.
    if (!validadorTema(tema)){
        if (comas ==0){
            errors +=' Error elección tema';
        }else{
            errors+=', error elección tema';
        }
        comas+=+1
    }

    //me aseguro que tenga el primer archivo seleccionado, que es obligatorio.
    //los otro 4 que pueden aparecer al hacer click son opcionales.
    if (!ValidarArchivo(archivo)){
        if (comas ==0){
            errors +=' Debe adjuntar la imagen obligatoria';
        }else{
            errors+=', debe adjuntar la imagen obligatoria';
        }
        comas+=+1
    }
    





	//Si hay errores se muestran como alerta
    /*Finalmente si hay errores lo escribimos en el contenedor de errores, en nuestro div al costado del formulario*/
    if(errors != ''){
		avisos= "Su formulario falló en:" + errors + "."
		alert(avisos);
		return false;
    }
    else {
        var element = document.getElementById('confirmacion');
	    element.style.display='block';

    }


}


//ACÁ SE HACEN LAS FUNCIONES PARA REALIZAR LAS VALIDACIONES.
//PARTE 1:LUGAR

function validarRegion(Reg,com){
	if (Reg=='sin-region'){
		return false;
	} else {
        if (com=='sin-comuna'){
            return false;
        } else {
            return true;
        }
	}
}

function validarComuna(com){
	if (com=='sin-region'){
		return false;
	} else {
		return true;
	}
}

function validarSector(secto){
	if (secto.length>100){
		return false;
	} else {
		return true;
	}
}


//PARTE 2: ORGANIZACION
//segunda parte

function validarNombre(nombre){
	if (nombre.length>0){
        if (nombre.length<201){
            return true;
        } return false;
	} else {
		return false;
	}
}


function validarEmail(emailAdress)
{
  let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  if (emailAdress.match(regexEmail)) {
    return true; 
  } else {
    return false; 
  }
}
  



function validarCelular(numero){
    var reg = /^\d+$/;
    if (reg.test(numero)){
		return true;
	} else {
		return false;
	}
  }




function validarContacto(red,inpu){
	if (red==0) {
        if (inpu.length ==0){
            return true;
        } else{
            return false;
        }
	} else {
        if ((inpu.length>2 && inpu.length<51 )){
            return true;
        } else {
            return false;
        }
	}
}

//PARTE 3: CUANDO Y DE QUE

//reviso término por término.
function validarFecha2(fecha){
    n=fecha.length;
    i=0;
    if (n!=16){
        return false;
    }
    while (i<n){
        revisar=fecha[i];


        if (i==0 && (!(Number(revisar) <10))){
            return false;
        }
        if (i==1 && (!(Number(revisar) <10))){
            return false;
        }
        if (i==2 && (!(Number(revisar) <10))){
                return false;
        }
        if (i==3 && (!(Number(revisar) <10))){
                return false;
        }
        if (i==5 && (!(Number(revisar) <10))){
                return false;
        }
        if (i==6 && (!(Number(revisar) <10))){
            return false;
        }
        if (i==8 && (!(Number(revisar) <10))){
            return false;
        }
        if (i==9 && (!(Number(revisar) <10))){
            return false;
        }
        if (i==11 && (!(Number(revisar) <10))){
            return false;
        }
        if (i==12 && (!(Number(revisar) <10))){
            return false;
        }
        if (i==14 && (!(Number(revisar) <10))){
            return false;
        }
        if (i==15 && (!(Number(revisar) <10))){
            return false;
        }
        if (i==4 && (revisar!='-')){
            return false;
        }
        if (i==7 && (revisar!='-')){
            return false;
        }

        if (i==13 && (revisar != ':')){
            return false;
            }
        
        if (i==10 && (revisar != ' ')){
            return false;
        }
        i=i+1
    }
    return true;
    
    
}



//validador input tema
function Validar_input_tema(aa){
    if (aa.length<3 || aa.length>15){
        return false;
    }
    return true;

}
//validador para el tema select.
function validadorTema(tema){
    if (tema==0){
        return false;
    }
    if (tema==10){
        tem_input= document.getElementById("si_otro").value;
        if(!Validar_input_tema(tem_input)){
            return false;
        } else {
            return true;
        }

    }
    return true;
}


//Validador para los archivos.
function ValidarArchivo(archivo){
    if(archivo == ''){
        return false;
    }
    //si no está vacio
    return true;
}



//CODIGO PARA ENVIAR EL FORMULARIO

function Enviar(){
    event.preventDefault();

    swal("“Hemos recibido su información, muchas gracias y suerte en su actividad", 
    "Continue a la portada:", "success").then(function() {
        document.formulario.submit();
        location.href = "http://anakena.dcc.uchile.cl/~cc500207/Tarea1copy/Portada.html";})
    
    
}


function No_Enviar(){
    var element = document.getElementById('confirmacion');
    element.style.display='none';
    return;
}
