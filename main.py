import speech_recognition as sr
import webbrowser 
import pyttsx3
import sounddevice as sd

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
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
        print("Listening...")

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
        

# try:
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source, timeout=2, phrase_time_limit=1)
#     word = r.recognize_google(audio)
#     if(word.lower() == "jarvis"):
#         speak("Yeah")
#         # Listen for command
#         with sr.Microphone() as source:
#             print("Jarvis Active...")
#             audio = r.listen(source)
#             command = r.recognize_google(audio)

#             processCommand()