# En este codigo se logra hacer un descencriptacion de esteganografia
# Con las variables exif que tiene una imagen

import os
from PIL import Image
import piexif

def extraer_metadato(ruta_imagen):
    try:
        imagen = Image.open(ruta_imagen)
        exif_dict = piexif.load(imagen.info.get('exif', b''))

        # Extraer UserComment (ID 37510)
        user_comment = exif_dict["Exif"].get(piexif.ExifIFD.UserComment, None)
        if user_comment:
            # Eliminar encabezado '\x00\x00' y decodificar
            texto = user_comment[2:].decode('utf-8', errors='ignore')
            return texto
        else:
            return None
    except Exception as e:
        print(f"Error con la lectura de la imagen: {e}")
        return None

def main():
    print("Lector de metadatos EXIF de imagen JPEG")

    # 1. Preguntar imagen
    ruta_imagen = input("Ruta de la imagen (ej. editada_foto.jpg): ").strip()
    if not os.path.exists(ruta_imagen):
        print("La imagen no se encontro")
        return

    if not ruta_imagen.lower().endswith((".jpg", ".jpeg")):
        print("Este extractor solo funciona con imágenes JPEG.")
        return

    # 2. Extraer y mostrar dato
    dato = extraer_metadato(ruta_imagen)
    if dato:
        print(f"Dato encontrado en metadato: '{dato}'")
    else:
        print("No se encontró ningún dato en el metadato.")

if __name__ == "__main__":
    main()

