# Se crean las variables con listas en su interior
lista = [1,"dos",3]
lista2 = [1,2,3,4]
buscar=3

print (buscar in lista)             #Para ver si la variable (buscar) esta en la lista 
print (lista.index(buscar))         #Para ver en que posicion esta la variable (buscar) en la lista 
lista.append("nuevo elemento")      #agregar un nuevo elemento al final de la lista
lista.insert(2, "nuevo")            #agregar un nuevo elemento en la posicion 2
lista.extend(lista2)                #agregar la lista (lista2) en la lista (lista)
lista.pop(1)                        #elimina esa posicion en la lista
print (lista)
print (lista.count(3))              #ver cuantas veces esta 3 en la lista
lista.reverse()                     #pone la lista de atras hacia adelante
print (lista)
