from gtts import gTTS #metin--> ses
import os
import time 
from playsound import playsound


def speak(met):
    tts=gTTS(text=met,lang="tr",slow=False)
    tts.save("met.mp3")
    os.system("met.mp3")
    
   


def intro():
    intr= " selam merhaba ben Aleksa"
    speak(intr)
    name=input("isim gir")
    if (name=="deniz"):
        soh=" hoşgeldiniz canım efendim"
        speak(soh)
        time.sleep(2)
    elif name!="deniz":
        speak("ben asla seni tanımıyorum yabancı gitmezsen bağırırım")
        time.sleep(3)
        speak("aaaaaaaaaaaaa")
        
    time.sleep(5)
    speak("çoook canın sıkıldıysa konuşalım")
    secim=input("secim?")
    if secim=="secim":
        sohbet(name)
    else:
        red()
     
def red():
    metin4="sen kimsin de beni reddediyorsun git buradan "
    speak(metin4)

def sohbet(name):
    metin="naber"+name+"im"
    speak(metin)
    cevap=input("cevap yaz")
    if cevap=="iyiyim":
        sohbet2="iyi çok mutlu oldum"
        speak(sohbet2)
    elif cevap=="kötüyüm":
        sohbet3="senin moralini nasıl düzeltirim"
        speak(sohbet3)
        a=input("cevap ver")
        if a=="bilmiyorum":
            speak("sana bir daha sormucam git hadi")
        elif a=="bana şarkı söyle":
            speak("mekanın sahibi geri geldi bebeleri pistten alalım,beğendin mi?")
            e=input("cevap ver")
            if e=="evet":
                speak("seni yerler yerler seni ham yapar bu zilliler")
            else:
                speak("sen yetenekten ne anlarsın be")
      
    
intro()
    