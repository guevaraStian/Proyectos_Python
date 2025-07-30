# En este software se muestra un ejemplo de analisis forense estatico
# Con la libreria yara se analiza un .txt en busqueda de palabras claves
# En este archivo hay un "Hola Mundo"
# pip install pefile

import yara

# Definir una regla YARA
regla = """
rule DetectaHolaMundo
{
    strings:
        $cadena1 = "Hola Mundo"
    condition:
        $cadena1
}

rule DetectaPalabraArchivo
{
    strings:
        $cadena2 = "archivo"
    condition:
        $cadena2
}
"""

# Compilar la regla
reglas = yara.compile(source=regla)

# Crear un archivo de prueba
with open("archivo_prueba.txt", "w", encoding="utf-8") as f:
    f.write("Este Archivo con A mayuscula dice : Hola Mundo")

# Aplicar la regla al archivo
matches = reglas.match("archivo_prueba.txt")

# Ver coincidencias
for match in matches:
    print(f"Regla que se encontro en el archivo : {match.rule}")