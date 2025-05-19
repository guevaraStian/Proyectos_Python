# Primero se instala pubchempy con el siguiente comando "pip install pubchempy"
import pubchempy
import pubchempy as pcp

#Ingrese el nombre de el quimico en ingles
nombre_quimico_en = input("Ingrese el nombre del elemento quimico en ingles: ")

#Se trae la informacion relacionada a ese nombre de ese quimico 
componentes_quimicos = pcp.get_compounds(nombre_quimico_en, 'name')[0]

#Con el siguiente codigo se imprime en pantalla la informacon
print(f"Nombre IUPAC: {componentes_quimicos.iupac_name}")
print(f"Simbolo quimico: {componentes_quimicos.molecular_formula}")
print(f"Nombre comun: {componentes_quimicos.synonyms[0]}")
print(f"El peso molecular: {componentes_quimicos.molecular_weight}")



    
    










