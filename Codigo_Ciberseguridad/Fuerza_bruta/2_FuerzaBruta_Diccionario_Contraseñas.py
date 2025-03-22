# Primero se instala hashlib con el siguiente comando "pip install hashlib"
import hashlib

#Primero guardamos el hash de la contraseña en una variable
hash_inicial = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"

#Guardamos en otra variable, la ruta donde esta el diccionario con las contraseñas
archivo_diccionario = input("ingrese la direccion del diccionario: ")

#Con el siguiente codigo se recorre la informacion dentro de el diccionario, seleccionando cada posible contraseña
with open(archivo_diccionario, 'r') as file:
    diccionario = [line.strip() for line in file]
    
    #En el siguiente codigo se recorre el diccionarios convirtiendo cada contraseña en hash
    for contraseña in diccionario:
        hash_calculado = hashlib.sha256(contraseña.encode()).hexdigest()

        #Luego de crear el hash de cada contraseña, se compara con la que queremos descifrar 
        #Si son identios los hash sale un mensaje indicandolo, si no, sale otro mensaje
        if hash_calculado == hash_inicial:
            print("la contraseña encontrada es: " + contraseña)
            break
        else:
            print("la contraseña no es la indicada ")



