# En el siguiente codigo de programacion, se muestra una forma sencilla
# De extraer un archivo texto en una imagen png
# Pirmero descargamos y usamos las librerias
# Primero se instala zipfile con el siguiente comando 
# "pip install zipfile"
import zipfile
import os

# Con el siguiente codigo se extrae un comprimido de adentro de la imagen
def extraer_zip_de_imagen(imagen_con_zip, salida_zip):
    with open(imagen_con_zip, 'rb') as archivo:
        datos = archivo.read()

    # Fin estándar de un PNG: IEND chunk + CRC
    fin_png = b'\x00\x00\x00\x00IEND\xaeB`\x82'
    index_fin = datos.find(fin_png)

    if index_fin == -1:
        print("La imagen que tiene la informacion, no se encontro")
        return

    # El .zip empieza justo después del final del PNG
    inicio_zip = index_fin + len(fin_png)

    with open(salida_zip, 'wb') as zip_file:
        zip_file.write(datos[inicio_zip:])

    print(f"El archivo zip extraido se llama: {salida_zip}")

# En este codigo se muestra como extraer un texto de un archivo zip
def extraer_txt_de_zip(archivo_zip, carpeta_destino='extraido'):
    os.makedirs(carpeta_destino, exist_ok=True)
    with zipfile.ZipFile(archivo_zip, 'r') as zipf:
        zipf.extractall(carpeta_destino)
    print(f"El archivo de text extraido del zip es: {carpeta_destino}")

# EJECUTAR FUNCIONES EXTRACCIÓN
extraer_zip_de_imagen('imagen_con_mensaje.png', 'extraido.zip')
extraer_txt_de_zip('extraido.zip')



