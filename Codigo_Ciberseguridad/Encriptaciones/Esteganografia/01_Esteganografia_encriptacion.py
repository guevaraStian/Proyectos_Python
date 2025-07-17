# En este codigo se logra hacer una esteganografia
# Con las variables exif que tiene una imagen

import os
from PIL import Image, ImageDraw, ImageFont
import piexif

def insertar_texto_visible(imagen, texto, posicion=(10, 10), color=(255, 255, 255)):
    draw = ImageDraw.Draw(imagen)
    font = ImageFont.load_default()
    draw.text(posicion, texto, fill=color, font=font)
    return imagen

def insertar_metadato(imagen, texto):
    try:
        exif_dict = piexif.load(imagen.info.get('exif', b''))
    except Exception:
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

    # Codificar como UserComment (ID 37510)
    user_comment = texto.encode('utf-8')
    exif_dict["Exif"][piexif.ExifIFD.UserComment] = b'\x00\x00' + user_comment
    return piexif.dump(exif_dict)

def main():
    print("🖼️ Programa para editar imagen e insertar información")

    # 1. Preguntar ruta de imagen
    ruta_imagen = input("Ruta de la imagen (ej. foto.jpg): ").strip()
    if not os.path.exists(ruta_imagen):
        print("❌ Imagen no encontrada.")
        return

    # 2. Preguntar el dato a insertar
    dato = input("Texto a insertar en la imagen y como metadato: ").strip()

    # 3. Abrir imagen
    try:
        imagen = Image.open(ruta_imagen).convert("RGB")
    except Exception as e:
        print(f"❌ Error al abrir imagen: {e}")
        return

    # 4. Insertar texto visible
    imagen = insertar_texto_visible(imagen, dato)

    # 5. Insertar metadato (si es JPG/JPEG)
    nueva_ruta = f"editada_{os.path.basename(ruta_imagen)}"
    try:
        if ruta_imagen.lower().endswith((".jpg", ".jpeg")):
            exif_bytes = insertar_metadato(imagen, dato)
            imagen.save(nueva_ruta, exif=exif_bytes)
        else:
            imagen.save(nueva_ruta)
        print(f"La imagen se almaceno como : {nueva_ruta}")
    except Exception as e:
        print(f"Error : {e}")

if __name__ == "__main__":
    main()










