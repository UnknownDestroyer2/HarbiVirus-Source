import random
import time
import os
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import tkinter as tk
from tkinter import messagebox

def set_volume_level(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level / 100, None)

def random_volume_changer(duration):
    end_time = time.time() + duration
    while True:  # Sonsuza kadar rastgele değiştirir
        random_volume = random.randint(0, 100)  # 0 ile 100 arasında rastgele bir ses seviyesi
        set_volume_level(random_volume)
        time.sleep(0.05)  # Aşırı hızlı değiştirme için bekleme süresi

def show_message():
    root = tk.Tk()
    root.withdraw()  # Ana pencereyi gizler
    if messagebox.askokcancel("Ses Seviyesi", "Bilgisayarının ses seviyesine bakar mısın?"):
        os.system("start file.mp3")  # MP3 dosyasını açar
    root.destroy()

# Mesaj göster ve 3 saniye bekle
root = tk.Tk()
root.withdraw()
message_id = root.after(0, show_message)  # Mesajı göster
root.after(3000, root.quit)  # 3 saniye sonra kapat
root.mainloop()

# Rastgele ses seviyesini değiştirmeye devam et
random_volume_changer(15)
