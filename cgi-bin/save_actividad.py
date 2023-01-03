#!/usr/bin/python3
# # -*- coding: utf-8 -*-
import cgi
import os
import sys
from db import DB
import re
from datetime import datetime
import html

#Para guardar los errores
errores=""
err=0

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea2')

form = cgi.FieldStorage()
#Hago la validación por parte del servidor.
#PARTE 1:DATOS UBICACIÓN


def es_lista(ob):
    try :
        if fileobj[0].type:
            return "Lista"
    except:
        return "Uno"


region=form['region'].value
comuna=form['comuna'].value
sector=form['sector'].value

#compruebo inyeccion de codigo 
if html.escape(region) !=region:
    print("Error en region")
    err=1
    sys.exit()
if html.escape(comuna) !=comuna:
    print("Error en comuna")
    err=1
    sys.exit()
if html.escape(sector) !=sector:
    print("Error en sector")
    err=1
    sys.exit()
#comprobando su largo me aseguro que se haya seleccionado region y comuna
if (len(region)==0 or len(comuna)==0):
    E=" Seleccione región y/o comuna. <br>"
    errores=errores+E
    print(errores)
    err=1
    sys.exit()

    sys.exit()
if len(sector)>100:
    E="Sector debe tener max 100 carácteres.<br>"
    errores=errores+E
    print(errores)
    err=1
    sys.exit()

#PARTE 2: QUIEN ORGANIZA
nombre=form['nombre'].value
email=form['email'].value
celular=form['celular'].value
contacto=form.getlist("contactar-por")
redes=form.getlist("contactar-nombre")

#compruebo inyeccion de codigo
if html.escape(nombre) !=nombre:
    print("Error en nombre")
    err=1
    sys.exit()
if html.escape(email) !=email:
    print("Error en email")
    err=1
    sys.exit()
if html.escape(celular) !=celular:
    print("Error en celular")
    err=1
    sys.exit()



if len(nombre)>200 or len(nombre)==0:
    E="Largo de nombre inválido. <br>"
    errores=errores+E
    err=1
    print(errores)
    sys.exit()


if len(email)==0:
    E="Ingrese email"
    errores=errores+E
    print(errores)
    sys.exit()
if (email):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    c=re.match(expresion_regular, email) 
    if c==None:
        E="Error formato de correo.<br>"
        errores=errores+E
        err=1
        print(errores)

        sys.exit()


if celular:
    if str.isdigit(celular)==False:
        E="Ingrese un celular válido. <br>"
        errores=errores+E
        print(errores)
        err=1
        sys.exit()


while c in contacto:
    if html.escape(c) !=c:
        print("Error en contacto")
        err=1
        sys.exit()
    if c<0 or c>6:
        print("Seleccione una red social valdia. <br>")
        E="Seleccione una red social valdia. <br>"
        errores=errores+E
        print(errores)
        err=1
    c+=1


for d in redes:
    if html.escape(d) !=d:
        print("Error en contacto")
        err=1
        sys.exit()
    if len(d)<4 or len(d)>50:
        E="Largo de la red social invalido.<br>"
        errores=errores+E
        print(errores)
        err=1
        sys.exit()


#PARTE 3:¿Cuándo y de qué trata?:
inicio=form['dia-hora-inicio'].value
termino=form['dia-hora-termino'].value
des= form['descripcion-evento'].value
tema= form['tema'].value
fileobj = form['foto-actividad']


if html.escape(inicio) !=inicio:
    print("Error en fecha de inicio")
    err=1
    sys.exit()
if html.escape(termino) !=termino:
    print("Error en fecha de inicio")
    err=1
    sys.exit()

if html.escape(des) !=des:
    print("Error en descripcion")
    err=1
    sys.exit()

if not inicio:
    E="ingrese fecha de inicio.<br>"
    errores=errores+E
    err=1
    sys.exit()

if len(termino)==0:
    E="ingrese fecha de termino.<br>"
    errores=errores+E
    err=1
    sys.exit()

if inicio:
    format = "%Y-%m-%d"
    dia,hora= inicio.split()
    res = True
    try:
        res = bool(datetime.strptime(dia, format))
    except ValueError:
        res = False
    if res==False:
        E="Error formato fecha de inicio"
        errores=errores+E
        err=1
        sys.exit()

if termino:
    format = "%Y-%m-%d"
    dia,hora= termino.split()
    res = True
    try:
        res = bool(datetime.strptime(dia, format))
    except ValueError:
        res = False
    if res==False:
        E="Error formato fecha de inicio"
        errores=errores+E
        err=1
        sys.exit()


if  tema==0:
    E="Debe seleccionar un tema"
    errores=errores+E
    err=1
    sys.exit()


if tema==10:
    nuevo=form['tema_nuevo'].value
    if len(nuevo)<3 or len(nuevo)>15:
        E="Problema en largo de tema"
        errores=errores+E
        err=1
        sys.exit()





#Si entrego una lista con imagenes

if es_lista(fileobj)=="Lista":
    fotos=[]
    for i in fileobj:
        fotos.append(i)
        tipo = i.type
        if tipo != 'image/png' and tipo != 'image/jpeg':
            E="Revise el formato de la imagen"
            errores=errores+E
            err=1
            sys.exit()

if es_lista(fileobj)=="Uno":
    if fileobj.filename:
        fotos=[fileobj]
        tipo = fileobj.type
        if tipo != 'image/png' and tipo != 'image/jpeg':
            E= "Revise el formato de la imagen"
            errores=errores+E
            err=1
            sys.exit()

        size = os.fstat(fileobj.file.fileno()).st_size
        MAX_FILE_SIZE= 1000000
        if size > MAX_FILE_SIZE:
            E='Error, archivo muy grande.'
            errores=errores+E
            print(errores)
            err=1
            sys.exit() 

    else:
        E="Seleccione imagen"
        errores=errores+E
        err=1
        print(errores)
        sys.exit()


com =db.get_comuna_id(comuna)[0][0]
data = (com, sector, nombre, email, celular, inicio, termino, des, tema)
contactar=(contacto, redes)

#PARA IMPRIMIR
head="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guardar actividad</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="/CSS/list.css"  />

</head>
"""
if err==0:
    body="""
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
    <div>
    <br><br>
    <h3>La información ha sido guardada exitosamente.</h3>
    </div>
    </body>
    """

n=db.get_tema_id()
m=n[0][0]+1



tema=int(tema)
if tema!=10:
    if tema>10:
        data = (com, sector, nombre, email, celular, inicio, termino, des, tema-1)
    db.save_data(data,fotos,contacto,redes,Tema="ok",m="nop")
    print ()
    print(head+body)
if tema==10: 
    
    data = (com, sector, nombre, email, celular, inicio, termino, des, m)
    Tema=form['tema_nuevo'].value

    db.save_data(data,fotos,contacto,redes,Tema,m)
    print ()
    print(head+body)

