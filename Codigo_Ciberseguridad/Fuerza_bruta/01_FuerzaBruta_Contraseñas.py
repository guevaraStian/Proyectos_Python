# Primero se instala hashlib con el siguiente comando "pip install hashlib"
import hashlib

#Ejemplo de hash, en este caso es el sha256 de la contraseña "test"
hash_file = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"

#Se ingresa una palabra que es la posible contraseña
posible_contrase = input("ingrese la palabra a probar : ")

#Luego convertimos la posible contraseña en un sha256
hash_calculado = hashlib.sha256(posible_contrase.encode()).hexdigest()

#Comparamos los 2 hash y si son iguales, se muestra un mensaje, si no son iguales sale unra respuesta
if hash_calculado == hash_file:
    print("Se encontro la contraseña y es: " + posible_contrase)
else:
    print("la contraseña NO es la ingresada ")



