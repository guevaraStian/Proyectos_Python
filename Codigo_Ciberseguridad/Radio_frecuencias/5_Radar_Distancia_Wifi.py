# En este ejemplo de codigo se muestra la creacion de un radar
# con la distancia de los dispositivos y el router
# pip install matplotlib
import subprocess
import re
import random
import math
import matplotlib.pyplot as plt

# En la siguiente funcion se ejecuta arp -a para ver que dispositivos estan conectados
def escanear_dispositivos():
    result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    dispositivos = []
    for line in result.stdout.splitlines():
        match = re.search(r'(\d+\.\d+\.\d+\.\d+)\s+([\w-]+)\s+(\w+)', line)
        if match:
            ip = match.group(1)
            dispositivos.append(ip)
    return dispositivos
# Distancia ficticia entre 2 y 10 metros (simulada)
def estimar_distancia_fake():
    return round(random.uniform(2, 10), 2)


# En la siguiente funcion se crea la grafica con las distancias entre el router y los dispositivos conectados
def mostrar_radar(dispositivos_info):
    fig, ax = plt.subplots()
    ax.set_title("Radar WiFi - Estimación Ficticia de Distancias")
    ax.set_xlim(-12, 12)
    ax.set_ylim(-12, 12)
    ax.set_aspect('equal')
    ax.grid(True)

    for ip, distancia in dispositivos_info:
        angle = random.uniform(0, 2 * math.pi)
        x = distancia * math.cos(angle)
        y = distancia * math.sin(angle)
        ax.plot(x, y, 'bo')
        ax.text(x, y, f"{ip}\n{distancia} m", fontsize=8)

    plt.show()

# En la funcion main se ejecutan las funciones creadas anteriormente
def main():
    dispositivos = escanear_dispositivos()
    dispositivos_info = []

    for ip in dispositivos:
        distancia = estimar_distancia_fake()
        dispositivos_info.append((ip, distancia))
        print(f"{ip} -> Distancia simulada: {distancia} m")

    mostrar_radar(dispositivos_info)

if __name__ == "__main__":
    main()








