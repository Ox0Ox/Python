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
from google import google
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


engine = pyttsx3.init()

client = wolframalpha.Client('AJ64YW-WRV7GL89KX')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

state = 'querymode'

def read_json():
    logging.info('Reading configuration data.')
    # Reading data file
    with open('config/config.json') as file:
        return json.load(file)

def print(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        print('good morning')
       
    elif hour >=12 and hour <18:
        print('good afternoon')
        
    else:
        print("good evening")
       
greetMe()

print('Harsh')
print('Friday here')
print('How may I help you?')


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
            print('Pardon me sir. Could you please repeat.')
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
                print('Pardon me sir. Could you please repeat.')
                print("Listening...")
                r.energy_threshold = 350
                r.pause_threshold =  1
                audio = r.listen(source)
            try:
                print("Recognising...")
                query = r.recognize_google(audio, language='en-in')
                print('User: ' + query + '\n')
            
            except sr.UnknownValueError:
                print('Sorry sir! I still couldn\'t get that! try typing the command')
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
    stMsgs = ['what shall I do next','what may I do for you now','what would you like me to do for you next','What assistance may I be of','what can I do for you']
    print(random.choice(stMsgs))

def GoogleSearchResult(query):
    try:    
        searchResult = google.search(query)
        for result in searchResult:
            print(result.description.replace('...','').rsplit('.',3))
            print(result.description.replace('...','').rsplit('.',3))
            break
    except:
        tabURL = "http://google.com/?#q="
        webbrowser.open(tabURL+query)
        print('Got it.')

def replacewords(query):
    if 'please' in query or 'do a'in query or 'on' in query or 'favour' in query or 'do me a' in query or 'could you' in query or 'can you' in query or 'about' in query or 'tell me' in query:
        query = query.replace('please ', '').replace('do a ', '').replace('on', '').replace('favour ', '').replace('do me a ', '').replace('could you ', '').replace('can you ', '').replace('about ', '').replace('tell me ', '')




if __name__ == '__main__':
    
    while True:

        if state == 'sleep':
            query = sleepCommand()
            query = query.lower()
            if 'wake up' in query:
                state = 'querymode'
                print('Friday online')
                print('How may I help you')
        
        if state == 'querymode':
            query = myCommand()
            query = query.lower()

        if 'friday' in query:
            query = query.replace('friday','')
            replacewords(query)
            
            if 'wake up' in query:
                print('I am already online sir')
                response()

            elif 'open' in query and 'folder' not in query and 'file' not in query:
                query = query.replace('open ','')
                print('opening'+query)
                anyURL = 'www.'+query+'.com'
                webbrowser.open(anyURL)
                response()

            elif 'open folder' in query:
                try:
                    print('opening'+query)
                    os.system('explorer C:\\HARSH PATNAIK\\"{}"'.format(query.replace('open folder ','')))
                    response()
                except:
                    print('Folder not found')
                    response()


            elif "wikipedia" in query:
                print("searching wikipedia...") 
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences = 2)
                print(results)
                print("According to wikipedia")
                print(results)
                response()

            elif 'how are you' in query:
                stMsgs = [ 'I am fine', 'I was wondering the same thing', 'I am full of energy', 'I am feeling energetic and im ready to comply!']
                print(random.choice(stMsgs))
                print('How are you?')
                userans = myCommand()
                if 'fine' in userans or 'happy' in userans or 'okay' in userans or 'not bad' in userans:
                    print('Thats Great') 
                    response() 
                elif 'not good' in userans or 'sad' in userans or 'upset' in userans or 'bad' in userans:
                    print('sorry to hear that')

                print('What would you like me to do for you')

            elif "remember that" in query:
                query = query.replace('remember that','')
                remember_text = query
                print("Alright sir I will remember that")

            elif "what did I ask you to remember" in query:
                try:
                    print("You told me to remember that" + remember_text)
                    print("You told me to remember that" + remember_text)
                    response()
                except:
                    print('You did not ask me to remember anything')
                    print('you did not ask me to remember anything')
                    response()

            elif "what\'s up" in query:
                stMsgs = ['Just doing my thing!','the sky','nothing much']
                print(random.choice(stMsgs))
                print('What would you like me to do for you')

            elif "who are you" in query or 'what is your name' in query or 'what are you' in query:
                print("I am Friday, your personal assistant")
                print('what can I do for you')

            elif 'sibling' in query or 'brother' in query or 'sister' in query and 'your' in query:
                print('We are here to talk about you, not me')
                print('What assistance may I be of')

            elif 'good morning' in query or 'good afternoon' in query or 'good evening' in query:
                hour = int(datetime.datetime.now().hour)
                if hour >=0 and hour<12:
                    print('good morning')
                elif hour >=12 and hour <18:
                    print('good afternoon')
                else:
                    print("good evening")

                print('What would you like me to do for you')

            elif 'what can you do' in query:
                print('here are a few thing which I can do')
                print('open websites, launch applications, search the web and communicate with you')
                print('What assistance may I be of')

            elif "the time" in query:
                time = datetime.datetime.now().strftime("%H:%M")
                print("Sir the time is")
                print(time)
                print(time)
                response()

            elif 'the day' in query:
                day = datetime.datetime.now()
                print('today is')
                print(day.strftime("%A"))
                print(day.strftime("%A"))
                response()

            elif 'sleep' in query:
                stMsgs = ['Going to sleep mode.']
                print(random.choice(stMsgs))
                state = 'sleep'

            elif 'quit' in query or 'abort' in query or 'bye' in query or 'stop' in query or 'good night' in query or 'nothing else' in query or 'no need to help me' in query:
                stMsgs = ['Goodbye sir. hope you have a great day.',"until next time",'till we meet again']
                RND = random.choice(stMsgs)
                print(RND)
                print(RND)
                sys.exit()

            elif 'shutdown' in query and 'computer':
                print('shutting down')
                print('shutting down')
                stMsgs = ['Goodbye sir. hope you have a great day.',"until next time"]
                print(random.choice(stMsgs))
                os.system('shutdown -s')
                os.system('TASKKILL /F /IM code.exe')
                sys.exit()

            elif 'restart' in query and 'computer':
                print('restarting...')
                print('restarting')
                stMsgs = ['Goodbye sir. hope you have a great day.',"until next time"]
                print(random.choice(stMsgs))
                os.system('shutdown -r')
                os.system('TASKKILL /F /IM code.exe')
                sys.exit()

            elif 'hello' in query or 'hey' in query:
                stMsgs = ['Hello Sir', 'Hello sir, always at your service']
                print(random.choice(stMsgs))
                print('what assistance may I be of')

            elif "launch chrome" in query or 'launch google chrome' in query:
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                print("Launching chrome")
                os.startfile(chromePath)
                response()

            elif "launch opera" in query:
                operaPath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Opera\\launcher.exe"
                print("Launching opera")
                os.startfile(operaPath)
                response()

            elif "launch notepad" in query:
                notePath = "C:\\Windows\\system32\\notepad.exe"
                print("Launching notepad")
                os.startfile(notePath)
                response()

            elif "launch calculator" in query:
                calcPath = "C:\\Windows\\system32\\calc.exe"
                print("Launching calculator")
                os.startfile(calcPath)
                response()

            elif 'launch powerpoint' in query or 'launch microsoft powerpoint' in query or 'launch ms powerpoint' in query:
                pptpath = 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\POWERPNT'
                print('launching MS powerpoint')
                os.startfile(pptpath)
                response()

            elif 'launch word' in query or 'launch microsoft word' in query or 'launch ms word' in query:
                wordpath = 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\WINWORD'
                print('launching MS word')
                os.startfile(wordpath)
                response()

            elif 'launch paint' in query or 'launch microsoft paint' in query or 'launch ms paint' in query:
                paintpath = 'C:\\Windows\\system32\\mspaint'
                print('launching MS paint')
                os.startfile(paintpath)
                response()

            elif 'launch vlc' in query:
                vlcpath = "C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe"
                print('launching vlc media player')
                os.startfile(vlcpath)
                response()

            elif "youtube" in query and 'search' in query:
                print("searching youtube...")
                print('searching youtube...')
                query = query.replace("youtube search","")
                try:
                    tabURL = "https://www.youtube.com/results?search_query="
                    webbrowser.open(tabURL+query)
                    print('got it')
                    response()
                except:
                    print('unable to connect')
                    response()

            elif 'search' in query and 'google' in query:
                print('searching google...')
                print('searching google...')
                query = query.replace("google ","").replace('search ','')
                tabURL = "http://google.com/?#q="
                webbrowser.open(tabURL+query)
                print('Got it.')
                response()


            elif "search" in query and 'google search' not in query and 'search google' not in query and 'youtube' not in query:
                print("searching...")
                query = query.replace("search","")
                try:
                        try:
                            res = client.query(query)
                            results = next(res.results).text or next(res.results).jpg
                            print('Got it.')
                            print(results)
                            print(results)
                            response()

                        except:
                            results = wikipedia.summary(query, sentences = 2)
                            print('got it')
                            print(results)
                            print(results)
                            response()

                except:
                    print('got it')
                    GoogleSearchResult(query)
                    response()

            else:
                query = query
                ans = ['give me a minute','just a second'] 
                print(random.choice(ans))
                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).text or next(res.results).jpg
                        print('got it')
                        print(results)
                        print(results)
                        response()

                    except:
                        results = wikipedia.summary(query, sentences = 2)
                        print('got it')
                        print(results)
                        print(results)
                        response()

                except:
                    print('got it')
                    GoogleSearchResult(query)
                    response()

        else:
            state = 'sleep'