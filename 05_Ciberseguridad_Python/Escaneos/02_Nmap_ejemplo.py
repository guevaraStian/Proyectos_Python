# Primero se instala python-nmap con el siguiente comando "pip3 install python-nmap"
# Es necesario que en la pagina nmap.org descargue la ultima version de nmap
import nmap

#En las siguientes lineas, se puede ver informacion de nmap
nmap.__version__
dir(nmap)
dir(nmap.PortScanner)

# Guardamos la configuracion de la opcion portsacanner de nmap
ep = nmap.PortScanner()

#Agregamos la ip del dispositivo que vamos a escanear, tambien los puertos que requerimos ver y su version
ep.scan('192.168.0.10','21,22,80,443,3389','-v')

# Con el siguiente codigo podemos ver en pantalla el comando nmap de la solicitud
ep.command_line()

# En este codigo se muestra la cantidad de dispositivos finales que hay en la consulta preparada
ep.all_hosts()

# Con este codigo se da un rango de dispositivos finales de 10 a 15 por los mismos puertos
ep.scan('192.168.0.10-15','21,22,80,443,3389', '-sV')

#Vemos el resultado detallado de la consulta
ep['192.168.0.10']

# Aqui vemos el estado de la ip
ep['192.168.0.10'].state()

#Informacion de los protocolos 
ep['192.168.0.10'].all_protocols()

#Guarda la informacion en un excel
ep.csv()