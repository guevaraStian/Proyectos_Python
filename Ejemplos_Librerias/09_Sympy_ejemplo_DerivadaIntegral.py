# Primero se instala sympy con el siguiente comando "pip install sympy"
# Luego de bajar librerias, las importamos
from sympy import *

# La variable con el simbolo x
x = Symbol('x')

# Se le pide la funcion al usuario del software
func = input("Por favor ingrese la funcion: ")

# Se le aplican diferentes operaciones a la funcion ingresada
derivada = diff(func, x)
derivada_2 = Derivative(func, x, evaluate = true)
limite = limit(func , x, 0)
integrada = integrate(func, x)
solucion = solve(func, x)

# Con este codigo se imprime cada solucion empleada
print(derivada)
print(derivada_2)
print(limite)
print(integrada)
print(solucion)





