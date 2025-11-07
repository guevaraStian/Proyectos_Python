# En este programa se muestra un codigo para consultar seguidos y seguidores en un github
# Luego se guarda en un txt los que no estan en las 2 listas Se usaran 
# Primero se instala captcha con el siguiente comando "pip install flask requests"
import requests

# 👇 Cambia esto con tu nombre de usuario de GitHub
username = 'Usuario_github'

# 👇 Si tienes token, pégalo aquí. Si no, déjalo como ''
token = 'Token_Alfanumerico'  # opcional pero recomendado

# Cabecera para autenticar con token (si lo usas)
headers = {'Authorization': f'token {token}'} if token else {}

# Función para obtener usuarios paginados (followers o following)
def get_paginated_users(url):
    users = []
    while url:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        users.extend([user['login'] for user in data])
        # Revisa si hay otra página
        url = response.links.get('next', {}).get('url')
    return users

# URLs de API
followers_url = f'https://api.github.com/users/{username}/followers'
following_url = f'https://api.github.com/users/{username}/following'

print("(+) Obteniendo seguidores...")
followers = get_paginated_users(followers_url)

print("(+) Obteniendo seguidos...")
following = get_paginated_users(following_url)

# Comparar listas: quiénes sigues que NO te siguen
no_te_siguen = [user for user in following if user not in followers]

# Guardar en archivo
with open('no_me_siguen.txt', 'w', encoding='utf-8') as f:
    for user in no_te_siguen:
        f.write(user + '\n')

print(f"\n(+) Usuarios que sigues y no te siguen: {len(no_te_siguen)}")
print("(+) Guardado en archivo: no_me_siguen.txt")