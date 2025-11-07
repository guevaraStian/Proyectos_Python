# Esta libreria ayudar a crear graficas de electronica
# Primero se instala schemdraw con el siguiente comando "pip install schemdraw"

import schemdraw
import schemdraw.elements as elm


# Se inicializa la libreria en la variable d
d = schemdraw.Drawing()

# Se crean los componentes que tendra la gafica
v = d.add(elm.SourceV().label('V', loc='left'))
r = d.add(elm.Resistor().label('R').right())
c = d.add(elm.Capacitor().label('C').right())
l = d.add(elm.Inductor().label('L').right())

# Se crea la grafica
d.add(elm.Ground().at(v.start))
d.add(elm.Ground().at(v.end))
d.draw()









