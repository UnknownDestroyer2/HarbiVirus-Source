from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import POINTER, cast
import simpleaudio as sa
from pydub.generators import Sine
from pydub import AudioSegment
import random

def set_volume_to_100():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    mute_status = volume.GetMute()  # Mevcut susturma durumunu kontrol et
    if mute_status:
        volume.SetMute(0, None)  # Susturmayı kapat
    volume.SetMasterVolumeLevelScalar(1.0, None)  # 1.0 = %100 ses seviyesi

def generate_glitch_sound(duration_ms=1000):
    """Rastgele frekanslar ve kopuk dalgalarla bozulma sesi oluşturur."""
    sound = AudioSegment.silent(duration=0)
    for _ in range(1000):  # 10 farklı rastgele bozulma sesi segmenti
        frequency = random.randint(300, 2000)  # 300 Hz ile 2000 Hz arası
        wave = Sine(frequency).to_audio_segment(duration=random.randint(50, 200))  # Kısa sinyal
        wave = wave + random.randint(99, 100)  # Ses yüksekliğinde rastgelelik
        if random.choice([True, False]):  # Rastgele distorsiyon
            wave = wave.reverse()
        sound += wave
        sound += AudioSegment.silent(duration=random.randint(50, 150))  # Kopukluklar
    return sound

def play_sound(sound):
    """Oluşturulan sesi çalar."""
    playback = sa.play_buffer(
        sound.raw_data,
        num_channels=sound.channels,
        bytes_per_sample=sound.sample_width,
        sample_rate=sound.frame_rate
    )
    playback.wait_done()

if __name__ == "__main__":
    set_volume_to_100()  # Ses seviyesini %100'e ayarla
    print("Ses seviyesi %100'e ayarlandı. Bozulma sesi çalınıyor...")
    glitch_sound = generate_glitch_sound(duration_ms=2000)
    play_sound(glitch_sound)
