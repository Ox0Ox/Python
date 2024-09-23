import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr 
import wikipedia
import datetime
from datetime import date
import wolframalpha
import os
import sys
#from google import google
from ctypes import windll
import string
import stat
import ast
import tempfile
from time import ctime
import time
from gtts import gTTS
import json
import logging
import platform
import sys
import pywhatkit
import pyjokes


engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('AJ64YW-WRV7GL89KX')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

state = 'querymode'

def read_json():
    logging.info('Reading configuration data.')
    # Reading data file
    with open('config/config.json') as file:
        return json.load(file)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak('good morning')
       
    elif hour >=12 and hour <18:
        speak('good afternoon')
        
    else:
        speak("good evening")
       
greetMe()

speak('Harsh')
speak('Friday here')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.energy_threshold = 350
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
       
    except sr.UnknownValueError:
        with sr.Microphone() as source:                                                                       
            speak('Pardon me sir. Could you please repeat.')
            print("Listening...")
            r.energy_threshold = 350
            r.pause_threshold =  1
            audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio, language='en-in')
            print('User: ' + query + '\n')
        
        except sr.UnknownValueError:
            with sr.Microphone() as source:                                                                       
                speak('Pardon me sir. Could you please repeat.')
                print("Listening...")
                r.energy_threshold = 350
                r.pause_threshold =  1
                audio = r.listen(source)
            try:
                print("Recognising...")
                query = r.recognize_google(audio, language='en-in')
                print('User: ' + query + '\n')
            
            except sr.UnknownValueError:
                speak('Sorry sir! I still couldn\'t get that! try typing the command')
                query = str(input('Command:'))

    if 'please' in query or 'tell me about' in query or 'do a'in query or 'on' in query or 'favour' in query or 'do me a' in query or 'could you' in query or 'can you' in query or 'about' in query or 'tell me' in query or 'friday' in query:
        query = query.replace('please ', '').replace('tell me about ', '').replace('do a ', '').replace('on', '').replace('favour ', '').replace('do me a ', '').replace('could you ', '').replace('can you ', '').replace('about ', '').replace('tell me ', '').replace('friday ', '')

    return query

def sleepCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.energy_threshold = 350
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
       
    except sr.UnknownValueError:
        query = 'none'

    return query

def response():
    stMsgs = ['what shall i do next','what may i do for you now','what would you like me to do for you next','What assistance may i be of','what can i do for you']
    speak(random.choice(stMsgs))

def GoogleSearchResult(query):
    try:    
        searchResult = google.search(query)
        for result in searchResult:
            print(result.description.replace('...','').rsplit('.',3))
            speak(result.description.replace('...','').rsplit('.',3))
            break
    except:
        tabURL = "http://google.com/search?q="
        webbrowser.open(tabURL+query)
        speak('Got it.')

def replacewords(query):
    if 'please' in query or 'do a' in query or 'on' in query or 'favour' in query or 'do me a' in query or 'could you' in query or 'can you' in query or 'about' in query or 'tell me' in query:
        query = query.replace('please ', '').replace('do a ', '').replace('on', '').replace('favour ', '').replace('do me a ', '').replace('could you ', '').replace('can you ', '').replace('about ', '').replace('tell me ', '')

#def joke1(query):
#    jk1 = pyjokes.get_joke()
#    print(jk1)
#    speak(jk1)
#    userans2 = myCommand()
#    if 'one more' in userans2 or 'another one' in userans2 or 'another joke' in userans2:
#        speak("alright, ")
#        joke1(query)
#        response()


#def joke(query):
#    if 'joke' in query:
#        jk = pyjokes.get_joke()
#        print(jk)
#        speak(jk)
#        userans1 = myCommand()
#        if 'one more' in userans1 or 'another one' in userans1 or 'another joke' in userans1:
#            speak("alright, ")
#            joke1(query)
#            response()

