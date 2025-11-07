# En el siguiente codigo se muestra como se crea una llave o key para encriptar un la informacion de un texto
# Luego se reemplaza el archivo por uno encriptado y por ultimo se desencripta
# pip install cryptography
from cryptography.fernet import Fernet

# Con el siguiente codigo se crea una llave, llave o key secreta y aleatoria
def generar_llave():
    llave = Fernet.generate_key()
    with open("llave.key", "wb") as archivo_llave:
        archivo_llave.write(llave)

# Se crea la funcion de cargar llave
def subir_llave():
    return open("llave.key", "rb").read()

# El siguiente codigo explica como se cifra la informacion de archivo con la libreria fernet
def encriptar_archivo(nombre_archivo):
    llave = subir_llave()
    fernet = Fernet(llave)
    
    with open(nombre_archivo, "rb") as archivo:
        datos = archivo.read()
    
    datos_cifrados = fernet.encrypt(datos)
    
    with open(nombre_archivo, "wb") as archivo:
        archivo.write(datos_cifrados)

# En la siguiente funcion se muestra como se descifran los datos
def desencriptar_archivo(nombre_archivo):
    llave = subir_llave()
    fernet = Fernet(llave)
    
    with open(nombre_archivo, "rb") as archivo:
        datos_cifrados = archivo.read()
    
    datos_descifrados = fernet.decrypt(datos_cifrados)
    
    with open(nombre_archivo, "wb") as archivo:
        archivo.write(datos_descifrados)

# Se ejecutan las 3 funciones creadas anteriormente
generar_llave()
encriptar_archivo("documento.txt")
desencriptar_archivo("documento.txt")

