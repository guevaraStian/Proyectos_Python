# pip install random
import random

#En la siguiente linea se ingresa la cantidad de caracteres que va a tener la contraseña
cantidad_caracteres = int(input("Porfavor ingrese la cantidad de caracteres: "))

#Se declaran los posibles caracteres que va a tener la contraseña
minuscula = "abcdefghijklmnñopqrstuvwxyz"
mayuscula = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%&/()=?¡¨*][_:;><]"

#Se agrupan todos los carecteres posibles en una variable
todos_los_caracteres = minuscula + mayuscula + numeros + simbolos

#Se crea la contraseña con la posiblidad de obtener todos los caracteres y se le adjunta la cantidad
contraseña = ''.join(random.sample(todos_los_caracteres, cantidad_caracteres))

print("La contraseña creada es : " + contraseña)

 



