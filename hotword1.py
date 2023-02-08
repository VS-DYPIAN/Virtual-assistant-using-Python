import os
import pyttsx3
import sys
import speech_recognition as sr


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',170)

def speak(audio):
    Assistant.say(audio)
    print(f":{audio}")
    Assistant.runAndWait()

def startup():
    speak("Initializing DYPIAN")
    

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        command.pause_threshold = 1
        audio = command.listen(source,0,5)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language='en-in')
            print(f"you said : {query}")

        except Exception as Error:
            return "none"
        query =str(query)
        return query.lower()

while(True) :
    wake_up =takecommand()
    if "wake up" in wake_up:
        startup()
        os.startfile("C:\\FOURTH SEMSTER\\JARVIS\\JARVIS AI\\Final_dypian.py")
    elif "sleep" in wake_up:
        speak("goodbye")
        sys.exit
    
    else:
        print("hotword Detection")