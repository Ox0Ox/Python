import threading
from datetime import datetime
import pyttsx3
import utils
from utils.alarm_utils.alarm_timing import AlarmTiming

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
        engine.say(audio)
        engine.runAndWait()

class Alarm(threading.Thread):
    def __init__(self, voice_input, response):
        threading.Thread.__init__(self)
        self.input = voice_input
        #self.response = response


    def run(self):
        new = AlarmTiming(self.input).get_expected_time()
        if new:
            new = datetime.strptime(new, "%Y-%m-%d %H:%M:00")
            print('Current time is : ' + str(datetime.now()))
            if datetime.now() > new:
                speak('Alarm time is greater than current time sir.')
            else:
                while True:
                    now = datetime.now().strftime('%Y-%m-%d %H:%M:00')
                    now = datetime.strptime(now, "%Y-%m-%d %H:%M:00")
                    if now == new:
                        speak('Ding Dong, Ding Dong, Ding Dong, Ding Dong, Ding Dong, Ding Dong, Ding Dong, Ding Dong, Ding Dong, Ding Dong')
                        break
