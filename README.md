Este corresponde a una página web sencilla, en la cual se puede agregar
información de actividades y las muestra, grafica información y resumen.
Esta página ha sido diseñada para ver desde notebook o computador, no para celular,
por lo que es posible que en caso de abrirlo desde un dispositivo móvil no se vean errores
de diseño.

Se usan las siguientes librerías:
-mapa usando Leaflet: https://leafletjs.com/
-Gráficos usando Highcharts: https://www.highcharts.com/blog/products/highcharts/

¿Que es cgi de python? https://www.geeksforgeeks.org/what-is-cgi-in-python/

Para poder ver la página se deben seguir los pasos:
1. Utilizar XAMPP, activar apache y sql.
2. Ir a http://localhost/phpmyadmin/index.php e importar los archivos BaseDeDatos.sql y DatosIniciales.sql. El nombre de la base de datos debe ser "tarea2".
3. Descargar el código y en consola escribir el comando "python -m http.server --bind localhost --cgi 8000"
4. Escribir en el navegador "http://[::1]:8000/cgi-bin/Portad.py" para ver la página.
5. Para ver las funcionalidades de la página agregar datos primero. 