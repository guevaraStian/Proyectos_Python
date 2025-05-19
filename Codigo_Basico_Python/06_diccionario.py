# Este software crea un diccionario con diferente informacion dentro y nos muesta como imprimir en pantalla cierta informacion
diccionario = {
	"redes_sociales": ["twitter","Facebook","linkedin"], 3: "tres","hola":"mundo"
}
print (diccionario)
print (diccionario.values())         #Encontrar valores dentro de todas las llaves
print (diccionario.pop(3))           #Encontrar valores dentro de la llave 3
print (diccionario.clear())          #Eliminar llaves y valores dentro de diccionario
diccionario["clave_nueva"] = "valor" #Agrega llave "clave_nueva"con el valor "valor"
diccionario2 = diccionario.copy()
print (diccionario)