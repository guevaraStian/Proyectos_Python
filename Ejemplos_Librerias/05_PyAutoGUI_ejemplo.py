# Primero se instala PyAutoGUI con el siguiente comando  "pip install PyAutoGUI"
import pyautogui
import time

#Con la funcion alert, mostramos en pantalla un mensaje con la informacion que queremos
#En este caso mostramos un size, que es el tamaño de la pantalla
pyautogui.alert(pyautogui.size())
#Se le da 5 segundos, por si el computadr es lento
time.sleep(5)
#En este caso mostramos un position, que es la ubicacion del maus en la pantalla
pyautogui.alert(pyautogui.position())
#Se le da 5 segundos, por si el computadr es lento
time.sleep(5)
#Con las 2 funciones siguientes, se mueve el mause hacia una coordenada exacta.
#Con moveTo, el puntero del mause llega rapido y con moverel, se demora su transporte
pyautogui.moveTo(15,15, duration=3)
pyautogui.moveRel(500,500, duration=3)
#Con el siguiente codigo se presiona el boton windows
pyautogui.press("win")
#Se le da 3 segundos, por si el computadr es lento
time.sleep(3)
#Con la caracteristica write de pyautogui, escribimos la palabra excel con un intervalo de 0.1 segundos y luego damos enter
pyautogui.write("excel", interval = 0.10)
pyautogui.press("enter")
#Esperamos 10 segundos para que abra el excel
time.sleep(10)
#Luego damos enter para abrir una pagina nueva de excel y posteriormente se escribe un texto
pyautogui.press("enter")
pyautogui.write("hola, soy un texto escrito", interval = 0.05)
#Luego movemos 1 vez hacia abajo y 1 vez a la derecha, para luego ingresar un numero y dar enter
pyautogui.press(['down', 'right'])
pyautogui.write('+1+3')
pyautogui.press("enter")
#Por ultimo damos el grupo de comandos para guardar y mostramos un alerta de terminar el software
pyautogui.hotkey('ctrl', 's')
pyautogui.alert('Terminamos el script.')

