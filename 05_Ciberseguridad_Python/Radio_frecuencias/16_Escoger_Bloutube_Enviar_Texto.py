# Con este codigo se crea un software que permite enviar
# Informacion por medio de bloutu a dispositivos cercanos
# Con la libreria de python 
# pip install bluetooth

import bluetooth

# Dirección del dispositivo receptor
bd_addr = "01:02:03:04:05:06"  
port = 1  

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

mensaje = "Hola desde Python"
sock.send(mensaje)  # Se envía en bytes automáticamente
sock.close()