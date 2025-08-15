# Este es un codigo para extraer la mayor cantidad de informacion de
# Un sistema operativo Android, como requisito hay que descargar
# El software y luego instalar las librerias de python
# Por ultimo dar los permisos adminin al archivo o terminal
# wsl --install
# pip install --user buildozer
# buildozer init
from jnius import autoclass, cast
from android.permissions import request_permissions, Permission
from android.storage import primary_external_storage_path
import os

def get_device_info():
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Context = cast('android.content.Context', PythonActivity.mActivity)
    Build = autoclass('android.os.Build')
    Locale = autoclass('java.util.Locale')
    DisplayMetrics = Context.getResources().getDisplayMetrics()
    TelephonyManager = cast('android.telephony.TelephonyManager',
        Context.getSystemService(Context.TELEPHONY_SERVICE))

    try:
        operator = TelephonyManager.getNetworkOperatorName()
        phone_number = TelephonyManager.getLine1Number()
        imei = TelephonyManager.getDeviceId()
        imsi = TelephonyManager.getSubscriberId()
        sim_serial = TelephonyManager.getSimSerialNumber()
    except Exception as e:
        operator = phone_number = imei = imsi = sim_serial = f"Error: {e}"

    info = {
        "Marca": Build.MANUFACTURER,
        "Modelo": Build.MODEL,
        "Android Version": Build.VERSION.RELEASE,
        "Resolución": f"{DisplayMetrics.widthPixels}x{DisplayMetrics.heightPixels}",
        "Idioma del sistema": str(Locale.getDefault().getLanguage()),
        "Operador móvil": operator,
        "Número de teléfono": phone_number,
        "IMEI": imei,
        "IMSI": imsi,
        "ICCID (SIM serial)": sim_serial,
        "Número de serie": Build.getSerial()
    }
    return info

def save_txt(data_dict, filename):
    path = primary_external_storage_path()
    full_path = os.path.join(path, 'Download', filename)
    with open(full_path, 'w') as f:
        for key, value in data_dict.items():
            f.write(f"{key}: {value}\n")

def main():
    request_permissions([
        Permission.READ_PHONE_STATE,
        Permission.READ_CONTACTS,
        Permission.READ_CALL_LOG,
        Permission.READ_SMS,
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.READ_EXTERNAL_STORAGE
    ])
    info = get_device_info()
    save_txt(info, 'info_dispositivo.txt')

if __name__ == '__main__':
    main()