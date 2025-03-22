# Se crean 2 listas diferentes, uno con numeros y el otro con letras
l = [1,2,3,4]
s = ["H","O","L","A"]

#Se crea un doble for, con un if adentro, para recorrer las listas eh imprimir cada parte de la lista
l2 =[c*num for c in s 
               for num in l
                   if num> 0]

print (l)
print (l2)