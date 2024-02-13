import pyttsx3
import datetime
import os
from gtts import gTTS

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis! Sir, Please tell me how may I help you")

def take_command():
    query = input("Enter your command: ").lower()
    return query

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            # code for searching Wikipedia and speaking the result
            
        elif 'open youtube' in query:
            # code for opening YouTube
            
        elif 'open google' in query:
            # code for opening Google
            
        elif 'the time' in query:
            # code for telling the time
            
        elif 'quit' in query:
            speak("Goodbye Sir! Jarvis signing off.")
            break

        # Add more elif conditions for additional functionalities

        else:
            speak("Sorry Sir, I didn't get that. Can you please repeat?")


