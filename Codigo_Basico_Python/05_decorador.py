# Un decorador es una funcion que recibe datos de otra funcion
loggeado = False
usuario = "CodigoFacilito"

def admin(f):
	def comprobar(*args,**kwargs):
		if loggeado:
			f(*args,**kwargs)
		else:
			print ("No tiene permiso de ejecutar")
	return comprobar


def decorador(funcion):
	def funcionDecorada(*args,**kwargs):
		print ("funcion ejecutada ", funcion.__name__)
		funcion(*args,**kwargs)
	return funcionDecorada

@decorador	
def resta(n,m):
	print (n-m)

resta(3,5)