import time
import threading
import keyboard
import numpy as np
import sounddevice as sd
import speech_recognition as sr
import os
import pyautogui
import subprocess as sp
import webbrowser
import imdb
from kivy.uix import widget,image,label,boxlayout,textinput
from kivy.uix.widget import Widget 
from kivy import clock
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,GEMINI_API_KEY
from utils import speak,search_on_google,search_on_wikipedia,send_email,get_news,find_my_ip
from jarvis_button import JarvisButton
import google.generativeai as genai

# Configure to GenAI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

class Jarvis(Widget):  # Ensure the base class is correctly defined
    def __init__(self, **kwargs):
        super(Jarvis, self).__init__(**kwargs)  # Corrected the typo in super().__init__()
        self.volume = 0
        self.volume_history = [0, 0, 0, 0, 0, 0, 0]
        self.volume_history_size = 140

        self.min_size = .2 * SCREEN_WIDTH
        self.max_size = .7 * SCREEN_WIDTH

        self.add_widget(image.Image(source='GUI/static/border.eps.png', size=(1920, 1080))) 
        self.circle = JarvisButton(size=(284.0, 284.0), background_normal = 'GUI/static/circle.png')
        self.circle.bind(on_press=self.start_recording)
        self.start_recording()
        self.add_widget(image.Image(source='GUI/static/jarvis.gif', size=(self.min_size, self.min_size), pos=(SCREEN_WIDTH / 2 - self.min_size / 2, SCREEN_HEIGHT / 2 - self.min_size / 2)))

        time_layout = boxlayout.BoxLayout(orientation='vertical', pos=(150, 900))
        self.time_label = label.Label(text='', font_size = 24, markup=True, font_name='GUI/static/mw.ttf')
        time_layout.add_widget(self.time_label)
        self.add_widget(time_layout)

        clock.Clock.schedule_interval(self.update_time, 1)

        self.title = label.Label(text='[b][color=3333ff]ERROR BY NIGHT[/color][/b]', font_size = 42, markup = True, font_name = 'GUI/static/dusri.ttf', pos=(920, 900))
        self.add_widget(self.title)

        self.subtitles_input = textinput.TextInput(
            text = 'Hello Sir! My name is Jarvis. How can I help you?',
            font_size = 24,
            readonly = False,
            background_color = (0, 0, 0, 0),
            foreground_color = (1, 1, 1, 1),
            size_hint_y = None,
            height = 80,
            pos = (720, 100),
            width = 1200,
            font_name = 'GUI/static/teesri.otf',
        )
        self.add_widget(self.subtitles_input)

        self.vrh = label.Label(text='', font_size = 30, markup = True, font_name = 'GUI/static/mw.ttf', pos = (1500, 500))
        self.add_widget(self.vrh)

        self.vlh = label.Label(text = '', font_size = 30, markup = True, font_name = 'GUI/static/mw.ttf', pos = (400, 500))
        self.add_widget(self.vlh)
        self.add_widget(self.circle)
        keyboard.add_hotkey('`',self.start_recording)

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            queri = r.recognize_google(audio, language='en-in')
            return queri.lower()
        
        except Exception:
            speak("Sorry I Couldn't understand. Could you please repeat?")
            queri = 'None'

    def start_recording(self, *args):
        print("recording started")
        threading.Thread(target=self.run_speech_recognition).start()
        print("recording ended")

    def run_speech_recognition(self):
        query = "None"  # Initialize query with a default value
        print('before speech rec obj')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            print("audio recorded")

        print("after speech rec obj")

        try:
            query = r.recognize_google(audio, language="en-in")
            print(f'Recognised: {query}')
            clock.Clock.schedule_once(lambda dt: setattr(self.subtitles_input, 'text', query))
            self.handle_jarvis_commands(query.lower())

        except sr.UnknownValueError:
            print("Google speech recognition could not understand audio")
    
        except sr.RequestError as e:
            print(e)
    
        return query.lower()

    
    def update_time(self, dt):
        current_time = time.strftime('TIME\n\t%H:%M:%S')
        self.time_label.text = f'[b][color= #3333ff]{current_time}[/color][/b]'

    def update_circle(self, dt):
        try:
            self.size_value = int(np.mean(self.volume_history))

        except Exception as e:
            self.size_value = self.min_size
            print('Warning:', e)

        if self.size_value <= self.min_size:
            self.size_value = self.min_size
        elif self.size_value >= self.max_size:
            self.size_value = self.max_size                                     
        self.circle.size = (self.size_value,self.size_value)
        self.circle.pos = (SCREEN_WIDTH / 2 - self.circle.width / 2, SCREEN_HEIGHT / 2 - self.circle.height / 2)
            
    def update_volume(self, indata, frames, time, status):
        volume_norm = np.linalg.norm(indata) * 200
        self.volume = volume_norm
        self.volume_history.append(volume_norm)
        self.vrh.text = f'[b][color= #3333ff]{np.mean(self.volume_history)}[/color][/b]'
        self.vlh.text = f'[b][color= #3333ff]{np.mean(self.volume_history)}[/color][/b]'
        self.vlh.text = f'''[b][color= #3344fff]
            {round(self.volume_history[0],7)}\n
            {round(self.volume_history[1],7)}\n
            {round(self.volume_history[2],7)}\n
            {round(self.volume_history[3],7)}\n
            {round(self.volume_history[4],7)}\n
            {round(self.volume_history[5],7)}\n
            {round(self.volume_history[6],7)}\n
            [/color][/b]'''
        
        self.vrh.text = f'''[b][color= #3344ff]
            {round(self.volume_history[0],7)}\n
            {round(self.volume_history[1],7)}\n
            {round(self.volume_history[2],7)}\n
            {round(self.volume_history[3],7)}\n
            {round(self.volume_history[4],7)}\n
            {round(self.volume_history[5],7)}\n
            {round(self.volume_history[6],7)}\n
            [/color][/b]'''
        
        if len(self.volume_history) > self.volume_history_size:
            self.volume_history.pop(0)

    def start_listening(self):
        self.stream = sd.InputStream(callback = self.update_volume)
        self.stream.start()

    def get_gemini_response(self, query):
        try:
            response = model.generate_content(query)
            return response.text
        except Exception as e:
            print(f"Error getting Gemini response: {e}")
            return "I'm sorry, I couldn't process that request."

    def handle_jarvis_commands(self, query):
        try:
            if "how are you" in query:
                speak("I am absolutely fine sir. What about you")

            elif "open command prompt" in query:
                speak("Opening command prompt")
                os.system('start cmd')

            elif "open camera" in query:
                speak("Opening camera sir")
                sp.run('start microsoft.windows.camera:', shell=True)

            elif "open notepad" in query:
                speak("Opening Notepad for you sir.")
                notepad_path = "C:\Windows\notepad.exe"
                os.startfile(notepad_path)

            elif "search on google" in query:
                speak(f"What do you want to search on google")
                query = self.take_commad().lower()
                search_on_google(query)

            elif "search on wikipedia" in query:
                speak("What do you want to search on Wikipedia sir?")
                search = self.take_command().lower()
                results = search_on_wikipedia(search)
                speak(f'According to wikipedia, {results}')

            elif "send an email" in query:
                speak("Whom do you want to send the email sir? Please enter in the terminal.")
                receiver_add = input("Email address:")
                speak("What should be the subject sir?")
                subject = self.take_command().capitalize()
                speak("What is the message?")
                message = self.take_command().captilaize()
                if send_email(receiver_add, subject, message):
                    speak("I have sent the email sir.")
                    print("I have sent the email sir.")
                else:
                    speak("something went wrong. Please check the error log.")

            elif "tell me news" in query:
                speak(f"I am reading out today's latest headlines sir.")
                speak(get_news())

            elif 'ip address' in query:
                ip_address = find_my_ip()
                speak(
                    f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                print(f'Your IP Address is {ip_address}')
            
            else:
                gemini_response = self.get_gemini_response(query)
                gemini_response = gemini_response.replace("*","")
                if gemini_response and gemini_response != "I'm sorry, I couldn't process that request.":
                    speak(gemini_response)
                    print(gemini_response)

        except Exception as e:
            print(e)
        
            


