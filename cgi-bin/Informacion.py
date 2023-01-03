#!/usr/bin/python3

# -*- coding: utf-8 -*-
import sys
import cgi
from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

arg=cgi.FieldStorage()

if "id" in arg:
    id_a = arg["id"].value    

db = DB('localhost', 'root', '', 'tarea2')

head="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informacion Actividad</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="/CSS/1.css"  />


</head>
"""

#obtener datos por id
U=db.get_datos_ubicacion(id_a)
R=db.get_region(U[0][3])[0][0]
N=db.get_nombre_id(R)[0][0]

O=db.get_datos_org(id_a)
contacto=db.get_contactos(id_a)

Act=db.get_info_actividad(id_a)
imagenes= db.get_foto_por_id(id_a)


def imprimir_imagenes(imagen):
    pr=""
    for i in imagen:
        fot=i[2]
        prim='<img alt="" onclick="javascript:this.width=800 ;this.height=600" ondblclick="javascript:this.width=320; this.height=240" src="'
        im=f'../media/{fot}" width="320"/><br>'        
        pr=pr+prim+im
    return pr


im_imag=imprimir_imagenes(imagenes)
def contactos(contacto):
    imprimir=""
    i=0
    while i<len(contacto):
        conta=contacto[i]
        imprimir= imprimir +conta[0]+": "+conta[1]+" <br> "
        i=i+1
    return imprimir

imp=contactos(contacto)

inicio="""
<body>
    <nav>
  <ul class="menu">
            <h1>Calendario actividades recreativas </h1>
            <hr/>
            <li class="item"><a href="Portad.py">Inicio</a></li>
            <li class="item"><a href="listado.py">Ver listado de actividades</a></li>
            <li class="item"><a href="Estadisticas.py">Estadísticas</a></li>
            <br><br>
        </ul>
</nav>
    <div id="informacion_actividad" style = 'width: 85%;' >
    <br>
        <h3>Información de la actividad:</h3>
    <br>
"""

p1="""<div id="Información_de_ubicación" style = 'border:1px solid rgb(0, 0, 0);'>"""

tabla1=f"""
<h4>Información de la ubicación:</h4>
            <table class="table table-bordered">
                <tr>  
                    <td>Región: </td>
                    <td>{N}</td>
                </tr>
                <tr>
                    <td>Comuna: </td>
                    <td>{U[0][1]}</td>
                </tr>
                <tr>
                    <td>Sector: </td>
                    <td>{U[0][2]}</td>
                </tr>
                

            </table>
        """
T1="""</div> <br> <br>"""

p2="""<div id="Informacion_de_organizador" style = 'border:1px solid rgb(0, 0, 0);'>
            <h4>Información del organizador </h4>"""
tabla2=f"""
<table class="table table-bordered">
                <tr>  
                    <td>Nombre: </td>
                    <td>{O[0][0]}</td>
                </tr>
                <tr>
                    <td>Email: </td>
                    <td>{O[0][1]}</td>
                </tr>
                <tr>
                    <td>N° de celular: </td>
                    <td>{O[0][2]}</td>
                </tr>
                <tr>
                    <td>Contactar por: </td>
                    <td>{imp}</td>
                </tr>
            </table>
"""


T2="""</div> <br> <br>"""

p3="""<div style = 'border:1px solid rgb(0, 0, 0);'>
        <h4>Información de la actividad </h4>"""

tabla3=f"""
<table class="table table-bordered">         
                <tr>  
                    <td>Dia-Hora inicio: </td>
                    <td>{Act[0][0]}</td>
                </tr>
                <tr>
                    <td>Dia-Hora final: </td>
                    <td>{Act[0][1]}</td>
                </tr>
                <tr>
                    <td>Descripción: </td>
                    <td>{Act[0][2]}</td>
                </tr>
                <tr>
                    <td>Tema: </td>
                    <td>{Act[0][3]}</td>
                </tr>
                <tr>
                    <td>Imágenes: </td>
                    <td>{im_imag}
                    </td>
                </tr>
            </table>
"""

T3="""
            <p>*Para agrandar una imagen, haga click sobre ella. Para reducirla, haga doble click.</p>
        </div>

    </div>
"""

FIN="""
 
    <br><br><br>"""

body=inicio+p1+tabla1+T1+p2+tabla2+T2+p3+tabla3+T3+FIN
print(head+body)