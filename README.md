# Kalki AI Virtual Assistant

A lightweight, voice-activated desktop AI assistant built with Python. Kalki listens for a wake word, processes speech-to-text commands, automates desktop web browsing and news fetching, and routes conversational queries through the Groq API (powered by open-weight LLMs).

---

## Features

* **Two-Stage Speech Loop:** Constantly listens for the wake word "Kalki" before activating full command mode.
* **Text-to-Speech (TTS):** Provides verbal responses using pyttsx3.
* **Automated Web Navigation:** Voice commands to open Google, YouTube, Cricbuzz, and custom websites.
* **Automated Music Player:** Opens music streams based on user input.
* **Live News Headlines:** Fetches current top news headlines from the NewsAPI REST endpoint and reads them aloud.
* **LLM Integration:** Directs open-ended queries to the Groq API for rapid, concise speech-ready replies.

---

## Tech Stack & Libraries

* **Language:** Python 3.x
* **Speech Recognition:** speech_recognition (Google Speech Recognition API)
* **Text-to-Speech:** pyttsx3
* **API Engine:** groq (LLM completion engine)
* **HTTP Client:** requests (for REST API communication)
* **Web Automation:** webbrowser

---

## Quickstart Guide

```bash
# 1. Clone the repository
git clone [https://github.com/akhileshshetti2/Kalki-AI-Virtual-Assistant.git](https://github.com/akhileshshetti2/Kalki-AI-Virtual-Assistant.git)
cd Kalki-AI-Virtual-Assistant

# 2. Install dependencies
pip install speechrecognition pyttsx3 requests groq

# Note for Windows Users: If you run into PyAudio issues, install via:
pip install pyaudio

# 3. Set your API keys in your environment (recommended)
export GROQ_API_KEY="your-groq-api-key"
export NEWS_API_KEY="your-news-api-key"

# 4. Run the assistant from your terminal
python aiengine.py


Interaction Flow:
Say "Kalki" to trigger wake-word detection.
Once Kalki responds with "Ya", speak your command (e.g., "Open YouTube", "Tell me the news", or ask any question).

Future Enhancements:
Transition from hardcoded API keys to environment variable loading via python-dotenv.
Add object-oriented command registry for cleaner module extensions.
Implement system automation commands (e.g., volume control, opening local apps).
