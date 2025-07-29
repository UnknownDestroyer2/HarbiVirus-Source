import wave
import numpy as np

def increase_volume(input_file, output_file, gain_dB):
    with wave.open(input_file, 'rb') as wav:
        params = wav.getparams()
        frames = wav.readframes(params.nframes)
    
    # PCM verisini numpy array'e çevir
    audio_data = np.frombuffer(frames, dtype=np.int16)

    # Ses seviyesini artır (5dB ≈ 1.78 kat)
    gain = 10**(gain_dB / 20)
    audio_data = np.clip(audio_data * gain, -32768, 32767).astype(np.int16)

    # Yeni dosya olarak kaydet
    with wave.open(output_file, 'wb') as wav_out:
        wav_out.setparams(params)
        wav_out.writeframes(audio_data.tobytes())

# 5dB artırılmış yeni dosyayı kaydet
increase_volume("monosound.wav", "monosound_loud.wav", 5)
