#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sys

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea2')
#Se crea head
head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estadisticas</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>

    <script src="https://code.highcharts.com/highcharts.js"></script>
    <script src="https://code.highcharts.com/modules/series-label.js"></script>
    <script src="https://code.highcharts.com/modules/exporting.js"></script>
    <script src="https://code.highcharts.com/modules/export-data.js"></script>
    <script src="https://code.highcharts.com/modules/accessibility.js"></script>

   <link rel="stylesheet" type="text/css" href="/CSS/estadis.css"  />

    <script src="/JS/Estadisticas.js"></script>
</head>
"""
#Se inicia  body. Se hace un div para cada grafico
inicio="""
<body>
<div id="todo">
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
  <div id="myLabel" style = 'width: 85%;'>
    
    
    <div id="divcontenedor">
       <h3>Informacion sobre las actividades registradas:</h3>
       <br>



    """
#Se printea esta parte 
print(head+inicio)

#Procesamiento python para crear primer grafico. C=[0, 0, 8, 27, 0, 0, 0] por ejemplo.
#Donde la posición indica el día, así hay 8 actividades miercoles y 27 el jueves.
dias= db.get_fecha_inicio()
C=[0,0,0,0,0,0,0]
for j in dias:
  fecha=j[0]
  dia=fecha.isoweekday()
  i=1
  while i<8:
    if dia==i:
      C[i-1]=C[i-1]+1
    i=i+1



#Se llama al grafico generado por la funcion graf1 de js como archivo aparte.
b1=f"<button style='background-color: #e7e7e7; color: black;width: 500px; height: 30px;' onclick='javascript:graf1({C});'>Ver N° de actividades por día de la semana</button> <br><br>"

print(b1)
ht1="""
<div id=foto1></div>
       <div id=foto11></div>"""

print(ht1)
#Se printea esta parte

#PARA EL SEGUNDO GRAFICO

#Procesamiento de los datos
tem=db.get_categ()

Temas=[]
Todos_los_temas=db.get_todos_temas()
for i in Todos_los_temas:
    Temas.append(i[0])

Temas_unicos=[]
count=[]
for i in Temas:
    if i not in Temas_unicos:
        Temas_unicos.append(i)
        c=Temas.count(i)
        count.append(c)

'''
En tem se deja el formato para dejar en el formulario
Será algo tipo tem={nombre:'música',y:5},{nombre:'deporte',y:1},
 {nombre:'ciencias',y:26},{nombre:'tecnología',y:1},{nombre :'baile',y:1},
 {nombre:'comida',y:1}
'''

max=len(Temas_unicos)
s=0
t=""
while s<len(Temas_unicos):
    if s==max-1:
        t=t+f"""{{name:'{Temas_unicos[s]}',y:{count[s]}}}"""
        s+=1
    else:
        t=t+f"""{{name:'{Temas_unicos[s]}',y:{count[s]}}},"""
        s+=1


tem=t



#El botón no funciona, la función js no está bien
b2=f"""<button style='background-color: #e7e7e7; color: black;width: 500px; height: 30px;' onclick="javascript:segundografico({Temas_unicos},{count});">Ver N° de actividades por tipo</button><br><br>"""
print(b2)
ht="""
      <div id=foto2></div>
       <div id=foto22></div>

    """

print(ht)




#PARA EL TERCER GRÁFICO
"""
Como resultado final se tendrá en dat lo que se quiera poner el el gráfico
Y este tiene la forma:
 "{nombre:'mañana', datos:[0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0]},
  {nombre:'Mediodia', datos:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
  {nombre:'tarde', datos:[0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0]}"
"""

mañana=[0,0,0,0,0,0,0,0,0,0,0,0]
mediodia=[0,0,0,0,0,0,0,0,0,0,0,0]
tarde=[0,0,0,0,0,0,0,0,0,0,0,0]

for i in dias:
    d=i[0]
    mes=d.month
    hora=d.hour
    m=int(mes)
    h=int(hora)
    j=0
    while j<13:
        if m==j:
            if h<11:
                mañana[m-1]=mañana[m-1]+1
            if h>=11 and h<15:
                mediodia[m-1]=mediodia[m-1]+1
            if h>=15 and h<24:
                tarde[m-1]=tarde[m-1]+1
        j=j+1
dat=""
dat=dat+"{name:'mañana', data:"+f"{mañana}"+"},"
dat=dat+"{name:'Mediodia', data:"+f"{mediodia}"+"},"
dat=dat+"{name:'tarde', data:"+f"{tarde}"+"}"
d=[]
d.append(mañana)
d.append(mediodia)
d.append(tarde)

#Boton para actualizar
b2=f"""<button style='background-color: #e7e7e7; color: black;width: 500px; height: 30px;' onclick="javascript:tercergrafico({d});">Ver horario de actividades por mes</button> <br><br>"""
#Se imprime
print(b2)
#Se hace la zona
ht3=f"""
<div id=foto3></div>
       <div id=foto33></div>
       <br>
    </div>"""

print(ht3)


#Termina el archivo
end="""
<br>
    
    <br>
    <br>
    </div>
    </div>
    </body>"""
#Se imprime
print(end)
