# Coder_Petrochelli_BT
3ra_Pre-entrega_PF_Coderhouse (enfocada en website proyecto para trabajo)

1-Creo el proyecto en Github

2-Hago Gitclone y el directorio de mi proyecto Github
    git clone directorio "https" de github
    
    Gitignore no se sube a Python ya que son archivos temporales

4- Creo entorno virtual (entorno aislado para cuando instalemos Django, no lo mezcle con lo global)
    python -m venv .venv (-m significa que voy a ejecutar un modulo de python. ".venv" es el nombre del entorno virtual. 
    Puedo renombrarlo como quiero pero debere agregar ese nombre de entorno en archivo gitignore ("Enviromnents"))

5-Ejecuto entorno virtual con "CTRL+SHIFT+P" y tipear Python Interpreter (seleccionar interprete - Recommended Python .venv.)
    Luego cierro terminal y vuelvo a abrir, y me aparece en color verde (.venv)

6- Una vez en el entorno virtual, instalo Django con "pip install django"

PARA NO INSTALAR TODO DE NUEVO, EN EL DIRECTORIO RAIZ, PUEDO EJECUTAR "pip freeze >> requirements.txt"
Se abre un archivo "requirements.txt" que contiene todo lo que necesito para mi proyecto. Si no quiero instalar todo individualmente, puedo ejecutar "pip install -r requirements.txt" que instala todo.

7- Creo una carpeta "project" y ejecuto "django-admin startproject config ." para ejecutar el proyecto (crea una carpeta "config" que es la carpeta de configuracion)

8- Una vez ejecutado, entro a project-config-settings.py y selecciono el idioma y la zona horaria (en mi caso, EN (ingles) y ET (Eastern Time))

9- Creo aplicaciones con "django-admin startapp core" 
    La aplicacion general (CORE) es la que contiene el menu, los estilos, la base de html, los estilos, el login, los urls y las vistas.
    Creo las aplicaciones segun las necesidades de mi proyecto (en mi caso, About Us, FAQs, Get Started)
    Los nombres de las aplicaciones deben ser con guion bajo, sin caracteres especiales, en minuscula, y no ser nombres genericos ni usar palabras claves de django o python

10- Registro las aplicaciones en project>config>settings.py> installed apps, y las nombro con comillas, y comas

11- En la carpeta principal Core, creo una carpeta "templates", y dentro de esa carpeta, creo otra carpeta "core". 
    Dentro de core, creamos un nuevo archivo "index.html". 
    Hago lo mismo para mis otras aplicaciones (faqs, about_us, get_started), para evitar ambiguedades.
        Para crear mi archivo html, en core>index, presiono SHIFT+1+TAB
    Nombro cada una de las aplicaciones con h1+tab (en mi caso, Home (en core), About Us, FAQs y Get Started)

12- Agrego las urls de "Config" en la carpeta "core".
    Borro comentarios y admin (porque lo tiene config)
    
    En views, defino la funcion core como: 
    
    from django.shortcuts import render

    def home(request):
        return render(request, "core/index.html")

    La palabra render, significa que html va a dibujar o renderizar. Al ingresar a un determinado url, se ejecutara esa funcion. 
    
    Importo la views a mi archivo urls.py y creo la url:
    from . import views

    urlpatterns = [
     path('core/', views.home),
    ]

    En la carpeta urls de config, incluyo el nombre del paquete. Como core es el principal, pongo el primer termino sin nombre:
    path('',include('core.urls'))

    Hago lo mismo en urls de mi proyecto en core, elimino la palabra "core" como sigue:
    urlpatterns = [
    path('', views.home),
    ]

    Luego, agrego los paths de las otras aplicaciones:

       path('about_us', include('about_us.urls')),
       path('faqs', include('faqs.urls')),
       path('get_started', include('get_started.urls')),


13- Copio los archivos urls y views de config a las otras aplicaciones y en views, cambio el segundo argumento de la funcion (ej. about us)

    def home(request):
        return render(request, "about_us/index.html")

    El archivo urls.py queda igual para todas las aplicaciones.

14- NAVEGAR ENTRE LAS URLS
    Le doy nombre a los archivos urls de cada app con: app_name="about_us", etc.
    Agrego un argumento mas en urlspatterns que sea name="index" para cada archivo urls.py de cada aplicacion
    En index.html de core/templates, agrego:
    <ul>
        <li><a href="{% url 'about_us:index' %}">About Us</a></li>
        <li><a href="{% url 'faqs:index' %}">FAQs</a></li>
        <li><a href="{% url 'get_started:index' %}">Get Started</a></li>
    </ul>

    En cada archivo index de cada app, puedo hacer lo mismo ingresando el siguiente codigo:
    <a href="{% url 'core:index' %}">Back to home</a>

