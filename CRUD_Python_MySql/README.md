CRUD Python MySQL Flask Windows Ubuntu


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySql](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) - 
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white) - 
![Microsoft](https://img.shields.io/badge/Microsoft-0078D4?style=for-the-badge&logo=microsoft&logoColor=white) 
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

Los pasos para poner en ejecución son los siguientes
Ir a la pagina web de Python y descargarlo para tu sistema operativo, escoger la opción "add path" con el fin de poder ejecutar comandos de Python en la terminal de comandos

```Pagina web
https://www.python.org/downloads/
https://git-scm.com/downloads
```

Vamos a la pagina web de MySQL y descargamos el ejecutable MSI y lo ejecutamos, luego de finalizar la instalación abrimos el MySQL Workbench

```Pagina web
https://www.mysql.com/downloads/
```

Luego de tener instalado Python podemos ejecutar los siguientes comandos hasta llegar a la carpeta del proyecto y estando ahí ejecutamos los siguientes codigos

```Terminal de comandos
cd
python --version
pip --version
```

Despues de haber instalado python y confirmar la version, instalamos git y descargamos el proyecto.
```Terminal de comandos
git --version
git init
git clone https://github.com/guevaraStian/CRUD_Python_MySql.git
cd CRUD_Python_MySql
git push origin master
```

Posteriormente ingresamos a la carpeta creada e instalamos las librerias y ejecutamos el proyecto.

```Terminal de comandos
pip install flask flask_mysqldb
python app.py
```

Luego que el proyecto ya se este ejecutando, podemos verlo funcionar en la siguiente ruta url

```Pagina web
http://localhost:3000
http://127.0.0.1:3000
```

