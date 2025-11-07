# En el siguiente codigo de programacion, se muestra una forma sencilla
# De guardar un archivo texto en una imagen png
# Pirmero descargamos y usamos las librerias
# Primero se instala zipfile con el siguiente comando 
# "pip install zipfile"

import zipfile
from PIL import Image
from cryptography.fernet import Fernet

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os

# La siguiente funcion sirve para crear un archivo texto con una informacion
def crear_txt(nombre_txt):
    with open(nombre_txt, 'w') as f:
        # Encriptar
        # Generar clave
        # clave =  b'yRsR02RWd4ePvfb6LFYI9etNYVu7vF0A1TVVjoi9-ws='
        texto_plano = input('Por favor ingresar el texto que se va a guardar: ')
        llave = input('Por favor ingresar el la LLAVE de encriptacion : ')
        # Salt constante (¡debe ser exactamente igual siempre!)
        salt_fijo = b'salt-fijo-16bytes'  # 16 bytes exactos
        # Generar clave Fernet
        clave = generar_clave_fernet_desde_texto(llave, salt_fijo)
        fernet = Fernet(clave)
        # Encriptar (devuelve bytes base64)
        texto_cifrado_bytes = fernet.encrypt(texto_plano.encode())
        # Convertir bytes a string para guardar como texto plano en archivo
        texto_cifrado_str = texto_cifrado_bytes.decode()
        print("(+) Texto encriptado:", texto_cifrado_str)
        f.write(texto_cifrado_str)
    print(f" (+) El archivo .txt se creo sin problemas: {nombre_txt}")

# Con esta funcion se crea una imagen con un nombre indicado
def crear_imagen_png(nombre_imagen):
    img = Image.new('RGB', (200, 200), color='lightgreen')
    img.save(nombre_imagen)
    print(f"(+) Imagen PNG creada: {nombre_imagen}")

# En este codigo se muestra como meter un archivo texto a un archivo comprimido zip
def crear_zip(nombre_zip, archivo_txt):
    with zipfile.ZipFile(nombre_zip, 'w') as zipf:
        zipf.write(archivo_txt)
    print(f"(+) El ZIP creado sin problema: {nombre_zip}")

# En este codigo se explica como ingresarle el texto a la imagen con un archivo zip
def fusionar_imagen_y_zip(imagen_png, archivo_zip, salida_png_con_zip):
    with open(imagen_png, 'rb') as img_file:
        datos_img = img_file.read()

    with open(archivo_zip, 'rb') as zip_file:
        datos_zip = zip_file.read()

    with open(salida_png_con_zip, 'wb') as salida:
        salida.write(datos_img)
        salida.write(datos_zip)

    print(f"(+) La imagen quedo con el zip comprimido adentro: {salida_png_con_zip}")


def generar_clave_fernet_desde_texto(texto: str, salt_constante: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt_constante,
        iterations=100_000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(texto.encode()))


# EJECUTAR FLUJO COMPLETO
crear_txt('Texto_a_guardar.txt')
crear_imagen_png('imagen_base.png')
crear_zip('archivo.zip', 'Texto_a_guardar.txt')
fusionar_imagen_y_zip('imagen_base.png', 'archivo.zip', 'imagen_con_mensaje.png')


