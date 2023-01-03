//Función que dado C de la forma [0, 0, 8, 27, 2, 0, 15] crea el gráfico de líneas
function graf1(C){
    Highcharts.chart('foto11', {
        chart:{
            type:'line'
        },
        title: {
            text: 'N° de actividades por día de semana'
        },
        yAxis: {
            title: {
            text: 'Numero de actividades'
            }
        },
        xAxis: {
            categories : ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        },
        series: [{
            name: 'Actividades por día',
            data:[C[0], C[1], C[2],C[3],C[4],C[5],C[6]]
        }],
    });
}


function datos_2(temas_unicos,count){
  var length = temas_unicos.length;
  var cod="";
  for (i in temas_unicos){
    if (i==length-1){
      cod=cod+ 'name:'+Temas_unicos[i]+', y:'+count[i]

    } else {
      cod=cod+ 'name:'+Temas_unicos[i]+', y:'+count[i]+','
    }

  }
  return cod;
}
//Problema en esta función. Solo toma el primer dato 
//Recubiendo un dat de la forma{nombre:'música',y:5},{nombre:'deporte',y:1},{nombre:'ciencias',y:26},{nombre:'tecnología',y:1}
//Estos arreglos tienen un largo desconocido.
function segundografico(Temas_unicos,count){
  var m=Temas_unicos.length;
  i=0;
  const arr=[]
  while (i<m){
    let x={name:Temas_unicos[i],y:count[i]}
    arr.push(x);
    i=i+1;
  
    
  }console.log(arr)
    Highcharts.chart('foto22', {
        chart: {
          plotBackgroundColor: null,
          plotBorderWidth: null,
          plotShadow: false,
          type: 'pie'
        },
        title: {
          text: 'N° de actividades por tipo'
        },
        tooltip: {
          pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        accessibility: {
          point: {
            valueSuffix: '%'
          }
        },
        plotOptions: {
          pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
              enabled: true,
              format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
          }
        },series: [{
            name: 'Brands',
            colorByPoint: true,
            data: arr         
        }]
      });
}

//Genera el gráfico de barras tomando como parámetro, por ejemplo, 
//d=[0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0] 
function tercergrafico(d){
    Highcharts.chart('foto33', {
        chart: {
          type: 'column'
        },
        title: {
          text: 'Horario de actividades por mes'
        },
        xAxis: {
          categories: [
            'Ene',
            'Feb',
            'Mar',
            'Abr',
            'May',
            'Jun',
            'Jul',
            'Ago',
            'Sep',
            'Oct',
            'Nov',
            'Dic'
          ],
          crosshair: true
        },
        yAxis: {
          min: 0,
          title: {
            text: 'N° de actividades'
          }
        },
        plotOptions: {
          column: {
            pointPadding: 0.2,
            borderWidth: 0
          }
        },
        series: [{name:'mañana', data:d[0]},
        {name:'Mediodia', data:d[1]},
        {name:'tarde', data:d[2]}]
      });

}




