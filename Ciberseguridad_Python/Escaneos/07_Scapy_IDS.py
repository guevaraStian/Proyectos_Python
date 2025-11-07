# Con este codigo se realiza un IDS detector de animalias en la red
# Con la libreria de python Scapy
from scapy.all import sniff, IP, TCP
from collections import defaultdict
import time

# Se crean las variables necesarias
connection_tracker = defaultdict(int)
PORT_SCAN_THRESHOLD = 20
TIME_WINDOW = 60  # segundos
ip_timestamps = defaultdict(list)

# Se crea la funcion del IDS
def detect_intrusion(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_src = packet[IP].src
        tcp_flags = packet[TCP].flags
        current_time = time.time()

        # Solo analizamos paquetes SYN
        if tcp_flags == "S":
            ip_timestamps[ip_src].append(current_time)
            # Filtra eventos viejos
            ip_timestamps[ip_src] = [t for t in ip_timestamps[ip_src] if current_time - t < TIME_WINDOW]

            # Si se excede el umbral, hay posible escaneo
            if len(ip_timestamps[ip_src]) > PORT_SCAN_THRESHOLD:
                print(f"[ALERTA] Posible escaneo de puertos detectado desde {ip_src}")
                ip_timestamps[ip_src] = []  # Reset para evitar spam de alertas

# Iniciar captura (puedes cambiar "eth0" por tu interfaz de red)
print("IDS corriendo... Presiona Ctrl+C para detener.")
sniff(filter="tcp", prn=detect_intrusion, store=0)