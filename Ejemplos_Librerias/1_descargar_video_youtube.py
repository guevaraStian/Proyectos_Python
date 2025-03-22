# Primero se instala pytube con el siguiente comando  "pip install pytube"
from pytube import YouTube

#Los siguientes codigo solicitan la url del video y lo convierte en datos 
link = input("Por favor, ingrese la direccion del video en youtube: ")
yt = YouTube(link)
formatos_video= yt.streams.all()

#La siguiente linea, organiza los tipos de formato del video que se puede descargar
video =list(enumerate(formatos_video))

#Este for imprime los tipos de formato de video en los que se puede descargar
for i in video:
    print(i)

#Se pregunta cual de los formatos de descarga va a elegir y lo guarda en la variable option_escogida
print("ingrese la opción deseada para descargar el formato ")
option_escogida = int(input(" La opcion es : "))

descargar_video= formatos_video[option_escogida]
descargar_video.download()  #Con este comando se descarga el video

print(" Descarga exitosa")






