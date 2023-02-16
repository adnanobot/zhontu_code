import speech_recognition as sr
import pyttsx3
from gtts import gTTS as gt
from playsound import playsound

def bola():
    engine = pyttsx3.init()
    voice_id = 1
    engine.setProperty('rate', 120)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)
    engine.say("Assalamu alaikum")
    engine.say("Beluman, hoi hoi. Beluman")
    engine.say("Where is Muaz?")
    engine.runAndWait()


def shuna():
    speech = sr.Recognizer()
    print('Python is listening...')

    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        audio = speech.listen(source)
        inp = speech.recognize_google(audio)

    print(f'You just said {inp}.')

# bola()

text = "Astaghfirullah"
converted_speech = gt(text, 'en', slow=False)
converted_speech.save("kotha.mp3")
playsound("kotha.mp3")
