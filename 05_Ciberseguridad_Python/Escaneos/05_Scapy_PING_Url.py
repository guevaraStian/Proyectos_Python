from scapy.all import IP, ICMP, sr1

def ping(host):
    # Se guarda en una variable la respuesta, de un icmp a un host o url
    packet = IP(dst=host)/ICMP()
    # Se guarda en una variable la repuesta de un sr1 con sus variables asignadas
    response = sr1(packet, timeout=2, verbase=0)
    # Si dio respuesta el ping entonces da una respuesta y si no, da otra
    if response:
        return f"{host} Esta en linea"
    else:
        return f"{host} No esta en linea"

url = input("Por favor, la direccion url de la pagina web (ej: www.google.com) : ")
# url = "www.google.com"
result = ping(url)
print(result)

