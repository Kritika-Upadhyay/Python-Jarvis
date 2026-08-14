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

```text
User says "Jarvis"
        ↓
Jarvis detects the wake word
        ↓
Jarvis activates and says "Yeah"
        ↓
Listens for the user's command
        ↓
Converts speech → text
        ↓
Checks the command
        ↓
 ┌───────────────────────────────┐
 │                               │
Predefined command          Other question
 │                               │
 ↓                               ↓
Open website /             Send to Gemini AI
Play music / News /              │
Sleep                             ↓
 │                         Generate response
 │                               │
 └───────────────┬───────────────┘
                 ↓
          Jarvis speaks response
                 ↓
       Continues listening for
          another command
                 ↓
        User says "Sleep"
                 ↓
       Returns to wake-word mode
```

### 🎙️ Voice Recognition

Jarvis uses `sounddevice` to record audio from the microphone and `SpeechRecognition` to convert the recorded speech into text.

The assistant listens for the wake word **"Jarvis"** and, once activated, can continuously listen for multiple commands without requiring the wake word again.

### 🗣️ Text-to-Speech

Jarvis uses the Windows `System.Speech` engine through PowerShell to convert text into spoken responses.

This allows Jarvis to speak AI responses, confirmations, and news headlines without requiring an additional text-to-speech service.

### 🤖 Gemini Integration

Jarvis uses the **Google Gemini API** to handle general questions and commands that are not covered by the predefined functions.

The user's command is sent to Gemini, the generated response is received by Jarvis, and the response is then converted into speech.

Gemini is instructed to avoid Markdown, headings, bullet points, and code blocks because its responses are meant to be spoken aloud.

### 🔐 API Keys & Security

Jarvis requires API keys for **Google Gemini** and **NewsAPI**.

The keys are stored in a `.env` file instead of being written directly into the Python source code.

The `.env` file is included in `.gitignore` so that the API keys are not accidentally uploaded to GitHub.

```text
Gemini_API_KEY=your_gemini_api_key
News_API_KEY=your_news_api_key
```

> **Never share or commit your actual API keys.**

### 🐍 Virtual Environment

The project was developed using a Python virtual environment named `.venv`.

A virtual environment keeps the project's Python packages isolated from the system-wide Python installation and helps prevent dependency conflicts.

### 📦 Requirements

The project includes a `requirements.txt` file containing the Python packages required to run Jarvis.

After creating and activating a virtual environment, the required dependencies can be installed using:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd Jarvis
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create the `.env` File

Create a file named `.env` in the project directory and add your own API keys:

```text
Gemini_API_KEY=your_gemini_api_key
News_API_KEY=your_news_api_key
```

> **Never share or upload your `.env` file or API keys to GitHub.**

### 6. Run Jarvis

```bash
python main.py
```

Jarvis will initialize and start listening for the wake word:

```text
Jarvis
```

After activation, you can give multiple commands without repeating the wake word.

### 📌 Requirements

- Python 3.x
- Working microphone
- Internet connection
- Google Gemini API key
- NewsAPI key
- Windows OS (required for the current `System.Speech` text-to-speech implementation)

---

## 💬 Example Interaction

```text
Jarvis: Initializing Jarvis...

User: Jarvis
Jarvis: Yeah

User: Open YouTube
Jarvis: [Opens YouTube]

User: Open Spotify
Jarvis: [Opens Spotify]

User: What is Python?
Jarvis: Python is a high-level, general-purpose programming language known
for its simplicity, readability, and versatility.

User: Tell me the latest news
Jarvis: [Reads the latest available headlines]

User: Sleep
Jarvis: Going to Sleep...
```

The continuous listening feature allows multiple commands to be given after activating Jarvis, without requiring the wake word before every command.

---

