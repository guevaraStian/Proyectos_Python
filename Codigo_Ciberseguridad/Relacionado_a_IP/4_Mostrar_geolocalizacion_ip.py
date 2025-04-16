# Primero se instala requests con el siguiente comando  "pip install requests"
#Primero se instala json con el siguiente comando  "pip install json"
import requests
import json

# URL de la API
api_url = "http://ip-api.com/json/"

# Definimos los parametros de respuesta que queremos obtener
parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
data = {"fields":parametros}

def ubicaciongeoip (ip=""):
 # Nos conectamos con la API
 res = requests.get(api_url+ip, data=data)
 # Obtenemos y procesamos la respuesta JSON
 api_json_res = json.loads(res.content)
 return api_json_res

if __name__ == '__main__':
 # Solicitamos la entrada
 ip = input("Ingrese la dirección IP: ")
 
 # Llamamos a la función ubicaciongeoip y mostramos los resultados
 par = parametros.split(",")
 for x in par:
  print(x.upper(), ":")
  print(ubicaciongeoip(ip)[x])
  print("n")

