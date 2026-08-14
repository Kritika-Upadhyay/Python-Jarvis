# 🤖 Jarvis

Jarvis is a Python-based AI voice assistant that can listen to voice commands, perform predefined tasks, and use Google's Gemini AI to answer general questions.

The project combines speech recognition, text-to-speech, web automation, APIs, and AI to create a simple personal voice assistant.

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
