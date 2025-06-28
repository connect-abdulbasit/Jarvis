import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import requests
import wikipedia
import sys
import os
from dotenv import load_dotenv
# Initialize modules
engine = pyttsx3.init()
recognizer = sr.Recognizer()
wikipedia.set_lang("en")

# Speak function
def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

# Get weather
def get_weather(city="Karachi"):
    try:
        api_key = os.getenv('OPENWEATHER_API_KEY')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        res = requests.get(url).json()
        if res["cod"] == 200:
            temp = res["main"]["temp"]
            desc = res["weather"][0]["description"]
            speak(f"The weather in {city} is {desc} with a temperature of {temp}°C.")
        else:
            speak("Sorry, I couldn't find the weather for that city.")
    except Exception as e:
        speak("Error fetching weather.")
        print("Weather Error:", e)

# Time and date
def tell_time():
    now = datetime.datetime.now()
    speak(f"The current time is {now.strftime('%I:%M %p')}")

def tell_date():
    now = datetime.datetime.now()
    speak(f"Today is {now.strftime('%A, %B %d, %Y')}")

# Wikipedia lookup
def answer_query(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)
    except:
        speak("Sorry, I couldn't find information on that.")

# Perform task based on voice command
def performTask(c):
    c = c.lower()
    print("Command:", c)

    if "youtube" in c:
        webbrowser.open("https://www.youtube.com")
    elif "facebook" in c:
        webbrowser.open("https://www.facebook.com")
    elif "google" in c:
        webbrowser.open("https://www.google.com")
    elif "linkedin" in c:
        webbrowser.open("https://www.linkedin.com")
    elif "github" in c:
        webbrowser.open("https://www.github.com")
    elif "netflix" in c:
        webbrowser.open("https://www.netflix.com")
    elif "play millionaire" in c:
        webbrowser.open("https://www.youtube.com/watch?v=XO8wew38VM8&list=RDXO8wew38VM8&start_radio=1")
    elif "time" in c:
        tell_time()
    elif "date" in c:
        tell_date()
    elif "weather" in c:
        city = c.split("in")[-1].strip() if "in" in c else "Karachi"
        get_weather(city)
    elif "search" in c:
        query = c.replace("search", "").strip()
        if query:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            speak(f"Searching Google for {query}")
        else:
            speak("What should I search?")
    elif "who is" in c or "what is" in c:
        answer_query(c)
    else:
        speak("Sorry, I don't understand that command.")
        return -1
    return 0

# Listen from microphone
def listen_command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            print("No command detected.")
        except sr.UnknownValueError:
            print("Could not understand.")
        except sr.RequestError:
            print("Speech recognition service error.")

# Handle active mode
def jarvisActivate():
    while True:
        command = listen_command()
        if command:
            command = command.lower()

            print(command)
            if "sleep" in command:
                speak("Going to sleep. Say 'Jarvis' to wake me up.")
                break
            elif "shutdown" in command or "exit" in command or "quit" in command:
                speak("Shutting down. Goodbye!")
                sys.exit(0)

            # Perform tasks
            performTask(command)

# Wake loop
speak("Initializing JARVIS...")
while True:
    command = listen_command()
    if command and "jarvis" in command.lower():
        speak("Jarvis Activated")
        jarvisActivate()
