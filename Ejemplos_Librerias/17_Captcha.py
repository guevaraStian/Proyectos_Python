# En este programa se muestra un codigo para crear y validar un captcha
# Se usaran 3 librerias flask, captcha y random, para crear la imagen chaptcha
# Primero se instala captcha con el siguiente comando "pip install flask captcha pillow"
from flask import Flask, session, request, send_file, render_template_string, redirect, url_for
from captcha.image import ImageCaptcha
import random
import string
import io

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'  # Necesaria para usar sesiones

# Generador de texto CAPTCHA
def generar_texto(longitud=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=longitud))

@app.route('/')
def index():
    return render_template_string('''
        <h2>Por favor, Introduce el texto que ves en la imagen:</h2>
        <form method="post" action="/verificar">
            <p><img src="/captcha" alt="CAPTCHA"></p>
            <p><input type="text" name="captcha_input"></p>
            <p><input type="submit" value="Verificar"></p>
        </form>
    ''')

@app.route('/captcha')
def captcha():
    imagen_capchat = ImageCaptcha()
    texto = generar_texto()
    session['captcha_texto'] = texto  # Guardamos el texto en la sesión
    data = imagen_capchat.generate(texto)
    return send_file(data, mimetype='image/png')

@app.route('/verificar', methods=['POST'])
def verificar():
    texto_ingresado_usuario = request.form['captcha_input']
    captcha_correcto = session.get('captcha_texto', '')
    # Con el siguiente if, se valida que el captcha sea correcto
    if texto_ingresado_usuario.upper() == captcha_correcto:
        return "<h2>✅ CAPTCHA correcto</h2><a href='/'>Volver</a>"
    else:
        return "<h2>❌ CAPTCHA incorrecto</h2><a href='/'>Intentar de nuevo</a>"

if __name__ == '__main__':
    app.run(debug=True)