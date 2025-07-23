# En el siguiente codigo de programacion, se muestra una forma sencilla
# De extraer un archivo texto en una imagen png
# Pirmero descargamos y usamos las librerias
# Primero se instala zipfile con el siguiente comando 
# "pip install Fernet"

import os
from PIL import Image, ImageDraw, ImageFont
import piexif
from cryptography.fernet import Fernet


from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os

# Se ingresan texto en la imagen
def insertar_texto_visible(imagen, texto, posicion=(10, 10), color=(255, 255, 255)):
    draw = ImageDraw.Draw(imagen)
    font = ImageFont.load_default()
    draw.text(posicion, texto, fill=color, font=font)
    return imagen

# Se ingresa el texto a los metadatos
def insertar_metadato(imagen, texto):
    try:
        exif_dict = piexif.load(imagen.info.get('exif', b''))
    except Exception:
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

    # Codificar como UserComment (ID 37510)
    user_comment = texto.encode('utf-8')
    exif_dict["Exif"][piexif.ExifIFD.UserComment] = b'\x00\x00' + user_comment
    return piexif.dump(exif_dict)


# Se crea la llave basandose en un texto que le ingresa
def generar_clave_fernet_desde_texto(texto: str, salt_constante: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt_constante,
        iterations=100_000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(texto.encode()))

# En el main se ejecutan las funciones
def main():
    print("!! Se empieza a encriptar la informacion y a guardarla en la imagen !!")

    # 1. Preguntar ruta de imagen
    ruta_imagen = input("Ruta de la imagen (ej. foto.jpg): ").strip()
    if not os.path.exists(ruta_imagen):
        print("(-) No se encontro la imagen.")
        return
    # Encriptar
    # Generar clave
    texto_plano = input('Por favor ingresar el texto que se va a guardar: ')
    llave = input('Por favor ingresar el la LLAVE de encriptacion : ')

    # Salt constante (¡debe ser exactamente igual siempre!)
    salt_fijo = b'salt-fijo-16bytes'  # 16 bytes exactos
    # Generar clave Fernet
    clave = generar_clave_fernet_desde_texto(llave, salt_fijo)
    texto_llave_str = clave.decode()

    fernet = Fernet(texto_llave_str)
    # Encriptar (devuelve bytes base64)
    texto_cifrado_bytes = fernet.encrypt(texto_plano.encode())
    # Convertir bytes a string para guardar como texto plano en archivo
    texto_cifrado_str = texto_cifrado_bytes.decode()
    print("(+) Texto encriptado:", texto_cifrado_str)
    # Abrir la imagen
    try:
        imagen = Image.open(ruta_imagen).convert("RGB")
    except Exception as e:
        print(f"(-) No se abrio la imagen: {e}")
        return

    # Se guarda la informacion en la imagen
    imagen = insertar_texto_visible(imagen, texto_cifrado_str)

    # Se guardan los datos en el metadatos
    nueva_ruta = f"editada_{os.path.basename(ruta_imagen)}"
    try:
        if ruta_imagen.lower().endswith((".jpg", ".jpeg")):
            exif_bytes = insertar_metadato(imagen, texto_cifrado_str)
            imagen.save(nueva_ruta, exif=exif_bytes)
        else:
            imagen.save(nueva_ruta)
        print(f"(+) La imagen fue guardada sin problema: {nueva_ruta}")
    except Exception as e:
        print(f"(-) No se guardo la imagen : {e}")

if __name__ == "__main__":
    main()










