import pywhatkit
import speech_recognition as sr
import pyttsx3
import pyaudio
from pyttsx3 import engine

listz = sr.Recognizer()
try:
    with sr.Microphone() as src:
        print('Tell me...')
        voice = listz.listen(src)
        comm = listz.recognize_google(voice)
        comm = comm.lower()
        if 'alexa' in comm:
            print(comm)
except:
    pass


