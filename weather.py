
# Python program to find current 
# weather details of any city
# using openweathermap api
  
# import required modules
import requests, json
import pyttsx3
import shutil
import ctypes
import speech_recognition as sr
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
  
# Enter your API key here
api_key = ""
  
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name
speak("city name")
print("city name :")
city_name = takeCommand()
  
# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + str(city_name)
  
# get method of requests module
# return response object
response = requests.get(complete_url)
  
# json method of response object 
# convert json format data into
# python format data
x = response.json()
  
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
  
    # store the value of "main"
    # key in variable y
    y = x["main"]
  
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
  
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
  
    # store the value corresponding
    # to the "humidity" key of y
    current_humidiy = y["humidity"]
  
    # store the value of "weather"
    # key in variable z
    z = x["weather"]
  
    # store the value corresponding 
    # to the "description" key at 
    # the 0th index of z
    weather_description = z[0]["description"]
  
    # print following values
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description))
  
else:
    print(" City Not Found ")


