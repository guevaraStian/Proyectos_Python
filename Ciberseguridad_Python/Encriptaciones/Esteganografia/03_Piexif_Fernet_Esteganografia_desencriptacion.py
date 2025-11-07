# En el siguiente codigo de programacion, se muestra una forma sencilla
# De extraer un archivo texto en una imagen png
# Pirmero descargamos y usamos las librerias
# Primero se instala zipfile con el siguiente comando 
# "pip install Fernet"

from PIL import Image
import piexif
from cryptography.fernet import Fernet

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os

# Se extraen los metadatos de la imagen
def extraer_metadato(ruta_imagen):
    try:
        imagen = Image.open(ruta_imagen)
        exif_dict = piexif.load(imagen.info.get('exif', b''))

        # Extraer UserComment (ID 37510)
        user_comment = exif_dict["Exif"].get(piexif.ExifIFD.UserComment, None)
        if user_comment:
            # Eliminar encabezado '\x00\x00' y decodificar
            texto = user_comment[2:].decode('utf-8', errors='ignore')
            return texto
        else:
            return None
    except Exception as e:
        print(f"❌ Error al leer metadato: {e}")
        return None

# Se genera la llave fernet con basandose en un texto que le ingresan
def generar_clave_fernet_desde_texto(texto: str, salt_constante: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt_constante,
        iterations=100_000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(texto.encode()))


# En el main se ejecutan las funcion
def main():
    print("!!  Empieza a leer los metadatos de la imagen !!")

    # Se solicita la ubicacion de la imagen
    ruta_imagen = input("Ruta de la imagen (ej. editada_foto.jpg): ").strip()
    if not os.path.exists(ruta_imagen):
        print("(-) No se encontro la imagen")
        return

    if not ruta_imagen.lower().endswith((".jpg", ".jpeg")):
        print("(-) Solo se usan imagenes jpg")
        return

    # Se extraen los datos de la imagen
    texto_encriptado = extraer_metadato(ruta_imagen)
    print(texto_encriptado)
    if texto_encriptado:
        # Desencriptar
        # Generar clave
        llave = input('Por favor ingresar la LLAVE de encriptacion : ')
        # Salt constante (¡debe ser exactamente igual siempre!)
        salt_fijo = b'salt-fijo-16bytes'  # 16 bytes exactos
        # Generar clave Fernet
        clave = generar_clave_fernet_desde_texto(llave, salt_fijo)

        fernet = Fernet(clave)
        texto_desencriptado = fernet.decrypt(texto_encriptado).decode()
        print("(+) Texto desencriptado:", texto_desencriptado)
    else:
        print("(-) No se encontró ningún dato en el metadato.")

if __name__ == "__main__":
    main()

