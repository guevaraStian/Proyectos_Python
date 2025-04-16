# Primero se instala geopy con el siguiente comando  "pip install geopy"
#Primero se instala folium con el siguiente comando  "pip install folium"
# importando Geopy
import geopy
import folium
# obtener un manejador para un objeto de servicio de Nominatim
service = geopy.Nominatim(user_agent = "myGeocoder")
# Solicitamos el nombre de la ciudad que se va a mostrar en el mapa
nombre_ciudad = input("Ingrese el nombre de la ciudad que necesita localizar: ")
# guardamos el nombre de la ciudad codificado en la variable
ubicacion = service.geocode(nombre_ciudad)
# latitud
#print(locationObj.latitude)
# longitud
#print(locationObj.longitude)

# crear un mapa base centrado en la longitus y latitud de la ciudad escogida
ObjetoMapa = folium.Map(location = [ubicacion.latitude,ubicacion.longitude], zoom_start = 5, tiles='OpenStreetMap')
# crear un objeto marcador para la ciudad escogida
SeñalarUbicacion = folium.Marker(location = [ubicacion.latitude,ubicacion.longitude])
# añadir marcador al mapa
SeñalarUbicacion.add_to(ObjetoMapa)
# guardamos el mapa en un archivo .html para poderlo visualizar
ObjetoMapa.save('mapa.html')



