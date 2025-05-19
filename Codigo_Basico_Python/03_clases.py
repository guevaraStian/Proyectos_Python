# Se crena clases que solicitaran 1 dato de entrada para mostrar la informacion final
class humano:
	def __init__(self,edad):
		self.edad = edad

	def hablar(self, mensaje):
		print (mensaje)

class ingsistemas(humano):
	def programar(self, lenguaje):
		print ('voy a programar en ', lenguaje)

class derecho(humano):
	def estudiarcaso(self, de):
		print ('Debo estudiar el caso de ', de)

class estudioso(ingsistemas,derecho):
	pass

pedro = ingsistemas(26)
raul = derecho(30)

#Se invoca la funcion con una variable de ingreso
pedro.programar('python')
raul.estudiarcaso('Pedro')