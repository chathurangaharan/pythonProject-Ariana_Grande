import pywhatkit
import speech_recognition as sr
import pyttsx3
import pyaudio
from pyttsx3 import engine
import datetime
import wikipedia
import pyjokes
import os
import docx

listz = sr.Recognizer()
engine = pyttsx3.init()



def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as src:
            print('Listening...')
            voice = listz.listen(src)
            command = listz.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                # talk(command)
                return command

    except:
        pass

def run_al():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Chathuranga feel the song'+song)
        print('playing'+song)
        pywhatkit.playonyt(song)
    if 'search' in command:
        serchz = command.replace('search', '')
        talk('Chathu your search,'+serchz+'is ready')
        print('searching'+serchz)
        pywhatkit.search(serchz)
    elif 'time' in command:
        e = datetime.datetime.now()
        print("Current date and time = %s" % e)
        talk("Hi, Blacksy, The time is  :  %s:%s:%s" % (e.hour, e.minute,''))
    elif 'information' in command:
        obj = command.replace('information', '')
        info = wikipedia.summary(obj, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        jokk = pyjokes.get_joke()
        print(jokk)
        talk(jokk)
    elif 'notepad' in command:
        talk('Notepad is opening')
        cmd = 'notepad'
        os.system(cmd)
    elif 'name' in command:
        talk('you already know my name, if you do not call me alexa, I will not work, read the code line, if alexa in command'  )
    else:
        talk('Please say again')

while True:
    run_al()
