# Primero se instala PyAutoGUI con el siguiente comando  "pip install PyAutoGUI"
import pyautogui
import time

#Con las 2 funciones siguientes, se mueve el mause hacia una coordenada exacta.
#Con moveTo, el puntero del mause llega rapido y con moverel, se demora su transporte

#Se realiza una seccion de movimiento ante de entrar al ciclo
pyautogui.moveTo(300,300, duration=5)
pyautogui.press("enter")
pyautogui.moveRel(300,300, duration=5)
time.sleep(5)

#Se crea el ciclo, donde se realiza el movimiento constante por 15 minutos
ciclo =0
while ciclo <=10:
	if ciclo <=10 :
		pyautogui.moveTo(300,300, duration=30)
		pyautogui.moveRel(300,300, duration=30)
		time.sleep(5)
		break 
	print ("Vas en la ejecucion: "+ str(ciclo))
	ciclo = ciclo +1

#Sale una alerta que dice que ya se acabo el script
pyautogui.alert('Terminamos el script.')

