import speech_recognition as sr
import webbrowser 
import pyttsx3
import sounddevice as sd

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True: 
        print("Listening...")

        # Record audio from microphone
        sample_rate = 16000
        duration = 5

        recording = sd.rec(
            int(duration * sample_rate),
            samplerate = sample_rate,
            channels = 1,
            dtype = "int16"
        )

        sd.wait()

        # Convert recording to SpeechRecognition AudioData
        audio = sr.AudioData(
            recording.tobytes(),
            sample_rate,
            2
        )

        print("Recognizing...")

        try:
            text = recognizer.recognize_google(audio)
            print("Google thinks you said: " + text)

        except sr.UnknownValueError:
            print("Google could not understand audio")

        except sr.RequestError as e:
            print(f"Google error; {e}")
        