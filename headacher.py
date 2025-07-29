from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import simpleaudio as sa

# Seçilen frekans (Hz cinsinden)
frequency = 5555  # Tek bir frekans seçildi (0-20 Hz aralığından)
duration = 180  # 3 dakika (saniye cinsinden)
sample_rate = 44100

# Ses dalgası oluştur
time = np.linspace(0, duration, int(sample_rate * duration), False)
waveform = 0.5 * np.sin(2 * np.pi * frequency * time)  # Sin dalgası oluştur

# 16-bit PCM formatına çevir
waveform = (waveform * 32767).astype(np.int16)

# Ses oynatma
play_obj = sa.play_buffer(waveform, num_channels=1, bytes_per_sample=2, sample_rate=sample_rate)
play_obj.wait_done()
