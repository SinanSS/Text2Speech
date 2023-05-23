from gtts import gTTS
import os
import playsound


def speak(text, language):
    tts = gTTS(text=text, lang=language)

    filename = 'result.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


text = input('Metin giriniz: ')
language = input('Dil seçiniz (Örn: tr, en): ')

speak(text, language)
