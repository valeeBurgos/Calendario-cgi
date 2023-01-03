#!/usr/bin/python3

# -*- coding: utf-8 -*-
import sys

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea2')


head="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Listado Actividades</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>

 <link rel="stylesheet" type="text/css" href="\CSS\list.css"  />
</head>
"""
inicio="""
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


"""

datos= db.get_actividades()
tabla = """
<br><br><br>
<div id = "tabla">
        <table id="myTable" class="table">
        <thead class="thead-light">
        <tr>
        <th scope="col">Inicio</th>
        <th scope="col">Término</th>
        <th scope="col">Comuna</th>
        <th scope="col">Sector</th>
        <th scope="col">Tema</th>
        <th scope="col">Nombre organizador</th>
        <th scope="col">N° de fotos</th>
        </tr>
        </thead>
        <tbody>
        """
for p in datos:
    f=db.contador_fotos(p[6])
    
    tabla+=f""" 
        <tr>
        <td><a href="Informacion.py?id={p[6]}"> {p[0]}</a></td>
        <td><a href="Informacion.py?id={p[6]}"> {p[1]}</a></td>
        <td><a href="Informacion.py?id={p[6]}"> {p[2]}</a></td>
        <td><a href="Informacion.py?id={p[6]}"> {p[3]}</a></td>
        <td><a href="Informacion.py?id={p[6]}"> {p[4]}</a></td>
        <td><a href="Informacion.py?id={p[6]}"> {p[5]}</a></td>
        <td><a href="Informacion.py?id={p[6]}"> {f[0][0]}</a></td>
        </tr>
        """

tabla+="""
    </tbody>
    </table>
    <ul class="pagination pagination-sm justify-content-center" id="myPager"></ul>"""


js ="""
<body>
<script>
$.fn.pageMe = function(opts){
    var $this = this,
        defaults = {
            perPage: 5,
            showPrevNext: true,
            hidePageNumbers: false
        },
        settings = $.extend(defaults, opts);
    
    var listElement = $this.find('tbody');
    var perPage = settings.perPage; 
    var children = listElement.children();
    var pager = $('.pager');
    
    if (typeof settings.childSelector!="undefined") {
        children = listElement.find(settings.childSelector);
    }
    
    if (typeof settings.pagerSelector!="undefined") {
        pager = $(settings.pagerSelector);
    }
    
    var numItems = children.size();
    var numPages = Math.ceil(numItems/perPage);

    pager.data("curr",0);
    
    if (settings.showPrevNext){
        $('<li><a href="#" class="prev_link">«</a></li>').appendTo(pager);
    }
    
    var curr = 0;
    while(numPages > curr && (settings.hidePageNumbers==false)){
        $('<li><a href="#" class="page_link">'+(curr+1)+'</a></li>').appendTo(pager);
        curr++;
    }
    
    if (settings.showPrevNext){
        $('<li><a href="#" class="next_link">»</a></li>').appendTo(pager);
    }
    
    pager.find('.page_link:first').addClass('active');
    pager.find('.prev_link').hide();
    if (numPages<=1) {
        pager.find('.next_link').hide();
    }
  	pager.children().eq(1).addClass("active");
    
    children.hide();
    children.slice(0, perPage).show();
    
    pager.find('li .page_link').click(function(){
        var clickedPage = $(this).html().valueOf()-1;
        goTo(clickedPage,perPage);
        return false;
    });
    pager.find('li .prev_link').click(function(){
        previous();
        return false;
    });
    pager.find('li .next_link').click(function(){
        next();
        return false;
    });
    
    function previous(){
        var goToPage = parseInt(pager.data("curr")) - 1;
        goTo(goToPage);
    }
     
    function next(){
        goToPage = parseInt(pager.data("curr")) + 1;
        goTo(goToPage);
    }
    
    function goTo(page){
        var startAt = page * perPage,
            endOn = startAt + perPage;
        
        children.css('display','none').slice(startAt, endOn).show();
        
        if (page>=1) {
            pager.find('.prev_link').show();
        }
        else {
            pager.find('.prev_link').hide();
        }
        
        if (page<(numPages-1)) {
            pager.find('.next_link').show();
        }
        else {
            pager.find('.next_link').hide();
        }
        
        pager.data("curr",page);
      	pager.children().removeClass("active");
        pager.children().eq(page+1).addClass("active");
    
    }
    
};

$(document).ready(function(){
    
  $('#myTable').pageMe({pagerSelector:'#myPager',showPrevNext:true,hidePageNumbers:false,perPage:5});
    
});
</script>
"""
print(head+js+inicio+tabla)