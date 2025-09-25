# Este es un codigo para extraer la mayor cantidad de informacion de
# Un sistema operativo Android, como requisito hay que descargar
# Tambien graba camaras y microfono por 5 segundos
# El software y luego instalar las librerias de python
# Por ultimo dar los permisos adminin al archivo o terminal
# pip install kivy plyer
# pip install buildozer

from jnius import autoclass, cast
from android.permissions import request_permissions, Permission
from android.storage import primary_external_storage_path
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from plyer import gps
from kivy.clock import Clock
import os
import time
from datetime import datetime
from jnius import autoclass, cast
from android.permissions import request_permissions, Permission

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


# GRABACION DE PANTALLA Y CAMARAS Y AUDIO POR 5 SEG


class MainApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.button = Button(text='Iniciar Grabación 5s')
        self.button.bind(on_press=self.start_process)
        self.layout.add_widget(self.button)
        return self.layout

    def start_process(self, instance):
        request_permissions([
            Permission.CAMERA,
            Permission.RECORD_AUDIO,
            Permission.ACCESS_FINE_LOCATION,
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.READ_EXTERNAL_STORAGE
        ], self.after_permission)

    def after_permission(self, permissions, grants):
        if all(grants):
            self.get_location()
        else:
            print("Permisos no concedidos.")

    def get_location(self):
        try:
            gps.configure(on_location=self.on_location, on_status=self.on_status)
            gps.start(minTime=1000, minDistance=0)
            # Esperamos 5 segundos por GPS
            Clock.schedule_once(lambda dt: gps.stop(), 5)
        except NotImplementedError:
            print("GPS no implementado en este dispositivo")

    def on_location(self, **kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        print(f"Ubicación: {lat}, {lon}")
        self.lat = lat
        self.lon = lon
        self.start_recording()

    def on_status(self, stype, status):
        print(f"Estado GPS: {stype} - {status}")

    def start_recording(self):
        # Obtenemos nombre del dispositivo
        Build = autoclass('android.os.Build')
        device_name = Build.MODEL

        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        folder_name = f"Informe_{device_name}_{timestamp}_{self.lat}_{self.lon}"
        base_path = f"/sdcard/{folder_name}"
        os.makedirs(base_path, exist_ok=True)

        # Usamos la app de cámara nativa para grabar video 5s
        Intent = autoclass('android.content.Intent')
        MediaStore = autoclass('android.provider.MediaStore')
        Uri = autoclass('android.net.Uri')
        File = autoclass('java.io.File')
        Environment = autoclass('android.os.Environment')

        video_file = File(f"{base_path}/video.mp4")
        video_uri = autoclass('androidx.core.content.FileProvider').getUriForFile(
            self._get_activity(),
            f"{self._get_activity().getPackageName()}.provider",
            video_file
        )

        intent = Intent(MediaStore.ACTION_VIDEO_CAPTURE)
        intent.putExtra(MediaStore.EXTRA_DURATION_LIMIT, 5)
        intent.putExtra(MediaStore.EXTRA_OUTPUT, cast('android.os.Parcelable', video_uri))
        intent.addFlags(Intent.FLAG_GRANT_WRITE_URI_PERMISSION)

        self._get_activity().startActivity(intent)

    def _get_activity(self):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        return PythonActivity.mActivity



if __name__ == '__main__':
    main()
    MainApp().run()











