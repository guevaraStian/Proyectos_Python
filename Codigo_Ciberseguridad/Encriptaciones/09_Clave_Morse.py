# En este texto se muestra un cambio de letras a codigo morse
# Se ingresan primero las variables con su respuesta en un orden especifico

abc = {"A":".-", "N":"-.", "B":"-...","O":"---","C":"-.-.","P":".--."}
abc2 = {"D":"-..","Q":"--.-", "E":".","R":".-.","F":"..-.","S":"..."}
abc3 = {"G":"--.","T":"-", "H":"....", "U":"..-","I":"..","V":"...-"}
abc4 = { "J":".---",  "W":".--", "K":"-.-","X":"-..-", "L":".-..", "Y":"-.--", "M":"--","Z":"--.."}

num1 = {"1":".----", "2":"..---","3":"...--","4":"....-", "5":".....","6":"-...."}
num2 = {"7":"--...", "8":"---..","9":"----.","0":"-----"}

Lista_caracteres = {}

# Se ingresa las listas de las letras en un solo arreglo o lista
Lista_caracteres.update(abc)
Lista_caracteres.update(abc2)
Lista_caracteres.update(abc3)
Lista_caracteres.update(abc4)
Lista_caracteres.update(num1)
Lista_caracteres.update(num2)


# Luego creamos un while para solicitar las palabras 
# Por los codigos de calve morse que corresponden
while True:
    while True:
        palabra = input("Ingresa una palabra sin espacios: ")
        if palabra.isalnum():
            palabra = palabra.upper()
            break
        else:
            print("Por favor sin espacios \n")
            break
    break

# Se ingresa la cantidad de letras que tiene la palabra en una variable

largo_palabra = len(str(palabra))

print("\n" + palabra, "En morse es : ")

# Se recorre un for con cada letra de la palabra, 
# Agregando un espacio al final para mostrarlo por partes
for y in range(0, largo_palabra):
      for x in Lista_caracteres.keys():
        if x == palabra[y]:
            print(Lista_caracteres[x], end=' ')
            

          


















