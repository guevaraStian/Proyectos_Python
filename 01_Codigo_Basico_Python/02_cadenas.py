# Teniendo el hola mundo, como una cadena de texto, se puede imprimir informacion con los siguientes comando
s = "Hola mundo"

print (len(s))           #Sirve para imprimir la cantidad de caracteres hay en la cadena S
print (s.count("o"))     #Sirve para encontrar la cantidad de caracteres O en la cadena s
print (s.count("o",0,5)) #Sirve para encontrar la cantidad de caracteres O en la cadena s desde el caracter 0 al 5
print (s.lower())        #Sirve para poner toda la cadena en minuscula
print (s.upper())        #Sirve para poner toda la cadena en mayuscula
print (s.replace("o", "x")) #Sirve para reemplazar la letra o por la x
print (s.split("o", 1))  #Sirve para cortar la cadena en la letra o , 1 vez
print (s.find("a"))      #Sirve para mostrar la posicion donde esta esa variable en la cadena
print (type(s))          #Sirve para mostrar el tipo de caracter que hay