15- Para evitar duplicar codigo, creo un archivo base.html en templates/core
    Pongo alli dos bloques que son partes de codigo que son personalizables entre apps. El primer bloque"contenido_titulo" y el segundo "contenido"
    En el index de core, elimino todo lo comun (a), y con extend, hago una herencia de html(b).
    (a)
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    </head>
    <body>

    </body>
    </html>

    (b)
    {% extends 'core/base.html' %}
    y reutilizo los bloques de base

    Puedo tambien agregar un nuevo bloque en base.html con un footer (legal disclaimer, o direccion, info, etc. de la empresa)

16- Modelos de Django y Bases de Datos Relacionales:
    Creamos dos modelos en la aplicacion Get Started con el archivo models.py
    Creo las migraciones con "python manage.py makemigrations"
    Esto genera el archivo "0001_initial.py" en la carpeta Get Started (en mi caso), y es un archivo que no hay que tocar.
    Para que haga las modificaciones en la base de datos, hay que ejecutar "python manage.py migrate"
    Esta accion crea las tablas en el archivo db.sqlite3 del proyecto y ahi vamos a poder ver la informacion.

17- Administrador
    En Get Started, abro archivo "admin.py" y registro alli mis modelos.
    Importo los modelos y los registro como sigue:

    from . import models

    admin.site.register(models.Region)
    admin.site.register(models.Country)
    admin.site.register(models.User)

    Creacion de superusuario con: python manage.py createsuperuser
    ingresar nombre (admin), email (opcional) y password

    En el servidor, puedo agregar paises, usuarios, regiones. Para verlos, voy a models.py
    
    El archivo "modelos_tipos_de_datos" contiene informacion relevante para crear las clases.
    Este archivo se puede previsualizar con CTRL+MAYUS+V

18- Front-end: LOOK & FEEL 
    Selecciono una plantilla de https://startbootstrap.com
    La descargo y en Core -carpeta que contiene templates/core-, creo una carpeta "static" y dentro una core, y pego alli el archivo css, assets y js
    index.html queda en templates/core, y es el archivo que utiliza los estilos de bootstrap (renombro el archivo index anterior como index2 para no "pisarlo")
    el archivo favicon tiene que tener formato .ico. Para esto, puedo trabajar en paint y cambiar extension.
    Si ejecuto el servidor, aparece la plantilla cargada pero sin formato>>> archivos estaticos (css, javascript, videos, imagenes), django los manipula como si fuera una url.

19- Cargar estilos, fav icon, etc: para cargar, se usa en index descargado de Internet, la funcion load static.
    Modificar los archivos estaticos css, js, etc. apagar y reiniciar el servidor, ya que estos archivos no se reinician automaticamente.

20- Customizar contenido en archivo index.html (titulo, leyendas, clases, etc.)
    
21- Barra de navegacion navbar: para ir descomponiendo el index, creo un archivo navbar.html en core, y pego alli todo el contenido de navbar. Luego, uso el tag "include core/navbar.html" en index para "llamar al archivo navbar.

22- Customizo secciones navegando por index (agrego imagenes descargandolas para que siempre esten disponibles, cambio contenido, etc.)

23- En index, agrego bloques anteriores de base, y elimino ese archivo. Renombro el index a base.
    Vuelvo a renombrar index2 a index para que funcionen los paths creados anteriormente.
    Este paso no se si es necesario-preguntar si se puede eliminar y crear urls en el mismo template que bajamos de bootstrap.

24- Para usar los links de bootstrap en nuestras aplicaciones, ir a navbar y renombrar segun nuestra web. El simbolo #! significa que el link no funciona. Puedo reemplazar por la url

Creamos archivo about.html que extiende de core/base.html
en urls agrego la url about y antes creo la funcion en views
Luego inserto urls en cada funcion #Falta crear contacts y chequear que funcione bien la dinamica de la pagina.
No me gusta el display

25- Ver clientes directo desde html en el servidor - chequear, no anda!!!!

26- en views de get_started: crear countries and regions
NO ME FUNCIONA - PREGUNTAR QUE HICE MAL!!!!!
Busqueda del minuto 1.52 de clase 28/11 no lo hice porque no funciona lo anterior

Ver archivo filtros para esto