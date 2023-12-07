import requests
import pyttsx3
import json

engine = pyttsx3.init()
engine.setProperty('rate', 170)

city = input("Enter the city name : ")
url = f"http://api.weatherapi.com/v1/current.json?key=5f9b5fd4e5344727a54195420230711&q={city}&aqi=yes"
req = requests.get(url)

dict = json.loads(req.text)

temp = dict["current"]["temp_c"]
engine.say(f"The temperation of {city} is {temp} in celcius")
engine.runAndWait()


