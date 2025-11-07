# En este programa se muestra un codigo para crear y validar un Cookie
# Se usaran 3 librerias flask, json y base64, para crear la imagen un software que de cookies
# Primero se instala captcha con el siguiente comando "pip install flask base64"
from flask import Flask, request, make_response
import json
import base64

app = Flask(__name__)

# Se programa un diccionario como JSON y luego a base64
def encode_cookie_data(data):
    json_data = json.dumps(data)
    return base64.b64encode(json_data.encode()).decode()

# Decodifica y convierte de nuevo a diccionario
def decode_cookie_data(encoded_data):
    try:
        decoded = base64.b64decode(encoded_data).decode()
        return json.loads(decoded)
    except Exception:
        return {}

@app.route('/guardar_cookie')
def set_cookie():
    # Información que queremos guardar
    cookie_data = {
        "user": "Sebas123",
        "theme": "dark",
        "language": "es",
        "session_id": "123abc456",
        "last_visited": "/productos",
        "logged_in": True
    }

    encoded = encode_cookie_data(cookie_data)
    response = make_response("Cookies creada.")
    response.set_cookie('user_data', encoded, max_age=60*60*24*7)  # 7 días
    return response

@app.route('/obtener_cookie')
def get_cookie():
    encoded = request.cookies.get('user_data')
    if encoded:
        data = decode_cookie_data(encoded)
        return f"Los datos actuales de la cookie:<br><pre>{json.dumps(data, indent=2)}</pre>"
    return "No hay cookie 'user_data'."

if __name__ == '__main__':
    app.run(debug=True)