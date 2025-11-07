Proyectos DJANGO

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)

Los pasos para poner en ejecución son los siguientes
Ir a la pagina web de Python y Git, luego descargarlo para tu sistema operativo, escoger la opción "add path" con el fin de poder ejecutar comandos de Python en la terminal de comandos

```Pagina web
https://www.python.org/downloads/
https://git-scm.com/downloads
```
Luego de tener instalado Python podemos ejecutar los siguientes comandos hasta llegar a la carpeta del proyecto y estando ahí ejecutamos los siguientes codigos

```Terminal de comandos
cd    
python --version
pip --versión
pip install --upgrade pip
pip install django==2.1.7
```

Despues de haber instalado python y confirmar la version, instalamos git y descargamos el proyecto.
```Terminal de comandos
git --version
git init
git clone https://github.com/guevaraStian/Tutorial_Django.git
git push origin master
```

El siguiente comando es para crear el proyecto django
```Terminal de comandos
django-admin startproject proyecto1
```

Luego se ejecuta el proyecto con los siguientes comandos
```Terminal de comandos
cd Tutorial_Django
python manage.py runserver
```

Luego que el proyecto ya se este ejecutando se darán diferentes respuestas en consola o pestañas emergentes
```
```Pagina web
http://localhost:8000
http://127.0.0.1:8000
```

- El archivo settings.py -> templates -> se anexa a dirs la direccion de la carpeta, pero con los "/" de dividir (esta direccion se consigue dando click en guardar como y luego en links)

- En archivo llamado views.py ->  importamos de django http, HttpResponse ,template, context , template.loader, get_template
También anexamos a el arrchivo views.py -> crea la def (request) , se pone la direccion del get_template('miplantilla.html') 
Por ultimo en views.py -> se renderisa la variable plantillarender=plantilla.render() y se retorna la variable en HttpResponse

- Crear la plantilla html
url -> importar funciones asi "from nombreproyecto.views import saludo" y en urlpatterns -> path('saludo/', saludo),
probar

```Terminal de comandos
python manage.py createsuperuser 
python manage.py makemigrations
python manage.py migrate
```
