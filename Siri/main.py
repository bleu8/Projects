from gtts import gTTS #metin--> ses
import os

tts=gTTS(text="merhaba",lang="tr")
tts.save("merhaba.mp3")
os.system("merhaba.mp3")