# En este programa se muestra como eliminar texto particular en un
# Archivo TXT 
import re

def limpiar_texto(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    resultado = []

    meses = "enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre"
    patron_fecha = re.compile(rf'(\d{{1,2}}\s+(?:{meses})\s+\d{{4}})', re.IGNORECASE)

    for linea in lineas:
        # Datos a eliminar
        linea = re.sub(r'\[.*?\]', '', linea)

        # Verificar en que parte del texto esta esta informacion y eliminarla
        if "Sebastian Guevara Sanchez:" in linea:
            linea = linea.replace("Sebastian Guevara Sanchez:", "").strip()
            if linea:
                resultado.append(linea)
            continue  # evita agregar la línea original

        linea = linea.strip()

        if linea:
            # Luego de identificar la fecha, poner un enter atras de ella
            if patron_fecha.search(linea):
                resultado.append("")  # línea en blanco
            resultado.append(linea)

    # Editar que solo haya 1 espacio
    contenido_final = "\n".join(resultado).strip()

    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(contenido_final)

    print("Proceso completado correctamente.")


# 🔹 USO
archivo_entrada = "entrada.txt"
archivo_salida = "salida.txt"

limpiar_texto(archivo_entrada, archivo_salida)
