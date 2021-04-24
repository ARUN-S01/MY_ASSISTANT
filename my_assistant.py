#CODE WRITTEN BY (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ (ARUN) (u‿ฺu✿ฺ)



import subprocess
import wolframalpha
import pyttsx3
import turtle
import tkinter
import cv2
from turtle import *
import datetime
import winsound
from win10toast import ToastNotifier
import psutil
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import google
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import datetime
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning  !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon  !")  
  
    else:
        speak("Good Evening !") 
  
    assname =("VERONICA")
    speak("I am your personal voice Assistant" + assname)
     
 
def usrname():
    speak("What should i call you ")
    uname = takeCommand()
    if uname == "Arun":
        speak("hello boss")
        print("hello boss")
        speak("Welcome, i am glad that you are here")
        speak("how can i help you")
    elif uname != "Arun":
        speak("welcome,glad to meet you " + uname)
        print("Welcome,Glad to meet you " + uname)
        speak("How can i Help you")
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
     
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('your email id', 'your email passowrd')
    server.sendmail('your email id', to, content)
    server.close()

if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    usrname()
    while True:
         
        query = takeCommand().lower()
         
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif "what's your name" in query or "What should I call you" in query:
            speak("My friends call me" + assname)
            print("My friends call me" + assname)
 

 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
 
        elif 'open amazon' in query:
            speak("Here you go to amazon,happy shopping")
            webbrowser.open("amazon.in")  
 
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            try :
                music_dir = webbrowser.open("https://wynk.in/music")
            except:  
                random = os.startfile(os.path.join(music_dir, songs[1]))
 
        elif 'time please' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f", the time is {strTime}")
            print(strTime)
 
        elif 'open chrome' in query:
            codePath = r"C:\Program Files\Google\Chrome\Application"
            os.startfile(codePath)
 
        elif 'email to ARUN' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver email address"   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you")

        elif 'translate' in query:
            speak('ok')
            import tran
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            uname = query
 
        elif "change name" in query:
            speak("What would you like to call me")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What should I call you" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me" + assname)
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by ARUN.")
             
        elif 'tell a joke' in query:
            speak(pyjokes.get_joke())
            
        elif 'draw indian flag' in query:
            speak("ok")
            import flag
            
 
             
        elif "calculate" in query:
             
            app_id =  "your api id" 
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
 
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search","")
            query = query.replace("play","")         
            webbrowser.open(query)
        elif 'battery percentage' in query:
            battery = psutil.sensors_battery()
            percent = str(battery.percent)
            speak("your device is running at " +percent + "% battery")
            print("your device running at " +percent + "% Battery")
 
        elif "who am i" in query:
            speak("If you talk then definately your human.")
 
        elif "why you came to this world" in query:
            speak("Thanks to ARUN. further It's a secret")
 
        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\a2r0u\\Desktop\\ANIMATRONICS - Shortcut.lnkPresentation\\Voice Assistant.pptx"
            os.startfile(power)
 
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by ARUN")
        
        elif 'tic tac toe game' in query:
            speak("sure")
            import tictactoegame
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by ARUN ")
 
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed succesfully")
 
 
        elif 'news' in query or 'play news' in query:
             
            try:
                jsonObj = urlopen('https://timesofindia.indiatimes.com/')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
 
         
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
        elif 'set an alarm' in query:
            timing = input('Time Please :')

            message = input("enter your message :")

            while message:
                  current_time=datetime.datetime.now()
                  alarm_time = str(current_time.hour)+":"+str(current_time.minute)

                  if alarm_time == timing:
                      notification = ToastNotifier()
                      winsound.Beep(frequency=2500,duration=1000)
                      notification.show_toast("alarm",message,duration=50)
                      break

        
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                os.system("shutdown  /s /t 1")
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want me to stop from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        elif 'tell me the cricket scores' in query:
            speak("ok")
            import score
                 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate" + location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
 
        elif "camera" in query or "take a photo" in query:
            camera = cv2.VideoCapture(0)
            for i in range(1):
                return_value, image = camera.read()
                cv2.imwrite('opencv'+str(i)+'.png', image)
            del(camera)
           
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            subprocess.call(["shutdown", "/l"])
 
        elif "write a note" in query:
            speak("What should i write")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak(" Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("notes.txt", "r")
            print(file.read())
            speak(file.read(6))
 
        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream = True)
             
            with open("Voice.py", "wb") as Pypdf:
                 
                total_length = int(r.headers.get('content-length'))
                 
                for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                    if ch:
                      Pypdf.write(ch)
                     
        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "veronica" in query:
             
            wishMe()
            speak("i am at your service")
 
        elif "show me weather" in query:
            speak("sure")
            import weather
           
             
        elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = ''
                auth_token = ''
                client = Client(account_sid, auth_token)
 
                message = client.messages \
                                .create(
                                    body = takeCommand(),
                                    from_='+918122230060',
                                    to ='Receiver No'
                                )
 
                print(message.sid)
 
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
       
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you ")
            speak(assname)
 
        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
 
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
 
        elif "i love you" in query:
            speak("It's hard to understand")
 
        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client("same api key")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
 
        # elif "" in query:
            # Command go here
