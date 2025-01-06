import pyttsx3
import requests
import speech_recognition as sr
import keyboard
import os
import subprocess as sp
import imdb
import wolframalpha
import pyautogui
import webbrowser
import time

from datetime import datetime
from decouple import config
from const import random_text
from random import choice
from online import find_my_ip, search_on_google, search_on_wikipedia, send_email, get_news

engine = pyttsx3.init()
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 220)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

USER = config('USER')
HOSTNAME = config('BOT')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_me():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good morning {USER}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good afternoon {USER}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good evening {USER}")
    speak(f"I an {HOSTNAME}. How may I assist you? {USER}")


listening = False


def start_listening():
    global listening
    listening = True
    print("started listening")


def pause_listening():
    global listening
    listening = False
    print("stopped listening")


keyboard.add_hotkey('ctrl+alt+k', start_listening)
keyboard.add_hotkey('ctrl+alt+p', pause_listening)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        queri = r.recognize_google(audio, language='en-in')
        print(queri)
        if not 'stop' in queri or 'exit' in queri:
            speak(choice(random_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Goodnight sir, take care!")
            else:
                speak("Have a good day sir!")
            exit()

    except Exception:
        speak("Sorry I couldn't understand. Can you please repeat that?")
        queri = 'None'
    return queri 

if __name__ == '__main__':
    greet_me()
    while True:
        if listening:
            query = take_command().lower()
            if "how are you" in query:
                speak("I am absolutely fine sir. What about you?")

            elif "open command prompt" in query:
                speak("opening command prompt")
                os.system('start cmd')

            elif "open camera" in query:
                speak("opening camera sir")
                sp.run('start microsoft.windows.camera:', shell=True)

            elif "open notepad" in query:
                speak("Opening Notepad for you sir.")
                notepad_path = "C:/Windows/notepad.exe"
                os.startfile(notepad_path)

            elif "open google" in query:
                speak(f"What do you want to search on google {USER}")
                query = take_command().lower()
                search_on_google(query)

            elif "wikipedia" in query:
                speak("what do you want to search on wikipedia sir?")
                search = take_command().lower()
                results = search_on_wikipedia(search)
                speak(f"According to wikipedia, {results}")
                speak("I am printing it on a terminal.")
                print(results)

            elif "send an email" in query:
                speak("Whom do you want to send the email sir? Please enter in the terminal.")
                receiver_add = input("Email address:")
                speak("What should be the subject sir?")
                subject = take_command().capitalize()
                speak("What is the message?")
                message = take_command().capitalize()
                if send_email(receiver_add, subject, message):
                    speak("I have sent the email sir.")
                    print("I have sent the email sir.")
                else:
                    speak("something went wrong. Please check the error log.")

            elif "give me news" in query:
                speak(f"I am reading out today's latest headlines sir.")
                speak(get_news())
                speak("I am printing it on screen sir.")
                print(*get_news(), sep='\n')

            elif 'ip address' in query:
                ip_address = find_my_ip()
                speak(
                    f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                print(f'Your IP Address is {ip_address}')

            elif 'what is' in query or 'who is' in query or 'which is' in query:
                app_id = ""
                client = wolframalpha.Client(app_id)
                try:

                    ind = query.lower().index('what is') if 'what is' in query.lower() else \
                        query.lower().index('who is') if 'who is' in query.lower() else \
                            query.lower().index('which is') if 'which is' in query.lower() else None
                    
                    if ind is not None:
                        text = query.split()[ind + 2:]
                        res = client.query(" ".join(text))
                        ans = next(res.results).text
                        speak("The answer is " + ans)
                        print("The answer is " + ans)
                    else:
                        speak("I couldn't find that. Please try again.")
                except StopIteration:
                    speak("I couldn't find that. Please try again.")



            



