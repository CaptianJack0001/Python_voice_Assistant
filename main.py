import speech_recognition as sr
import datetime
import os
import webbrowser
import openai
from config import apikey
import json
import requests
import pyttsx3
import time
import numpy as np
import win32com.client
import random

# speaker= win32com.client.Dispatch("SAPI.SpVoice")
#
# while 1:
#      print("1.Chat with Jarvis")
#      s= input()
#      speaker.speak(s)
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
chat =""                  # this we defined as o initially

def chat(query):
    global chatStr
    #print(chatStr)
    openai.api_key = apikey
    chatStr+= f"Harry:{query}\n Jarvis: "    # this stores the chat histrory
    response = openai.Completion.create(
        model="text-davinci-002",   # this is the open ai model
        prompt= chatStr,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
   )



    say(response["choices"][0]["text"])              # this is the response from open ai.....choice 0 means
             # the first choice here
    chatStr+=f"response['choices'][0]['text']\n"       #here it stores the response in chatSt
    return(response["choices"][0]["text"])  # ye written me aara he     #now it return the ans in console


        #write a program to generate api key







def ai(prompt):
  try:
    # line me dekho niche prompt= prompt he toh ye pass hora jha ab hum question passs krege as prompt
    openai.api_key = apikey        # here we store the api
    text=f"Open Ai response for prompt : {prompt}"     # this is the text that we want to print
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt= prompt,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
   )

    generated_text = response["choices"][0]["text"]
    print(generated_text)
    text += generated_text
        # we store the response in text
    # todo: wrap it inside a try and catch as sometimes choices ni hoti

    # idhr response[0] kra cz response [0] text ko direct krta he and ye mujhe
    # pta lga he code dekh kr CWH ka.
    if not os.path.exists("Openai"):  # agr openai krke path in he toh means
        os.mkdir("Openai")             # toh create krdo vo kha he
    with open(f"Openai/{''.prompt.split('intelligence')[1:]}.txt","w") as  f:
        f.write(text)

  except Exception as e:
        print(f"An error occurred: {str(e)}")

def say(text):             # jo upr text hua submit vo ab bol rha jarvis..
    os.system(f' say"{text}" ')  # this allows to take command
def check_weather(location):
    # Make a GET request to a weather API (such as OpenWeatherMap)
    api_key = "7261a60a99fd13b9a71ced0810818f5c"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)

    if 'main' in data:
        # Extract relevant weather information from the response
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        # Say the weather information to the user using the say() function
        say(f"The current weather in {location} is {description}. The temperature is {temperature} Kelvin, and the humidity is {humidity}%.")
    else:
        # Handle the case when the required weather information is not available
        say("Sorry, I couldn't retrieve the weather information for the specified location.")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:  # source of info is microphone
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
          query = r.recognize_google(audio, language="en-in")
          print("User said : {query")
          return query
        except Exception as e:
          return "Some errors occured. Sorry from ai"




if __name__ == '__main__':
    print('PyCharm')
    say("hello i am jarvis ai")
    while True:
        print("Listening. . . ")
        query = takeCommand()
        # ye niche humne array bna diya , ky ky store kr skte he hum isme
        sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"],]
        #
        for site in sites:
        # jo mu se bolunga co text ke through return
        #say(query)
          if f"Open {site[0]}".lower() in query.lower():
            say("opening {site[0]} sir")
            webbrowser.open(site[1])
          elif "open music " in query:     #yha tum music play kroge like bolo open music and ye play hoga and path diya hua he
              musicpath = "/users/music/bewafa.mp3"
              os.system(f"open {musicpath}")

          elif "the time " in query:             #ye jese upr open music kra vese hi niche time dekhne ke liye kra ye se
              #aap ab time ko hindi me bhi bula skte ->   say(f"bdka time tuhada hua he {strfTime}")
              #isme dekho optimize kr skte ye main baat he smjhe

              strfTime= datetime.datetime.now().strftime("%H:%M:%S")
              say(f"sir the time is {strfTime}")


          elif "open facetime".lower() in query.lower():
              os.system(f"open/system/application/Facetime.app")


          elif "open spotify".lower() in query.lower():   # yha humne spotify app open kra jese website open kr rhe the vese hi ek app open kra humne abhiiii!!!

               os.system(f"open/system/application/spotify.app")

          elif "Using artificial intelligence".lower() in query.lower():
               ai(prompt=query)
          elif "check weather" in query:
            # Extract the location from the query
            location = query.replace("check weather", "").strip()
            check_weather(location)

          elif "Jarwis.Quit".lower() in query.lower():
              say("bye sir")
              exit()

          elif "reset chat".lower() in query.lower():
               chatstr=""

          elif "tell me a joke" in query:
            say("Why don't scientists trust atoms? Because they make up everything!")
          elif "search" in query:
            search_query = query.replace("search", "").strip()
            search_url = f"https://www.google.com/search?q={search_query}"
            say(f"Searching for {search_query}")
            webbrowser.open(search_url)  # Open search results page in a new browser wind

          else:
              print("chatting ....")
              chat(query)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
