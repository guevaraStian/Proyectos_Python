# Primero se instala datetime con el siguiente comando  "pip install datetime"
from datetime import datetime
import os
while True:
    a = datetime.now()
    # se selecciona la hora y luego se agrega el audio que va a sonar
    if a.hour==4: 
        os.popen2('/usr/bin/totem --play /usr/share/sounds/')  
        # se selecciona la hora y luego se agrega el audio que va a sonar  
        break 

