import speech_recognition as sr
import webbrowser 
import subprocess
import sounddevice as sd
import Music_Library

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
