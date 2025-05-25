# En este software se muestra un ejemplo de analisis forense estatico
# Con la libreria pefile se analiza el .exe de notepad y se muestra
# que librerias usa ese ejecutable
#  pip install pefile
import pefile

# Se indica la ruta del ejecutable
pe = pefile.PE("C:\\Windows\\System32\\notepad.exe")

# Se realiza un ciclo for que muestra en pantalla las direccioon, 
# tamaño de memoria y de tamaño de archivo
for section in pe.sections:
    print(f"La Sección: {section.Name.decode().rstrip('\\x00')}")
    print(f"  La Dirección Virtual del archivo: {hex(section.VirtualAddress)}")
    print(f"  El tamaño en memoria: {hex(section.Misc_VirtualSize)}")
    print(f"  El tamaño del archivo: {hex(section.SizeOfRawData)}")
    print()

# Mostrar la dirección de entrada del ejecutable
print(f"Entry Point: {hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint)}")

# Se imprime en pantalla la información de la cabecera
print(f"Image Base: {hex(pe.OPTIONAL_HEADER.ImageBase)}")

# Mostramos los imports del archivo
if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        print(f"Importado de: {entry.dll.decode()}")
        for imp in entry.imports:
            print(f"  {hex(imp.address)} - {imp.name.decode() if imp.name else 'Import by ordinal'}")

# Cerramos la ejecucion de la libreria
pe.close()