if __name__ == '__main__':
    
    while True:

        if state == 'sleep':
            query = sleepCommand()
            query = query.lower()
            if 'wake up' in query:
                state = 'querymode'
                speak('Friday online')
                speak('How may i help you')
        
        if state == 'querymode':
            query = myCommand()
            query = query.lower()
            print("Bot: ")

        if 'friday' in query:
            query = query.replace('friday','')
            replacewords(query)
            
            if 'wake up' in query:
                speak('i am already online sir')
                response()

            elif 'open' in query and 'folder' not in query and 'file' not in query:
                query = query.replace('open ','')
                speak('opening'+query)
                anyURL = 'www.'+query+'.com'
                webbrowser.open(anyURL)
                response()

            elif 'open folder' in query:
                try:
                    speak('opening'+query)
                    os.system('explorer C:\\HARSH PATNAIK\\"{}"'.format(query.replace('open folder ','')))
                    response()
                except:
                    speak('Folder not found')
                    response()


            elif "wikipedia" in query:
                speak("searching wikipedia...")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences = 2)
                print(results)
                speak("According to wikipedia")
                speak(results)
                response()

            elif 'how are you' in query:
                stMsgs = [ 'I am fine', 'i was wondering the same thing', 'I am full of energy', 'i am feeling energetic and im ready to comply!']
                speak(random.choice(stMsgs))
                speak('How are you?')
                userans = myCommand()
                if 'fine' in userans or 'happy' in userans or 'okay' in userans or 'not bad' in userans:
                    speak('Thats Great') 
                    response() 
                elif 'not good' in userans or 'sad' in userans or 'upset' in userans or 'bad' in userans:
                    speak('sorry to hear that')

                speak('What would you like me to do for you')

            elif 'play' in query:
                query = query.replace('play', '')
                speak("Playing" + query)
                print("Playing" + query)
                pywhatkit.playonyt(query)
                response()

            elif 'joke' in query:
                jk1 = pyjokes.get_joke()
                print(jk1)
                speak(jk1)

            elif 'another one' in query or 'one more' in query:
                if 'joke' in prevQ:
                    speak("alright, ")
                    jk2 = pyjokes.get_joke()
                    print(jk2)
                    speak(jk2)

            elif "remember that" in query:
                query = query.replace('remember that','')
                remember_text = query
                speak("Alright sir i will remember that")

            elif "what did i ask you to remember" in query:
                try:
                    print("You told me to remember that" + remember_text)
                    speak("You told me to remember that" + remember_text)
                    response()
                except:
                    print('You did not ask me to remember anything')
                    speak('you did not ask me to remember anything')
                    response()

            elif "what\'s up" in query:
                stMsgs = ['Just doing my thing!','the sky','nothing much']
                speak(random.choice(stMsgs))
                speak('What would you like me to do for you')

            elif "who are you" in query or 'what is your name' in query or 'what are you' in query:
                speak("I am Friday, your personal assistant")
                speak('what can i do for you')

            elif 'sibling' in query or 'brother' in query or 'sister' in query and 'your' in query:
                speak('We are here to talk about you, not me')
                speak('What assistance may i be of')

            elif 'good morning' in query or 'good afternoon' in query or 'good evening' in query:
                hour = int(datetime.datetime.now().hour)
                if hour >=0 and hour<12:
                    speak('good morning')
                elif hour >=12 and hour <18:
                    speak('good afternoon')
                else:
                    speak("good evening")

                speak('What would you like me to do for you')

            elif 'what can you do' in query:
                speak('here are a few thing which i can do')
                speak('open websites, launch applications, search the web and communicate with you')
                speak('What assistance may i be of')

            elif "the time" in query:
                time = datetime.datetime.now().strftime("%H:%M")
                speak("Sir the time is")
                print(time)
                speak(time)
                response()

            elif 'the day' in query:
                day = datetime.datetime.now()
                speak('today is')
                print(day.strftime("%A"))
                speak(day.strftime("%A"))
                response()

            elif 'sleep' in query:
                stMsgs = ['Going to sleep mode.']
                speak(random.choice(stMsgs))
                state = 'sleep'

            elif 'quit' in query or 'abort' in query or 'bye' in query or 'stop' in query or 'good night' in query or 'nothing else' in query or 'no need to help me' in query:
                stMsgs = ['Goodbye sir. hope you have a great day.',"until next time",'till we meet again']
                RND = random.choice(stMsgs)
                speak(RND)
                print(RND)
                sys.exit()

            elif 'shutdown' in query and 'computer':
                print('shutting down')
                speak('shutting down')
                stMsgs = ['Goodbye sir. hope you have a great day.',"until next time"]
                speak(random.choice(stMsgs))
                os.system('shutdown -s')
                os.system('TASKKILL /F /IM code.exe')
                sys.exit()

            elif 'restart' in query and 'computer':
                print('restarting...')
                speak('restarting')
                stMsgs = ['Goodbye sir. hope you have a great day.',"until next time"]
                speak(random.choice(stMsgs))
                os.system('shutdown -r')
                os.system('TASKKILL /F /IM code.exe')
                sys.exit()

            elif 'hello' in query or 'hey' in query:
                stMsgs = ['Hello Sir', 'Hello sir, always at your service']
                speak(random.choice(stMsgs))
                speak('what assistance may i be of')

            elif "launch chrome" in query or 'launch google chrome' in query:
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                speak("Launching chrome")
                os.startfile(chromePath)
                response()

            elif "launch opera" in query:
                operaPath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Opera\\launcher.exe"
                speak("Launching opera")
                os.startfile(operaPath)
                response()

            elif "launch notepad" in query:
                notePath = "C:\\Windows\\system32\\notepad.exe"
                speak("Launching notepad")
                os.startfile(notePath)
                response()

            elif "launch calculator" in query:
                calcPath = "C:\\Windows\\system32\\calc.exe"
                speak("Launching calculator")
                os.startfile(calcPath)
                response()

            elif 'launch powerpoint' in query or 'launch microsoft powerpoint' in query or 'launch ms powerpoint' in query:
                pptpath = 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\POWERPNT'
                speak('launching MS powerpoint')
                os.startfile(pptpath)
                response()

            elif 'launch word' in query or 'launch microsoft word' in query or 'launch ms word' in query:
                wordpath = 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\WINWORD'
                speak('launching MS word')
                os.startfile(wordpath)
                response()

            elif 'launch paint' in query or 'launch microsoft paint' in query or 'launch ms paint' in query:
                paintpath = 'C:\\Windows\\system32\\mspaint'
                speak('launching MS paint')
                os.startfile(paintpath)
                response()

            elif 'launch vlc' in query:
                vlcpath = "C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe"
                speak('launching vlc media player')
                os.startfile(vlcpath)
                response()

            elif "youtube" in query and 'search' in query:
                speak("searching youtube...")
                print('searching youtube...')
                query = query.replace("youtube search","")
                try:
                    tabURL = "https://www.youtube.com/results?search_query="
                    webbrowser.open(tabURL+query)
                    speak('got it')
                    response()
                except:
                    speak('unable to connect')
                    response()

            elif 'search' in query and 'google' in query:
                speak('searching google...')
                print('searching google...')
                query = query.replace("google ","").replace('search ','')
                tabURL = "http://google.com/search?q="
                webbrowser.open(tabURL+query)
                speak('Got it.')
                response()


            elif "search" in query and 'google search' not in query and 'search google' not in query and 'youtube' not in query:
                speak("searching...")
                query = query.replace("search","")
                try:
                        try:
                            res = client.query(query)
                            results = next(res.results).text or next(res.results).jpg
                            speak('Got it.')
                            print(results)
                            speak(results)
                            response()

                        except:
                            results = wikipedia.summary(query, sentences = 2)
                            speak('got it')
                            print(results)
                            speak(results)
                            response()

                except:
                    speak('got it')
                    GoogleSearchResult(query)
                    response()

            else:
                query = query
                ans = ['give me a minute','just a second'] 
                speak(random.choice(ans))
                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).text or next(res.results).jpg
                        speak('got it')
                        print(results)
                        speak(results)
                        response()

                    except:
                        results = wikipedia.summary(query, sentences = 2)
                        speak('got it')
                        print(results)
                        speak(results)
                        response()

                except:
                    speak('got it')
                    GoogleSearchResult(query)
                    response()

        else:
            state = 'sleep'