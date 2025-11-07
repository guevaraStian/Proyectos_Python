# Primero se instala wifiqrcode con el siguiente comando "pip install python-barcode" "pip install Ipython"
import barcode
from barcode.writer import ImageWriter
from IPython.display import Image, display

# Con el siguiente codigo, se guarda la informacion dentro del codigo de barras y el nombre del archivo
contenido = input("Por favor ingrese 12 digitos de la informacion del Codigo de barras: ")
nombre_archivo = "CodigoDeBarras"

#Se escoge el formato ean13 del barcode
formato_codigo_barras = barcode.get_barcode_class('ean13')

#Se crea la imagen de codigo de barras y se guarda en una variable
imagen_codigo_barras = formato_codigo_barras(contenido, writer = ImageWriter())
imagen_codigo_barras.save(nombre_archivo)

#Se muestra la imagen creada
display(Image(filename = f'{nombre_archivo}.png'))




