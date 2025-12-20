import requests

# URL de la API
url = "https://api-resultadosloterias.com/api/results/2025-01-01"

# Hacer la solicitud GET
response = requests.get(url)

# Verificar que la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Convertir la respuesta JSON en un diccionario de Python
    data = response.json()
    # Mostrar los resultados en pantalla
    print("Resultado de la consulta:")
    print(data)
else:
    print(f"Error en la consulta: {response.status_code}")
