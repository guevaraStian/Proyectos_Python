# En el siguiente codigo de programacion, se muestra una forma sencilla
# De guardar un archivo texto en una imagen png
# Pirmero descargamos y usamos las librerias
# Primero se instala zipfile con el siguiente comando 
# "pip install zipfile"


import zipfile
from PIL import Image

# La siguiente funcion sirve para crear un archivo texto con una informacion
def crear_txt(nombre_txt, contenido):
    with open(nombre_txt, 'w') as f:
        f.write(contenido)
    print(f"El archivo .txt se creo sin problemas: {nombre_txt}")

# Con esta funcion se crea una imagen con un nombre indicado
def crear_imagen_png(nombre_imagen):
    img = Image.new('RGB', (200, 200), color='lightgreen')
    img.save(nombre_imagen)
    print(f"Imagen PNG creada: {nombre_imagen}")

# En este codigo se muestra como meter un archivo texto a un archivo comprimido zip
def crear_zip(nombre_zip, archivo_txt):
    with zipfile.ZipFile(nombre_zip, 'w') as zipf:
        zipf.write(archivo_txt)
    print(f"[✔] ZIP creado: {nombre_zip}")

# En este codigo se explica como ingresarle el texto a la imagen con un archivo zip
def fusionar_imagen_y_zip(imagen_png, archivo_zip, salida_png_con_zip):
    with open(imagen_png, 'rb') as img_file:
        datos_img = img_file.read()

    with open(archivo_zip, 'rb') as zip_file:
        datos_zip = zip_file.read()

    with open(salida_png_con_zip, 'wb') as salida:
        salida.write(datos_img)
        salida.write(datos_zip)

    print(f"La imagen quedo con el zip comprimido adentro: {salida_png_con_zip}")

# EJECUTAR FLUJO COMPLETO
crear_imagen_png('imagen_base.png')
crear_zip('archivo.zip', 'Texto_a_guardar.txt')
fusionar_imagen_y_zip('imagen_base.png', 'archivo.zip', 'imagen_con_mensaje.png')


