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

7- Creo una carpeta "project" y ejecuto "django-admin startproject config ." para ejecutar el proyecto (crea una carpeta "config" que es la carpeta de configuracion)

8- Una vez ejecutado, entro a project-config-settings.py y selecciono el idioma y la zona horaria (en mi caso, EN (ingles) y ET (Eastern Time))

9- Creo aplicaciones con "django-admin startapp core" 
    La aplicacion general (CORE) es la que contiene el menu, los estilos, la base de html, los estilos, el login, los urls y las vistas.
    Creo las aplicaciones segun las necesidades de mi proyecto (en mi caso, About Us, FAQs, Get Started)
    Los nombres de las aplicaciones deben ser con guion bajo, sin caracteres especiales, en minuscula, y no ser nombres genericos ni usar palabras claves de django o python





