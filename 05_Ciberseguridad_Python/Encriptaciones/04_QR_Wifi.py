# Primero se instala wifiqrcode con el siguiente comando "pip install wifi-qrcode-generator"
from wifi_qrcode_generator import wifi_qrcode

# Con esta libreria, se crea el codigo qr y dentro de el codigo la informacion de la conexion a wifi
Codigo_qr = wifi_qrcode("nombre_de_wifi", hidden=False, authentication_type="WPA", password="Contraseña_wifi")
Imagen_qr = Codigo_qr.make_image()
Imagen_qr.save("wifi_qr_code.png")







