# En este programa se muestra un codigo para guardar mucha informacion de una usuario web
# Se usaran 2 librerias flask y requests, para ver la informacion de el usuario web
# Primero se instala captcha con el siguiente comando "pip install flask requests"
from flask import Flask, request, jsonify
import requests
from datetime import datetime
import socket
from datetime import datetime

app = Flask(__name__)

# En el siguiente codigo se guarda la direccion ip de el usuario
def get_client_ip():  
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0].split(',')[0]
    else:
        ip = request.remote_addr
    return ip

# Con la siguiente funcion se obtienen datos geograficos de una ip con esa api
def get_geo_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        return response.json()
    except Exception:
        return {}

# En esta funcion se valida datos de la conectividad con User-Agent (simplificado).
def get_connection_type(user_agent):
    ua = user_agent.lower()
    if "mobile" in ua or "android" in ua or "iphone" in ua:
        return "Móvil"
    else:
        return "Fija o desconocida"
    
# Con el siguiente codigo se indica que sistema operativo tiene el usuario
def detect_os(user_agent):
    ua = user_agent.lower()
    if "windows" in ua:
        return "Windows"
    elif "mac os" in ua or "macintosh" in ua:
        return "macOS"
    elif "linux" in ua:
        return "Linux"
    elif "android" in ua:
        return "Android"
    elif "iphone" in ua or "ios" in ua:
        return "iOS"
    else:
        return "Desconocido"

# En la siguiente funcion, se obtiene el hostname del usuario con socket
def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return "No disponible"


# Se indica con la funcion router de flask datos del usuario 
@app.route("/")
def index():
    ip = get_client_ip()
    user_agent = request.headers.get("User-Agent")
    referer = request.headers.get("Referer", "No especificado")
    connection_time = datetime.utcnow().isoformat() + "Z"
    cookies = request.cookies
    headers = dict(request.headers)
    geo_info = get_geo_info(ip)
    connection_type = get_connection_type(user_agent)
    os_info = detect_os(user_agent)
    hostname = get_hostname(ip)

    # Se guarda los datos en un JSON
    result = {
        "IP pública": ip,
        "Sistema operativo": os_info,
        "Hostname del cliente": hostname,
        "Hora de conexión (UTC)": connection_time,
        "Cookies": {k: v for k, v in cookies.items()},
        "Tipo de conexión": connection_type,
        "User-Agent": user_agent,
        "Referer": referer,
        "Geolocalización aproximada": {
            "País": geo_info.get("country"),
            "Región": geo_info.get("regionName"),
            "Ciudad": geo_info.get("city"),
            "Proveedor (ISP)": geo_info.get("isp"),
            "Latitud": geo_info.get("lat"),
            "Longitud": geo_info.get("lon")
        },
        "Headers HTTP": headers
    }

    return jsonify(result)

# El main para ejecutar la aplicacion
if __name__ == "__main__":
    app.run(debug=True)