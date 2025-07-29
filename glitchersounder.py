import numpy as np
import sounddevice as sd

# Parametreler
duration = 180  # 3 dakika (saniye cinsinden)
samplerate = 44100  # Standart CD kalitesinde ses örnekleme oranı

# Beyaz gürültü (cızırtı sesi) oluştur
noise = np.random.uniform(-1, 1, int(duration * samplerate))

# Sesi çal
sd.play(noise, samplerate)

# Bitmesini bekle
sd.wait()
