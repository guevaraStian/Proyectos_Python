# En este programa se muestra un codigo para dejar de seguir usuarios en instagram
# Se usaran 2 librerias os y instagrapi
# Primero se instala captcha con el siguiente comando "pip install instagrapi"
# archivo: generar_sh.py

nombre_script_py = "script.py"
nombre_script_sh = "ejecutar_script.sh"

contenido_sh = f"""#!/bin/bash
# Script generado automáticamente
python3 {nombre_script_py}
"""

with open(nombre_script_sh, 'w') as archivo_sh:
    archivo_sh.write(contenido_sh)

# Hacer el archivo .sh ejecutable
import os
os.chmod(nombre_script_sh, 0o755)

print(f"Archivo '{nombre_script_sh}' creado y listo para ejecutar '{nombre_script_py}'.")