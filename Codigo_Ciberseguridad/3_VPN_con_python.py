# Primero se instala datetime con el siguiente comando  "pip install datetime"
#Primero se instala os con el siguiente comando  "pip install os"
import os
from time import sleep
import random

ListaDeCodigos= ["TR", "US","DE", "NL", "CH","CA-W", "GB"]

#Por medio de la libreria de sistema operativo, se reconecta a internet con una ip diferente
try:
    os.system("windscribe connect")
    while True:
        CambioCodigo = random.choice(ListaDeCodigos)
        sleep(random.randrange(12,30))
        print("#Cambiando la direccion ip...")
        os.system("windscribe connect "+ CambioCodigo)
except:
    os.system("windscribe disconnect")
    print("Error...")