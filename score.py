import requests
from bs4 import BeautifulSoup
from time import sleep
import pyttsx3
import speech_recognition as sr
import ctypes
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"

url ="https://static.cricinfo.com/rss/livescores.xml"
while url:
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    data= soup.find_all("description")
    score = data[1].text
    print(score)
    speak(score)
    break
