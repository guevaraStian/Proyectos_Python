# Primero se instala pyshorteners con el siguiente comando  "pip install pyshorteners"
import pyshorteners
# Agregamos el enlace
link='https://github.com/guevaraStian'
# Mostramos el enalce acortado
print(pyshorteners.Shortener().clckru.short(link))

