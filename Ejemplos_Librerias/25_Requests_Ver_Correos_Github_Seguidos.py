# En este programa se muestra un codigo para guardar los correos electronicos 
# de los usuarios de github que sigue una cuenta
# Se usaran 1 libreria requests, para ver la informacion de el usuario web
# Primero se instala captcha con el siguiente comando "pip install requests"
import requests

# === CONFIGURACIÓN ===
GITHUB_USERNAME = "USUARIO_GITHUB"
GITHUB_TOKEN = "GITHUB_TOKEN"
OUTPUT_FILE = "emails.txt"

# === FUNCIONES ===
def get_following_users(username, token):
    url = f"https://api.github.com/users/{username}/following"
    headers = {"Authorization": f"token {token}"}
    following = []
    page = 1

    while True:
        response = requests.get(url, headers=headers, params={"per_page": 100, "page": page})
        if response.status_code != 200:
            print("Error al obtener usuarios seguidos:", response.status_code, response.text)
            break

        data = response.json()
        if not data:
            break

        following.extend([user["login"] for user in data])
        page += 1

    return following

def get_user_email(username, token):
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error al obtener datos de {username}: {response.status_code}")
        return None

    user_data = response.json()
    return user_data.get("email")  # Puede ser None

def save_emails_to_file(emails, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for email in emails:
            if email:
                f.write(email + "\n")

# === PROGRAMA PRINCIPAL ===
def main():
    print(f"Obteniendo usuarios que sigue {GITHUB_USERNAME}...")
    following_users = get_following_users(GITHUB_USERNAME, GITHUB_TOKEN)
    print(f"Total usuarios seguidos: {len(following_users)}")

    emails = []
    for user in following_users:
        email = get_user_email(user, GITHUB_TOKEN)
        if email:
            print(f"{user}: {email}")
            emails.append(email)

    save_emails_to_file(emails, OUTPUT_FILE)
    print(f"\nSe guardaron {len(emails)} correos en {OUTPUT_FILE}")

if __name__ == "__main__":
    main()