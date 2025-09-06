# En este programa se muestra un codigo para guardar mucha informacion de una usuario web
# Se usaran 2 librerias flask y requests, para ver la informacion de el usuario web
# Primero se instala captcha con el siguiente comando "pip install flask requests"
import requests

import time

# Tu usuario de GitHub
username = 'Usuario_Github'

# Tu token personal (de GitHub)
token = 'Token_Alfanumerico'

# Ruta al archivo con usuarios que quieres dejar de seguir
archivo = 'no_me_siguen.txt'

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github+json'
}

# Leer usuarios del archivo
with open(archivo, 'r', encoding='utf-8') as f:
    usuarios = [line.strip() for line in f if line.strip()]

# Iterar sobre la lista y dejar de seguir
for usuario in usuarios:
    url = f'https://api.github.com/user/following/{usuario}'
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f'(+) Dejaste de seguir a: {usuario}')
    elif response.status_code == 404:
        print(f'(+-) No estabas siguiendo a: {usuario}')
    else:
        print(f'(-) Error al dejar de seguir a {usuario}: {response.status_code} - {response.text}')

    time.sleep(1)  # Espera 1 segundo por seguridad (limita velocidad)