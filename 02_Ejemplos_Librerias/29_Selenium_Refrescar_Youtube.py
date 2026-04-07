# Software que refresca una paginas de youtube varias veces
# pip install webdriver-manager selenium pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time

# Se ingresan la cantidad de repeticiones que se haran
repeticiones = int(input("Por favor, ingrese la cantidad de repeticiones de reproduccion del video: "))

# Se ingresa el link de vide de youtube que se reproducira
url = input("Por favor, ingrese la url del video de youtube: ")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

wait = WebDriverWait(driver, 1)

for i in range(repeticiones):
    print(f"Iteración #{i+1}")

    # Se refresca la pagina 
    driver.refresh()
    video = wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))

    # Reproducir video
    driver.execute_script("arguments[0].play();", video)
    print("Video reproduciéndose")

    # Movimiento visible de esquina a esquina
    acciones = ActionChains(driver)
    start_time = time.time()


    while time.time() - start_time < 30:
        try:
            pyautogui.moveTo(300,300, duration=15)
            pyautogui.moveRel(300,300, duration=15)

        except:
            # reiniciar posición del mouse si se sale del rango
            acciones.move_by_offset(0, 0).perform()

driver.quit()