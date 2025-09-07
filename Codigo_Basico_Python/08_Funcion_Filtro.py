# Esta funcion, nos muestra los numeros mayores que 0
def filtro (elem):
	return (elem >0)

l=[1,-3,2,-7,-8,9,10]
lr = filter(filtro,l)

print (l)
print (lr)