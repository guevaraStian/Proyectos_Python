# Primero se instala speedtest con el siguiente comando "pip install speedtest-cli"
import speedtest as st

#En la funcion llamada prueba de velocidad esta toda la logica del programa
def prueba_de_velocidad():
    prueba = st.Speedtest()
    
    #Con el siguiente bloque de codigo, se una la opcion dowload de la libreria para ver la velocidad de bajada
    velocidad_bajada = prueba.download()
    velocidad_bajada = round(velocidad_bajada / 10**6, 2)
    print("Velocidad de bajada en Mbps: ", velocidad_bajada)

    #Con el siguiente bloque de codigo, se una la opcion upload de la libreria para ver la velocidad de subida
    velocidad_subida = prueba.upload()
    velocidad_subida = round(velocidad_subida / 10**6, 2)
    print("Velocidad en subida en Mbps: ", velocidad_subida)

    #Por ultimo se muestra el ping de la comunicacion a internet
    ping = prueba.results.ping
    print("El pign actual es : ", ping)
prueba_de_velocidad()



    
    










