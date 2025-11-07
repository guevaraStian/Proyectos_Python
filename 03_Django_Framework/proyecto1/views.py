from importlib.abc import Loader
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template

def saludo (request):
    var_nombre = "Sebas"
    var_apellido = "tian"


# ##### DESCOMENTAR PARA ENTENDER EL PASO A PASO 
# # # al momento de pegar el link hay que poner las / de dividir 
#     doc_externo=open("C:/Users/Sesagean/Desktop/Resumenes/CLASES/DJANGO/proyecto1/proyecto1/plantillas/miplantilla.html")
#     plt= Template(doc_externo.read()) #Se usa Template con .read() para leer el archivo .html y guardarlo en una variable
#     doc_externo.close() 
#     ctx=Context({"nombre": var_nombre ,"apellido": var_apellido, "temas": ["uno", "dos", "tres"]}) # se usa para paginas dinamicas, no hay informacion dentr de context porque es pagina sencilla 
#     documento=plt.render(ctx) #Se renderiza la pagina en 1 sola variable con su respectivo contect
#     #documento2=Template(doc_externo.read()).render(Context())
   

# #FORMA SIMPLIFICADA 
   #En settings se modifica DIRS para poner la direccion de las plantillas
    doc_externo= get_template('miplantilla.html')
    documento=doc_externo.render({"nombre": var_nombre ,"apellido": var_apellido, "temas": ["uno", "dos", "tres"]}) #Se renderiza la pagina en 1 sola variable con su respectivo contect



    return HttpResponse(documento)

def html (request):
    
    return HttpResponse("<h1>Hola </h1>  <h4>como estas?</h4>")

def otra (request):
    valor1 = 2
    valor2 = 3
    total = valor1 + valor2
    doc_externo= get_template('otra.html')
    documento=doc_externo.render({"total":total})
    
    return HttpResponse(documento)


def conestilos (request):

    doc_externo= get_template('conestilos.html')
    documento=doc_externo.render()
    
    return HttpResponse(documento)
