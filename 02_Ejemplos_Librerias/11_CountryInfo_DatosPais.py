####
# Primero se instala countryinfo con el siguiente comando "pip install countryinfo"
# Luego de bajar librerias, las importamos
from countryinfo import CountryInfo

# Se guarda en una variable el nombre de un pais en el idioma ingles
Nombre_Pais = input("Ingrese el nombre de un pais en el idioma ingles: ")

# luego guardamos la informacion en una variable, despues de consultar el nombre del pais
info_pais = CountryInfo(Nombre_Pais)

# El siguiente codigos se imprime en pantalla diferentes datos del pais consultado
print("La capital es :", info_pais.capital())
print("Simbolos de su moneda : ", info_pais.currencies())
print("El idioma mas usado es : ", info_pais.languages())
print("Los paises en frontera son : ", info_pais.borders())
print("Nombre completo : ", info_pais.alt_spellings())