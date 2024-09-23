from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import time as tm


flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")

def display_time():
    current_time = tm.strftime('%H:%M:%p')
    current_time.after(5000,display_time)

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()
    
    def STT(self):
   
   
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

    def JARVIS(self):
        wish()
        while True:
            query = self.STT()
            query = query.lower()
            if 'bye' in query:
                sys.exit()
            elif 'open google' in query:
                webbrowser.open('www.google.com')
                speak("opening google")
            elif 'open youtube' in query:
                webbrowser.open("www.youtube.com")











FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"C:\HARSH PATNAIK\Python\GUI Trial\Interface.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,575)
        self.label_7 = QLabel
        self.Exit = QPushButton
        ##self.Exit.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        ##self.label_4.setMovie(self.label_7)
        ##self.label_7.start()

        #self.ts = time.strftime("%A, %d %B")
        self.time = display_time()

        Dspeak.start()
        self.label_9.setText("<font size=8 color='aqua'>"+self.ts+"</font>")
        self.label_9.setFont(QFont(QFont('Comic Sans MS',6)))
        self.label_10.setText("<font size=8 color='aqua'>"+self.time+"</font>")
        self.label_10.setFont(QFont(QFont('Comic Sans MS',6)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())