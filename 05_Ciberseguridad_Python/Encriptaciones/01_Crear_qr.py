# Primero se instala qrcode con el siguiente comando  "pip install qrcode"
import qrcode

#Se solicita la informacion y se crea la variable con el nombre del archivo
contenido = input("Por favor ingrese la informacion del QR: ")
nombre_archivo = "qr.png"

#Usando el make de qrcode se guarda
img = qrcode.make(contenido)
img.save(nombre_archivo)

