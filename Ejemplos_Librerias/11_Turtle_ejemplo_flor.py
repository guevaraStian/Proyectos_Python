####
# Primero se instala turtle con el siguiente comando "pip install turtle"
# Luego de bajar librerias, las importamos
import turtle

# Se crean las variables que muestran el dibujo de la flor
t= turtle.Turtle()
s= turtle.Screen()
s.bgcolor('#474747')
t.pencolor('#ff0000')
t.speed(100)

# Creamos la variable que tiene los colores que se usaran en la sombraa de la flor
col=('#ff5000','#ff5500','#ff5555','#ff8888')

# El siguiente grupo de for es la descripcion de el camino que hara el objeto dibujante
# Recorriendo un cuadro de diferentes colores
for n in range(5):
    for x in range(8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(2)
            t.circle(90+n*20,90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n%4])
s.exitonclick()






