# 🎙️ Voice Assistant

A Python-based Voice Assistant that listens to voice commands, performs useful tasks, and responds using text-to-speech. The assistant can answer greetings, tell the time and date, perform web searches, fetch weather information, send emails, set reminders, and more.

---

## 📌 Objective

Develop a Python-based voice assistant that recognizes speech, processes user commands, and performs various real-world tasks using speech recognition, text-to-speech, and external APIs.

---

## 🚀 Features

### ✅ Beginner Features
- 🎤 Voice input using SpeechRecognition
- 👋 Responds to greetings
- 🕒 Tells current date and time
- 🌐 Performs web searches
- 🔊 Text-to-speech responses
- ❌ Graceful error handling for unrecognized speech

### ⭐ Advanced Features
- 🧠 Natural language command recognition
- 📧 Send emails using voice commands
- ⏰ Set reminders with audible alerts
- 🌦 Live weather updates using OpenWeatherMap API
- ❓ Answer general knowledge questions
- ⚙️ Support for custom voice commands
- 🔒 Privacy documentation

---

## 🛠️ Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- PyAudio
- Requests
- smtplib
- datetime
- webbrowser
- OpenWeatherMap API

---

## 📂 Project Structure

```
TASK-1-VOICE-ASSISTANT/
│── main.py
│── commands.py
│── config.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ▶️ Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Move into the project folder

```bash
cd TASK-1-VOICE-ASSISTANT
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the project

```bash
python main.py
```

---

## 🔒 Privacy

This project processes voice input locally using the SpeechRecognition library. Weather requests are sent to the OpenWeatherMap API only when requested by the user. No personal voice recordings are stored permanently.

---

## 👨‍💻 Author

**Anil Kumar Senapati**
Computer Science Engineering Student  
C.V. Raman Global University