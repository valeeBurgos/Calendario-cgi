#!/usr/bin/python3

# -*- coding: utf-8 -*-
import sys
import cgi
from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea2')


tem=db.get_temas_id()

head="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agregar Actividad</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>

    <script src="/JS/Agr.js"></script>
    <script src="/JS/AgregarValidaciones.js"></script>
     <link rel="stylesheet" type="text/css" href="/CSS/formulario.css"  />
</head>
"""

b1="""
<body>
    <nav>
        <ul class="menu">
            <h1>Calendario actividades recreativas </h1>
            <h2> Bienvenido: ¿Qué podemos hacer por ti? </h2>
            <hr/>
            <li class="item"><a href="Portad.py">Inicio</a></li>
            <li class="item"><a href="listado.py">Ver listado de actividades</a></li>
            <li class="item"><a href="Estadisticas.py">Estadísticas</a></li>
            <br><br>
        </ul>
    </nav>

    <div class="form-row" id="padre">
        <br><br><br>
        <form name="formulario" action="save_actividad.py" method ="post" enctype="multipart/form-data" >
            <h3>Ingrese la información de la actividad que desea agregar.</h3>
            <br><br>
            <!-- información del lugar -->
            
            <div id="primera_parte">
                <h3 class="fs-title">Datos ubicación</h3>
                <label for="regiones">Región:</label> <br>
                <select id="regiones" name="region"></select>
                <select id="comunas" name="comuna"></select><br><br>
    
                <label for="sector">Sector:</label> <br>
                <input type="text" placeholder="Sector ubicación" id="sector" size="100" name ="sector" > <br>
                <br>
    
            </div>
            

            <fieldset>
                <!-- información del organizador -->

                <div id="segunda_parte">
                    
                    <h3 class="fs-title">¿Quién organiza?</h3>
                    <div>
                        <label for="nombre_organizador">Nombre del organizador:</label> <br>
                        <input type="text" placeholder="Nombre organizador" id="nombre_organizador" size="100" maxlength="200" name ="nombre" > <br>
                    </div>
                    <br>
                    <div>
                        <label for="email_organizador">Email:</label> <br>
                        <input type="text" placeholder="Ingrese su dirección de correo electrónico" id="email_organizador" size="100" maxlength="320" name ="email" > <br>
                    </div>
                    <br>
                    <div>
                        <label for="celular_organizador">Número de contacto (celular):</label> <br>
                        <input type="text" placeholder="Ej: 56 9 11111111" id="celular_organizador" size="15" name ="celular" > <br>
                    </div>
                    <br>
                    <div>
                        <label for="contacto_organizador">Contatar por:</label>
                    
                        <div id="redes_sociales">
                            <select name="contactar-por" id="contacto_organizador">
                                <option value="0"  >Seleccione forma de contacto</option>
                                <option value="1"  >Whatsapp</option>
                                <option value="2"  >Telegram</option>
                                <option value="3"  >Twitter</option>
                                <option value="4"  >Instagram</option>
                                <option value="5"  >Tik Tok</option>
                                <option value="6"  >Otra</option>
                            </select>
                            <input type="text" placeholder="Escriba URL o nombre" id="@red" size="15" name ="contactar-nombre" > 

                        </div>

                        <br>        
                        <div id="q">
                            <h6> Agregar más redes sociales:</h6>
                            <div id="Hijo"></div>

                        </div>
                    
                        <button type="button" id="boton_agregar" class="btn btn-outline-dark" onclick="agregarCosa()">Agregar</button>

                    </div>
                    <br>
            
                </div>
               
            </fieldset>
           
           

            <fieldset>
                <!-- información de la actividad -->
                <div id="tercera_parte">
                    <h3 class="fs-title">¿Cuándo y de qué trata?:</h3> <br><br>
                    <div id="inicio">
                        <label for="fecha_inicio">Día y hora de inicio:</label> <br>
                        <input type="text" id="fecha_inicio" name="dia-hora-inicio">
                        <script>
                            var today = new Date();
                            mes=(today.getMonth()+1);
                            dia= today.getDate();
                            hora=(today.getHours());
                            min= today.getMinutes();
                            if (mes<10){
                                mes='0'+mes;
                            }
                            if (dia<10){
                                dia='0'+dia;
                            }
                            if (hora<10){
                                hora='0'+hora;
                            }
                            if (min<10){
                                min='0'+min;
                            }
                    
                            var date = today.getFullYear()+'-'+mes+'-'+dia+' '+ hora + ":" + min;
                            document.getElementById("fecha_inicio").value = date;
                        </script>
                        
                    </div>
                    <div id="hora_termino">
                        <label for="fecha_termino">Día y hora de término:</label> <br>
                        <input type="text" id="fecha_termino" name="dia-hora-termino">
                        <script>
                            var today = new Date();
                            mes=(today.getMonth()+1);
                            dia= today.getDate();
                            hora=(today.getHours()+3);
                            min= today.getMinutes();
                    
                            if (hora>=24 && min!=0){
                                hora= hora-24;
                                dia=dia+1
                            }
                            if (dia>31){
                                dia=1;
                                mes=mes+1
                            }
                            if (mes>12){
                                mes=1;
                            }
                            if (min<10){
                                min='0'+min;
                            }
                            if (hora<10){
                                hora='0'+hora;
                            }
                            if (mes<10){
                                mes='0'+mes;
                            }
                            if (dia<10){
                                dia='0'+dia;
                            }
                            var date = today.getFullYear()+'-'+mes+'-'+dia+' '+ hora + ":" +min;
                            document.getElementById("fecha_termino").value = date;
                        </script>
                    </div>

                    <div id="descripcion">
                        <label for="descrip">Descripción:</label> <br>
                        <textarea name="descripcion-evento" id="descrip" cols="50" rows="10"></textarea><br> <br>

                    </div>
