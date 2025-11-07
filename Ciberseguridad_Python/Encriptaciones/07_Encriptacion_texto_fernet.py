# En el siguiente codigo se muestra como se crea una llave o key para encriptar un texto
# Luego se ingresa un texto y se muestra encriptada la informacion
# pip install cryptography
from cryptography.fernet import Fernet

# Ingresamos el texto que se va a encriptar 
contenido = input("Por favor ingrese la informacion que va a encriptar: ")
mensaje = contenido.encode()

# Generar una clave, llave o key secreta y aleatoria
clave = Fernet.generate_key()
print(f"Llave generada: {clave}")

# Se crea un objeto con la clave guardada
fernet = Fernet(clave)

# Se procede a encriptar el mensaje
mensaje_cifrado = fernet.encrypt(mensaje)
print(f"El mensaje cifrado: {mensaje_cifrado}")

# El siguiente codigo sirve para descifrar el mensaje
mensaje_descifrado = fernet.decrypt(mensaje_cifrado)
print(f"El mensaje descifrado: {mensaje_descifrado.decode()}")