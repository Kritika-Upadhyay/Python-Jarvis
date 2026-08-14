# 🤖 Jarvis

Jarvis is a Python-based AI voice assistant that can listen to voice commands, perform predefined tasks, and use Google's Gemini AI to answer general questions.

The project combines speech recognition, text-to-speech, web automation, APIs, and AI to create a simple personal voice assistant.

---

## ✨ Features

- 🎙️ Voice-based interaction
- 🔊 Text-to-speech responses
- 🤖 Google Gemini AI integration
- 🌐 Website automation
- 🎵 Music playback
- 📰 News updates using NewsAPI
- 🔁 Continuous command mode
- 😴 Sleep mode
- 🔐 API keys stored using environment variables
- 🛡️ Basic speech-recognition error handling

---

## 🧠 What Can Jarvis Do?

### 🌐 Open Websites

Jarvis can open:

- Google
- Facebook
- YouTube
- Instagram
- LinkedIn
- Spotify

Example:

> "Jarvis, open YouTube."

### 🎵 Play Music

Jarvis can play songs stored in the custom `Music_Library.py` file.

Example:

> "Jarvis, play [song name]."

### 📰 Get News

Jarvis can fetch the latest Indian news headlines using **NewsAPI** and read them aloud.

Example:

> "Jarvis, tell me the news."

### 🤖 Answer Questions with Gemini

If a command doesn't match one of the predefined functions, Jarvis sends it to **Google Gemini** and speaks the generated response.

Example:

> "Jarvis, explain what Python is."

### 🔁 Continuous Commands

After saying **"Jarvis"** once, the assistant remains active and accepts multiple commands without requiring the wake word again.

### 😴 Sleep Mode

Jarvis can return to wake-word detection when the user says:

- sleep
- go to sleep
- go to sleep jarvis
- goodbye
- bye

Example:

> User: Sleep
> Jarvis: Going to Sleep

Jarvis is now waiting for "Jarvis" again.

Example:

```text
User: Jarvis
Jarvis: Yeah

User: Open YouTube
Jarvis: Opens YouTube

User: Open Spotify
Jarvis: Opens Spotify

User: Play a song
Jarvis: Plays the song
```

---

## 📁 Project Structure

```text
Jarvis/
│
├── main.py
├── Client.py
├── Music_Library.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 📄 File Description

| File | Description |
|---|---|
| `main.py` | Main Jarvis program containing voice recognition, commands, Gemini integration, news, and continuous listening. |
| `Client.py` | Used for testing and integrating the Gemini API. |
| `Music_Library.py` | Stores song names and their corresponding links. |
| `requirements.txt` | Contains the Python packages required to run the project. |
| `.env` | Stores API keys such as the Gemini and NewsAPI keys. |
| `.gitignore` | Prevents sensitive and unnecessary files from being committed. |
| `README.md` | Project documentation. |

> **Note:** `.env` and `.venv` should never be uploaded to GitHub.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **SpeechRecognition** | Converts spoken commands into text |
| **SoundDevice** | Records audio from the microphone |
| **Google Gemini API** | Handles AI-powered questions and responses |
| **System.Speech / PowerShell** | Converts text responses into speech |
| **Webbrowser** | Opens websites through voice commands |
| **Requests** | Communicates with NewsAPI |
| **NewsAPI** | Provides news headlines |
| **python-dotenv** | Loads API keys from the `.env` file |
| **Git & GitHub** | Version control and project management |

---

## ⚙️ How Jarvis Works

1. 🎙️ **Listens for the wake word**  
   Jarvis continuously listens through the microphone and waits for the user to say **"Jarvis"**.

2. 🔊 **Activates**  
   Once the wake word is recognized, Jarvis responds with **"Yeah"** and enters active mode.

3. 🗣️ **Recognizes the command**  
   Jarvis listens to the user's command and converts the speech into text using `SpeechRecognition`.

4. ⚙️ **Processes the command**  
   The command is checked against predefined actions such as opening websites, playing music, fetching news, or entering sleep mode.

5. 🤖 **Uses Gemini when needed**  
   If the command doesn't match a predefined action, it is sent to the **Google Gemini API** for an AI-generated response.

6. 🗣️ **Speaks the response**  
   Jarvis converts the response into speech using Windows `System.Speech`.

7. 🔁 **Continues listening**  
   After completing a command, Jarvis remains active and waits for another command without requiring the user to say **"Jarvis"** again.

8. 😴 **Returns to standby**  
   When the user says **"sleep"**, **"go to sleep"**, **"go to sleep jarvis"**, **"goodbye"**, or **"bye"**, Jarvis leaves active mode and starts waiting for the wake word again.
