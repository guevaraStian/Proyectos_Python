# Este programa nos muestra, funciones sencillas
li =[1,-2,1,-4]
lo = [5,3,6,7]
s = "Hoola mundo"

print (map(lambda n,m: n+m , li,lo))
print (filter(lambda n: n=='o' , s))