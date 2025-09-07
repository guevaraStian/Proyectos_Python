# Primero se instala wifiqrcode con el siguiente comando "pip install tqdm"
from tqdm import tqdm_notebook as tqdm
import time

# Con el siguiente codigo, se crea la barra de progreso que poco a poco se llena
for i in tqdm(range(20)):
    print(i)






