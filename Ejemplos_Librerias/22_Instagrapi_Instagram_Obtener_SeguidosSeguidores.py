# En este programa extrae los seguidores y los seguidos de una cuenta instagram
# Se usaran 2 librerias os y instagrapi 
# Primero se instala instagrapi con el siguiente comando "pip install instagrapi"
# Toca hacer una consulta por ejecucion

from instagrapi import Client
import os


# Credenciales
usuario = "Usuario_Instagram"
contraseña = "Contraseña"

# Iniciar sesión en Instagram
cl = Client()
try:
    cl.login(usuario, contraseña)
    print(f"(+) Inicio sesion: ")
except Exception as e:
    print(f"(-) Error al iniciar sesión: {e}")
    exit()

# Obtener los primeros 50 usuarios que sigues
seguidos = cl.user_following(cl.user_id, amount=200)
print(f"(+) Se cargaron los seguidos ")
# Obtener todos los seguidores (quiénes te siguen)
#seguidores = cl.user_followers(cl.user_id, amount=300)
#print(f"(+) Se cargaron los seguidores ")
# Extraer solo usernames
usernames_seguidos = [u.username for u in seguidos.values()]
print(f" (+) Se camnio el id por el nombre seguidos ")
#usernames_seguidores = {u.username for u in seguidores.values()}
#print(f"(+) Se camnio el id por el nombre seguidores ")
# Verificar quién no te sigue de vuelta (solo entre los 50 primeros)
#no_me_siguen = [u for u in usernames_seguidos if u not in usernames_seguidores]
# print(f"Se hizo la validacion: ")
# Guardar resultados
with open("seguidos_inst.txt", "w", encoding="utf-8") as archivo:
    for usuario in usernames_seguidos:
        archivo.write(usuario + "\n")
#with open("seguidores_inst.txt", "w", encoding="utf-8") as archivo:
#    for usuario in usernames_seguidores:
#        archivo.write(usuario + "\n")
print(f"(+) Guardado: {len(usernames_seguidos)} de los primeros 50 que no te siguen (en no_me_siguen.txt)")
#print(f"(+) Guardado: {len(usernames_seguidores)} de los primeros 50 que no te siguen (en no_me_siguen.txt)")