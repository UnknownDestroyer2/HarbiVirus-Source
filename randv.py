from ctypes import cast, POINTER
import os
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_volume_to_100():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    mute_status = volume.GetMute()  # Mevcut susturma durumunu kontrol et
    if mute_status:
        volume.SetMute(0, None)  # Susturmayı kapat
    volume.SetMasterVolumeLevelScalar(1.0, None)  # 1.0 = %100 ses seviyesi

# Sesi %100 yap
set_volume_to_100()

# MP3 dosyasını başlat
os.system("start file.mp3")
