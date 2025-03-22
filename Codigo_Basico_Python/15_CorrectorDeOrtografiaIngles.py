# Primero se instala textblob con el siguiente comando "pip install textblob"
# Luego de bajar librerias, las importamos
from textblob import TextBlob

#Pedimos que ingresen el texto en ingles con errores de ortografia
# ejemplo de texto mal escrito "I havv a guud ideea"
texto_con_errores_ortograficos = input("Por favor ingresen el texto en ingles a corregir: ")

#Guardamos el texto en una variable 
texto_analizado = TextBlob(texto_con_errores_ortograficos)

# El texto lo corregimos y lo guardamos corregido en una variable
texto_corregido = texto_analizado.correct()

# Mostramos en pantalla los 2 textos el errado y el corregido
print("Texti escrito : ", texto_analizado)
print("Texto corregido :", texto_corregido)










