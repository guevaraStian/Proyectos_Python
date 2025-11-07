# En este programa se muestra un codigo para dejar de seguir usuarios en instagram
# Se usaran 2 librerias os y instagrapi
# Primero se instala captcha con el siguiente comando "pip install instagrapi"
import os
from instagrapi import Client
import time

usuario = "Usuario_Instagram"
contraseña = "Contraseña"

# Ruta para guardar sesión
SESSION_PATH = "session.json"
# Crear cliente
cl = Client()

# Intentar cargar sesión existente
if os.path.exists(SESSION_PATH):
    cl.load_settings(SESSION_PATH)
    try:
        cl.login(usuario, contraseña)
        print("(+) Se logueo")
    except Exception as e:
        print("(+-) Sesión caducada. Reautenticando...")
        cl.set_settings({})
        cl.login(usuario, contraseña)
        cl.dump_settings(SESSION_PATH)
        print("(+) Se logueo")
else:
    cl.login(usuario, contraseña)
    cl.dump_settings(SESSION_PATH)
    print("(+) Se logueo")

# Leer usernames del archivo
with open("no_en_ambas.txt", "r", encoding="utf-8") as archivo:
    usernames = [line.strip() for line in archivo if line.strip()]
print("(+) Se cargaron los datos del .txt")
# Dejar de seguir a cada uno
unfollow_count = 0

for username in usernames:
    try:
        user_id = cl.user_id_from_username(username)
        if cl.user_unfollow(user_id):
            print(f"(+) Dejaste de seguir a: {username}")
            unfollow_count += 1
        else:
            print(f"(-) No se pudo dejar de seguir a: {username}")
    except Exception as e:
        print(f"(+-) Error con {username}: {e}")
    time.sleep(50)  # ⏳ Pausa para evitar bloqueos

print(f"\n(+) Total dejado de seguir: {unfollow_count}")