"""


base="""
<div id="Elegir_tema">
                        <label for="temas">Tema:</label> <br>
                        <select name="tema" id="temas" onchange="add_input(this.value)" >
                            <option value="0"  >Seleccione tema</option>
                            <option value="10"  >Otro</option>
"""
j=1
for i in tem:
    if j==10:
        j=j+1
    if i!=10:
        base+=f"""<option value={str(j)} >{i[0]}</option>
        """
        j=j+1

final="""
</select>

                        <input type="text" name="tema_nuevo" id="si_otro" placeholder="Especifique" style='display:none;'/> 
                        
                        <div id="otro"></div>
                        <br> <br>
                    </div>
"""
b2=base+final

b3="""
<div id="foto">
                        <label for="archivp">Foto de la actividad:</label><br> 
                        <input type="file" id="archivp" name="foto-actividad"  ><br>

                        <div id="agregar_mas_fotos">
                            <br>
                            <p>Opcionales:</p>
                        </div>
                        <br>
                        <label for="boton_agregar_fotos">¿Desea agregar más fotos?</label><br>
                        <button type="button" id="boton_agregar_fotos" class="btn btn-outline-dark" onclick="Agregar_fotos()">Agregar más imágenes</button>

                    </div>
                </div>  
                
            </fieldset>

            <div id="confirmacion" style='display:none;'>
                <label> ¿Está seguro que desea agregar esta actividad?</label> <br>

                <button type="button" id="boton_enviar"  class="btn btn-outline-dark" onclick="document.formulario.submit();">“Sí, estoy seguro” </button>
                <button type="button" id="boton_No_enviar" class="btn btn-outline-dark" onclick="No_Enviar()">“No, no estoy seguro, quiero volver al
                    formulario” </button>

            </div>

            <br><br><br>



    
            <button type="button" class="btn btn-lg btn-primary" onclick="Validar()">  Agregar esta actividad</button>
        </form>
         
    </div>
    <br> <br> <br> <br>
          
</body>

"""

print(head+b1+b2+b3)