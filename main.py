import speech_recognition as sr
import webbrowser 
import pyttsx3
import sounddevice as sd
from faster_whisper import WhisperModel

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Load the Whisper model
model = WhisperModel("base", device="cpu", computer_type="int8")

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

        print("Recognizing...")

        # Save the recording temporarily as WAV
        import wave

        with wave.open("temp_audio.wav", "wb") as audio_file:
            audio_file.setnchannels(1)
            audio_file.setsampwidth(2)
            audio_file.setframerate(sample_rate)
            audio_file.writeframes(recording.tobytes())

        # Recognize speech using Faster-Whisper
        segments, info = model.transcribe("temp_audio.wav")

        text = ""

        for segment in segments:
            text += segment.text

        text = text.strip()

        if text:
            print("You said: ", text)
        else:
            print("Could not understand audio")
        