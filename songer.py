from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("glitchsong.mp3")

song = song + 15

play(song)
