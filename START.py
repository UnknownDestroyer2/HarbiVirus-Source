import subprocess
import time

# Dosya yolları
video_path = "bayrak.mp4"
audio_path = "mehter.mp3"
audio_path1 = "boom.mp3"
audio_path2 = "narrator.mp3"
batch_file_path = r"C:\data\HarbiVirus.bat"  # Batch dosyasının tam yolu



subprocess.Popen(["ffplay", "-nodisp", "-autoexit", "-af", "volume=10dB", audio_path1], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(3)
# Video ve sesi eş zamanlı başlat
subprocess.Popen(["ffplay", "-fs", "-autoexit", video_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.Popen(["ffplay", "-nodisp", "-autoexit", "-af", "volume=10dB", audio_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 15 saniye bekle ve sonra HarbiVirüs.bat'ı çalıştır
time.sleep(15)
subprocess.Popen([batch_file_path], shell=True)

# Toplam 2 dakika 16 saniye bekle
time.sleep(136 - 15)  # İlk 15 saniye çıkarıldı

# Süre bitiminde video ve sesi durdur
subprocess.call("taskkill /im ffplay.exe /f", shell=True)  # Windows için
subprocess.call("pkill -f ffplay", shell=True)            # Linux/MacOS için
