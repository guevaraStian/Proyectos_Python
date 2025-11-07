# En el siguiente codigo de programacion, se muestra una forma sencilla
# De extraer informacion en una imagen
# Pirmero descargamos y usamos las librerias
# "pip install piexif"

import os
from PIL import Image
import piexif

# Con el siguiente codigo se extrae el metadato que esta encriptado
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
        print(f"(-) No se pudo leer el dato: {e}")
        return None

def main():
    print("!! Empieza a leer los metadatos de la imagen !!")

    # La siguiente pregunta pide la ruta de la imagen
    ruta_imagen = input("Ruta de la imagen (ej. editada_foto.jpg): ").strip()
    if not os.path.exists(ruta_imagen):
        print("(-) No se encontro la imagen")
        return

    if not ruta_imagen.lower().endswith((".jpg", ".jpeg")):
        print("(-) La imagen no es jpg")
        return

    # 2. Extraer y mostrar dato
    dato = extraer_metadato(ruta_imagen)
    if dato:
        print(f"(+) El dato encontrado en la imagen es : '{dato}'")
    else:
        print("(-) No se encontro metadatos")

if __name__ == "__main__":
    main()

