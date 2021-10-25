import pywhatkit
import speech_recognition as sr
import pyttsx3
import pyaudio
from pyttsx3 import engine

listz = sr.Recognizer()
engine = pyttsx3.init()



def talk(text):
    engine.say(text)
    engine.runAndWait()


try:
    with sr.Microphone() as src:
        print('Listening...')
        voice = listz.listen(src)
        comm = listz.recognize_google(voice)
        comm = comm.lower()
        if 'alexa' in comm:
            talk(comm)
except:
    pass


