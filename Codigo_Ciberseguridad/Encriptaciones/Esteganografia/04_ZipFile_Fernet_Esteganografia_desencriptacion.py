# En el siguiente codigo de programacion, se muestra una forma sencilla
# De extraer un archivo texto en una imagen png
# Pirmero descargamos y usamos las librerias
# Primero se instala zipfile con el siguiente comando 
# "pip install zipfile"
import zipfile
import os


from cryptography.fernet import Fernet

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os

# Con el siguiente codigo se extrae un comprimido de adentro de la imagen
def extraer_zip_de_imagen(imagen_con_zip, salida_zip):
    with open(imagen_con_zip, 'rb') as archivo:
        datos = archivo.read()

    # Fin estándar de un PNG: IEND chunk + CRC
    fin_png = b'\x00\x00\x00\x00IEND\xaeB`\x82'
    index_fin = datos.find(fin_png)

    if index_fin == -1:
        print("La imagen que tiene la informacion, no se encontro")
        return

    # El .zip empieza justo después del final del PNG
    inicio_zip = index_fin + len(fin_png)

    with open(salida_zip, 'wb') as zip_file:
        zip_file.write(datos[inicio_zip:])

    print(f"(+) El archivo zip extraido se llama: {salida_zip}")

# En este codigo se muestra como extraer un texto de un archivo zip
def extraer_txt_de_zip(archivo_zip, carpeta_destino='extraido'):
    os.makedirs(carpeta_destino, exist_ok=True)
    with zipfile.ZipFile(archivo_zip, 'r') as zipf:
        zipf.extractall(carpeta_destino)
    print(f"(+) El archivo de text extraido del zip es: {carpeta_destino}")


def leer_texto_de_zip(nombre_zip, nombre_archivo_txt):
    with zipfile.ZipFile(nombre_zip, 'r') as zip_ref:
        with zip_ref.open(nombre_archivo_txt) as file:
            texto_encriptado = file.read().decode('utf-8')  # Leer y decodificar a texto
            print(texto_encriptado)
            # Desencriptar
            # Generar clave
            # clave =  b'yRsR02RWd4ePvfb6LFYI9etNYVu7vF0A1TVVjoi9-ws='
            llave = input('Por favor ingresar el la LLAVE de encriptacion : ')
            # Salt constante (¡debe ser exactamente igual siempre!)
            salt_fijo = b'salt-fijo-16bytes'  # 16 bytes exactos
            # Generar clave Fernet
            clave = generar_clave_fernet_desde_texto(llave, salt_fijo)
            fernet = Fernet(clave)
            texto_desencriptado = fernet.decrypt(texto_encriptado).decode()
            print("(+) Texto desencriptado:", texto_desencriptado)

def generar_clave_fernet_desde_texto(texto: str, salt_constante: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt_constante,
        iterations=100_000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(texto.encode()))


# EJECUTAR FUNCIONES EXTRACCIÓN
extraer_zip_de_imagen('imagen_con_mensaje.png', 'extraido.zip')
extraer_txt_de_zip('extraido.zip')
leer_texto_de_zip('extraido.zip', 'Texto_a_guardar.txt')


