import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr 
import wikipedia
import datetime
import wolframalpha
import os
import sys
#from google import google
from ctypes import windll
import string

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('AJ64YW-WRV7GL89KX')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def GetDrives():
    drives = []
    value = windll.kernel32.GetLogicalDrives()
    for char in string.ascii_uppercase:
        if value & 1:
            drives.append(char)
        value>>=1
    return drives

file_system_dict = {}
def find():
    drives = GetDrives()

    for drive in drives:
        for root, dirs, files in os.walk(drive + ':\\HARSH PATNAIK\\'):
            for f in files:
                key = os.path.join(root, f).rsplit('\\')[-1]
                file_system_dict.update({key: os.path.join(root, f)})

            for dir in dirs:
                key = os.path.join(root, dir).rsplit('\\')[-1]
                file_system_dict.update({key: os.path.join(root, dir)})
    
    return file_system_dict

print(find())

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
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command:'))

    return query

def GoogleSearchResult(query):
    try:    
        searchResult = google.search(query)
        for result in searchResult:
            print(result.description.replace('...','').rsplit('.',3))
            speak(result.description.replace('...','').rsplit('.',3))
            break
    except:
        tabURL = "http://google.com/?#q="
        webbrowser.open(tabURL+query)
        speak('Got it.')




if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()
        
        if 'open' in query and 'open folder' not in query:
            query = query.replace('open ','')
            speak('opening'+query)
            anyURL = 'www.'+query+'.com'
            webbrowser.open(anyURL)

        elif 'open folder' in query:
            try:
                speak('opening'+query)
                os.system('explorer C:\\"{}"'.format(query.replace('open folder ','')))
            except:
                speak('Folder not found')

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            print(results)
            speak("According to wikipedia")
            speak(results)

        elif 'how are you' in query:
            stMsgs = [ 'I am fine', 'i was wondering the same thing', 'I am full of energy', 'i am feeling energetic and im ready to comply!']
            speak(random.choice(stMsgs))
            speak('How are you?')
            userans = myCommand()
            if 'fine' in userans or 'happy' in userans or 'okay' in userans:
                speak('Thats Great')  
            elif 'not' in userans or 'sad' in userans or 'upset' in userans:
                speak('sorry')

        elif "what\'s up" in query:
            stMsgs = ['Just doing my thing!','the sky','nothing much']
            speak(random.choice(stMsgs))

        elif "who are you" in query or 'what is your name' in query or 'what are you' in query:
            speak("I am Friday, your personal assistant")

        elif 'sibling' in query or 'brother' in query or 'sister' in query:
            speak('We are here to talk about you, not me')

        elif 'good morning' in query or 'good afternoon' in query or 'good evening' in query:
            hour = int(datetime.datetime.now().hour)
            if hour >=0 and hour<12:
                speak('good morning')
            elif hour >=12 and hour <18:
                speak('good afternoon')
            else:
                speak("good evening") 

        elif 'what can you do' in query:
            speak('here are a few thing which i can do')
            speak('open websites, launch applications, search the web and communicate with you')

        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the time is")
            speak(time)

        elif 'quit' in query or 'bye' in query or 'stop' in query or 'good night' in query:
            stMsgs = ['Bye Sir, have a good day.',"until next time"]
            speak(random.choice(stMsgs))
            sys.exit()
           
        elif 'hello' in query or 'hi' in query:
            stMsgs = ['Hello Sir', 'Hello sir, always at your service']
            speak(random.choice(stMsgs))

        elif "launch chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            speak("Launching chrome")
            os.startfile(chromePath)

        elif "youtube search" in query:
            speak("searching youtube...")
            query = query.replace("youtube search","")
            try:
                tabURL = "https://www.youtube.com/results?search_query="
                webbrowser.open(tabURL+query)
                speak('got it')
            except:
                speak('unable to connect')

        elif "search" in query:
            speak("searching google...")
            query = query.replace("search","")
            try:
                GoogleSearchResult(query)
            except:
                speak('unable to connect')

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text or next(res.results).jpg
                    speak('Got it.')
                    print(results)
                    speak(results)
                    
                except:
                    GoogleSearchResult(query)
       
            except:
                speak('unable to connect')
        
        speak('Next Command')