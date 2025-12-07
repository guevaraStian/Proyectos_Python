# Con este codigo se crea un software que crea un radar 
# Se actualiza cada 5 segundos con la ubicacion de los bloutube
# Informacion de bluetooth a dispositivos cercanos
# pip install bleak
import asyncio
import threading
import pygame
import math
from bleak import BleakScanner

# Lo primero es configurar las variables del radas
WIDTH, HEIGHT = 600, 600
CENTER = WIDTH // 2, HEIGHT // 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Se esta ejecutando el radar Bluetooth con Distancia")

# En esta funcion se calcula la distancia con la variable RSSI
def Distancia_Con_RSSI(rssi, tx_power=-59, n=2):
    return 10 ** ((tx_power - rssi) / (10 * n))

# La siguiente funcion scanea los bluetooth cercanos
def Escaner_Bluetooth_Cercanos(Lista_Dispositivos_Cercanos):
    async def scan_loop():
        while True:
            try:
                Dispositivos = await BleakScanner.discover()
                Lista_Dispositivos_Cercanos.clear()
                for d in Dispositivos:
                    Lista_Dispositivos_Cercanos.append((d.name or "Desconocido", d.rssi))
            except Exception as e:
                print("Error BLE:", e)
            await asyncio.sleep(5)  # escanear cada 5 segundos

    asyncio.run(scan_loop())

# Lista compartida entre hilos
Lista_Dispositivos_Cercanos = []

# Iniciar hilo BLE
ble_thread = threading.Thread(target=Escaner_Bluetooth_Cercanos, args=(Lista_Dispositivos_Cercanos,), daemon=True)
ble_thread.start()

# Con la siguiente funcion se grafica la distancia
def Graficador_Radar(Dispositivos):
    screen.fill((0, 0, 0))

    # Dibujar círculos concéntricos
    for r in [50, 100, 150, 200, 250]:
        pygame.draw.circle(screen, (0, 255, 0), CENTER, r, 1)

    # Dibujar líneas centrales
    pygame.draw.line(screen, (0, 255, 0), (CENTER[0]-250, CENTER[1]), (CENTER[0]+250, CENTER[1]), 1)
    pygame.draw.line(screen, (0, 255, 0), (CENTER[0], CENTER[1]-250), (CENTER[0], CENTER[1]+250), 1)

    # Fuente para mostrar texto
    font = pygame.font.Font(None, 20)

    # Dibujar dispositivos detectados
    for i, (name, rssi) in enumerate(Dispositivos):
        Distancia = Distancia_Con_RSSI(rssi)
        Radio_distancia = min(int(Distancia * 25), 250)  # mapear distancia a píxeles
        Angulo_Radar = i * 30  # distribución angular simple

        x = CENTER[0] + int(Radio_distancia * math.cos(math.radians(Angulo_Radar)))
        y = CENTER[1] + int(Radio_distancia * math.sin(math.radians(Angulo_Radar)))

        # Color según distancia
        color = (255, max(0, 255 - int(Radio_distancia*255/250)), 0)

        pygame.draw.circle(screen, color, (x, y), 6)

        # Mostrar nombre y distancia en metros
        text_surface = font.render(f"{name} ({Distancia:.1f}m)", True, (255, 255, 255))
        screen.blit(text_surface, (x + 8, y))

    pygame.display.flip()

# Con el siguiente bucle se ejecuta el programa
Ejecutandose = True
clock = pygame.time.Clock()

while Ejecutandose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Ejecutandose = False

    Graficador_Radar(Lista_Dispositivos_Cercanos)
    clock.tick(30)  # refresco 30 FPS
