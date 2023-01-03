
//Recibe como parámetro una lista con todas las comunas.
function createMap(comunas,conteo,cordenadas,informacion){

    var map = L.map('map').setView([-33.4500000, -70.6666667], 4);
    var popup = L.popup();
    L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    var length = comunas.length;
    j=0;
    while (j<length){
        console.log("COMUNA")
        console.log(j)
        let informacion_tabla=informacion[j]
        console.log(informacion_tabla)
        cm=comunas[j];
        cn=conteo[j];
        cord=cordenadas[j];
        let titulo= cm+':Se tienen '+cn+" imágenes"
        var marker = L.marker(cord).addTo(map).bindPopup('');
        marker.on('mouseover', function(evt) {
            evt.target.bindPopup(titulo).openPopup();
            })
            marker.on('click', function(evt) {
                evt.target.bindPopup(create_tabla(informacion_tabla)).openPopup();
            });

        //L.marker(cord,{'title':titulo}).addTo(map)
        //console.log(informacion[j][0],informacion[j][1],informacion[j][2],informacion[j][3])
        //.on('click',onMapClick());
        j=j+1
    }
    function onMapClick(e) {{
        popup
            .setLatLng(e.latlng)
            .setContent('')
            .openOn(map);
    }}
    
    map.on('click', onMapClick);
}

//recibe datos de la comuna como un arreglo.
function create_tabla(inf){
    console.log("En tabla se tienen los datos")
    console.log(inf)
    let dat;
    let tabla= '<table class="table table-hover">'+
                '<thead>'+
                    '<tr>'+
                        '<th scope="col">Inicio</th>'+
                        '<th scope="col">Tema</th>'+
                        '<th scope="col">Sector</th>'+
                    '</tr>'+
                '</thead>'
            console.log("INFORMACOIN")
            console.log(inf[0])

    for (k in inf){
        console.log("DATO")
        dat=inf[k]
        console.log(dat)
        tabla=tabla+'<tr>'+
                    '<td><a href="Informacion.py?id='+dat[3]+'"> '+dat[0]+'</td>'+
                    '<td><a href="Informacion.py?id='+dat[3]+'+">'+dat[1]+'</td>'+
                    '<td><a href="Informacion.py?id='+dat[3]+'+"> '+dat[2]+'</td>'+
                '</tr>'
    }
   
    return tabla;
}