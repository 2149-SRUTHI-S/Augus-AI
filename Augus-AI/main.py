# AUGUS AI - AI Based Desktop Assistant for Blind 
# By Sruthi Sivasankararaj   
  
import speech_recognition as sr
import os
import pyttsx3

import webbrowser
import openai
import datetime

import wikipedia
import pyjokes
import pywhatkit


def say(text):
    os.system(f"say {text}")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=0.6
        audio=r.listen(source)

        try:
            print("Recognizing")
            query=r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred,Sorry from Augus"
            
def run_jarvis(q):
    
    if 'play' in q:
        song=q.replace('play',' ')
        print(song)
        engine = pyttsx3.init()
        engine.say('playing '+song)
        pywhatkit.playonyt(song)

if __name__=='__main__':

    engine = pyttsx3.init()
    engine.say("Hello I am Augus AI!! How can I help you")
    print("Hello I am Augus AI")

    engine.runAndWait()
    while True:
        print("Listening.....")
        
        query=takeCommand()
        
        engine = pyttsx3.init()
        engine.say(query)
        engine.runAndWait()
        
        sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],
               ["Google","https://www.google.com"],["SkillRack","https://www.skillrack.com"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                engine = pyttsx3.init()
                engine.say(f"Opening {site[0]} mam....")
                engine.runAndWait()
                webbrowser.open(site[1])

        if "the time" in query:
            
            time=datetime.datetime.now().strftime('%I:%M %p')
            hour=datetime.datetime.now().strftime("%I")
            min=datetime.datetime.now().strftime("%M")
            print(time)
            
            engine = pyttsx3.init()
            engine.say(f"The Time is{hour} hours {min} minutes")
            engine.runAndWait()
            
        if  'who is' in query or 'tell me' in query:

            person=query.replace('who is','')
            person = query.replace('tell me', '')

            info=wikipedia.summary(person,1)
            print(info)
            engine = pyttsx3.init()
            engine.say(info)
            engine.runAndWait()

        if "play" in query:
            run_jarvis(query)
        if "How are you".lower() in query.lower():
            engine = pyttsx3.init()
            engine.say("I am fine,thank you Mam what about you")
            print("I am fine,thank you Mam  what about you")

            engine.runAndWait()
        if "I am good".lower() in query.lower():
            engine = pyttsx3.init()
            engine.say("Awesome Mam")
            print("Awesome Mam")

            engine.runAndWait()
        if "Bye".lower() in query.lower():
            engine = pyttsx3.init()
            engine.say("Bye! Pleasure talking to you...,have a great day....")
            print("Bye! Pleasure talking to you...,have a great day....")

            engine.runAndWait()

        if "developed".lower() in query.lower():
            engine = pyttsx3.init()
            engine.say("I am developed by Sruthi, Shrilakshmi, Yuthika")
            print("I am developed by Sruthi, Shrilakshmi, Yuthika")

            engine.runAndWait()
