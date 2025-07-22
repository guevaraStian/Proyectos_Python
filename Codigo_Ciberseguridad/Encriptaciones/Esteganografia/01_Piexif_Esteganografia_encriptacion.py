# En el siguiente codigo de programacion, se muestra una forma sencilla
# De guardar informacion en una imagen
# Pirmero descargamos y usamos las librerias
# "pip install piexif"

import os
from PIL import Image, ImageDraw, ImageFont
import piexif

# Con el siuiente codigo se ingresan textos a los datos de una imagen
def insertar_texto_visible(imagen, texto, posicion=(10, 10), color=(255, 255, 255)):
    draw = ImageDraw.Draw(imagen)
    font = ImageFont.load_default()
    draw.text(posicion, texto, fill=color, font=font)
    return imagen

# Variables de metadatos
def insertar_metadato(imagen, texto):
    try:
        exif_dict = piexif.load(imagen.info.get('exif', b''))
    except Exception:
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

    # Codificar como UserComment (ID 37510)
    user_comment = texto.encode('utf-8')
    exif_dict["Exif"][piexif.ExifIFD.UserComment] = b'\x00\x00' + user_comment
    return piexif.dump(exif_dict)

# Se ejecuta el main con las funcion
def main():
    print("!! Este es un programa para editar imagen e insertar información !!")

    # Se pide que ingresen la ruta de la imagen
    ruta_imagen = input("Ruta de la imagen (ej. foto.jpg): ").strip()
    if not os.path.exists(ruta_imagen):
        print("(-) No se encontro la imagen")
        return

    # La primera pregunta es la ubicacion de la imagen
    dato = input("Texto a insertar en la imagen y como metadato: ").strip()

    # Con el siguiente codigo se abre la imagen teniendo su ruta
    try:
        imagen = Image.open(ruta_imagen).convert("RGB")
    except Exception as e:
        print(f"(-)  No se pudo abrir la imagen : {e}")
        return

    # Se ingresa el texto a la imagen
    imagen = insertar_texto_visible(imagen, dato)

    # Creamos una imagen nueva con la informacion
    nueva_ruta = f"Editada_{os.path.basename(ruta_imagen)}"
    try:
        if ruta_imagen.lower().endswith((".jpg", ".jpeg")):
            exif_bytes = insertar_metadato(imagen, dato)
            imagen.save(nueva_ruta, exif=exif_bytes)
        else:
            imagen.save(nueva_ruta)
        print(f"(+) Imagen guardada sin problemas : {nueva_ruta}")
    except Exception as e:
        print(f"(-) No se pudo guardar la imagen: {e}")

if __name__ == "__main__":
    main()










