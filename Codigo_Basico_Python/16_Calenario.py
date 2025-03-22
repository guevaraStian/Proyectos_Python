# Primero se instala calendar con el siguiente comando "pip install calendar"
# Luego de bajar librerias, las importamos
import calendar

# En la siguiente linea se cre la funcion
def display_calendar():
    #Se guardan las variables de año y mes
    año= int(input("Enter year: "))
    mes = int(input("Enter month (1-12): "))
    #Se crea la variable con la configuracion del calendario hasta domingo
    calen = calendar.TextCalendar(calendar.SUNDAY)
    #se le ingresa el año y el mes del calendario que se quiere mostrar en pantalla
    mes_calendario = calen.formatmonth(año, mes)
    # Se muestra en pantalla el calendario
    print(mes_calendario)
display_calendar()


