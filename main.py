from dotenv import load_dotenv
import os

import speech_recognition as sr
import webbrowser 
import subprocess
import sounddevice as sd
import Music_Library
import requests

load_dotenv()

openai_api_key = os.getenv("OpenAI_API_KEY")
news_api_key = os.getenv("News_API_KEY")

recognizer = sr.Recognizer()

def speak(text):
    powershell_command = f'''
    Add-Type -AssemblyName System.Speech
    $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $speak.Speak("{text}")
    '''

    subprocess.run(
        ["powershell", "-Command", powershell_command],
         capture_output=True 
    )

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")

    elif c.lower().startswith("play"):
        song = c.lower()[5:].strip()
        link = Music_Library.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}")

        print("News API status: ", r.status_code)
        
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])
            if articles:
                # Read the headlines
                for article in articles:
                    speak(article['title'])

            else:
                speak("Sorry, I couldn't find any news right now.")

    else:
        # Let OpenAI handle the request
        pass

def listen():
    sample_rate = 16000
    duration = 5
            
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate = sample_rate,
        channels = 1,
        dtype = "int16"
    )
            
    sd.wait()
            
    return sr.AudioData(
        recording.tobytes(),
        sample_rate,
        2
    )

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True: 
        print("Recognizing...")

        try:
            
            # Listen for wake word
            audio = listen()
            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                print(word)
                speak("Yeah")

                # Listen for command
                print("Jarvis Active...")

                audio = listen()
                command = recognizer.recognize_google(audio)
                print(command)

                processCommand(command)

        except Exception as e:
            print(f"Error; {e}")
