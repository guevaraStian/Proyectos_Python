# Primero se instala img2pdf con el siguiente comando "pip install img2pdf"
# Luego de bajar librerias, las importamos
import img2pdf

# En la siguiente linea se guarda y se convierte la imagen en bytes
with open("imagen.png", "rb") as image:
    pdf_bytes = img2pdf.convert(image.read())

# Se crea el documento pdf en este caso con la imagen en su contenido
with open("documento.pdf", "wb") as pdf:
    pdf.write(pdf_bytes)
 
# Si el proceso se realizo, se imprime en pantalla
print("La imagen se convirtio en pdf!!")




