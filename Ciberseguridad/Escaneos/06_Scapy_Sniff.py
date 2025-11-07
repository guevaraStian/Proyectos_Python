from scapy.all import IP, sniff

# Se guarda en una variable la interface que se va a validar en la victima
interface = "eth0"

# Se crea la funcion que realiza el sniff por paquetes cuando le indican una ip
def print_packet(packet):
    ip_layer = packet.getlayer(IP)
    print("[!] New packet: {src} -> {dst}".format(src=ip_layer.src, dst=ip_layer.dst))


# se ejecuta la funcion y se imprime en pantalla informacion 
print("Empieza a sniffing..")
sniff(iface=interface, filter="ip", prn=print_packet)
print("Para la sniffing")


