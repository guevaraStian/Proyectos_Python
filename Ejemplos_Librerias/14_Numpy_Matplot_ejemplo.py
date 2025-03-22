# Primero se instala numpy con el siguiente comando "pip install numpy"
# Primero se instala matplotlib con el siguiente comando "pip install matplotlib"
# Primero se instala mpl_toolkits con el siguiente comando "pip install mpl_toolkits"
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3D

#En las siguientes lineas, se especifica los rangos de informacion en cada eje de la grafica
x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
x, y = np.meshgrid(x,y)
z= np.exp(-0.5 * (x**2 + y**2)) * 10

#En los siguientes codigos se crea la figura dentro del plano carteciano 
fig = plt.figure(figsize = (10,8))
ax = fig.add_subplot(111, projection = '3d')
surf = ax.plot_surface(x,y,z, cmap='terrain', edgecolor= 'none')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

#Se le ponen nombre a las dimensiones de el plano carteciano 3d
ax.set_title("Simulacion relieve de una montaña sintetica")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Elevacion Z")
plt.show()










