#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sys
from db import DB
import json

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')


db = DB('localhost', 'root', '', 'tarea2')

#Cabezera e inicio del archivo
head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Portada</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>
   
   
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.8.0/dist/leaflet.css"
   integrity="sha512-hoalWLoI8r4UszCkZ5kL8vayOGVae1oxXe/2A4AO6J9+580uKHDO3JdHb7NzwwzK5xr/Fs0W40kiNHxM9vyTtQ=="
   crossorigin=""/>

   <script src="https://unpkg.com/leaflet@1.8.0/dist/leaflet.js"
   integrity="sha512-BB3hKbKWOc9Ez/TAwyWxNXeoV9c1v6FIeYiBieIWkpLjauysF18NzgR1MBNBXf8/KABdlkX68nAhlwcDFLGPCQ=="
   crossorigin=""></script>



    <link rel="stylesheet" type="text/css" href="/CSS/Portada.css"  />

    <script src="/JS/Portada.js"></script>
</head>
"""



Inicio="""
<body>
<div id="todo">
<nav>
  <ul class="menu">
    <h1>Calendario actividades recreativas </h1>
    <h2> Bienvenido: ¿Qué podemos hacer por ti? </h2>
     <hr/>
    <li> <a href="formulario.py">Agregar actividad</a> </li>
    <li><a href="listado.py">Ver listado de actividades</a></li>
    <li><a href="Estadisticas.py">Estadísticas</a></li>
    <br><br>
    <button id='Actualizar' style='width: 400px; height: 50px;' onclick="javascript:asyncChange();">Actualizar información</button>


  </ul>
</nav>
<br>
<div id="tab" style = 'width: 85%;'>

<h3> Información últimas 5 actividades agregadas.</h3>
<br><br><br>

"""
#Se imprime esto
print(head+Inicio)

#TABLA CON ULTIMAS 5 ACTIVIDADES

#Primero se procesa en python la información.
datos=db.get_5_actividades()

#Se crea la tabla
tabla = """
        <table class="table">
        <thead>
            <tr>
                <th scope="col">Inicio</th>
                <th scope="col">Término</th>
                <th scope="col">Comuna</th>
                <th scope="col">Sector</th>
                <th scope="col">Tema</th>
                <th scope="col">Foto</th>
            </tr>
        </thead>
        <tbody>
"""
for p in datos:
    fo=db.get_foto_por_id(p[0])
    fot=fo[0][2]
    tabla+=f""" 
        <tr>
            <td>{p[6]}</td>
            <td>{p[7]}</td>
            <td>{p[1]}</td>
            <td>{p[2]}</td>
            <td>{p[9]}</td>
            <td><img src=../media/{fot} width=120 height=120</td>
        </tr>
"""

tabla+="""
    </tbody>
    </table>
    <br><br><br>
     """

#Se printea la tabla
print(tabla)



#AHORA SE TRABAJA EN EL MAPA
#Procesamiento de datos en python

#SELECT DISTINCT CO.nombre FROM actividad AC,comuna CO WHERE AC.comuna_id=CO.id 
com=db.get_comunas_usadas()


conteo=[]
comunas=[]
for i in com:
    comunas.append(i[0])
    com_id=db.get_comuna_id(i[0])
    con=db.get_n_fotos(com_id[0][0])
    conteo.append(con[0][0])
f=conteo

def tabla(comuna):
    datos=[]
    info=db.get_actividades_por_comuna(comuna)
    for i in info: 
        p=[]
        hora_str = i[0].strftime('%d/%m/%Y %H:%M')
        p.append(hora_str)
        p.append(i[1])
        p.append(i[2])
        p.append(i[3])
        datos.append(p)
    return datos

datos_tabla=[]
for comuna in comunas:
    datos_tabla.append(tabla(comuna))


with open(r'JSON\comu.json','r') as file:
    data=json.load(file)

def buscar_coordenadas(Comuna):
    for i in data:
        name=str(i['name'])
        if name==Comuna:
            lat=float(i['lat'])
            lon=float(i['lng'])
            
            return [lat,lon]
cordenadas=[]

for i in comunas:
    cordenadas.append(buscar_coordenadas(i))


#FILTRADO DE DATOS.
#se filtran todos los datos que hayan podido dar problemas.
co=[]
C=[]
cor=[]
ta=[]
m=len(comunas)
j=0
for i in cordenadas:
    if i==None:
        j=j+1
    else:
        co.append(comunas[j])
        C.append(conteo[j])
        cor.append(cordenadas[j])
        ta.append(datos_tabla[j])
        j=j+1



boton1=f"""<button id='m' style='background-color: #e7e7e7; color: black;width: 100%; height: 40px;'  onclick="javascript:createMap({co},{C},{cor},{ta});">Ver información geográfica de todas las actividades agregadas</button>

"""
print(boton1)
#Se crea el div que va a contener el mapa estatico y se imprime.
mapa_contenedor="""
<div id="map"  ></div>"""

print(mapa_contenedor)




#Término del archivo
Fin=f"""

</div>
</div>
<br><br><br><br><br><br></body>
"""
print(Fin)
