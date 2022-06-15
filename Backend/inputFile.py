from setuptools import Command
import speech_recognition as sr
from colorama import Fore
from outputFile import output 
import random

def speech_to_text():
    query = ''
    r=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            print('Listening...')
            audio=r.listen(source, timeout=8, phrase_time_limit=8)
            print('Done Listening...')
            query = r.recognize_google(audio)
        
    except Exception:
            print("No input")
        
    print(query)
    return query.lower()