# Con este codigo se crea un software que permite enviar
# Informacion por medio de bloutu a dispositivos cercanos
# Con la libreria de python 
# pip install scapy pushbullet.py
# radar_bluetooth.py
import asyncio
import threading
import pygame
import math
from bleak import BleakScanner

# ------------------------------
# Configuración del radar
# ------------------------------
WIDTH, HEIGHT = 600, 600
CENTER = WIDTH // 2, HEIGHT // 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Radar Bluetooth Dinámico")

# ------------------------------
# Función para convertir RSSI a distancia (aproximada)
# ------------------------------
def rssi_to_distance(rssi, tx_power=-59, n=2):
    """
    Convierte el RSSI en dBm a distancia aproximada en metros.
    tx_power: RSSI a 1 metro (default -59)
    n: factor de propagación (2 a 4 según entorno)
    """
    return 10 ** ((tx_power - rssi) / (10 * n))

# ------------------------------
# Hilo separado para escanear BLE
# ------------------------------
def scan_devices_thread(devices_list):
    async def scan_loop():
        while True:
            try:
                devices = await BleakScanner.discover()
                devices_list.clear()
                for d in devices:
                    devices_list.append((d.name or "Desconocido", d.rssi))
            except Exception as e:
                print("Error BLE:", e)
            await asyncio.sleep(5)  # escanear cada 5 segundos

    asyncio.run(scan_loop())

# Lista compartida entre hilos
devices_list = []

# Iniciar hilo BLE
ble_thread = threading.Thread(target=scan_devices_thread, args=(devices_list,), daemon=True)
ble_thread.start()

# ------------------------------
# Función para dibujar el radar
# ------------------------------
def draw_radar(devices):
    screen.fill((0, 0, 0))

    # Dibujar círculos concéntricos
    for r in [50, 100, 150, 200, 250]:
        pygame.draw.circle(screen, (0, 255, 0), CENTER, r, 1)

    # Dibujar línea central (opcional)
    pygame.draw.line(screen, (0, 255, 0), (CENTER[0]-250, CENTER[1]), (CENTER[0]+250, CENTER[1]), 1)
    pygame.draw.line(screen, (0, 255, 0), (CENTER[0], CENTER[1]-250), (CENTER[0], CENTER[1]+250), 1)

    # Dibujar dispositivos detectados
    for i, (name, rssi) in enumerate(devices):
        distance = rssi_to_distance(rssi)
        radius = min(int(distance * 25), 250)  # mapear distancia a píxeles
        angle = i * 30  # asignación angular simple para distribución

        x = CENTER[0] + int(radius * math.cos(math.radians(angle)))
        y = CENTER[1] + int(radius * math.sin(math.radians(angle)))

        # Color según distancia (cercano=rojo, lejos=amarillo)
        color = (255, max(0, 255 - int(radius*255/250)), 0)

        pygame.draw.circle(screen, color, (x, y), 6)
        # Mostrar nombre del dispositivo
        font = pygame.font.Font(None, 20)
        text_surface = font.render(name, True, (255, 255, 255))
        screen.blit(text_surface, (x + 8, y))

    pygame.display.flip()

# ------------------------------
# Bucle principal de Pygame
# ------------------------------
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_radar(devices_list)
    clock.tick(30)  # refresco 30 FPS
