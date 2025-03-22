# Primero se instala pytube con el siguiente comando  "pip install geopy"
#Primero se instala pytube con el siguiente comando  "pip install ArcGIS"
# importando Geopy
from geopy.geocoders import ArcGIS
from geopy.distance import geodesic

#Se declara l usuario de ArcGIS
geolocator = ArcGIS(user_agent="my_application")

#Solicitamos los nombres de la ciudad inicial y la ciudad final
nombre_ciudad_1 = input("Ingrese el nombre de la ciudad inicial : ")
nombre_ciudad_2 = input("Ingrese el nombre de la ciudad final : ")

#Con los nombres y ArcGIS guardamos la ubicacion de cada ciudad 
position_1 = geolocator.geocode(nombre_ciudad_1)
position_2 = geolocator.geocode(nombre_ciudad_2)

#la ubicacion de cada ciudad se convierte en coordenadas
coords_1 = ((position_1.latitude, position_1.longitude ))
coords_2 = ((position_2.latitude, position_2.longitude ))

#Con geodesic, se logra la distancia en kilometros de las 2 ciudades
distancia = str(geodesic(coords_1, coords_2).km)

#Imprimimos la respuesta
print("La distancia entre la ciudad "+ nombre_ciudad_1 +" y la ciudad "+ nombre_ciudad_2 + " es de "+distancia+" Kms")
