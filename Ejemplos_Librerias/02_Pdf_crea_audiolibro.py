# Primero se instala PyPDF3, pyttsx3 y pdfplumber con el siguiente comando  "pip install PyPDF3" , "pip install pyttsx3" , "pip install pdfplumber"
import PyPDF3
import pyttsx3
import pdfplumber

#Guardamos el nombre del pdf
nombre_pdf = 'pdf.pdf'
#El nombre del pdf mas rb que es para windows
book = open(nombre_pdf, 'rb')
#solicitamos leer ese documento
pdfReader = PyPDF3.PdfFileReader(book)
#implementamos el numpages y declaramos la variable del texto final
pages = pdfReader.numPages
finalText = ""

#se usa la libreria pdfplumber para abrir el pdf con el nombre ya guardado anteriormente
with pdfplumber.open(nombre_pdf) as pdf:
    #se ejecuta el for que recorre las paginas del pdf almacenando su contenido en una variable llamada finalText
    for i in range(0, pages): 
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text

#Se inicia la libreria pyttsx3 y luego se guardar el audio luego de recibir el texto final en una variable
# y el nombre del audio
engine = pyttsx3.init()
engine.save_to_file(finalText, 'mp3.mp3')
engine.runAndWait()





