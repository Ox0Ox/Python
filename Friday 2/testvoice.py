# Python program to show
# how to convert text to speech
import pyttsx3
  
# Initialize the converter
converter = pyttsx3.init()

voices = converter.getProperty('voices')

#converter.setProperty('rate', 180)

converter.setProperty('volume', 2.5)

converter.setProperty('voice', voices[1].id)
  
converter.say("Hello, My name is Jarvis.")
converter.say("How may I help?")
converter.runAndWait()
'''
i = -1
for voice in voices:
    i = i+1
    # to get the info. about various voices in our PC
    print('Index:',i) 
    print("Voice:")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages)
    print('')
    '''